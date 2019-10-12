#KÜTÜPHANE KURULUMU


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#VERİ ÖN İŞLEME


#kaggle'dan aldığım 1998 - 2017 yılları arasında Brezilya daki orman yangınları verilerini içeren excel dosyasını içe aktarıyoruz. 
df=pd.read_excel('amazon.xlsx')

#Sütun isimlerini düzenliyoruz. (number yazıyordu onun yerine frequency yazdım.)
df.columns=['year', 'state', 'month', 'frequnecy', 'date']

#Zaten yıl diye ayrı bir sütun olduğu ve girilen verilerin sadece yıllık girildiği için tarih kısmını çıkarttım.
df=df.iloc[:,:4]


#VERİ GÖRSELLEŞTİRME


#seaborn kütüphanesi ile görselleştiriyorum.(Frekans tabloları genellikle barplot ile görselleştiriliyor.)
sns.barplot(x='year',y='frequnecy',data=df)
#Çizilen tabloyu ekrana yazdırıyorum.
plt.show()


#Çok fazla yıl olduğu için yan yana yazıldığında okunmuyor.Bazı verileri eledim.
df.drop(df[df['year']%3==0].index,inplace=True)
#Tablo çizdiriyorum.
sns.barplot(x='year',y='frequnecy',data=df)
#Çizilen tabloyu ekrana yazdırıyorum.
plt.show()


