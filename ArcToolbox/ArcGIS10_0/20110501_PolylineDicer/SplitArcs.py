#SplitArcs.py
#
#The purpose of this script is to split the features in a polyline featureclass into seperate records,
#each with a maximum, user-defined length.
#
#The output is a new feature class
#
# http://www.maprantala.com/2011/05/01/quick-dirty-arcpy-batch-splitting-polylines-to-a-specific-length/

import arcpy
import sys, math

def printit(inMessage):
    print inMessage
    arcpy.AddMessage(inMessage)

if len(sys.argv) > 1:
    inFC = sys.argv[1]
    outFC = sys.argv[2]
    alongDistin = sys.argv[3]
    alongDist = float(alongDistin)
else:
    inFC = "C:/temp/asdfasdf.mdb/jkl"
    OutDir = "C:/temp/asdfasdf.mdb"
    outFCName = "jkl2d"
    outFC = OutDir+"/"+outFCName
    alongDist = 1000

if (arcpy.Exists(inFC)):
    print(inFC+" does exist")
else:
    print("Cancelling, "+inFC+" does not exist")
    sys.exit(0)

def distPoint(p1, p2):
    calc1 = p1.X - p2.X
    calc2 = p1.Y - p2.Y

    return math.sqrt((calc1**2)+(calc2**2))

def midpoint(prevpoint,nextpoint,targetDist,totalDist):
    newX = prevpoint.X + ((nextpoint.X - prevpoint.X) * (targetDist/totalDist))
    newY = prevpoint.Y + ((nextpoint.Y - prevpoint.Y) * (targetDist/totalDist))
    return arcpy.Point(newX, newY)

def splitShape(feat,splitDist):
    # Count the number of points in the current multipart feature
    #
    partcount = feat.partCount
    partnum = 0
    # Enter while loop for each part in the feature (if a singlepart feature
    # this will occur only once)
    #
    lineArray = arcpy.Array()

    while partnum < partcount:
        # Print the part number
        #
        #print "Part " + str(partnum) + ":"
        part = feat.getPart(partnum)
        #print part.count

        totalDist = 0

        pnt = part.next()
        pntcount = 0


        prevpoint = None
        shapelist = []

        # Enter while loop for each vertex
        #
        while pnt:

            if not (prevpoint is None):
                thisDist = distPoint(prevpoint,pnt)
                maxAdditionalDist = splitDist - totalDist

                print thisDist, totalDist, maxAdditionalDist

                if (totalDist+thisDist)> splitDist:
                    while(totalDist+thisDist) > splitDist:
                        maxAdditionalDist = splitDist - totalDist
                        #print thisDist, totalDist, maxAdditionalDist
                        newpoint = midpoint(prevpoint,pnt,maxAdditionalDist,thisDist)
                        lineArray.add(newpoint)
                        shapelist.append(lineArray)

                        lineArray = arcpy.Array()
                        lineArray.add(newpoint)
                        prevpoint = newpoint
                        thisDist = distPoint(prevpoint,pnt)
                        totalDist = 0

                    lineArray.add(pnt)
                    totalDist+=thisDist
                else:
                    totalDist+=thisDist
                    lineArray.add(pnt)
                    #shapelist.append(lineArray)
            else:
                lineArray.add(pnt)
                totalDist = 0

            prevpoint = pnt
            pntcount += 1

            pnt = part.next()

            # If pnt is null, either the part is finished or there is an
            #   interior ring
            #
            if not pnt:
                pnt = part.next()
                if pnt:
                    print "Interior Ring:"
        partnum += 1

    if (lineArray.count > 1):
        shapelist.append(lineArray)

    return shapelist

if arcpy.Exists(outFC):
    arcpy.Delete_management(outFC)

arcpy.Copy_management(inFC,outFC)

#origDesc = arcpy.Describe(inFC)
#sR = origDesc.spatialReference

#revDesc = arcpy.Describe(outFC)
#revDesc.ShapeFieldName

deleterows = arcpy.UpdateCursor(outFC)
for iDRow in deleterows:
     deleterows.deleteRow(iDRow)

del iDRow
del deleterows

inputRows = arcpy.SearchCursor(inFC)
outputRows = arcpy.InsertCursor(outFC)
fields = arcpy.ListFields(inFC)

numRecords = int(arcpy.GetCount_management(inFC).getOutput(0))
OnePercentThreshold = numRecords // 100

printit(numRecords)

iCounter = 0
iCounter2 = 0

for iInRow in inputRows:
    inGeom = iInRow.shape
    iCounter+=1
    iCounter2+=1
    if (iCounter2 > (OnePercentThreshold+0)):
        printit("Processing Record "+str(iCounter) + " of "+ str(numRecords))
        iCounter2=0

    if (inGeom.length > alongDist):
        shapeList = splitShape(iInRow.shape,alongDist)

        for itmp in shapeList:
            newRow = outputRows.newRow()
            for ifield in fields:
                if (ifield.editable):
                    newRow.setValue(ifield.name,iInRow.getValue(ifield.name))
            newRow.shape = itmp
            outputRows.insertRow(newRow)
    else:
        outputRows.insertRow(iInRow)

del inputRows
del outputRows

printit("Done!")
