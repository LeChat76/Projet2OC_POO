from models.category import Category
from views.user import UserView
from controllers.csv_file import CSV
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
            categories = category.names_categories

            userview = UserView()
            userview.prompt_for_category(categories)
            userview.prompt_for_img_download()
            img_download = userview.img_download

            now_begin = datetime.datetime.now()
            now_end = ""
            if userview.cat_choice.upper() == "T":
                for category in categories:
                    csv = CSV(category, img_download)
                    csv.recording()
                    now_end = datetime.datetime.now()
                now_delta = now_end - now_begin
                print("Fin de l'extraction, vous pouvez consulter les fichiers CSVs horodatés à la date du jour dans le"
                      " dossier \\Data\\CSVs.")
                if img_download.upper() == "Y":
                    print("Les images de couvertures sont enregistrées dans chaque dossiers nommés de leurs catégories"
                          ".")
                print("\nTemps de traitement : " + str(now_delta)[:7])
            else:
                csv = CSV(categories[userview.index], img_download)
                csv.recording()
                now_end = datetime.datetime.now()
                now_delta = now_end - now_begin
                print("Fin de l'extraction, vous pouvez consulter le fichiers CSV horodaté à la date du jour dans le "
                      "dossier \\Data\\CSVs.")
                if img_download.upper() == "Y":
                    print("Les images de couvertures sont enregistrées dans le dossier Data" + "\\" +
                          categories[userview.index] + ".")
                print("\nTemps de traitement : " + str(now_delta)[:7])

        except KeyboardInterrupt:
            print("\n\nFin du script par l'utilisateur.\n")
