
#ÖNÇELLİKLE NOT HESAPLAMA ADINDA FONKSİYON TANIMLIYORUZ
#FONKSİYONU SIRALAMAK İÇİN LEN FONKSİYONUNU KULLANIP SIRALIYORUZ
def notHesaplama ():
    a=0
    for a in range(len(sinav_sonuc["Vize"])):
        vize=sinav_sonuc["Vize"][a]
        final=sinav_sonuc["Final"][a]
        #GEÇME NOTUNU HESAPLATIYORUZ
        sonuc=(vize*0.3)+(final*0.7)
        sinav_sonuc["sonuc"].append(sonuc)
    #KULLAMICIDAN İSİM ALIYORUZ VE ONU SINAV SONUC İSİMLİ SÖZLÜGE EKLİYORUZ
    name=input ("isim giriniz")
    sinav_sonuc["isim"].append(name)
    #KULLANICIDAN CİNSİYET ALIYORUZ VE ONU DA SINAV SONUC İSİMLİ SÖZLÜĞE EKLİYORUZ
    cinsiyet=input ("cinsiyet giriniz= kadın\erkek= ")
    sinav_sonuc["Cinsiyet"].append(cinsiyet)
    #KULLANICIDAN VİZE NOTUNU ALIYORUZ SİNAV SONUC İSİMLİ SÖZLÜGE EKLİYORUZ
    vize=int (input ("vize notunuzu giriniz= "))
    sinav_sonuc["Vize"].append(vize)
    #KULLANICIDAN FİNAL NOTUNU ALIYORUZ SİNAV SONUC İSİM SÖZLÜGE EKLİYORUZ
    final=int (input("final notunuzu giriniz= "))
    sinav_sonuc["Final"].append(final)
    
    sonuc=(vize*0.3)+(final*0.7)
    sinav_sonuc["sonuc"].append(sonuc)
    #SİNAV_SONUC İSİMLİ SÖZLÜK OLUŞTURUYORUZ CİNSİYETİ İSİMLERİ VİZE FİNAL VE SONUCU BURAYA ATIYORUZ
sinav_sonuc = {'isim':['Ayşe K.','Ahmet M.','Nuri C.','Nawar T.','Suzan T.','Ala B.'],
'Cinsiyet':['K','E','E','E','K','K'],
'Vize':[80,60,77,25,36,75],
'Final':[90,50,53,100,98,66],
#SONUC İSİMLİ BOŞ SÜTUN OLUŞTURUYORUZ 
'sonuc':[]}
i=0
while i<2:
    #İKİ YENİ KAYIT ALMAK İÇİN WHİLE DÖNGÜSÜ KULLANIYORUZ 
    notHesaplama()
    i+=1
    #PRİNT KOMUTU İLE VERİLERİ EKRANA YAZDIRIYORUZ 
print(sinav_sonuc)
