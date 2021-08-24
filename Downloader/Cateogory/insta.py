from bs4 import BeautifulSoup
import requests
import time
import os
from Downloader.configuration import INSTAGRAM_PATH
from Downloader.Utils.tasks import shutdown


def download_insta_image(link):
    page = requests.get(link).content.decode('utf-8')
    soup = BeautifulSoup(page, 'lxml')
    img = soup.find('img', class_='FFVAD')
    img_url = img['src']
    r = requests.get(img_url)
    with open("instagram" + str(time.time()) + ".png", 'wb') as f:
        f.write(r.content)
    print('success')


def download_insta_images(_links, _shutdown='no', _path=INSTAGRAM_PATH):
    os.chdir(_path)
    for link in _links:
        download_insta_image(link)
    shutdown(_shutdown)
