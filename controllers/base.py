from models.category import Category
from views.user import UserView
from controllers.csv_file import CSV


class Controller:
    """ Main controller """
    def start_scraping(self):
        """ launch all necessary method to scrape the website """
        category = Category()
        category.names()
        category.urls_cats()
        categories = category.categories

        csv = CSV()

        userview = UserView()
        userview.prompt_for_category(categories)
        userview.prompt_for_img_download()

        if userview.cat_choice.upper() == "T":
            for category in categories:
                csv.recording(category)
        else:
            csv.recording(categories[userview.index])
