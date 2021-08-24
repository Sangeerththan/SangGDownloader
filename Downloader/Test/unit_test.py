from Downloader.Utils.regex import youtube_regex


def test_fb_youtube_regex():
    assert youtube_regex.match('https://www.youtube.com/watch?v=x6Q7c9RyMzk') is not None
