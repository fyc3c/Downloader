import sys
import os
from tools.youtube import  res360p
from tools.youtube import pyaudio

os.system("clear")

def mainMenu():
    print ("\n\t[1] Resolusi 360p")
    print ("\t[2] Resolusi 720p")
    print ("\t[3] Convert MP4 to MP3")
    print ("\t[4] Exit")
    print ("\t╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━ ")

    choice = int(input("\tChoice ► "))

    if choice == 1:
        res360p.mainYt()

    elif choice == 2:
        print ("Resolusi 720p")

    elif choice == 3:
        pyaudio.mainAudio()

    elif choice == 4:
        sys.exit("See You Next Time")

if __name__=="__main__":
    mainMenu()
