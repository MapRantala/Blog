#-------------------------------------------------------------------------------
# Name:        usi_dataprep_Add_STCONABR
#
# Purpose:     This can be used to add [CT_CON_ABR] to Hennepin County, MN
#              centerlines. This is a concatenated, abbreviated full name of
#              the street. This used to be included in the data but
#              disappeared from the downloads in the summer of 2017.
#
#              Data available at: http://www.hennepin.us/gisopendata
#
# Author:      mrantala
#
# Created:     2017.10.04
#
# Github:      https://github.umn.edu/MGS/mgs_PythonTemplate
#------------------------------------------------------------------------------

import arcpy

############################################
## Custom Variables
#These are the fields that are concatenated. Hennepin has others but were always blank.
requiredFieldList = ["ST_PRE_DIR","ST_PRE_TYP","ST_NAME","ST_POS_TYP","ST_POS_DIR"]
#This is the name of the field to add
newFieldName = "ST_CON_ABR"

#These are the abbreviations for [ST_POS_TYPE]. The list was created using a sample of
#Hennepin's centerline data & Esri Tech article: http://support.esri.com/en/technical-article/000008454
# Note that I intentionally left cases in where there is no abbreviation (Fall, for example) as a means of
#documenting the fact that it should NOT change.

abbList = []
abbList.append(["Alcove","Alcove"]) #Hennepin Specific
abbList.append(["Alley","Aly"])
abbList.append(["Annex","Anx"])
abbList.append(["Arcade","Arc"])
abbList.append(["Avenue","Ave"])
abbList.append(["Bay","Bay"]) #Hennepin Specific
abbList.append(["Bayoo","Byu"])
abbList.append(["Beach","Bch"])
abbList.append(["Bend","Bnd"])
abbList.append(["Bluff","Blf"])
abbList.append(["Bluffs","Blfs"])
abbList.append(["Bottom","Btm"])
abbList.append(["Boulevard","Blvd"])
abbList.append(["Branch","Br"])
abbList.append(["Bridge","Brg"])
abbList.append(["Brook","Brk"])
abbList.append(["Brooks","Brks"])
abbList.append(["Burg","Bg"])
abbList.append(["Burgs","Bgs"])
abbList.append(["Bypass","Byp"])
abbList.append(["Camp","Cp"])
abbList.append(["Canyon","Cyn"])
abbList.append(["Cape","Cpe"])
abbList.append(["Causeway","Cswy"])
abbList.append(["Center","Ctr"])
abbList.append(["Centers","Ctrs"])
abbList.append(["Crossings","Crossings"]) #Hennepin Specific
abbList.append(["Crossroad","Xrd"])
abbList.append(["Chase","Chase"]) #Hennepin Specific
abbList.append(["Circle","Cir"])
abbList.append(["Circles","Cirs"])
abbList.append(["Cliff","Clf"])
abbList.append(["Cliffs","Clfs"])
abbList.append(["Club","Clb"])
abbList.append(["Close","Close"]) #Hennepin Specific
abbList.append(["Common","Cmn"])
abbList.append(["Commons","Cmns"]) #Hennepin Specific
abbList.append(["Corner","Cor"])
abbList.append(["Corners","Cors"])
abbList.append(["Corridor","Corridor"]) #Hennepin Specific
abbList.append(["Course","Crse"])
abbList.append(["Court","Ct"])
abbList.append(["Courts","Cts"])
abbList.append(["Cove","Cv"])
abbList.append(["Coves","Cvs"])
abbList.append(["Creek","Crk"])
abbList.append(["Crescent","Cres"])
abbList.append(["Crest","Crst"])
abbList.append(["Cross","Cross"]) #Hennepin Specific
abbList.append(["Crossing","Xing"])
abbList.append(["Curve","Curve"])
abbList.append(["Dale","Dl"])
abbList.append(["Dam","Dm"])
abbList.append(["Divide","Dv"])
abbList.append(["Down","Down"]) #Hennepin Specific
abbList.append(["Downs","Downs"]) #Hennepin Specific
abbList.append(["Drive","Dr"])
abbList.append(["Drives","Drs"])
abbList.append(["Edge","Edge"]) #Hennepin Specific
abbList.append(["Entry","Entry"]) #Hennepin Specific
abbList.append(["Estate","Est"])
abbList.append(["Estates","Ests"])
abbList.append(["Expressway","Expy"])
abbList.append(["Extension","Ext"])
abbList.append(["Extensions","Exts"])
abbList.append(["Fall","Fall"])
abbList.append(["Falls","Fls"])
abbList.append(["Ferry","Fry"])
abbList.append(["Field","Fld"])
abbList.append(["Fields","Flds"])
abbList.append(["Flat","Flt"])
abbList.append(["Flats","Flts"])
abbList.append(["Ford","Frd"])
abbList.append(["Fords","Frds"])
abbList.append(["Forest","Frst"])
abbList.append(["Forge","Frg"])
abbList.append(["Forges","Frgs"])
abbList.append(["Fork","Frk"])
abbList.append(["Forks","Frks"])
abbList.append(["Fort","Ft"])
abbList.append(["Freeway","Fwy"])
abbList.append(["Gables","Gables"]) #Hennepin Specific
abbList.append(["Garden","Gdn"])
abbList.append(["Gardens","Gdns"])
abbList.append(["Gate","Gate"]) #Hennepin Specific
abbList.append(["Gateway","Gtwy"])
abbList.append(["Glade","Glade"]) #Hennepin Specific
abbList.append(["Glen","Gln"])
abbList.append(["Glens","Glns"])
abbList.append(["Green","Grn"])
abbList.append(["Greens","Grns"])
abbList.append(["Greenway","Greenway"]) #Hennepin Specific
abbList.append(["Grove","Grv"])
abbList.append(["Groves","Grvs"])
abbList.append(["Harbor","Hbr"])
abbList.append(["Harbors","Hbrs"])
abbList.append(["Haven","Hvn"])
abbList.append(["Heights","Hts"])
abbList.append(["Highway","Hwy"])
abbList.append(["Hill","Hl"])
abbList.append(["Hills","Hls"])
abbList.append(["Hollow","Holw"])
abbList.append(["Horn","Horn"]) #Hennepin Specific
abbList.append(["Inlet","Inlt"])
abbList.append(["Island","Is"])
abbList.append(["Islands","Iss"])
abbList.append(["Isle","Isle"])
abbList.append(["Junction","Jct"])
abbList.append(["Junctions","Jcts"])
abbList.append(["Key","Ky"])
abbList.append(["Keys","Kys"])
abbList.append(["Knoll","Knl"])
abbList.append(["Knolls","Knls"])
abbList.append(["Lake","Lk"])
abbList.append(["Lakes","Lks"])
abbList.append(["Land","Land"])
abbList.append(["Landing","Lndg"])
abbList.append(["Lane","Ln"])
abbList.append(["Light","Lgt"])
abbList.append(["Lights","Lgts"])
abbList.append(["Loaf","Lf"])
abbList.append(["Lock","Lck"])
abbList.append(["Locks","Lcks"])
abbList.append(["Lodge","Ldg"])
abbList.append(["Loop","Loop"])
abbList.append(["Mall","Mall"])
abbList.append(["Manor","Mnr"])
abbList.append(["Manors","Mnrs"])
abbList.append(["Meadow","Mdw"])
abbList.append(["Meadows","Mdws"])
abbList.append(["Mews","Mews"])
abbList.append(["Mill","Ml"])
abbList.append(["Mills","Mls"])
abbList.append(["Mission","Msn"])
abbList.append(["Motorway","Mtwy"])
abbList.append(["Mount","Mt"])
abbList.append(["Mountain","Mtn"])
abbList.append(["Mountains","Mtns"])
abbList.append(["Neck","Nck"])
abbList.append(["Orchard","Orch"])
abbList.append(["Oval","Oval"])
abbList.append(["Overpass","Opas"])
abbList.append(["Park","Park"])
abbList.append(["Parks","Park"])
abbList.append(["Parkway","Pkwy"])
abbList.append(["Parkways","Pkwy"])
abbList.append(["Pass","Pass"])
abbList.append(["Passage","Psge"])
abbList.append(["Path","Path"])
abbList.append(["Pike","Pike"])
abbList.append(["Pine","Pne"])
abbList.append(["Pines","Pnes"])
abbList.append(["Place","Pl"])
abbList.append(["Plain","Pln"])
abbList.append(["Plains","Plns"])
abbList.append(["Plaza","Plz"])
abbList.append(["Point","Pt"])
abbList.append(["Points","Pts"])
abbList.append(["Port","Prt"])
abbList.append(["Ports","Prts"])
abbList.append(["Prairie","Pr"])
abbList.append(["Radial","Radl"])
abbList.append(["Railroad","Railroad"]) #Hennepin Specific
abbList.append(["Ramp","Ramp"])
abbList.append(["Ranch","Rnch"])
abbList.append(["Rapid","Rpd"])
abbList.append(["Rapids","Rpds"])
abbList.append(["Rest","Rst"])
abbList.append(["Ridge","Rdg"])
abbList.append(["Ridges","Rdgs"])
abbList.append(["Rise","Rise"]) #Hennepin Specific
abbList.append(["River","Riv"])
abbList.append(["Road","Rd"])
abbList.append(["Roads","Rds"])
abbList.append(["Route","Rte"])
abbList.append(["Row","Row"])
abbList.append(["Rue","Rue"])
abbList.append(["Run","Run"])
abbList.append(["Shoal","Shl"])
abbList.append(["Shoals","Shls"])
abbList.append(["Shore","Shr"])
abbList.append(["Shores","Shrs"])
abbList.append(["Skies","Skies"]) #Hennepin Specific
abbList.append(["Skyway","Skwy"])
abbList.append(["Spring","Spg"])
abbList.append(["Springs","Spgs"])
abbList.append(["Spur","Spur"])
abbList.append(["Spurs","Spur"])
abbList.append(["Square","Sq"])
abbList.append(["Squares","Sqrs"])
abbList.append(["Station","Sta"])
abbList.append(["Stravenue","Stra"])
abbList.append(["Stream","Strm"])
abbList.append(["Street","St"])
abbList.append(["Streets","Sts"])
abbList.append(["Summit","Smt"])
abbList.append(["Terrace","Ter"])
abbList.append(["Throughway","Trwy"])
abbList.append(["Trace","Trce"])
abbList.append(["Track","Trak"])
abbList.append(["Trafficway","Trfy"])
abbList.append(["Trail","Trl"])
abbList.append(["Tunnel","Tunl"])
abbList.append(["Turn","Turn"]) #Hennepin Specific
abbList.append(["Turnpike","Tpke"])
abbList.append(["Underpass","Upas"])
abbList.append(["Union","Un"])
abbList.append(["Unions","Uns"])
abbList.append(["Valley","Vly"])
abbList.append(["Valleys","Vlys"])
abbList.append(["Viaduct","Via"])
abbList.append(["View","Vw"])
abbList.append(["Views","Vws"])
abbList.append(["Village","Vlg"])
abbList.append(["Villages","Vlgs"])
abbList.append(["Ville","Vl"])
abbList.append(["Vista","Vis"])
abbList.append(["Walk","Walk"])
abbList.append(["Walks","Walk"])
abbList.append(["Wall","Wall"])
abbList.append(["Way","Way"])
abbList.append(["Ways","Ways"])
abbList.append(["Well","Wl"])
abbList.append(["Wells","Wls"])

