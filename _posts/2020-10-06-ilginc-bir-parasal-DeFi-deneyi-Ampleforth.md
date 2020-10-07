---
layout: post
title:  "Defi'de ilginç bir parasal deney: Ampleforth"
date:   2020-10-06 18:47:56 +0300
categories: Genel
tags: Yazılar DeFi
---

Bugün sizlere geçtiğimiz aylarda ilk çıktığında büyük sükse yapan, sonrasında ardına ardına gelen yeni girişimlerin de etkisiyle ana sahneden uzaklaşan ilginç bir DeFi projesinden bahsedelim. 

Gözden ırak olan gönülden de ırak olmaz mı? Neden zaman ayırıp bakalım? Çünkü kripto dünyası şu anda emekleme aşamasında. İçinde o kadar farklı ve ilginç dinamikler ve değişkenler taşıyor ki bunların her biri ile oynayarak pek çok farklı deney yapılabiliyor. Çıkan her proje yaşanmakta olan bir derde deva olabildiği kadar beraberinde başka sorunlar getirebiliyor, ya da kullanıcılarda yeni ihtiyaçlar ortaya çıkarabiliyor. İşte bu yazımızın konusu olan [Ampleforth](https://www.ampleforth.org/) da benzer şekilde mevcut bir soruna merkeziyetsiz bir çözüm getirmek hedefiyle ortaya çıkmış bir proje. Gelin bakalım neymiş:

### Nedir Ampleforth?

Ampleforth bir deney - nihai hedefi alışverişte kullanılabilecek kadar stabil ancak Bitcoin benzeri değeri kendinden menkul bir para olmak. Ve bunu yaparken de hem stabil paraların hem de Bitcoin'in zayıf yanlarını güçlendirecek çözümler getirmek. Önce bu sıkıntılara bir göz atalım:  

#### Stabil paraların sıkıntısı
Piyasada yeterince stabil kripto para varken neden Ampleforth'a ihtiyaç olsun? Çünkü stabil paralar özünde bir itibari paraya bağlılar (itibari paranın devletlerin merkez bankaları tarafından basılan ABD Doları, Euro benzeri paralar olduğunu tekrar hatırlatalım). Bu itibari paralar görünüşte değerlerini koruyor gibi görünseler de aslında uzun vadede sürekli değer kaybı yaşıyorlar. Amerika Birleşik Devletleri altını 1933 yılında onsu [20 ABD Doları'ndan halktan toplamıştı](https://en.wikipedia.org/wiki/Executive_Order_6102) (enflasyon etkisini yedirseniz bile günümüzde 408 ABD Doları'na geliyor), şu anda altın 2,000 ABD doları seviyelerinde. Şimdi ABD Dolarının değerinin sabit kaldığını söyleyebilir misiniz? 

| ![BTC_dominance](/assets/Executive_Order_6102_640.jpg)|
|:--:| 
| *ABD hükümetinin halktan zorla altın topladığı meşhur 6102 sayılı emir.  Kaynak: [Wikipedia](https://https://en.wikipedia.org/wiki/Executive_Order_6102)*|

Ayrıca  bu stabil kripto paralar ödemeler konusunda çözüm olsalar da, bu paraları basanların ağırlıklı bir kısmının merkezi yapılar olması beraberinde yeni sorunlar getiriyor. Yakın zamanda yaşadığımız [Tether'in müşteri hesaplarını dondurabilme gücü]((https://en.ethereumworldnews.com/bitfinex-and-tether-freeze-33m-usdt-from-kucoin-hack/)) (ki Kucoin hack'inde 33 milyon ABD Dolarını dondurdular) kripto dünyasının bireylere en büyük faydası olarak da bilinen "dijital varlığa tümüyle sahip olma" özelliğinin nasıl delik deşik edildiğinin de bir göstergesi aslında. 

#### Bitcoin'in sıkıntısı
Bitcoin benzeri sınırlı arza sahip paralar teori olarak güzel: Değer anlamında hiçbir kuruma bağlı olmayan, bütünüyle bağımsız, sansüre karşı dayanıklı ve sınırlı arzı ile değerini teorik olarak koruması gereken bir para. Ancak bu sınırlı miktardaki arz, artıp azalan talep ile bir araya geldiğinde ortaya son derece oynak bir para çıkıyor. Her ne kadar uzun vadede son on yılda yaşanan fiyat artışının en önemli nedenlerinden birinin bu kısıtlı arz olduğu düşünülse de kısa vadelerde oluşan oynaklık sinirleri zorlayacak seviyede. 


| ![BTC_price](/assets/BTC_price_coingecko_800.png)|
|:--:| 
| *BTC'nin baş döndürücü dalgaları.  Kaynak: [CoinGecko](https://www.coingecko.com/en/coins/bitcoin)*|


**İşte Ampleforth, bir yandan Bitcoin gibi uzun vadede yatırımcısına değeri artacak bir varlık sunarken, diğer yandan stabil paralar gibi kısa vadede değeri değişmeyen ve bu sayede alışverişlerde kullanılabilecek bir para yaratma hedefinde.** 

Peki nasıl bir taşla iki kuş vuracak? Anlatalım: 

### Nasıl çalışıyor Ampleforth?

Ampleforth, fiyat tarafında görülen oynaklığı önlemek adına, talepte meydana gelebilecek değişimlerin fiyata radikal etki etmesinin önüne geçmek yani paranın değerini dengelemek için paranın arzının değiştirilmesi prensibine dayanıyor. Hem de ne değiştirmek! Gelin biraz daha açalım bunu: 

Ampleforth otomatik olarak çalışan bir algoritma - insan eli değmiyor, "kod kanun" bir başka deyişle. **Algoritmanın tek bir hedefi var: O da sistemin parası AMPL'yi sabit bir değerde tutmak.** Bu değer 2019 yılındaki 1 ABD Dolarına eşitlenmiş. Şu an için enflasyon giydirilmiş [olarak 1.019 ABD Doları seviyesinde](https://www.ampleforth.org/dashboard/). 

Bir sistemin parasını sabit tutarken yatırımcıların ilgisini nasıl çekebilirsiniz? Öyle ya, hisse değeri sabit kalırsa benim varlığımın değeri de aynı kalır. İşte burada yatırım ile ilgili kafamızdaki klasik kalıpları şöyle bir yeniden gözden geçirmekte fayda var:

#### Önce bir zihnimizi açıp, ezber bozalım

Bir şirketin hisse senedini satın aldığımızda yatırımımızın toplam değeri, şirketin toplam hisse senetlerinden elimizdeki kaç tanesi varsa bunun her bir hissenin değeri ile çarpılması sonucu ortaya çıkar. Ancak elimizde tuttuğumuz hisse senedi adedi genelde değişmediği için yatırımızın toplam değerindeki değişimi genelde hisse senedindeki hareketlerden hesaplarız (alım ya da satım yapmadığımızı varsayarsak). Bir başka deyişle, bir adet hissenin değeri yatırımımızın değerini bulmada bize 'kısa yol' olur. 

Ama Ampleforth, yukarıda yazdık, her bir token'in (yani hissenin) değerini sabit tutmak istiyor. Nasıl olacak bu? Diyelim bir anda token'a bir talep oldu, insanlar deli gibi AMPL almaya başladılar. Fiyat nasıl aynı kalacak? Kalmalı mı? Token değerini sabit tutmak ile yatırımın değerini artırmak birbiri ile çelişiyor mu? İşte burada, yukarıdaki paragraftaki önyargımızı bir kenara bırakalım.

**Bakmamız gereken tüm sistemin değeri ve bizim onun içindeki toplam payımızın büyüklüğü olmalı. Token'in değeri değil.** 

Peki nasıl olacak bu? Toplam değerin iki çarpanı var demiştik. Toplam token adedi ve her bir token'in değeri. Eğer talep artışından dolayı sistemin toplam değerinin artması bekleniyor ama bir yandan da bir tokenin değerinin sabit kalması isteniyorsa o zaman token adedini artırırız!

Ezberlerimizi yeterince bozduk mu? :) 

Sistemin nasıl çalışacağını gelin bir de örnek üzerinden anlatalım: 

#### AMPL token fiyatı yükselirse ne oluyor?

Varsayalım, 1 AMPL 1 ABD Dolarına eşit ve yatırımcımızın da 100 AMPL'si var, yani 100 ABD Dolarına eş bir yatırımı. Bir anda piyasalarda AMPL'ye talep oldu ve AMPL fiyatı 1.5 AMPL'ye çıktı. İşte o zaman algoritma otomatik olarak devreye giriyor (mevcut fiyat ile hedef arasında artı/eksi %5'den fazla fark olursa algoritma çalışıyor) ve her bir AMPL karşılığı yatırımcılara 0.5 AMPL daha veriyor. Yatırımcımızın artık 150 AMPL'si var!

