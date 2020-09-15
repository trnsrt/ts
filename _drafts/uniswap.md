
### Nedir bu Uniswap?

Uniswap merkeziyetsiz olarak işlem yapılan bir kripto para borsası - ve bu alanın eskilerinden. Her ne kadar borsa olarak adlandırsak da Uniswap özünde İngilizcesi market maker olarak adlandırılan piyasa yapıcı bir havuz. Biraz daha açalım: 

Öncelikle merkeziyetsizliğe bakalım. Merkez olmayınca aklımıza ilk olarak kişiden-kişiye (peer-to-peer P2P) işlem geliyor ancak Uniswap biraz daha farklı olarak kişiden-kontrata (peer-to-contract) işlem denen bir sistem ile çalışıyor . Yani kişi bir işlem yapmak istediğinde karşısında bir başka kişi yok, bir kontrat var. Ve bu kontratın arkasında da bir havuz. 

Piyasa yapıcı olmak ise bir alım ya da satış yapmak istediğinizde size istediğiniz ürünü satmak ya da sizden o ürünü almak için hazırda bekleyen bir taraf olması anlamına geliyor. 

Sonuç olarak kişiler birbirleri ile değil, yapmak istedikleri her işlemi gerçekleştiren bir havuza karşı işlem yapıyorlar. 

Temel olarak iki ana grup var Uniswap'ta. İlki kullanıcılar; bunlar bildiğimiz anlamda işlem yani alım-satım yapanlar. Bir de havuza likidite sağlayanlar - ki bunlara hissedar denebilir ama biz paydaş terimini kullanalım ([bir önceki SNX yazımızda olduğu gibi](/genel/2020/08/28/Defi-turev-piyasasi-synthetix-nasil-calisiyor.html)). Şimdi gelin kim neden kullanır bu sistemi ona bakalım. 


### Kim neden Uniswap’ta işlem yapar?

UniSwap’ın popüler olmasının birkaç temel nedeni var: 

