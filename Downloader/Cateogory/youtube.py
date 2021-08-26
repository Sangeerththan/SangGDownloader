import datetime
import time
import pytube

from Downloader.Utils.file_operations import progress_function
from Downloader.Utils.tasks import shutdown
from Downloader.configuration import YOUTUBE_PATH
from Downloader.Utils.file_operations import create_folder


def download_youtube_videos(_links, _shutdown='no',_path=YOUTUBE_PATH):
    create_folder(_path)
    resolutions = ["1080p", "720p", "480p", "360p"]
    count = 0
    for link in _links:
        count += 1
        yt = pytube.YouTube(link, on_progress_callback=progress_function)
        for resolution in resolutions:
            stream = yt.streams.filter(progressive=True, res=resolution).first()
            if stream is not None:
                break;
        start_time = time.time()
        print("Start Time for Download Link " + str(count) + ": " + link + " " + str(datetime.datetime.now()))
        print("Download Started ".center(50, "*"))
        stream.download(output_path=_path)
        finish_time = time.time();
        print("Download finished ".center(50, "*"))
        print("Finish Time for Download Link " + link + " " + str(datetime.datetime.now()))
        interval = finish_time - start_time
        duration = str(round(interval / 60, 3)) + " Minutes " + str(round(interval % 60, 3)) + " Seconds"
        print(("Time taken for downloading " + link + " is " + duration).center(50, "*"))
        shutdown(_shutdown)
