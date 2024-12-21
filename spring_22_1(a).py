def highest_odd_index(lst):
     odd=[]

     for i in range(len(lst)):
         if i%2!=0:
             odd.append(lst[i])

     boro= max(odd)
     print(boro)

lst=[1,2,3,40,5,6,7,8,9,10]
highest_odd_index(lst) 