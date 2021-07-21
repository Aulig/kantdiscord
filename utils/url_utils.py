import random

import requests


def url_prepare_string(input):
    if not input:
        return "_"
    else:
        # best option would be to url-encode like this:
        # return urllib.parse.quote(input)
        # but discord won't embed correctly encoded urls for some reason?
        return input.replace(" ", "_")


def download_file(url):
    randnum = random.randint(0, 10000)

    local_name = f"tmp-{randnum}"

    response = requests.get(url)
    if response.status_code == 200:
        with open(local_name, 'wb') as f:
            f.write(response.content)

    return local_name