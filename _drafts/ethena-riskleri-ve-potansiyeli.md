---
layout: post
title:  "Ethena: Riskleri ve potansiyeli"
date:   2024-05-30 12:17:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Bu yazımızda, geçtiğimiz hafta başladığımız Ethena sisteminin derinliklerine iniyoruz. 

Geçtiğimiz haftaki yazımızda stabil paralardaki son duruma göz atmış ve bu alanda son çıkan ürün olan Ethena'nın kapısını şöyle bir aralamıştık. 

Özetlemek gerekirse, Ethena'nın sunduğu USDe, merkeziyetsiz bir para ve değeri bir ABD dolarına çıpalanmış şekilde işlem görüyor. Her bir USDe'nin arkasında ona eşdeğer bir kriptopara teminat var. Bu teminatın piyasadaki değerinin artıp azalması USDe değerini etkilemesin diye stokta duran kriptopara kadar bir değer vadeli piyasalarda 'short' ediliyor. Bu sayede, teminatların değerinin ABD doları cinsinden sabit kalması hedefleniyor. 

Ethena'nın stabil para değil de 'sentetik para' olarak nitelediği USDe'nin bir de gelir getirici bir yanı olabiliyor. O da basılan USDe'lerin sisteme kilitlenmesi durumunda, yukarıda bahsedilen işlemden doğan kârın USDe sahibine veriliyor olması. 

"Bu kâr nedir?" diye soracak olursanız: İki farklı parçası var. Birincisi nispeten daha stabil olan, ETH olarak verilen teminatın Ethereum sistemine stake edilmesinden doğan ödül. İkincisi ise teminat kadar rakamın 'short' edilmesinden doğan bir kâr (ki bu kimi zaman negatif olup zarar da yazabililyor). 

USDe'nin sisteme kitlenmesi sonrası oluşturulan sUSDe tokeninin getirisi değişken olmakla birlikte %30-40'lar bandına kadar çıkabiliyor. Tabii bu kadar ciddi kâr getiren bu ürün, aynı zamanda ciddi olarak dikkat edilmesi gereken riskleri de beraberinde getiriyor. Gelin şimdi bu risklere göz atalım. 

### Sistemin riskleri neler?
Ethena'nın kurduğu bu sistem oldukça kompleks ve bu nedenle üzerinde fazlaca risk barındırıyor. Zaten Ethena da bu riskleri tek tek ortaya koyup, nasıl önlemler aldığını açık açık yazıyor. Gelir sırayla bakalım bu risklere: 

#### Short'lamak her zaman gelir getirmiyor ya uzun süre negatif gidip zarar yazarsa?
Kendinizi sağlama almak için riskinizi satmak istediğinizde (İngilizce buna 'hedge' etmek deniyor) kullandığınız vadeli piyasalara perpetuals (kısaca 'perp') piyasalar deniyor[^4]. Bu piyasalarda risk almak isteyenler ile riski satmak isteyenler bir araya geliyorlar. Hangi taraf ağırlıkta ise diğerine 'fonlama maliyeti' adı altında bir ödeme yapıyor. 

Genelde bu piyasalarda işlem yapanlar risk alma iştahına sahipler. Yani işlem yaptıkları varlığın fiyatının yükseleceğini düşünüyorlar ve bu nedenle o varlığın riskini (ve değerinin yükselmesi beklentisini) satın alıyorlar (ingilizcesi 'long' olmak). Long gidenler bunun tam tersi riski satmak isteyen (ingilizcesi 'short' olmak) taraflara ödeme yapıyorlar. Kimi durumlarda, özellikle ayı piyasası hakimken bunun tam tersi de olabiliyor. Yani 'short' olanlar 'long' olanlara ödeme yapıyorlar. 

