import re

youtube_regex = re.compile(r'''(http:|https:)?\/\/(www\.)?(youtube.com|youtu.be)\/(watch)?(\?v=)?(\S+)?
        ''', re.VERBOSE)
fb_regex = re.compile(r'^(https:|)[/][/]www.([^/]+[.])*facebook.com')


def test_youtube_regex():
    assert youtube_regex.match('https://www.youtube.com/watch?v=x6Q7c9RyMzk') is not None


def test_fb_regex():
    assert fb_regex.match('https://www.facebook.com/FirstMediaBlossom/videos/170422694626128/') is not None
