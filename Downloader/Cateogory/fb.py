from datetime import datetime
from tqdm import tqdm
import requests
import re
import os
from Downloader.Config.configuration import FB_PATH
from Downloader.Utils.tasks import shutdown


def download(link):
    page = requests.get(link).content.decode('utf-8')
    _qualityhd = re.search('hd_src:"https', page)
    _qualitysd = re.search('sd_src:"https', page)
    _hd = re.search('hd_src:null', page)
    _sd = re.search('sd_src:null', page)
    list = []
    _thelist = [_qualityhd, _qualitysd, _hd, _sd]
    for id, val in enumerate(_thelist):
        if val != None:
            list.append(id)
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
    print("\nVideo downloaded successfully.")


def fb_download_videos(_links, _shutdown='no', _path=FB_PATH):
    os.chdir(_path)
    for link in _links:
        download(link)
    shutdown(_shutdown)
