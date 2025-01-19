class Book:
    _is_checked_out = False
    
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
class Library:
    _books = []
    def add_book(self,book):
        if(book in self._books):
            print("The book already exists.")
        else:
            self._books.append(book)
    def check_out_book(self,title):
        pass
    def return_book(self,title):
        pass
    def list_available_books(self):
        if(self._books !=''): 
            print(self._books)