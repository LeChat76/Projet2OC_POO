from models.category import Category
from views.user import UserView
from controllers.csv_file import CSV


class Controller:
    """ Main controller """

    def __init__(self):
        self.download_img = ""
    def start_scraping(self):
        """ launch all necessary method to scrape the website """
        category = Category()
        category.get_names_cat()
        category.get_urls_cats()
        categories = category.names_categories

        userview = UserView()
        userview.prompt_for_category(categories)
        userview.prompt_for_img_download()
        self.download_img = userview.img_download

        if userview.cat_choice.upper() == "T":
            for category in categories:
                csv = CSV(category)
                csv.recording()
        else:
            csv = CSV(categories[userview.index])
            csv.recording()
