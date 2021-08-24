import os
import shutil
import sys


def move_files(src, destination):
    files = os.listdir(src)
    for f in files:
        file_path = os.path.join(src, f)
        print(("copying file " + str(f)).center(70, "#"))
        if os.path.isfile(file_path) and os.path.isdir(destination):
            print(("Moving file " + str(f)).center(70, "#"))
            print(file_path)
            shutil.move(file_path, destination)


# Display a download progress bar
def progress_function(stream, _chunk, bytes_remaining):
    current = ((stream.filesize - bytes_remaining) / stream.filesize)
    percent = '{0:.1f}'.format(current * 100)
    progress = int(50 * current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()


# create a folder if not exists
def create_folder(_dir):
    if not os.path.exists(_dir):
        os.makedirs(_dir)
