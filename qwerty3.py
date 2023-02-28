#Soru 20

sayi= int(input("Lutfen bir sayi giriniz:"))
tekToplam=0
ciftToplam=0
for i in range(1,sayi):
    if (i%2==0):
        ciftToplam+=i
    else:
        tekToplam+=i
print("{0} ile {1} arasindaki tek sayilarin toplami: {2}" .format(1,sayi,tekToplam))
print("{0} ile {1} arasindaki cift sayilarin toplami: {2}" .format(1,sayi,ciftToplam))


