import shutil  # to save it locally

import requests  # to get image from the web
import wget


class imgdownload:
    def __init__(self, url):
        self.url = url
        self.counter = 0

    def download(self):
        image_url = self.url
        filename = image_url.split("/")[-1]

        r = requests.get(image_url, stream = True)
        r.raw.decode_content = True
        if r.status_code == 200:
            r.raw.decode_content = True
            with open("screenshots/" + filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            pass
