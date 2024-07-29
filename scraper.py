import requests 
from bs4 import BeautifulSoup
import pandas
import os

class Scraper:
    def __init__(self) -> None:
        self.csvfile = pandas.read_csv(os.path.join(os.getcwd(),"links.csv"))
    
    def getinfo(self,colname) -> list[str]:
        return self.csvfile[colname]
    
    def scrape(self):
        URLS = self.getinfo("Links")
        for URL in URLS:
            link = requests.get(URL)
            print(link.status_code)
            soup  = BeautifulSoup(link.content,"html.parser")
            box   = soup.find("div",{"class":"a-box-inner"})
            print(box)
            price = box.find("span",{"class":"a-price-whole"})
            priceparsed = price[:price.find(".")]
            print(priceparsed)


if __name__ == '__main__':
    s = Scraper()
    s.scrape()
