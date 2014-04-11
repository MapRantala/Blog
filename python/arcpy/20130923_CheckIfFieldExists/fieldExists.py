# Check to see if a field exists in a feature class
#
# http://www.maprantala.com/2013/09/23/arcpy-check-if-a-field-exists/

def fieldExists(inFeatureClass, inFieldName):
   fieldList = arcpy.ListFields(inFeatureClass)
   for iField in fieldList:
      if iField.name.lower() == inFieldName.lower():
         return True
   return False