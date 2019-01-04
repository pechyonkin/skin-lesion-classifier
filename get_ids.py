import requests
import json
import csv
from pprint import pprint


def ids_to_csv(filepath, list_of_str):
    """ Write each string onto a separate line of csv. """
    with open(filepath, "w") as out_file:
        wr = csv.writer(out_file)
        for id in list_of_str:
            wr.writerow([id])


def get_ids():
    base_url = "https://isic-archive.com/api/v1"
    image = "/image"

    start = 0
    step = 1000

    indices = []

    while True:

        params = {
            "offset": start,
            "limit": step,
            "sort": "name",
            "detail": False,
        }

        response = requests.get(base_url + image, params=params)

        response_content = json.loads(response.content)
        # response_headers = response.headers

        # print(response.status_code)
        # print(type(response_content))
        # print(len(response_content))
        # pprint(response_content)
        # pprint(type(response_headers))

        for elem in response_content:
            indices.append(elem['_id'])

        start += step

        if len(response_content) == 0:
            print(f"There are {len(indices)} ids in total.")
            break

        print(f"Have {len(indices)} ids.")

    return indices


ids = get_ids()
ids_to_csv("ids.csv", ids)

