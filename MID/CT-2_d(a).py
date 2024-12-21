def simple_calcilator(a,b,op):
     if op=="+":
          return a+b
     elif op=="-":
          return a-b
     elif op=="*":
          return a*b
     elif op=="/":
          return a/b

print(simple_calcilator(5,3,"+"))

def count_item_frequency(list):
     frequency={}
     for i in list:
          if i in frequency:
               frequency[i]+=1
          else:
               frequency[i]=1
     return frequency
items = ["apple", "banana", "apple", "orange", "banana", "banana"]

print(count_item_frequency(items))