#http://www.maprantala.com/2011/03/14/failed-to-delete-domain-from-dataset-the-domain-is-used-as-default-domain/

import arcpy

min_workspace = r"C:\Users\mranter\AppData\Roaming\ESRI\Desktop10.0\ArcCatalog\min.minstaff.sde"

infgdb=(min_workspace)
arcpy.env.workspace = infgdb

def listfc(inDataset):
   featureclasses = arcpy.ListFeatureClasses("","",inDataset)
   for f in featureclasses:
      print "feature class: ",f

lfields=arcpy.ListFields(f)

for lf in lfields:
   if lf.domain < "":
      print "      domain",f, lf.name, lf.domain

def listds():
   listfc("")
   
   datasets=arcpy.ListDatasets ("","")
   for d in datasets:
      print "  dataset: ",d

listfc(d)
listds()