Öncelikle alım-satım yapanlar için Uniswap ve (genel olarak DeFi) en önemli kullanım nedeni [kolaylığı](/genel/2020/07/23/DeFi-yeni-ICO-cilginligi-mi.html). Kullanıcının öyle çok büyük parası olması gerekmiyor, belli spesifik bir ülkede oturmak gibi coğrafi bir kısıtı yok. Herhangi bir şekilde hiç bir yere kayıt, evrak vs gönderip başvuru sonucunu beklemesine gerek yok.  DeFi kullanmak isteyen birinin tek ihtiyacı olan bir kripto cüzdan. Kullanıcı Uniswap [sitesine](https://app.uniswap.org/#/swap) girdikten sonra sağ üst tarafta bulunan butona basıp cüzdanını bağladığı anda sistemi kullanmaya saniyeler içinde başlayabiliyor. Teknik olarak bir öğrenme süreci gerektirse de klasik finans sisteminin çoğunlukla aşılamayan engelleri yok burada. 

Bunun yanında emir defteri ile çalışan piyasa yapıcılar, istedikleri emir gerçekleşmeden önce pek çok geçici emir yazıp sonra iptal ederler. DeFi dünyasında özellikle yoğunluğu bağlı olarak sistem kullanım ücretlerinin ([daha önce bahsettiğimiz gas ücretleri](/genel/2020/08/06/gelecekte-eth-nin-degerini-neler-etkileyecek.html)) yüksek olması piyasa yapıcıların bu tip emir yazma/iptal işlemlerinin maliyetlerini çok artırıyor. Bu nedenle Uniswap’ın özellikle likit havuzlarında işlem yapmak alım-satım yapanlar için daha az maliyet çıkarabiliyor. 

Kripto alanındaki girişimler için de belli avantajları var Uniswap'ın. Önceleri bir kripto paranın merkezi borsalarda işlem görebilmesi için bu borsaların koyduğu kurallara uyması ama daha da ötesi bu borsalara ciddi paralar ödemesi gerekiyordu. Uniswap ise Blokzincir’in “izin gerektirmeyen (permissionless)" ruhuna uygun olarak isteyen herkesin listeleme yapabileceği bir pazar. Küçük girişimler çıkardıkların tokenlara pazar tarafından değer biçilebilmesi ve likidite sağlanabilmesi için Uniswap'ı kullanmaya başladılar. Bu arada, Uniswap popüler olmaya başlayınca 2020 yaz aylarında Binance ve FTX gibi borsaların da yeni tokenları bir an önce hızlıca listelemeye başladıklarını gördük - ne demişler "rekabet her zaman iyidir". 

### Peki nasıl çalışıyor sistem?

UniSwap aslında robot (otomatik) bir piyasa yapıcı. Robot denmesinin nedeni fiyatların çok basit bir algoritma ile otomatik olarak “el değmeden” belirlenmesi. Gelin kısaca göz atalım bu otomatik sistemin nasıl çalıştığına: 

Uniswap’ta bütün işlemler için çift bölmeli yani iki farklı tokendan oluşan bir havuzlar var. **Siz kullanıcı olarak herhangi bir havuzdan bir token almak istiyorsanız, karşılığında içerideki diğer tokeni havuza bırakmak zorundasınız**.  Yani alım-satım dediğimiz aslında bir swap (bir tokeni diğeri ile değiştirme) işlemi oluyor. 

Herhangi bir Havuz ilk kurulurken içindeki iki bölmenin piyasa değeri birbirine eşit oluyor. Her bir bölme içine ne kadar gerekiyorsa o kadar token ile dolduruluyor. Sonrasında bu token adetleri çarpılarak sabit bir toplam havuz büyüklüğü bulunuyor. İşte bu sabit havuz büyüklüğü sayısı kritik, çünkü tüm sistem hesaplamaları bu sayıya dayanıyor. 

Dilerseniz bir örnek ile anlatalım: 

Diyelim bir havuz oluşturulacak. Bir bölüme ETH, diğerine ise USDC (bir çeşit sanal ABD Dolarına çıpalı bir sabit para) konacak. 

- İlk başlangıçta kurulurken bu iki havuzun piyasa değerleri birbirine eşit olmalı ki işe doğru bir şekilde başlansın.  Basit olması için başlangıçta havuzu doldururken piyasalarda 1 ETH’nin değerinin 300 USDC'ne denk olduğunu varsayalım. ETH havuzuna 100 ETH konursa, USDC havuzuna da bunun eş değeri 30,000 USDC konacak. 
- Şimdi gelelim temel prensibe: “**İki havuzdaki para adedinin (değer değil ADET) çarpımı her zaman sabit olacak**”. Kulağa saçma geliyor değil mi? Haklısınız, ama örneğimizden devam edelim: Burada 100 adet ETH ve 30.000 adet USDC olduğu için toplam havuz katsayımız bu iki sayının çarpımı olan 3.000.000. Bu sayı hep sabit. [^1]
- İşlem yapmak isteyen biri havuza geldiğinden ETH satmak istiyorsa karşılığında havuzdan bunun karşılığı USDC alacak, eğer ETH almak istiyorsa bunun karşılığı kadar USDC koyacak. Peki bu “karşılık” nasıl belirlenecek? İşte orada temel prensibimize geri dönüyoruz. Yani sabit sayımıza. Örnekten devam edelim:
   1. *Diyelim biri gelip 1 adet ETH satmak istiyor:* Bu durumda ETH havuzu bir adet artıp 101 ETH’ye çıkacak. Sabit sayımız 3.000.000 idi ve bu sayı ETH adedi ile USDC adedinin çarpımına eşit olacaktı. Bu işlem gerçekleştiğinden havuzun büyüklüğünün sabit kalması için havuzda 3.000.000/101=29.703 adet USDC olmalı. Yani ETH alan kişiye havuzdaki ETH’lerin 30.000-29.703=297 adedi gönderilir. Ama fiyat 300 USDC olacak idi, neden 297 alıyorum? Çünkü likit olmayan bir piyasada büyük bir işlem yaptınız ve piyasayı hareket ettirdiniz. Buna slippage (kaygan düşüş-performans düşüşü) deniyor. Çok büyük bir havuzda küçük işlem yapanlar için böyle büyük farklar çıkmaz
   2. *Peki biri daha gelip bir ETH daha satmak isterse?:* Aynı işlem tekrarlanıyor. Yani ETH sayısı 102’ye çıkacak o zaman USDC rakamı 3.000.000/102=29.412 adede inmeli. Havuzda ise önceki işlemden kalma 29.703 adet USDC var. İkisinin farkı 291 adet USDC kullanıcıya gönderiliyor. Birinci ile ikinci ETH satanın aldıkları USDC'lerin arasındaki farkın ne kadar ciddi olduğunu görüyorsunuz değil mi? Arz-talep dengesi işte bu şekilde çalışıyor, bir ürünün adedi arttıkça değeri azalıyor. 
   3. *Peki üçüncü bir işlem olarak biri gelir ve bu sefer satmak yerine 1 ETH almak isterse?:* Farketmişsinizdir sistem hep ne koyacağınıza bakıp size ne koymanız gerektiğini söylüyor. Havuza "1 ETH almak istiyorum" dediğinizde havuz size göndereceğiniz USDC'yi hesaplıyor. Katsayımız 3.000.000’u yeni oluşacak ETH havuzundaki adet olan olan 101'e böldüğünüzde USDC havuzu rakamının 29.703 olacağı ortaya çıkıyor. Yani kullanıcının bir ETH alabilmesi için 297 adet USDC koyması gerekiyor havuza. Farkı görüyorsunuz değil mi? Piyasada olsa 1 ETH'yi 300 USDC'ye alabilecek iken havuzda daha önceki işlemlerden dolayı ETH fazlalığı olduğu için aynı ETH'yi şimdi 297 USDC'ye alabiliyor bir kullanıcı.

Yukarıdaki üç işlemin sonucu havuzdaki ETH, USDC ve havuz büyüklüğündeki değişimleri bir tabloda toplarsak: 

![Uniswap_islemler_640.png](/assets/Uniswap_islemler_640.png)

Hemen belirtelim: yukarıda verdiğimiz işlemler oldukça sığ bir havuz için yapılmış bir örnek. . Havuz ne kadar büyük olursa, ya da yapılan işlemin havuzun büyüklüğüne oranı ne kadar küçük olursa bu fark o kadar az oluyor. İşte bu nedenle bu tip borsalar için likidite hayati bir öneme sahip. (Adım adım Uniswap işlemlerini nasıl yapılıyor görsel olarak görmek isterseniz [şu Medium yazısında](https://medium.com/@obiwancoin/uniswap-kullan%C4%B1m-rehberi-obi-wan-bd73503fb9d6) oldukça güzel anlatılmış). 

### Kim neden havuza para koyar?

Peki kim havuza bu parayı koyuyor? Yatırımcılar ya da likidite sağlayıcılar dediğimiz paydaşlar. Neden koyuyorlar bu parayı? İşlem yapıldığında belli bir komisyon ücreti ortaya çıkıyor (Uniswap için şu anda %0,3 oranında) ve toplanan komisyonlar likidite sağlayıcılar arasında pay ediliyor. Dolayısıyla yukarıda yazdığımız likiditenin önemi bir kez daha ortaya çıkıyor. Zira likidite hem sistemi yürütüyor, hem de ne kadar çok olursa o kadar az kayıp olacağı için al-sat yapanı havuza çekiyor ve işlem hacmini büyütüyor, bu da sistemin kârlılığını artırıyor. 

#### Havuza para koymak çok kârlı gibi görünüyor?
Kulağa çok hoş gelse de havuza para koymak her zaman kârlı olmayabiliyor. Bakın neden: 

Sistemdeki en kritik risk ani ve kalıcı fiyat artışlarında ortaya çıkıyor. Eğer piyasalarda ETH fiyatı aniden 400 USDC’ye çıkarsa, Uniswap robot sistem olduğu için ani tepki veremiyor. Bunun ne gibi zararı var? Bir kısım arbitraj yapanlar, anında UniSwap havuzuna USDC koyup ETH’leri ucuzdan çekebiliyorlar (1 ETH'nin karşılığı 400 USDC'ye denk olana kadar). 

Şimdi yukarıdaki senaryoya sisteme likidite sağlamış bir kişinin perspektifinden bakalım: 
- Diyelim bu kişi en başta havuzun bir tarafına 10 ETH diğer tarafına ise 3.000 USDC koymuş yani havuzun %10'una sahip olmuştu. 
- Yukarıda bahsettiğimiz ETH fiyatı artıp 400 USDC’ye çıkınca al-sat’çılar havuzdaki ETH'leri alıp yerine USDC ile koyar. Havuzda şimdi toplam 86,6 ETH ve 34.641 USDC olacak. (Neden derseniz ayrıntılı işlemi dipnotta) [^2]. 
- Bu kişiye de %10 payı olarak 8,66 ETH ve 3.464 USDC’ye düşecek. Bu da USDC cinsinden 8,66 ETH x400=3.464 artı 3.464 USDC toplam 6.928 USDC olur. 
- Halbuki bu kişi ETH ve USDC'sini havuza yatırmayıp elinde utsaydı USDC cinsinden 10 ETH x 400=4.000 artı 3.000 USDC toplam 7.000 USDC varlığı olacaktı. 
- Aradaki para nereye gitti? Sistemde fiyatların ani artışını değerlendiren al-sat’cılara. Buna “geçici kayıp” (impermanent loss) deniyor, zira bir noktada ETH tekrar 300’e gelirse o zaman havuza likidite koyanın zararı ortadan kalkıyor. 

Bu komisyonlardan kazanılan para şimdiye kadar ani değişikliklerden kaybedilen paranın önüne geçmiş ama bu ileride de böyle olacağı anlamına gelmiyor. Yani likidite koyanlar ciddi bir risk taşıyorlar. 

| ![USDC getirileri](/assets/USDC_Uniswap_returns_1200.png)|
|:--:| 
| *Uniswap içindeki en büyük havuz olan USDC havuzunun son bir yıl getirisi. Kırmızı çizgi gelir, mavi çizgi kayıp, sarı çizgi ise kâr (ROI) - [Kaynak](https://zumzoom.github.io/analytics/uniswap/roi/)*|

Ani ve kalıcı fiyat değişikliklerinden bu kadar etkilendiği düşünüldüğünde havuzlar içinde en kârlı olanları aslında değerlerinin tekrar eski haline döneceğini bekleyeceğiniz token çiftleri. Nedir bunlar derseniz, stabil para havuzları. Örneğin USDC/DAI çiftinden oluşan havuzlar. Stabil paralar genelde 1 ABD Doları’nın etrafında gezinir dururlar. Bazen üzerine çıkar, bazen altına inerler. Dolayısıyla likidite koyanlar "geçici kayıp" fazla yaşamazlar ve oldukça iyi kâr ederler. 

Tabii, madalyonun öbür tarafında bu çiftlerde fiyat değişimleri de çok küçük boyutlarda olur, işlem yapılınca elde edilen kârlar da az olur. Marjların az olduğu bir yerde bir de UniSwap’a 0.3% komisyon vermek ister mi al-sat yapanlar? Tabii ki hayır ve işte bu nedenle stabil paraların ikili havuzlarını yaratan Curve daha popüler oldu. Yazı çok uzadı. Sonraki yazılarda gerek Curve gerekse Balancer gibi yenilikçi piyasa yapıcılar ile Sushiswap gibi Uniswap klonlarını inceleyelim. 

### Sonuç 
Uniswap, çok basit bir algoritma ile merkeziyetsiz olarak alım-satım yapmayı sağlayan bir platform. Güçlü bir ekibi ve sağlam bir yatırımcı grubu var arkasında. Uniswap'da işlem yapanlar, işlem sırasında kendilerine verilen ile son işlem öncesi fiyatlara dikkat etmeli. Ayrıca, merkeziyetsiz bir borsa olmasından dolayı isteyen herkes havuz kurabildiği için işlem yapılan tokenların doğru token olduğuna emin olmalı. Uniswap havuzlarına likidite sağlayanlar ise sistemin yetersiz kaldığı noktalara dikkat ederek, "dimyata pirince giderken eldeki bulgurdan olmamalı". Uniswap sonrası çıkan yeni rakipler, hem onun kullanıcılara veremediği özellikler (daha düşük komisyon, farklı havuz oranları), hem de likidite sağlayıcılara verdikleri ekstra yönetim token'ları ile farklılaşma yaratmaya çalışıyorlar. Önümüzdeki günlerde üçüncü versiyonunu çıkarmayı planlayan Uniswap bakalım bu ataklara nasıl karşılık verecek?

---


[^1] Basitleştirmek için böyle yazıldı. İki istisnası var havuz büyüklüğünü değiştiren: 
Birincisi havuza başka yatırımcılar para koyarsa havuzun toplam büyüklüğü değişiyor normal olarak. Örnek olarak bir yatırımcı gelip 10 ETH ve 300 USDC koyarsa, havuzun toplam büyüklüğü 300.000’den 363.000’e (110 ETH x 3,300 USDC) çıkıyor. 
İkincisi ise işlem yapanlardan alınan komisyonlar (Uniswap için %0.3) bu havuza ekleniyor, dolayısıyla havuz büyüklüğü otomatik artıyor. 

[^2] Matematiksel olarak havuzun içindeki USDC adedinin (A) ETH adedine (B) bölünmesi 1 adet ETH'nin fiyatını (A/B) verir. Neden? Çünkü havuza eşit değerde USDC ve ETH konmuştu. Örneğimizde  havuza 30.000 USDC ve 100 ETH konmuştu dolayısıyla bir ETH'nin fiyatı 30.000/100=300 USDC ediyor idi. Öte yandan USDC adedi ile ETH adedinin çarpılması havuzun sabit sayısını (AxB) veriyor demiştik. O zaman ETH fiyatı (A/B) ile havuz sabitinin (AxB) çarpımının karekökü USDC adedini verir. Bu işlemi yaparsanız USDC adedi 34.641’i çıkar. Bu sayıyı toplam havuz değerine bölersek ETH adedi olan 86,6’e ulaşırız.  Sağlama için USDC adedini (34.641) ETH adedine (86,6) bölersek ETH fiyatı olan 400 çıkar. (Daha detaylı açıklamayı ingilizce olarak [Uniswap sitesindeki şu linkte bulabilirsiniz](https://uniswap.org/docs/v2/advanced-topics/understanding-returns/))


