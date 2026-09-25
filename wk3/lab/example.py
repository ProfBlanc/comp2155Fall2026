"""
Create multiple classes
    Book
    EBook based on Book
    AudioBook   based on Book
    Library
        store multiple books (reg, ebook, audiobook)
Work with static & class methods
"""
# create the class headers for each of the 3 classes
# type DONE when finished
# class header? first line when declaring a class
# book constructor: title, author, num_pages
# Ebook constructor: above 3 + file_size
# Audiobook constructor: above 3 + total_time

# create methods that refer to 1 or many properties/attributes of class
class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def is_long_book(self):
        return self.num_pages >= 200

    # static method is a method declared inside class
    # but has no access to an instance of the object properties
    # why create? this method belongs to this class
    @staticmethod
    def is_valid_release_year(year):
        import datetime
        this_year = datetime.datetime.now().year
        return year >= this_year - 100 and year <= this_year + 1
    def __str__(self):
        return f"Title={self.title}, Author={self.author}, NumPages={self.num_pages}"

class EBook(Book):
    def __init__(self, title, author, num_pages, file_size):
        super().__init__(title, author, num_pages)
        self.file_size = file_size
    def is_heavy_file(self):
        return self.file_size > 2048

    @classmethod
    def convert_book_to_ebook(cls, book: Book):
        if not type(book) == Book:
            raise TypeError("Book must be of type Book")
        return cls(title=book.title,
                   author=book.author,
                   num_pages=book.num_pages,
                   file_size= book.num_pages * 10 # every book page is 10kb file size
                   )

    def __str__(self):
        return super().__str__() + f", File Size={self.file_size}"

class AudioBook(Book):
    def __init__(self, title, author, num_pages,total_time ):
        super().__init__(title, author, num_pages)
        self.total_time = total_time
    # create a method that evaluates an audiobook
    # name is is_lengthly => total time is greater than a specified value
    # type done when finished
    def is_lengthy(self, minutes, hours):
        return self.total_time > 60 * minutes * hours # 3 hours

    # in AudioBook, create a classmethod that converts a book to an audiobook
    # in AudioBook, create any static method of your choice
    @classmethod
    def convert_book_to_audiobook(cls, book: Book):
        if not type(book) == Book:
            raise TypeError("Book must be of type Book")

        return cls(title=book.title,
                   author=book.author, num_pages=book.num_pages,
                   total_time= book.num_pages * 30
                   )
    @staticmethod
    def is_english_language_supported(languages: list[str]):
        return "english" in languages
    def __str__(self):
        return super().__str__() + f", Total Time={self.total_time}"


# Bonus: create a class named Library
# store inventory of {books: [list of books], ebook: [list of ebook],
# audiobook: [list of audio book]}

class Library:
    def __init__(self, name):
        self.name = name
        self.__inventory_keys = "Book,EBook,AudioBook".split(",")
        self.__inventory = {
            self.__inventory_keys[0]: [],
            self.__inventory_keys[1]: [],
            self.__inventory_keys[2]: []
        }
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self.__name = value
        else:
            raise ValueError("Invalid Name")
    def add_item_to_inventory(self, item: Book | EBook | AudioBook):
        item_type = self.__inventory_keys[0]
        if type(item) == EBook:
            item_type = self.__inventory_keys[1]
        elif type(item) == AudioBook:
            item_type = self.__inventory_keys[2]

        self.__inventory[item_type].append(item)
    def display_inventory(self):
        for key, value in self.__inventory.items():
            print("Category", key, "has", len(value), "value(s)")
            for book in value:
                print(book, sep=",")
            print()


def main():
    example2()

def example2():
    library = Library(name="Our Lib")

    library.add_item_to_inventory(Book("Book 1", "Author 1", 100))
    library.add_item_to_inventory(Book("Book 2", "Author 2", 150))
    library.add_item_to_inventory(EBook("Book 3", "Author 3", 180, file_size=1024))
    library.add_item_to_inventory(AudioBook("Book 4", "Author 4", 200, total_time=3600))

    library.display_inventory()

def example1():
    print(Book.is_valid_release_year(2026))
    b1 = Book("Title", "Author", 100)
    eb1 = EBook.convert_book_to_ebook(b1)
    print(eb1.file_size)

if __name__ == '__main__':
    main()