#tester.py
#
#This code was used to figure out why a Windows scheduled task was not working.
#The python script ran fine when logged in but would not run when run as a Task Scheduler
#Task.
#
# This script calls any other python scripts in the same directory that start with test_
# and do NOT have a corresponding .start file.  If it finds test_run.py in the directory
# it runs it if there is NOT a test-run.start file.
#
# This script continues to run until it finds tester.stop in the same directory.
#
# This was useful because I launched this script from a Scheduled task on the local machine and logged out.
#
# I then used a remote machine to edit the script I was having trouble with. I would save changes, delete
#the corresponding .start file and within a minute (I have a 60 second sleep inthe loop) my new script would be launched.
# This saved me the hassle of making edits, logging into the machine, scheduling the task, and logging out to replicate the
# environment.
#
# This isn't something you probably want to run on a continual basis but using it during the debug process
# was very helpful for me.
#
# http://www.maprantala.com/2011/07/11/debugging-a-python-scheduled-task/

import sys, string, os
import glob
import datetime, shutil
import time, inspect
import getpass

totalstarttime = datetime.datetime.now()

dateString = datetime.date.today().strftime("%Y%m%d_")+datetime.datetime.now().strftime("%H%M%S") #datetime.date.today().strftime("%Y%m%d")
debugfile = inspect.getfile(inspect.currentframe()).replace(".py","_"+dateString+"_Debug.txt")
stopfile = inspect.getfile(inspect.currentframe()).replace(".py",".stop")
newdebugfile = False

codeDir = os.path.dirname(inspect.getfile(inspect.currentframe())).replace("\\","/")

def printit(inText):
    global newdebugfile

    print inText

    if os.path.exists(debugfile):
        if (newdebugfile == False):
            tmpfile = open(debugfile,"w")
            newdebugfile = True
        else:
            tmpfile = open(debugfile,"a")
    else:
        tmpfile = open(debugfile,"w")

    tmpfile.write(inText)
    tmpfile.write("\n")
    tmpfile.close()
    newdebugfile = True

stopFileExists = False
printit("Code Directory: "+codeDir)
printit("Starting at: "+datetime.date.today().strftime("%Y-%m-%d_")+datetime.datetime.now().strftime("%H:%M:%S"))
printit("Stopfile : "+stopfile+"/n")
while (stopFileExists == False):
    for iFile in glob.glob(codeDir+"/test_*.py"):

        thisStartfile = iFile.replace(".py",".start")

        if not (os.path.exists(thisStartfile)):
            printit ("Launching: "+iFile)
            iTmpfile = open(thisStartfile,"w")
            iTmpfile.write("started")
            iTmpfile.close()
            os.system("Start "+iFile)

    if (os.path.exists(stopfile)):
        stopFileExists = True
    else:
        time.sleep(60)

    printit("\nEnd of Loop: "+datetime.date.today().strftime("%Y-%m-%d_")+datetime.datetime.now().strftime("%H:%M:%S")+"\n")

printit("Done!")
