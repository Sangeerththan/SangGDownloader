import libtorrent as lt
import time

ses = lt.session()
ses.listen_on(6881, 6891)
params = {
    'save_path': '/home/sangee/Torrents',
    'storage_mode': lt.storage_mode_t(2)}
link = "link"
handle = lt.add_magnet_uri(ses, link, params)
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
