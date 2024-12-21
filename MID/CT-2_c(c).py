def tribonacchi_series(n):
     list=[0,1,1]
     for i in range(n-3):
          element= list[-1]+list[-2]+list[-3]
          list.append(element)
     return list
print(tribonacchi_series(10))

def add_contact(contact_book, name, phone_number):
     for key in contact_book.keys():
          if key== name:
               contact_book[key]=phone_number
               return contact_book
     contact_book[name]=phone_number
     return contact_book

contact_book = {
    "Alice": "123",
    "Bob": "987"
}
print(add_contact(contact_book, "Charlie", "555"))
print(add_contact(contact_book, "Alice", "111"))