import re

youtube_regex = re.compile(r'''(http:|https:)?\/\/(www\.)?(youtube.com|youtu.be)\/(watch)?(\?v=)?(\S+)?
        ''', re.VERBOSE)


def test_fb_youtube_regex():
    assert youtube_regex.match('https://www.youtube.com/watch?v=x6Q7c9RyMzk') is not None
