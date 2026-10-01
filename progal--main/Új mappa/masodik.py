evszam = int(input("mejik evben szuletel "))

print(evszam)

kor =  2026 - evszam 


print(kor,"éves vagy ")
if 18 < kor: 
    print("felnöt")

elif kor == 18 :
   print("gratulálok")

else : print("gerek vagy")

x = int(input("elsőszám"))
y = int(input("második szám"))
z = int(input("harmadik szám"))
at = (x + y + z) / 3

print(at)


if at == 5 :
 print("kitűnő ") 
elif at >= 3 :
   print("átmentél")
elif at >= 2 :
   print("majdnem ")
else :
 print( "nemsikerült")
 if at >=2 :
    print("átmentél")
 