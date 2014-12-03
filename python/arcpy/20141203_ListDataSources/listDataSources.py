# http://www.maprantala.com/

import arcpy, glob,os

theDir = r"L:\gdrs\data\org\us_mn_state_dnr\elev_minnesota_lidar\\"
os.chdir(theDir)

for iFile in glob.glob("*.lyr"):
    print iFile
    lyr = arcpy.mapping.Layer(iFile)
    for i in arcpy.mapping.ListLayers(lyr):
        try:
            print "    {0}: {1}".format(i,i.dataSource)
        except:
            print "    {0}: Does not support dataSource".format(i)

print "Done!"

