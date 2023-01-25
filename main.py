from models.books import Book
from models.category import Category


def main():
    #book = Book("https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html")
    #book.get_product_info()

    #print(book.image_url)

    category = Category()
    category.create_list_url_category(category)



if __name__ == "__main__":
    main()
