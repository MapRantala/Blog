'''
# ZipShapefile.py
#
# This script shows how a shapefile
# can be zipped by using python.
#
# It is set up to be used as an ArcGIS
#
# 12/10/2010
#
#
# Updated 5/5/2014 with the option to ignore .lock files. This can be a bit
# dangerous because if the shapefile is being editted, unexpected results
#(including corrupting your shapefile) may occur.
#
# Matthew Rantala
# MapRantala@Gmail.com
# https://MapRantala.com
'''

import zipfile
import sys
import os
import glob

theShapeFile = sys.argv[1]
outputZipFile = sys.argv[2]
skipLockFile = sys.argv[3]

def zipShapefile(inShapefile, newZipFN, skipLockFile):
    print 'Starting to Zip '+inShapefile+' to '+newZipFN

    if not (os.path.exists(inShapefile)):
        print inShapefile + ' Does Not Exist'
        return False

    if (os.path.exists(newZipFN)):
        print 'Deleting '+newZipFN
        os.remove(newZipFN)

        if (os.path.exists(newZipFN)):
            print 'Unable to Delete'+newZipFN
            return False

    zipobj = zipfile.ZipFile(newZipFN,'w')

    for infile in glob.glob( inShapefile.lower().replace(".shp",".*")):
        print infile
        if not ((os.path.splitext(infile.lower())[1] == ".lock") and (skipLockFile.lower() == "true")):
            zipobj.write(infile,os.path.basename(infile),zipfile.ZIP_DEFLATED)

    zipobj.close()

    return True

zipShapefile(theShapeFile,outputZipFile,skipLockFile)
print "done!"