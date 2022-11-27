---
layout: post
title:  "Blokzincirin geleceği geliştiricilerin elinde"
date:   2022-01-31 17:47:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Bu yazımızda Ocak ayı başında yayınlanan Electric Capital'in Geliştirici (Developer) Raporu üzerinden farklı blokzincir platformları ve üstlerine kurulu girişimlerin gelişimine bakacağız. 

En sık karşılaşılan sorulardan biridir: Hangi blokzincir daha büyük, hangisinin potansiyeli daha yüksek? Bu soruların elbette net bir yanıtı yok, bunun da temel birkaç nedeni var. 

### Karşılaştırma yapmak neden zor?

Öncelikle sağlıklı ve tarafsız bir veriye ulaşmak oldukça zor. Blokzincirlerin kendi açıkladıkları verilerde genelde kuvvetli taraflarına ışık tutup, göreceli zayıf taraflarını gizlemeye çalışırlar. "Hiç kimse ayranım ekşi demez" sonuçta.

"İyi ama işlemler blokzincire yazılıyordu, bilgi zaten şeffaf değil miydi?" Haklısınız. Yine de blokzincire yazılan verilerin bile manipüle edilmesi riski var. İşlem hacimlerinde "wash trading" dediğimiz hacim artırma klasik borsalarda sık yaşanan bir olay, blokzincir üzerinde de pekala yapılabilir. 

Öte yandan ne kadar iyi niyetli olursanız olun ya da elinizde blokzincirin yarattığı milyonlarca data olsun, objektif kriterler ya da belli bir standarda oturmuş parametreler yok ortada. Hangi kriteri kullandığınıza göre değerlendirmeler çok değişiyor. Bakılabilecek kriterler neler olabilir?

- Piyasa değerleri (ingilizcede Market Cap kısaca mCap - piyasada dolaşımda olan ya da toplam token adedi üzerinden)
- Sisteme kilitlenmiş değer (ingilizcede 'Total Value Locked' kısaca TVL)
- Başka blokzincirlerden köprüler aracılığıyla transfer edilmiş değer
- Sistem üzerinde çalışan uygulama sayısı (ingilizcede 'decentralized app' kısaca dApp)
- Bu uygulamaların işlem hacimleri
- Sistemleri kullanan cüzdan (bir diğer deyişle) hesap sayısı
- Ne kadar merkeziyetsiz olduğu (validatör sayısı)
- Sisteme ve üzerindeki girişimlere akan girişim sermayesi yatırımları

Yukarıdaki parametrelerin her biri farklı insanlar tarafından farklı şekillerde kullanılabilir. Bugün gelin, şahsen blokzincirleri karşılaştırmada en önem verdiğim raporlardan biri olan Electric Capital geliştirici raporuna göz atalım.

