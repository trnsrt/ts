---
layout: post
title:  "Uniswap rakipleri: Curve, Balancer ve Sushiswap"
date:   2020-09-22 18:47:56 +0300
categories: Genel
tags: Yazılar DeFi
---

Hatırlarsanız [geçtiğimiz yazıda](/genel/2020/09/15/nedir-bu-uniswap.html) en büyük merkeziyetsiz borsa olan Uniswap'tan bahsetmiştik. Bu yazımızda ise DeFi dünyasındaki diğer merkeziyetsiz borsalara ve Uniswap'tan ne şekilde farklılaştıklarına bakalım. 

<img align="left" src="/assets/Uniswap_logo_250.png" style="width:40%; padding-right:20px"> Kısaca hatırlamak gerekirse Uniswap, çiftli (iki tokena sahip) havuzlar aracılığıyla, işlem yapmak isteyenlere emre amade (istendiği anda) alım-ya da satım imkanı verebilen bir borsa. Klasik borsalara giriş yapamayan ya da yapmayı zahmetli bulan kullanıcılar ve yine klasik borsalara giremeyen ya da girmek istemeyen tokenlar için adeta çölde bir vaha. 

2020 yılının Mart ayından başlayarak artan işlem hacmine paralel Uniswap havuzlarına konan para yani likidite arttı (ki bu ikisi --yani işlem hacmi ve likidite-- yumurta-tavuk misali birbirini etkiler). Özellikle son zamanlarda, kimi günler Uniswap bir büyük merkezi kripto borsasından daha fazla işlem hacmi yaratmaya başladı. 

Tabii Uniswap'ın rakipleri de yok değil. DeFi sistemleri için "lego gibi" benzetmesi yapılır. Farklı platformlarda yapılabilenleri çok hızlıca bir araya getirerek kullanıcılara yepyeni ürünler sunabilirsiniz. Bu ürünlerin ucu bucağı yok. Bir sistemi daha iyi anlamak istiyorsanız rakiplerin nasıl farklılaştıklarına bakmak iyi bir yöntem olabilir. Gelin hep birlikte bakalım, rakipler Uniswap'ın hangi özelliklerinde nasıl farklılaşıyor: 

### Nasıl farklılaştı rakipler?

#### Farklı algoritmalar
Uniswap'ın özünde bir otomatik piyasa yapıcısı olduğundan bahsetmiştik [geçen yazımızda](/genel/2020/09/15/nedir-bu-uniswap.html). Bunun anlamı şu:  Alım-satım yapmak isteyen kullanıcılara sistemin verdiği fiyatlar otomatik olarak belirleniyor. Fiyat derken kastettiğimiz değiş-tokuş değeri. Havuzdaki bir tokeni almak için havuzdaki diğer tokenin oraya konması gerekiyor. 

Ne kadar token konacağı için ise basit bir formül var: Her bir havuzun iki tarafını oluşturan token adetlerinin çarpımı her zaman bir sabit sayıya eşit olacak. O kadar. Mantık basit aslında: Bir tokena talep varsa havuzdan çekilir ve karşılığında diğer tokendan konur. "Havuz büyüklüğü" dediğimiz sabit sayıyı korumak esas: Havuzdaki azalan tokendan yeni bir tane almak için her seferinde diğer tokendan daha fazla konmalı. Basit bir arz-talep dengesi. 

**Uniswap algoritmasının temel hedefi likidite yani her ne olursa olsun işlem yapmak isteyenlere sunulabilecek bir token bulundurmak**. Yukarıdaki algoritma işte bu amacı gerçekleştirmeye en uygun olan mantık. Tabii bunun kimi durumlarda dezavantajları da olabiliyor: Örneğin kimi zaman bir tokena çok talep olunca o tokenın fiyatı (havuzdaki diğer token ile değiştirme oranı) saçma yerlere gelebiliyor. Ya da, kullanıcı işlem yapmadan önce sistemde bir alım-satım oranı görürken işlem yapmaya başladığında birden bunun değiştiğini farkediyor. Bunun nedeni şu: Sistem başlangıçta en son yapılmış işlem oranını gösterirken, kullanıcı işlem yapmak istediğinde ona yapacağı işlem sonrasında havuzdaki sabit sayıyı tutturacak olan oranı gösteriyor. Bu duruma performans düşüklüğü (slippage) deniyor ve özellikle likiditesi az havuzlarda yapılan işlemlerde kendini hissettiriyor. Uniswap için bu iki sıkıntının da bir önemi yok - onlar için önemli olan işlem yapmak için gelen karşısında bir fiyat buldu mu? Buldu ise sorun yok. 

