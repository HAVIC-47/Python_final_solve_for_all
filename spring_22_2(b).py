# method overloading using multipledispatch
from multipledispatch import dispatch

class calculator:
     @dispatch(int,int)
     def jog_korbo(self, num1,num2):
          return num1+num2
     @dispatch(int,int,int)
     def jog_korbo(self, num1,num2,num3):
          return num1+num2+num3
     
     @dispatch(int,int,int,int)
     def jog_korbo(self, num1,num2,num3,num4):
          return num1+num2+num3+num4
     
     @dispatch(float,float)
     def jog_korbo(self, num1,num2):
          return num1+num2
     
c1=calculator()
c1.jog_korbo(2,3)
c1.jog_korbo(2,3,4)
c1.jog_korbo(2,3,4,5)
c1.jog_korbo(2.5,3.5)

# Method Overriding
class ami:
     def pora_pari(self):
          return("ami pora pari na")
     
class amar_bondhu(ami):
     def pora_pari(self):
          return("amar bondhu pora pare")\
          
class sharif_bolod(ami):
     def pora_pari(self):
          return("sharif bolod")
     
faisal=ami()
nusaiba=amar_bondhu()
sharif=sharif_bolod()


print(faisal.pora_pari())
print(nusaiba.pora_pari())
print(sharif.pora_pari())