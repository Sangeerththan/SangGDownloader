from datetime import datetime
from tqdm import tqdm
import requests
import re
import os
from Downloader.configuration import FB_PATH
from Downloader.Utils.tasks import shutdown
from Downloader.Utils.file_operations import create_folder


def download(link):
    page = requests.get(link).content.decode('utf-8')
    resolutions = ['hd', 'sd']
    video_url = ''
    for resolution in resolutions:
        _url = re.search(rf'{resolution}_src:"(.+?)"', page)
        if _url is not None:
            video_url = _url.group(1)
            break
    file_size_request = requests.get(video_url, stream=True)
    file_size = int(file_size_request.headers['Content-Length'])
    block_size = 1024
    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
    with open(filename + '.mp4', 'wb') as f:
        for data in file_size_request.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()


def download_fb_videos(_links, _shutdown='no', _path=FB_PATH):
    create_folder(_path)
    os.chdir(_path)
    for link in _links:
        download(link)
    shutdown(_shutdown)
