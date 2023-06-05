"""a=int(input("Lütfen a sayısını  giriniz: "))
b=int(input("Lütfen b sayısını giriniz: "))
print(f"Girilen {a}, {b} sayısının toplamı: {a+b},farkı :{a-b},çarpımı: {a*b},bölümü: {a/b}, tam bölümü: {a//b},modu: {a%b} ve üssü: {a**b}'dir.")"""



"""------------------#KARŞILAŞTIRMA OPERATÖRLERİ-----------------
#== eşit midir
#!= farklı mıdır
sayi1=5
sayi2=5
sayi3=5
sayi1==sayi2==sayi3
#birden fazla karşılaştırma yapılabilir
sayi1=12
sayi2=15
sayi3=17
sayi1<sayi2<sayi3

a,b,c=5,6,7
#a=5,b=6,c=7 ile aynı"""



#---------------------MANTIKSAL OPERATÖRLER(and ,or, not)-----------------------------
#7>2 and "merhaba"=="merhaba" and 5>17 sonucu False   not(7>5) cevabı False


#********************If-Elif-Else*************************
#pyhton biçimsel bir dil.Kodlar aynı hizada yazılır.Özellikle : olduğunda
"""a,b=5,12
if a>b:
    print(f"{a} sayısı {b} sayısından büyüktür.")
else:
    print(f"b büyüktür a'dan")"""


"""sayi=int(input("Lütfen bir sayı giriniz: "))
if sayi>0:
    input("Sayı pozitiftir.")
elif sayi==0:
    print("Sayı sıfırdır.")
else:
    print("Sayı negatiftir.")
#kısa yazımı
#sadece if ve else ile kullanabiliriz.elif kullanılmıyor(bu yazımda)
print("Sayı pozitiftir...")if sayi>=0 else print("Sayı negatiftir...")"""


"""sayi=int(input("Lütfen bir sayı giriniz: "))
print("Sayı çifttir.") if sayi%2==0 or sayi==0 else print("Sayı tektir.")"""


"""while True:
 sayi1=int(input("Lütfen 1. sayıyı giriniz:"))
 sayi2=int(input("Lütfen 2.sayıyı giriniz: "))
 sayi3=int(input("Lütfen 3.sayıyı giriniz: "))
 if sayi1> sayi2 and sayi1>sayi3 :
    print(f"En büyük sayı:{sayi1}")
 elif sayi2>sayi1 and sayi2>sayi3:
    print(f"En büyük sayı:{sayi2}")    
 else:
    print(f"En büyük sayı:{sayi3}")"""


"""import random
oyunSayisi=random.randint(1,100)
while True:
    tahmin=int(input("Lütfen 1-100 arasında tahmininizi giriniz: "))
    if tahmin > oyunSayisi:
        print("tahmininiz oyun sayısından büyüktür.")
    elif tahmin< oyunSayisi:
        print("Tahmininiz oyun sayısından küçüktür.")
    else:
        print(f"Tebrikler.Oyunuz kazandınız.Sayı: {oyunSayisi}")  
        break"""


"""
while True:
    vize=int(input("Vize notunu giriniz:"))
    final=int(input("Final notunu giriniz: "))
    if 0<=vize<=100 and 0<=final<=100:break     
    else:print("Lütfen geçerli bir not giriniz")       
ortalama=(vize*0.3)+(final*0.7)
print("Not ortalamanız: ",ortalama)
if ortalama<50:print("Harf notunuz: F.Kaldınız")
elif  ortalama<70:print("harf notunuz: C")       
elif ortalama<90:print("Harf notunuz: B.")
else:print("Harf notunuz : A")"""
      
    #**********************2.DERS************************


"""
for sayi in range(1000,10000):
    ilkIki=sayi//100
    sonIki=sayi%100
    if sayi==(ilkIki+sonIki)**2:print(sayi) """


"""SORUNLU
for sayi in range(1000,10000):
    strSayi=str(sayi)
    ilkIki=int(strSayi[0]+strSayi[1])
    sonIki=int(strSayi[strSayi.__len__-1]+strSayi[strSayi.__len__])
    if sayi==(ilkIki+sonIki)**2:print(sayi)"""


    #*****************DÖNGÜLER*****************
    #for ve in standart 1.parametre kaçtan başladığı,2. parametre kaçtan bittiği(dahil değil ör.101),3.parametre artış miktarı for i in range(başlangıç,bitiş,artış miktrı)
"""for i in range(1,101,1):
    print(f"{i}.kez Merhaba")"""

"""
isim=input("Lütfen isminizi giriniz: ")
baslangiçDegeri=int(input("Lütfen başgangıç değerinizi giriniz:"))
bitisDegeri=int(input("Lütfen bitiş değerini giriniz: "))
for i in range(baslangiçDegeri,bitisDegeri+1): print(f"{i}.kez"+ isim)
isim="Gökçe"
for i in range(100,0,-1):print(f"{i}.kez "+isim)
#*************** ÖNEMLİ ,JAVADAN FARKLIIII**********(Bir string ifadeyi array olarak forun içine yazabiliriz.)
isim="Elginkan"
for i in isim:
    print(i)"""

#--------------------DÖNGÜLEER---------------
#-pass-Görevi hiçbir şey yapmamak.
#-continue-İçinde bulunduğu ifadeyi durdurur ve sonrakine geçmesinii sağlar.
#-break-durdurur,sonlandırır.
"""
for i in range(1,101,1):
    if i%2==0:continue
    print(i)"""
"""
sayi=int(input("Lütfen bir sayı giriniz."))
toplam=0
for i in range(1,sayi+1,1):
    toplam+=i
    print(i)
print(toplam)

for i in range(1,10):
    for j in range(1,10):
        print(f"i={i},j={j}")

for i in range (1,10):
    print("----------")
    for j in range(1,10):
        print(f"{i}*{j}={i*j}")
#başlangıç değerini yazarız ilk.while koşul döndürür.
i=1
while i<=100:
    print(f"{i}.kez Gök")
    i+=1
#sonsuz döngü while ile sağlanır. while True:    """

"""
sayi=int(input("lütfen bir sayı giriniz: "))
toplam=0
i=1
j=1
while i<=sayi:
    if i%2==0:
        toplam+=i
        print(f"{j}.sayı: {i}")
        j+=1
    i+=1 

print(f"Toplam: {toplam}")"""




sinirSayisi=int(input("Lütfen bir sınır sayısı giriniz:"))
asalToplam=0
toplam=0
bolen=2
for i in range(1,sinirSayisi+1):
   
    while i>0:
        rakam=i//10
        toplam+=rakam
        i//=10
    while i>bolen:
        counter=0
        if i%bolen==0:
            asalToplam+=bolen
            i/=bolen
        else:
            bolen+=1
    if asalToplam==toplam:print(i)













        












    



