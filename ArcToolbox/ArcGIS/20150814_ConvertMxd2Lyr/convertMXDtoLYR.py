###################################################
## convertMXDtoLyr.py
##
## The purpose of this script is to convert an MXD
## to a layer file. It groups all the layers in the
## first dataframe of the MXD into one group and
## saves that as a .lyr file.
##
## Thanks to Petr Krebs for the info on using a
## .lyr file with an empty layer
## http://gis.stackexchange.com/questions/4681/adding-new-group-layer-with-arcpy
##
## Matt Rantala, matt@maprantala.com
## http://www.WSBENG.com
##
##
##################################################

import os
import arcpy
import inspect
import glob
import uuid
import inspect

codeDir = os.path.dirname(inspect.getfile(inspect.currentframe()))
EmptyGroupLayerFile = codeDir+"/EmptyGroup.lyr"
inArg1 = sys.argv[1]
inArg2 = sys.argv[2]

def printit(inMessage):
    arcpy.AddMessage(inMessage)

def makeLyrFromMXD(inMXD, outLyr):
    if not (os.path.exists(inMXD)):
        printit( "ERROR: {} does not exist".format(inMXD))
        return False
    if not (os.path.exists(EmptyGroupLayerFile)):
        printit( "ERROR: {} does not exist".format(EmptyGroupLayerFile))
        return False
    if  (os.path.exists(outLyr)):
        printit( "Skipping: {} already exists".format(outLyr))
        return True

    printit( "Making Layer file: {0}".format(outLyr))

    mxd = arcpy.mapping.MapDocument(inMXD)
    ###Right now, just doing the first Dataframe, this could be modified
    df = arcpy.mapping.ListDataFrames(mxd)[0]

    theUUID = str(uuid.uuid1())

    iGroupLayerRaw = arcpy.mapping.Layer(EmptyGroupLayerFile)
    iGroupLayerRaw.name = theUUID
    arcpy.mapping.AddLayer(df,iGroupLayerRaw,"TOP")
    groupBaseName = os.path.basename(outLyr).split(".")[0]

    for lyr in arcpy.mapping.ListLayers(df):
        if not (lyr.name == theUUID):
            if (lyr.isGroupLayer):
                print "Adding Group: "+lyr.name
                arcpy.mapping.AddLayerToGroup (df, iGroupLayer, lyr, "Bottom")
            elif (lyr.longName == lyr.name):
                arcpy.mapping.AddLayerToGroup (df, iGroupLayer, lyr, "Bottom")
        else:
            iGroupLayer = lyr

    iGroupLayer.name = groupBaseName
    arcpy.SaveToLayerFile_management(iGroupLayer, outLyr)
    return os.path.exists(outLyr)

def doMultiple(inDir,outDir):
    for iMxd in glob.glob(inDir+"/*.mxd"):
        lyrFile = outDir+"/"+os.path.basename(iMxd).lower().replace(".mxd",".lyr")
        makeLyrFromMXD(iMxd, lyrFile)

if(not os.path.exists(EmptyGroupLayerFile)):
    printit("Error: {} is missing, can not run.".format(EmptyGroupLayerFile))
else:
    if (os.path.isdir(inArg1) and (os.path.isdir(inArg2))):
        doMultiple(inArg1,inArg2)
    elif (os.path.isfile(inArg1)):
        if (os.path.exists(inArg2)):
            printit("Error: {} already exists".format(inArg2))
        else:
            makeLyrFromMXD(inArg1,inArg2)
    else:
        printit("Unable to understand input parameters")
