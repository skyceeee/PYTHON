#---------------------------------------örnekler-------------------------------
"""
sayi=int(input("Lütfen bir sayı giriniz: "))
sayiAsalMi=True

for i in range(2,sayi//2+1):
     if sayi%i==0:
        print(f"{sayi} asal değildir.") 
        sayiAsalMi=False
        break
if sayiAsalMi==True:
    print(f"{sayi} asaldır.")"""

"""
sayi=int(input("Lütfen bir sınır sayısı giriniz: "))
tekToplam=0
ciftToplam=0
for i in range(1,sayi+1):
    if i%2==0:
        ciftToplam+=i
    else:
        tekToplam+=i

print(f"Tek sayıların toplamı: {tekToplam}")
print(f"Çift sayıların toplamı: {ciftToplam}")"""

"""
sayi=int(input("Sayi:"))
tt=0
ct=0
for i in range(1,sayi+1):
    ct+=i if i%2==0 else tt+=i"""
#----------------------------------------------------------------------------numpy methodu özel araştır yapay zekada kullanılacak
#---------LİSTE----------------------
"""
liste=[] boş  liste
liste=list()
liste=[1,2,3,4,5] ile oluşturulur.
liste[0] sıfırıncı elemanı getirir.
listenin elemanları aynı türde olmak zorunda değil.
liste[-1] sonn eleman liste[-2] sondan ikinci eleman

liste=[i for i in range(1,101)]
#1 den 100e kadar bir list5e oluşturur
liste=[0 for i in range(1,101)]
#100 tane 0 dan oluşan bir liste oluşturur
liste[kaçıncıindeksdenbaşlasın:kaçakadardevametsin:artışmiktarrı]

"""
"""
liste=["Fiat","Mazda","Wv","Toyota","Hyundai"]
print(liste[0:3:1])
#tamamını yazdırır
print(liste[:])
#2.indiksten başlayarak yazdırır
print(liste[2:])
#sondan yazdırır
print(liste[::-1])
#listenin uzunluğunu verir
print(len(liste))
#stringin uzunluğunu verir
print(len("Merhaba"))"""

#liste=["ahmet","mehmet","ali","yavuz","mecnun","leyla","ismail"]
"""
for i in range(0,len(liste)):
    print(f" Listenin {i}. elemanı {liste[i]}")
#python pratik yöntem
for isim in liste:
    print(isim)
#indeks numarası ve değer olarak döndürür
for index,isim in enumerate(liste):
    print(f"{index}.indeksin değeri={isim}")"""
"""
#listeye erdal eklendi
liste.append("erdal")
#1.indekse çağlar eklendi
liste.insert(1,"çağlar")
#değer değiştirme(1.indeksdeki eleman ozan olarak değiştirildi)
liste[1]="ozan"
#listeden son elemanı çıkarır indeks numarasına göre çıkarır
liste.pop()
#listeden ikinci indeksdeki elemanı çıkarır
liste.pop(2)
#listeden değere göre eleman çıkarır(mehmet listeden silindi.)
#liste.remove("mehmet")
#liste elemanlarını temizler
#liste.clear()
#listeyi tamamen siler ramden siler
#del liste
#liste.sort() alfabetik olarak listeyi sıralar(int ise küçük büyük olarak).liste.sort(reverse=True) listeyi sondan düzenler ex:z--a türkçe karakterleri sıralamaya eklemez
#liste farklı türden elemanlardan oluşuyırsa sıralama işlemi yapılmaz
#string olarak rakam verirsek ve isim de verirsek sıralama yapar
#count-----elemanın liste içine kaç tane yazıldığını sayar liste.count("ahmet")
"ozan" in liste
#listenin içinde ozan var mı
#extend ile iki listeyi birleştirebiliriz
"""
"""
liste1=[1,2,3,4,5]
liste2=[6,7,8,9,10]
#liste2yi liste 1e ekler
print(liste1.extend(liste2))"""
#-------liste eşitleme---- birine yapılan değişiklik diğerine de yansır javadan farkı vae karıştırma liste1=liste2
#liste3=liste1.copy liste1in bir kopyasını liste 3 e gönder
#liste3=liste1+liste2 toplanabilir liste1 de yapılan değişiklik liste 3'etkilemez
#liste4=liste1*10 liste1 i on defa yazdırılmış bir dekilde liste oluşturur
#----------iç içe geçmiş listeler------------
#list[listenin x.elemanına git][x.elemanın y.indeksi]
"""
import random

a=random.randint(0,9)
list=["fal0","Fal1","Fal2","fal3","fal4","fal5","fal6","fal7","fal8","fal9"]
print(f"{a}. fal: {list[a]}")"""