Buraya kadar her şey otomatik el değmeden çalıştı. Piyasa fiyatını gören sistem para arzını otomatik artırdı. Bundan sonrasında beklenen, piyasanın tepkisel davranması ve paranın bollaşması ile birlikte fiyatın hedeflenen seviyeye düşmesi. Başta ne demiştik; sistemin hedefi AMPL'nin 1 ABD Doları'na geri dönmesi. Sistemin para yaratmasının arkasında yatan düşünce şu: Eğer bir anda insanların elindeki yatırım 1 ABD Doları iken, fiyat artışından dolayı 1.5 ABD Doları'na, sonrasında AMPL artışından dolayı 1.5 AMP x 1.5 ABD Doları = 2.25 ABD Doları'na çıkarsa, insanlar, özellikle al-sat yapanlar, kârı realize etmek için ellerindeki AMPL'yi satarlar. Bu da AMPL fiyatını düşürür. Nereye kadar? Fiyat tekrar 1 AMPL = 1 ABD Doları olana kadar. 

Böyle olunca ne oldu? Hızlı hareket eden al-satçılar ciddi bir para kazandılar. Sistemin buna bir itirazı yok - zira sistemin tek isteği AMPL fiyatının tekrar 1 ABD Doları'na dönmesi. Peki alım satım yapmayıp ellerinde tutanlar? Onlar da aslında ekstra bir kâr/zarar etmediler. Yukarıdaki yatırımcımızın başlangıçtaki yatırımı 100 dolar idi, sonra sistem onlara AMPL verdiği için ellerinde 150 AMPL oldu ve ilk anda 225 ABD Dolarına eşitti ancak fiyat tekrar 1 ABD Dolar seviyesine geldiğinde son durumda yatırımın değeri 150 ABD Doları'na çıktı. Yani ilk fiyat artışı sonrası gibi yatırımcı %50 kazancı cebine koymuş oldu. 

