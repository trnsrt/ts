

Not: 
İşlemler şu şekilde gerçekleşiyor: 
- Uniswap üzerinde yapılan bir işlem akıllı kontrat aracılığıyla Ethereum blokzincirine yazılır
- Graph sisteminin endeksçileri her yeni Ethereum bloğunu tarayarak bu bilgileri yakalarlar
- Eğer yakalanan kontrat bilgileri içinde sizin istediğiniz koşullara uygun olanlar varsa bu bilgiler bir araya getiriliyor


---

Compound: 

### Ne tip sıkıntıları var?

Compound, DeFi hareketinin üç büyüklerinden ama en büyük MakerDAO'nun oldukça gerisinde. Neden? [[Sanırım en önemli nedeni, likidite konusundaki sıkıntıları]

### Potansiyeli var mı?

#### Şu anki büyüklüğü ne kadar? Bir yılda ne kadar büyümüş?

#### Gelecekte ne bekleniyor? Neden büyümesi bekleniyor?


### Peki rakipleri kimler?


---


### Rakipler kimler? 

#### Curve: 
Curve daha çok sabit paralar üzerine uzmanlaşmış bir sistem. Zira Curve’un komisyonlar UniSwap’un aksine 0.04% oranında ve işlemlerde kullandığı algoritma UniSwap’a nazaran özellikle stabil paralar için daha uygun. O nedenle işlemler ciddi şekilde Curve’e kaymış durumda. [^2]. Öte yandan Curve likidite sağlayanlara komisyon dışında bir de kendi yönetim tokenini (CRV) veriyor - bu nedenle oldukça rağbet görüyor. 

#### Balancer: 
UniSwap’tan bahsederken temel bir özelliğin havuzun iki bölmesine eşit değerde iki para koymak olduğunu belirtmiştik. Balancer temel olarak burada sistemi bir adım öteye götürerek, havuza iki bölmesine konan paraların 50%-50% değil istenen oranlarda olmasına imkan tanıyor. Balancer da aynı Curve gibi likidite sağlayacılara BAL token'i dağıtıyor, bu nedenle oldukça sisteme ilgi oldukça yüksek

#### Sushiswap, Mooniswap, vb:
Uniswap'ın birebir klonlanmış benzerleri olan bu sistemler, üzerien Curve ya da Balancer gibi bir de yönetim token'ı verdikleri için yaz ayları içinde oldukça popüler oldular. [Bir önceki yazımızda](https://turansert.com/genel/2020/09/08/defi-cok-mu-hizli-gidiyor.html) da detaylı olarak anlattığımız bu klonlar henüz kendilerini kanıtlamış değiller.


[^2] Curve’in özelliği stabil paralara uyacak bir algoritma içermesi. Uniswap havuz değeri için A ve B token’larının çarpımını sabit tutarken, Curve A ve B tokenlarının toplamını sabit tutuyor. Böyle olunca, birbirine yakın ve fiyatları genelde çok ayrışmayan (burada stabil paralar gibi 1 ABD Doları’na yakınsayan) paralarda değer çok daha yavaş değişip işlem olduğunda büyük fiyat farkları oluşmuyor. Ama eğer çok büyük hacimler olur ve iki token arasında fiyat farkları oluşursa o zaman Uniswap daha gerçekçi fiyatlar veriyor. 


----


### Teknolojik yenilik
Özellikle iç yönetim (governance) bakımından merkezi girişimlerin teknolojik yenilik getirmede daha avantajlı olacağını söylemek mümkün. Bugün Bitcoin için yapılan en büyük eleştirilerden biri teknolojik olarak yenilik getiremiyor olması. Bunda Bitcoin'in bir "para" olmasının ve yapılacak her tür değişikliğin etkilerinin çok detaylıca tartılması gerekliliğinin payı yüksek. Yapılacak hataların direkt bireylerin varlıklarına değerine etkisi olacak - o nedenle "deneysellik" olabildiğince az kullanılabiliyor.  Keza, Ethererum için de benzer bir durum söz konusu. Gerek merkezi olmayan bir grup tarafından sürdürülüyor olması, gerekse üzerinde binlerce uygulama hali hazırda çalıştığı için yenilikler çok yavaş gerçekleşiyor. Ethereum 2.0 denen güncelleme iki yıllık bir süreç içinde hayata geçecek gibi görünüyor. 


---


Ancak bunlarla da sınırlı değil yapabildikleriniz. İleride üzerinde daha da duracağız ama örneğin gerçek dünyada kurduğunuz kanuni yapıların (anonim şirket, kooperatif gibi) benzerlerini ama bu sefer arada sınırlar olmadan yüzlerce kişi ile birlikte kurabiliyorsunuz. Üstelik sudan ucuz bir fiyata. Bu yapıları nasıl yönetebileceğiniz konusunda alternatifler sınırsız. Aradaki anlaşmazlıkların nasıl çözüleceği konusunda "kod kanundur" düsturundan gelen Akıllı Kontratları kullanabileceğiniz gibi, arada uyuşmazlık olduğunda size arabulucu ya da mahkeme hizmeti veren (tamamen merkeziyetsiz) hizmetler bile mümkün bu yapılarda. 
Şu anda hayal, ya da oyuncak gibi görünen bu yapılar bir gün gerçek olacak mı? Bugünden kestirmek zor. Ama hep yazdığımız gibi yapılabilecekleri düşünmek bile çok ama çok heyecan verici.. 

---


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

