from datetime import datetime
import requests


def download_video(video_url):
    """Download the video """
    file_size_request = requests.get(video_url, stream=True)
    print(file_size_request)
    # file_size = int(file_size_request.headers['Content-Length'])
    block_size = 1024
    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    # t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=False)
    with open(filename + '.mp4', 'wb') as f:
        for data in file_size_request.iter_content(block_size):
            f.write(data)
    print("\nVideo downloaded successfully.")
