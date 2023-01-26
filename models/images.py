import shutil
import requests
from bs4 import BeautifulSoup
import os


class Images:
    """ Images class"""
    def __init__(self, url_book, title, category):
        self.url_book = url_book
        self.category = category
        self.title = title
    def get_image_file(self):
        """ method for download image of cover book"""
        product_page = requests.get(self.url_book)
        soup_img = BeautifulSoup(product_page.content, 'html.parser')

        image = str(soup_img.find(class_="item active"))
        pos1 = image.find("../../") + 6
        pos2 = image.find("jpg", pos1) + 3
        image_url = ("http://books.toscrape.com/" + (image[pos1: pos2]))

        img_folder = os.path.join("data", self.category)
        if not os.path.exists(img_folder):
            os.makedirs(img_folder)

        """ downloading image file """
        img = requests.get(image_url, stream=True)

        """ replace special caracters incompatible with name file """
        title = self.title.replace(":", " ").replace("'", " ").replace("*", ".").replace("/", "-").replace('"', '-').replace(
                "?", ".").replace(",", " ")

        """ to keep the same extension in cas of other image format (bmp or other) """
        image_ext = image_url[-4:]
        with open(os.path.join(img_folder, title + image_ext), 'wb') as img_file:
            shutil.copyfileobj(img.raw, img_file)
            img_file.close()
