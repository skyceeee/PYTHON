'''print("Hello World\n" * 5)
print("""Atatürk'ün de dediği gibi  "İstikbal göklerdedir..." """)
print("""HELLO
Hİİİİ""")
print('Hello\'s')
print('c:\n\deneme.txt')
print('c:\\n\\deneme.txt')'''
'''print("hello world")
print( int(input('Lütfen 1. sayıyı giriniz: '))+int(input('Lütfen 2. sayıyı giriniz: ')))'''
#2.ders
"""a=5
print(a)
print(type(a))"""

#input()
'''sayi1=int(input("Lütfen sayıyı giriniz: "))
# "","iki ifadeyi tipi farketmeksizin biir boşluk bırakarak toplar
print("Girdiğiniz sayı:",sayi1)
sonuc=(sayi1)**2
print("Girdiğiniz sayının karesi: "+ str(sonuc))'''


#birden fazla satırda işlem yapmak istiyorsak üç tırnak kullanmalıyız
'''ptint("""1...topla
2...çıkar
3...böl
4...çarp""")'''


"""a=1
b=2
c=3
#sepin default hali boşluk " "(virgülün işlevi)
#print(a,b,c, sep="-")
#end in default hali"\n"
print(a,b,c,end=" ")
print(a,b,c)
print("hello \nworld")"""


#---FORMAT YÖNTEMİ---
"""sayi1=int(input("Lütfen 1.sayıyı giriniz: "))
sayi2=int(input("Lütfen 2.sayıyı giriniz: "))
sonuc=sayi1+sayi2
#print(sayi1,"+",sayi2,"=",sonuc)
#kısa yöntem
#değişken gönderdiğimiz yerlere süslü parantez kullandık
#print("{0}+{1}={2}\nGirilen ilk sayı {0}.\nİkinci sayı {1}.\nSonuç ise {2}.".format(sayi1,sayi2,sonuc))
#enkısa yöntem
#f yazmalıyız
print(f"{sayi1}+{sayi2}={sonuc}")"""



#---------İLK ÖRNEK----------
#Girilen sangrt sıcaklığı fahren. çevirme
"""sayi1=int(input("Lütfen sıcaklık için bir değer giriniz: "))
sonuc=sayi1*1.8+32
print("{0}C derecenin fahrenght karşılığı {1} dir.".format(sayi1,sonuc))"""

#print("{:*^50}".format("Menü"))



"""kullanıcıAdı=input("Lütfen isminizi giriniz: ")
kullanıcıYas=input("Lütfen yaşınızı giriniz: ")
print(f"Hoşgeldin {kullanıcıAdı}.{kullanıcıYas} yaşında olduğunu söyledin.")"""






"""kenar1=int(input("Lütfen birinci kenaar için bir doğal sayı giriniz: "))
kenar2=int(input("Lütfen ikinci kenar için bir doğal sayı giriniz: "))
print(f"Birinci kenarı {kenar1}, ikinci kenarı {kenar2} olan dikdörtgenin çevresi {2*(kenar1+kenar2)},alanı {kenar1*kenar2}'dır")"""



"""yariCap=int(input("Lütfen dairenin yarıçapını giriniz: "))
print("{:*^20}".format('SONUÇ'))
print(f"Yarıçapı {yariCap} olan dairenin alanı: {yariCap*yariCap*3.14} ve çevresi: {2*yariCap*3.14}")"""
















      

