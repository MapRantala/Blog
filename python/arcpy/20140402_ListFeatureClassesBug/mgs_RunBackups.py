# http://www.maprantala.com/2014/04/02/arcpy-listfeatureclasses-bug/

import arcpy

testGDBname = "mgs_sandbox.sde"
arcpy.env.workspace = testGDBname

def copyAll():
    for iFeatureClass in arcpy.ListFeatureClasses():
        print(" Feature Class: {0}".format(iFeatureClass))
    iFeatureClassFull = None

copyAll()
for iFD in arcpy.ListDatasets("","Feature"):
    print("Feature Dataset {0}:".format(iFD))
    arcpy.env.workspace = testGDBname+"/"+str(iFD)
    copyAll()
