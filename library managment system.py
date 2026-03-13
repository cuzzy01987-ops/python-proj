# library managment system

# library managment system
 
class Library:
     def __init__(self, name):
         self.name = name
         self.books = []
         
     def add_book(self, book):
         self.books.append(book)
         print(f'Book "{book}" added to the library.')
         
         
     def remove_book(self):
         if book in self.books:
             self.books.remove(book)
             print(f"book {book} removed from library")
         else:
            print(f'Book "{book}" not found in the library.') 
        

  
   







     def list_books(self):
         if self.books:
             print("Books in the library:")
             for book in self.books:
                 print(f'- {book}')
         else:
             print("No books in the library.")
             
     def borrow_book(self, book):
                 if book in self.books:
                     self.books.remove(book)
                     print(f'You have borrowed "{book}".')
                 else:
                     print(f'Book "{book}" is not available for borrowing.')
     def return_book(self, book):
         self.books.append(book)
         print(f'You have returned "{book}".')
         

lib1 = Library("City Library")
lib2 = Library("Community Library")
lib3 = Library("University Library")

lib1.add_book("1984 by George Orwell")
lib1.add_book("To Kill a Mockingbird by Harper Lee")
lib1.add_book("The Great Gatsby by F. Scott Fitzgerald")

lib2.add_book("Jane Eyre by Charlotte Brontë")
lib2.add_book("Pride and Prejudice by Jane Austen")
lib2.add_book("Wuthering Heights by Emily Brontë")
lib2.add_book("The Catcher in the Rye by J.D. Salinger")

lib3.add_book("Introduction to Algorithms by Cormen, Leiserson, Rivest, and Stein")
lib3.add_book("Artificial Intelligence: A Modern Approach by Stuart Russell and Peter Norvig")
lib3.add_book("Database System Concepts by Silberschatz, Korth, and Sudarshan")




lib1.return_book("1984 by George Orwell")
lib1.borrow_book("1984 by George Orwell")


lib2.borrow_book("Pride and Prejudice by Jane Austen")
lib2.return_book("Pride and Prejudice by Jane Austen")

lib2.list_books()
lib3.list_books()
lib1.list_books()






    