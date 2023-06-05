#----------------Nesneye yönelik programama-------
"""
class Kullanicilar():
    isim=""
    kid=""
    bolum="Bilgisayar Mühendisliği"
    ktur=""
Kullanicilar.ktur="Genel kullanıcı"
ogrenci=Kullanicilar()#örnek nesne
ogretmen=Kullanicilar()#örnek nesne
ogrenci.isim="Gökçe"
ogretmen.isim="Ozan"
ogrenci.kid="111"
ogretmen.kid="123"
print(ogrenci.isim)
print(ogrenci.bolum)
print(ogrenci.ktur)
print(ogrenci.kid)
print(ogretmen.isim)
print(ogretmen.bolum)
print(ogretmen.ktur)
print(ogretmen.kid)"""
"""
class Araba():
    tekerlekSayisi="4"
    marka=""
    model=""
    yakitTuru=""

fosiller=Araba()
fosiller.marka="BMW"
fosiller.model="AA"
fosiller.yakitTuru="Fosil"
elektrikliler=Araba()
elektrikliler.marka="Togg"
elektrikliler.model="BB"
elektrikliler.yakitTuru="Elektrikli"
print(fosiller.yakitTuru)
print(fosiller.tekerlekSayisi)
print(elektrikliler.yakitTuru)
print(elektrikliler.tekerlekSayisi)"""
"""
class Ogrenciler():
    okulNo=""
    isim=""
    bolum=""
    def BilgileriYazdir(self,vize,final):#self nesnenin kendisini fiade eder.istersek self yerine başka kelime de kullanabiliriz.ilk değişken classı tutar
        self.vize=vize#classa attribute ekledik
        self.final=final
        print(self.okulNo,self.isim,self.bolum,(vize+final)/2,)

ozan=Ogrenciler()
ozan.okulNo=1234
ozan.isim="Ozan Alptekin"
ozan.bolum="Bilgisayar müheendisliği"
ozan.BilgileriYazdir(50,70)#selfi yazmadık çünkü self ozan oldu"""

"""
class Ogrenciler():#sınıf
    def __init__(self,vize,final):#parametre verirken işimize yarayacak---YAPILANDIRICI FONK---
        self.vize=vize#özellik
        self.final=final
    def OrtalamaHesapla(self):#olay yani method
        print(f"Öğrencinin ortalaması: {(self.final)+(self.final)/2}")

#ozan=Ogrenciler()#bunda hata veriri
ozan=Ogrenciler(30,50)#hata vermez#nesne
ozan.OrtalamaHesapla()#methodu . ile direkt çalıştırabiliriz."""
"""
class Personel():
    
    def __init__(self,isim,kid,telNo="Belirtilmemiş"):#init constructor gibi çalışır
        self.telNo=telNo
        self.kid=kid
        self.isim=isim
    def BilgileriYazdir(self):
        print(self.isim,self.kid,self.telNo)

ayse=Personel("Ayşe","234567")   
ali=Personel("alii",123,"12345678")
ayse.BilgileriYazdir()
ali.BilgileriYazdir()"""
"""
class Ogrenci():
    def __init__(self,kid,isim):
        self.kid=kid
        self.isim=isim
    def OrtalamaHesapla(self,vize,final):
        self.ortalama=(vize+final)/2
    def Yazdir(self):#her zaman ilk parametre classın kendisi olur
        print(f"İsim: {self.isim},Kullanıcı id: {self.kid},ortalama: {self.ortalama}")
   
a1=Ogrenci(12,"ayşe")
a1.OrtalamaHesapla(50,80)
a1.Yazdir()"""

"""
class Ogrenci():
    def __init__(self,kid,isim):
        self.kid=kid
        self.isim=isim
    def OrtalamaHesapla(self,vize,final):
        return (vize+final)/2
    
    def Yazdir(self,vize,final):#her zaman ilk parametre classın kendisi olur
        print(f"İsim: {self.isim},Kullanıcı id: {self.kid},ortalama: {self.OrtalamaHesapla(vize,final)}")
   
a1=Ogrenci(12,"ayşe")
a1.Yazdir(70,80)"""