Aslına bakarsanız, AMPL sisteminin yapmaya çalıştığı, paranın arzını artırarak yatırımcılar üzerindeki etkiyi büyütmek ve onların daha hızlı reaksiyon vermesini sağlamak. Biraz açalım bu dediğimizi: Diyelim aldığınız bir token'da %60 kazanç beklentiniz var, eğer token size %60 kazandırırsa yeterli olduğunu düşünüp satacaksınız. Yukarıdaki senaryoda eğer para arzı sabit kalsa idi, fiyat %50 arttığından dolayı satmayacaktınız. Ama elinizdeki tokenların sayısı da artınca toplam kazancınız bir anda %125'e çıktı, hemen harekete geçip satmaz mısınız? Sizin gibi satmaya başlayanlar olacaktır, bunun sonucu token fiyatı düşmeye başlar ama hâlâ kazanç yüksek olduğu için bekletinizin gerçekleşeceği rakama kadar satamaya devam edersiniz. İşte böyle böyle düşen token fiyatı sistemi hedeflediği noktaya kadar getirir. 

Bir başka bakış açısından, **sistem kendi içinde talebin değişmesinden dolayı oluşabilecek fiyat hareketlerindeki volatilite yükünü, arzı değiştirerek fiyattan yani sistemden alıp, yatırımcıya geçiriyor**. Bir önceki paragrafı tekrar edelim: Arzı değiştiriyor, dolayısıyla yatırımcılar hisse fiyatındaki değişimin daha da fazlasını varlıklarındaki değişimlerde hissedip daha hızlı bir şekilde aksiyon alıyorlar, bu da hisse fiyatını eski haline döndürüyor. 

