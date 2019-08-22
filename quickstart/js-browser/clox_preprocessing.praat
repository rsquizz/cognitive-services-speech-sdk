#################################
#   CLOx Preprocessing Script   #
#           8/22/2019           #
#         Rob Squizzero         #
#################################

#This script takes a .wav file and formats it to work with CLOx automatic transcription
#Load in your sound file, select it, and run this script from the Praat Objects Window
#This converts the file to mono and resamples it
#It then segments the file into 9.5-minute (570-second) chunks
#This script does not work on "long sound" files - sound files must be opened using "read from file"

beginPause: "Choose a directory to save the files in"
endPause: "OK", 1
dirName$ = chooseDirectory$ ("Choose a directory to save the files in")
if dirName$ = ""
	exit
endif

name$ = selected$("Sound")
Convert to mono
Resample: 16000, 50
sound = selected ("Sound")
segmentStart = 0
totalDuration = Get total duration
while segmentStart < totalDuration 
	if (segmentStart + 570) > totalDuration
		segmentEnd = totalDuration
	else
		segmentEnd = segmentStart + 570
	endif
	Extract part: segmentStart, segmentEnd, "rectangular", 1, "no"
	newName$ = name$ + "_" + string$(segmentStart * 1000)
	Save as WAV file... 'dirName$'/'newName$'.wav
	segmentStart += 570
	selectObject: sound
endwhile