#List of changes for [St_POS_Dir]
posDirList = [["North","N"],["East","E"],["South","S"],["West","W"],["Northeast","NE"],["Northwest","NW"],["Southeast","SE"],["Southwest","SW"]]
preDirList = [["North","N"],["East","E"],["South","S"],["West","W"]]
############################################
## Read Arguments

if (len(sys.argv) > 1):
    inFC = sys.argv[1]

############################################
# General Purpose Functions
def printit(inputString):
    try:
        print(inputString)
        arcpy.AddMessage(str(inputString))
    except:
        pass

def printerror(inputString):
    print (inputString)
    arcpy.AddError(inputString)

def getField(inFeatureClass, inFieldName):
  fieldList = arcpy.ListFields(inFeatureClass)
  for iField in fieldList:
    if iField.name.lower() == inFieldName.lower():
      return iField
  return None

def fieldExists(inFeatureClass, inFieldName):
  return getField(inFeatureClass,inFieldName) <> None

############################################
# Initial QC

def initialQC():
    if (arcpy.Exists(inFC)):
        printit("PASS: Feature Class {} Exists".format(inFC))
    else:
        printerror("ERROR: Feature Class {} Does Not Exist, Cancelling...".format(inFC))
        return False

    for iFld in requiredFieldList:
        if (fieldExists(inFC,iFld)):
            printit("PASS: Feature Class {} Has Field [{}]".format(inFC,iFld))
        else:
            printerror("ERROR: Feature Class {} Does Not Have Field [{}], Cancelling...".format(inFC,iFld))
            return False

    if not (fieldExists(inFC,newFieldName)):
        printit("GOOD: Feature Class {} Does Not Already Have Field [{}]".format(inFC,newFieldName))
        printit(" ADDING Field [{}]".format(newFieldName))
        try:
            arcpy.AddField_management(in_table=inFC, field_name=newFieldName, field_type="TEXT", field_precision="", field_scale="", field_length="100", field_alias="", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
        except:
            printerror("ERROR: Error While Adding Field [{}], Cancelling...".format(newFieldName))
            return False
        if not (fieldExists(inFC,newFieldName)):
            printerror("ERROR: Unable to Add Field [{}], Cancelling...".format(newFieldName))
            return False
    else:
        printerror("ERROR: Feature Class {} Already Has Field [{}], Cancelling...".format(inFC,newFieldName))
        return False

    return True

############################################
# Main

def makeSubstitution(inList,inValue,inFieldName):
    for iAbbreviationPr in inList:
        if (inValue == iAbbreviationPr[0]): #Found a Match
            return iAbbreviationPr[1]
    printit("WARNING: [{}] of {} does not have a value in the abbreviation list! Potential Error...".format(inFieldName,inValue))
    return inValue

def main():
    cursorFieldList = requiredFieldList
    cursorFieldList.append(newFieldName)

    try:
        iUCursor = arcpy.da.UpdateCursor(inFC,cursorFieldList)
        iRowCount = 0
        iRowMax = 1
        for uRow in iUCursor:

            #Just to give user an indicator that progress is being made
            if (iRowCount>iRowMax):
                printit(" {}".format(iRowCount))
                iRowMax *= 10
                iRowCount+=1

            abbreviateConcatenatedName = ""
            iFldIndex = 0
            for iFld in requiredFieldList:


                if (iFld == newFieldName):
                    uRow[iFldIndex] = abbreviateConcatenatedName
                    iUCursor.updateRow(uRow)
                else:
                    iValue = uRow[iFldIndex].strip() #Strip is just a safe-guard


                    if ((iValue != "") and (iValue != None)):
                        if (iFld == "ST_PRE_DIR"):
                            iValue= makeSubstitution(preDirList,iValue,"ST_PRE_DIR")
                        if (iFld == "ST_POS_TYP"):
                            iValue= makeSubstitution(abbList,iValue,"ST_POS_TYPE")
                        if (iFld == "ST_POS_DIR"):
                            iValue = makeSubstitution(posDirList,iValue,"ST_POS_DIR")

                        if (abbreviateConcatenatedName == ""):
                            abbreviateConcatenatedName = iValue
                        else:
                            abbreviateConcatenatedName+=" "+iValue
                iFldIndex += 1

        del iUCursor
    except RuntimeError as e:
        printerror("ERROR: Error {} Occurred, Cancelling...".format(e))
        try:
            del iUCursor
            del uRow
        except:
            return False
    return True


if __name__ == '__main__':
    if (initialQC() == True):
        if (main() == True):
            printit("Done!")

