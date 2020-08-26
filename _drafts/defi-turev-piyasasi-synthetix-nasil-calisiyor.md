Geçtiğimiz yazıda DeFi yani merkeziyetsiz finans alanındaki türev piyasaları nasıl olur ona bakmış, bu piyasaların nasıl çalıştığını bu yazıya bırakmıştık. Gelin şimdi 2020 yılının yaz aylarında bu alanın lideri olan sentetik ürünlerin piyasası Synthetix'i inceleyelim:

#### Synthetix ne yapar?
Türev piyasaların yükselen yıldızı Sythetix Avustralya çıkışlı ekip. ICO piyasasının en sıcak olduğu 2018 yılının başlarında yaklaşık 30 milyon ABD Doları yatırım alarak projeyi hayata geçirmeye başlamışlar. 

#### Nasıl çalışıyor sistem?

Sistem kısaca şöyle çalışıyor. Normalde bir türev piyasasında iki parti olması gerekirken, Synthetix'de sadece siz varsınız bir de karşınızda bir havuz. Havuz kısmına birazdan değineceğin ama gelin öncelikle işin basit kısmından, sistemi kullanmak isteyen kişilerden (trader) başlayalım ve bu kişilere "kullanıcı" diyelim. 

#### Nasıl işlem yapıyor kullanıcılar Synthetix sisteminde?

Kullanıcılar, herhangi bir varlığa sahip olmadan o varlığın riskini (yani getiri ya da götürüsünü) almak isteyen kişiler. Bunu Synthetix'de yapabilmek için bir kullanıcının öncelikle sisteme girebilmesi gerekiyor. 

