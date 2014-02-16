#http://MapRantala.com

import os.path
import datetime
import shutil
import sys

theEmailText = "nStart: " + str(datetime.datetime.now())

#This example shows three different ways for a script to receive input parameters.
#
# First, if it was run with the necessary number of parameters, as if launched by
# an ArcToolbox tool, it uses those parameters.

if len(sys.argv) == 2:
    wellsShapeFile = sys.argv[0]
    unwellsShapeFile = sys.argv[1]
    theEmailText = theEmailText + "nUsing Parameters Passed In:nn Located Wells File: "+wellsShapeFile+"n Unlocated Wells File: "+unwellsShapeFile
else:
    dateString = datetime.date.today().strftime("%Y%m%d")
    wellsShapeFile = "C:/cwi5_bk/wells/temp/wells_.shp"
    unwellsShapeFile = "C:/cwi5_bk/wells/temp/unloc_wells.shp"

    #Second attempt is if there are default values that should be used.
    #I use this for a process that is run via scheduled Windows Task
    if (os.path.exists(wellsShapeFile)) and (os.path.exists(unwellsShapeFile)):
        theEmailText = theEmailText + "nUsing Automated Date-Based file names:nn Located Wells File: "+wellsShapeFile+"n Unlocated Wells File: "+unwellsShapeFile
    else:
        #The third method is used for debugging/running in the IDE.
        #I put a check condition so this is valid for one day only
        #And then hard-code the temporary paths.
        #
        #Note that you may want to modify the structure of the IF statement
        #used for methods 2 & 3 so that it checks for the manual-override (3rd)
        #method first
        if dateString == '20101213':
            wellsShapeFile = "C:/cwi5_bk/wells/temp/wells.shp"
            unwellsShapeFile = "C:/cwi5_bk/wells/temp/unloc.shp"
            theEmailText = theEmailText + "nUsing Manual Override file names:nn Located Wells File: "+wellsShapeFile+"n Unlocated Wells File: "+unwellsShapeFile
        else:
            theEmailText = theEmailText + "n Manual Override for file names does not meet data filter"

    if (not os.path.exists(wellsShapeFile)) or (not os.path.exists(unwellsShapeFile)):
        from Tkinter import *
        msgbox = Tk()
        msgbox.title('Error')
        Message(msgbox,text="Must either use ArcTool to launch or edit file parameters", bg='royalblue',fg='ivory', relief=GROOVE).pack(padx=10, pady=10)
        msgbox.mainloop()
        print theEmailText
        quit()

print theEmailText