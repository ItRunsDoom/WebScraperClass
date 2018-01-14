# Made by Leon Goldner-Katz, Jan 14, 2018
# Scrapes user-inputted URL and lets the user manipulate it
import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url, tag):
        self.url = url
        self.tag = tag
    def manURL(self, tagSearch, prettify):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        if tagSearch == True:
            searchedTag = soup.find_all(self.tag)
            return searchedTag
        if prettify == True:
            prettifiedSoup = soup.prettify()
            return prettifiedSoup
