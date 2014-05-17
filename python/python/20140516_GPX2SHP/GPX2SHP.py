import glob, os
import xml.etree.ElementTree as ET
import shapefile
import shutil

theNS = "{http://www.topografix.com/GPX/1/1}".lower()
theNS2 = "{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}".lower()
templatePRJfile = "template.prj"

def elementIs(inElement,inTag):
    item1 = inTag.lower()
    item2 = elementName(inElement)
    return (inTag.lower() == elementName(inElement).lower())

def elementName(inElement):
    item1= inElement.tag.lower().replace(theNS,"").replace(theNS2,"")
    return item1

def convertTimeToSeconds(inTime):
    theSeconds = -1

    if (inTime.count(":")) == 2:
        try:
            inHour = inTime.split(":")[0]
            inMin = inTime.split(":")[1]
            inSec = inTime.split(":")[2]

            totalSec = float(inSec)
            totalSec += (float(inMin) * 60)
            totalSec += (float(inHour) * 3600)
            theSeconds = totalSec
        except:
            pass

    return theSeconds


def writeSHP(inSourceFile,inTrkList):
    w = shapefile.Writer(shapefile.POINT)
    w.field("file")
    w.field("segment","N","8",0)
    w.field("vertex","N","8",0)
    w.field("datetime","C",30)
    w.field("date","C","10",0)
    w.field("time","C","8",0)
    w.field("sec","N","8",0)
    w.field("isec","N","8",0)
    w.field("totsec","N","8",0)
    w.field("elev","N","24",14)
    w.field("hr","N","8",0)
    w.field("last","N","1",0)
    w.field("lat","N","24",16)
    w.field("lon","N","24",16)

    iTrkSegIndex = 0
    startSec =-1
    prevSec = -1
    for iTrkSeg in inTrkList:
        iTrkPtIndex = 0
        for iTrkPtDict in iTrkSeg:
            thisLine = "{0},{1},{2},*time*,*ele*,*hr*,*lat*,*lon*".format(inSourceFile,iTrkSegIndex,iTrkPtIndex)

            theLat = None
            if (iTrkPtDict.has_key('lat')):
                try:
                    theLat = float(iTrkPtDict['lat'])
                except:
                    pass

            theLon = None

            if (iTrkPtDict.has_key('lon')):
                try:
                    theLon = float(iTrkPtDict['lon'])
                except:
                    pass

            theDate = None
            theTime = None
            theSeconds = -1
            segSeconds = -1
            totSeconds = -1

            if (iTrkPtDict.has_key('time')):
                theDateTime = iTrkPtDict['time']
                if ("T" in theDateTime):
                    theDate = theDateTime.split("T")[0]
                    theTimePlue = theDateTime.split("T")[1]
                    if ("+" in theTimePlue):
                        theTime = theTimePlue.split("+")[0]
                        theSeconds = convertTimeToSeconds(theTime)

                        if (prevSec < 0):
                            prevSec = theSeconds
                        if (startSec<0):
                            startSec = theSeconds

                        segSeconds = theSeconds - prevSec
                        prevSec = theSeconds
                        totSeconds = theSeconds - startSec
            else:
                theDateTime = None

            if (iTrkPtDict.has_key('ele')):
                theElev = iTrkPtDict['ele']
            else:
                theElev = None

            if (iTrkPtDict.has_key('hr')):
                theHR = iTrkPtDict['hr']
            else:
                theHR = None

            if (iTrkPtIndex == len(iTrkSeg) - 1):
                theLast = 1
            else:
                theLast = 0

            w.point(theLon, theLat)
            try:
                                  w.record(inSourceFile.replace(".gpx",""),iTrkSegIndex,iTrkPtIndex,theDateTime,theDate,theTime,theSeconds,segSeconds,totSeconds,theElev,theHR,theLast,theLat,theLon)

            except:
                print "############## ERROR ####################"
            iTrkPtIndex+=1

        iTrkSegIndex+=1


    w.save(inSourceFile.lower().replace(".gpx",""))
    w = None
    if (os.path.exists(templatePRJfile)):
        newPRJFN = inSourceFile.lower().replace(".gpx",".prj")
        shutil.copyfile(templatePRJfile,newPRJFN)

def mainLoop():
    for iFile in glob.glob("*.gpx"):
        print iFile
        tree = ET.parse(iFile)
        root=tree.getroot()

        theTrkList = []

        for iRoot in root:
            if elementIs(iRoot,"trk"): #"http://www.topografix.com/gpx/1/1}trk" in iRoot.tag.lower():
                for iTrkSeg in iRoot:
                    if not elementIs(iTrkSeg,"trkseg"):
                        continue
                    thisTrk = []

                    pntIndex = 0
                    for iTrkPt in iTrkSeg:
                        if not elementIs(iTrkPt,"trkpt"):
                            continue
                        trkPntDict = dict()
                        trkPntDict["pntIndex"] = pntIndex
                        trkPntDict['lat'] = iTrkPt.get('lat')
                        trkPntDict['lon'] = iTrkPt.get('lon')

                        pntIndex+=1
                        for iElem in iTrkPt:
                            if elementIs(iElem,"extensions"):
                                for iSubElem in iElem:
                                    if (elementIs(iSubElem,"TrackPointExtension")):
                                        for iExtensionElem in iSubElem:
                                            if elementIs(iExtensionElem,"hr"):
                                                trkPntDict[elementName(iExtensionElem)] = iExtensionElem.text
                            else:
                                trkPntDict[elementName(iElem)] = iElem.text

                        #print trkPntDict
                        thisTrk.append(trkPntDict)

                    theTrkList.append(thisTrk)
        writeSHP(iFile.lower(), theTrkList)


theLineList = mainLoop()
