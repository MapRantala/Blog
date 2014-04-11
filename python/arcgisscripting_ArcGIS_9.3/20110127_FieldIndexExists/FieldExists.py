# http://www.maprantala.com/2011/01/27/checking-to-see-if-a-field-index-exists-using-python/
# An example to check if a field index exists

import arcgisscripting

gp = arcgisscripting.create(9.3)

def indexExists(tablename,indexname):
 if not gp.Exists(tablename):
  return False

 indexList = gp.listindexes(tablename)

 for iIndex in indexList:
  if (iIndex.Name == indexname):
   return True

 return False