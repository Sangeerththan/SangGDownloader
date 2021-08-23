import os
import pyperclip
import re


def shutdown(shut):
    if shut == 'yes':
        os.system("systemctl poweroff")
    else:
        exit()


def links_copied_to_clipboard(limit, regex):
    links = []
    while True:
        copied_link = str(pyperclip.paste())
        match = regex.match(copied_link)
        if match is not None:
            links.append(copied_link)
        if len(set(links)) >= limit:
            break
    unique_links = list(set(links))
    return unique_links
