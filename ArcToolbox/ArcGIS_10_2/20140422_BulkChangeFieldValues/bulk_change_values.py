#-------------------------------------------------------------------------------
# Name:        bluk_change_values
# Purpose:     Add a field to a feature class and set the value to the name
#              of the feature class.
#
# Author:      mjr
#
# Created:     4/22/2014
#
# Github:      http://MapRantala.com
#------------------------------------------------------------------------------

import arcpy
import sys, string, arcgisscripting
import arcpy

def printit(inString):
    print inString
    arcpy.AddMessage(inString)

def printerr(inString):
    print inString
    arcpy.AddError(inString)

def fieldExists(tablename,indexname):

 if not arcpy.Exists(tablename):
  return False

 tabledescription = arcpy.Describe(tablename)

 for iField in tabledescription.fields:
     if (iField.Name.lower() == indexname.lower()):
         return True

 return False


if len(sys.argv) > 1:
    inDirectory = sys.argv[1]
    inFieldNameRaw = sys.argv[2]
    oldValue = sys.argv[3].replace(","," ")
    newValue = sys.argv[4].replace(","," ")
    caseSensitiveRaw = sys.argv[5]
else:
    inDirectory = r"C:\temp\test\stratest"
    inFieldNameRaw = "strat"
    oldValue = "go, goc, sgb".replace(","," ")
    newValue = "gro grc grb".replace(","," ")
    caseSensitiveRaw = "true"

caseSensitive = (caseSensitiveRaw.lower() == "true")
fieldNameList = inFieldNameRaw.replace(","," ").split()

printit("Starting")
printit(" Workspace: "+str(inDirectory))
printit( " inFieldName: "+str(inFieldNameRaw))
printit( " oldValue: "+str(oldValue))
printit( " newValue: "+str(newValue))
printit( " caseSensitive: "+str(caseSensitive))

valueDict = dict()

def initialQC():
    global valueDict

    if not (arcpy.Exists(inDirectory)):
        printerr("Workspace {0} does not exist".format(inDirectory))
        return False

    if (len(oldValue.split()) <> len(newValue.split())):
        printerr("Number of values in {0} does not equal number of values in {1}".format(oldValue,newValue))
        return False

    iValueIndex = 0
    for iOldValue in oldValue.split():
        if (caseSensitive):
            thisKey = iOldValue
        else:
            thisKey = iOldValue.lower()

        if (valueDict.has_key(thisKey)):
            printerr("ERROR: Value, {0}, is repeated, cancelling...".format(thisKey))
            return False

        valueDict[thisKey] = newValue.split()[iValueIndex]
        iValueIndex+=1
    return True

def makeFieldList(inFC):
    thisFieldList = []

    for iField in fieldNameList:
        if (fieldExists(inFC,iField)):
            thisFieldList.append(iField)

    return thisFieldList


def main():
    arcpy.env.workspace = inDirectory
    printit(valueDict)
    for iFC in arcpy.ListFeatureClasses():
        printit("Working on {0}".format(iFC))

        iFieldList = makeFieldList(iFC)
        if (len(iFieldList) == 0):
            printit(" No fields to change, Skipping...")
            continue

        rows = arcpy.UpdateCursor(iFC)

        changes = 0
        printit(" Changing Rows")
        for row in rows:
            iChange = 0
            for iField in iFieldList:
                iValue = str(row.getValue(iField))
                newValue = iValue

                if valueDict.has_key(iValue):
                    newValue = valueDict[iValue]
                else:
                    if not (caseSensitive):
                        if valueDict.has_key(iValue.lower()):
                            newValue = valueDict[iValue.lower()]

                if (newValue <> iValue):
                    printit("CHANGE {0}".format(newValue))
                    row.setValue(iField,newValue)
                    iChange+=1

            if (iChange > 0):
                changes+=1
                rows.updateRow(row)
        printit("  Made {0} changes".format(changes))
        del row
        del rows

    printit("Main")

if (initialQC()==True):
    main()

printit("Done")

