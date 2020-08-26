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

Sistemde iki taraf olmadığı ve yaratılan türev ürünlerin hepsi sistem içi ürünler olduğu için bu ürünlerin fiyatlarının belirlenmesinde, piyasa fiyatları alınıyor. Merkezi olmayan sistemlerde piyasa fiyatlamaları genelde Oracle denen dış (off-chain) bilgi sağlayıcılardan üç dakikada bir alınıyor. 

#### Sorular, sorular... 

Buraya kadar her şey basit ve anlaşılır umarım. Ancak ortada birkaç soru var sorulması gereken - sizin de aklınıza takılıyor olabilir. 
- Bu sUSD ne menem bir şeydir? Nereden çıkmış, neden ben kullanıcı olarak sUSD satın almak için para vereyim? 
- Sonra yarın öbür gün sBTC’mi satmak istediğimde yerine bana verecekleri sUSD’yi alacak biri çıkacak mı? 
- Bir sUSD bir ABD Doları’na eşit diye kim söylüyor, kim böyle bir garanti veriyor? Verilen garanti ne kadar güvenilir? 
- Sonra yarın öbür gün örneğin bütün kullanıcılar Bitcoin’in yükseleceğin düşünüp sBTC alırsa, ve BTC iki katına çıkarsa kim ödeyecek bu BTC’leri bu kullanıcılara?

Bunların hepsi çok mâkul sorular, ve hepsine tek tek cevap vermeden içimizin rahat etmesi mümkün değil. Gelin tek tek bakalım bu sorulara: 

#### Hepimizin çok sevdiği havuz problemi - ne menem şeydir bu havuz?.. 

Synthetix sistemini aslında sanal bir ülke gibi düşünmek mümkün. Nasıl bir ülkenin Merkez Bankası, o ülkede dolaşımda olan parayı basar, Sythetix sisteminin para birimi olan sUSD’yi basanlar da aslında o ülkenin Merkez Bankası oluyor - burada sUSD’yi basan bir kurum değil merkezi olmayan binlerce kişi.(Bu kişilere Ingilizce de “staker" deniyor - Türkçe çevirisi tam olarak yok, para koyucu, hissedar gibi denebilir ama ben bu yazı özelinde “paydaş” terimini kullancağım). Biliyorsunuz tedavülde olan Merkez Bankası’nın bastığı para esasında bankanın o parayı kullananlara bir borcu. Synthetix’de de benzer şekilde paydaşlar sUSD basıp havuza koyarak sisteme borçlanıyorlar. 

Şimdilerde artık o nosyonu kaybettik gerçi ama 20. Yüzyılın başlarında Merkez Bankaları para bastıklarında, halka bunun ödemesinin garantisi olarak stokta altın tutarlardı. Synthetix’de de sUSD basan paydaşlar bu borçlarının karşılık Synthetix’in kendi parası olan SNX’i teminat olarak göstermek zorundalar. 

Havuzun çalışma sistemi ise şöyle: Her bir paydaş yarattığı sUSD oranında havuzun borcuna ortak oluyor. Eğer işlem yapanlar sBTC aldılar ve sBTC yükseldi ise, o zaman havuzun borcu büyüyor dolayısıyla havuzdan borç alanların da borcu büyüyor.  Tam tersi durumda işlem yapan zarar ederse (bu örnekte olduğu gibi sBTC fiyatı düşerse) o zaman da havuz kâr etmiş oluyor ve borcu düşüyor. 



##### İyi de karşı parti olmadan piyasa çalışmaz ki? 
Çok haklısınız. Synthetix'de ise karşı taraf olarak bir havuz var. 

Bu havuz sistemin parası olan SNX'lerden oluşuyor.  SNX sistemin temel direği. Zira SNX, DeFi sistemlerin en büyük ihtiyacı olan likiditeyi sağlıyor sistem. Bir piyasa ne kadar az likit ise al-sat arasındaki fark da o kadar büyük olur ve yatırımcı olarak gereksiz bir kayba uğrarsınız. Hele bir de farklı farklı bir sürü ürün olursa, karşı parti bulmak o kadar zorlaşır ve likidite iyice azalır. SNX sistemin ortak parası olarak tüm ürünlerde kullanıcılar için karşı parti oluyor, yani tüm ürünlere bir havuz aracılığıyla likidite sağlıyor. 

##### Peki nereden geliyor bu SNX? 
Havuz sistemine SNX koyan ve bunun karşılığında para kazanan paydaşlardan. 

SNX koyan yatırımcılar nasıl para kazanıyorlar? Öncelikle havuzu kullanarak alım-satım yapan her kullanıcı bunun karşılığında bir bedel ödüyor. Bu ödenen bedel SNX sahiplerine gidiyor. Bunun yanında tabii ki, kullanıcı yaptığı işlemden kâr ederse bu kâr havuzun zararı oluyor ve havuzdan kullanıcıya ödeniyor. Ya da zarar ederse aynı şekilde bu zarar havuzun kârı olarak havuza aktarılıyor ve sonunda SNX sahiplerinin oluyor. 

##### O zaman çok riskli değil mi SNX yatırımcısı olmak? Ya kullanıcılar hep kârlı işlem yapar da havuz zarar ederse? 
Doğru böyle bir risk var. Bu riski bertaraf etmek için başlangıç aşamasında sistem belli aralıklarla SNX basıp kullanıcılara dağıtarak yatırımcıları teşvik etmeye çalışmış ama bu durum bundan sonra devam edecek mi bir garantisi yok.   [BUNU TEKRAR CHECK ETMEKTE FAYDA VAR]

Öte yandan hiçbir ürün sürekli yükselmez, genel anlamda yükselişlerde bile arada düşüşler yaşar. Kişilerin beklentileri de her zaman aynı yönde olmaz. Burada da her bir ürünü alabildiğiniz gibi satabiliyorsunuz da.. Dolayısıyla piyasa ne kadar likit olup yükseliş ve düşüşe oynayanlar karşı karşıya gelirse aslında havuz riski de o kadar düşüyor ve havuz her iki taraftan da işlem ücreti alarak hayatına devam ediyor. 





Niye SNX gibi bir ürün çıkmış peki? Temel nedeni sisteme özgü, sistemde duran bir para olan SNX kullanılarak bir türev üründen diğerine hızlı ve ucuz sağlanıyor (ingilizcede friction-sürtünme ve slippage/sızıntı olarak tabir edilen kayıplar önleniyor). 


Kim kurmuş?
Nasıl çalışır?

### UMA nasıl 

Ortakları kimler?
Nasıl çalışır

### Synthetix ile UMA'nın farkları
