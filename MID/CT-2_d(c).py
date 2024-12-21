def string_formatter(str1, str2,op):
     if op=="combine":
          return str1+str2
     if op== "upper":
          return str1.upper()+str2.upper()
     if op=="lower":
          return str1.lower()+str2.lower()
     if op== "reverse":
          return str1[::-1]+str2[::-1]
     
print(string_formatter("hello","world","combine"))

def delete_contact(contact_book, name,phone_number):
     for key in contact_book.keys():
          if key== name and contact_book[key]==phone_number:
               del contact_book[key]
               return contact_book
     return "the phone number does not exist"

contact_book = {
    "Alice": "123",
    "Bob": "987"
}

print(delete_contact(contact_book, "Alice", "123"))