import zipfile
import sys
import os
import glob
wellsShapeFile = "C:/cwi5_bk/WELLS/wells.SHP"
wellsZipFile = "C:/cwi5_bk/WELLS/test5.zip"

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

zipShapefile(wellsShapeFile,wellsZipFile)
print "done!"