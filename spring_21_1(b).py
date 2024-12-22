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


