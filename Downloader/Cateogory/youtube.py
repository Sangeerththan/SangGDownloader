from __future__ import unicode_literals
import datetime
import time
import youtube_dl
from Downloader.Utils.tasks import shutdown
from Downloader.configuration import YOUTUBE_PATH
from Downloader.Utils.file_operations import create_folder
import os


def download_youtube_videos(_links, _shutdown='no', _path=YOUTUBE_PATH):
    create_folder(_path)
    resolutions = ["1080p", "720p", "480p", "360p"]
    count = 0
    for link in _links:
        count += 1
        start_time = time.time()
        print("Start Time for Download Link " + str(count) + ": " + link + " " + str(datetime.datetime.now()))
        print("Download Started ".center(50, "*"))
        ydl_opts = {
            'outtmpl': os.path.join(_path, '%(title)s.%(ext)s')
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        finish_time = time.time();
        print("Download finished ".center(50, "*"))
        print("Finish Time for Download Link " + link + " " + str(datetime.datetime.now()))
        interval = finish_time - start_time
        duration = str(round(interval / 60, 3)) + " Minutes " + str(round(interval % 60, 3)) + " Seconds"
        print(("Time taken for downloading " + link + " is " + duration).center(50, "*"))
        shutdown(_shutdown)
