
#Bu işlemleri yapmak için bilgisayarınzda Java Development Kit kurulu olmasi gerekir. Kurulu değilse aşağıdaki bağlantıdan kurabilirsiniz.
#https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html




import jpype
# JVM başlat
# Aşağıdaki adresleri java sürümünüze ve jar dosyasının bulunduğu klasöre göre değiştirin
#Windows için:"C:/Program Files/Java/jdk1.8.0_221/jre/bin/server/jvm.dll"
#Linux için:"/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server/libjvm.so"
#-Djava.class.path= zemberek-tum-2.0.jar dosyasının konumu
jpype.startJVM("C:/Program Files/Java/jdk1.8.0_221/jre/bin/server/jvm.dll",
         "-Djava.class.path=C:/Users/xxx/Desktop/zemberek-tum-2.0.jar", "-ea")
# Türkiye Türkçesine göre çözümlemek için gerekli sınıfı hazırla
Tr = jpype.JClass("net.zemberek.tr.yapi.TurkiyeTurkcesi")
# tr nesnesini oluştur
tr = Tr()
# Zemberek sınıfını yükle
Zemberek = jpype.JClass("net.zemberek.erisim.Zemberek")
# zemberek nesnesini oluştur
zemberek = Zemberek(tr)
#Çözümlenecek örnek kelimeleri belirle
kelimeler = ["fatih","okulda","naber","tırmalamışsa"]
for kelime in kelimeler:
    if kelime.strip()>'':
        yanit = zemberek.kelimeCozumle(kelime)
        if yanit:
            print("{}".format(yanit[0]))
        else:
            print("{} ÇÖZÜMLENEMEDİ".format(kelime))
#JVM kapat
jpype.shutdownJVM()
