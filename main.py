"""Module imports"""
import random
import string

import cfscrape
import requests
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
        while int(self.imagelimit) > self.imagecount:
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

        self.download(self.sorted_list[10])


    def download(self, imgurl):
        """Download image from URL"""

        if imgurl.split("/")[2] == "st.prntscr.com":
            imgurl = "http:" + imgurl
        print(imgurl)
        filename = imgurl.split("/")[-1]

        response = requests.get(imgurl, headers={'User-Agent': 'Chrome'})

        print(response.status_code)
        if response.status_code == 200:
            with open("screenshots/" + filename,'wb') as f:
                f.write(response.content)
        else:
            pass

if __name__ == "__main__":
    Imagehandler().main()
