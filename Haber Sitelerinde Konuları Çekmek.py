import requests
from bs4 import BeautifulSoup

#r = requests.get('xxx') xxx yerine yazılan sitenin kodlarını çeker. Çekemediği zaman genellikle fazla Script kodlarından dolayı oluyor.
r = requests.get('https://www.iha.com.tr/')

#bs4, html kodlarının düzenli gösterilmesini sağlar.
source = BeautifulSoup(r.content,"lxml")




#html kodları içerisinde  'a' etiketli 's-item2 std' classını bulup, href'in karşılığını getirdi.
#Bu blok programın kendini güncel tutması için yazıldı.



y=source.find('a',attrs={'class':'s-item2 std'})
t=y.get('href')
t = requests.get(t)
source = BeautifulSoup(t.content,"lxml")

dictt={}




#html kodları içerisinde BÜTÜN 'a' etiketli 's-item2 horizontal' classını bulup, href'in karşılığını getirdi.

for x in source.find_all('a',attrs={'class':'s-item2 horizontal'}):
    r=x.get('href')
    r = requests.get(r)
    source = BeautifulSoup(r.content,"lxml")
    
    
    
    #html kodları içerisinde 'h1' etiketli 'htitle' classını bulup, text'e çevirdi.
    title=source.find('h1',attrs={"class":"htitle"}).text
    #Haber Başlıkları
    
    
    #Popüler haberlerin başlık ID'lerini aldık
    a='contentWrp_'+str(r.url.split('-')[-1][:-1])
    
    #Popüler haberlerin konusunu bulmak için BÜTÜN 'div' etiketli a değişkenli id'yi bulup, data_targeting'in karşılığını getirdi.
    for i in source.find_all('div',attrs={"id":"%s"%(a)}):
        topic=i.get('data-targeting')
        dictt[title]=topic
        break
        
    
[print('Başlık:\t%s\nKonu:\t%s'%(title,topic))for title,topic in zip(dictt.keys(),dictt.values())]
    