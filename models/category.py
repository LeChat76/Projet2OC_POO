""" create objects category and URL """
import requests
from bs4 import BeautifulSoup

MAIN_URL = "http://books.toscrape.com/"


class Category:
    """ Category class """
    INDEX = 0

    def __init__(self):
        """ init of the beautifulsoup result """
        main_page = requests.get(MAIN_URL)
        self.main_page_soup = BeautifulSoup(main_page.content, 'html.parser')
        self.main_categories = []
        self.main_url_categories = []

    def create_list_category(self):
        """Find all categories """
        main_li = self.main_page_soup.find_all("li")
        for li in main_li:
            if "category" in str(li) and not "books_1" in str(li):
                """ extraction of the category """
                pos1 = str(li).find("                                ") + 32
                pos2 = str(li).find("\n", pos1)
                cat = (str(li)[pos1:pos2])
                self.main_categories.append(cat)

    def create_list_url_category(self, create_list_category):
        """Find all url categories """
        main_li = self.main_page_soup.find_all("li")
        for li in main_li:
            if "category" in str(li) and not "books_1" in str(li):
                """ extraction of the URL of this category """
                pos1 = str(li).find("href") + 6
                pos2 = str(li).find(".html") + 5
                url_cat = "http://books.toscrape.com/" + str(li)[pos1:pos2]
                self.main_url_categories.append(url_cat)
                print(str(self.main_categories[Category.INDEX]) + " : " + url_cat)
                Category.INDEX += 1
