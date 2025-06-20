class DigitalLibrary:
    def __init__(self):
        self.books_collection = []

    def insert_book(self, title, author):
        self.books_collection.append({"title": title, "author": author, "is_available": True})
        print(f"'{title}' by {author} has been added to the library.")

    def lend_book(self, title):
        for book in self.books_collection:
            if book["title"] == title:
                if book["is_available"]:
                    book["is_available"] = False
                    print(f"You have successfully borrowed '{title}'.")
                    return
                else:
                    print(f"Sorry, '{title}' is currently checked out.")
                    return
        print(f"Sorry, the book '{title}' does not exist in our records.")

    def list_available_books(self):
        return [book for book in self.books_collection if book["is_available"]]

# Usage
my_library = DigitalLibrary()
my_library.insert_book("Machine Learning Basics", "Anjali Rao")
my_library.insert_book("Artificial Intelligence", "Rajesh Kumar")

my_library.lend_book("Machine Learning Basics")
print("Available Books:", my_library.list_available_books())
