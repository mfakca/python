import pyodbc 
import pandas as pd
#Kullandığınız kütüphaneye göre söz dizim değişebiliyor.Ben pyodbc ile çalıştım.


#'Driver={SQL Server};'
#'Server=xxx;' : xxx yerine kurmuş olduğunuz server ismini yazmanız gerekiyor. Öntanımlı bir şekilde kurduysanız bilgisayarınızın ismi oluyor.Bilmiyorsanız cmd içerisinde 'hostname' yazarak öğrenebilirsiniz.
#'Database=AdventureWorks;': İşlem yapacak olduğunuz Database ismi. Ben AdwentureWorks ile çalıştım.
#'Trusted_Connection=yes;' : Eğer kendi bilgisayarınızda kurulu (yerel) bir server üzerinde çalışacaksanız bu değerin 'yes' olması gerekiyor.

#Bağlantı için istenilen değerleri girdikten sonra bağlatıyı kurduk.
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=xxx-xxx;'
                      'Database=AdventureWorks;'
                      'Trusted_Connection=yes;')

#İşlem yapmak için imleç oluşturuyoruz.
cursor = cnxn.cursor()


#execute()'ın içine yapacak olduğumuz işlemin SQL kodunu giriyoruz.
cursor.execute('SELECT * FROM AdventureWorks.Sales.CreditCard')


#Gerekli listeleri tanımladık.
cardID,cardType,cardNumber,expMonth,expYear,modifiedDate=[],[],[],[],[],[]

#Çektiğimiz verileri listelere alıyoruz.
for row in cursor:
    cardID.append(row[0])
    cardType.append(row[1])
    cardNumber.append(row[2])
    expMonth.append(row[3])
    expYear.append(row[4])
    modifiedDate.append(row[5])


#SQL bağlantımızı kopartıyoruz.Bundan sonra ihtiyacımız yok.   
cnxn.commit()



#Listeleri DataFrame'e çeviriyoruz.
df=pd.DataFrame(cardID,columns=['ID'])
df['Card Type']=cardType
df['Card Number']=cardNumber
df['expMonth']=expMonth
df['expYear']=expYear
df['ModifiedDate']=modifiedDate


#Çektiğimiz veride ID olduğu için index'e gerek duymuyoruz ve index dahil olmayacak bir şekilde df DataFrame'ini yeniden tanımlıyoruz.
df=df.iloc[:,1:]


import matplotlib.pyplot as plt
import seaborn as sns


#En çok kullanılan kart tipini görmek için kart tiplerini saydırıyoruz ve tablo çizdiriyoruz.Daha dikkat çekici olması için '-or' yazdım.
#-or: (o) X eksenindeki her değerin y eksenindeki karşılıına nokta koyar.
#-or: (-) Çizilen noktalar arasında çizgi çizer.
#-or: (r) Çizgi ve Noktaların rengini kırmızı (red) yapar.
plt.plot(df['Card Type'].value_counts(),'-or')

#X ekseni etiketi
plt.xlabel('Card Type')
#Y ekseni etiketi
plt.ylabel('Frequency')

