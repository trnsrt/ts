Bugün sizlere geçtiğimiz aylarda ilk çıktığında büyük sükse yapan, sonrasında ardına ardına gelen yeni girişimlerin de etkisiyle ana sahneden uzaklaşan ilginç bir DeFi projesinden bahsedelim. 

Gözden ırak olan gönülden de ırak olmaz mı? Neden zaman ayırıp bakalım? Çünkü kripto dünyası şu anda emekleme aşamasında. İçinde o kadar farklı ve ilginç dinamikler ve değişkenler taşıyor ki bunların her biri ile oynarak pek çok farklı deney yapılabiliyor. Çıkan her proje yaşanmakta olan bir derde deva olabildiği kadar beraberinde başka sorunlar getirebiliyor, ya da kullanıcılarda yeni ihtiyaçlar ortaya çıkarabiliyor. Ampleforth da benzer şekilde mevcut bir soruna merkeziyetsiz bir çözüm getirmek hedefiyle ortaya çıkmış bir proje. Gelin bakalım neymiş:

### Nedir Ampleforth?

Ampleforth bir deney - nihai hedefi alışverişte kullanılabilecek kadar stabil ancak Bitcoin benzeri değeri kendinden menkul bir para olmak. Ve bunu yaparken de hem stabil paraların hem de Bitcoin'in zayıf yanlarını güçlendirecek çözümler getirmek. Önce bu sıkıntılara bir göz atalım:  