Gördüğünüz gibi Uniswap algoritması olarak bahsettiğimiz sabit sayı ve hesaplaması afaki ve kimi zaman sıkıntılara da yol açabiliyor - yani isteyen istediği şekilde bu hesaplamayı değiştirerek yeni bir algoritma oluşturabilir. Nitekim rakiplerin bir kısmı bu algoritmaları değiştirerek kendilerine farklılaştırıyorlar. 

#### Çoklu havuzlar
Uniswap'daki her bir havuzun iki bölmesi var demiştik - ve her bir bölmede de birer token. İllâ iki token mı olması lazım? Daha çok token koyulamaz mı? Olur tabii - neden olmasın? İşte rakip olarak çıkan kimi sistemler üç, dört hatta 8'e kadar sayıda tokenlar koydular havuzlarına. Böylece likidite sağlayıcılara birden fazla tokena aynı anda yatırım yapma imkanı vermiş oldular. 

#### Farklı havuz oranları
Uniswap'taki her havuzda iki bölme olmasının yanında algoritmaya göre her bir bölmede eşit değerde token olması gerekiyor. Yani bir havuzun bir tarafında 1000 ETH var ve bir ETH de 300 USDC ise, havuzun diğer tarafında da 300,000 USDC olmalı ki sistem dengede olsun. Peki bu oran hep %50-50 mi olmalı? Uniswap algoritması gereği öyle olabilir ama her zaman %50-50 olmasına gerek yok havuzların. Farklı ağırlıklı havuzlar da gayet rahat şekilde kurulabilir. 

Neden farklı havuzlara ihtiyaç var? Özellikle likidite sağlayanlar havuza token koyduklarında esasında havuzun her iki tarafına da yatırım yapıyorlar. Zaman içinde değişen beklentilere göre bu iki token için farklı ağırlıklarda yatırım yapmak isteyebilirler. Örneğin ETH'nin artacağı konusunda bir beklentisi var ise neden %50-50 ETH/USDC havuzuna para koysun ki, %80-20 oranlı bir havuz çok daha cazip olabilir. 

#### Yönetim tokenı
Uniswap'ta likidite sağlayıcıların  Eylül 2020 başına kadar gelirleri yalnızca sağladıkları likiditeye karşılık yapılan işlemlerden aldıkları komisyonlar idi. Halbuki rakip projeler, bu komisyonlar dışında kullanıcılara ve likidite sağlayıcılara kendi tokenlarını veren teşvik mekanizmaları geliştirdiler. İşte geçtiğimiz haftaki yazının hemen ardından Uniswap da benzer bir tokenı kendi paydaşlarına dağıtmaya başladı. Üstelik oldukça demokratik bir biçimde, geçtiğimiz dönemde (1 Eylül 2020'ye kadar) Uniswap kullanıp da işlem yapmış her bir hesaba 400 UNI tokenı bedava verdiler. Bu dağıtım sonrasındaki bir hafta içinde bir UNI token fiyatının 3-8 ABD Doları arasında değiştiği düşünülürse, geniş bir kitlenin mutlu olduğunu söylemeye gerek yok.

#### Diğer projeler ile birlikte çalışabilmek
DeFi projelerinin klasik projelere göre en önemli farklarından biri, farklı projelerin birbirleriyle uyumlu çalışabilmesi. Buna "money lego" diyenler de var. İşte, Uniswap rakipleri başka başka projeler ile iletişim içinde yeni ve kazancı daha yüksek ürünler çıkarabiliyorlar. 

