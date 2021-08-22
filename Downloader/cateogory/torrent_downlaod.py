import libtorrent as lt
import time
import os

BASE_PATH = "/home/sangee/Videos/Movies/New"


def download_magnetic_link(_link, _path):
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


def downloads(links, _path=BASE_PATH, shutdown='no'):
    download_magnetic_link(
        "magnet:?xt=urn:btih:3dfc016e786850cfe49dbe09f988aeeeb29437a5&dn=www.4MovieRulz.tc%20-%20THITTAM%20IRANDU%20(2021)%20Tamil%20HQ%20HDRip%20-%20x264%20-%20AAC%20-%20700MB%20-%20ESub.mkv&tr=udp%3a%2f%2ftracker.leechers-paradise.org%3a6969%2fannounce&tr=udp%3a%2f%2fp4p.arenabg.com%3a1337%2fannounce&tr=http%3a%2f%2fpow7.com%3a80%2fannounce&tr=udp%3a%2f%2f9.rarbg.me%3a2970%2fannounce&tr=udp%3a%2f%2f9.rarbg.com%3a2790%2fannounce&tr=udp%3a%2f%2f9.rarbg.to%3a2730%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.yoshi210.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounce&tr=http%3a%2f%2ftracker2.itzmx.com%3a6961%2fannounce&tr=udp%3a%2f%2f151.80.120.114%3a2710%2fannounce&tr=http%3a%2f%2ftracker.yoshi210.com%3a6969%2fannounce&tr=udp%3a%2f%2fopen.stealth.si%3a80%2fannounce&tr=http%3a%2f%2ft.nyaatracker.com%3a80%2fannounce",
        BASE_PATH)
    download_magnetic_link(
        "magnet:?xt=urn:btih:02422a0a98678f3e1560796e74b190d04c08a248&dn=www.4MovieRulz.lc%20-%20iSMART%20SHANKAR%20(2021)%20Tamil%20HQ%20HDRip%20-%20x264%20-%20Original%20Aud%20-%20700MB%20ESub.mkv&tr=udp%3a%2f%2ftracker.leechers-paradise.org%3a6969%2fannounce&tr=udp%3a%2f%2fp4p.arenabg.com%3a1337%2fannounce&tr=http%3a%2f%2fpow7.com%3a80%2fannounce&tr=udp%3a%2f%2f9.rarbg.me%3a2970%2fannounce&tr=udp%3a%2f%2f9.rarbg.com%3a2790%2fannounce&tr=udp%3a%2f%2f9.rarbg.to%3a2730%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.yoshi210.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounce&tr=http%3a%2f%2ftracker2.itzmx.com%3a6961%2fannounce&tr=udp%3a%2f%2f151.80.120.114%3a2710%2fannounce&tr=http%3a%2f%2ftracker.yoshi210.com%3a6969%2fannounce&tr=udp%3a%2f%2fopen.stealth.si%3a80%2fannounce&tr=http%3a%2f%2ft.nyaatracker.com%3a80%2fannounce",
        BASE_PATH)
    shutdown(shutdown)


def shutdown(shut):
    if shut == 'no':
        exit()
    else:
        os.system("shutdown /s /t 1")


downloads([], '', 'yes')
