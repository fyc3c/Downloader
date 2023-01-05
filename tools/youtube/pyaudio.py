import os
from pytube import YouTube

def mainAudio():
    yt = YouTube(str(input("Masukan Url ▶ ")))

    video = yt.streams.filter(only_audio = True).first()

    print("Enter the destination (leave blank for current directory)")

    destination = str(input("▶ ")) or '.'

    out_file = video.download(output_path = destination)

    #Save The File
    base, ext = os.path.splitext(out_file) 

    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(yt.title + " has been successfully downloaded.")
