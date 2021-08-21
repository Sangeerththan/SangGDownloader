import datetime
import os
import time

import pyperclip
import pytube
import wget
import re

from Utils.file_operations import move_files, progress_function

links = []
destination = "/home/sangee/Videos"
movingDirectory = "/home/sangee/Videos/CuttingEdge/TensorFlow/Projects"


def download_videos(_links, youtube=False):
    resolutions = ["1080p", "720p", "480p", "360p"]
    count = 0
    for link in _links:
        if youtube:
            count += 1
            yt = pytube.YouTube(link, on_progress_callback=progress_function)
            yt.register_on_progress_callback(progress_function)
            for resolution in resolutions:
                stream = yt.streams.filter(progressive=True, res=resolution).first()
                if stream is not None:
                    break;
            start_time = time.time()
            print("Start Time for Download Link " + str(count)+": "+link + " " + str(datetime.datetime.now()))
            print("Download Started ".center(50, "*"))
            stream.download(output_path=destination)
            finish_time = time.time();
            print("Download finished ".center(50, "*"))
            print("Finish Time for Download Link "+link + " " + str(datetime.datetime.now()))
            interval = finish_time - start_time
            duration = str(round(interval / 60, 3)) + " Minutes " + str(round(interval % 60, 3)) + " Seconds"
            print(("Time taken for downloading " + link + " is " + duration).center(50, "*"))
        # This is incomplete and currently not working
        else:
            print("Downloading Non Youtube File".center(70, "*"))
            # getting video
            count += 1
            wget.download(link, os.path.join(destination, str(count) + ".mp4"))
            print("Finished Downloading Non Youtube File".center(70, "*"))


def shutdown(shut):
    if shut == 'no':
        exit()
    else:
        os.system("shutdown /s /t 1")


def main():
    youtube_regex = re.compile(r'''(http:|https:)?\/\/(www\.)?(youtube.com|youtu.be)\/(watch)?(\?v=)?(\S+)?
    ''', re.VERBOSE)

    # Downloading limit of links
    download_limit = int(input("Enter links count: "))
    shut_down = input("Do you wish to shutdown your computer ? (yes / no): ")
    while True:
        copied_link = str(pyperclip.paste())
        # print("youtube regex is:"+str(youtube_regex.findall(copied_link)))
        match = youtube_regex.match(copied_link)
        if match is not None:
            links.append(copied_link)
        if len(set(links)) >= download_limit:
            break
    unique_links = list(set(links))
    print("Download Links are" + str(unique_links))
    download_videos(unique_links, True)

    # check whether directory is present
    if not os.path.exists(movingDirectory):
        os.makedirs(movingDirectory)

    print(("Files are copied from " + destination + " to " + movingDirectory).center(70, "*"))
    # moving downloads to directory
    move_files(destination, movingDirectory)
    shutdown(shut_down)


if __name__ == '__main__':
    main()
