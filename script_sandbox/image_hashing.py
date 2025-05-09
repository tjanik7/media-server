import requests
import os

def get_files_in_dir():
    base_path = '/Users/tyjanik/devel/media_server/script_sandbox/files_to_send'

    files = []

    directory = os.fsencode(base_path)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".png") or filename.endswith(".jpg"):
            full_path = os.path.join(directory, file)
            files.append(full_path)

    return files


def send_images(images):
    url = 'http://127.0.0.1:8000/media/hi'

    # images = [
    #     'cubs.png',
    #     'img1.jpg',
    # ]

    # { filename -> opened file handle }
    file_list = {image: open(image, 'rb') for image in images}

    response = requests.post(url, files=file_list)
    print(response.text)

imgs = get_files_in_dir()
send_images(imgs)