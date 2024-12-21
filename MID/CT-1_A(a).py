n= int(input("Enter a number: "))
numbers=[]

for i in range(n):
     element= int(input("Enter a number: "))
     numbers.append(element)

avarage=sum(numbers)/len(numbers)
print(avarage)

quique_numbers= list(set(numbers))
print(quique_numbers)