# -*- coding: cp1252 -*-
# Name: ListFields_compareFields.py
#
# Purpose: Compares the fieldsd in two feature classes and reports differences found
#
# http://www.maprantala.com/2014/07/07/quick-dirty-arcpy-compare-feature-class-table-schemas

import arcpy,sys,os

def printit(inMessage):
    print inMessage
    arcpy.AddMessage(inMessage)

featureclass1 = sys.argv[1]
featureclass2 = sys.argv[2]

tableheaders = 'name, type, width, precision, domain'

def makeFieldDict(inFC):
    d = arcpy.Describe(inFC)
    printit("Dataset: "+d.baseName)
    printit("Type: "+d.dataType)
    printit("Path: "+d.catalogPath)
    printit(" ")

    lFields=arcpy.ListFields(inFC)

    printit (tableheaders)
    fieldDict = dict()
    printit (lFields)
    for lf in lFields:
        fieldDict[lf.name] = [lf.name,lf.type,lf.length,lf.precision,lf.domain]
        printit (lf.name+", "+lf.type +", "+str(lf.length)+", "+str(lf.precision)+", "+lf.domain)
    return fieldDict

fieldDict1 = makeFieldDict(featureclass1)
fieldDict2 = makeFieldDict(featureclass2)
errorList = []
printit(" ")
printit(" ")
printit("Comparing Fields:")
for iField in sorted(list(set(fieldDict1.keys()+fieldDict2.keys()))):
    if not (fieldDict1.has_key(iField)):
        theResult = " {0} not found in {1}".format(iField,featureclass1)
        errorList.append(theResult)
    elif not (fieldDict2.has_key(iField)):
        theResult = " {0} not found in {1}".format(iField,featureclass2)
        errorList.append(theResult)
    else:
        if (fieldDict1[iField] == fieldDict2[iField]):
            theResult = " {0} OK".format(iField)
        else:
            theResult = " {0} Have Different Definitions \n   {1}: {2}\n   {3}: {4}".format(iField,featureclass1,fieldDict1[iField],featureclass2,fieldDict2[iField])
            errorList.append(theResult)

    printit( theResult )

printit(" ")
printit(" ")
if len(errorList) == 0:
    printit("GOOD! No difference Found!")
else:
    printit("These Differences Found:")
    for iError in errorList:
        printit(iError)

printit("Done!")








