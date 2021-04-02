---
layout: post
title:  "DeFi'nin lider borsası Uniswap'ın son durumu"
date:   2021-04-02 09:47:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Bu yazımızda geçtiğimiz hafta içinde açıklanan merkeziyetsiz takas borsası Uniswap'ın yeni versiyonuna bakacağız hep birlikte: 

Uniswap, merkeziyetsiz finans dünyasının ağır toplarından. Daha önce kendisi ile ilgili iki yazı yazmıştık: Birincisi [Uniswap ve sahip olduğu havuz sistemini](/genel/2020/09/15/nedir-bu-uniswap.html), ikincisi ise [rakiplerini ve farklarını](/genel/2020/09/22/uniswap-rakipleri-curve-balancer-ve-sushiswap.html) anlatıyor. Önce gelin bu yazımızda hafızamızı tazeleyecek bir özet geçelim, şu anki sıkıntıları neymiş görelim, sonraki yazımızda da yeni versiyon neler getiriyor ona bakarız. 

### Neydi bu Uniswap?
Uniswap, klasik borsaların yaptığı hisse alım satım işlemlerini merkeziyetsiz bir şekilde gerçekleştiren bir DeFi protokolü. Sisteminin çalışması klasik borsalardan farklı: 

Klasik borsalarda her bir token ya da hisse senedi için işlem ekranları vardır. Alıcı ve satıcılar işlem yapmak istedikleri miktarları ve fiyatları yazarlar, sonrasında bu taleplerine bir karşılık bulurlarsa işlem gerçekleşir. Bunlara emir defteri işlemleri denir. 

Uniswap ise farklı bir şekilde çalışıyor: Merkeziyetsiz borsalar alım satım işlemleri için yeterince likidite bulamadığından çözüm olarak havuz sistemini kullanıyor. 

"Nedir bu havuz sistemi?" diye soracak olursanız: Bu sistemde her bir havuzun içinde iki adet token var. İşlem yapmak isteyenler bu ikili tokenlardan birini alıp diğerini koyuyor havuza, yani takas yapıyor. Dolayısıyla al-sat yapanlar birbirlerine karşı değil sürekli likidite barındıran bir havuza karşı işlem yapıyorlar.  

