def jog_ar_gun_korbo(a,b,c):
     jog_korbo=a+b+c
     gun_korbo=a*b*c
     return jog_korbo,gun_korbo

a=int(input("'a' er man ta bolen: "))
b=int(input("'b' er man ta bolen: "))
c=int(input("'c' er man ta bolen: "))

jog_ar_gun_kore_pai=jog_ar_gun_korbo(a,b,c)
gun_kore_pai=jog_ar_gun_korbo(a,b,c)
print("jog_ar_gun_kore_paisi : ", jog_ar_gun_kore_pai)


# ii

jog_lambda=lambda a,b,c: (a+b+c)
gun_lambda=lambda a,b,c: (a*b*c)
print("jog_lambda : ", jog_lambda(a,b,c))
print("gun_lambda : ", gun_lambda(a,b,c)) 

vag_lambda= lambda a,d: (a/b)
print("vag_lambda : ", vag_lambda(a,b))

odd_even_lambda= lambda a: "even" if a%2 ==0 else "odd"
print("odd_even_lambda : ", odd_even_lambda(a))


boro_choto_lambda = lambda a: "up dosh "if a>10  else "bellow dosh"
print("boro ma choto  :", boro_choto_lambda(a))

b_choto=lambda b : "b boro" if b>10  else "b choto"
print(b_choto(b))

loop_korbe= lambda a: "done" 
for i in range(a):
     print ("ami valo")
print(loop_korbe(a))
