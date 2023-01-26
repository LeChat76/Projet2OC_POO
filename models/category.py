""" create objects category and URL """
import requests
from bs4 import BeautifulSoup

MAIN_URL = "http://books.toscrape.com/"
MAIN_PAGE = requests.get(MAIN_URL)
MAIN_PAGE_SOUP = BeautifulSoup(MAIN_PAGE.content, 'html.parser')
MAIN_LI = MAIN_PAGE_SOUP.find_all("li")


class Category:
    """ Category class """
    def __init__(self, category=""):
        """ init of the beautifulsoup result and lists"""
        self.category = category
        self.names_categories = []
        self.urls_categories = []
        self.url_category = ""

    def get_names_cat(self):
        """Find all categories names
        (for userview selection of category to extract
        """
        for li in MAIN_LI:
            if "category" in str(li) and not "books_1" in str(li):
                """ extraction of the category """
                pos1 = str(li).find("                                ") + 32
                pos2 = str(li).find("\n", pos1)
                cat = (str(li)[pos1:pos2])
                self.names_categories.append(cat)

    def get_urls_cats(self):
        """Find all url of categories """
        index = 0
        for li in MAIN_LI:
            if "category" in str(li) and not "books_1" in str(li):
                """ extraction of the URL of this category """
                pos1 = str(li).find("href") + 6
                pos2 = str(li).find(".html") + 5
                url_cat = "http://books.toscrape.com/" + str(li)[pos1:pos2]
                self.urls_categories.append(url_cat)
                index += 1

    def get_url_cat(self):
        """Find url for ONE category """
        for li in MAIN_LI:
            if ("  " + self.category) in str(li) and not "books_1" in str(li) and "category" in str(li):
                # extraction of the URL of this category
                pos1 = str(li).find("href") + 6
                pos2 = str(li).find(".html") + 5
                self.url_category = "http://books.toscrape.com/" + (str(li)[pos1:pos2])
