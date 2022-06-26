"""Module imports"""
import itertools
import os
import random
import string
import time
import math
from datetime import datetime
from threading import Thread

import cfscrape
import requests
from bs4 import BeautifulSoup


class Imagehandler():
    """class to handle images"""
    def __init__(self) -> None:
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.url = "https://prnt.sc/"
        self.mode = ""
        self.imglimit = 0
        self.imgcount = 0
        self.errors = 0

    def main(self):
        """main func to call all functions"""

        if not os.path.isdir("screenshots"):
            os.mkdir("screenshots")
        os.system("title Get-Screenshots by Pfefan#4055")

        print("""
_________                                         .__            __          
/   _____/ ___________   ____   ____   ____   _____|  |__   _____/  |_  ______
\_____  \_/ ___\_  __ \_/ __ \_/ __ \ /    \ /  ___/  |  \ /  _ \   __\/  ___/
/        \  \___|  | \/\  ___/\  ___/|   |  \\___ \|   Y  (  <_> )  |  \___ \ 
/_______  /\___  >__|    \___  >\___  >___|  /____  >___|  /\____/|__| /____  >   by Pfefan#4055 and Dovid
        \/     \/            \/     \/     \/     \/     \/                 \/   

        """)
        self.imglimit = input("Enter amount of pictures: ")
        while self.mode not in ["1", "2"]:
            self.mode = input("Enter mode (1: random mode, 2: structured mode): ")

        Thread(target=self.interface, daemon=True).start()
        while int(self.imglimit) > self.imgcount:
            if self.mode == "1":
                ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 6))
                self.urlget(self.url + str(ran))
            elif self.mode == "2":
                fulllist = self.letters + self.num
                for i in itertools.combinations(fulllist, 6):
                 self.urlget(self.url + "".join(i))
            self.imgcount += 1
        time.sleep(1.1)
        input("press any key to continue...")

    def interface(self):
        """Print info about the programm"""
        line_length = 50
        start = datetime.now()
        print(f"[{'-'*(line_length)}]", end="\r")
        while int(self.imglimit) > self.imgcount:
            elapsed_time = datetime.now()-start
            percent = (self.imgcount)/int(self.imglimit)
            print(f"[{'#'*math.ceil(line_length*percent)}{'-'*math.ceil(line_length*(1-percent))}]"+
            f" {self.imgcount}|{self.imglimit}, errors: {self.errors},"+
            f"elapsed time: {elapsed_time}", end="\r")
            time.sleep(1)
        print(f"[{'#'*(line_length+1)}]  {self.imgcount}|{self.imglimit}, errors: {self.errors}, "+
        f"elapsed time: {elapsed_time}")

    def urlget(self, url):
        """funtion to get urls of pictures"""
        sorted_list = []
        scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
        scraped_content = scraper.get(url).content
        html_page = BeautifulSoup(scraped_content, 'html.parser')
        images = html_page.find_all("meta")

        for i in images:
            out = str(i).split('"')
            sorted_list.append(out[1])

        if len(sorted_list) >= 10:
            self.download(sorted_list[10])
        else:
            self.errors += 1



    def download(self, imgurl):
        """Download image from URL"""

        if imgurl.split("/")[2] == "st.prntscr.com":
            imgurl = "http:" + imgurl
        filename = imgurl.split("/")[-1]
        try:
            response = requests.get(imgurl, headers={'User-Agent': 'Chrome'})

            if response.status_code == 200:
                with open("screenshots/" + filename,'wb') as file:
                    file.write(response.content)
        except:
            self.errors += 1

if __name__ == "__main__":
    Imagehandler().main()