#------------------------------------------------2.GÜN----------------------------------------------------------------------------------
"""
isim=["ahmet","mehmet","ali","yusuf","tarık"]
maas=[7000,9000,15000,5500,22000]
toplam=0 
enYuksekMaas=maas[0]
enDusukMaas=maas[0]
print("{:*^50}".format("Menü"))
arananIsim=input("Lütfen aranan ismi giriniz: ")
for index,i in enumerate (isim):
    if i.lower()==arananIsim.lower():
        print(f"{i} isimli personelin maaşı: {maas[index]}")
        break
else:
    print("Kullanıcı bulunamadı.")   
for i in range(0,len(maas)):
    print(f"{isim[i]} -Maaşı: {maas[i]}")

for i in maas:
    toplam+=i
    if i>=enYuksekMaas:
       enYuksekMaas=i
    elif i<=enDusukMaas:
        enDusukMaas=i
       
    
ortalamaMaas=toplam/len(maas) 
#print(min(maas))
# print(max(maas))
# temp=maas.copy()
# tmp.sort()
# print(temp[0]) en küçük
# print(temp[-1])  en büyük
print(f"En yüksek maaş: {enYuksekMaas}--En düşük maaş: {enDusukMaas}--Toplam maaş: {toplam}--Ortalama maaş: {ortalamaMaas}")"""

"""
a=["ahmet","mehmet","ali"]
print(a.index("ahmet"))
b=[1000,1500,2000]
print(b[a.index("mehmet")])        
#mehmetin maaşını verdi.indisi tuttuk"""

#-------------------TUPLE(DEMETLER)-------------------
#tuple bi kez oluşturulduğunda listedeki gibi sonradan eleman silme,ekleme gibi işlemleri yapamıyoruz.() kullanılır.listede []
#eğer demet bir elemandan oluşuyorsa elemandan sonra virgül konulmlıex:demet=("aa",) demet.count("ALİ") çıktı 3
# demet=([1,3,5],[2,4,6],(7),8) demetin içindeki listede eleman değiişikliği yapabiliriz      


#--------KÜMELER(SET)----------
#bir eleman sadece bir kez kullanılabilir+indisleme yok+bir liste bir kümenin elemanı olamaz
#kume={1,2,3,4,5} boşküme oluştururken seti kullanırız. kume=set()
#"n" in b b kümesinde n var mı diye sorar boolean döner.
#iki kümeyi birleştirmek için c=a.union(b) kullanılır.| birleşimi verir. a|b =a birleşim b a-b =a fark b a&b a kesişim b
#dir(list()) listlerdeki methotları görürüz dir eki ile
"""
isim="elginkan"
print(list(isim))
print(tuple(isim))
print(set(isim))"""
#---------DİCİONARİES(SÖZLÜKLER)-------------
#dic{} indislemeyi biz yaparız.değerlerini biz veririz.{key:value,key:value} in ile arama işlemi sadece anahtar için yapılır
"""
sozluk={"Hi":"Merhaba","car":"araba","yellow":"sarı"}
print(sozluk)
print(sozluk["Hi"]) #hi ın karşılığını getirir
sozluk["Hi"]="Selam"
for key in sozluk:
    print(key)
    print(sozluk[key])


for anahtar,deger in sozluk.items():
    print(anahtar,deger)

sozluk["black"]=["kara","siyah"]
"""
sozluk={"one":"bir","two":"iki","three":"üç","four":"dört"}
kelime=input("Lütfen birden beşe kadar bir ingilizce rakam yazınız:")

print(f"{kelime}= {sozluk[kelime]}")
    

    
       
    

        
        
