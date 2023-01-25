""" create object book"""
import requests
from bs4 import BeautifulSoup


class Book:
    """ Book class"""

    def __init__(self, product_page_url):
        self.product_page_url = product_page_url

    def get_product_info(self):
        """ requesting web site """
        product_page = requests.get(self.product_page_url)
        soup = BeautifulSoup(product_page.content, 'html.parser')

        """ values in 'td' will be used 4 times, so I declared "globally"
        # [0] universal product code
        # [2] price excluding tax
        # [3] price including tax
        # [5] number of books available """
        td = soup.find_all("td")

        universal_product_code = td[0].string

        title = (soup.find("li", class_="active"))
        self.title = title.string

        """ price_including_tax """
        self.price_including_tax = td[3].string

        """ price_excluding_tax """
        self.price_excluding_tax = td[2].string

        """ number_available """
        number_available = td[5].string
        self.number_available = (number_available.replace("In stock (", "")).replace(" available)", "")

        """ product_description """
        desc = soup.find("meta", attrs={"name": "description"})
        desc = (str(desc).replace("&quot;", "")).replace(";", ",")
        self.product_description = desc[20:-31]

        """ image_url """
        image = str(soup.find(class_="item active"))
        pos1 = image.find("../../") + 6
        pos2 = image.find("jpg", pos1) + 3
        self.image_url = ("http://books.toscrape.com/" + (image[pos1: pos2]))

        """ review_rating """
        review_rating = str(soup.find("p", class_="star-rating"))
        pos1 = review_rating.find("star-rating") + 12
        pos2 = review_rating.find(">") - 1
        self.review_rating = review_rating[pos1: pos2]
