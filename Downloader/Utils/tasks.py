import os


def shutdown(shut):
    if shut == 'yes':
        os.system("systemctl poweroff")
    else:
        exit()