""""
#soru13

for i in range(1,101):
    if (i%2==1):
        print(i)
        
"""

"""

#Soru 14

for i in range(1,101):
    if i%3==0 or i%5==0:
        print(i)
"""

"""
#Soru 15

sayi= int(input("Sayi giriniz?"))
for i in range(1,int(sayi)+1):
    print(i)
"""

"""
#Soru 16

uzunkenar= int(input("Lutfen dikdortgenin uzun kenarini giriniz="))

kisakenar= int(input("Lutfen dikdortgenin kisa kenarini giriniz="))

alan= uzunkenar*kisakenar

cevre= 2*(uzunkenar + kisakenar)

print("Dikdortgenin alani=", alan , "Cevresi=", cevre)

"""
"""
#Soru 17

isim= input("Lutfen adinizi giriniz:")
sayac=0
while sayac < len(isim):
    print(isim[sayac])
    sayac += 1
"""
"""
#Soru 18

toplam=0

sayi1= int(input("Birinci sayiyi giriniz:"))
sayi2= int(input("Ikinci sayiyi giriniz."))
for i in range ((sayi1)+1, sayi2):
    toplam+=i
print("{0} ile {1} arasindaki sayilarin toplami: {2}" .format(sayi1,sayi2,toplam))

"""

"""
#Soru 19

sayac=0
sayi= int(input("Lutfen bir sayi giriniz:"))
for i in range(2,sayi):
    if sayi%i==0:
        sayac+=1
        break
if sayac==0:
    print("Sayiniz asal!")
else:
    print("Sayiniz asal degil.")

"""
#Soru 20

sayi= int(input("Lutfen bir sayi giriniz:"))
tekToplam=0
ciftToplam=0
for i in range(1,sayi):
    if (i%2==0):
        ciftToplam+=i
    else:
        tekToplam+=1
print("{0} ile {1} arasindaki tek sayilarin toplami: {2}" .format(1,sayi,tekToplam))
print("{3} ile {4} arasindaki cift sayilarin toplami: {5}" .format(1,sayi,ciftToplam))

