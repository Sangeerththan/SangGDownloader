import re

youtube_regex = re.compile(r'''(http:|https:)?\/\/(www\.)?(youtube.com|youtu.be)\/(watch)?(\?v=)?(\S+)?
        ''', re.VERBOSE)

torrent_regex = re.compile(r'^(magnet:\?xt=urn:btih:).*')

fb_regex = re.compile(r'(^(https:|)[/][/]www.([^/]+[.])*facebook.com)|(^https://fb.watch/)')

instagram_regex = re.compile(r'(https?:\/\/www\.)?instagram\.com(\/p\/\w+\/?)')