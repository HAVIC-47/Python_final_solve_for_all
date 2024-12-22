n= int(input("enter an integer:" ))

sum = 0
for i in range(n):
    sum += i

print(sum)

mul=1
i=1
while i<=n:
    mul*=i
    i+=1

print(mul)

if n%2==0:
     print("even")  
else:
     print("odd")
