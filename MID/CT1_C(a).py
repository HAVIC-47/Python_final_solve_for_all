my_list =[5,10,15,20,25,30,35,40,45]
a=my_list[1:8:3]
print(a)

b=my_list[-1:-4:-1]
print(b)
sum=0
for i in my_list:
    sum=sum+i
print(sum)
my_string="hello world"
c=my_string[6:11]
print(c)

numbers=[1,2,3,4,5,6,7,8,9,10,14]
even=0
odd=0
for i in numbers:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print(even)
print(odd)
if even>odd:
    print(" more even")   
else:
    print("more odd")