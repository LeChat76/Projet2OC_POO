""" Base view """


class UserView:
    """ User view """

    def __init__(self):
        self.img_download = False
        self.cat_choice = ""
        self.categories_names = ""
        self.index = ""

    def prompt_for_category(self, categories_names):
        """ Prompt for category to scrape"""
        self.cat_choice = ""
        self.categories_names = categories_names
        self.index = -1

        while self.cat_choice.upper() != "S" and self.cat_choice.upper() != "T":
            self.index += 1
            self.cat_choice = input("Analyser catégorie " + self.categories_names[self.index]
                                    + " ([ENTER] pour suivante, (s)electionner celle ci ou (t)outes)?")

            """ if all categories listed, back to the first + warning """
            if self.index + 1 == len(self.categories_names):
                print("\nVous avez fait le tour de toutes les categories, retour à la première!\n")
                self.index = -1

    def prompt_for_img_download(self):
        """prompt user for download image or not (for speed scraping) """
        download_pic = " "
        while download_pic.upper() != "Y" and download_pic.upper() != "N" and download_pic != "":
            download_pic = input("Télécharger les images? (Y/n) ")
            if download_pic == "" or download_pic.upper() == "Y":
                self.img_download = True
