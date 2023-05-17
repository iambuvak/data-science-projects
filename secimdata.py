import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını okuma
df = pd.read_csv('./data/book-data.csv')

# En çok okunan yazarı bulma
en_cok_okunan_yazar = df['Kitap Yazarı'].value_counts().idxmax()

# En çok okunan konuyu bulma
en_cok_okunan_konu = df['Konusu'].value_counts().idxmax()

# Toplam sayfayı hesaplama
toplam_sayfa = df['Sayfa'].sum()

# Ortalama okunan sayfayı hesaplama
ortalama_sayfa = df['Sayfa'].mean()

# Toplam okunan süreyi hesaplama
toplam_sure = df['Okunan Süre'].sum()

# Okuma günü hesaplama
okuma_gunu = toplam_sure / 24  # Örneğin, saat cinsinden hesaplama, 24 saate bölünerek güne dönüştürülebilir.

# Sonuçları ekrana yazdırma
print(f"En çok okunan yazar: {en_cok_okunan_yazar}")
print(f"En çok okunan konu: {en_cok_okunan_konu}")
print(f"Toplam sayfa: {toplam_sayfa}")
print(f"Ortalama okunan sayfa: {ortalama_sayfa:.2f}")
print(f"Toplam okunan süre: {toplam_sure} saat")
print(f"Okuma günü: {okuma_gunu:.2f} gün")

# Grafik oluşturma
df['Konusu'].value_counts().plot(kind='bar')
plt.title('En Çok Okunan Konular')
plt.xlabel('Konu')
plt.ylabel('Okuma Sayısı')
plt.show()
