from models.category import Category
from views.user import UserView
from controllers.csv import CSV

class Controller:
    """ Main controller """
    def start_scraping(self):
        """ launch all necessary method to scrape the web site """
        category = Category()
        """ list all names of all categories """
        category.names()
        categories = category.categories
        """ list all URL for ONE category """
        category.urls_cat()
        urls_cat = category.urls_categories

        csv = CSV()

        userview = UserView(categories)

        userview.prompt_for_category()
        userview.prompt_for_img_download()

        if userview.cat_choice.upper() == "T":
            for url in urls_cat:
                csv.recording(url)
        else:
            csv.recording(urls_cat[userview.index])
