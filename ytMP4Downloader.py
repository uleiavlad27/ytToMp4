from pytube import YouTube
import os

print("Merge")
URL = input("Enter the URl of the video you want to download: \n>>")
yt = YouTube(URL)

try:
    audio = yt.streams.filter(only_audio=True).first()
    out_file = audio.download()
    destination = str(input(">> ")) or '.'
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print('Downloaded')

except:
    print("\nError. Please Try Again\n")