İşte Ethena'nın sürekli 'short' pozisyon oynadığını düşündüğümüzde, belirli aralıklarla 'fonlama maliyeti' ödeyerek zarar yazması da mümkün. Peki geçmişte bu ne kadar gerçekleşmiş? Ethena'nın açıkladığı verilere göre son üç yılın yaklaşık beşte birinde short'lar fonlama maliyeti ödemiş (ödedikleri fonlama maliyeti de ortalama yıllık %8.8'e denk geliyor). Kalan zamanda beşte dördünde ise longlar ödeme yaptığı için kâr etmiş. 

| ![eth-perp-kayip-kazanc](/assets/eth-perp-kazanc-kayip-oranlav2.png)|
|:--:| 
| *ETH perpetuals piyasalarında son üç yıl içinde short pozisyon açanların fonlama geliri/gideri. Kaynak: [Ethena Labs](https://app.ethena.fi/dashboards/hedging/ETH)*|

Peki ya piyasa çok uzun süre ayıda kalır, short'lar ağır basar ve fonlama maliyeti nedeniyle Ethena'nın ettiği zarar uzun süre devam ederse ne olacak?

İşte önemli sorulardan biri bu. Zira, zararın uzun süre devam ettiği noktada USDe'nin arkasındaki teminatın azalıp negatife geçme ihtimali olabilir. Ethena bu durumun önüne geçmek için bir rezerv fon oluşturmuş durumda. Kazandığı paraların bir kısmını bu fona koyuyor. 

Geçtiğimiz üç yıla bakacak olursak, shortların zarar yazdığın en uzun dönemin 13 gün ile bir kez gerçekleştiğini görüyoruz. 

| ![ethena-ardisik-gun-sayilari](/assets/ethena_ardisik_gun-sayilari.png)|
|:--:| 
| *Perpetual piyasalarında fonlama maliyetlerinin serileri (5 günden fazla seriler). Yeşil olanlar art arda pozitif gelir getirdiği günler (180 güne kadar çıkmış), kırmızı olanlar ise negatif getiriler (en fazla 13 gün olmuş). Kaynak: [Ethena Labs](https://ethena-labs.gitbook.io/ethena-labs/solution-overview/risks/funding-risk)*|

Burada hemen bir parantez açarak, Ethena'nın nereden para kazandığına bakalım. Aslında para kazanma yöntemi çok basit. Sonuçta Ethena kişilerden aldığı kriptoparaları staking ve vadeli piyasalarda hedge ederek para kazanıyor. Bu kazandığı paradan yaptığı ödeme ise sadece USDe'yi stake edenlere. USDe'yi stake etmeyip piyasada kullananların verdiği fonların getirisi Ethena'ya kalıyor! (Yazı yazıldığı sırada piyasadaki [USDe miktarı](https://etherscan.io/token/0x4c9edd5852cd905f086c759e8383e09bff1e68b3) 2.8 milyar ABD Doları, [sUSDe miktarı](https://etherscan.io/token/0x9D39A5DE30e57443BfF2A8307A4256c8797A3497) ise 976 milyon ABD Doları seviyesinde).

İşte Ethena bu gelirlerinden bir kısmını (%80'ini) şu anda rezerv fona koymakla meşgul. Rezerv fonun hayata geçtiği son üç ay içinde şu ana kadar [40 milyon ABD doları toplanmış durumda](https://app.ethena.fi/dashboards/solvency). Ethena'ın risk profilini yapan [Chaos Labs'e göre](https://596495599-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsBsPyff5ft3inFy9jyjt%2Fuploads%2FXx0DNbv33KWqybLS4HvU%2FChaos%20Labs%20-%20Ethena%20Perpetual%20Assessment%20Report%20Final.pdf?alt=media&token=0d167789-ee8b-4135-9ebd-d5e07033aa48) vadeli piyasalardaki fonlama maliyetini ödemesinden dolayı zarar edilmesi durumunda rezervde tutulması gereken para her bir milyar USDe için yaklaşık 33 milyon ABD doları. Ethena'nın şu ana dek yaklaşık 2.3 milyar USDe bastığını düşünürsek, şu anda bir açık olduğunu ama bu açığın kapanmakta olduğunu belirtelim. 

| ![ethena-rezerv-vs-usde](/assets/ethena-rezerv-geliri-tablosu_v2.png)|
|:--:| 
| *Ethena'nın elinde tuttuğu rezervin ve USDe'nin aylar içinde gelişimi. Kırmızı çizgi ile gördüğünüz Chaos Labs tarafından önerilen rezerv miktarı. Gördüğünüz gibi rezerv sürekli artıyor olsa da USDe de arttığı için yetersiz kalıyor. Kaynak: Delphi Digital 'The rise of Ethena - Unpacking the Emerging Synthetic Dollar' raporu*|

Diğer yandan, bu analizin geçmiş verilere dayandığını, gelecekte yaşanabilecek çok uzun süreli ayı dönemlerinde daha büyük bir zarar oluşabileceğini söyleyelim. Bu nedenle rezerv fonunun bu tip dönemleri düşünerek çok daha yüksek olması gerekli (önümüzdeki dönemde takip edilmesi gereken konulardan biri bu). Diğer yandan Ethena'nın elinde sadece rezerv fonu silahı yok, hazinesinde duran ENA tokenler de var. Olası bir zararı karşılamak için bu tokenlerin kullanılması da söz konusu. 

Peki böyle bir durumda ne olur? Arkasındaki teminat azaldığı için teorik olarak USDe'nin değerinin azalması beklenebilir. Öyle olduğunda da elinde USDe tutanlar öncelikle piyasada bu USDe'leri bozdururlar. Likit olarak USDe'nin olduğu yer Curve havuzları. Bu havuzlarda USDe'nin değeri düşer. Değeri düşen USDe'yi satın alan 'onaylı' aracılar bunu getirip Ethena'ya koyar, bu paranın karşılığı teminat olarak tutulan kriptoparayı sistemden çekerler. Peki bu satışlar özellikle Ethena çok büyürse piyasayı etkiler mi? Belki, ama Ethena öncelikle elindeki ETH ve BTC teminatları satmayı planlıyor. Eğer bunlar biter ve geriye kalan likit stake tokenleri satmak zorunda kalırsa o zaman nispeten daha sığ olan bu tokenlerin fiyatına negatif etki etme durumu olabilir. Bu arada elinde sUSDe olanların bu  parayı bozdurmak istediklerinde 7 gün beklemek zorunda olduklarını da hatırlatalım. 

Yine de şunu belirtelim; Ethena'yı duyan kişilerin ilk tepkisi "bu para, bir zamanlar gümbür gümbür batan UST'ye benziyor" oluyor ama yukarıda bahsettiğimiz senaryoda USDe bir dolara olan çapasını kaybetse bile burada öyle birden bire sıfıra düşecek bir durum yok. Bu, yavaş yavaş gelişecek bir süreç ve negatif fonlamanın daha uzun süreceğini düşünenler ellerindeki USDe'yi satarak çok daha az zararla piyasadan çıkabilirler (negatif fonlama oranı %100'e çıksa bile  bunun günlük maliyeti 100/365=%0.273 oluyor). 

#### Ethena riski 'hedge' etmek için merkezi borsalar kullanıyor. Bu riskli değil mi?
Öncelikle şunu belirtelim - Ethena'nın kurduğu sistemin benzeri geçmişte denendi ancak istenen seviyelere ulaşamadı. Bunun temel nedeni, bunu deneyen projelerin riski satmak için kullandıkları merkeziyetsiz türev platformlarının çok sığ olması idi. 

Bundan ders alan Ethena, türev piyasalarının çok daha likit olduğu merkezi kurumları kullanıyor. Peki bu daha riskli değil mi? Elbette. Sonuçta vadeli piyasada bu tip işlemlere girdiğinizde bir teminat vermelisiniz. Bu teminat da müşteri varlıkları. Ya bu borsalar bir anda batarsa ne olacak?

Bu riski yok etmek mümkün değil ancak Ethena riski azaltmak için çeşitli aksiyonlar almış durumda. Öncelikle, tek bir borsa değil en büyüklerden Deribit, Binance, Bybit, Bitget ve OKX ile çalışıyorlar. Bunun yanında, Ethena teminat verdiği varlıkların tam kontrolünü elinde tutuyor. Borsada herhangi bir sorun olması durumunda teminatını diğer borsalara taşıyabiliyor. (Bu arada yeri gelmişken belirtelim; Ethena kaldıraç kullanmıyor)

Peki ya Ethena takımı elinde tuttuğu bu paraları 'iç ederse'? Varlıklar üzerindeki bütün kontrolü elinde tutan Ethena saklama ve mahsuplaşma için Copper, Ceffu ve Cobo'yu kullanıyor. Peki ya Copper'a bir şey olursa? Orada da müşteri bakiyeleri olası bir iflastan etkilenmeyen kanuni bir yapıda saklanıyor (ingilizcesi bankruptcy-remote). 

Peki bakiyemizi borsada shortladık, para da kazanıyorduk ama borsa gitti battı. Ana bakiyeyi kaybetmedik ama kazancımız gitti. Şimdi ne olacak? Bunu önlemek için Ethena, genelde 8 ile 24 saatte bir,elde ettiği kârı borsalardan alıyor. Dolayısıyla risk sadece bu süre ile kısıtlı. 

Ethena tüm bakiyeleri ve short pozisyonlarını API'ler aracılığıyla alıp sitesinde yayınlıyor. Bunun dışında aylık olarak da emanet tuttuğu yerlerde duran bakiyelerin tam olduğunun teyidini (İngilizce attestation) alıp duyuracak. 

#### Kaldı mı başka risk?
Olmaz mı? Örneğin tüm DeFi'de olduğu gibi Ethena'nın kullandığı akıllı kontratlar da risk barındırıyor. Sonuçta bu yeni bir ürün, henüz savaş alanında test edilmedi. 

Sonra, Ethena uygulamasını kullanırken dışarıdan pek çok piyasa bilgisi almak zorunda. Bunun için de oracle dediğimiz bilgi sağlayıcıları kullanıyor. Buralarda oluşabilecek sorunlar Ethena'yı etkileyebilir. Ethena bu riski önlemek için hem Chainlink hem de Pyth bilgi sağlayıcılarını kullanmakta. 

Bu arada, özellikle ABD'deki düzenleyici otoritelerin kriptoya karşı hasmane tutumundan korunmak isteyen Ethena, emanet servisi ve borsa hizmetlerini ABD'den almıyor ve bu ülkeden kullanıcı kabul etmiyor. 

Bunların ötesinde henüz öngöremediğimiz senaryoların getirebileceği başka riskler de olabilir. Bunları da unutmamak gerek. 

#### Riskler çok mu fazla?
Ne kadar çok risk var değil mi? Evet doğru ama diğer yandan USDT ya da USDC tutan kullanıcılar da benzer şekilde riskler taşıyorlar. Orada da Tether'e ve paraları tutan bankalara güvenmek zorunda kullanıcı. 

Sonuç olarak kullanıcının kendi içinde bir risk değerlendirmesi yapması gerekli: Göreceli daha az riskli görünen ama herhangi bir getiri sağlamayan diğer stabil paralara mı gitmeli, yoksa daha riskli ama ciddi bir getiri sağlaması beklenen bu paraya mı yatırım yapmalı?

### Ethena nereye kadar büyür?
Ethena kurulduktan bu yana geçen üç ay içinde 2.3 milyar ABD doları büyüklüğe ulaşarak piyasanın en iyimserlerini bile şaşırtmayı başardı. Daha önünde gideceği çok yol var ancak potansiyelinin belli sınırları olduğunu da kabul etmek gerek. 

Öncelikle, short pozisyon açtığı platformlarda kullanabileceği limit sınırlı. Ethena ekibi, bu sınırın piyasadaki toplam açık pozisyon limitinin %30'u oranında olduğunu düşünüyor. Şu an piyasada ETH kontratı olarak 8 milyar ABD dolarlık bir büyüklük olduğunu düşünürsek bu 2.4 milyar USDe'lik bir limit demek. Tabii bu sadece ETH için. Bunun yanında BTC de kullanılabilir, ki orada da 16 milyar ABD dolarlık bir limit var. Bu da toplam sınırı bir anda 7.2 milyar USDe'ye getiriyor. Bu arada Chain Labs analizine göre ETH'nin piyasa değerindeki %1'lik bir artışın vadeli pazarları %1.2-%.1.45 oranında büyüttüğünü belirtelim. Yani, ETH ve BTC'deki değer artışları Ethena için daha fazla büyüme imkanı demek.

### Ethena'nın yönetişim tokeni ENA
Geçtiğimiz dönemde Ethena'nın çok kullanılmasının nedenlerinden biri de sistemi kullananlara verdikleri ENA yönetişim tokeni. ENA her ne kadar yönetişim tokeni olsa da ileride Ethena'nın kazançlarından bir kısmını almasını bekleyebiliriz.

Peki Ethena nasıl bir gelir yaratır? Burada üç tane varsayım yapmak gerekiyor. Sisteme teminat olarak yatırılan para ortalama ne kadar olacak? Bu paranın ne kadarı sUSDe olarak geri sisteme konacak? Son olarak da bu para nasıl bir getiri sağlayacak? Eğer i) Ethena sistemine yatırılan para şu anki gibi 2 milyar ABD doları civarında olmaya devam ederse ve ii) sUSDe olarak kilitlenen para toplam miktarın %50'si olursa; bu Ethena'nın kalan 1 milyar ABD dolarından gelen kazancı cebine atması demek. 2024 yılının ilk altı ayındaki short pozisyon gelirlerinin yaklaşık %12 olduğunu varsayarsak[^3], Ethena'nın yıllık olarak 120 milyon ABD doları bir gelir kazanması işten bile değil. Bu durumda Ethena, en karlı DeFi ürünlerinden biri olarak tarihe geçecek.

Bu arada şu anki short pozisyon gelirlerinin geçmiş yıllara göre az olduğunu, normalde bu ortalamanın yaklaşık %30'lar seviyesinde olduğunu belirtelim. Yine de Ethena, long ve short pazarındaki dengesizlikten yararlanarak bu kadar yüksek getiriler elde ediyor. İleride, bu pazara girecek kurumsal oyuncular da benzer şekilde short pozisyon açarak bu gelirden pay almak isteyecekler. Bu da short pozisyonları long pozisyonlara yaklaştıracağı için, elde edilen 'finansman geliri' haliyle azalacak.

### Bir nokta daha: MakerDAO da trene bindi
Bu arada yaşanan ilginç bir gelişme daha var. Piyasanın merkeziyetsiz oyuncusu olan DAI'yi çıkaran MakerDAO, yakın bir zaman önce açılan DAI/USDe ve DAI/sUSDe havuzlarına 300 milyon DAI enjekte etti. Temel olarak yapılmak istenen şu: ellerinde sUSDe tutan kullanıcılar, bu parayı getirip bu havuza koyarak karşılığında DAI borçlanabilecekler. Sonrasında bu DAI'yi satıp USDe alacak ve aldıkları bu USDe'yi tekrar Ethena sistemine kilitleyerek sUSDe alacak ve bunu tekrar bu havuza koyacaklar. Bu durum, sUSDe getirisi DAI borçlanma getirisinden yüksek olduğu sürece devam edebilecek[^5]. 

MakerDAO, kendisinden borçlanma yoluyla alınan DAI'ler için [şu anda  %20.82 oranında bir faiz uyguluyor](https://app.morpho.org/market?id=0xc581c5f70bd1afa283eed57d1418c6432cbff1d862f94eaf58fdd4e46afbb67f).  Bu durum hem USDe'nin kullanımını artırıyor, hem de MakerDAO için ekstra bir gelir kapısı yaratıyor. İki tarafı için de kazan-kazan (win-win) bir durum bu. 

### Sonuç 
Ethena'nın çıkardığı iki token hem rezerv para olma hem de bir bono gibi kazanç sağlama anlamında yatırımcıların bir kısmını tatmin edebilecek ürünler. 

Kompleks yapıları nedeniyle riskleri, yazımızda da anlattığımız gibi oldukça fazla. Üstelik henüz keşfedilmemiş yeni risklerin de gelmesi olası. Ne var ki, getirilerin yüksek olması uzun vadede yatırımcıları kendine çekecek gibi görünüyor. Buna bir de kısa vadede bu yıl sonuna kadar sistemi kullananlara verilecek ENA token teşviklerini eklediğinizde Ethena'nın bir anda bu kadar popüler olmasını anlamak zor değil. 

Burada üzerinde düşünülmesi ve takip edilmesi gereken, uzun vadede yukarıda bahsedilen risklerin Ethena ekibi tarafından nasıl minimize edileceğini görmek. Ayrıca alınan önlemlerin oluşabilecek risklere karşı sistemi ne kadar koruyacağını test etmek için de zamana ihtiyaç var. Öte yandan, piyasalardaki dengesizlik nedeniyle ortaya çıkan fonlama kazançlarının, Ethena daha da büyüdüğünde nereye evrileceğini, bu kadar kârlı kalıp kalmayacağını gözlemek de önemli. Dikkatle takip ediyor olacağız.

---

*Bu yazının hazırlanmasında [Ethena](https://ethena-labs.gitbook.io/ethena-labs) ve Delphi Digital'in 'The rise of Ethena - Unpacking the Emerging Synthetic Dollar' yazısı kaynak olarak kullanıldı.*

Notlar:
[^1]: Yazının hazırlanması sırasında bu oran [%0 seviyesinde idi](https://app.spark.fi/dashboard). 

[^2]: Basitleştirmek amacıyla 'kullanıcı' terimini kullandık. Aslında, bu para basma işinin sadece önceden onaylanmış (ingilizcesi white-listed) oyuncular yapabiliyor.  Bu arada her ne kadar Ethena sansüre dayanıklı olduğunu iddia etse de, yarın öbür gün piyasadaki kimi USDe'leri dondurması istenince nasıl bir davranış sergileyecek, bunu tam olarak bilmiyoruz. 

[^3]: Short pozisyon gelirleri 2024 yılının ilk çeyreğinde %17.6, ikinci çeyrek Mayıs ayı ortasına kadar %7.92 olarak gerçekleşmiş durumda. 

[^4]: Bu aslında klasik anlamda bildiğimiz futures vadeli piyasanın bir başka versiyonu. Klasik anlamdaki futures'dan farkı, perpetuals piyasasında herhangi bir vade yok. 

[^5]: Peki bu durumun MakerDAO için riskleri yok mu? Var ancak konumuz bu olmadığı için şimdilik dışarıda bırakıyoruz. Bu riskleri merak edenler Delphi Digital'in yukarıda kaynak olarak verdiğimiz raporunu inceleyebilirler. 

[^6]: Circle'in eski ortağı olan Coinbase USDC'yi kendisine kilitleyenlere [belirli bir oranda getiri veriyor](https://help.coinbase.com/en/coinbase/coinbase-staking/rewards/usd-coin-rewards-faq).

---

*Not 1: Bu yazı ilk olarak 30 Mayıs 2024'de [BTC Haber'de yayınlandı]()*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Piyasada oluşacak ihtimalleri değerlendiren bu yazıyı, yatırım tavsiyesi olarak almamanızı rica ederiz. Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

**Dipnotlar**
