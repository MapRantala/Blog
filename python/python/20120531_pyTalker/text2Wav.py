# This python script will take a text file and convert it to a .wav file
# uses Microsoft's Sppech API (SAPI).
# http://msdn.microsoft.com/en-us/library/ms723627%28v=vs.85%29
#
# http://www.maprantala.com/2012/05/31/quick-dirty-python-converting-a-text-file-to-audio-wav/

from comtypes.gen import CreateObject

engine = CreateObject("SAPI.SpVoice")
stream = CreateObject("SAPI.SpFileStream")

infile = "c:/temp/text.txt"
outfile = "c:/temp/text4.wav"
stream.Open(outfile, SpeechLib.SSFMCreateForWrite)
engine.AudioOutputStream = stream

f = open(infile, 'r')
theText = f.read()
f.close()

engine.speak(theText)

stream.Close()