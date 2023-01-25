import os
import csv
import datetime
from models.books import Book
class CSV:
    """ CSV class """
    def __init__(self):
        self.header = ["product_page_url", "universal_product_code (upc)", "title", "price_including_tax",
                  "price_excluding_tax",
                  "number_available", "product_description", "category", "review_rating", "image_url"]
        self.now = datetime.datetime.now()
        self.date_time = self.now.strftime("%d%m%Y_%H%M%S")
    def recording(self, url_cat):
        """ manage recording of the CSV file """
        book = Book()
        self.url_cat url_cat

        csv_folder = os.path.join("data", "CSVs")
        if not os.path.exists(csv_folder):
            os.makedirs(csv_folder)

        path_csv = os.path.join(csv_folder, self.url_cat + "_" + self.date_time + "_CSV.csv")

        """ testing if exists CSV or create it """
        if not os.path.exists(path_csv):
            try:
                with open(path_csv, "a", newline='', encoding="utf-32") as csv_file:
                    writer = csv.writer(csv_file, delimiter=",")
                    writer.writerow(self.header)
                    csv_file.close()

            except IOError:
                print("\nErreur lors de la creation du fichier CSV.\nAvez vous les droits de création?")
                exit()

        with open(path_csv, "a", newline='', encoding="utf-32") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")

        book_infos = book.get_product_info(self.product_page_url)
