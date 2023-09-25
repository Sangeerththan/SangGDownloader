import os
import time
import torrent
from Downloader.Utils.tasks import shutdown
from Downloader.configuration import TORRENT_PATH
from Downloader.Utils.file_operations import create_folder


def download_magnetic_link(links, _shutdown='no', _path=TORRENT_PATH):
    if not os.path.exists(_path):
        os.makedirs(_path)

    for link in links:
        client = torrent.Client()
        client.fetch(link, _path)

        print(f"Downloading {link}")

        while not client.is_seed():
            status = client.get_status()
            print(f"Progress: {status.progress * 100:.2f}%")
            time.sleep(5)

        client.shutdown()

    if _shutdown == 'yes':
        torrent.Client.shutdown()

def download_torrents(links, _shutdown='no', _path=TORRENT_PATH):
    create_folder(_path)
    for link in links:
        download_magnetic_link(link, _path)
    shutdown(_shutdown)
