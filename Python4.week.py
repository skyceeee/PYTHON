"""
cumle=input("Lütfen bir cümle giriniz: ")
harf=input("Lütfen harfi giriniz: ")
#print(cumle.count(harf))
sayac=0
for i in cumle:
    if i==harf:sayac+=1

print(f"Cümledeki {harf} harfinin sayısı {sayac}")"""

"""
#-------------polindrom kelime-------------
cumle=input("Lütfen cümleyi giriniz.").lower()
harfler=set(cumle)
for harf in harfler:
    print(f"{harf} karakterinden {cumle.count(harf)}")"""
"""
kelime=input("Bir kelime giriniz: ").lower()
for i in range(0,len(kelime)//2):
    if kelime[i]!=kelime[len(kelime)-1-i]:
        print(f"{kelime} polindrom bir kelime değildir")
        break
else:print(f"{kelime} polindrom bir kelimedir.")

cumle=input("kelime giriniz:")
ters=cumle[::-1]
if cumle==ters:print(f"{cumle} polindromdur.")
else:print(f"{cumle} polindrom değildir.")"""

import random
"""
sayilar=[]
for i in range(0,50):
      sayilar.append(random.randint(1,100))
sayilar=[random.randint(1,100) for i in range(50)]
girilenSayi=int(input("lütfen 1-100 arası bir sayı giriniz:"))
print(f"random sayılar: {sayilar}")
ks=[]
bs=[]
for i in sayilar:
    if girilenSayi<i:bs.append(i)        
    else:ks.append(i)
print(f"Küçük sayılar: {ks}")
print(f"büyük sayılar: {bs}")"""

#-------------------------------------FONKSİYONLARRR--------------------------------------
#fonk içinde kullandığımız şeylere parametre denir.ex: def Topla(parametre1,parametre2) arguman:parametreli fonk parametre yerineyazdığımız değer.
#ex: Topla(3,4)
#Def komutu ile yazılır.
"""
def Mesaj():
    print("İlk fonksiyonum.")

Mesaj()
def Topla(parametre1,parametre2):
    topla=parametre1+parametre2
    print(topla)

Topla(4,7)"""
"""
#yıldız ile istediğimiz kadar departman ekleyebiliriz.
def DepartmanlariYaz(*departmanlar):
    for i,departman in enumerate(departmanlar):     
       print(f"{i+1}. departanımız: {departmanlar}")    
DepartmanlariYaz("Arge","Muhasabe")
DepartmanlariYaz("aa","bb","cc")
#bize tuple olarak döner
def DepartmanlariYaz(dep1,dep2,dep3):
    print(dep1,dep2,dep3)
DepartmanlariYaz(dep3="Muhasebe",dep2="Satış",dep1="Arge")
#** sözlük olarak tutuyor
def DepartmanlariYaz(**departmanlar):
    print(departmanlar)
DepartmanlariYaz(dep3="Muhasebe",dep2="Satış",dep1="Arge")"""
"""
def DaireAlanı(r,pi=3):
    print(pi*r**2)
#eğer kullanıcı değer verirse o değeri kullanır.vermezse bizim atadığımız pi değerini kullanır.
DaireAlanı(3)
DaireAlanı(3,3.14)

def TipiYaz(param):
    print(type(param))

TipiYaz("merhaba")
TipiYaz(5)
TipiYaz(True)
TipiYaz([2,6,8])
TipiYaz({1:"a",2:"b"})"""
#-----------------------------2.gün-----------------------------------
"""
def UsAl(taban,tavan):  
    return taban**tavan
x=int(input("Lütfen x sayısını giririniz:"))
#x**4+3*x**3+2*x**2
birinci=UsAl(x,4)
ikinci=UsAl(x,3)
ucuncu=UsAl(x,2)
print(birinci+3*ikinci+2*ucuncu)


def RandomList(kactane,baslangic,bitis):
    liste=[random.randint(baslangic,bitis) for i in range(kactane)]
    return liste

kacTane=int(input("Lütfen listeniz için eleman sayısı giriniz:"))
baslangic=int(input("Lütfen başlangıç değeri giriniz:"))
bitis=int(input("Lütfen bitis değeri giriniz:"))
liste=RandomList(kacTane,baslangic,bitis)
print(liste)

def listeOlustur():
    import random
    #listee=[random.randint(random.randint(1,40),random.randint(60,100)) for i in range(random.randint(1,100))]
    return  [random.randint(random.randint(1,40),random.randint(60,100)) for i in range(random.randint(1,100))]#listee
def ListeAnalizi(listee):  
    return max(listee),min(listee),len(listee)
liste=listeOlustur()
liste2=[2,4,6,8]
enb,enk,uzunluk=ListeAnalizi(liste)
#print(f"{liste} listesinin en büyük,en küçük ve eleman sayısı: {ListeAnalizi(liste)}") tuple olarak döner.
print(f"{liste} listesinin Uzunluğu: {uzunluk},maximum değeri: {enb},minimum:{enk}")"""