#### Stabil paraların sıkıntısı
Piyasada yeterince stabil kripto para varken neden Ampleforth'a ihtiyaç olsun? Çünkü stabil paralar özünde bir itibari paraya bağlılar (itibari paranın devletlerin merkez bankaları tarafından basılan ABD Doları, Euro benzeri paralar olduğunu tekrar hatırlatalım). Bu itibari paralar görünüşte değerlerini koruyor gibi görünseler de aslında uzun vadede sürekli değer kaybı yaşıyorlar. Amerika Birleşik Devletleri altını 1933 yılında onsu [20 ABD Doları'ndan halktan toplamıştı](https://en.wikipedia.org/wiki/Executive_Order_6102) (enflasyon etkisini yedirseniz bile günümüzde 408 ABD Doları'na geliyor), şu anda altın 2,000 ABD doları seviyelerinde. Şimdi ABD Dolarının değerinin sabit kaldığını söyleyebilir misiniz? 

| ![BTC_dominance](/assets/Executive_Order_6102_640.jpg)|
|:--:| 
| *ABD hükümetinin halktan zorla altın topladığı meşhur 6102 sayılı emir.  Kaynak: [Wikipedia](https://https://en.wikipedia.org/wiki/Executive_Order_6102)*|

Ayrıca  bu stabil kripto paralar ödemeler konusunda çözüm olsalar da, bu paraları basanların ağırlıklı bir kısmının merkezi yapılar olması beraberinde yeni sorunlar getiriyor. Yakın zamanda yaşadığımız Tether'in müşteri hesaplarını dondurabilme gücü (ki yakın zamanda yaşanan Kucoin hack'inde [33 milyon ABD Doları bir miktar için bunu yaptılar](https://en.ethereumworldnews.com/bitfinex-and-tether-freeze-33m-usdt-from-kucoin-hack/)) kripto dünyasının bireylere en büyük faydası olarak da bilinen "dijital varlığa tamamıyle sahip olma" özelliğinin nasıl delik deşik edildiğinin de bir göstergesi aslında. 

#### Bitcoin'in sıkıntısı
Bitcoin benzeri sınırlı arza sahip paralar teori olarak güzel: Değer anlamında hiçbir kuruma bağlı olmayan, tamamıyle bağımsız, sansüre karşı dayanıklı ve sınırlı arzı ile değerini teorik olarak koruması gereken bir para. Ancak bu sınırlı miktardaki arz, artıp azalan talep ile bir araya geldiğinde ortaya son derece oynak bir para çıkıyor. Her ne kadar uzun vadede son on yılda yaşanan fiyat artışının en önemli nedenlerinden birinin bu kısıtlı arz olduğu düşünülse de kısa vadelerde oluşan oynaklık sinirleri zorlayacak seviyede. 

**İşte Ampleforth, bir yandan Bitcoin gibi uzun vadede yatırımcısına değeri artacak bir varlık sunarken, diğer yandan stabil paralar gibi kısa vadede değeri değişmeyen ve bu sayede alışverişlerde kullanılabilecek bir para yaratma hedefinde.** Peki nasıl olacak bu bir taşla iki kuş vurma? Anlatalım: 

### Nasıl çalışıyor Ampleforth?

Ampleforth, fiyat tarafında görülen oynaklığı önlemek adına, talepte meydana gelebilecek değişimlerin fiyata radikal etki etmesinin önüne geçmek yani paranın değerini dengelemek için paranın arzının değişirilmesi prensibine dayanıyor. Hem de ne değiştirmek! Gelin biraz daha açalım bunu: 

Ampleforth otomatik olarak çalışan bir algoritma - insan eli değmiyor, "kod kanun" bir başka deyişle. **Algoritmanın tek bir hedefi var: O da sistemin parası AMPL'yi sabit bir değerde tutmak.** Bu değer 2019 yılındaki 1 ABD Dolarına eşitlenmiş. Şu an için enflasyon giydirilmiş olarak 1.019 ABD Doları seviyesinde. 

Bir sistemin parasını sabit tutup nasıl yatırımcıların ilgisini çekebilirsiniz? İşte burada yatırım ile ilgili kafamızdaki klasik kalıpları yeniden gözden geçirmekte fayda var:

Bir yatırım yaptığımızda elimizdeki varlığın değeri, toplam yatırım içindeki payımızın (buna hisse ya da token diyelim), her bir payın değeri ile çarpılması ile ortaya çıkar. Genelde yatırım içindeki payımız sabit olduğu için varlığımızın değerinin artıp azalışını hisse değerindeki hareketlerden çıkarırız (bir an için alım ya da satım yapmadığımızı varsayalım) . Bir nevi hissenin değeri bizim varlığımızın değerini bulmamızda bize 'kısa yol' olur. 

Ama Ampleforth, her bir payın (yani tokenin) değerini sabit tutmak istiyor. Nasıl olacak o zaman? Diyelim bir anda varlığa bir talep oldu, insanlar deli gibi AMPL almaya başladılar. Fiyat nasıl aynı kalacak? Kalmalı mı? Token değerini sabit tutmak ile varlığın değerini artırmak birbiri ile çelişiyor mu? İşte burada, yukarıdaki paragraftaki önyargımızı bir kenara bırakalım. Bakmamız gereken tüm sistem ve bizim onun içindeki payımızın değeri. Hissenin değeri değil. Peki nasıl olacak bu? Toplam değerin iki çarpanı var demiştik. Pay adedi ve her bir payın değeri. Eğer tüm sistemin değeri değişecek ise ve payın değerini artırmak istemiyorsak o zaman pay adedini artırırız!

Ezberlerimizi yeterince bozduk mu? :) 

Sistemin nasıl çalışacağını gelin bir de örnek üzerinden anlatalım: 

#### AMPL token fiyat yükselirse ne oluyor?

Varsayalım, 1 AMPL 1 ABD Dolarına eşit ve yatırımcımızın da 100 AMPL'si var, yani 100 ABD Dolarına eş bir varlık. Bir anda piyasalarda AMPL'ye talep oldu ve AMPL fiyatı 1.5 AMPL'ye çıktı. İşte o zaman algoritma otomatik olarak devreye giriyor ve her bir AMPL karşılığı yatırımcılara 0.5 AMPL daha veriyor. Yatırımcımızın artık 150 AMPL'si var.  

Buraya kadar herşey otomatik el değmeden çalıştı. Bundan sonrasında sistem, piyasanın davranışsal davranacağını düşünüyor. Başta ne demiştik, sistemin hedefi AMPL'nin 1 ABD Doları'na geri dönmesi. Bu hareketin arkasında yatan düşünce şu: Eğer bir anda insanların elindeki varlık, 1 ABD Doları iken, fiyat artışından dolayı 1.5 ABD Doları'na, sonrasında AMPL artışından dolayı 1.5 AMP x 1.5 AMPL = 2.25 ABD Doları'na çıkarsa, insanlar, özellikle al-sat yapanlar, kârı realize etmek için ellerindeki AMPL'yi satarlar. Nereye kadar, fiyat tekrar 1 AMPL'ye dönene kadar. 

Böyle olunca ne oldu? Hızlı hareket eden al-satçılar ciddi bir para kazandılar. Sistemin buna bir itirazı yok - zira sistemin istediği AMPL fiyatının tekrar 1 ABD Doları'na dönmesi. Peki alım satım yapmayıp ellerinde tutanlar? Onlar da aslında ekstra bir kar/zarar etmediler. Yukarıdaki yatırımcımızın başlangıçtaki varlığı 100 dolar idi, sonra sistem onlara AMPL verdiği için ellerinde 150 AMPL oldu ve ilk anda 225 ABD Dolarına eşitti ancak fiyat tekrar 1 ABD Dolar seviyesine geldiğinde son durumda varlığı 150 ABD Doları'na çıktı. Yani ilk fiyat artışında olduğu gibi %50 kazancını cebine koymuş oldu. 

Aslına bakarsanız, AMPL sisteminin yapmaya çalıştığı, paranın arzını artırarak yatırımcılar üzerindeki etkiyi büyütmek ve onların daha hızlı reaksiyon vermesini sağlamak. Biraz açalım bu dediğimizi: Diyelim aldığınız bir tokenda %60 kazanç beklentiniz var, eğer token size %60 kazandırırsa yeterli olduğunu düşünüp satacaksınız. Yukarıdaki senaryoda eğer para arzı sabit kalsa idi, fiyat %50 arttığından dolayı satmayacaktınız. Ama elinizdeki tokenların sayısı da artınca toplam kazancınız bir anda %125'e çıktı, hemen harekete geçip satmaz mısınız? Sizin gibi satmaya başlayanlar olacaktır, bunun sonucu token fiyatı düşmeye başlar ama hâlâ kazanç yüksek olduğu için bekletinizin gerçekleşeği rakama kadar satamaya devam edersiniz. İşte böyle böyle düşen token fiyatı sistemi hedeflediği noktaya kadar getirir. 

Bir başka bakış açısından, **sistem kendi içinde talebin değişmesinden dolayı oluşabilecek fiyat hareketlerindeki volatilite yükünü, arzı değiştirerek fiyattan yani sistemden alıp, yatırımcıya geçiriyor**. Bir önceki paragrafı tekrar edelim: Arzı değiştiriyor, dolayısıyla yatırımcılar hisse fiyatındaki değişimin daha da fazlasını varlıklarındaki değişimlerde hissedip daha hızlı bir şekilde aksiyon alıyorlar, bu da hisse fiyatını eski haline döndürüyor. 

### Peki ya fiyat düşerse?

Tabii bir de madalyonun öbür yüzü var. Ya, talepte bir azalma olur ve token değeri bir anda düşerse? Diyelim, bir hareket ile hisse değeri %50 değer kaybetti ve 1 AMPL 0.5 ABD Doları'na eşit hale geldi. 

İşte orada da sistem tam tersi çalışıyor. Yatırımcıların cüzdanlarındaki AMPL'lerin yarısını ellerinden alıyor! Yok artık! Evet, aynen öyle. Niye? Aslında mantık yukarıda anlattığımızın aynısı. Sistem şöyle düşünüyor: "Ampleforth'un toplam sistem değeri düşüyor - olabilir ama bu beni ilgilendirmiyor. Beni ilgilendiren 1 AMPL'nin tekrar 1 ABD Doları'na denk hale gelmesi. İnsanlar satıyor AMPL'leri, demek ki piyasada AMPL bolluğu var. Ben bu AMPL'leri piyasadan çekersem hem arz azalmış olacak, hem de AMPL sistem değeri düştüğü için ucuzlamış olacak. Bunu gören yatırımcılar nasıl hisse değeri düştüğünde o hisseyi almaya çalışıyorlarsa burada da AMPL sistem değeri kat be kat düştüğü için almaya koşacaklar. 

Yukarıdaki örnekten devam edersek. Başlangıçta 100 ABD Dolarına eş 100 AMPL vardı elinizde. Token değer kaybedince varlığınız önce 100 AMPL x 0.5 cent = 50 ABD Doları seviyesine düştü. Sonra bir de sistem elinizdeki AMPL'lerin yarısını aldı, dolayısıyla varlığınız bir anda geçici olarak 50 AMPL x 0.5 cent = 25 ABD Doları'na geriledi. Sizin sistem içindeki payınız hiç değişmedi. AMPL sistemi değer kaybetti. AMPL kendi içinde %50 değer kaybetti ancak tüm sistem %75 değer kaybetmiş oldu. Bu kadar ucuzlamış bir sistemi almak için üşüşen yatırımcılardan dolayı AMPL tekrar değer kazandı, nereye kadar? Dengenin oturacağı 1 AMPL = 1 ABD Doları seviyesine kadar. O zaman son durumda varlığınız ne oldu? 50 AMPL x 1 ABD Doları = 50 ABD Doları.  Varlığınız değer kaybetti mi? Gayet tabii - zira talep azaldığı için zaten başta kaybetmiştiniz onu. Geçici olarak arz kısılmasından dolayı daha da kaybettiniz ama en sonunda %50 kaybettiğiniz ilk noktaya döndünüz. 

#### Fiyat konusundaki bu ısrar neden?

Hisse (ya da token) fiyatını sabit tutmak neden önemli? Bir paranın alım satım ve ticaret için kullanımı ancak değerinin "gerçek" anlamda sabit olması durumunda gerçekleşebilir. Öte yandan yatırımcılar tarafından bu paranın rağbet görmesi için varlığın değerinin artması gerekir. İşte Ampleforth, sabit değerli bir para yaratarak alışverişlerde güvenle kullanılabilecek bir para yarattıktan sonra, bu paranın rağbet görmesi durumunda yatırımcısına da değer kazandıracak bir enstrümana dönüşmesini sağlıyor. Sabit paralardan en büyük farkı bu: Kullanan için sabit para, yatırımcısı için eğer kabul görüp yaygınlaşır ise değer kazandırıcı bir enstrüman. 

### Ampleforth'un vizyonu

Ampleforth'un arzı ile oynamak suretiyle üçlü aşamalı bir vizyonu var aslında: 

İlk aşama kısa vadede portföyünde kripto varlık tutanlara risklerini dağıtmaya yardımcı olmak. Çıkış noktaları şu: Bitcoin piyasanın büyüğü olarak büyük bir ağırlığa sahip. 

| ![BTC_dominance](/assets/bitcoin_dominance_v2_800.png)|
|:--:| 
| *Bitcoin'in kripto dünyasındaki ağırlığı - şu ara %60 seviyesinde.  Kaynak: [TradingView](https://www.tradingview.com/symbols/CRYPTOCAP-BTC.D/)*|

Dolayısıyla piyasadaki bütün kripto paralar ağırlıklı olarak Bitcoin ile ortak hareket ediyorlar. Yani, Bitcoin artarsa artıyorlar, azalırsa azalıyorlar (genellikle bu artış ve azalışları daha uç noktalarda yaşıyorlar). Ampleforth yaratıcıları, paralarının ilk çıkış aşamasında öyle hemen stabil bir hâle gelmesini beklemiyorlar. Bunun yerine yarattıkları strateji sayesinde AMPL değerindeki değişimlerin diğer bütün kripto paralardan farklı şekilde yol alacağının bunun da poftföy yöneticilerine riski çeşitlendirerek azaltmak konusunda bir opsiyon sunacağını düşünüyorlar. 

Değeri kendinden menkul paraların son 90 gün içindeki değer artış/azalış ilişkisini gösteren aşağıdaki tabloya bakıldığında bu düşüncelerinde çok da haksız sayılmazlar: 

| ![AMPL_chart](/assets/AMPL_correlation_800_v2.png)|
|:--:| 
| *Değişik kripto paraların fiyat ilişkileri. 1 değeri birbiri ile aynı hareket eden paraları, 0 değeri ilgisiz, -1 değeri ise ters hareket eden paraları gösterir. Kaynak: [Ampleforth](https://www.ampleforth.org/dashboard)*|

İkinci aşamada ise AMPL fiyatındaki başta yaşanan volatilitenin zaman geçtikçe azalması sonrası AMPL'nin artık bir rezerv para olarak kullanılabilmesini yaygınlaşması var. AMPL özünde Tether ya da DAI gibi itibari bir paraya bağlı bir para değil - Bitcoin, Ethereum benzeri kıymeti kendinden menkul ve bağımsız, sansürlenemez bir para. Bir yandan da itibari paraların merkez bankalarının hadsiz hudutsuz para basmalarından dolayı ciddi değer kaybetmeleri ve rezerv para fonksiyonlarının ortadan kalkmasını bekleyenler var. Dolayısıyla, rezerv para olarak sansüre uğramayacak tam anlamıyla kullanıcıların sahip olabileceği değeri büyük dalgalanmalar göstermeyen bir rezerv para olma hedefleri var. 

Rezerv para ile kastedilen şu. Daha önceki bir yazımızda MakerDAO sistemi ile merkeziyetsiz olarak kişilerin kendilerine kredi yaratmasını anlatmıştık. Hatırlarsanız basitçe şöyle idi: Kişi sahip olduğu ETH'leri getirip teminat olarak veriyor, karşılığında DAI isimli ABD Doları'na çapalanmış bir stabil para yaratıyor yani borç alıyor. Ancak kredilerde en büyük sorun karşı parti riski - teminat da bunun için alınıyor, ya borç alan borcunu ödemez ise. Ancak teminat alınan ETH kendisi çok inişli çıkışlı bir para, kredi olarak alınan DAI ise gayet stabil bir para olduğu için, sistem riski azaltmak adına %150 oranında teminat istiyordu. 100 birim DAI alacaksanız 150 birime denk gelecek kadar ETH koymalısınız. Tekrar edelim, bu kadar yüksek bir teminat istenmesinin nedeni ETH'nin fiyatının yarın öbür gün ciddi değer kaybetmesi. Peki ya bunun yerine değerini aşağı yukarı koruyan bir para teminat olarak verilebilseydi? O zaman bu kadar yüksek bir teminat vermek, yani borç alan bu kadar yüksek bir teminatı sisteme kilitlemek zorunda kalmazdı. İşte Ampleforth, AMPL'yi ETH ya da Bitcoin gibi değeri kendinden menkul ama sabit bir para olarak DeFi yani merkeziyetsiz sistemlerde rezerv para olarak kullandırmayı hedefliyor. 

Bu arada şunu da hemen belirtelim. Bir DeFi projesi olarak Ampleforth şu aşamada bu alanın en yaygın kullanılan ağı olan Ethereum'u kullanıyor - yani AMPL özünde ERC 20 standardı ile çalışan bir token. Yarın öbür gün, aynı Tether örneğinde olduğu gibi AMPL'nin başka Blockchain altyapılarında da yer almasının önünde herhangi bir engel yok. AMPL kendini Blockchain bağımsız bir ürün olarak konumlandırıyor. Mevcut para politikası ve havuzunun içinde yer aldığı sürece her tür Blockchain içinde token çıkarabilir.  

Üçüncü aşamada ise kullanımın yaygınlaşması ve arzın artması ile birlikte artık geniş kitleler tarafından ödemeler için kullanılabilecek güvenli, bağımsız bir para olma hedefi var. Yani aslında bir nevi Satoshi'nin Bitcoin'e başlangıçta koyduğu vizyona ulaşmak. Uzun vadede yeterli büyüklüğe ulaşıldığında volatilitenin azalması ile birlikte paraya olan talebin ancak büyük makro ekonomik değişiklikler olması durumunda değişiklik göstereceğini, bunun da şimdiki gibi sık olmasa da yapılacak arz değişiklikleri ile yatırımcılara yansıtılacağını düşünüyorlar.  

Geniş kitlelere yayılmasında teknik olarak belli engeller de olabilir bu arada. Özellikle merkezi borsalarda işlem görmek yaygınlaşma için önemli. Ancak böyle bir durumda, müşteri cüzdanlarının merkezi borsalarda nasıl işleneceği teknik bir sorun olabilir gibi görünüyor - özellikle de kullanıcıların verdikleri emirler gerçekleşmeden önce yapılan para arzı artışı ya da kısıtlamaların müşteri cüzdanlarına nasıl yansıtılacağı konusunda. 

### SONUC

Ampleforth, Bitcoin sonrası ortaya çıkan kripto dünyasının geniş kitlelere yayılabilmesi için ortaya konan deneysel çözümlerden makro ekonomik para politikalarına odaklanan bir tanesi. Ekonomide teori olarak ortaya konan kavramların gerçek hayatta nasıl gelişeceğini göstermesi açısından ilginç bir deney. Nasıl gelişeceği, ne kadar yaygınlaşacağı, çıkan sorunlara nasıl adapte olacağı ve bir gün Bitcoin'e rakip olup olmayacağını ise bize önümüzdeki yıllar gösterecek. Hep dediğimiz gibi, bu heyecanlı bekleyişin sonunu hep birlikte göreceğiz. 


---

### Bitcoin'in sıkıntısı

Kripto dünyasında bugüne kadar kendini kanıtlama anlamında en ileriye gitmiş proje Bitcoin. On yılı aşkın bir süredir tıkır tıkır çalışıyor. Durdurmayı ya da sekteye uğratmayı başaran olmadı. Sıkıntıları yok mu var tabii. 

Bitcoin ile ilgili pek çok sıkıntı sayabiliriz aslında - kişiden kişiye de değişir bu sıkıntıların neler olduğu. Teknolojik olarak yavaş evrilmesi (ki bunu bir sorun değil "gerekli bir özellik" olduğunu savunanlar da var), basitliği nedeniyle üzerine kurulacak yeni yapılara çok uygun olmaması genelde şikayetlerin başında gelir. 

Teknolojik olarak yavaş evrilmesine verilen en kritik örneklerden biri kişiden kişiye ödemelerde çok da yaygınlık kazanamamış olması. Hem de Bitcoin'in tanıtım dokümanı (white paper) başlığının "[Bitcoin - Eşten-eşe Elektronik Nakit Sistemi](https://bitcoin.org/bitcoin.pdf)" olmasına rağmen. İşte bu nedenle Bitcoin savunucularının son yıllardaki argümanları daha çok onun bir Dijital Altın olduğu ve ödeme işlemlerinden ziyade değer saklama aracı olarak görülmesi gerektiğine evrilmiş durumda. 

Bitcoin sorunları çözmek amacıyla sonrasında pek çok klonu çıktı. Sayı olarak [100'ün üzerinde]()https://atomicwallet.io/how-many-bitcoins-are-there. Aslında bunda şaşıracak bir durum da yok, zira açık kaynak bir uygulama olduğunuzda isteyen herkes oturup bir klonunu yaratabilir. Çok basit. Asıl zor olan, sisteminize inanmış bir topluluk yaratabilmek. İşte en başarılı Bitcoin klonunun bile (ki muhtemelen Bitcoin Cash'dir bu) en sıkıntı yaşadığı konu hep bu oldu. 

Bitcoin klonları da genellikle bu ödeme özelliği perspektifinden rekabet etmeye çalışıyorlar. Ödeme konusunda Bitcoin'in neden yaygınlaşmadığına ilişkin teşhis ve tedavi yöntemleri de aslında bu klonların kendilerini farklılaştırma stratejilerinde ortaya çıkıyor. Litecoin örneğinde olduğu gibi her 10 dakikada bir uzlaşma yapmak yerine 2.5 dakikada bir yapmak, böylece işlemlerin teyidini hızlandırmak bunlardan biri. Ya da Bitcoin Cash örneğinde olduğu gibi Keza uzlaşma yapılan blok büyüklüğünü artırmak böylece yoğun işlem zamanlarında blokların dolmasında ötürü oluşacak gecikmeleri önlemek bir diğeri. Ve nihayet, Lightning Network gibi Bitcoin üzerine kurulu ikinci seviye çözümler ile blok zincirini daha az kullanarak maliyetleri azaltmak ve ufak ödemeler (örneğin kahve almak gibi) için kullanışlı hâle getirmek bir başkası çözüm örneği. 

Bunlar işin teknoloji yönünden getirilmeye çalışılan yenilikler. Kabul etmemiz gereken bir gerçek var, o da Bitcoin'in genel olarak gündelik hayatımıza girememesinin en önemli nedenlerinden biri aslında fiyat olarak çok dalgalı olması. Bu dalgalanmalar kayıp ve kazanç anlamında riskleri de beraberinde getirdiği için Bitcoin'i alışveriş aracı olarak kullanmak imkansız. Zira alışverişte ihtiyaç duyulan adil ve değeri değişmeyen bir aracı kullanmak - ki tarafların kafası rahat olsun, asıl işlerine odaklanabilsinler. 

İşte bu dalgalanma sorununu çözebilmek amacıyla itibari paralara çapalanmış stabil paralar çıkarıldı ve büyük de ilgi gördü. Ancak bu paraları çıkaranların ağırlıklı bir kısmının merkezi yapılar olması, ödemeler konusunda sorun çözse de merkezilik nedeniyle yeni sorunlar çıkardı. Yakın zamanda yaşadığımız Tether'in yapılmış işlemleri geçersiz hale getirebilme gücü (ki yakın zamanda gerçekleşen Kucoin hack'inde bunu yaptılar) kripto dünyasının bireylere en büyük faydası olarak da bilinen "dijital varlığa tamamıyle sahip olma" özelliğinin nasıl delik deşik edildiğinin de bir göstergesi aslında. 

İşte bu nedenle, Bitcoin benzeri bağımsız, sansürsüz ama bir yandan da fiyat volatilitesi daha düşük kripto paralara bir ihtiyaç var gibi görünüyor. İşte Ampleforth bu sorunu çözmeye odaklanmış bir kripto para. 

-- 

#### Bu sistemde kimler kazanıyor, kimler kaybediyor?
Sistemin şu aşamada henüz birinci aşamasındayız. Bu birinci aşama fiyatların henüz tam olarak oturmadığı bir zaman dilimi. Bu da spekülatif hareketlerden dolayı kazanç sağlanabildiği anlamına geliyor. Zaten sistem, fiyatların oturabimesi için fiyat artış ya da azalışlarında sistemdeki dengesizlik üzerine işlem yapıp kar sağlayacak spekülatörlerin desteğine ihtiyaç duyuyor. Burada da hız çok önemli. Ampleforth sistemi için yalnızca fiyat hareketine bakmak yetmiyor. Bunun yanında para arzının ne yöne gittiğini ve toplam sistem büyüklüğünü de iyi kestirmek gerekiyor. Yalnızca kestirmek değil aynı zamanda hızlı hareket edebilmek. Dolayısıyla, sistemi iyi bilen ve al-sat konusunda uzmanlaşmış olanların kar etme olasılığı daha yüksek.  Öte yandan, sistemin doğru çalışacağına inananlar için eğer Bitcoin'de olduğu gibi herhangi bir işlem yapmayıp tokenlarını ellerinden tutmaları durumunda, eğer beklentilerine uygun olarak AMPL sisteminin toplam değeri yükselir ise kar etme olasılıkları da aynı şekilde yükseliyor. Peki o zaman kim kaybediyor bu sistemde? Daha çok, ani fiyat hareketlerini tam olarak izleyemeyen işlem yapan ama geç kalanlar denebilir. 

-- 


Ampleforth'un paranın arzını değiştiriyor. "Peki, ortaya çıkan paranın arzını azaltan ya da artıran pekçok farklı parasal politikaya  sahip kripto para var zaten, ne var ki bunda?" Ancak kazın ayağı öyle değil. Ampleforth'da bu değişen arz yalnızca yeni olarak piyasaya sürülecek olan paralara yönelik değil. Akıllı kontratlar marifetiyle, sizin cüzdanınızdaki paranın miktarını da değiştiriyorlar!

“Eyvah, cüzdanımdan paramı mı alıyor?” Evet aynen öyle. Panik yapmalı mısınız? Şöyle düşünün, eğer sistem teoriye uygun olarak işler ise, sistemin toplam değerinin % kaçı sizin elinizde ise bu hiçbir zaman değişmiyor. Yani eğer sistemin parasal büyüklüğünün binde biri cüzdanınızda ise, sistem herkesten eşit oranda kesim yapacağı için, paranız azalıyor ama sistemin yine binde birine sahip oluyorsunuz. 

Aslında bu durumun Bitcoin’den bir farkı yok. Bitcoin maksimalistlerinin bir deyişi vardır. Fiyat sorulduğunda “1 Bitcoin = 1 Bitcoin, dün de böyleydi, bugün de böyle” derler. Örnek olarak 21 Bitcoin’ininiz var ise (keşke dediğinizi duyar gibiyim) fiyat ne olursa olsun, bugünde toplam sistemin milyonda birine sahipsiniz, yarın da. 

Peki fiyatın tekrar dengeye geleceğini nereden biliyoruz? İşte burada sistem piyasada al-sat yapan ve kar peşinde koşanların rasyonel hareket edeceği mantığına dayanıyor. Sistemi işleyişini tetikleyen marketteki talep.  Marketteki arzın artması ya da azalması sonucu paranın kurunun değişiyor, kur değişimi para arzı hareketini tetikliyor, bu para arzı hareketi sonrası ise paranın kurunun eski haline gelmesi bekleniyor.

Ampleforth'da amaç paranın değerini belli bir seviyede tutmak. Seviye derken kastedilen, değerini belli bir hedefin %5 altı ya da üstündeki bir bantta hareket ediyor olması. Hedef 2019 yılındaki 1 ABD Doları bazının enflasyon ile artırılması ile Ekim 2020 tarihi için 1.019 ABD Doları seviyesinde. 

Eğer hedef değer bu bandın dışına çıkarsa o zaman Akıllı Kontrat devreye giriyor. Peki ne yapıyor bu kontrat? Diyelim talebin artması sonucu değer bir anda arttı ve 1 ABD Doları olan Ampleforth parası AMPL 2 Doları seviyesine geldi. Sizin elinizde 10 AMPL var ise bu paraların değeri de 10 ABD Dolarından 20 ABD Dolarına çıktı. Sistem sizin elinizde olan AMPL miktarını kademeli olarak iki katına çıkarıyor. Dikkat edin, elinizdeki parayı almıyor, tam tersine artırıyor. 

Burada umulan, para miktarının bir anda iki katına çıkması ile birlikte değerin tekrar 1 dolar seviyesine düşmesi ve sizin elinizde yine 20 ABD Doları değerinde bir varlık olması. Yani fiyat artışının varlığınızdaki değer artışı etkisi korunurken paranın değerinin aynı seviyede kalması. Bunu yapan kontratın ise tamamen dış manuel etki olmadan yazılı tarafından otomatik gerçekleştirildiğine de belirtelim. Nasıl, ilginç değil mi?

Peki nasıl olacak da fiyat tekrar 1 dolar seviyesine düşecek? Buradaki düşünce, fiyatın ve elindeki token miktarı artan spekülatörlerin, kâr realizasyonu amacıyla satış yapmaları, bunun da AMPL fiyatına düşürücü bir etkisi olması. 

Tabii yukarıdaki senaryodaki kritik nokta arzın iki katına çıkması durumunda paranın eski sabit değerine düşeceği argümanı. Teorik olarak öyle olmalı, ancak pratikte öyle mi?... 

Bir de madalyonun öbür yüzü var. Eğer bir olay oldu da AMPL değeri 50 cent'e indi ise o zaman elinizdeki 10 AMPL'nin yarısı "uçuyor" ve sizde 5 AMPL kalıyor. Beklenen fiyatın bir anda 1 ABD Doları seviyesine çıkarak varlığınızın değerinin 5 ABD Doları kalması. Ama böyle bir senaryoda eğer fiyat 1 ABD Doları'na çıkmaz ise, varlığınız 10 ABD Doları'ndan 5 ABD Dolarına inmiyor, 2.5 ABD Dolarına iniyor. İşte bir anda içimize düşen kuşku:

#### Ya bir girdabın içinde fiyat düşmeye devam ederse?
Arz azalımı ancak fiyat belli bir seviyenin altına düştüğü zaman gerçekleşiyor. O zaman akla ilk gelen soru: Ya arz azalımından dolayı fiyat azalırsa ve fiyat geri yükselmez ise, fiyat yükselmediği için arz biraz daha düşerse - acaba sonsuz bir döngüye girer miyiz?
Bitcoin ya da her tür token için aslında benzer bir risk söz konusu. Fiyat düşünce panik başlar, satışlar artar, sonra fiyat daha da düşer, daha da panik olur gibi.. Ancak geçmişte pek çok kez benzer düşüşleri yaşasa da, Bitcoin sonunda toparlandı. Ampleforth’da da bunu daha dramatik yaşama ihtimali var gibi görünüyor. Sadece fiyat değil, elinizdeki adet de azalıyor. Tamamen farklı alışık olmadığımız bir sistem deneyi. Fiyatın sonrasında geri geleceğine düşünenlerin argümanı şu: Fiyatın ve arzın çok düştüğü durumda tüm sistemin değeri dramatik olarak düşmüş olacak - dolayısı ile bu dışarıdan izleyenlerde ucuza alım fırsatı imkanı doğuracak. Öte taraftan tokeni elinde tutan kişiler fiyatın bu kadar düşmesi durumunda eğer sisteme inanıyorlar ise ellerindeki ürünleri ucuzdan satmak yerine beklemeyi tercih edecekler. 

Burada temel olarak düşünülen toplam piyasa değerinin aynı kalması. Piyasa değeri dediğimiz hisse (ya da token) adedi ile hisse (ya da token) fiyatının çarpımı. Benzer şekilde sizin hissedar olarak varlığınız elinizdeki hisse adedi ile hisse fiyatının çarpımından oluşuyor. Sabit/stabil kripto paralar söz konusu olduğunda varlığınızın sabit kaldığını düşünüyorsunuz ama o kripto paranın bağlı oldukları itibari paralarda dış etkene bağlı olarak değer değişimlerine karşı korumasızsınız. Değeri kendinden menkul paralarda en azından itibari paralarda olduğu gibi devletlerin para politikalarından etkilenmiyorsunuz. Ama orada da fiyat değişimleri sizin varlığınızı etkiliyor. Peki, nasıl elinizde tuttuğunuz varlığın değerini değiştirmeden hisse fiyatını nasıl sabit tutarsınız? 
