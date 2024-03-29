---
layout: post
title:  "DeFi türev piyasası Synthetix nasıl çalışıyor?"
date:   2020-08-28 18:47:56 +0300
categories: Genel
tags: Yazılar DeFi
---


Geçtiğimiz [yazıda](/genel/2020/08/20/defi-turev-piyasalari-nasil-oluyor.html) DeFi yani merkeziyetsiz finans alanında türev piyasası olur mu ona bakmış, bu piyasaların nasıl çalıştığını bu yazıya bırakmıştık. Gelin şimdi de 2020 yılının yaz aylarında bu alanın lideri haline gelen sentetik ürünler piyasası [Synthetix](https://www.synthetix.io/community)'i inceleyelim:

### Synthetix ne yapar?

Türev piyasaların yükselen yıldızı Synthetix Avustralya çıkışlı (Kripto dünyasının en önemli özelliklerinden biri fiziki dünyada nerede olduğunuzun o kadar da önemli olmaması. O nedenle bir gün Türkiye'den de benzer şekilde başarılı girişimlerin çıkacağını görmek en büyük umudumuz). Ekip, ICO piyasasının en sıcak olduğu 2018 yılının başlarında yaklaşık 30 milyon ABD Doları yatırım alarak projeyi hayata geçirdi. 2020 yılının başlarına kadar likidite sıkıntıları nedeniyle istenen hacimlere ulaşamayan sistem, sonrasında DeFi piyasasına olan ilginin artmasının da etkisi ile yaz ayları içinde adeta uçuşa geçti.  


| ![Synthetix Locked Value](/assets/Synthetix_locked_value_800.jpg)|
|:--:| 
| *Synthetix'de kilitlenen para miktarı [Kaynak](https://defipulse.com/synthetix)*|


### Nasıl çalışıyor sistem?

Sistem çalışması kısaca şöyle: Normalde bir türev piyasasında alan ve satan olarak iki parti bulunması gerekirken, Synthetix'de al-sat işleminde bir taraf var bir de karşısında bir havuz. Havuz kısmına birazdan değineceğin ama gelin öncelikle işin basit kısmından, sistemi kullanmak isteyen yani al-sat işlemi yapanlardan (trader) başlayalım ve basitlik adına bu kişilere "kullanıcı" diyelim.

### Nasıl işlem yapıyor kullanıcılar Synthetix sisteminde?

Kullanıcılar, özünde herhangi bir varlığa sahip olmadan o varlığın riskini (yani getiri ya da götürüsünü) almak isteyen kişiler oluyor.

Synthetix sistemindeki gerçek varlık yok. Onun yerine her bir ürünün sentetik denen türevi var. Bu ürünleri alabilmek için kullanıcının öncelikle sistemin parasına sahip olması lazım. O para da sentetik bir ürün: adı da sUSD. 

sUSD bir ABD Dolarına çıpalanmış bir sabit para. Bu parayı elde edebilmenin iki yolu var. Birincisi çeşitli borsalardan sUSD satın almak (ki o borsaların listesini [şurada](https://www.coingecko.com/en/coins/susd) bulabilirsiniz), ikincisi ise az sonra detaylı anlatacağımız "paydaş" yöntemi. 

Kullanıcı elindeki sUSD ile sistemde bulunan herhangi bir sentetik ürünü alabiliyor. Örneğin Bitcoin satın almak isterse gerçek BTC'yi değil onun sentetik türevi olan sBTC'yi alıyor. Canı istediğinde ise sBTC'yi sistemde sUSD karşılığı satıp, eline geçen sUSD'yi de yine aynı şekilde kripto para borsalarında satarak sistemden çıkabiliyor.

Klasik piyasalar yerine neden burada işlem yapsın bir kullanıcı? Bir önceki yazımızda kısaca değinmiştik. DeFi piyasaları interneti olan herkesin erişimine açık, klasik borsalarda olduğu gibi "nitelikli" bir kesime özel değil. Öte yandan özellikle çok al-sat yapanlar için, ürünlerin sentetik olması nedeniyle kullanıcılar herhangi bir üründen diğerine çok rahat geçebiliyor ve bu geçişler sırasında herhangi bir kayıp (sızıntı) yaşamıyorlar.

### Ne tip ürünler var Synthetix'de?

Beş ayrı kategori var: İtibari paralar, emtialar, kripto paralar, kripto para endeksleri ve kripto para fiyatlarını tersten izleyen inverse-kripto paralar.. Bu beş kategoride Ağustos 2020 itibariyle [32 adet ürün](https://dashboard.synthetix.io/) bulunuyor. [^1]

### Peki sistemdeki ürünlerin fiyatlarını kim belirliyor?
Sistemde iki taraf olmadığı ve yaratılan türev ürünlerin hepsi sistem içi ürünler olduğu için bu ürünlerin fiyatlarının belirlenmesinde, piyasa fiyatları göz önüne alınıyor. Merkezi olmayan sistemlerde piyasa fiyatlamaları genelde oracle denen dış (off-chain) bilgi sağlayıcılardan geliyor. Synthetix oracle olarak [Chainlink'i kullanıyor](https://blog.synthetix.io/chainlink-decentralizes-first-wave-of-synthetix-price-feeds/) ve piyasa bilgilerini her üç dakikada bir alıp güncelliyor. 

Buraya kadar her şey basit ve anlaşılır umarım. Eğer amacınız sadece sentetik ürün alıp satmak ise o zaman bu kadarı yeterli belki de. Ancak "bu değirmenin suyu nereden geliyor, havuz nasıl çalışıyor?" şeklinde aklınıza takılan sorular varsa o zaman okumaya devam.

### Sorular, sorular... 
Örneğin birkaç soru var hemen akıllara gelen:  
- Kullanıcılara karşı risk alan havuz nasıl oluyor? Arkasında kim var? Güvenilir mi? Nasıl merkeziyetsiz oluyor?
- Bu sUSD ne menem bir şeydir? Nereden çıkmış, neden ben kullanıcı olarak sUSD satın almak için para vereyim? 
- Sonra yarın öbür gün sBTC’mi satmak istediğimde yerine bana verecekleri sUSD’yi alacak biri çıkacak mı? 
- Bir sUSD bir ABD Doları’na eşit diye kim söylüyor, kim böyle bir garanti veriyor? Verilen garanti ne kadar güvenilir? 
- Sonra yarın öbür gün örneğin bütün kullanıcılar Bitcoin'in yükseleceğin düşünüp sBTC alırsa ve BTC iki katına çıkarsa kim ödeyecek bu kârı bu kullanıcılara?
- 
Bunların hepsi çok makul sorular ve hepsine cevap vermeden içimizin rahat etmesi mümkün değil. Ayrıca kimi sorulara cevap verdikçe yeni sorular da takılacak aklımıza - malum, sistem oldukça karışık. Gelin tek tek bakalım bu sorulara: 

#### Hepimizin çok sevdiği havuz problemi - ne menem şeydir bu havuz?
Synthetix sistemini aslında sanal bir ülke gibi düşünmek mümkün. Nasıl bir ülkenin Merkez Bankası, o ülkede dolaşımda olan parayı basar, burada da benzeri var: Synthetix sisteminin para birimi olan sUSD'yi basanlar da aslında o ülkenin Merkez Bankası oluyor. Tek fark burada sUSD'yi basan bir kurum değil merkezi olmayan binlerce kişi (Bu kişilere İngilizcede "staker" deniyor-Türkçe çevirisi tam olarak yok, yatırımcı, para koyucu, hissedar denebilir ama bu yazı özelinde "paydaş" terimini kullanacağız).

Biliyorsunuz Merkez Bankası’nın bastığı ve tedavüle soktuğu para esasında bankanın o parayı kullananlara yani halka bir borcudur. Synthetix’de de benzer şekilde paydaşlar sUSD basıp havuza koyarak sistemi kullananlara borçlanıyorlar. 

Şimdilerde artık o nosyonu kaybettik gerçi ama 20. Yüzyılın başlarında Merkez Bankaları para bastıklarında, halka bunun ödemesinin garantisi olarak stoklarında altın tutarlardı. Synthetix’de de sUSD basan paydaşlar bu borçlarına karşılık Synthetix’in kendi tokeni olan SNX’i teminat olarak göstermek zorundalar. 

Havuzun çalışma sistemi ise şöyle: Her bir paydaş yarattığı sUSD oranında havuzun borcuna ortak oluyor. Eğer kullanıcılar yani işlem yapanlar sBTC aldı ve sonrasında sBTC yükseldi ise, o zaman havuzun borcu büyüyor. Dolayısıyla havuzdan borç alanların borcu da büyüyor.  Tam tersi durumda işlem yapan zarar ederse (bu örnekte olduğu gibi sBTC fiyatı düşerse) o zaman da havuz kâr etmiş oluyor ve paydaşların da aynı oranda borcu düşüyor. 

#### sUSD nasıl yaratılıyor?
sUSD yaratımında teminat olarak konan SNX borsalarda alıp satılan bir token. Paydaş SNX satın alıp sisteme kilitleyip karşılığında sUSD basabiliyor. Merkez Bankası eskiden bire-bir altın karşılığında para basar idi. Ama altın dediğimiz maden binlerce yıldır ortada olan ve belli bir değeri olan bir varlık. Hiç SNX ile altın bir olur mu? Olmaz tabii. 

O nedenle, sUSD basarken SNX olarak çok daha fazlasını tutmak zorunda paydaşlar. Ne kadar? Şu anda teminat oranı %700. Yani 700 ABD Doları değerinde SNX'i teminat gösterirse ancak 100 ABD Doları karşılığı sUSD basabiliyor. (Karşılaştırma olarak MakerDAO'da bu oran %150, yani bir ABD Doları karşılığı olan bir DAI basmak için 1.5 ABD Doları karşılığı ETH koymak gerekiyor - ki [Synthetix de ETH teminatlı benzer bir modeli deniyor şu aralar](https://blog.synthetix.io/ether-collateral-second-trial/))

#### Peki nereden geliyor bu SNX? 
Havuz sistemine SNX kilitleyip sUSD basan ve bunun karşılığında para kazanan paydaşlardan. SNX bir token - 2018 yılında 100 milyon adet olarak basılıp ekibe, ilk yatırımcılara ve ICO'da genel halka dağıtılmış. Aslında orijinalde planlanan tüm SNX miktarı bu iken, sonrasında ekip para politikasını değiştirmeye ve [2024 yılına kadar ekstra 145 milyon SNX daha dağıtmaya karar vermiş](https://messari.io/asset/synthetix/profile#launch). (Nasıl dağıtılacağı bir sonraki bölümde) 

| ![SNX_price_2020](/assets/SNX_price_2020_short_v2.png)|
|:--:| 
| *SNX'in 2020 yılı içindeki değişimi (2018-2020 arası yatay seyretmiş) [Kaynak](https://www.coingecko.com/en/coins/synthetix-network-token)*|

Peki bir paydaş neden SNX alsın ve kendini riske atsın? Öncelikle SNX basılmaya başladığı günden bugüne çok ciddi değer kazandı. Ağustos 2020 itibariyle SNX piyasa değeri 700 milyon ABD Doları civarında. Ama bu spekülatif bir değer. SNX tokenin paydaşlara nakit getirisi var mı? Gelin bir de ona bakalım şimdi. 

#### Bu "paydaşlar" nereden para kazanıyorlar? 
Havuzdan borç alarak sUSD yaratanların iki temel kazancı var: 

Bunlardan birincisi, kullanıcıların havuzda yaptıkları işlemler için  (örneğin sBTC satın almak gibi) ödediği komisyonlar (şu anda %0.3). Bu komisyonlar havuza kâr olarak yazılıyor ve her hafta hesaplanıp sUSD yaratan paydaşlara veriliyor. 

İkincisi ise sUSD yaratanlar havuza can suyu yani likidite sağladıkları için her hafta sistem tarafından belli bir ödüle sahip oluyorlar. Ödül ise bir önceki bölümde bahsettiğimiz her yıl basılacak olan ekstra SNX'ler. Paydaşlar yarattıkları sUSD bazında oransal olarak bu SNX'lerden kazanıyorlar. Aynı Bitcoin sistemini korumak için enerji sarfeden madencilerde olduğu gibi. 

Bunun yanında tabii ki, kullanıcılar yaptıkları al-sat işlemlerinden kâr ederlerse bu kâr havuzun zararı oluyor ve havuzdan kullanıcılara ödeniyor. Ya da zarar ederlerse aynı şekilde bu zarar havuzun kârı olarak havuza aktarılıyor ve sonunda SNX sahiplerinin oluyor. 

#### sUSD yaratan "paydaş" bununla neler yapabilir?
Paydaş yarattığı sUSD ile sBTC ve benzeri türev ürünler satın alabiliyor ve kendisi de sistemin bir kullanıcısı olabiliyor. 

Sadece bununla sınırlı değil yapabildikleri: sUSD'yi kripto para borsalarında satabiliyor ya da sUSD'yi alıp başka platformlarda (örneğin [Aave](https://aave.com/)) borç vermekte kullanabiliyor.

Bütün bunların hiçbirini yapmayıp sUSD'yi öylece boşta da tutabilir paydaşlar ancak bunun oldukça riskli! Zira sUSD yarattığınız her noktada havuzda işlem yapan kullanıcıların karşı riskini (kâr ya da zararı da) almış oluyorsunuz. 

#### “Peki ben havuzun nimetlerinden yararlanmak istiyorum ancak riskini almak istemiyorum” derseniz? 
O da mümkün. Nasıl mı? Böyle bir durumda paydaş yarattığı sUSD ile gidip sistem üzerindeki yapılmış sentetik işlemlerin oransal olarak aynısını kendisi de gerçekleştirir (hatta bunu endeks fonu gibi otomatik yapan araçlar da var). Böylece riskini karşılamış (hedge etmiş) olur; havuz kaybederse paydaş o kaybettiği parayı kullanıcı olarak yaptığı karşı işlemden kazanmış olur.

#### SNX'in değeri değişince ne oluyor?
Peki ya SNX’in değeri değişince ne oluyor? Öyle ya borsada alınıp satılan bir token bu. SNX’in değer değişikliği teminatın değerinin de aynı şekilde değişmesi anlamına geliyor. 

Eğer SNX fiyatı artarsa, o zaman paydaşın teminat miktarı benzer şekilde artıyor ve %700’e gelecek kadar ekstra sUSD basma (yani ekstra borçlanma) hakkına sahip oluyor. 

Peki ya düşerse? O zaman da, teminat oranının altına düşme riski beliriyor. Bu durumda iki seçecek var izlenebilecek: Ya piyasadan SNX satın alarak teminat oranını %700’e yükseltecek, ya da borçlandığı sUSD’lerin bir kısmını ödeyerek (buna para yakma da deniyor) minimum teminat oranına çıkacak. Peki paydaş bu ikisini de yapmaz ise ne oluyor? Öyle ya, sanal dünya bu, nasıl zorlayacaksınız? 

Öncelikle teminat oranı %700'ün altına düşerse paydaş havuzun verdiği komisyon kârları ve ödül paralardan yararlanamıyor. Bu kâr ve ödüller teminatı yeterli olan diğer paydaşlara dağıtılıyor. 

Bunun da ötesinde eğer [teminat miktarı %200'ün altına düşerse o zaman kontrat tasfiye ediliyor](https://blog.synthetix.io/liquidation-faqs/#:~:text=Liquidation%20ratio%3A%20200%25,Liquidation%20penalty%3A%2010%25), ve minimum teminat miktarına getirene kadar paydaşın kilitlediği bütün SNX'ler satılıp sUSD yakılarak borç azaltılıyor. 

#### sUSD'nin sabit kalacağını nasıl garanti ediyorlar?
Aslında böyle bir garanti yok - ancak sistemin işleyişine baktığınızda neden 1 sUSD 1 Amerikan Dolarına eşit olur anlaşılıyor. Başta da yazdığımız gibi paydaşlar sUSD'yi basarak sisteme borçlanıyorlar ve bu borcu kapatmak için sUSD yakmak zorundalar:

Eğer sUSD'nin değeri 1 ABD Doları'nın altına düşerse, paydaşların piyasadan ucuza sUSD satın alıp borçlarını kapatmasını beklersiniz. Örneğin sUSD 90 cente düştü. Sistemde 1000 sUSD yaratmış (ve o sırada yaklaşık 1000 ABD Doları eline almış) bir paydaş, hemen gidip 1000 adet sUSD'ye 900 ABD Doları vererek sahip olup borcu olan 1000 sUSD'yi yakar ve 100 ABD Doları kâr eder. 

Peki ya sUSD'nin değeri yükseldi ve 1.10 ABD Doları'na geldi. O zaman da yine paydaşların hemen sisteme SNX kilitleyip karşılığında sUSD yarattığını görürsünüz. Aynı örnekten gidersek bir paydaş böyle bir durumda 1000 sUSD yaratıp bunu 1.10 ABD Doları'ndan sattığında otomatik olarak 100 dolar kâr eder. 


### Riskler, çekinceler

"Sistem çok güzel kurulmuş, riskler yok mu?" derseniz, hâlâ akla takılan ya da risk olarak görülebilecek alanlar var: 

Birinci ve en önemlisi, yazıdan anlaşılıyor olmalı ama tekrar edelim: Başka DeFi ürünlerde likidite sağlamak için para koyduğunuzda genel olarak düşük riskli ürünlere yatırım yapıyorsunuz. Synthetix'de ise SNX aldığınız ve sUSD yarattığınız noktada havuzun borcuna ve riskine ortak oluyorsunuz - ve bu ufak bir risk değil. 

Bununla bağlantılı ikinci temel risk ise şu: yapılan işlemlerin ağırlık olarak bir tarafa kayması sonucu riskin ve havuzun borcunun bir anda büyümesi: Örneğin Ağustos 2020 itibariyle sistemde sBTC tutanların oranı %22. 


| ![SNX_price_2020](/assets/synthetix_distribution-640.jpg)|
|:--:| 
| *SNX ürünlerinin Ağustos 2020 itibariyle dağılımı [Kaynak](https://dashboard.synthetix.io/)*|

Bu oran %100’lere yaklaşırsa ve aniden Bitcoin fiyatı iki katına çıkarsa o zaman bu işlem yapanlara havuz bu parayı nasıl ödeyecek? Paydaşlar havuza para koymaya devam edecekler mi? Yoksa “elimde tuttuğum SNX’ler feda olsun, ben borcumu ödemiyorum” deyip sistemden kaçabilirler mi?. Özellikle bir panik havası ile SNX'in değeri de düşemeye başlarsa. Elbette yukarıda bahsettiğimiz gibi teminat miktarı yaklaşık %700 oranlarında - bu endişeleri gidermekte bir miktar faydalı olabilir - keza %200'ün altında teminat oranlarında kontratın bozulup borcun kapanıyor olması da. Ancak yine de bu ani teminat düşüşlerinde risk olmadığı anlamına gelmiyor. 

Ayrıca şunu da unutmamak lazım - bu teminat SNX değeri üzerinden belirleniyor. SNX fiyatı 2019 yazında 30 centten bir yıl sonra 6 ABD Doları'na kadar geldi. SNX değeri artınca paydaşların teminat miktarları da artıyor ve paydaşlar daha fazla sUSD üretebiliyorlar, bu da likiditeyi artırdığı gibi riski de artırıyor. Yarın öbür gün SNX fiyatında hızlı bir düşüş yaşanırsa teminatların istenen seviyenin altında kalmasının getirdiği streslere sistem ne kadar dayanıklı önceden tahmin etmek zor. [^2]

Yukarıdaki iki konu gibi risk olmasa da sistem ile ilgili bir başka sıkıntı da yüksek gas fiyatları (sistemde borç yaratmak gibi işlemler için Ethereum üzerindeki işlem maliyeti). Bunun da temel nedeni türev işlemlerinin çok karmaşık olması nedeniyle Ethereum sistemine ağır gelmesi. Synthetix ekibi bunun önüne geçmek için Ethereum üzerine [ikinci seviye çözümler üzerinde çalışıyor](https://synthetix.community/docs/why-is-gas-so-high)

### Sonuç

Öncelikle yazıyı buraya kadar okuduysanız tebrikler!.. 

![Genius!](/assets/futuresmath_400.jpg)

Özet olarak düşüncemi şuraya bırakayım: 

- Synthetix türev piyasaları, internet bağlantısı olan herkese türev ürünlerini hızlıca alıp satmak ya da farklı türev ürünleri arasında masrafsız geçiş yapabilmek konularında büyük rahatlık sağlıyor. 
- Genel olarak DeFi'ya ilginin had safhada olmasının getirdiği artan iş hacimleri sayesinde yükselen komisyonlar ve dağıtılan ödüller SNX'e olan talebi ve dolayısıyla paranın değerini artırıyor.
- Ancak bu piyasaya likidite sağlamak amacıyla konan (stake edilen) paranın diğer DeFi platformlardan farklı olarak aynı zamanda risk getirdiği de göz önünde bulundurulmalı. 
- Uzun vadede özellikle uzun süreli boğa piyasası olması ve Synthetix'de açılan türev işlemlerinin sürekli kazandıran belli bir ürünlere kayması [^3] durumunda sistemin yapısından gelen riskleri kaldıramama ihtimali olduğu da unutulmamalı. 

---


[^1] *Synthetix üzerindeki her bir sentetik ürüne kısaca Synth deniyor ancak çok fazla terim olmaması adına dipnot olarak buraya bırakıyoruz..* 

[^2] *Kontratların nasıl likidite edileceği ile ilgili detaylı bilgiye [şu linkten](https://blog.synthetix.io/liquidation-faqs/#:~:text=Liquidation%20ratio%3A%20200%25,Liquidation%20penalty%3A%2010%25) ulaşabilirsiniz*

[^3] *Açılan işlemlerin dağılımını [Synthetix Dashboard](https://dashboard.synthetix.io/)'da alt tarafa doğru Synthetic Distribution tablosunda görebilirsiniz.* 

---

*Not 1: Bu yazı ilk olarak 28 Ağustos 2020'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/defi-turev-piyasasi-synthetix-nasil-calisiyor/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*
