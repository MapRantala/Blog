'''
# ZipShapefile.py
#
# This script shows how a shapefile
# can be zipped by using python.
#
# It is set up to be used as an ArcGIS
#
# Peace
#
# 12/10/2010
# Matthew Rantala
# MapRantala@Gmail.com
# https://MapRantala.com
'''

import zipfile
import sys
import os
import glob

theShapeFile = sys.argv[1]
wellsZipFile = sys.argv[2]

def zipShapefile(inShapefile, newZipFN):
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
        zipobj.write(infile,os.path.basename(infile),zipfile.ZIP_DEFLATED)

    zipobj.close()

    return True

zipShapefile(theShapeFile,wellsZipFile)
print "done!"