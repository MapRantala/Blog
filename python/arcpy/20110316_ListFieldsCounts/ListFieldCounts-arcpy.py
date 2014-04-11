# Name: ListFields-arcpy.py
#
# Purpose: Lists the fields, their type, width, and precision
#          Can either have it export it to a CSV file or copy
#          and paste from the results window.
#
#          To use, create a tool from the script and add 3 parameters:
#             1) Table, Input, Required
#             2) Boolean, Input, Required (controls whether or not domains are exported)
#             3) Boolean, Input, Rekquired (controls whether or not you want to get the number of
#                Populated records.  (Your defintion of populated may vary from my code)
#             4) File, Output, Optional (optional output file to write)
#
# http://www.maprantala.com/2011/03/17/quick-dirty-field-listings-using-arcpy/

import arcpy,sys,os

def printit(inMessage):
    print inMessage
    arcpy.AddMessage(inMessage)

if len(sys.argv) > 4:
    featureclass = sys.argv[1]
    includedomainstring = sys.argv[2]
    doCountsRespone = sys.argv[3]
    outputFile = sys.argv[4]
else:
    featureclass = "C:/temp/before.shp"
    includedomainstring = "false"
    doCountsRespone = "true"
    outputFile = "C:/temp/before.csv"

if (outputFile == "#"):
    doOutputFile = False
else:
    doOutputFile = True

if (str(doCountsRespone).lower() == "true"):
    doCounts = True
else:
    doCounts = False

if (str(includedomainstring).lower() == "true"):
    includedomain = True
else:
    includedomain = False

lfields=arcpy.ListFields(featureclass)

d = arcpy.Describe(featureclass)
printit("Dataset: "+d.baseName)
printit("Type: "+d.dataType)
printit("Path: "+d.catalogPath)
printit(" ")

tableheaders = 'name,type,width,precision'

if (doCounts == True):
    tableheaders+=",count"

if (includedomain == True):
    tableheaders+=",domain"

if (doOutputFile):
    tmpfile = open(outputFile,"w")
    tmpfile.write(tableheaders)
    tmpfile.write("\n")

printit (tableheaders)
for lf in lfields:

    pThisline = lf.name+","+lf.type +","+str(lf.length)+","+str(lf.precision)

    if (doCounts == True):

        rowCount = 0

        #Note that I do not account for all field types
        #Also note that my defition of being populated may vary from yours.
        #I am using -999 as a flag to indicate a field type was not successfully
        #identified.
        if (lf.type == "Double") or (lf.type == "Single")  or (lf.type == "Integer") or (lf.type == "SmallInteger"):
            queryString = '"'+lf.name + '" > 0'
            rows = arcpy.SearchCursor(featureclass, queryString, "", "", "")
        elif (lf.type == "String"):
            queryString = '"'+lf.name + '" <> ' + "''"
            rows = arcpy.SearchCursor(featureclass, queryString, "", "", "")
        else:
            rowCount = -999
            #rows = arcpy.SearchCursor(featureclass, "", "", "", "")

        if (rowCount == 0):
            for row in rows:
                rowCount+=1

        pThisline=pThisline+","+str(rowCount)

    if (includedomain == True):
        pThisline=pThisline+","+lf.domain

    printit (pThisline)

    if (doOutputFile):
        tmpfile.write(pThisline)
        tmpfile.write("\n")

if (doOutputFile):
    tmpfile.close
