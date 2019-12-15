try:
    #Verileri okuma
    def bilgi_cek():
        with open("veriler.txt","r+") as file:

            veriler_read=file.readlines()
            return veriler_read


    #Okunan verilerin değişkenlere atılması.
    bilgiler=bilgi_cek()
    yemeksepeti=bilgiler[0]
    facebook=bilgiler[1]
    twitter=bilgiler[2]


    #Profil bilgilerinin parçalanması.
    global yemeksepeti_kullanici_adi,yemeksepeti_sifre,facebook_kullanici_adi,facebook_sifre,twitter_kullanici_adi,twitter_sifre
        #Yemeksepeti
    yemeksepeti,yemeksepeti_profil_bilgileri=yemeksepeti.split(":")
    yemeksepeti_kullanici_adi,yemeksepeti_sifre=yemeksepeti_profil_bilgileri.split(",")
        #Facebook
    facebook,facebook_profil_bilgileri=facebook.split(":")
    facebook_kullanici_adi,facebook_sifre=facebook_profil_bilgileri.split(",")
        #Twitter
    twitter,twitter_profil_bilgileri=twitter.split(":")
    twitter_kullanici_adi,twitter_sifre=twitter_profil_bilgileri.split(",")


except:
    print("Lütfen veriler.txt dosyasına profil bilgileriniz belirtilen formatta giriniz.")
