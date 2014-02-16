import Project_Reclassify

mConversion = "3.28084"
mProjection = "PROJCS['NAD_1983_UTM_Zone_15N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-93.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]"
mCellSize = "10"

#Project_Reclassify.Process("C:\mgs\Projects\NED_10m\n44w092\grdn44w092_13", mProjection, mConversion,"C:\mgs\Projects\NED_10m\n44w092\try30",mCellSize)

def CallIt (inDir,inGrid,outGrid):
fullinFN = inDir+'\'+inGrid
fulloutFN = 'C:\mgs\Projects\NED_10m\Output\'+outGrid
tmpGridFN = 'c:\temp\t'+outGrid
Project_Reclassify.Process(fullinFN, mProjection, mConversion,fulloutFN,mCellSize,tmpGridFN)

def CallIt2 (inGrd,inoutGrd):
outDir = 'C:\mgs\Projects\NED_10m\' + inGrd + '\' + inGrd

outGrd = 'grd'+inGrd+'_13'

CallIt(outDir,outGrd,inoutGrd)

#CallIt2("n44w092","LaCrosse_W")
CallIt2("n44w093","MasonCity_E")
CallIt2("n44w094","MasonCity_W")
CallIt2("n44w095","Fairmont_E")
CallIt2("n44w096","Fairmont_W")
CallIt2("n44w097","SiouxFalls_E")
#CallIt2("n45w092","EauClaire_W")
CallIt2("n45w093","StPaul_E")
CallIt2("n45w094","StPaul_W")
CallIt2("n45w095","NewUlm_E")
CallIt2("n45w096","NewUlm_W")
CallIt2("n45w097","Watertown_E")
#CallIt2("n46w093","Stillwater_E")
#CallIt2("n46w094","Stillwater_W")
#CallIt2("n46w095","StCloud_E")
CallIt2("n46w096","StCloud_W")
CallIt2("n46w097","Milbank_E")
#CallIt2("n47w092","Ashland_W")
#CallIt2("n47w093","Duluth_E")
CallIt2("n47w094","Duluth_W")
CallIt2("n47w095","Brainerd_E")
CallIt2("n47w096","Brainerd_W")
CallIt2("n47w097","Fargo_E")
#CallIt2("n48w090","Hancock_W")
#CallIt2("n48w091","TwoHarbors_E")
#CallIt2("n48w092","TwoHarbors_W")
#CallIt2("n48w093","Hibbing_E")
#CallIt2("n48w094","Hibbing_W")
CallIt2("n48w095","Bemidji_E")
CallIt2("n48w096","Bemidji_W")
CallIt2("n48w097","GrandForks_E")
#CallIt2("n48w098","GrandForks_W")
#CallIt2("n49w090","ThunderBay_W")
#CallIt2("n49w091","Quetico_E")
#CallIt2("n49w092","Quetico_W")
#CallIt2("n49w093","InternationFalls_E")
#CallIt2("n49w094","InternationFalls_W")
CallIt2("n49w095","Roseau_E")
CallIt2("n49w096","Roseau_W")
#CallIt2("n49w097","ThiefRiverFalls_E")
CallIt2("n49w098","ThiefRiverFalls_W")
#CallIt2("n50w095","Kenora_E")
#CallIt2("n50w096","Kenora_W")