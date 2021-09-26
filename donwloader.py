from pytube import YouTube
import os

def downloadYoutube(vid_url, path):
    yt = YouTube(vid_url)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

url = 'https://www.youtube.com/watch?v=60ItHLz5WEA'
path = 'Downloads'
downloadYoutube(url, path)