---
layout: post
title:  "Finansın Domino Taşları 1- Son Krizde Neler Yaşandı?"
date:   2022-07-22 17:17:56 +0300
categories: Genel
tags: Yazılar, DeFi, CoindeskTR
---

Bu yazımızda, son zamanlarda DeFi'de yaşanan olayları mercek altına alıyoruz. Nasıl başladı, son gelişmeler neler, sorunun kaynağı ne?

Yaklaşık iki ayı aşkın bir süredir kriptopara piyasalarında derin bir karamsarlık söz konusu. Özellikle sektörün iki büyük parası BTC ve ETH'nin düşüşüne paralel yaşanan iflas olayları ve zor duruma düşen kurumsal yatırımcı haberleri bu karamsarlığın temel nedenleri arasında.

### Nasıl başladı?

8 Mayıs tarihinde UST'de yaşanan sıkıntı ile başlayan ve sonrasında domino taşları gibi teker teker birbirini etkileyen olaylar zincirinin başrol oyuncularını inceleyelim öncelikle:

| ![domino_falls](/assets/domino-163523_800.jpg)|
|:--:| 
| *Image by [PublicDomainPictures](https://pixabay.com/users/publicdomainpictures-14/) from [Pixabay](https://pixabay.com/)*|

#### UST

Yaşanan sarsıntının temelinde Terra sisteminin stabil parası olan UST'nin bir ABD dolarına sabitlenmiş çıpasını kaybetmesi var. 

Daha önceki iki yazıda ayrıntılarını incelediğimiz gibi dolara sabit olmakla birlikte Anchor Protokol tarafından yıllık %20 gibi ağız sulandırıcı bir faiz oranı ile yatırımcılara sunulan UST, bir yıldan kısa bir zaman içinde yaklaşık 18 milyar ABD Doları gibi bir büyüklüğe ulaştı. (Yazıların [ilkine](https://medium.com/turansert/ba%C5%9F%C4%B1ma-gelenler-ustnin-hikayesi-21324bb4969f) ve [ikincisine](https://medium.com/turansert/ust-olay%C4%B1nda-son-perde-cd48c9c6e15b) bağlantılardan okuyabilirsiniz)

| ![domino_falls](/assets/ust_piyasa_degeri_800.jpg)|
|:--:| 
| *UST Piyasa Değeri. Kaynak: [CoinGecko](https://www.coingecko.com/en/coins/terraclassicusd)*|

Büyük ölçüde hormonlu olarak gerçekleşen bu büyümenin sürdürülebilir olmadığı aslında apaçık ortaydı ancak müzik çalarken bütün oyuncular dans etmeye devam ettiler. 

Sonrasında müzik susunca, dans pistinde en hareketli oyuncu olan Three Arrows Capital (3AC)'nin oturacak sandalye bulamadığını gördük. Önce bu arkadaşları bir tanıyalım: 

#### Three Arrows Capital - 3AC

2012 yılında [Zhu Su](https://twitter.com/zhusu) ve [Kyle Davies](https://twitter.com/kyleldavies) adında iki trader [tarafından Singapur'da](https://en.wikipedia.org/wiki/Three_Arrows_Capital)  kurulan [Three Arrows Capital](https://www.threearrowscap.com/about-us/) (kısa adıyla 3AC) esas olarak bir arbitraj fonu. Ne demek arbitraj fonu? Benzer ürünlerin farklı piyasalar arasındaki fiyat farklılıklarından doğan fırsatları değerlendiren bir fon. İşlem yaptıkları  benzer karaktere sahip enstrümanları bir piyasada alıp (ya da borç alıp) diğer tarafta satan (ya da borç veren) böylece riski minimuma indirerek kazanç sağlayan yapılar. 

3AC'nin bu tip piyasa farklılıklarından yararlanarak işlem yaptığı üç temel ürün var (başka pek çok yatırımı dışında). Bunlar BTC/GBTC, ETH/stETH ve USD/UST idi.  (En sondaki dipnot'ta bu üç ürünün neler olduğu konusunda detaylı bilgiyi bulabilirsiniz). 

İşte 3AC piyasadan olabildiğince borçlanıp yukarıdaki üç 'arbitraj' fırsatını kullanarak ciddi bir şekilde büyüdü. Hesaba katmadıkları ne oldu? Yukarıdaki sistemlerin piyasalar yükselişte iken yani müzik devam ederken kazanç sağladığı, piyasaların düşüşe geçtiği noktada ise göz ardı edilen bütün risklerinin bir anda başa geldiği. Neydi bu riskler? 

Birincisi USDT(C) gibi paraları borç alıp UST'ye yatırma stratejisinin, her iki paranın da ABD dolarına çıpalanması nedeniyle 'sıfır risk' gibi algılanırken, aslında UST'nin gerçek risklerini gizlemesi. Nedir bunlar? UST'nin aslında temel fonksiyonu olan geniş kitlelerce kullanılma yerine, büyümek için sürdürülemez bir şekilde faiz vermesinin yarattığı ince buzda yürümesi. Bu buz kırıldığında en çabuk batan en çok yük taşıyanlar oldu ki bunların başında 3AC geliyordu. 

İkincisi ise likidite sıkıntısı. 3AC, USD/UST stratejisini olabildiğince sömürmek adına fazla fazla USDC (ve USDT) borçlanabilmek için teminatlar verdi. Nedir verilen bu teminatlar? Yukarıda bahsettiğimiz arbitrajlar sırasında aldığı GBTC ve stETH'ler ya da başta BTC ve ETH olmak üzere likit kriptoparalar. UST'nin çıpasını kaybettiği noktada 3AC'ye borç verenler kredileri geri çağırmaya, kredi geri ödenmediği  nokta da ellerinde tuttukları bu teminatları bozdurmaya başladılar. İşte bu bozdumalar sonrası GBTC'nin piyasa değeri BTC'ye göre %34'e yakın [geriliyor](https://ycharts.com/companies/GBTC/discount_or_premium_to_nav), aynı şekilde stETH'nin değeri 0,93 ETH'ye [düşüyor](https://coinmarketcap.com/currencies/steth/steth/eth/). BTC, Haziran ayında şimdiye kadar en kötü performans gösterdiği ayı yaşayıp %39.7 oranında değer kaybediyor. Bütün bu yaşananlar, teminatların değerini daha da düşürüp, daha fazla teminatın bozulmasına yol açıyor.

Yukarıda yaşananların dışında 3AC'nin elindeki GBTC'leri farklı kurumlara teminat göstererek kredi aldığı şeklinde iddialar var ki, doğru ise dolandırıcılık olarak adlandırılabilecek bu durumu 3AC'nin kurulu olduğu Singapur otoritelerinin incelemeye aldığını da belirtelim. 

Gelinen son noktada, 3AC, British Virgin Islands'da mahkemelere başvurup [iflasını isteyerek](https://www.coindeskturkiye.com/sirketler/three-arrows-capital-new-yorkta-iflas-basvurusunda-bulundu-939) beyaz bayrağı çekmiş durumda. En son bu hafta Pazartesi günü açıklanan belgelere göre toplam 30 merkezi şirket 3.5 milyar ABD Doları tutarında bir alacağı için iflas sürecini yöneten aracıya [başvuruda bulundu](https://www.theblock.co/post/158169/three-arrows-capital-3ac-creditors-list-3-5-billion-crypto-affidavits). Detaylar yavaş yavaş ortaya dökülmeye devam edecek. 


### Arkası yarın 
Domino taşları UST ile başlayıp 3AC ile devam ediyor ancak orada bitmiyor. Diğer taşlara ise önümüzdeki yazımızda bakmaya devam edeceğiz. 

Not: 

**1. BTC/GBTC:** Piyasadan BTC borçlanıp, bu BTC ile GBTC almak. GBTC, elinde BTC tutan özel bir fon (İngilizce'de trust fund). ETF dediğimiz sahip olduğu ürünlerin fiyatını takip eden fonlar ABD'de çok yaygın ancak ABD'nin SPK'sı olan SEC  kripto için bu fonlara izin vermiyor. Kriptoparalara yatırım yapmak isteyen büyük emeklilik fonları, ETF'lere izin verilmediği için başlangıçta gidip GBTC alıyorlar idi. Bu aşırı talep nedeniyle GBTC, elinde tuttuğu BTC'den daha yüksek bir değere sahip idi. GBTC'nin birkaç özelliği var; herkes alamıyor (sadece belirli bir nitelikli grup), aldıktan sonra altı ay boyunca satamıyorsunuz, ayrıca öyle geri verip karşılığında BTC almak da yok, satışı sadece piyasaya yapabiliyorsunuz. GBTC primli olduğunda aslında bu bir sorun değil. Eğer %10 primli ise, BTC'ni yatır, altı ay bekle altı ay sonunda %10 primli olarak piyasada sat. İşte 3AC'nin yaptığı işlemlerden biri bu idi. Teorik olarak yok diyenler çıkabilir, zira en kötü GBTC'nin içinde o kadar BTC var, ama pratikte? Ya GBTC'ye olan talep azalır ve GBTC iskontoya düşerse? O zaman zarar etmemek için GBTC'yi satmaz elinizde tutmaya devam edersiniz. Ne zamana kadar? GBTC'ye talebin ve buna bağlı fiyatın artmasını bekleyeceksiniz. Bu nasıl olur? Kolay değil ancak bir çıkış yolu olarak GBTC'yi çıkaran Grayscale bu fonu ETF'e çevirmek için SEC'ye başvurdu. GBTC ETF'e çevrilirse o zaman, tipik bir ETF gibi piyasa yapıcılar girip fiyatı BTC ile denk hale getirebilirler, siz de elinizdeki GBTC'leri elden çıkabilirsiniz. Peki ya SEC izin vermezse (ki vermedi) o zaman? Ya beklemeye devam ya da beklemeye tahammülünüz kalmazsa (ya da zorunlu kalırsanız) piyasada zararına satacaksınız. (Grayscale fonları ile ilgili geçtiğimiz yıl yayınlanan detaylı yazıya [şuradan](https://medium.com/turansert/grayscale-fonlar%C4%B1-6e3de0040881) ulaşabilirsiniz)

**2. ETH/stETH:** Ethereum yeni versiyonunda PoW denen iş kanıtı yönteminden, daha az enerji harcayan PoS sahiplik kanıtı yöntemine geçecek. Sistemin güvenliğini ve işleyişini artık madenciler değil sisteme ETH rehin etmiş onaylayıcılar sağlayacaklar. Bu nedenle onaylayıcı olmak isteyenler 2020 yılının Aralık ayından bu yana ellerindeki ETH'yi (en az 32 ETH olacak şekilde) sisteme kilitliyorlar ve bunun karşılığı bir faiz alıyorlar. Sisteme kilitlenen bu ETH'leri geri çekmek şu an için mümkün değil. Bunun için önce PoS sistemine geçilmesi sonra da yaklaşık altı ay kadar  beklenmesi gerekiyor (kesin süre belli değil). İşte kilitlenen bu ETH'leri likit hale getirmek için çeşitli tokenler türetilmiş durumda. Bunlardan en büyüğü ise [Lido Finance](https://lido.fi/) tarafından çıkarılan staked ETH tokenler ([stETH](https://www.coingecko.com/en/coins/lido-staked-ether)). ETH'nizi Lido Finance'e kilitlediğinizde karşılığında stETH alıyorsunuz. stETH ile hem varlığınızı PoS sistemine kilitlemiş gibi faiz alıyor hem de bu tokeni DeFi sisteminde kullanarak (örneğin varlığınızı başka sistemlere likidite sağlayarak) ekstra gelir elde ediyorsunuz.  Eğer günün birinde ETH ihtiyacınız olursa stETH'yi satabiliyorsunuz ama bunu piyasada yapmak zorundasınız. (Lido Finance ETH'nizi stake ettiği için size geri vermiyor. Siz gidip piyasada satıyorsunuz, dolayısıyla stETH'nin değerini piyasa belirliyor.)  Teorik olarak stETH ile ETH'nin değerinin eşit olması gerek. Zira konan her bir ETH için bir stETH yaratılıyor. Zaten bir gün ETH'ler PoS sisteminden çekilebilir olduğunda stETH'ler de benzer şekilde ETH'ye çevrilebilir. O güne kadar ya bekleyeceksiniz ya da piyasa size ne dikte ediyorsa (ki bu genelde iskontolu bir fiyat oluyor) oradan satacaksınız. 

**3. USD/UST:** UST'nin büyümesinin temel nedenlerinden biri yatırımcıların (ya da al-sat yapan piyasa oyuncularının), bulabildikleri her yerden USD'ye çıpalı paraları (USDT, USDC) borçlanıp bu paraları UST'ye yatırmaları oldu. Öyle ya, bankaların USD mevduata %1'in altında bir faiz verdiği ortamda, USDC için %4 vaat etmek yatırımcılar için müthiş cazip. USDC'yi bu orandan borç alıp %20 ile UST'ye yatırdığınızda da bu da sizin için müthiş. Alan memnun satan memnun. Nereye kadar? Müzik sona erinceye. 


---

*Not 1: Bu yazı ilk olarak 22 Temmuz 2022'de [Coindesk Türkiye](https://www.coindeskturkiye.com/))'de [yayınlandı](https://www.coindeskturkiye.com/yazarlar/turan-sert/finansin-domino-taslari-1-son-krizde-neler-yasandi-1217)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*
