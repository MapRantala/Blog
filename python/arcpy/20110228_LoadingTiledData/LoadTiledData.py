# Simple script to copy a series of rasters with the same name into the same
# workspace. Each raster gets renamed with the name of the directory it is currently
# in.
#
# To use I set up a Toolbox tool, launch in batch mode, then using Windows
# Explorer, I select & drag a batch of images into the Tool.
#
# http://www.maprantala.com/2011/02/28/loading-tiled-same-name-data-in-batch-mode/

import arcpy
import os, sys

inRaster = sys.argv[1]
basedir = os.path.basename(os.path.dirname(inRaster)).lower()
outRaster = "Database Connections/mgs_lidar.lidar.sde/mgs_lidar.lidar."+basedir

def printit(inMessage):
    print inMessage
    arcpy.AddMessage(inMessage)

if not (arcpy.Exists(outRaster)):
    printit ("Importing: "+basedir)
    arcpy.CopyRaster_management(inRaster,outRaster,"#","#","#","NONE","NONE","#")
else:
    printit ("Skipping: "+basedir+" because it already exists!")