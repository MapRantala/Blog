##################################################################
## Various scripts for working with ArcGIS domains. Right now, focus
## is on Coded Value Domains for feature Classes
##
## http://MapRantala.com
## https://github.com/MapRantala
##
## 12/18/2014
##
##
##

import arcpy

inFeatureClass = sys.argv[1]
inField = sys.argv[2]
inValue = sys.argv[3]

# getFeatureClassParentWorkspace: This script gets the geodatabase for a
# feature class. The trick here is that feature classes can be within a
# feature dataset so you need to account for two possible levels in the
# directory structure.
def getFeatureClassParentWorkspace(inFeatureClass):
    describeFC = arcpy.Describe(inFeatureClass)
    if (describeFC.dataType == 'FeatureClass') or (describeFC.dataType == 'Table'):
        workspace1 = describeFC.path
        describeWorkspace1 = arcpy.Describe(workspace1)
        if (describeWorkspace1.dataType == 'FeatureDataset'):
            return describeWorkspace1.path
        return workspace1

    return None

# Find a field within a feature class
def getField(inFeatureClass, inFieldName):
  fieldList = arcpy.ListFields(inFeatureClass)
  for iField in fieldList:
    if iField.name.lower() == inFieldName.lower():
      return iField
  return None

#Get a field's domain
def getDomain(inFeatureClass, inField):
    theField = getField(inFeatureClass,inField)
    if (theField <> None):
        searchDomainName = theField.domain
        if (searchDomainName <> ""):
            for iDomain in arcpy.da.ListDomains(getFeatureClassParentWorkspace(inFeatureClass)):
                if iDomain.name == searchDomainName:
                    return iDomain
    return None

#Get the domain.
def validDomainValue(inFeatureClass,inField,inValue):
    theDomain = getDomain(inFeatureClass,inField)

    if not (theDomain is None):
        if (theDomain.domainType == "CodedValue"):
            if theDomain.codedValues.has_key(inValue):
                return True
    return False

if (validDomainValue(inFeatureClass,inField,inValue)):
    arcpy.AddMessage("Value ({0}) is valid for field [{1}].".format(inValue,inField))
else:
    arcpy.AddError("ERROR: Value ({0}) is invalid for field [{1}].".format(inValue,inField))
