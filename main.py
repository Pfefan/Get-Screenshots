"""Module imports"""
import random
import shutil  # to save it locally
import string

import cfscrape
import requests  # to get image from the web
from bs4 import BeautifulSoup

class Imagehandler():
    """class to handle images"""
    def __init__(self) -> None:
        self.Url = "https://prnt.sc/"
        self.Stringlen = 6
        self.sorted_list = []
        self.imagecount = 0
        self.imagelimit = 0

    def main(self):
        """main func to call all functions"""

        self.imagelimit = input("enter how many pictures you want: ")
        while int(self.imagelimit) >= self.imagecount:
            self.urlget()
            self.imagecount += 1

    def urlget(self):
        """funtion to get urls of pictures"""

        self.Url = "https://prnt.sc/"
        self.sorted_list.clear()
        ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = self.Stringlen))    #random 6 character long string
        self.Url = self.Url + str(ran)

        scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
        scraped_content = scraper.get(self.Url).content
        html_page = BeautifulSoup(scraped_content, 'html.parser')
        images = html_page.find_all("meta")

        for i in images:
            out = str(i).split('"')
            self.sorted_list.append(out[1])
        try:
            self.download(self.sorted_list[10])
        except:
            pass

    def download(self, imgurl):
        """Download image from URL"""

        image_url = imgurl
        filename = image_url.split("/")[-1]

        r = requests.get(image_url, stream = True)
        r.raw.decode_content = True
        if r.status_code == 200:
            r.raw.decode_content = True
            with open("screenshots/" + filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            pass

if __name__ == "__main__":
    Imagehandler().main()