#### Fiyat
Uniswap her bir işlem için al-sat yapan kullanıcılardan %0.3 komisyon alıyor. Bu oldukça yüksek bir rakam - her ne kadar 1 Eylül 2020 tarihine kadar kendisi üzerinden işlem yapmışlara 400 UNI token hediye ederek bu komisyonların bir kısmını kullanıcılara geri vermiş olsa da.  Uniswap likidite sağlayıcılara gelir olarak yalnızca bu işlem komisyonlarını önerebildiği için rakamı çok da düşüremiyor ve bu da rekabette onu zorluyor. Zira rakiplerin komisyon oranları hem düşük hem de havuzdan havuza değişebiliyor. Ancak son açıklanan UNI token ile birlikte likidite sağlayıcılar artık komisyon yanında UNI token ile ciddi bir ekstra gelir de kazanma şansına sahip. O nedenle bir sonraki versiyonunda Uniswap'ın (v3) bu komisyonları da düşürmesi beklenebilir.  


### Rakipleri tanıyalım
Peki Uniswap'ın hangi rakibi yukarıdaki hangi özellikte ondan farklılaşıyor? Gelin anlamaya çalışalım:

#### Curve

<img align="left" src="/assets/curve_logo_250_v2.png" style="width:40%; padding-right:20px"> [Curve](https://www.curve.fi/) yukarıdaki Uniswap algoritmasını farklı bir şekilde uyguluyor. Rakamsal olarak ne olduğunun çok önemi yok bu yazı için. Kullanıcıların bilmesi gereken, Uniswap algoritmasının amacı kullanıcılara her ne olursa olsun işlem yapabilecekleri bir token sunmak iken, **Curve algoritması için önemli olan - yukarıda Uniswap için bahsettiğimiz - işlem yaparken al-sat yapanın yaşadığı performans düşüklüğünü en aza indirmek**.

Curve'un kullandığı bu algoritma, daha çok al-sat yapan kullanıcılar için yüksek hacimli ve fiyatı fazla oynamayan token çiftlerinde avantaj sağlıyor. Örneğin ABD Doları'na bağlı olan iki stabil kripto paranın (Tether yani USDT ve USDC çifti gibi) olduğu havuzlarda Curve'in algoritması çok daha iyi çalışıyor[^1]. 

Bunun dışında üç-dört stabil paradan oluşan havuzlar da kurabiliyor Curve - Uniswap gibi yalnız ikili havuzlar yok. Bunun nedeni, kullanıcıların farklı sabit paralarla işlem yapmak isteğine cevap vermek, likiditeyi ayrı havuzlara bölerek sığlaştırmak yerine bir arada toplamak. Böylece kullanıcı her bir paradan diğerine geçerken ayrı ayrı havuzları kullanmak yerine olabilecek tüm farklı işlem taleplerini bir havuzdan gerçekleştirebiliyor. Uniswap'ta farklı paralarda alım-satım yapmak isteyen biri iki ayrı havuz kullanacağı için çifte komisyon verip, bir de potansiyel olarak daha sığ iki havuzda daha fazla kayganlık (slippage) yaşarken, Curve kullanan bu ekstra kayıplardan kaçınabiliyor. 

Bütün bunların yanında Curve, sistemine likidite sağlayanlara CRV yönetim tokenı da veriyor. Likidite sağlayıcılar için havuzdaki işlem ücretinden aldıkları komisyonlar dışında bir kazanç kapısı daha. Bu önemli, zira Curve al-sat işlemi yapan kullanıcılara cazip gelebilmek için komisyon oranlarını %0.14 seviyesinde tutuyor (Uniswap'ın %0.3'üne göre). O zaman likidite sağlayıcı neden parasını buraya koysun? Hem düşük komisyon hem de daha az performans düşüklüğü ile kendisine çektiği al-sat yapan kullanıcılardan yarattığı yüksek işlem hacmi ile kazandığı komisyon yanında bir de CRV tokenı veriyor ki sistem likidite sağlayıcılar için cazip olsun. 

Ayrıca özellikle diğer projeler ile çalışma anlamında ilginç birliktelikleri var Curve'in. Örneğin, ilk çıkardıkları USDC/DAI (her ikisi de sabit para) havuzundaki likiditeyi, bir borç verme platformu olan Compound'a koydular. Böylece Curve'e likidite sağlayanlar aynı zamanda Compound'da kredi olarak verilen para üzerinden faiz kazandı.  Bunun yanında [geçtiğimiz bir yazımızda](/genel/2020/08/28/Defi-turev-piyasasi-synthetix-nasil-calisiyor.html) bahsettiğimiz kripto para türev borsası Synthetix ile ortak bir ürün çıkardılar ve ellerindeki likiditeyi Synthetix havuzlarına da kullandırdılar. Karşılığında da Curve likidite sağlayıcıları Synthetix tokenı olan SNX kazandılar... 

Likiditenin DeFi ürünlerinde ne kadar önemli olduğunu görüyorsunuz değil mi? **Özünde Curve bir nevi likidite ticareti yapıyor**. Likidite sağlayıcılardan aldığı parayı gerek sabit para al-sat yapmak isteyen kullanıcılara, gerekse kendi sistemini kuvvetlendirmek isteyen başka platformlara götürerek ekstra getiriler elde ediyor. 

[Bitti mi? Hayır](https://www.youtube.com/watch?v=Im1SqKh9qgg). Zaman içinde bu likidite oyununu giderek artırdı Curve. Compound ile ortak ürün çok güzel. Likidite sağlayan biri, hem işlem üzerinden komisyon, hem CRV tokenı, hem Compound faizi, hem de COMP yönetim tokenı kazanıyor. Ancak ya faiz olarak Compound'un önerdiği faizler az ise? Öyle ya bir tek Compound yok kredi veren platformlar içinde.. [Aave](https://aave.com/) var, [dYdX](https://dydx.exchange/) var. Ya onlar daha iyi faiz verirse? Likidite sağlayıcılar "mağdur" mu olsun? İşte o nedenle Curve, [Yearn](https://yearn.finance/) isimli portföy yönetimi yapan bir platform ile bir başka ürün daha çıkardı. Bu üründe, likidite sağlayıcı parayı koyuyor Curve sistemine, Yearn bu parayı en yüksek faiz veren kredi platformunda otomatik değerlendiriyor, gerekirse birinden alıp öbürüne geçiriyor. Nasıl? DeFi ürünleri hakikaten akıl sınırlarını zorluyor, değil mi?

#### Balancer
<img align="left" src="/assets/balancer_logo_250.png" style="width:40%; padding-right:20px"> [Balancer](https://balancer.exchange/), Uniswap'a kullanıcı arayüzü olarak çok benziyor olsa da, getirdiği yenilikler ile yatırımcılara farklı alternatifler sunuyor. Neler bunlar hızlıca bakalım: 

İkili değil sekize tokena kadar ve %50-50 değil farklı oranlarda token konabilen havuzlar sağlıyor öncelikle. Örneğin içinde %40 WETH, %35 DAI, %25 USDC olan bir havuz var. Ne işe yarar bu? Likidite sağlayıcılar için kendi risk ve beklentilerine uygun olarak istedikleri türden bir endeks fonuna yatırım yapma imkanı. Adeta kişiye özel bir yatırım fonu! Bu tip havuzlardan [1700 adet mevcut](https://pools.balancer.exchange/#/) Balancer’da.   Üstelik klasik bir endeks fonunda fon yöneticisine yönetim payı verirken, burada likidite sağlayıcılar hem yapılan işlem üzerinden komisyon hem de Balancer'ın yönetim tokenı olan BAL'ı almaya hak kazanıyor.

Öte yandan Balancer üzerinde kurulan havuzların içinde yapılan işlemlerden alınan komisyon oranları Uniswap gibi sabit değil. Her bir havuz kurucusu farklı bir komisyon belirleyebiliyor. Örneğin yukarıda bahsettiğimiz havuzun komisyon oranı %0.07. Likidite sağlarken komisyon oranlarını incelemekte fayda var. Bunun yanında kimi likidite sağlayıcılar kurdukları havuzu özel tutup, dışarıdan başka para almamayı tercih edebiliyorlar. 

Neden böyle yapıyorlar tartışılır - ama çok uç bir örnek olarak, geleneksel şirketler mevcut hisse senetlerini geri almak (buy-back) suretiyle bu senetlerin dolaşımdaki miktarını kontrol etmek isterler. Kripto dünyasında da kimi girişimler dolaşımda olan tokenlarının emisyon hacimlerini kontrol altında tutmak isterken karmaşık hesaplar, yeni token basma ya da token yakma yerine, Balancer üzerine havuz kurup bunu kullanabilirler. Hatta, böyle bir durumda, havuzda manipülasyon yapılmasın diye yüksek işlem komisyonu (örneğin %5) belirleyip ancak çok yüksek fiyat değişikliklerinde son çare olarak havuzlarının kullanılmasını isteyebilirler. Görüyorsunuz, bu tip ürünlerde amaç ve isteğe göre o kadar farklı senaryo ve alternatif çıkabiliyor ki. 


#### Sushiswap

<img align="left" src="/assets/sushi_logo.png" style="width:40%; padding-right:20px"> Yukarıda bahsettiğimiz gibi, özünde Uniswap çok basit bir algoritma. Bir DeFi platformu olarak aynı zamanda açık kaynak vizyonu ile çalışıyor - yani ürün (yani kod) tamamen açık. Dolayısıyla, Uniswap'ın kodunu kopyalayıp (forklamak) benzer bir ürünü çıkarmak o kadar zor değil. Nitekim [Sushiswap](https://sushiswapclassic.org/) bu şekilde Uniswap kopyası olarak ortaya çıkmış bir platform. Unsiwap'ın özelliklerini aynen alıp üzerine tek bir ekleme yaptı, o da parayı kendilerinde tutanlara verdiği [Sushi token](https://www.coingecko.com/en/coins/sushi).. Bir anda ciddi bir likidite (ki bunlar ellerinden büyük miktarda token tutan balinalar) Sushiswap'a kaydı. 

Ancak sonrasında DeFi en büyük krizlerinden birini yaşadı. Sushiswap'ın [kurucusu (ismi bilinmeyen) olan yazılımcı](https://twitter.com/NomiChef), geliştirici payı olarak kendine ayırdığı 15 milyon ABD Doları civarındaki Sushi tokenı piyasalarda bozdurdu. Bu topluluk içinde büyük bir fırtınaya neden oldu ve gelen tepkiler üzerine bu kişi sattığı o tokenları iade etti. Sinek küçük ama mide bulandırır tarzı bir hareket oldu bu (ki 15 milyon hiç de küçük değil). Sushiswap yoluna devam ediyor - zira gerek kullanıcı gerekse likidite sağlayıcılar aldıkları komisyon ve Sushi token ödüllerine bakıyorlar. Ancak bu olay klonların imajını ciddi şekilde sarstı. 

Her ne kadar "kod" olarak aynı olsalar da, geliştirici ekip ve etrafında kümelenmiş ciddi bir topluluk olmadıkça, Sushiswap benzeri klonların uzun vadede Uniswap'tan geri kalacağını beklemek çok da yanlış olmaz. Sadece para ile saadet olmuyor maalesef. 


### Uniswap rakiplerine nasıl cevap verecek?

Şu an için Uniswap'ın en büyük avantajı sahip olduğu havuzlardaki likidite ve bunun sağladığı ağ (network) etkisi. Ancak DeFi hızlı ilerlemesine rağmen henüz emekleme aşamasında olan bir sektör, o nedenle her an herşey değişebilir. Bu ağ etkisinin çok kalıcı olmadığını düşünenler de var. 

Strateji pazarlama alanındaki en önemli konulardan biri müşteri bağlılığıdır (customer stickiness). Müşteriyi nasıl kendinize bağlarsınız? Klasik finans sistemi oyuncuları maalesef daha çok kendi sistemlerinden çıkmayı zorlaştırarak müşterileri kendilerine bağlıyorlar. Ancak DeFi'da öyle değil - zira varlık platformda değil, kullanıcının elinde. Al-sat işlemini bugün sizden yapar - yarın daha iyi fiyat bulursa ya da daha az komisyon veriyorsa anında gidip rakip platforma geçer. Hatta farklı platformlara bakmasına bile gerek yok. [1inch](https://1inch.exchange/#/) gibi hizmet sağlayıcılar onun adına hangi platform daha uygun fiyat veriyor anında gidip bulur. 

Likidite sağlayıcılar için de durum benzer şekilde. Likiditeyi bugün burada tutar - daha iyi bir imkan bulursa anında çeker, başka bir yere gider. 

Öte yandan, TVL (Total Value Locked) olarak da bilinen DeFi platformlara bağlanan paraların küçük yatırımcılardan çok ellerinde büyük miktarlarda kripto tutan yatırımcılardan geldiği biliniyor. Balina olarak adlandırılan bu yatırımcılar da anında yer değiştirebiliyorlar. Baksanıza son üç ayda bu dört büyük platforma bağlanmış para miktarlarının oynaklığına:


| ![Dört platform likidite miktarları](/assets/Four_DiFi_Dexes_v3_1200.png)|
|:--:| 
| *Dört büyük merkeziyetsiz borsaya bağlanmış olan kripto para miktarı - [Kaynak](https://defipulse.com)*|


Rakiplerin kendisine göre hızla yol almalarına karşı Uniswap da belli aksiyonlar almaya başladı. Örneğin Eylül başında çıkardığı UNI token esas olarak kendi klonu olan Sushiswap'a karşı gösterdiği bir reaksiyon. Uniswap likidite sağlayıcılara gelir olarak yapılan işlemlerden komisyon verdiği için işlemlerden aldığı %0.3 ücreti yüksek olmasına rağmen düşüremiyordu. UNI token ile likidite sağlayıcılar artık ciddi bir ekstra gelir kazanacaklar. 

Yakında çıkması planlanan Uniswap 3.0 versiyonda, al-sat komisyon ücretlerinin (UNI sayesinde artan diğer gelirler ile birlikte) azalması beklenebilir. Bunun yanında ikili havuzlar yerine çoklu havuzları da uygulamaya alabilir Uniswap. 

### Sonuç
DeFi platformları özünde birbirleri ile uyumlu çalışabilen ve içinde ne olduğunu herkesin görebildiği açık yazılımlar. Bu nedenle, farklı platformlar ile bir araya getirilerek kullanıcılara eşsiz kazanç olanakları sunulabiliyor ama öte yandan hızlıca da kopyalanabiliyorlar. 

Sektör bağımsız sıklıkla duyarız "rekabet çok artıyor" sözünü. Bunu söyleyenleri getirip DeFi dünyasını göstermek lazım. Kullanıcıları elde tutabilmek çok zor. Bunu için platformların kaliteli ve yenilikçi ürünleri hızlı bir şekilde kullanıcıya sunmaları gerekiyor - hızlı derken günleri kastediyoruz, ayları değil. Ayrıca platformu destekleyen gönüllü bir topluluğa sahip olmanız gerekiyor ki - hem ürünü test etsinler, hem platforma yol gösterip teşvik edip yoldan çıkmasını engellesinler. 

Önümüzdeki dönemlerde her tür öne çıkan DeFi platformunda Uniswap'a benzer şekilde rakipler çıkacak, yeni ürünler sunulacak, lider platformlar karşı aksiyonlarda bulunacak. Ve bütün bunlar ışık hızında olacak. Tabii ki bu hız yanında yol kazalarını da beraberinde getirecek. Ama sonuç: sürekli gelişen, ilerleyen ve oturmaya başlayan DeFi ürünleri olacak. Görünen o ki, ok yaydan çıktı ve DeFi geleneksel finans sistemini gün geçtikçe daha hızlı bir şekilde sallamaya devam edecek. 

---

*Not 1: Bu yazı ilk olarak 22 Eylül 2020'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/uniswap-rakipleri-curve-balancer-ve-sushiswap/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

---

[^1] Curve algoritması Uniswap algoritmasına göre birbirine yakın değerdeki iki tokenda arz ve talep sonucu ortaya çıkan farkı minimumda tutuyor. Buna Stablswap adı veriliyor- detayları [Curve tanıtım yazısı (whitepaper- pdf)](https://www.curve.fi/stableswap-paper.pdf) bulabilirsiniz. Eğer arz ve talep değişikliği çok yüksek oranlarda olursa o zaman Curve daha dezavantajlı hale geliyor. Ancak Curve havuzları genelde birbirine yakın ve hep 1 ABD Doları'na geri dönen stabil paralardan oluştuğu için Curve algoritması bu havuzlarda daha kullanışlı. 



<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Introducing The Degenerator. <br><br>Spin up a new <a href="https://twitter.com/hashtag/DeFi?src=hash&amp;ref_src=twsrc%5Etfw">#DeFi</a> project in as little as 5 minutes! <a href="https://t.co/qpiod6uqSf">pic.twitter.com/qpiod6uqSf</a></p>&mdash; Jordan Lyall 🍍 (@JordanLyall) <a href="https://twitter.com/JordanLyall/status/1294466755692081152?ref_src=twsrc%5Etfw">August 15, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


