import os
import time
import libtorrent as lt
from Downloader.Utils.tasks import shutdown
from Downloader.configuration import TORRENT_PATH
from Downloader.Utils.file_operations import create_folder


def download_magnetic_link(_link, _path=TORRENT_PATH):
    ses = lt.session()
    ses.listen_on(6881, 6891)
    if not os.path.exists(_path):
        os.makedirs(_path)
    params = {
        'save_path': _path,
        'storage_mode': lt.storage_mode_t(2)}
    handle = lt.add_magnet_uri(ses, _link, params)
    ses.start_dht()

    print('downloading metadata...')
    while not handle.has_metadata():
        time.sleep(1)
    print('got metadata, starting torrent download...')
    while handle.status().state != lt.torrent_status.seeding:
        s = handle.status()
        state_str = ['queued', 'checking', 'downloading metadata', \
                     'downloading', 'finished', 'seeding', 'allocating']
        print('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
               s.num_peers, state_str[s.state]))
        time.sleep(5)


def download_torrents(links, _shutdown='no', _path=TORRENT_PATH):
    create_folder(_path)
    for link in links:
        download_magnetic_link(link, _path)
    shutdown(_shutdown)
