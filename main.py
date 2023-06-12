from pytube import YouTube

link = input("Paste the YouTube video link: ")
YouTube_video = YouTube(link)

print("Title:", YouTube_video.title)
print("Views:", YouTube_video.views)
print("The YouTube video is downloading...")
yd = YouTube_video.streams.get_highest_resolution()
yd.download('.')