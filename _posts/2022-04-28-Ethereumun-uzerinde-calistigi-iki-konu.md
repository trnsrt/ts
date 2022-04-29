---
layout: post
title:  "Ethereum'un üzerinde çalıştığı iki konu"
date:   2022-04-28 17:47:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Ethereum'un yeni versiyonunu incelediğimiz bir önceki [yazımızdan](/genel/2022/04/20/yeni-ethereumu-beklerken.html) sonra, şimdi de işin derinine iniyoruz.

Önce geçtiğimiz yazıyı kısaca özetleyelim: Ethereum büyük bir dönüşümden geçiyor. Bunu yaparken başlangıçta koyduğu planın kimi parçalarını hayata geçirirken kimilerini de rafa kaldırdılar. Bu yazımızda, yeni versiyonun üstesinden gelmeyi planladığı iki değişiklik olan enerji tasarrufu ve ölçeklenebilirlik konularına daha detaylı bir şekilde bakacağız. 

### Sistem güvenliğinde enerji tasarrufu (PoS'a geçiş)
Enerji tasarrufu konusu gerek Bitcoin gerekse de Ethereum'un zayıf karnı denilebilir. Bitcoin tarafından kullanılan PoW (proof-of-work; Türkçesi 'iş kanıtı') mekanizması, Ethereum tarafından da benimsenmişti. Bu mekanizma, blokzincir üzerindeki güvenliğin sağlanabilmesi için, sistemi yürüten onbinlerce makinenin enerji harcaması esasına dayanıyor. Ethereum sonrası çıkan pek çok yeni blokzincir ise, bunun yerine PoS (proof-of-stake; Türkçesi 'hisse kanıtı') adı verilen başka bir mekanizma kullandılar. 

Bitcoin topluluğu felsefi olarak PoW'u bırakmayıp devam ederken Ethereum topluluğu PoS sistemini sevdi ve kendini o sisteme geçmek için hazırlamaya başladı. PoS sistemi sayesinde Ethereum'un enerji harcaması %99 oranında düşecek. Dolayısıyla bundan sonra bazı politikacıların kulaktan dolma bilgilerle çok sık kullandıkları 'ama blokzincir çok enerji harcıyor' argümanı ile bundan böyle sadece Bitcoin topluluğu muhatap olacak. 

