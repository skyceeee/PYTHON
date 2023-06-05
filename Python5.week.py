#-----------------HATA İŞLEMLERİİ------------------------
#try:(kod hata denetimi) except:hata yerine kendi istediğimiz çıktıyı veriri -try da programı verdik.hata varsa -except.hata yoksa -else gider.hata olsa da olmasa da -finally gider.
"""
while(True):
    try:
        sayi1=int(input("Bölünen sayı:"))
        sayi2=int(input("Bölen sayi:"))
        print(sayi1/sayi2)
    except ZeroDivisionError:
        print("Hiçbir sayı sıfıra bölünemez.")
    except ValueError:
        print("Lütfen tam sayı giriniz.")
    except:
        print("Sistem hatası oluştu.")
    else:#hata yoktur.
        print("Herhangi bir hata oluşmadı.İşlem başarılı.")
    finally:#hata var ya da yok diyemeyiz.
        print("Program sonlandırıldı.")"""

#assert /raise hata fırlatma.
"""
sayi1=int(input("Bölünen sayı:"))
sayi2=int(input("Bölen sayi:")) 
if sayi2==0:
    raise Exception("Üzgünüm sayı 0'a bölünemez.")    
else:
    print(sayi1/sayi2)"""

#-----------------DOSYA İŞLEMLERİ-------------
#CSU h5 JSON dat Xml txt bin vs
#----klasik dosya açma-----
"""
dosya=open("c:\\notlar\\a.txt")#open=dosyayı açar.
#print(dosya.read(1))#read=dosyayı okur
#print(dosya.read())
#print(dosya.readline())
satirlar=dosya.readlines()
#print(satirlar)
for satir in satirlar:
    print(satir)
print(type(dosya.read()))
dosya.close()#yaptığımız değişikliklerin kaydedilmesi için dosyayı kapatmamız lazım."""
"""
#------------2.yol------------- bu yöndemde close yapmaya gerek yok
for satir in open("c:\\notlar\\a.txt"):
    print(satir) 
#-----------3.yol---------- close yapmaya gerek yok
with open("c:\\notlar\\a.txt") as dosya:
    for satir in dosya:
        print(satir)"""
"""
with open ("c:\\notlar\\a.txt","w+") as dosya:#dosyayı içini bulup üstüne yazar.bulamazsa yeni bir dosya yazar
    dosya.write("merhaba dünya\n")
    print(dosya.read())
with open ("c:\\notlar\\a.txt","a+") as dosya:
    dosya.write("MERHABA DÜNYA\n")
    print(dosya.read())
    
with open("c:\\notlar\\a.txt") as dosya:
    print(dosya.read())"""

#örnek:kullanıcıdan aldığı isim soy isim ve telefon numarasını dosyaya kaydeden program.
"""
try:
    isim=input("Lütfen isminizi giriniz.")
    soyIsim=input("Soy isminizi giriniz:")
    telefon=int(input(" Telefon numaranızı giriniz."))
    with open ("c:\\notlar\\telrehberi.txt","a")as dosya:
        dosya.write(f"{isim} {soyIsim} {telefon}\n")
except ValueError:
    print("Telefon numarası sadece sayılardan oluşmalıdır.")
except:
    print("Dosya kayıt işlemi gerçekleşmedi.")
else:
    print("Dosya kayıt işlemi başarılı bir şekilde sonuçlandı.")
finally:
    print("Program sonlandırıldı.")"""
"""
a=["merhaba\n","dünya\n"]
with open("c:\\notlar\\telrehberi.txt","a") as dosya:
    dosya.writelines(a)"""

#import os sadece osun remove methodunu kullanacağımız için.rmdir=klasör boşsa siler.
"""
from os import remove as r
try:
    r("c:\\notlar\\a.txt")
except FileNotFoundError:
    print("Dosya bulunamadı.")
else:
    print("Silme işlemi tamamlandı.")"""
"""
import os
try:
    ad="ozan"
    soyad="alptekin"
    tel="555555555"
    if os.path.exists("c:\\notlar\\telrehberi.txt")==True:
        mode="a"
    else:
        mode="w"
    with open("c:\\notlar\\telrehberi.txt",mode) as dosya:
        dosya.write(f"{ad} {soyad} {tel}")
except:
    print("Hata")"""

#-------------------XML--------------
"""
from turtle import pen
import xml.etree.ElementTree as ET
object1=ET.parse("C:\\Users\\goook\\Desktop\\deneme.xml")
kok=object1.getroot()
print(kok,"---------",kok[0],"---------",kok[1].tag)
print(kok[1].attrib)
print("-------------------------")
for dugum in kok:
    print(kok.tag)#kok kitaplar kokün sıfırıncı elemanı kitap1 dugum kokun elemanlarını tutar.
    print(kok.attrib)
    print(dugum.tag)
    print(dugum.attrib)

print("---------------------")

for eleman in kok.iter():
    print(eleman.tag)
    print(eleman.attrib)

print("-----------------------")

for kitap in kok.iter('yazar'):
    print(kitap.text)#text metodu değerleri text olarak geri döndürür

print("------------------------")

for xml in kok.findall("kitap"):#findall tüm kitap düğümlerini çağırır.
    print(xml.get("id"))#özellikler get ile çağırılır
    print(xml.find("yazar").text)#elemanlar find ile çağırılır
    print(xml.find("baslik").text)
    print(xml.find("tur").text)
    print(xml.find("basimTarihi").text)
    print(xml.find("fiyat").text)

print("--------------------")
print(kok[0].find("fiyat").text)"""

#---JSON------sözlük gibi yazılır
"""
import json
sozluk={"isim":"gökce","meslek":"ogrenci","egitim":"universite"}
with open("C:\\Users\\goook\\Desktop\\deneme.json","w") as dosya:
    dosya.writelines(json.dumps(sozluk))
print("İşlem tamamlandı...")
with open("C:\\Users\\goook\\Desktop\\deneme.json","r") as dosya:
    veriler=json.load(dosya)
print(veriler)
print(type(veriler))"""
"""
print("-----------")
sozlukk={"1":{"isim":"ozan","meslek":"öğretmen","eğitim":"doktora"},
"2":{"isim":"mehmet","meslek":"mühendis","eğitim":"lisans"}
}
print(sozlukk["2"]["isim"])

for i in range(1,100):
    print(str(i),sozlukk[i]["meslek"])"""