#### Peki ya fiyat düşerse?

Tabii bir de madalyonun öbür yüzü var. Ya, talepte bir azalma olur ve token değeri bir anda düşerse? Diyelim, bir hareket ile hisse değeri %50 değer kaybetti ve 1 AMPL 0.5 ABD Doları'na eşit hale geldi. 

İşte orada da sistem tam tersi çalışıyor. Yatırımcıların cüzdanlarındaki AMPL'lerin yarısını ellerinden alıyor! Yok artık! Evet, aynen öyle. Niye? Aslında mantık yukarıda anlattığımızın aynısı. Sistem şöyle düşünüyor: "Ampleforth'un toplam sistem değeri düşüyor - olabilir ama bu beni ilgilendirmiyor. Beni ilgilendiren 1 AMPL'nin tekrar 1 ABD Doları'na denk hale gelmesi. İnsanlar satıyor AMPL'leri, demek ki piyasada AMPL bolluğu var. Ben bu AMPL'leri piyasadan çekersem hem arz azalmış olacak, hem de AMPL sistem değeri düştüğü için ucuzlamış olacak. Bunu gören yatırımcılar nasıl hisse değeri düştüğünde o hisseyi almaya çalışıyorlarsa burada da AMPL sistem değeri kat be kat düştüğü için almaya koşacaklar. 

Yukarıdaki örnekten devam edersek. Başlangıçta 100 ABD Dolarına eş 100 AMPL vardı elinizde. Token değer kaybedince varlığınız önce 100 AMPL x 0.5 cent = 50 ABD Doları seviyesine düştü. Sonra bir de sistem elinizdeki AMPL'lerin yarısını aldı, dolayısıyla varlığınız bir anda geçici olarak 50 AMPL x 0.5 cent = 25 ABD Doları'na geriledi. Sizin sistem içindeki payınız hiç değişmedi. AMPL sistemi değer kaybetti. AMPL kendi içinde %50 değer kaybetti ancak tüm sistem %75 değer kaybetmiş oldu. Bu kadar ucuzlamış bir sistemi almak için üşüşen yatırımcılardan dolayı AMPL tekrar değer kazandı, nereye kadar? Dengenin oturacağı 1 AMPL = 1 ABD Doları seviyesine kadar. O zaman son durumda varlığınız ne oldu? 50 AMPL x 1 ABD Doları = 50 ABD Doları.  Varlığınız değer kaybetti mi? Gayet tabii - zira talep azaldığı için zaten başta kaybetmiştiniz onu. Geçici olarak arz kısılmasından dolayı daha da kaybettiniz ama en sonunda %50 kaybettiğiniz ilk noktaya döndünüz. 

#### Fiyat konusundaki bu ısrar neden?

Hisse (ya da token) fiyatını sabit tutmak neden önemli? Bir paranın alım satım ve ticaret için kullanımı ancak değerinin "gerçek" anlamda sabit olması durumunda gerçekleşebilir. Öte yandan yatırımcılar tarafından bu paranın rağbet görmesi için varlığın değerinin artması gerekir. İşte Ampleforth, sabit değerli bir para yaratarak alışverişlerde güvenle kullanılabilecek bir para yarattıktan sonra, bu paranın rağbet görmesi durumunda yatırımcısına da değer kazandıracak bir enstrümana dönüşmesini sağlıyor. Sabit paralardan en büyük farkı bu: Kullanan için sabit para, yatırımcısı için eğer kabul görüp yaygınlaşır ise değer kazandırıcı bir enstrüman. 

Yani tekrar edecek olursak, **yatırımcılar AMPL'nin sabit değerli bir para olarak kullanımının yaygınlaşmasını, yaygınlaşan kullanımın AMPL token'ına yönelik talebi yukarıya çekmesini, yükselen talebi karşılamak amacıyla ekstra AMPL token yaratılmasını dolayısıyla Ampleforth sisteminin toplam ağ değerinin artmasını bekliyorlar**. Artan Ampleforth sistem değeri sonucu ortaya çıkan ekstra AMPL'ler de yatırımcılara dağıtılacağı için AMPL değeri sabit kalsa bile toplam yatırımlarından kâr sağlama beklentisi içindeler. 

