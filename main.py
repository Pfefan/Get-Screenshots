import string, random, cfscrape
from bs4 import BeautifulSoup

from image_download import imgdownload

Url = "https://prnt.sc/"
Stringlen = 6
sorted_list = []
imagecount = 0
pass_limit = input("enter how many pictures you want: ")

while(imagecount < int(pass_limit)):
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = Stringlen))    #random 6 character long string
    Url = Url + str(ran)

    scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
    scraped_content = scraper.get(Url).content
    html_page = BeautifulSoup(scraped_content, 'html.parser')
    images = html_page.find_all("meta")
    for i in images:
        out = str(i).split('"')
        sorted_list.append(out[1])
    try:
        imgdownload(sorted_list[10]).download()
    except:
        pass

    imagecount += 1
    Url = "https://prnt.sc/"
    sorted_list = []
