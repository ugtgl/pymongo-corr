# Korelasyon aracı



## Kurulum

#### Pycharm için:

Yeni bir proje oluşturun ardından main.py, thewidget.py, tasarim.ui ve requirements.txt dosyalarını projenin kök dizinine atın.

PyCharm proje terminalinde şu komutu girin:

```
pip install -r requirements.txt
```



#### Anaconda için:

Yeni bir klasöre main.py, thewidget.py , tasarim.ui ve requirements.txt dosyalarını atın ve klasörde Anaconda Prompt başlatın. Ardından sırasıyla şu komutları girin.

```
conda create korelasyon
conda activate korelasyon
conda install --file requirements.txt
python main.py
```



#### Sisteme kurulmuş Python:

##### Windows:

main.py, thewidget.py, tasarim.ui ve requirements.txt dosyalarını bir klasöre atın.

Klasörde komut istemi açın ve sırasıyla şu komutları girin:

```
pip install -r requirements.txt
python main.py
```

##### Linux

main.py, thewidget.py, tasarim.ui ve requirements.txt dosyalarını bir klasöre atın.

Terminali başlatın ve **cd** komutu ile klasörün bulunduğu yolu seçin.

```
python main.py
```

ile çalıştırın.





## Çalışma mantığı:

1.  MongoDB client bağlantısı kur.
2.  Kullanıcının sağ tarafta seçtiği dropdown seçeneklerine göre belirlenen database'den belirlenen collection'ı getir.
3.  İşlenecek veri object içinde array'de tutulduğu için bir üst kısma taşı.
4.  Verilerin işlenebilmesi için nümerik verilere dönüştür, dönüşmeyenleri NaN olarak gir.
5.  Tüm kolonların korelasyonunu hesapla, kullanıcının istediği kolonların korelasyonunu da yazdır.
6.  Kullanıcının okumasını zorlaştırdığı için tekrarlanan verileri sil, üst üçgensel matris ve alt üçgensel matris değerleri aynı olduğu için üst üçgensel matris değerlerini sil.
7.  Korelasyon matrisini seaborn heatmap kullanarak Qt5 widget içerisinde göster.
8.  Korelasyon değerlerini dosyaya kaydet, çok küçük değerleri kaydederken sorunları engellemek için değerlerin ondalık kısmını sadece 3 basamak olarak kaydet.