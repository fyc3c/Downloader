# Import Module
import os
import sys
from tools.youtube.bannerYoutube import bannerYoutube1 as by
from tools import load
from pytube import YouTube

def mainYt():
    os.system("clear")

    by()

    link = input("Input Link or command ;) ▶ ")

    if link == "exit":
        sys.exit("See You~")

    elif link == "back":
        print ("Back To Menu")

    yt = YouTube(link)

    # Yt Title
    print ("\n\nYoutube Title ▶ ", yt.title)
    # Yt Thumbnail
    print ("\nLink Thumbnail ▶ ", yt.thumbnail_url)

    # Proses download, gua download res 360 :P
    load.load1()
    yt.streams.filter(res="360p").first().download()
    # Animasi Loading file load.py def load():
    load.load2()

    # Thanks for pytube module :)
    print ("\t\t Download Selesai...")

    # Download Gidah sepuas lu asal ada kouta :V...

if __name__=='__main__':
    mainYt()