### Neden önemli bu rapor?
2019 yılından beri toplanan veriler üzerinden yayınlanan [geliştirici raporu](https://medium.com/electric-capital/electric-capital-developer-report-2021-f37874efea6d) ([pdf](https://github.com/electric-capital/developer-reports/blob/master/dev_report_2021_updated_012622.pdf)) blokzincirler üzerinde çalışan geliştirici sayısının yıldan yıla değişimini gözlemeye çalışıyor. 

Geliştirici sayısı bir blokzincir ekosisteminin nereye doğru evrilmekte olduğunu göstermesi açısından önemli. Bir blokzincir üzerinde ne kadar çok geliştirici çalışıyor ise, beklenti o zincirin teknolojik olarak yenilik yapma ya da ürün çıkarma potansiyelinin o kadar yüksek olması yönünde oluyor. Sadece farklı zincirleri karşılaştırmak için kullanılmıyor bu rapor.  Bir blokzincir üzerinde bir yıl içinde oluşan gelişimci sayısındaki değişimi dolayısıyla o blokzincire olan ilginin ne şekilde geliştiğini anlatması açısından da faydalı.

| ![dandelion](/assets/dandelion-g3a7c93841_800.jpg)|
|:--:| 
| *Image by [adege](https://pixabay.com/users/adege-4994132/) from [Pixabay](https://pixabay.com/)*|


Yaklaşık 100'den fazla gönüllünün veri toplama üzerinde çalıştığı toplam 500,000'den fazla Github kod kaynağında bulunan 160 milyondan fazla kod yüklemesinin incelendiği rapor hayli detaylı. Üstelik tüm bu kaynakları tek tek inceleme şansı da [mevcut](https://electric-capital.github.io/). 

Gelin şimdi de raporun detaylarına hızlıca bakalım:

### Raporun detaylarında neler var?

Öncelikle büyük resme bakalım. Yıllar içinde blokzincir ya da merkeziyetsiz sistemlerin artık yeni adı olan Web3 alanında çalışan geliştirici sayısı nasıl gelişmiş?

| ![gelisim](/assets/web3_ecosistem_grafik_sayfa_119_800.jpg)|
|:--:| 
| *Yıllar itibariyle Web3 geliştirici sayıları değişimi. Kaynak [Electric Capital Developer Report](https://medium.com/electric-capital/electric-capital-developer-report-2021-f37874efea6d) - Sayfa 119*|

2017 yılındaki ICO patlaması ile birlikte ciddi bir artış gösteren Web3 üzerinde çalışan geliştirici sayısı, sonraki üç yıl bir duraksamaya girmişti. Sonrasında Web3'ün finans kolu DeFi'nin (merkeziyetsiz finans) ön plana çıkması ile birlikte geliştiricilere olan talebin ciddi şekilde arttığını görüyoruz. 2021 yılı içinde ekosisteme akan girişim sermayesi rakamının 8 katına çıkmasının, bu alana geliştirici çekmesinde bir etken olduğunu da söyleyebiliriz.  Tabii blokzincirlere ait tokenlerin değerlerinin artmasının da önemli nedenlerden biri olduğunu unutmamak gerek. 

Peki Web3 ne kadar büyük? Gelin bir de büyük resime bakalım: 

| ![buyuk_resim](/assets/web3_ekosistem_grafik_sayfa_122_800.jpg)|
|:--:| 
| *Web3 ile dünyadaki tüm geliştiricilerin karşılaştırması. Kaynak [Electric Capital Developer Report](https://medium.com/electric-capital/electric-capital-developer-report-2021-f37874efea6d) - Sayfa 122*|

Gördüğünüz gibi Web3 henüz emekleme aşamasında. Bunu 'henüz çok küçük, dikkate almaya değmez' ya da 'burada büyük potansiyel var' olarak iki farklı şekilde okuyabilirsiniz, size kalmış.

İyi ama Web3 için çalışan bu geliştirici sayısı nasıl bulunuyor? Yukarıda bahsettiğimiz 500 binin üzerindeki GitHub kaynağına (repository) ekleme/güncelleme yapan geliştiriciler toplanarak (tüm detaya [şu link](https://electric-capital.github.io/)ten ulaşabilirsiniz). 

Peki tek tek blokzincirleri incelediğimizde durum ne? Ekosisteme bir bütün olarak baktığımızda karşımıza aşağıdaki gibi bir tablo çıkıyor: 

| ![tum_blokzincirler](/assets/smart_platform_L_devs_v2_sayfa_64.jpg)|
|:--:| 
| *Blokzincir ekosistemi. En büyük 5 zincir. Kaynak [Electirc Capital Developer Report](https://medium.com/electric-capital/electric-capital-developer-report-2021-f37874efea6d) - Sayfa 64*|

Öncelikle grafiği nasıl okuyacağımıza kısaca değinelim: Yatay eksen 2020 yılı sonunda her bir blokzincir üzerinde çalışan toplam geliştirici sayısını gösteriyor. Dikey eksen ise aynı blokzincirin 2021 yılı sonundaki geliştirici sayısını. Grafiği ortadan çapraz bölen kırık çizgiye dikkatinizi çekerim. Bu çizginin üst tarafında bulunan blokzincirler bir yıl içinde geliştirici sayısını artırmış, altında kalanların ise geliştirici sayısı azalmış, çizginin üstü ise sabit kalmış.  Bir nokta daha; eğer bir blokzincir ne kadar dikey eksene yakın ise, bir yıl öncesine göre geliştirici sayısı o kadar fazla artmış anlamına geliyor. 

Gördüğünüz gibi, ekosistem olarak geliştirici sayısı en büyük 'mahşerin beş atlısı' Ethereum, Polkadot, Cosmos, Solana ve Bitcoin olarak sıralanıyor.  Burada en yüksek ivmeyi yaklaşık dört kat artış gösteren Solana'da görüyoruz. Bunun temel nedeni Solana'nın yıl içinde üzerine kurulu olan girişimlere verdiği teşvikler olabilir. Bitcoin geliştirici sayısı ise aynı kalmış. Bu da beklenen bir durum zira, Bitcoin kendisini teknolojik olarak gelişen bir platform olarak değil güvenilir bir para olarak tanımlıyor. Bu da geliştirmelerin ağır ve emin adımlarla yapılmasına neden oluyor. Bitcoin üzerine yeni sistemler kurmak benzer şekilde oldukça güç, bu da blokzincir dünyasına yeni giren girişimcilerin Bitcoin sistemi yerine diğer sistemlere yönelmesine yol açıyor. 

Tabii grafikteki asıl 'fil' Ethereum. Neredeyse kendinden sonra gelen dört sistemin toplamı kadar geliştiriciye sahip. Üstelik 2021 yılı içinde bile yaklaşık %20 artış göstermiş geliştirici sayısı. Tabii Ethereum diğer blokzincirlere bu kadar fark atınca, grafikteki daha küçük oyuncuları görmek oldukça zor oluyor. Gelin sol alt taraftaki kalabalık gruba zoom yapalım şimdi de: 

| ![300den_buyuk_blokzincirler](/assets/smart_platform_L_devs_v3_sayfa_67.jpg)|
|:--:| 
| *Blokzincir ekosistemi. Ethereum ve Polkadot dışındaki büyük platformlar. Kaynak [Electric Capital Developer Report](https://medium.com/electric-capital/electric-capital-developer-report-2021-f37874efea6d) - Sayfa 67*|

300'den daha fazla geliştiriciye sahip blokzincirleri gösteren bu grafiğe baktığımızda ise, yukarıda bahsettiğimiz beş büyüğün yanına Near, Cardano, Binance Smart Chain, Kusama'nın eklendiğini görüyoruz. Polygon, bir Ethereum yan zinciri olarak geçtiğimiz yıl içinde hem işlem hacmi ve kilitli değer hem de yaptığı satın almalar ile ön plana çıkıyor. Binance Smart Chain de Binance ekosistemi ve maddi gücünü arkasına alarak verdiği teşviklerin karşılığını almış görünüyor. Cardano, Near ve Kusama (ki Polkadot'un testneti olur kendisi) henüz çok aktif olmamalarına rağmen ciddi sayıda geliştiriciye sahip olmaları önümüzdeki dönemde buradan çıkacak olan uygulamaların adlarını daha sık duyacağımız anlamına gelebilir (ya da bir ihtimal geliştiriciler Godot'yu bekler gibi bekledikleri Cardano'dan umudu kesip başka zincirlere yönelebilirler). 

Sol alttaki buluta bir zoom daha yapıp yazımızı sonlandıralım: 

| ![50_300_arasi_blokzincirler](/assets/smart_platform_M_devs_v2_sayfa_72.jpg)|
|:--:| 
| *Blokzincir ekosistemi. Ethereum ve Polkadot dışındaki büyük platformlar. Kaynak [Electic Capital Developer Report](https://medium.com/electric-capital/electric-capital-developer-report-2021-f37874efea6d) - Sayfa 72*|

Tabloda oldukça çok sayıda blokzincir var. İlgi çekici birkaç noktayı kısaca belirtelim. Ülkemizde de oldukça geniş bir topluluğa sahip olan Avalanche, hem 3,5 kata yakın artışı hem de yüksek geliştirici sayısı ile önümüzdeki yıl en büyük platformlar arasında adını yazdırmaya namzet bir aday gibi görünüyor. Öte yandan gizlilik coini Monero, bir zamanlar çok konuşulan ama son zamanlarda esamesi okunmayan EOS ve yine geçtiğimiz yılın gözdelerinden Filecoin'in geliştirici kaybetmiş olması da dikkate değer. 

### Sonuç
Geliştiriciler, teknoloji alanında girişimlerin lokomotif gücü. Aktif oldukları alanlar ve yıldan yıla değişimleri bir nevi 'öncü gösterge' olarak yorumlanabilir. Electric Capital'in bu raporu bu anlamda önemli bir kaynak. 130 sayfalık bu raporun içinde bu satırlara alamadığımız daha pek çok tablo ve detay olarak çıkarılabilecek dersler mevcut. Konuya ilgi duyanların incelemesinde büyük fayda olabilir. 

Blokzincirin şeffaflığını kullanan ve olabildiğince objektif hazırlanmaya çalışılan bu rapor, elbette yüzde yüz ekosistemi yansıtmıyor. Hangi blokzincire sorsanız, muhtemelen raporun kendi güçlerini doğru yansıtmadığını, rakiplerini ise olduğundan büyük gösterdiğini iddia edecek. Bu tip yorumları bir kenara bırakırsak, sadece yıldan yıla değişimleri görmek bile bundan sonrası için bize önemli ipuçları veriyor. Bu tip raporların çoğalması dileğiyle. 

---

*Not 1: Bu yazı ilk olarak 31 Ocak 2022'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/blokzincirin-gelecegi-gelistiricilerin-elinde/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*
