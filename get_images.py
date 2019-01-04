import requests
import time
import csv
import json


def download_image(id, path = ''):
    BASE_URL = "https://isic-archive.com/api/v1"
    IMAGE = "/image"
    ID = id
    DOWNLOAD = "/download"

    response = requests.get(BASE_URL + IMAGE + '/' + ID + DOWNLOAD)

    # print(response.headers)

    # print(len(response.content))

    with open(path + f"{ID}.jpg", "wb") as f:
        f.write(response.content)

list_ids = []

with open('ids.csv', 'r') as f:
    for line in f:
        list_ids.append(line.strip('\n'))

start_time = time.time()

for i, id in enumerate(list_ids):
    download_image(list_ids[i], 'test/')
    if i % 100 == 0:
        print(f'Did {i} images, last 100 in {time.time() - start_time} seconds.')
        start_time = time.time()

