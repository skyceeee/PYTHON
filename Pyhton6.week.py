#--------Proje yarışması------------


import json
def yeniKayitEkle():
    import json
    with open(r"C:\Users\goook\Desktop\proje.json","r") as dosya:
        yeniKayıt=json.load(dosya)
        
    isim=input("isim:")
    iss=input("iş:")
    egitim=input("eğitim:")
    maas=int(input("Maaş:"))
    yeniKayıt[str(len(yeniKayıt)+1)]={"isim":isim,"meslek":iss,"egitim":egitim,"maas":maas}
    
    with open(r"C:\Users\goook\Desktop\proje.json","w") as dosya:
        dosya.writelines(json.dumps(yeniKayıt))

  
yeniKayitEkle()

      

        


   

       





