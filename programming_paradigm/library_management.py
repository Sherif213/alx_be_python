class Book:
    _is_checked_out = False
    
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
class Library:
    _books = []
    def __init__(self):
        pass
    def add_book(self,book):
        if(book in self._books):
            print("The book already exists.")
        else:
            self._books.append(book)
    def check_out_book(self,title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = True
    def return_book(self,title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = False
    def list_available_books(self):
        if(self._books !=''): 
            for book in self._books:
                if book._is_checked_out == False:
                    print(f"{book.title} by {book.author}")
            
    