#---------------GLOBAL VE YEREL DEĞİŞKENLER--------------
#yerel değilken:bulunduğu yerde bulunduğu fonk geçerli.(şimdiye kadar bunları gördük)fonk içinde tanımlanır.
#global:tüm program tarafından tanınır.fonk dışında tanımlanır.ana programda tanımlayınca fonk içinde kullanılabilkiriz.
"""
def Topla():
    global a #eğer fonk içinde a da değişiklik yapmak istiyorsak onu fonk içinde gloal olarak tanımlamalıyız.
    a+=1
    print(a+b)
a=5
b=6
Topla()
print(a+b)"""


"""
def MesajYaz(girdi):
    print(girdi)
MesajYaz(input("Lütfen mesajı giriniz:))"""




"""
def Hesapla(sayi1,sayi2):
    return sayi1**2-sayi2**2
sayi11=int(input("Sayı 1:"))
sayi22=int(input("Sayi 2:"))
print(f"Girilen sayıların karelerinin farkları: {Hesapla(sayi11,sayi22)}")"""


"""
liste=[random.randint(1,200) for i in range(50)]
print(liste)
birBasamakli=[]
ikiBasamakli=[]
ucBasamakli=[]
for i in liste:
    if(i<10):
        birBasamakli.append(i)
        i+=1
    elif(i<100):
        ikiBasamakli.append(i)
        i+=1
    else:
        ucBasamakli.append(i)
        i+=1
    

print(f"Bir basamaklı sayılar: {birBasamakli}, iki basamaklı sayılar: {ikiBasamakli},üç basamaklı sayılar: {ucBasamakli}")"""

"""
dizi=[random.randint(1,100)for i in range(50)]
print(dizi)
yeniDizi=[(dizi[0]+dizi[1])/2,(dizi[2]+dizi[3])/2]
print(yeniDizi)

dizi=[10,11,9,12,8,10,10,10]
count=0
toplam=0

for i in dizi:
    toplam+=i
ortalama=toplam/len(dizi)
for i in dizi: 
    if(i==ortalama):
        count+=1      
print(f"{dizi} dizisinin ortalaması {ortalama}'dır.Tekrar sayısı: {count}")"""
"""
def KombinasyonHesapla(n,r):
    a,x,y=1
    for i in range(n,1,-1):x*=i
    for i in range(r,1,-1): y*=i
    for i in range(n-r,1,-1): a*=i   
    return x/(y*a)
print(KombinasyonHesapla(4,2))"""

"""
def Fibo(terim):
    fib=[]
    fib.append(1)
    fib.append(1)
    for i in range(2,terim):
        fib.append(fib[i-2]+fib[i-1])
    return  fib

terimSayisi=int(input("Lütfen fibonacci sayıları için terim sayısı giriniz:"))
print(Fibo(terimSayisi))"""

"""
def KombinasyonHesapla(sayi):
    x=1
    for i in range(sayi,1,-1):x*=i
    return x
n=int(input("Lütfen kombinasyon işlemi için n sayısını giriniz:"))
r=int(input("Lütfen kombinasyon işlemi için r sayısını giriniz:"))
işlem=KombinasyonHesapla(n)/(KombinasyonHesapla(n-r)*KombinasyonHesapla(r))
print(işlem)"""
"""
def CollatzDiziOlustur(sayi):
    dizi=[sayi]
    while sayi!=1:
        if sayi%2==0:
            dizi.append(sayi/2)
            sayi/=2
        else:
            dizi.append(3*sayi+1)
            sayi=sayi*3+1 
    return dizi  
baslangic=int(input("Lütfen bir başlangıç sayısı giriniz:"))
print(CollatzDiziOlustur(baslangic))"""

"""
def AsalCarpanlarıListele(sayi):
    print("Asal çarpanlar: ")
    for i in range(2,sayi+1):
        if sayi%i==0: 
            j=i   
            while(sayi%j==0):
                sayi/=j
            print(i)
sayii=int(input("Lütfen bir sayı giriniz: "))
print(AsalCarpanlarıListele(sayii))"""

"""
def sayiOnBireBolunuyorMu(sayi):
    elemanlar=[]
    tekToplam=0
    ciftToplam=0
    sayii=sayi
    while sayii>0:
        elemanlar.append(sayii%10)
        sayii//=10
    for i in elemanlar:
        if(i%2==0):
            ciftToplam+=elemanlar[i]
        else:
            tekToplam+=elemanlar[i]
    if((ciftToplam-tekToplam)/11==0):
        print(f"{sayi} sayısı 11'e tam bölünür.")
    else:
        print(tekToplam)
        print(f"{sayi} sayısı 11'e tam bölünmez.")
        

sayi1=int(input("Lütfen bir sayı giriniz:"))
sayiOnBireBolunuyorMu(sayi1) """
