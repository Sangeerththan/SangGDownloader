import libtorrent as lt
import time
import os

from Downloader.Utils.tasks import shutdown, get_download_inputs, links_copied_to_clipboard
from Downloader.Utils.regex import torrent_regex
from Downloader.Config import TORRENT_PATH


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


def downloads(_path=TORRENT_PATH, _shutdown='no'):
    download_limit, _shut_down = get_download_inputs()
    links = links_copied_to_clipboard(download_limit, torrent_regex)
    for link in links:
        download_magnetic_link(link, _path)
    shutdown(_shutdown)


downloads()
