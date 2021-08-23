import re

youtube_regex = re.compile(r'''(http:|https:)?\/\/(www\.)?(youtube.com|youtu.be)\/(watch)?(\?v=)?(\S+)?
        ''', re.VERBOSE)

torrent_regex = re.compile(r'^(magnet:\?xt=urn:btih:).*')
