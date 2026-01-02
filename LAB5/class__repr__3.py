'''
Docstring for LAB5.class__repr__3
Create a class with a meaningful __repr__. Create a class where __repr__ returns 
a string that could realistically recreate the object.
'''
class Book:
    def __init__(self, title, author, YOP):
        self.title = title
        self.author = author
        self.YOP = YOP

    def __repr__(self):
        return f'Book {self.title} written by author {self.author} published in year {self.YOP}'
    
book1 = Book("Pippi Langstrump",'Astrid Lindgren',1945)
book2 = Book('The Little Prince','Antoine de Saint',1943)
print(repr(book1))
print(repr(book2))
# re_book = eval(repr(book2))
# print(re_book.title)