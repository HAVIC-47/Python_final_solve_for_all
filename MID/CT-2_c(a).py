def fibonacci_series(n):
     list=[0,1]
     for i in range(n-2):
          element=list[-1]+list[-2]
          list.append(element)
     return list

print(fibonacci_series(6))

def add_book(library_inventory,title, status):
     for key in library_inventory.keys():
          if key== title:
               library_inventory[key]=status
               return library_inventory
     library_inventory[title]=status
     return library_inventory
library_inventory = {
"The Great Gatsby": "available",
"To Kill a Mockingbird": "checked out"
}
add_book(library_inventory, "1984" , "available")
add_book(library_inventory, "The Great Gatsby" , "c ut")

print(library_inventory)