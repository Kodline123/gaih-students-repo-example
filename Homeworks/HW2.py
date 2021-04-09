#Kullanıcı hesabı ödevi.

GİRİLENKULLANICIADI = input('KULLANICI ADINIZI GİRİNİZ:')
GİRİLENŞİFRE = input('ŞİFRENİZİ GİRİNİZ:')
print("KULLANICI HESABI OLUŞTURULDU BANKAMIZI KULLANDIĞINİZ İÇİN TEŞEKKÜRLER")
kullanıcıseçimi = input('PARA GÖNDERME İŞLEMİ YAPMAK İSTİYORSANIZ EVET İSTEMİYORSANIZ HAYIR YAZINIZ:')
if kullanıcıseçimi == "Evet" :


    KULANİCİADİ = input('KULLANICI ADI GİRİNİZ:')
    ŞİFRE = input('ŞİFRE GİRİNİZ:') 

    if KULANİCİADİ == GİRİLENKULLANICIADI and ŞİFRE == GİRİLENŞİFRE :
        İSİM = input('GÖNDERİLEN KİŞİ ADI')
        SOYİSİM = input('SOYİSİM:')
        YAŞ = int(input('YAŞINIZI GİRİNİZ:'))
        TC = int(input('TC KİMLİK NO GİRİNİZ:'))
        TUTAR = int(input('GÖNDERİLECEK TUTAR:'))
        print(İSİM + " " + SOYİSİM + " " + str(YAŞ) + " " + str(TC) + " " + str(TUTAR)  + " " + 'TEŞEKKÜRLER İŞLEMİNİZ TAMAMLANDI')
    else :
        print("Kullanıcı adı ve şifre hatalı")
else :
    print("BANKAMIZI TERCİH ETTİĞİNİZ İÇİN TEŞEKKÜRLER BİR DAHA BEKLERİZ (: (:")

