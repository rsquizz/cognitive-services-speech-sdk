#################################
#   CLOx Preprocessing Script   #
#           8/21/2019           #
#         Rob Squizzero         #
#################################

#This script takes a .wav file and formats it to work with CLOx automatic transcription
#Load in your sound file, select it, and run this script from the Praat Objects Window
#This converts the file to mono and resamples it
#This script does not work on "long sound files" - sound files must be opened using "read from file"

beginPause: "Choose a directory to save the file in"
endPause: "OK", 1
dirName$ = chooseDirectory$ ("Choose a directory to save the file in")
if dirName$ = ""
	exit
endif

name$ = selected$("Sound")
Convert to mono
Resample: 16000, 50
sound = selected ("Sound")
startTime = Get start time
newName$ = name$ + "_" + string$(startTime * 1000)
Save as WAV file... 'dirName$'/'newName$'.wav
