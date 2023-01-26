""" create objects books"""
import requests
from bs4 import BeautifulSoup


class Book:
    """ Book class"""
    def __init__(self, product_page_url=""):
        self.product_page_url = product_page_url
        self.product_info = ""
        self.urls_books = []
        self.url_category = ""
        self.title = ""

    def get_product_info(self):
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
        price_including_tax = td[3].string

        """ price_excluding_tax """
        price_excluding_tax = td[2].string

        """ number_available """
        number_available = td[5].string
        number_available = (number_available.replace("In stock (", "")).replace(" available)", "")

        """ product_description """
        desc = soup.find("meta", attrs={"name": "description"})
        desc = (str(desc).replace("&quot;", "")).replace(";", ",")
        product_description = desc[20:-31]

        """ category """
        for link in soup.find_all('a'):
            if "../category/books/" in str(link):
                pos1 = str(link).find("books") + 6
                pos2 = str(link).find("index", pos1) - 3
                category = str(link)[pos1: pos2]

        """ image_url """
        image = str(soup.find(class_="item active"))
        pos1 = image.find("../../") + 6
        pos2 = image.find("jpg", pos1) + 3
        image_url = ("http://books.toscrape.com/" + (image[pos1: pos2]))

        """ review_rating """
        review_rating = str(soup.find("p", class_="star-rating"))
        pos1 = review_rating.find("star-rating") + 12
        pos2 = review_rating.find(">") - 1
        review_rating = review_rating[pos1: pos2]

        self.product_info = [self.product_page_url, universal_product_code, self.title, price_including_tax,
                             price_excluding_tax, number_available, product_description, category, review_rating,
                             image_url]

    def get_urls_books(self, url_category):
        """Find all books urls for ONE url category """
        product_page = requests.get(url_category)
        while product_page.status_code == 200:
            soup = BeautifulSoup(product_page.content, 'html.parser')
            products_url = soup.find_all("h3")

            for url in products_url:
                pos1 = str(url).find("../../") + 9
                pos2 = str(url).find("index.html", pos1)
                product_url = ("http://books.toscrape.com/catalogue/" + str(url)[pos1: pos2])
                self.urls_books.append(product_url)

            """ test if next page exists """
            next_category_page_name = str(soup.find("li", class_="next"))
            if next_category_page_name != "None":
                pos1 = next_category_page_name.find("href=") + 6
                pos2 = next_category_page_name.find(">next") - 1
                next_category_page_name = next_category_page_name[pos1:pos2]
                next_category_page_url = url_category.replace("index.html", next_category_page_name)
                product_page = requests.get(next_category_page_url)
            else:
                product_page.status_code = 404
