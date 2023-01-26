import os
import datetime
import csv
from models.books import Book
from models.category import Category
from models.images import Images

HEADER = ["product_page_url", "universal_product_code (upc)", "title", "price_including_tax",
          "price_excluding_tax", "number_available", "product_description", "category", "review_rating",
          "image_url"]


class CSV:
    """ CSV class """
    def __init__(self, category, img_download):
        self.category = category
        self.img_download = img_download

    def recording(self):
        """ manage recording of the CSV file """
        category = Category(self.category)
        category.get_url_cat()
        book = Book()
        book.get_urls_books(category.url_category)

        now = datetime.datetime.now()
        date_time = now.strftime("%d%m%Y_%H%M%S")

        csv_folder = os.path.join("data", "CSVs")
        if not os.path.exists(csv_folder):
            os.makedirs(csv_folder)

        path_csv = os.path.join(csv_folder, self.category + "_" + date_time + "_CSV.csv")

        """ testing if exists CSV or create it """
        if not os.path.exists(path_csv):
            try:
                with open(path_csv, "a", newline='', encoding="utf-32") as csv_file:
                    writer = csv.writer(csv_file, delimiter=",")
                    writer.writerow(HEADER)
                    csv_file.close()

            except IOError:
                print("\nErreur lors de la creation du fichier CSV.\nAvez vous les droits de création?")
                exit()

        with open(path_csv, "a", newline='', encoding="utf-32") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")

            for url_book in book.urls_books:
                book = Book(url_book)
                book.get_product_info()
                writer.writerow(book.product_info)

                if self.img_download == "Y":
                    image = Images(url_book, book.title, self.category)
                    image.get_image_file()

        csv_file.close()
