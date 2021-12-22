# create the class for book
class Book():
    favs = []

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    # create a class method to check if the current book
    # is less than 100pages
    def is_short(self):
        if (self.pages < 100):
            return True
    
    # case where an object is passed to print
    def __str__(self):
        return f"{self.title}, {self.pages} pages long"
    