"""
import datetime
class Personel():
    sehir="Manisa"
    sirketIsim="Elginkan Holding"
    def __init__(self,kid,isim,departman,baslangicYili):
        self.kid=kid
        self.isim=isim
        self.departman=departman
        self.baslangicYili=baslangicYili
        
    def maasHesapla(self,cocukSayisi):
        kidemYili=datetime.datetime.today().year-self.baslangicYili#bize direkt integer olarak bulunduğumuz yılı verir
        return 5000+(500*kidemYili)+(cocukSayisi*750)
       
    def maasiYazdır(self,cocukSayisii):
        print(f"{self.isim} adlı çalışanın maaşı: {self.maasHesapla(cocukSayisii)}")
        
    def bilgileriYazdir(self):
        print(f"Kullanıcı adı:{self.isim} , kullanıcı id: {self.kid}, Şirkete başlangıç yılı: {self.baslangicYili}, Şehir: {self.sehir},Şirket ismi:{self.sirketIsim} ")
    
    def genelYazdir(self,**kwarg):#tek yıldızda ne gönderirsek bir liste şeklinde tutar.çift yıldızda keyii ayrı valueyi ayrı tutar
        for key,value in kwarg.items():#key ve valueyi kwarg içinde sözlük olarak tut
            print(f"{key}={value}")

personel1=Personel(1,"ahmet yılmaz","arge",2000)
personel2=Personel(2,"Serap kaya","Muhasabe",2020)
Personel.sirketIsim="İstanbul"
personel1.maasiYazdır(3)
personel2.maasiYazdır(1)
personel1.bilgileriYazdir()
personel2.bilgileriYazdir()
personel1.genelYazdir(kid=personel1.kid,isim=personel1.isim,departman=personel1.departman,baslangicYili=personel1.baslangicYili,sehir=personel1.sehir,sirketIsim=personel1.sirketIsim)
personel1.genelYazdir(maas=personel1.maasHesapla(3))
"""
#----------INHERITANCE-----------
"""
class Anne():
    gozRengi="Mavi"
    sacRengi="Siyah"
class Baba():
    gozRengi="kahverengi"
    sacRengi="Sarı"
    boy="uzun"
class Cocuk(Anne,Baba):#ilk yazdığımız superclassın özelliklerini alır
    pass#eğer bir işlem yapmayacaksak pass deriz
class Torun(Cocuk):
    pass
cocuk1=Cocuk()
torun1=Torun()
print("torun 1 göz rengi: ",torun1.gozRengi)
print(cocuk1.gozRengi,cocuk1.boy)"""
"""
class AtaSinif():
    def __init__(self,ad,soyad):
        self.ad=ad
        self.soyad=soyad

    def yazdir(self):
        print(self.ad,self.soyad)

class CocukSinif(AtaSinif):
    def __init__(self, sacRengi, gozRengi,boy):
        self.sacRengi=sacRengi
        self.gozRengi=gozRengi
        self.boy=boy
    def yazdir(self):
        print(self.gozRengi,self.sacRengi,self.boy)

cocuk2=CocukSinif("kahverengi","yesil","uzun")
cocuk2.yazdir()"""
"""
class Ata():
    def __init__(self,ad,soyad):
        self.ad=ad
        self.soyad=soyad
class Cocuk(Ata):
    def __init__(self,ad,soyad,numara,sinif):
        super().__init__(ad,soyad)
        self.numara=numara
        self.sinif=sinif
    def _Yazdir(self):
        print(self.ad,self.soyad,self.numara,self.sinif)

cocuk1=Cocuk("gökçe","keskin",123,2)        
cocuk1._Yazdir()"""
#****************ENCAPSULATION******************üst örnekle bağlantılı __ ileyapılır._ olursa bunu değiştirebilirsiin ama bence değiştirme der gibi
""""
class Ogrenciler():
    def __init__(self,ad,soyad,tckimlik,not1,not2):
        self.ad=ad
        self.soyad=soyad
        self.__tckimlik=tckimlik
        self.__not1=not1
        self.__not2=not2
    def OrtalamaHesapla(self):
        print((self.__not1+self.__not2)/2)
    def getterNotlar(self):
        print(f"{self.__not1}=not 1,{self.__not2}=not 2")
    def setterNotlar(self,tmpnot1,tmpnot2):
        self.__not1=tmpnot1
        self.__not2=tmpnot2

ahmet=Ogrenciler("Ahmet","yılmaz","123456",50,90)
ahmet.getterNotlar()
ahmet.OrtalamaHesapla()
ahmet.setterNotlar(50,70)
ahmet.getterNotlar()
ahmet.OrtalamaHesapla()"""
#print(ahmet.__not1) dışarıdan notlara ulaşamayız.

#--------POLYMORPHISM--------
"""
class Araba:
    def Tekerlek(self):
        return "Arabanın tekerlek sayısı 4'tür"
    def Kontrol(self):
        return "Arabanın kontrolü direksiyon ile sağlanır"
    def Yakit(self):
        return "Arabanın yakıtı fosil yakıttır"
class Bisiklet:
    def Tekerlek(self):
        return "Bisikletin tekerlek sayısı 4'tür"
    def Kontrol(self):
        return "Bisikletin kontrolü gidon ile sağlanır"
    def Yakit(self):
       return "Bisikletin insan gücüdür"
bisiklet=Bisiklet()
araba=Araba()
for tasit in (bisiklet,araba):
    print(tasit.Kontrol())
    print(tasit.Tekerlek())
    print(tasit.Yakit())"""



"""
class Ilkogretim():
    def Okul(self):
        print("Muzaffer Taşdemir İlköğretim Okulu")
class Lise():
    def Okul(self):
        print("Çınarlı Teknik Lisesi")
class Universite():
    def Okul(self):
        print("Ege Üniversitesi")
class YuksekLisans():
    def Okul(self):
        print("Beykent Üniversitesi")
def Okullar(param):
        param.Okul()

Okullar(Ilkogretim())
Okullar(Lise())
Okullar(Universite())
Okullar(YuksekLisans())"""


#**************RECURSIVE METHOD**************
def faktoriyelHesapla(sayi):
    if sayi==1:
        return 1
    else:
        return faktoriyelHesapla(sayi-1)*sayi


sayi=int(input("Lütfen bir sayı giriniz: "))
print(faktoriyelHesapla(sayi))

 
    
    
