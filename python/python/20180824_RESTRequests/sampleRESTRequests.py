import requests, urllib, httplib, urllib2, json

serverURL = 'https://sampleserver6.arcgisonline.com/arcgis/'
tokenURL =  serverURL+"tokens/"
phaseQueryURL = serverURL+"rest/services/Census/MapServer/3/query"

#Fields to be aware of:
# PhaseName = Name of the phase, a unique value.
# Status_Date = Date a phase was marked as "Live"
# PhaseStatus = Live, Provisioning, Pending

def makeRequest(inURL,inPayload):
    theRequest = urllib2.Request(url=inURL,data = urllib.urlencode(inPayload))
    theResponse = urllib2.urlopen(theRequest)
    responseString = theResponse.read()
    theJSON = json.loads(responseString)
    return theJSON

def getToken(inUser,inPass):
    inputData = {'username':inUser,'password':inPass, 'f':'json'}
    theJSON = makeRequest(tokenURL,inputData)
    print(theJSON)
    token = theJSON['token']
    return token

def queryAllStates(inToken):
    inputData = { 'where': "1=1", 'f': 'geojson', 'outFields': '*' , 'outSR': 4326, 'token':inToken}
    theJSON = makeRequest(phaseQueryURL,inputData)
    return theJSON

def queryState(inPhase,inToken):
    inputData = { 'where': "STATE_NAME = '{}'".format(inPhase), 'f': 'geojson', 'outFields': '*' , 'outSR': 4326, 'token':inToken}
    theJSON = makeRequest(phaseQueryURL,inputData)
    return theJSON

def findStateForPoint(inX,inY,inToken):
    inputData = {'geometry': { 'x': inX, 'y': inY}, 'geometryType': 'esriGeometryPoint', 'inSR':4326, 'spatialRel':'esriSpatialRelIntersects', 'outFields':'*', 'f': 'json','token':inToken}

    theJSON = makeRequest(phaseQueryURL,inputData)
    return theJSON

username = ""
password = ""

##theToken = getToken(username,password)
theToken = ""
print(theToken)

#Attribute Query to get information about one State
stateInfo = queryState('Wisconsin',theToken)
print(stateInfo)

#Attribute Query to get information about all States
statesInfo = queryAllStates(theToken)
print(statesInfo)


#Find phase for a lat-lon
theState = findStateForPoint(-93.280842,44.95531,theToken)
print(theState)


