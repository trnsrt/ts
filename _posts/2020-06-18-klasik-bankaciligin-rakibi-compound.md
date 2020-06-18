---
layout: post
title:  "Klasik bankacılığın rakibi Compound"
date:   2020-06-18 12:47:56 +0300
categories: Genel
tags: Yazılar DeFi
---

Kripto dünyasında ise DeFi hareketi benzer şekilde bize yeni alternatifler sunuyor. Henüz çok küçük ve deneyseller. Ama belli bir potansiyel sağlayacakları kesin. Gelin bugün bu alandaki ilginç yapılardan [Compound](https://compound.finance/)'a bakalım: 

Günümüzde klasik bankacılığın karşısına pek çok rakip çıkıyor. Özellikle Avrupa ve Amerika'da adına [Neobank](https://en.wikipedia.org/wiki/Neobank) denen yeni oluşumlara her geçen gün yenileri ekleniyor. Bunlar mevcut bankacılık hizmetlerini çok daha ucuza sağlıyorlar. Neden? Temelde klasik bankaların geçmişten gelen artık kemikleşmiş maliyetlerinin hiçbirine sahip değiller. 

### Nedir bu Compound?

[Compound](https://compound.finance/) klasik bankacılık sisteminin bir alternatifi. 

Klasik bankacılık en basit tarifi ile aslında mevduat sahiplerinin yatırdığı paraların ihtiyaç sahiplerine kredi olarak verilmesi. Mevduata verilen ile kredilere uygulanan faizler arasındaki fark da esas olarak bir bankanın kâr marjı (spread). 

Compound da benzer şekilde mevduat sahipleri ile kredi verenler arasında banka benzeri çalışan Ethereum üzerine kurulu bir sistem. 

&nbsp;

| ![Bank by Ethereum](/assets/money-3405700_640.jpg)| 
|:--:| 
| *([Kaynak](https://pixabay.com/illustrations/money-bank-business-finance-3405700/))* |

&nbsp;

### Nasıl çalışıyor sistem?

Compound sisteminde bireyler ellerindeki kripto paraları mevduat olarak yatırıp faiz kazanıyorlar. İhtiyacı olan bireyler ise bu faizin bir miktar fazlasına bu kripto paraları kredi olarak kullanıyorlar. Bu "bir miktar fazla" Compound'un bu işten aldığı komisyon. Bankalara göre çok daha az.

#### Faiz nasıl belirleniyor?

Sistemin faiz belirleme yöntemi aslında bankalara benziyor: Kredi isteyen ve mevduat yatıranların sayısına ve oluşturduğu havuza, yani arz ve talebe göre bir algoritma tarafından hesaplanıyor faiz. 

Ne sıklıkla? Çok! Ethereum üzerine kurulu bir sistem olarak Ethereum blok zincirine paralel şekilde borç verenlere ya da alanlara uygulanacak faiz her 15 saniyede bir belirleniyor. 

Basitçe denge sistemi ile çalışıyor sistem: Örneğin, faizlerin düşmesi durumunda mevduat sahiplerinin paralarını çekeceği, bunun da faizleri artırarak yeni bir denge oluşturacağı şeklinde özetlenebilecek temel ekonomik prensiplere dayanıyor. 

#### Faiz çok oynak görünüyor, ya sisteme giriş-çıkış nasıl oluyor?

Şunu da hemen belirtelim. neredeyse anlık değişen faize paralel olarak sisteme giriş çıkış da istenildiği zaman yapılabiliyor. Yani kredi aldığınızda istediğiniz zaman geri ödeyebiliyorsunuz. Aynı şekilde mevduat yaptığınızda da istediğiniz zaman paranızı çekebiliyorsunuz. 

#### Tahsilat riski nasıl aşılıyor?

Peki bankacılığın meşhur olayı "alacak riski (counter-party risk)" nasıl bertaraf ediliyor? Diğer DeFi projelerine (örneğin MakerDAO) benzer şekilde kredi alanın belli bir kripto parayı teminat olarak yatırması gerekiyor Compound sisteminde. Her kripto paranın teminat oranı farklı. En likit olan örneğin ETH en düşük teminat oranına sahip.

#### Hangi paralarda işlem yapılabiliyor?

Şu aşamada ETH, WBTC (Bitcoin'in değerine eşit ETH bazlı bir sentetik para), Augur gibi Ethereum bazlı kripto paralar ile USDC, Tether, DAI gibi sabit paralar ile mevduat yapabilir ya da kredi alabilirsiniz sistemden. 

#### Kimler kullanıyor?

Neden bir kişi sistemden borç almak ister? Teminat verecek kadar "param" varsa neden borç almak isteyeyim? Temel nedeni spekülatif hareketler. Örneğin bir nedenle sabit bir paraya sıkıştınız ancak elinizdeki ETH'i satmak istemiyorsunuz çünkü artacağını düşünüyorsunuz. Böyle bir durumda bu ETH'i teminat gösterip karşılığında ETH kredi alabilirsiniz. 

Neden borç verirsiniz peki? Yatırım amaçlı. Bir süreliğine kenarda tutmak istediğiniz bir paraya faiz kazanmak isterseniz bu sistem tam size göre. 

### Kim kurmuş bu Compound'u? Güvenilir mi peki?
Compound'u kuran ekip tecrübeli, ayrıca arkalarında teknoloji dünyasının en prestijli girişim sermayeleri var. Daha önce pek çok büyük kripto projesine yatırım yapmış [a16z](https://a16z.com/crypto/) ve [polychain capital](https://polychain.capital/) ve ABD'nin en büyük borsası [Coinbase](https://www.coinbase.com/)'in yatırım [fonu](https://ventures.coinbase.com/) bunlardan en belirgin ikisi. Bir DeFi hareketinin temel özelliği olarak tamamen şeffaf yürütülen sistem hem yatırımcılara hem de kullanıcılara bir nebze iç rahatlığı verebilir. Görebildiğim kadarıyla sistemdeki tek kapalı noktaya gelelim şimdi. 

#### Tamamen merkeziyetsiz mi?
Hayır. Merkeziyetsizlik "[uzun ince bir yol](https://www.youtube.com/watch?v=PXw3f9YTqV0)" ise Compound bu yolun ilerisinde ama sonunda değil. Olacak mı, o da belli değil açıkçası. 

Merkezilik nerede var? Öncelikle, geliştiren ekip merkezi ama bu o kadar da kritik değil. 

Asıl kritik olan, kredi alanlara hangi faiz oranı uygulayacağına bir "robot" karar veriyor. Peki bu robot nasıl karar veriyor? Compound'un içindeki (içeriği çok da bilinmeyen) bir algoritma sistemdeki arz ve talebe göre faizi belirliyor. Yani arz ve talep toplanıp bir havuz şeklinde düşünülüyor. 

Eğer tam merkeziyetsiz bir yapı düşünüyor olsaydık, o zaman direkt alıcı ile verici  pazaryeri misali birbirleri ile direkt biraraya gelebilirdi. O zaman da böyle bir karar kutuya ihtiyaç olmazdı. Birkaç yıl önce Dharma protokolü böyle bir niyetle ortaya çıktı ancak o projenin çok başarılı olduğu söylenemez. 

### MakerDAO'dan farkı ne?
[MakerDAO](https://makerdao.com/en/), DeFi dünyasının en büyüğü ancak daha karışık olduğu için DeFi hareketine Compound'u ile başladık. 

Compound, MakerDAO'ya göre bir parça daha basit. Bir analoji vermek gerekirse, Compound bir banka, MakerDAO ise merkez bankası. 

Belki de bu nedenle MakerDAO kendi sistemini sürdürmek için bir sabit para ([DAI](https://community-development.makerdao.com/makerdao-mcd-faqs/faqs/dai)) yaratmışken, Compound'da benzer bir para yok - onlar DAI de dahil başka paraları kullanıyorlar, aynı bir banka gibi. 

Compound'un nihai hedefi, faizi belirlemede bir gösterge olacak, üzerine pek çok başka uygulamanın yazıldığı, kurucularının hakimiyetinden uzaklaşmış merkeziyetsiz bir protokol olmak. 

Öte yandan Compound'un MakerDAO'dan bir diğer farkı da yönetim kısmında. Her iki sistemde de yönetim hakları için bir token çıkarılmış durumda: MakerDAO için [MKR](https://community-development.makerdao.com/makerdao-mcd-faqs/faqs/mkr-token), Compound için ise 2020 Haziran ayında çıkan COMP. 

Daha önce çıkan MKR özellikle Mart 2020'deki genel düşüş sonrasındaki aylarda çok ciddi değer kazandı. Fiyatı çok oynak olsa da yaklaşık 550 milyon ABD doları bir piyasa değerine sahip.
&nbsp;

| ![MakerDAO market cap](/assets/MKR_market_cap_800.png)| 
|:--:| 
| *MakerDAO tokeni MKR'in 2020 yılı piyasa değeri değişimi ([Kaynak](https://www.coingecko.com/en/coins/maker))* |

&nbsp;

Compound ise bu yazının yazıldığı tarih itibariyle henüz çok yeni. Ancak MKR'nin bu kadar ilgi görmesinden üzerine, muhtemelen yatırımcılarda oluşan FOMO (Fear of missing out - bir şeyleri kaçırma korkusu) nedeniyle ilk çıktığı fiyata göre bir haftada yaklaşık 80 kat değer kazandı (sonra düştü). Piyasa değeri yazının yazıldığı hafta içinde yaklaşık 520 milyon ABD Doları civarında. 

COMP tokenı üzerine bir değerlendirme yapmak için henüz çok erken. Yatırımcılar bu parayı MKR ile karşılaştırıyor olsalar da aslında "şeytan ayrıntıda gizli". Compound'un COMP'u ile MakerDAO'nun MKR'ı aslında birbirinden çok farklı tokenlar. Neden?

En basitinden MKR tokenı sahipleri bu parayı sadece MakerDAO sistemini yönetmek için kullanmıyorlar. Aynı zamanda sistemin kâr ya da zararına da ortaklar (bunun detayına MakerDAO'dan bahsedeceğimiz bir sonraki yazıda değineceğiz). 

COMP ise Compound'un CEO'sunun kendi ağzından yaptığı açıklama ile herhangi bir ekonomik değer atfedilmeden yalnızca sistemin yönetimi konusunda söz sahibi olacak bir token. Dolayısıyla her iki tokenı aynı kefeye koyup değerlendirmek elma ile armutları karşılaştırmaya benziyor. 

### Sonuç

Compound DeFi hareketinin MakerDAO ile birlikte ilk öncülerinden. Üzerine kurulacak farklı uygulamalar ile birlikte gelecekte adını daha sık duyma ihtimalimizin yüksek olduğu bir para piyasası aracı. Gelecek heyecan verici - hep birlikte takip edeceğiz.


Not: Bu yazı ilk olarak 18 Haziran 2020'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/klasik-bankaciligin-rakibi-compound/)
