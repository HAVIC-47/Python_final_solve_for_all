shal= int(input("shal ta bolen vai: "))

def nested_boro_bosor_naki(shal):
     if shal%4 ==0:
          if shal%100!=0 or shal%400==0:
               return True
          else:
               return False
     else:
          return False

print("nested diya korsi vai : " ,nested_boro_bosor_naki(shal))

def onek_condition_diya_shal_boro(shal):
     if shal%4 ==0 and (shal%100!=0 or shal%400==0):
          return True
     else:
          return False
     
print("onek condition diya korsi vai : " ,onek_condition_diya_shal_boro(shal))

def choto_kore_shal_boro(shal):
     return shal%4 ==0 and (shal%100!=0 or shal%400==0)

print("choto kore korsi vai : " ,choto_kore_shal_boro(shal))