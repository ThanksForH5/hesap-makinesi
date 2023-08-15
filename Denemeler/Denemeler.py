print("**islemlerin** \n 1.Toplama\n 2.Cikarman\n 3.Bolme\n 4.Carpma\n q Cikis")

while True:
    soru = input("Yapmak istedigin islemi sec: ")
    
    if soru == "q":
        print("C")
        break  # Sonsuz döngüden çýkýþ yap
        
    soru = int(soru)  # Kullanýcýnýn girdiði iþlemi tamsayýya çevir
    
    if soru == 1:
        sayi3 = int(input("Lutfen Sayi 1. Sayiyi Gir: "))
        sayi4 = int(input("Lutfen Sayi 2. Sayiyi Gir: "))
        print("Toplam:", sayi3 + sayi4)
    if soru == 2:
        sayi5 = int(input("Lutfen Sayi 1. Sayiyi Gir: "))
        sayi6 = int(input("Lutfen Sayi 2. Sayiyi Gir: "))
        print("Toplam:", sayi5 - sayi6)
    if soru == 3:
        sayi7 = int(input("Lutfen Sayi 1. Sayiyi Gir: "))
        sayi8 = int(input("Lutfen Sayi 2. Sayiyi Gir: "))
        print("Toplam:", sayi7 // sayi8)
    if soru == 4:
        sayi9 = int(input("Lutfen Sayi 1. Sayiyi Gir: "))
        sayi10 = int(input("Lutfen Sayi 2. Sayiyi Gir: "))
        print("Toplam:", sayi9 * sayi10)

    else:
        print("Yanlis ifade girdiniz")


