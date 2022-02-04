from bs4 import BeautifulSoup
import requests
import time
import os
from Downloader.configuration import INSTAGRAM_PATH
from Downloader.Utils.tasks import shutdown
from Downloader.Utils.file_operations import create_folder


def download_insta_image(link):
    page = requests.get(link).content.decode('utf-8')
    soup = BeautifulSoup(page, 'lxml')
    img = soup.find('img', class_='FFVAD')
    img_url = img['src']
    r = requests.get(img_url)
    with open("instagram" + str(time.time()) + ".png", 'wb') as f:
        f.write(r.content)


def download_insta_images(_links, _shutdown='no', _path=INSTAGRAM_PATH):
    create_folder(_path)
    os.chdir(_path)
    for link in _links:
        download_insta_image(link)
    shutdown(_shutdown)