Peki havuza tokenları başta kim koymuştu? Likidite sağlayıcı dediğimiz yatırımcılar. Neden likidite sağlıyorlar bu insanlar? Çünkü havuzda takas yapanlar yaptıkları her işlem için komisyon veriyorlar (Uniswap'ta bu binde üç oranında). İşte bu komisyonların neredeyse tamamı likidite sağlayıcılara gidiyor. 

| ![havuzlar](/assets/pool-406743_800.jpg)|
|:--:| 
| *Likidite sağlayanlar havuza katkı yaparken :). Image by [Hans Braxmeier](https://pixabay.com/users/hans-2/) from [Pixabay](https://pixabay.com/)*|

### Neden başarılı oldu?
Uniswap'ın başarılı olmasının küçük büyük pek çok nedeni var. 

Birincisi basit ve şeffaf bir sistem.. Token fiyatları çok basit bir algoritma ile belirleniyor. Her bir havuzda iki token var ve %50-%50 havuzu paylaşıyorlar. Komisyon oranı her havuz için binde üç. Özellikle likidite sahipleri için, 'koy paranı havuza unut git, sonra komisyon gelirlerini topla' şeklinde adlandırılabilecek bir sistem. Al-sat yapanlar için de likidite sıkıntısı olmadan işlem yapabilecekleri bir borsa. 

İkincisi, tamamen merkeziyetsiz ve isteyenin istediği gibi havuz kurabildiği bir sistem.. Bu sayede eskiden finansman bulabilmek ya da tokenlarına likidite kazandırmak için kripto para borsalarının kapısı önünde dilenci gibi bekleyen DeFi ürünleri artık özgürce diledikleri anda halka açılma hakkı elde ettiler. Bu şekilde Uniswap'ta oluşmuş [150'nin üzerinde aktif havuz](https://info.uniswap.org/pairs) var. 

Son olarak, merkeziyetsiz DeFi platformu olarak 'müşterini tanı' yani KYC ilkelerinden uzak olmasının belli kesimleri Uniswap'a çektiğini söylemek de yanlış olmaz.

### Gelelim yeni versiyona

Unsiwap'ın yeni versiyonu (ki buna v3 yani üçüncü versiyon deniyor) 2021'in Mayıs ayı başında [piyasaya sunulacak](https://uniswap.org/blog/uniswap-v3/). Ethereum blokzinciri üzerinde olacak bu yeni versiyonun  hemen arkasından Mayıs ortası gibi de Optimism denen ikinci seviye çözüm devreye girecek. 

Üçüncü versiyonda temel olarak hissedilen, eskinin basit ve sadeliğinden uzaklaşan daha karmaşık bir yapının gelmekte olduğu. Bu değişim, farklı özellikler arayan al-sat işlemcileri ve büyük miktarda likidite sağlayanların işine gelecek ancak küçük hacimli likidite sağlayıcıların hayatları çok zorlaşacak. UNI token sahipleri de yeni özellikler sayesinde daha fazla gelir kazanma ihtimaline kavuşacaklar. Kısacası Uniswap,  DeFi dünyasını şu an oynadığı kum havuzundan daha büyük sahneye çıkarmak için uğraşıyor. Burada hemen  sonda yapacağımız yorumu da ekleyelim: eğer köklerini unutursa, oturduğu halının ayaklarının altından çekildiğini de görebilir her an.

Evet, dönelim Uniswap'ın mevcut sıkıntılarına ve yeni versiyonun neler getirdiğine:

### En büyük sorun: Sığ havuzlar.. 

Uniswap, sistemini dizayn ederken birinci temel ilkesini **havuzdaki likiditenin tükenmemesi** üzerine kurmuştu. Ne demek bu? Havuzu oluşturan iki token çeşidinden de her zaman bulunması ve bu tokenların hiçbir şekilde bitmemesi. Likiditenin bitmemesi güzel bir özellik ama pratikte belli sıkıntıları oluyor. Neler bunlar?

Birincisi, havuzun verimliliğini azaltıyor bu durum. Özellikle likidite sağlayıcılar için. Neden? Çünkü, bu ilke nedeniyle havuzda fiyat her ne olursa olsun alıcılara servis edilecek token bulundurması gerekiyor. Bu da 0'dan sonsuza kadar giden geniş bir aralık için emre amade token bulundurmak demek. 

Bir örnek ile açıklayalım. Geçtiğimiz iki buçuk yıl içinde 1 ETH'nin fiyatı 0.015BTC ile 0.045BTC arasında seyretmiş, bu aralığın dışına çıkmamış. Ama eğer yatırımcı Uniswap'taki ETH/WBTC havuzuna likidite sağlarsa bu para hem bu aralık için hem de aralığın dışı (örneğin 0.0005 BTC ya da 0.95 BTC) için de hazır bekletiliyor. Yani likidite sağlayıcı tarafında ciddi bir para işleme girmeden atıl kalıyor.  Neden atıl kalıyor? Hemen açıklayalım. 

Pratikte bu havuzda işlemler genelde 0.03-0.04 arasında hatta çok daha dar bir aralıkta gerçekleşiyor. Ama havuz parayı bu aralıkta tutmayıp her alana dağıttığından bu alana düşen likidite az kalıyor. Bir bidon suyu on metrekare havuza ya da 100 metrekare havuza döktüğünüzü düşünün.  Havuz sığ kalınca, yüksek hacimli işlem olunca fiyatlar ani olarak düşüp yükselebiliyor. Bu hem likidite sağlayıcıya hem de işlem yapana sıkıntı yaratıyor:

Likidite sağlayıcı aslında havuzda para olmasına rağmen işlem yapılan alana yeterince para düşmediği için yapılan bir işlemin fiyata ani etki etmesi sonucu zarar ediyor (ki buna geçici kayıp ingilizcede impermanent loss adı veriliyor. Ne olduğunu ve nasıl çalıştığını [Uniswap yazımızda](/genel/2020/09/15/nedir-bu-uniswap.html) detaylıca anlatmıştık. Aşağıda dipnot olarak da verdik). Bu kayıp likidite sağlayacılar için kaçınılmaz bir şekilde var, ancak havuz sığ olduğunda etkisi daha vurucu oluyor. 

İşlem yapanlar ise, bir fiyattan almak için teklif verdiklerinde sıkıntı yaşıyorlar. Birincisi büyük bir emir verdiklerinde algoritma istedikleri fiyata çok az likidite bıraktığı için (likiditeyi tüm havuza paylaştırmak zorunda) yapılan işlemin fiyata ciddi bir etkisi oluyor (buna fiyat etkisi ya da 'price impact' deniyor). İkincisi ise havuzda çok sayıda işlem olması ama likiditenin sığ kalmasından dolayı, kullanıcının işlem emri verdiği sırada araya başka işlemler girdiği için verdiği emir fiyatı ile gerçekleşen fiyat arasında aleyhlerine bir fark olduğunu görüyorlar (ki buna ingilizcede slippage deniyor). 

### Başka ne sorunları var:

Uniswap'ın geçtiğimiz yaz aylarında yaşadığı büyük sıçramaya kısa süreli de sekte vuran gelişme, ürün kodlarını aynen kopyalayan Sushiswap'ın ciddi bir likiditeyi kendi platformuna çekmiş olmasıydı. Komisyon oranlarını benzer şekilde tutan Sushiswap likiditeyi kazanabilmek için kendi yönetim tokenini likidite sağlayıcılara vererek daha demokratik bir yapı olduğunu ilan etmişti. Bunun üzerine Uniswap da kendi tokenini çıkarıp dağıtmaya başladı ve likidite kanamasını bir nebze durdurmayı başardı. Token dağıtma bittikten sonra tekrar bir kayıp yaşasa da sonrasında  eski seviyelerine dönmeyi başardı. 

| ![uniswap-sushiswap](/assets/uniswap-sushi-liquidity_tr_800.png)|
|:--:| 
| *Kaynak: [TheBlock](https://www.theblockcrypto.com/)*|


### Arkası Yarın
Uniswap DeFi dünyasının en ağır toplarından.. DeFi dünyasında altyapıyı sağlayan Ethereum sonrasında değeri en yüksek olan protokol.. Üstelik bu sıçramayı geçtiğimiz bir yıl içinde yaptı.. Bu nedenle yaptıkları ve yapamadıkları yakından izleniyor.. Başta da yazdığımız gibi yeni versiyon bu sıkıntılara çare bulmak amacını taşıyor. Neler bu çareler? Yazı uzadığı için onu bir sonraki yazımıza bırakıyoruz artık... 

--

*Dipnot: Geçici Kayıp (Impermanent Loss) nasıl çalışır?
Örneğin ETH/USDC gibi bir havuza para koymak isteyen likidite sağlayıcıyı düşünelim. Önünde iki seçeneği var. Ya parasını kenarda ETH ve USDC olarak tutacak ya da havuza likidite koyacak. Eğer ETH fiyatı aniden yükselirse, kenarda para tutmak havuza para koymaktan daha kârlı hale geliyor. Eğer ETH fiyatı geri eski seviyesine düşerse o zaman bu kâr ortadan kalkıyor, ve havuza likidite sağlamak kazanılan komisyon gelirleri nedeniyle daha avantajlı hale geliyor. Bu nedenle bu kâra geçici kayıp dense de eğer ETH'nin sürekli yükseleceğini düşünüyorsanız bu aslında kalıcı hale geliyor.*


---

*Not 1: Bu yazı ilk olarak 2 Nisan 2021'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/definin-lider-borsasi-uniswapin-son-durumu/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*
