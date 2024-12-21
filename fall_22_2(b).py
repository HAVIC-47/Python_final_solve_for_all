def primecheck(n):
     if n<2:
          return False
     for i in range(2, int(n**0.5)+1):
          if n%i==0:
               return False
          
     return True


def multiplacationtable(n):
     for i in range(1,11):
          print(f"{n}X{i}={n*i}")


m=int(input("enter a integer number :"))

if primecheck(m):
     print(f"{m} is a prime number. Here is its multiplication table:")
     multiplacationtable(m)

else:
     print(f"{m} in not a prime number")