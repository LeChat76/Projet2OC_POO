""" create objects books"""
import requests
from bs4 import BeautifulSoup


class Book:
    """ Book class"""

    def get_product_info(self, product_page_url):
        """ requesting web site """
        self.product_page_url = product_page_url
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

    def urls_books(self, category):
        """Find all url for books of one category """
        self.category = category
        main_url = "http://books.toscrape.com/"
        main_page_soup = BeautifulSoup(main_page.content, 'html.parser')
        main_page = requests.get(main_url)
        list_products_url = []
        next_category_page_url = ""
        main_li = main_page_soup.find_all("li")
        for li in main_li:
            if ("  " + self.category) in str(li) and not "books_1" in str(li) and "category" in str(li):
                # extraction of the URL of this category
                pos1 = str(li).find("href") + 6
                pos2 = str(li).find(".html") + 5
                main_url_category = "http://books.toscrape.com/" + (str(li)[pos1:pos2])