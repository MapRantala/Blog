#http://MapRantala.com

gp = arcgisscripting.create()

#This will print both to the geoprocessing window or Python output window
def gpprint(inmessage):
 gp.addmessage(inmessage)
 print inmessage

# Code to do stuff&gt;

#Ok, I want to send a message:
gpprint('Hello, sailor!')