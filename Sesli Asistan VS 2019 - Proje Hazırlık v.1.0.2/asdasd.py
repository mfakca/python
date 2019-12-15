import speech_recognition as sr
import time
from selenium import webdriver
import profile_data
r = sr.Recognizer()
m = sr.Microphone()


cdriver= "chromedriver.exe"

profile_data.bilgi_cek()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Konuşabilirsin")
        with m as source: audio = r.listen(source)
        print("Biraz beklemelisin")
        
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio, language="tr-TR")
            x1=value.split()
            
            for i in x1:
                if i =="nedir":
                    
                    x1.remove(i)
                    for z in x1:
                        d=""
                        d=d+z
                    
                    driver= webdriver.Chrome(cdriver)
                    driver.get("http://google.com")
                    search = driver.find_element_by_name('q')
                    search.send_keys(d)

                    search.send_keys(u'\ue007')
                elif(i=="dolar"):
                    a=""
                    for z in x1:
                        a+=z
                        a+=" "
    
                    
                    driver= webdriver.Chrome(cdriver)
                    driver.get("http://google.com")
                    search = driver.find_element_by_name('q')
                    search.send_keys(a)
                    search.send_keys(u'\ue007')

                    
                elif i == "YouTube'dan":
                    kelime=value.split()
                    kelime.remove("YouTube'dan")
                    kelime.remove("aç")


                    
                    driver= webdriver.Chrome(cdriver)
                    driver.get("https://www.youtube.com")
                    search = driver.find_element_by_name('search_query')
                    
                    search.send_keys(kelime)

                    search.send_keys(u'\ue007')

                    time.sleep(3)
                    searchh = driver.find_element_by_id('video-title').click()  

                    
            if value =="yemek sepetine gir":
                
                    
                driver= webdriver.Chrome(cdriver)
                driver.get("https://www.yemeksepeti.com/sakarya")
                search = driver.find_element_by_name('UserName')
                searchh = driver.find_element_by_name('Password')
                search.send_keys(profile_data.yemeksepeti_kullanici_adi)
                searchh.send_keys(profile_data.yemeksepeti_sifre)

                searchh.send_keys(u'\ue007')

            elif value in "YouTube'dan":
                value=value[1:-1]

                    
                driver= webdriver.Chrome(cdriver)
                driver.get("https://www.youtube.com")
                search = driver.find_element_by_name('search')
                search.send_keys(value)

                search.send_keys(u'\ue007')


            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Ne dediğini anlayamadım.Tekrar söyleyebilir misin?")
        except sr.RequestError as e:
            print("Google servisine bağlanılamıyor.; {0}".format(e))
except KeyboardInterrupt:
    pass
