import os

import pyperclip


def shutdown(shut):
    if shut == 'yes':
        os.system("systemctl poweroff")
    else:
        pass


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


def get_download_inputs():
    download_limit = int(input("Enter links count: "))
    shut_down = input("Do you wish to shutdown your computer ? (yes / no): ")
    return download_limit, shut_down
