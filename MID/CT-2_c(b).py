def lucas_series(n):
     list=[2,1]
     for i in range(n-2):
          element=list[-1]+list[-2]
          list.append(element)
     return list
print(lucas_series(10))

def update_price(product_catalog, product, price):
     for key in product_catalog.keys():
          if key== product:
               product_catalog[key]=price
               return product_catalog
     product_catalog[product]=price
     return product_catalog
product_catalog = {

"Laptop": "$999",

"Smartphone": "$699"
}

update_price(product_catalog, "Tablet" , "$299")
update_price(product_catalog, "Laptop" , "$1099")

print(product_catalog)