Synthetix sistemindeki gerçek varlık yok. Onun yerine her bir ürünün sentetik denen türevi var. Bu ürünleri alabilmek için kullanıcının öncelikle sistemin parasını almanız lazım. O da sentetik bir ürün: adı sUSD. Bir ABD Dolarına çıpalanmış bir sabit para bu. Bu parayı alabilmenin iki yolu var. Birincisi [çeşitli borsalardan sUSD satın almanız](https://www.coingecko.com/en/coins/susd), ikincisi ise biraz daha aşağıda detaylı anlatacağımız paydaş yöntemi. 

Kullanıcı sonrasında elindeki bu sUSD ile istediği herhangi bir ürünü, örneğin sBTC’yi alıp istediği kadar elinde tutuyor. Canı istediğinde ise sBTC’yi sistemde satarak sUSD alıp, sUSD’yi yine aynı şekilde kripto para borsalarında satarak sistemden çıkabiliyor. 

#### Ne tip ürünler var bu Synthetix'de?

Beş ayrı kategori var. İtibari paralar, emtialar, kripto paralar, kripto para endeksleri ve kripto para fiyatlarını tersten izleyen inverse-kripto paralar.. Bu beş kategoride Ağustos 2020 itibariyle [16 adet ürün var](https://dashboard.synthetix.io/) var. 

#### Peki sistemdeki ürünlerin fiyatları kim belirliyor?

Sistemde iki taraf olmadığı ve yaratılan türev ürünlerin hepsi sistem içi ürünler olduğu için bu ürünlerin fiyatlarının belirlenmesinde, piyasa fiyatları alınıyor. Merkezi olmayan sistemlerde piyasa fiyatlamaları genelde Oracle denen dış (off-chain) bilgi sağlayıcılardan (Synthetix [Chainlink'i kullanıyor](https://blog.synthetix.io/chainlink-decentralizes-first-wave-of-synthetix-price-feeds/)) üç dakikada bir alınıyor. 

Buraya kadar her şey basit ve anlaşılır umarım. Eğer amacınız sadece sentetik ürün alıp satmak ise o zaman bu kadarı yeterli belki. Ancak "bu değirmenin suyu nereden geliyor?" ya da "bu işte bir bit yeniği var mı?" şeklinde kafanızda sorular varsa o zaman okumaya devam edebilirsiniz. 

##### Sorular, sorular... 

Örneğin birkaç soru var hemen aklınıza takılabilecek:  
- Bu sUSD ne menem bir şeydir? Nereden çıkmış, neden ben kullanıcı olarak sUSD satın almak için para vereyim? 
- Sonra yarın öbür gün sBTC’mi satmak istediğimde yerine bana verecekleri sUSD’yi alacak biri çıkacak mı? 
- Bir sUSD bir ABD Doları’na eşit diye kim söylüyor, kim böyle bir garanti veriyor? Verilen garanti ne kadar güvenilir? 
- Sonra yarın öbür gün örneğin bütün kullanıcılar Bitcoin’in yükseleceğin düşünüp sBTC alırsa, ve BTC iki katına çıkarsa kim ödeyecek bu BTC’leri bu kullanıcılara?

Bunların hepsi çok mâkul sorular, ve hepsine tek tek cevap vermeden içimizin rahat etmesi mümkün değil. Gelin tek tek bakalım bu sorulara: 

##### Hepimizin çok sevdiği havuz problemi - ne menem şeydir bu havuz?.. 

Synthetix sistemini aslında sanal bir ülke gibi düşünmek mümkün. Nasıl bir ülkenin Merkez Bankası, o ülkede dolaşımda olan parayı basar, Sythetix sisteminin para birimi olan sUSD’yi basanlar da aslında o ülkenin Merkez Bankası oluyor - burada sUSD’yi basan bir kurum değil merkezi olmayan binlerce kişi.(Bu kişilere Ingilizce de “staker" deniyor - Türkçe çevirisi tam olarak yok, yatırımcı, para koyucu, hissedar denebilir ama ben bu yazı özelinde “paydaş” terimini kullanacağım). Biliyorsunuz tedavülde olan Merkez Bankası’nın bastığı para esasında bankanın o parayı kullananlara bir borcu. Synthetix’de de benzer şekilde paydaşlar sUSD basıp havuza koyarak sisteme borçlanıyorlar. 

Şimdilerde artık o nosyonu kaybettik gerçi ama 20. Yüzyılın başlarında Merkez Bankaları para bastıklarında, halka bunun ödemesinin garantisi olarak stokta altın tutarlardı. Synthetix’de de sUSD basan paydaşlar bu borçlarının karşılık Synthetix’in kendi parası olan SNX’i teminat olarak göstermek zorundalar. 

Havuzun çalışma sistemi ise şöyle: Her bir paydaş yarattığı sUSD oranında havuzun borcuna ortak oluyor. Eğer işlem yapanlar sBTC aldılar ve sBTC yükseldi ise, o zaman havuzun borcu büyüyor dolayısıyla havuzdan borç alanların da borcu büyüyor.  Tam tersi durumda işlem yapan zarar ederse (bu örnekte olduğu gibi sBTC fiyatı düşerse) o zaman da havuz kâr etmiş oluyor ve borcu düşüyor. 

##### sUSD nasıl yaratılıyor?
sUSD yaratımında teminat olarak konan SNX’ler borsalarda alıp satılan tokenlar. Bunları satın alıp sisteme kilitleyip karşılığında sUSD basabiliyorsunuz. Merkez Bankası eskiden bire-bir altın karşılığında para basar idi. Ama altın dediğimiz maden binlerce yıldır ortada olan ve belli bir değeri olan bir varlık. Hiç SNX ile altın bir olur mu? Olmaz tabii. O nedenle, sUSD basarken SNX olarak çok daha fazlasını tutmak zorundasınız. Ne kadar? Şu anda teminat oranı %700. Yani 700 ABD Doları değerinde SNX’i teminat gösterirseniz ancak 100 ABD Doları karşılığı sUSD basabiliyorsunuz. (Karşılaştırma olarak MakerDAO’da bu oran %150, yani bir ABD Doları karşılığı olan bir DAI basmak için 1.5 ABD Doları karşılığı ETH koymanız gerekiyor - ki [Synthetix de ETH teminatlı benzer bir modeli deniyor şu aralar](https://blog.synthetix.io/ether-collateral-second-trial/))


##### Peki nereden geliyor bu SNX? 
Havuz sistemine SNX kilitleyip sUSD basan ve bunun karşılığında para kazanan paydaşlardan. SNX bir token - 2018 yılında 100 milyon adet olarak basılıp ekibe, ilk yatırımcılara ve ICO'da genel halka dağıtılmış. Aslında orjinalde planlanan tüm SNX miktarı bu iken, sonrasında ekip para politikasını değiştirmeye karar vermiş ve [2024 yılına kadar ekstra 145 milyon SNX daha dağıtmaya karar vermiş](https://messari.io/asset/synthetix/profile#launch). (Nasıl dağıtılacağı bir sonraki bölümde) 

| ![SNX_price_2020](/assets/SNX_price_2020_short_v2.png)|
|:--:| 
| *SNX'in 2020 yılı içindeki değişimi (2018-2020 arası yatay seyretmiş) [Kaynak](https://www.coingecko.com/en/coins/synthetix-network-token)*|


Peki bir paydaş neden SNX alsın ve kendini riske atsın? Öncelikle SNX basılmaya başladığı günden bugüne çok ciddi değer kazandı. Ağustos 2020 itibariyle SNX piyasa değeri 700 milyon ABD Doları civarında. Ama bu spekülatif bir değer. SNX tokenin paydaşlara nakit getirisi var mı? Gelin bir de ona bakalım şimdi. 

##### Bu "paydaşlar" nereden para kazanıyorlar? 
Havuzdan borç alarak sUSD yaratanların iki temel kazancı var. Bunlardan biri, kullanıcılar havuzda yaptıkları işlemler (örneğin sBTC satın almak gibi) için komisyon ödüyorlar. Bu komisyonlar havuza kâr olarak yazılıyor ve sUSD yaratanlara gidiyor. İkincisi ise sUSD yaratanlar havuza can suyu yani likidite sağladıkları için her hafta sistem tarafından belli bir ödüle sahip oluyorlar. Öncelikle havuzu kullanarak alım-satım yapan her kullanıcı bunun karşılığında bir bedel ödüyor. Bu ödenen bedel sUSD yaratmış paydaşlara gidiyor. 

İkinci temel kazanç ise bir önceki bölümde bahsettiğimiz her yıl basılacak olan SNX'ler. Bunlar, sUSD yaratarak sisteme likidite sağlayan paydaşlara gidiyor. Paydaşlar yarattıkları sUSD bazında oransal olarak ödül olarak verilen bu SNX'lerden kazanıyorlar. 

Bunun yanında tabii ki, kullanıcı yaptığı işlemden kâr ederse bu kâr havuzun zararı oluyor ve havuzdan kullanıcıya ödeniyor. Ya da zarar ederse aynı şekilde bu zarar havuzun kârı olarak havuza aktarılıyor ve sonunda SNX sahiplerinin oluyor. 

##### sUSD yaratan paydaş bununla neler yapabilir?

Paydaş yarattığı sUSD ile sBTC ve benzeri türev ürünler de satın alabiliyor ve aynı zamanda sistemin kullanıcısı olabiliyorlar. Ya da sUSD'yi borsalarda satıp karşılığında başka kripto paralar alabilir. Son olarak sUSD'yi alıp başka platformlarda borç olarak verebilir. 

Bütün bunların hiçbirini yapmayıp sUSD'yi öylece boşta da tutabilir paydaşlar ancak bunun riskli olduğu unutulmamalı. Zira sUSD yarattığınız her noktada havuzun diğer işlem yapanlara karşı olan riskini (kâr ya da zararı da) almış oluyorsunuz. 

##### O zaman çok riskli değil mi SNX yatırımcısı olmak? Ya kullanıcılar hep kârlı işlem yapar da havuz zarar ederse? 
Doğru böyle bir risk var. Bu riski bertaraf etmek için başlangıç aşamasında sistem belli aralıklarla SNX basıp kullanıcılara dağıtarak yatırımcıları teşvik etmeye çalışmış ama bu durum bundan sonra devam edecek mi bir garantisi yok.   [BUNU TEKRAR CHECK ETMEKTE FAYDA VAR]

Öte yandan hiçbir ürün sürekli yükselmez, genel anlamda yükselişlerde bile arada düşüşler yaşar. Kişilerin beklentileri de her zaman aynı yönde olmaz. Burada da her bir ürünü alabildiğiniz gibi satabiliyorsunuz da.. Dolayısıyla piyasa ne kadar likit olup yükseliş ve düşüşe oynayanlar karşı karşıya gelirse aslında havuz riski de o kadar düşüyor ve havuz her iki taraftan da işlem ücreti alarak hayatına devam ediyor. 

##### SNX'in değeri değişince ne oluyor?

Peki ya SNX’in değeri değişince ne oluyor? Öyle ya borsada alınıp satılan bir token. SNX’in değer değişikliği teminatın değerinin de aynı şekilde değişmesi anlamına geliyor. Eğer SNX fiyatı artarsa, o zaman fazla teminatınız oluyor ve %700’e gelecek kadar ekstra sUSD basma (yani ekstra borçlanma) hakkına sahip oluyorsunuz. Peki ya düşerse? O zaman da, teminat oranının altına düşüyorsunuz. Bu durumda iki seçeceğiniz var. Ya piyasadan SNX satın alarak teminat oranınızı %700’e yükselteceksiniz, ya da borçlandığınız sUSD’lerin bir kısmını ödeyerek (buna para yakma da deniyor) yine aynı şekilde minimum teminat oranına getireceksiniz. Peki paydaş bu ikisini de yapmaz ise ne oluyor? Öyle ya, sanal dünya bu, nasıl zorlayacaksınız? O zaman öncelikle havuzun paydaşlara verdiği komisyon kârları ve ödül paralardan yararlanamıyor. [Ayrıca bir noktada LIKIDITASYON???]

##### sUSD'nin sabit kalacağını nasıl garanti ediyorlar?
Aslında böyle bir garanti yok - ancak sistemin işleyişine baktığınızda neden 1 sUSD 1 Amerikan Dolarına eşit olur anlaşılıyor. Başta da yazdığımız gibi paydaşlar sUSD'yi basarak sisteme borçlanıyorlar ve bu borcu kapatmak için sUSD yakmak zorundalar. Eğer sUSD'nin değeri 1 ABD Doları'nın altına düşerse, paydaşların piyasadan ucuza sUSD satın alıp borçlarını kapatmasını beklersiniz. Örneğin sUSD 90 cente düştü. Sistemde 1000 sUSD yaratmış (ve o sırada yaklaşık 1000 ABD Doları eline almış) bir paydaş, hemen gidip 1000 adet sUSD'ye 900 ABD Doları vererek sahip olup borcu olan 1000 sUSD'yi yakar ve 100 ABD Doları kâr eder. 

Peki ya sUSD'nin değeri yükseldi ve 1.10 ABD Doları'na geldi. O zaman da yine paydaşların hemen sisteme SNX kilitleyip karşılığında sUSD yarattığını görürsünüz. Aynı örnekten gidersek bir paydaş böyle bir durumda 1000 sUSD yaratıp bunu 1.10 ABD Doları'ndan sattığında otomatik olarak 100 dolar kâr eder. 

##### “Peki ben havuzun nimetlerinden yararlanmak istiyorum ancak o riski almak istemiyorum” derseniz? 

O da mümkün. Nasıl mı? O zaman, yarattığınız sUSD ile gidin sistem üzerindeki yapılmış işlemlerden oransal olarak aynısını yapın (hatta bunu endeks fonu gibi otomatik yapan araçlar da var). Böylece riskinizi karşılamış (hedge etmiş) olacaksınız, havuz kaybederse siz kullanıcı olarak o kaybettiğiniz parayı işlem yaparak kazanmış olacaksınız. 


