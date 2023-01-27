from models.category import Category
from views.user import UserView
from models.csv_file import CSV
import datetime


class Controller:
    """ Main controller """

    def __init__(self):
        self.download_img = ""

    def start_scraping(self):
        try:
            """ launch all necessary method to scrape the website """
            category = Category()
            category.get_names_cat()
            category.get_urls_cats()

            userview = UserView()
            userview.prompt_for_category(category.names_categories)
            userview.prompt_for_img_download()

            now_begin = datetime.datetime.now()
            if userview.cat_choice.upper() == "T":
                for category in category.names_categories:
                    csv = CSV(category, userview.img_download)
                    csv.recording()
                now_end = datetime.datetime.now()
                now_delta = now_end - now_begin
                print("Fin de l'extraction, vous pouvez consulter les fichiers CSVs horodatés à la date du jour dans le"
                      " dossier \\Data\\CSVs.")
                if userview.img_download:
                    print("Les images de couvertures sont enregistrées dans chaque dossiers nommés de leurs catégories"
                          ".")
                print("\nTemps de traitement : " + str(now_delta)[:7])
            else:
                csv = CSV(category.names_categories[userview.index], userview.img_download)
                csv.recording()
                now_end = datetime.datetime.now()
                now_delta = now_end - now_begin
                print("Fin de l'extraction, vous pouvez consulter le fichiers CSV horodaté à la date du jour dans le "
                      "dossier \\Data\\CSVs.")
                if userview.img_download:
                    print("Les images de couvertures sont enregistrées dans le dossier Data" + "\\" +
                          category.names_categories[userview.index] + ".")
                print("\nTemps de traitement : " + str(now_delta)[:7])

        except KeyboardInterrupt:
            print("\n\nFin du script par l'utilisateur.\n")
