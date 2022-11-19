from pytube import YouTube

link=str(input("enter the link"))

yt=YouTube(link)

stream = yt.streams.get_highest_resolution()

stream.download()

print("downloaded sucessfully")