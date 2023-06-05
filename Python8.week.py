

"""
class Maas():
    def __init__(self,yetki,kidemYili,cocukSayisi,nott):
        self.yetki=yetki
        self.kidemYili=kidemYili
        self.cocukSayisi=cocukSayisi
        self.nott=nott
    
    def maasHesabi(self):
        liste=(15000,7500,5000)
        return liste[self.yetki-1]+(self.kidemYili*500)+(self.cocukSayisi*750)+(self.yabanciDil())
        

    def yabanciDil(self):
        ekodeme=0
        if 50<self.nott<70:
            ekodeme+=500
        elif self.nott<90:
            ekodeme+=1000
        elif self.nott<100:
            ekodeme+=1500
        return ekodeme
    
    def maasiYazdir(self):
        print(f"Maaşı: {self.maasHesabi()}") 



class Kullanicilar(Maas):
    def __init__(self,yetki,kidemYili,cocukSayisi,nott,idd,isim,eposta,telefon):
        super().__init__(yetki,kidemYili,cocukSayisi,nott)
        self.__idd=idd
        self.isim=isim
        self.eposta=eposta
        self.telefon=telefon
    def getterid(self):
        if self.yetki==1:
            return self.__idd
        else:
            print("Yetkiniz yok")
    def setterid(self,idd):
        if self.yetki==1:
            self.__idd=idd
        else:
            print("Yetkiniz yok")
    

    
    def bilgileriYazdir(self):
        print(f"isim: {self.isim},id no: {self.getterid()},e-posta: {self.eposta},telefon numarası: {self.telefon},çocuk sayısı:{self.cocukSayisi},Kıdem yılı: {self.kidemYili},ysd puandı: {self.nott}")

        

class Personel(Kullanicilar):
    def __init__(self,yetki,kidemYili,cocukSayisi,nott,idd,isim,eposta,telefon):
        super().__init__(yetki,kidemYili,cocukSayisi,nott,idd,isim,eposta,telefon)
        



personel1=Personel(1,15,2,90,2,"aysel","sdfghjk","sdfghjk")
personel1.bilgileriYazdir()
personel1.maasiYazdir()
"""
#------------------SON GÜN--------------
"""
import threading
import time
def MesajYaz(mesaj):
    i=1
    while i<10:
        print(f"{i}. mesaj")
        i+=1
        time.sleep(1)

def Carp(a,b):
    i=1
    while i<10:
        print(a*b)
        i+=1
        time.sleep(1)

t1=threading.Thread(target=MesajYaz,args=("Merhaba",))#tupleda tek arguman olmadığı için , koyduk.
t2=threading.Thread(target=Carp,args=(3,4))
t1.start()
t2.start()"""

import queue #pide kuyruğu
"""
q=queue.Queue()
for harf in "Merhaba":
    q.put(harf)#eleman eklemek için put kullanırız.yeni eleman sıranın en sonuna geldi


while not q.empty():
    print(q.get(),end=",")"""
#LifoQueue metodu queue modülü içerisinde LIFO prensibine 
#göre çalışır yani son giren ilk çıkar. Yazım şekli
"""
q=queue.LifoQueue()#(Max Kuyruk Uzunluğu)
for harf in "Merhaba":
    q.put(harf)


while not q.empty():
    print(q.get(),end=",")"""

q=queue.PriorityQueue()
q.put((2,"e"))
q.put((3,"r"))
q.put((6,"b"))
q.put((1,"M"))
q.put((5,"a"))
q.put((4,"h"))
q.put((7,"a"))

print(q.get()[1])
"""
while not q.empty():
    print(q.get()[1], end=",")"""




