from abc import ABC, abstractclassmethod
class liratyItem(ABC):
     def __init__(self, title,author, publication_date):
          self.title =title
          self.author= author
          self.publication_date=publication_date

     @abstractclassmethod
     def display_details(self):
          pass        

     def borrow(self):
          print(f"the item '{self.title}' has been borrowed")
     
     def return_item(self):
          print(f"the item '{self.title}' has been returned ")

class Book(liratyItem):
     def __init__(self, title, author, publication_date, isbn):
          super().__init__(title, author, publication_date)
          self.isbn=isbn

     def display_details(self):
          print(f"Book Details:\nTitle: {self.title}\nAuthor: {self.author}\nPublication Date: {self.publication_date}\nISBN: {self.isbn}")

class Magazine(liratyItem):
     def __init__(self, title, author, publication_date, issue_no):
          super().__init__(title, author, publication_date)
          self.issue_no=issue_no

     def display_details(self):
          print(f"Magazine Details:\nTitle: {self.title}\nAuthor: {self.author}\nPublication Date: {self.publication_date}\nIssue No: {self.issue_no}")

book=Book("amar boi","ami","2024","1234")
magazine=Magazine("amar mage", "ami","2021", "5678")

book.display_details()
book.borrow()
book.return_item()

magazine.display_details()
magazine.borrow()
magazine.return_item()