### Ampleforth'un vizyonu

Ampleforth'un arzı ile oynamak suretiyle üçlü aşamalı bir vizyonu var aslında: 

İlk aşama kısa vadede portföyünde kripto varlık tutanlara risklerini dağıtmaya yardımcı olmak. Çıkış noktaları şu: Bitcoin piyasanın büyüğü olarak yüksek bir ağırlığa sahip. 

| ![BTC_dominance](/assets/bitcoin_dominance_v2_800.png)|
|:--:| 
| *Bitcoin'in kripto dünyasındaki ağırlığı - şu ara %60 seviyesinde.  Kaynak: [TradingView](https://www.tradingview.com/symbols/CRYPTOCAP-BTC.D/)*|

Dolayısıyla piyasadaki bütün kripto paralar ağırlıklı olarak Bitcoin ile ortak hareket ediyorlar. Yani, Bitcoin artarsa artıyorlar, azalırsa azalıyorlar (genellikle bu artış ve azalışları daha uç noktalarda yaşıyorlar). Ampleforth yaratıcıları, paralarının ilk çıkış aşamasında öyle hemen stabil bir hâle gelmesini beklemiyorlar. Bunun yerine yarattıkları strateji sayesinde AMPL değerindeki değişimlerin diğer bütün kripto paralardan farklı şekilde yol alacağının bunun da portföy yöneticilerine riski çeşitlendirerek azaltmak konusunda bir opsiyon sunacağını düşünüyorlar. 

Değeri kendinden menkul paraların son 90 gün içindeki değer artış/azalış ilişkisini gösteren aşağıdaki tabloya bakıldığında bu düşüncelerinde çok da haksız sayılmazlar: 