| ![Pow_Pos_consumption](/assets/ethereum_power_consumption_v3_800.png)|
|:--:| 
| *İş Kanıtı (PoW) ve Hisse Kanıtı (PoS) sistemlerinin enerji tüketimi. Kaynak: [Ethereum](https://blog.ethereum.org/2021/05/18/country-power-no-more/).*|


Ethereum'da PoS'e geçiş sadece teoride kalmış değil, uzunca bir süredir pratik olarak da yol almış durumda. PoW mekanizmasında sistemi yürüten madenciler, PoS'da yerlerini ETH kilitleyerek sistemi koruyacak olan onaylayıcılara bırakıyorlar. Aralık 2020'den itibaren başlayan PoS sisteminde insanlar (ya da kurumlar) ellerindeki ETH'yi belirli bir faiz oranı karşılığında rehin etmeye ve onaylayıcı olmaya başladılar. Aradan sadece 15 ay geçmiş olmasına rağmen şu ana kadar [11.7 milyon ETH](https://beaconcha.in/) yani [toplam dolaşımdaki ETH'nin](https://etherscan.io/stat/supply) %9.7'si sisteme kilitlenmiş durumda. 

| ![total_staked_ETH](/assets/Ethereum_ETH_2_0_Staking_Rate_v3_800.png)|
|:--:| 
| *2020 Aralık'tan bu yana stake edilen ETH'nin toplam ETH'ye oranı. Kaynak: [CryptoQuant](https://cryptoquant.com/asset/eth/chart/eth2/eth-20-staking-rate-percent?window=DAY&sma=0&ema=0&priceScale=linear&metricScale=linear&chartStyle=column).*|

Bu değişiklik aslına bakarsanız son aşamaya gelmiş durumda ve planlandığı gibi gidiyor. Asıl sancılı süreç ölçeklenme konusunda yaşanıyor.  

### Sistemi ölçeklendirme (Sharding çözümü)
Ethereum'un 2020 ve 2021 yıllarında yaşadığı yoğunluk sonrası işlem ücretleri arşa çıktı. Niye bu kadar büyük bir yoğunluk yaşandı? Yaşanan sorun hızlı bir şekilde çözülemez miydi? 

Sorunun arkasında yatan neden, blokzincirlerin aslında çok kısıtlı bir kapasiteye sahip olması. Daha önceki yazılarımızda da belirtmiştik; blokzincirler öyle çok üstün süpersonik teknolojiler değiller. Üstelik yapıları gereği çok verimli de çalışmıyorlar. Aslına bakarsanız evinizde kullandığınız son model bir bilgisayarın işlem gücü, blokzincirin kapasitesinden çok daha üstün. Neden blokzincire ihtiyaç duyuyoruz o zaman? 

##### Neden blokzincire ihtiyaç duyarız?
Blokzincir aslında bize çok da farkında olmadığımız özel bir hizmet sunuyor; o da 'kimseye güven duymak zorunda olmamak'. Blokzincirin yaptığı işi çok daha verimli olarak bir sunucuda duran bilgisayar ile yapabilirsiniz. Gayet de güzel olur. Sorun ne peki?  Sorun o bilgisayarın sahibinin kim olduğu ve içine yazılanların, sahibi ya da başka bir güç tarafından değiştirilip değiştirilemeyeceği. İşte blokzincir, birbirinden bağımsız binlerce makinede çalışarak herhangi bir kişi ya da kurumun sistemi kendi nüfuzu altına almasına engel oluyor. İyi de gerçekten ihtiyaç var mı buna? 

Bunu kestirmek oldukça zor. Gündelik hayatımızda bugün çok ihtiyaç duymayabiliriz ama bu durum her an değişebilir. İsterseniz, Donald Trump'a bir sorun bunu: Bir gecede Twitter'daki 80 milyon takipçisini kaybettiğinde 'sesini kaybetmiş' gibi hissetti mi? Ya da Facebook üzerine oyun geliştirip ekmek parası kazanmayı uman geliştiriciler bir gece ansızın aldıkları bir mesaj ile platformdan atıldıklarında nasıl bir şok yaşadılar acaba? Ya da Rusya Merkez Bankası'na sorun bakalım, batıda tuttukları 400 milyar dolara el konulduğu gece uyuyabildiler mi?

İşte blokzincirler kullanıcılarına 'üzerlerine yazılı hiçbir bilginin değişmeyeceği' güvenini verebilmek için binlerce makineye ihtiyaç duyarlar. Binlerce makinenin sistemi yürütebilmesi için de, sistemin ve işlenecek bilgileri küçük tutmaları gerekir. Zira blokzincirin kapasitesi kısıtlı ve içinden olabildiğince farklı işlemi geçirebilmek için bu gerekli. Aksi takdirde kapasite dolduğunda sistem haraç mezat misali en yüksek parayı verenin işlemini gerçekleştiriyor, bu da işlem ücretlerini artırıyor. 

Neden bilginin yazılacağı alanı genişletip kullanıcıları rahatlatmıyorlar? Böyle bir durumda birkaç sorun çıkıyor ortaya. Blokzincirde yaptığınız her işlemin sisteme işlenmesi ve kaydedilmesi gerekiyor. Hem de bu onbinlerce makine tarafından. Eğer siz bilginin yazılacağı alanı genişletirseniz (yani her bir bloğu büyütürseniz) bunu işleyecek (ve birbirleri ile eş şekilde güncelleyecek) makine sayısı azalır (sonuçta bilgisayarların bir kapasitesi var) ve ortada sadece yüksek performanslı makineler kalır. Böyle olunca merkeziyetsizlikten ödün vermiş olursunuz, bu da sistem güvenliğini tehlikeye atabilir. Zira baktığınızda bin makineyi ele geçirmek on bin makineyi ele geçirmekten çok daha kolay bir iş. 

İşte bu nedenle, Ethereum geliştiricileri, merkeziyetsizlikten ödün vermemek adına, sistemi daha geniş kapasiteli yapma yoluna gitmediler. Bunun yerine farklı çözümler denediler. 

#### Ethereum'un ölçeklenme sorunu hikayesi
Ethereum'un ölçeklenme sorunu için bulduğu çözüme geçmeden önce Ethereum'un nasıl çalıştığına bir parça daha değinmekte fayda var. 

Ethereum bir 'akıllı kontrat platformu'. Bu ne demek? Üzerinde akıllı kontratların çalıştığı bir işletim sistemi (telefonunuzdaki iOS ya da Android gibi). Akıllı kontratlar da aslında telefonunuzdaki uygulamalar. Bu uygulamalar ilk kurulduklarında blokzincire yazılıyorlar. Daha sonra siz ne zaman işlem yapmak isterseniz bu kontratlar Ethereum blokzinciri üzerinde çalışarak işleminizi gerçekleştiriyorlar. İşte bu sayede yaptığınız her işlemi blokzincirin şeffaf yapısı sayesinde tam olarak izleyebiliyorsunuz.

Sorun da aslında burada başlıyor. Yukarıda daha fazla makinenin sistemi yürütebilmesi için blokların ufak tutulması gerektiğini söylemiştik. Bu akıllı kontratların gerçekleştirdiği işlemler özellikle karmaşık olduklarında bu bloklarda çok yer tutuyorlar. Böyle olunca bloklar hızlı doluyor ve işlem ücretleri arşa çıkmaya başlıyor.

Ethereum ekibi başlangıçta bu sorunu çözmek için, Ethereum'u 64 ayrı blokzincire bölerek ('sharding') kapasitesini artırmak gibi bir plan ortaya attılar. Böyle bir durumda işlemler ayrı blokzincirlerde yapılacak ve sonra bir ana zincir üzerinde toplanacaktı. Her ne kadar kapasiteyi artırsa da bir süre sonra bu çözümün de yeterli olmayacağı görüldü. İşte o nedenle geçtiğimiz aylarda yavaş yavaş bu planı da değiştirmeye başladılar. Nasıl bir yola girdiler? Birbiri ile bağlantılı iki uygulamaya ağırlık verdiler.

##### Birinci çözüm: İkinci seviye çözümler (bir diğer deyişle dürüm yani 'roll-up' sistemler)
Ethereum geliştiricileri başta Vitalik olmak üzere geçtiğimiz yıl hararetle ikinci seviye çözümleri ön plana çıkarmaya başladılar. 

İkinci seviye çözümler, Ethereum ekibi tarafından değil, bağımsız geliştiriciler tarafından geliştiriliyorlar. Temel olarak yaptıkları bizim bilgisayarlarda kullandığımız 'zip' dosyalardan farklı değil. 'Zip' dosyaları bilirsiniz; on tane Excel dosyasını bir zip dosyası haline getirirseniz, boyutunu aşağı yukarı onda birine indirirsiniz. İşte ikinci seviye çözümler de yapılan onlarca işlemin Ethereum üzerinde değil, kendi üzerlerinde yapılmasını sağlayıp, sadece sonuçlarını Ethereum üzerine yazıyorlar. Bu sayede yüzlerce işlemi tek bir büyük işlem gibi yazabilme imkanı doğuyor, bu da işlem maliyetlerini ciddi bir şekilde azaltıyor. 

İkinci seviye çözümler güvenli mi? Güvenirlik oldukça göreceli bir kavram. Öncelikle, paranızın güvende olup olmadığı perspektifinden bakıyorsanız, evet. Zira paranız Ethereum blokzinciri tarafından korunuyor. Yan zincirlerde örneğin Polygon'da paranızı yan zincir koruyor ve o zincirde bir sorun olursa paranız tehlikeye girebiliyor. Ya da Polygon zinciri durdu, paranıza erişemiyorsunuz (Solana'da çok sık yaşanan bir durum bu). İkinci seviye çözümlerde ise çözümde bir sorun olsa bile siz paranızı Ethereum üzerinde tutuyorsunuz ve başka çözümler kullanarak işleminizi gerçekleştirebilirsiniz. Bir diğer risk ikinci seviye çözümlerin yazılım kodlarında problem olma olasılığı ama Vitalik dahil Ethereum ekibi burada bir sorun görmüyor ve rahatlıkla bu çözümleri kullanıcılara [önerebiliyorlar](https://vitalik.ca/general/2021/01/05/rollup.html).

#### İkinci çözüm: Eth2'ye sadece sonuçları yazmak
Roll-up sistemlerine verilen ağırlık dışındaki ikinci önemli değişiklik ise yeni versiyonun mimarisinde yapıldı. Herhangi bir kullanıcının tüm işlemleri Ethereum üzerinde yapması tam bir şeffaflık getirse de yoğunluğa neden oluyordu. Yeni Ethereum her ne kadar kapasiteyi 64 katına çıkarsa da yine de yetmeyecekti. Bu nedenle, Ethereum geliştiricileri, kapasiteyi yine 64 kata çıkardılar ama önemli bir değişiklik ile. Sistemde işlemlerin hesaplanmasını değil, işlemlerin sadece sonuçlarını blokzincire yazıyorlar. İşlem hesaplamaları ise yukarıdaki roll-up çözümlere bırakılıyor. Bu, yer işgali anlamında muazzam bir tasarruf demek.

### Sonuç
Ethereum, PoW mekanizmasından PoS'e geçmeye uzun süredir hazırlanıyor ve bu alanda önemli bir sıkıntı görülmüyor. Asıl değişikliklerin yaşandığı ve 'kervanın yolda düzüldüğü' ölçeklenme konusunda, yolun başına göre artık çok daha rahat bir durumdalar. Bakalım, son dakika golleri olmadan rahat bir şekilde maçı bu yıl içinde tamamlayabilecekler mi?


*Not 1: Bu yazı ilk olarak 28 Nisan 2022'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı(https://www.btchaber.com/ethereumun-uzerinde-calistigi-iki-konu/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*
