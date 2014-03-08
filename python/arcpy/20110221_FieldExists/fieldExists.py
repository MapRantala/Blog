#http://www.maprantala.com/2011/02/21/checking-to-see-if-a-field-index-exists-using-arcpy-argis-10-0/

import arcpy

def indexExists(tablename,indexname):

 if not arcpy.Exists(tablename):
  return False

 tabledescription = arcpy.Describe(tablename)

 for iIndex in tabledescription.indexes:
  if (iIndex.Name == indexname):
   return True

 return False