| ![AMPL_chart](/assets/AMPL_correlation_800_v2.png)|
|:--:| 
| *Değişik kripto paraların fiyat ilişkileri. 1 değeri birbiri ile aynı hareket eden paraları, 0 değeri ilgisiz, -1 değeri ise ters hareket eden paraları gösterir. Kaynak: [Ampleforth](https://www.ampleforth.org/dashboard)*|

İkinci aşamada ise AMPL fiyatındaki başta yaşanan dalgalanmanın zaman geçtikçe azalması sonrası AMPL'nin artık bir rezerv para olarak kullanılabilmesini yaygınlaşması var. AMPL özünde Tether ya da DAI gibi itibari bir paraya bağlı bir para değil - Bitcoin, Ethereum benzeri kıymeti kendinden menkul ve bağımsız, sansürlenemez bir para. Bir yandan da itibari paraların merkez bankalarının hadsiz hudutsuz para basmalarından dolayı ciddi değer kaybetmeleri ve rezerv para fonksiyonlarının ortadan kalkmasını bekleyenler var. Dolayısıyla, rezerv para olarak sansüre uğramayacak tam anlamıyla kullanıcıların sahip olabileceği değeri büyük dalgalanmalar göstermeyen bir rezerv para olma hedefleri var. 

Rezerv para ile kastedilen şu. Daha önceki bir yazımızda MakerDAO sistemi ile merkeziyetsiz olarak kişilerin kendilerine kredi yaratmasını anlatmıştık. Hatırlarsanız basitçe şöyle idi: Kişi sahip olduğu ETH'leri getirip teminat olarak veriyor, karşılığında DAI isimli ABD Doları'na çapalanmış bir stabil para yaratıyor yani borç alıyor. Ancak kredilerde en büyük sorun karşı parti riski - teminat da bunun için alınıyor, ya borç alan borcunu ödemez ise. Ancak teminat alınan ETH kendisi çok inişli çıkışlı bir para, kredi olarak alınan DAI ise gayet stabil bir para olduğu için, sistem riski azaltmak adına %150 oranında teminat istiyordu. 100 birim DAI alacaksanız 150 birime denk gelecek kadar ETH koymalısınız. Tekrar edelim, bu kadar yüksek bir teminat istenmesinin nedeni ETH'nin fiyatının yarın öbür gün ciddi değer kaybetmesi. Peki ya bunun yerine değerini aşağı yukarı koruyan bir para teminat olarak verilebilseydi? O zaman bu kadar yüksek bir teminat vermek, yani borç alan bu kadar yüksek bir teminatı sisteme kilitlemek zorunda kalmazdı. İşte Ampleforth, AMPL'yi ETH ya da Bitcoin gibi değeri kendinden menkul ama sabit bir para olarak DeFi yani merkeziyetsiz sistemlerde rezerv para olarak kullandırmayı hedefliyor. 

AMPL'nin son üç aylık toplam değer, arz ve AMPL fiyat hareketlerine baktığımızda ise, volatilitenin azalması alanında daha almaları gereken çok yol olduğu kesin: 

| ![AMPL_volatility](/assets/ampleforth_price_supply_mcap_v2_1200.png)|
|:--:| 
| *Ampleforth sistem değeri (mavi çizgi), toplam AMPL miktarı (kırmızı çizgi) ve AMPL fiyat hareketi (yeşil çizgi). Aşağıda görünen üç kesik çizgi AMPL tokenin sistem tarafından izin verilen hedef 1 ABD Doları çevresindeki alt ve üst bandlarını gösteriyor. Kaynak: [Ampleforth](https://www.ampleforth.org/dashboard)*|


Bu arada şunu da hemen belirtelim. Bir DeFi projesi olarak Ampleforth şu aşamada bu alanın en yaygın kullanılan ağı olan Ethereum'u kullanıyor - yani AMPL özünde ERC 20 standardı ile çalışan bir token. Yarın öbür gün, aynı Tether örneğinde olduğu gibi AMPL'nin başka Blockchain altyapılarında da yer almasının önünde herhangi bir engel yok. AMPL kendini Blockchain bağımsız bir ürün olarak konumlandırıyor. Mevcut para politikası ve havuzunun içinde yer aldığı sürece her tür Blockchain içinde token çıkarabilir.  

Üçüncü aşamada ise kullanımın yaygınlaşması ve arzın artması ile birlikte artık geniş kitleler tarafından ödemeler için kullanılabilecek güvenli, bağımsız bir para olma hedefi var. Yani aslında bir nevi Satoshi'nin Bitcoin'e başlangıçta koyduğu vizyona ulaşmak. Uzun vadede yeterli büyüklüğe ulaşıldığında volatilitenin azalması ile birlikte paraya olan talebin ancak büyük makro ekonomik değişiklikler olması durumunda değişiklik göstereceğini, bunun da şimdiki gibi sık olmasa da yapılacak arz değişiklikleri ile yatırımcılara yansıtılacağını düşünüyorlar.  

Geniş kitlelere yayılmasında teknik olarak belli engeller de olabilir bu arada. Özellikle merkezi borsalarda işlem görmek yaygınlaşma için önemli. Ancak böyle bir durumda, müşteri cüzdanlarının merkezi borsalarda nasıl işleneceği teknik bir sorun olabilir gibi görünüyor - özellikle de kullanıcıların verdikleri emirler gerçekleşmeden önce yapılan para arzı artışı ya da kısıtlamaların müşteri cüzdanlarına nasıl yansıtılacağı konusunda. 

### Sonuç

Ampleforth, Bitcoin sonrası ortaya çıkan kripto dünyasının geniş kitlelere yayılabilmesi için ortaya konan deneysel çözümlerden makro ekonomik para politikalarına odaklanan bir tanesi. Ekonomide teori olarak ortaya konan kavramların gerçek hayatta nasıl gelişeceğini göstermesi açısından ilginç bir deney. Nasıl gelişeceği, ne kadar yaygınlaşacağı, çıkan sorunlara nasıl adapte olacağı ve bir gün Bitcoin'e rakip olup olmayacağını ise bize önümüzdeki yıllar gösterecek. Hep dediğimiz gibi, bu heyecanlı sonu merakla bekliyoruz. 

---

*Not 1: Bu yazı ilk olarak 6 Ekim 2020'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/defida-ilginc-bir-para-politikasi-deneyi-ampleforth/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

---
