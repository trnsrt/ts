# YAZI I

## DeFi'nin sigortası Nexus Mutual

[Nexus Mutual](https://nexusmutual.io), DeFi dünyasına çok ihtiyaç duyulan sigortalamayı getirmeye çalışan girişimlerin en büyüğü. İki yazıdan oluşacak seriminizin ilkinde gelin hep birlikte Nexus Mutual'a ekonomik ve potansiyel olarak bakalım. Bir sonraki yazımızda ise teknik olarak sistem nasıl çalışıyor, tokeni [NXM](https://www.coingecko.com/en/coins/nexus-mutual) nasıl fiyatlanıyor konularına değiniriz.  

### Merkeziyetsiz sigortacılık olur mu?

Her ne kadar bildiğimiz klasik finans ile belli alanlarda kesişse de DeFi yani merkeziyetsiz finans kendi içinde ayrı bir dünya olmaya doğru hızla ilerliyor. DeFi aktörlerinin nihai hedefi de bu aslında. Ancak fiziksel dünya ile iletişimi kesebilmek için belli temel gereksinimlerin karşılanması gerekiyor. Bunların en önemlilerinden biri de sigorta. Üstelik DeFi alanında klasik finansa göre daha da kritik bu gereksinim. Neden? 

Öncelikle daha önce de sıklıkla yazdığımız şu düsturu tekrar hatırlatalım: Klasik finans emanet/velayet (custodial) sistemi çalışır. Yani siz müşteri olarak finansal varlığınızı çalıştığınız kuruma kuzu kuzu verirsiniz. Zaten bu nedenle finans sektöründe çok sıkı kanun ve denetimler var - kanuni otoriteler halkın hakkını korumak için sektörü sıkı kontrol altında tutarlar - başkasının varlığına sahip olmak sorumluluk gerektirir, ağır bir yük. Ama bununla da yetinmez kurumlar - kullanıcı hesapları ile ilgili çeşit çeşit sigortalar da isterler tüketiciyi korumak için. (Ülkemizde mevduatlara verilen 150,000 TL'ye kadar garanti uygulanması gibi). 

DeFi ise emanetsiz/velayetsiz (non-custodial) bir şekilde çalışıyor. DeFi oyuncuları kullanıcının varlığına dokunmazlar. Dijital varlık, sahibinin uhdesinde yani cüzdanında durur.  Kripto dünyasında varlıklarınıza tam anlamıyla sahipsiniz, ama elinizden gittiğinde de "yandı gülüm keten helva". 

Emanetsiz/velayetsiz olma özelliği kullanıcılar için bir yandan finansal özgürlük getiriyor ama öte yandan onları büyük bir sorumluluk altına sokuyor. Zaten yeterince karışık ve teknik bir konuda böyle bir sorumluluk altına girmek kullanıcıları ciddi anlamda tedirgin ediyor. DeFi'nin geniş kesimlerce benimsenmesinin önündeki en büyük engellerden biri de bu. 

Halbuki DeFi dünyasını teknik olarak bilenler ya da projeleri yakından takip edenler için gerçek anlamda risk merkezi finansa göre çok daha düşük. Böyle olunca da alın size merkeziyetsiz bir iş modeli fikri:

Teknik olarak konuya aşina olmayan geniş kesimler, kendilerini güvende hissedebilmek için ufak bir ücret vermeye razı. İşin içine daha girmiş olanlar ise ücreti karşılığı o riski almaya hazır. İki taraf, arada masraflı bir aracı olmadan bir araya gelirse, merkezi olmayan şahane bir model ortaya çıkabilir.

### DeFi'da sigorta sisteminin farkı ne?

DeFi alanındaki sigortacılık klasik sigortacılığa mantık olarak çok benziyor:

Bu alanın lideri Nexus Mutual örneğinden gidersek temel olarak yapmaya çalıştıkları, mevcut sigortacılık sektörü oyuncularının kullandığı risk-hasar parametrelerine sadık kalarak, klasik sigortacılığın kullandığı kapital toplama, ürün çıkarma, risk primi yaratma, toplama ve hasar ödeme işlemlerini olabildiğince merkeziyetsiz hale getirmek. 

Uygulamada ise DeFi oyuncuları iki konuda mevcut sigortacılıktan farklılaşıyor: 

Birincisi klasik sigortacılar henüz çok küçük oldukları için DeFi dünyasına özel ürünler sunmuyorlar. Başka alanlar için düşünülmüş ürünler ise DeFi piyasasının risklerini tam olarak karşılamıyor ya da çok pahalı kaçıyor. Merkeziyetsiz sigortacılık işte bu DeFi platformlarına özgü ürünlerde uzmanlaşıyor. 
İkincisi ise tabii ki, sistemin katılımcılar bazında merkeziyetsiz olması.

 Sigortacılığı belli bir ücret karşılığı bir risk alma ve sonrasında bu riski yatırımcılara plase etme olarak düşünürseniz, klasik sigortacılar bu riski büyük kurumsal fonlara satıyorlar. DeFi dünyasında ise bu riskleri satın alanlar aynı sigortayı yaptıranlar gibi küçük yatırımcılar oluyor. Alıcı ile satıcı arasında ise merkezi bir ofisi olan bir sigorta şirketi yerine [kodları açık bir yazılım var](https://github.com/somish/NexusMutual). 

DeFi'da pek çok işlemde olduğu gibi Akıllı Kontratlar burada da devrede. Ne diyoruz hep: Bu dünyada kod kanun. Hangi durumlarda sigortanın geçerli olduğu baştan belli ve taraflarca kabul edildikten sonra, Akıllı Kontrat'ın yaptığı konu edilen olayın gerçekleşmesi durumunda zarar görene ödeme yapmak. Yatırımcılara da toplanan risk primlerinden gerçekleşen hasarlar düşüldükten sonra kalanını ödemek. Tabii bu teoride böyle.  İşin detaylarına baktığınızda tam bir merkeziyetsiz yapıya ulaşmak için daha kırk fırın ekmek yenmesi gerektiğini açıkça görüyorsunuz. Gelin sisteme daha detaylı bakalım şimdi:

### Nexus Mutual ne, nasıl çalışıyor?

Merkeziyetsiz sigortacılık alanında ortaya çıkmış ve yaygınlaşmış en büyük girişim Nexus Mutual. Kurucusu uzun yıllar sigortacılık sektöründe çalışmış bir Avustralyalı, [Hugh Karp](https://twitter.com/HughKarp). 

Kuruluş fikri, Ethereum'un ilk krizi olan "[The DAO hacki](https://medium.com/@iublocktech/ethereum-ve-dao-hack-daba3f215205)" sonrası ortaya çıkıyor. 2017 yılında ICO çılgınlığı sırasında kurulan girişim uzun süre kendine ait doğru bir iş modeli kurmak konusunda sıkıntı yaşamış, hatta bir kaç kere kapanmanın eşiğine kadar gelmiş. 2020 yılı başlarında ancak 1.5 milyon ABD Doları kadar bir koruma sağlanabilirken, Ekim aylarına geldiğimizde bu rakam 200 milyon ABD Doları'na kadar çıkıyor

Bunun temel nedeni 2020 yazında hareketlenmeye başlayan DeFi piyasası. İngilizce'de FOMO (Fear-of-Missing-Out) olarak adlandırılan, "bir şeyleri kaçırıyorum" duygusunun da etkisi ile bu alana giren bireysel yatırımcılar sayesinde [DeFi pazarı katlanarak arttı](https://defipulse.com). Piyasaya yeni giren yatırımcıların kendilerini teknik olarak yetersiz hissetmeleri Nexus benzeri sigortalara olan ilgiyi tetikledi. Keza sonrasında getiri çiftçiliği olarak adlandırılan 'yield farming'in Ağustos ve Eylül aylarından arşa çıkması sırasında varlıklarını DeFi platformlara emanet eden yatırımcıların duydukları tedirginlik Nexus ürünlerine talebi daha da artırdı.

Temel olarak çalışma şekli kullanıcıların Nexus Mutual sistemine üye olduktan sonra sigorta yaptırmak istedikleri DeFi platformunu (örneğin Compound), süreyi ve miktarı [seçmeleri](https://app.nexusmutual.io/cover/buy/select-contract). Bunun karşılığı olarak sistem kendilerine bir prim rakamı veriyor. Kullanıcı da cüzdanını bağlayıp ETH ya da DAI kullanarak bu primi ödeyip kendini sigortalayabiliyor. Bu arada Nexus Mutual'un sigorta sözcüğünden kaçınarak onun yerine ürünlerine kapsam/koruma (coverage) adını verdiğini de belirtelim.

#### Neler sigortalanıyor, neler sigorta dışı?

Öncelikle şunu belirtmekte fayda var - şu aşamada sigorta edilebilen riskler çok kısıtlı. Neler sigorta ediliyor derseniz, temel olarak sadece 'token satın alan bir kullanıcının, yatırım yaptığı projedeki teknik risklerden dolayı oluşacak zararlar' diyebiliriz. 

Nedir bunlar? Örneğin, Akıllı Kontrat'ın yazılımındaki bir hatadan dolayı dış dünyadan kimi aktörler sistemde kilitli olan tüm parayı çekebilir. Sigorta işte böyle bir durumda kullanıcının satın aldığı token kadar bir miktarı onun cüzdanına gönderiyor. 

Şu aşamada Nexus sigortasının yaptığı sadece bu. Hep söylediğimiz gibi DeFi henüz emekleme aşamasında, bu alandaki ürünler de benzer şekilde yeni yeni çıkıyor ortaya. Nexus, farklı alanlarda farklı riskleri kapsayacak yeni ürünler üzerinden çalıştığını söylüyor. Neler olabilir bunlar dediğimizde yine [Nexus'a kulak vermekte fayda var](https://bankless.substack.com/p/how-to-assess-the-risk-of-lending): 

Özellikle kodun düzgün çalıştığı (kod hatası içermeyen) platformlarda çıkabilecek diğer sorunlar  henüz kapsam dışı. Nedir bunlar derseniz, örneğin, sisteme bilgi veren dış kaynaklarda (oracle da diyoruz bunlara) oluşabilecek sorunlar yani dış kaynaktan sisteme yanlış bilgi gelmesi bir sorun. Ya da DeFi sistemlerinin yönetim yapıları yeni yeni oturmaya başlıyor, burada çıkabilecek yönetimsel sorunlar bir başkası. Farklı bir örnek: platformların verdiği yönetim ile ilgili teşviklere göre hareket eden kimi kullanıcıların aldığı aksiyonlar başka diğer kullanıcılar için zarara neden olabilir. İşte bu tip koda dayanmayan hataları karşılayacak bir sigorta henüz yok. Nexus Mutual hangi riskleri kapsayacak ürünler çıkaracak bekleyip göreceğiz.

#### Ortaklıklar
Nexus Mutual'un sigortasının başarısı diğer projelerin de ilgisini çekti - ve ilginç ortaklıklar/ürünler de gelişmeye başladı. 

Örneğin bu satırlarda sıkça bahsettiğimiz merkeziyetsiz portföy yönetim platformu [yEarn](https://yearn.finance), Nexus Mutual sigortalarını kullanarak [yinsure](https://yinsure.finance/) adında bir ürün çıkardı. Benzer şekilde tekil tokenların bulunduğu [Rarible](https://rarible.com/) platformunda da yNFT denen NXM'e bağlı tokenlar bir süreliğine işlem görmeye başladı - henüz deneme aşamasında olan farklı Nexus ürün ve vadeleri için farklı tokenlar yaratıldı. Benzer şekilde [daha önce bir yazımızda bahsettiğimiz ETC pazarlarında işlem gören BTC](/genel/2020/07/09/eth-gorunumlu-btc-olur-mu.html)'lerde olduğu gibi [ETH tokeni gibi işlem gören WNXM tokenlar](https://www.coingecko.com/en/coins/wrapped-nxm) da çıkarıldı. 

Ne işe yarıyor bu ürünler? NXM, sadece üyeleri tarafından alınıp satılabilen dolayısıyla KYC (know-your-customer, müşterini tanı) prosedürü uygulanan bir token. Merkeziyetsiz Finans dünyasının kullanıcıların gizliliği konusunda hassas olan kesimlerine hitap edemiyor. Yukarıdaki üç ürün de [KYC olmadan sigorta alınabilmeye olanak sağlıyor](https://cryptobriefing.com/nexus-mutual-just-ran-out-defi-coverage-heres-why/). 

### Nexus'un önümüzdeki dönemde başarılı olması için neler gerekli?

Nexus özünde DeFi için yaratılmış bir proje. Başarısı için DeFi pazarının büyümesi gerekli. Daha farklı platformlar için yeni ürünler çıkarmaya devam etmeleri şart. Ama asıl büyüme, farklı riskleri de kapsama alanı için almaları durumunda olacak - yalnızca kontrat hatalarına karşı kullanıcıları koruyarak gidebileceğiniz yol kısıtlı - üstelik kullanıcıların mevcut platformlarda zaman geçirdikçe kendilerini daha rahat hissedip platform riskine para ödemeyi bırakmaları da söz konusu olabilir. yEarn benzeri yapacakları ortaklıklar onların daha geniş kitleler tarafından kullanılmasını sağlayabilir.

Bunun yanında Nexus Mutual'ın olası riskleri karşılamak için elinde tuttuğu bir kapital var - [bu 2020 Ekim aylarında  200 bin ETH (yaklaşık 75 milyon ABD Doları) seviyesinde](https://nexustracker.io/capital_pool). Nexus şu aşamada bu havuzu ekstra yatırımlar için kullanmıyor. Bunun temel nedeni bu kapitali riske etmeden yapılacak yatırımların yeterli olgunluğa ulaşmamış olması. ETH 2.0 ile birlikte gelecek olan Proof of Stake, yani Ethereum sisteminin güvenliğini sağlamak amacıyla fonların kilitlenmesi süreci başladığında, Nexus Mutual için elindeki ETH'yi buraya koyarak ekstradan gelir kazanma ihtimali de doğacak. 

Öte yandan her ne kadar merkeziyetsiz desek de Nexus Mutual hâlâ pek çok konuda merkezi. Örneğin, az önce bahsettiğimiz gibi sisteme üye olmak için KYC prosedürlerinden geçmeniz gerekiyor. Sistemi yürüten Nexus, İngiltere'de kurulu bir şirket. Kullanıcılar sistemin tokeni olan NXM'i alıp satmayı şu aşamada sadece Nexus üzerinde yapabiliyorlar. Öte yandan hasar taleplerinin değerlendirmesi merkeziyetsiz bir şekilde Nexus yatırımcıları tarafından yapılsa da, bu yatırımcıların kurallara uyup uymadığını denetleyen bir merkezi Danışma Kurulu var. Bütün bunlar, Nexus Mutual'ın merkeziyetsiz olma yolunda önünde çözmesi gereken pek çok konu olduğunu gösteriyor. 

### Arkası yarın

Merkeziyetsiz Finans'ın en ilginç projelerinden biri olan Nexus Mutual sigortacılık konusunda neredeyse tekel.  Ancak hâlâ önünde alacağı çok yol var. Yeni çıkan DeFi platformları hızlı bir şekilde ürün olarak sunması, kapsama alanını farklı riskleri de içerecek şekilde genişletmesi, yapacağı yeni pazarlama ortaklıkları Nexus'un büyümesine fayda sağlayacak. Öte yandan sigorta sisteminin karmaşıklığından dolayı henüz merkezi olan kısımlarını yavaş yavaş merkeziyetsiz hale getirmeleri de başarılı olmaları için gerekli. Önümüzdeki yazıda hem Nexus sisteminin merkezi kısımlarından, hem de sistemin tokeni NXM'in nasıl çalıştığından bahsedeceğiz. 


[^1] Eylül ayındaki SAFE olayından sonra bir anda 200 milyon ABD Dolarına çıkan sigorta miktarı, aylık alınan bu poliçelerini dolması ve yenilenmemesi nedeniyle Ekim ayı ortalarında tekrar Eylül ayı öncesi 50 milyon ABD Doları rakamlarına inmiş durumda. 

---

# YAZI II

Geçtiğimiz yazıda merkeziyetsiz bir sigorta sistemi olan [Nexus Mutual'ın hikayesine bakmıştık](). Bu yazımızda ise işin biraz daha tekniğine girerek [Nexus Mutual](https://nexusmutual.io/) sistemi nasıl çalışır, sistemin tokeni NXM nasıl fiyatlanır ona bakacağız. Arkasından NXM tokenları ile yapılabilecek staking benzeri farklı işlemlerden de bahsedeceğiz. 

[ESKİ YAZIYA LİNK]

### Peki nasıl çalışıyor Nexus sistemi?
Nexus Mutual kendisine sigorta demiyor - bunun en önemli nedeni kanuni olarak sigorta mevzuatına takılmamak. Bunun yerine Akıllı Kontratlarda çıkabilecek açıklara karşı "koruma" sağladıklarını belirtiyorlar. 

#### Havuz problemleri yine karşımızda... 
Sistemin çalışması aslında bir havuz şeklinde. Evet, [daha önceki Uniswap yazımızda bahsettiğimiz havuz sistemi](/genel/2020/09/15/nedir-bu-uniswap.html) burada da geçerli. Hatırlarsak, Uniswap'da iki bölmeli iki paradan oluşan havuzlar vardı. Alım satım yapanlar havuzdaki bir paradan almak istedikleri yerine orada bulunan diğer parayı bırakıyorlardı. Nexus Mutual havuzunun çalışma prensipleri ise bir parça farklı. Gelin hızlıca bir göz atalım:

Nexus Mutual'in havuzu özünde sistem tarafında alınan risklere karşılık ödenebilecek kapital rakamının toplamı. Sigorta satın alanların ödedikleri tüm ücretler havuzun içine girişleri oluşturuyor. Yapılan hasar ödemeleri ise temel çıkışları. 

Havuzun sahibi tüm üyeler. Nasıl sahip oluyorlara bu havuza? Aynı hisse senedinde olduğu gibi havuzun sahipliğini gösteren sistemin parası NXM ile. Dolayısı ile NXM sahibi olmak hem havuzun riskini hem de getirisini paylaşmak anlamına geliyor. 

Havuzdaki para ETH olarak tutuluyor. Dolayısıyla Nexus Mutual dünyasının temeli ETH'e dayanıyor, en azından şimdilik. Bu da anlaşılır, zira koruma verdikleri DeFi platformlarının çoğunluğu da Ethereum üzerinde işlem yaptığı için risk ETH, bu riske karşı fonları da ETH olarak değerlendirmek mantıklı. 

### Kim niye NXM alsın? 
Birkaç neden var. 

Öncelikle sigorta yaptırmak, pardon "Akıllı Kontratlar'a karşı koruma satın almak" istiyorsanız bunu NXM ile yapıyorsunuz.  Yaptırmak istediğiniz sigorta miktarı ve süresine bağlı olarak aldığınız korumanın ücretini NXM olarak veriyorsunuz (bir başka deyişle NXM yakıyorsunuz). NXM'i de havuzdan ETH ya da [stabil bir kripto para olan DAI](/genel/2018/07/20/Orasi-cok-dalgali-sakin-sulara-gel-sabitparalar.html) karşılığı alacaksınız, yani primi bir nevi ETH ile ödüyorsunuz. 

İkincisi ise yatırım olarak almak. Sonuç olarak NXM aldığınızda havuzun bir parçasına sahip oluyorsunuz. NXM değerini neler etkiliyor, hemen bir sonraki bölümde değerlendireceğiz. 

Bunun dışında NXM sahibi olarak tazminat isteyenlerin taleplerini değerlendirmek, az sonra bahsedeceğimiz çeşitli ürünlere direkt olarak yatırım yapmak, ya da NXM yönetim sisteminde (yeni ürünleri belirlemek benzeri oylamalara katılmak) söz sahibi olmak gibi Nexus Mutual'a özel belli para kazandırıcı aktivitelere katılmak da mümkün. 

Bu arada bir konuyu tekrarlamakta fayda var: Her ne kadar merkeziyetsiz bir sistem olsa da Nexus Mutual'ın belli alanlarda kısıtları olduğunu belirtmiştik. Örneğin, NXM yalnızca Nexus Mutual'un kendi kurduğu platformda işlem görüyor. NXM satın almak isteyenler Nexus Mutual sistemine üye olmak zorundalar. Üye olmak için de müşterini tanı (KYC - Know your customer) işleminden geçmek gerekiyor.  KYC işlemlerini yapan Nexus Mutual kurucularının girişimi İngiltere merkezli ve lisanslı bir şirket. 

### NXM fiyatı neye göre belirleniyor?

İşte Nexus Mutual'ın diğer merkeziyetsiz sistemlerden bir farkı daha. Nexus'un tokeni NXM'in değeri serbest piyasadaki arz ve talebe göre belirlenmiyor, zira NXM kripto para borsalarında işlem gören bir token değil. Bunun yerine NXM'in fiyatı bir algoritma ile hesaplanıyor. Nasıl bir hesaplama bu?

Hatırlarsanız, [Uniswap kendi içinde basit bir algoritma kullanarak al-sat yapmak isteyenlere bir fiyat veriyordu](/genel/2020/09/15/nedir-bu-uniswap.html). Bunu yaparken algoritmanın temel hedefi, ne olursa olsun işlem yapmak isteyenlere bir fiyat vermek idi. **Nexus Mutual algoritması da benzer şekilde işlem yapmak isteyenlere otomatik bir fiyat veriyor. Ama bunu yaparken hem arz ve talebi, hem de Nexus Mutual havuzunun finansal sağlığını korumaya çalışıyor**.

Nexux'un havuzunun temel amacı olası hasarlara karşı ödeme yapabilmek - bu sistemin olmazsa olması. **Bu nedenle havuzun içinde talepleri belirli oranda karşılayabilecek kadar kapital bulunması birincil hedef**. Eğer havuzun içinde o belirlenen minimum oran kadar para yoksa öncelikle hiç kimse NXM satıp ETH alamıyor (bu oranın adı MCR - minimum capital requirement, minimum karşılık olarak düşünülebilirsiniz)[^3]. 

Algoritmanın ikinci amacı ise, gelişen arz ve talebe göre NXM fiyatını ayarlayarak sistemi sağlıklı tutmak. Bunu da otomatik bir formül ile yapıyor[^4]. Bu da şu şekilde oluyor: 

Eğer havuzda toplanan para minimum rakamın %30'dan fazlasına ulaşırsa, formül NXM fiyatını hızlı bir şekilde yükseltmeye başlıyor. Bunun nedeni yüksek NXM fiyatı olduğunda, elinde NXM tutan yatırımcıların NXM satıp havuzdan ETH çekmesini sağlamak. Neden böyle yapıyor? Çünkü havuzda değerlendirilmeden duran para, verimsizlik göstergesi. 

Bu arada, Nexus Mutual yönetiminin elde fazla kapital olması durumunda alacağı bir aksiyon daha var. O da yeni sigorta ürünleri çıkarmak. Bu sayede sistemi büyütebilirler. Yeni ürünler çıkması insanların bu ürünler için de karşılık ayrılmasını gerektireceği için minimum karşılık oranını yükseltecek. 

Yine aynı şekilde eğer havuzdaki para minimum rakama doğru yaklaşmaya başlarsa formüle göre NXM fiyatı hızlı bir şekilde düşmeye başlıyor. Mantık aynı: Eğer NXM'in fiyatı ucuzlar ise, o zaman yatırımcılar çok daha ucuza havuzdan pay sahibi olmak hakkını kaçırmak istemeyecekler, bu nedenle havuza ETH koyup NXM satın alacaklar. Böylece havuzdaki kapital yani ETH miktarı artacak. 

Özetle algoritma dediğimiz basit formül sayesinde hedeflenen, NXM fiyatı ile oynayarak, havuzdaki kapital miktarının belli bir bant içinde oynamasını sağlamak. Bu bandın altı minimum karşılık oranı olan MCR, üstü ise MCR'nin %30 fazlası. 

### Nasıl sigorta yapıyorsunuz?
Üye olduktan sonra aslında çok da karmaşık değil. Kullanıcı farklı ürünlerden hangisine karşı kendisini korumak istiyor ise onu seçiyor, kaç gün için ve ne kadarlık bir miktar için korunma istediğini belirliyor. Sistem kendisine bir oran veriyor. Burada kullanıcı ödemeyi dilerse NXM dilerse ise ETH ile yapabiliyor. 

#### Peki bu oranı kim nasıl belirliyor?
Bu oranı belirlemek işini aslında Nexus Mutual yatırımcıları yapıyor. Bunu da staking dediğimiz rehin verme işlemi ile yapıyorlar. 

Staking daha fazla risk karşılığı daha da fazla getiri almak isteyenler için kurulmuş bir sistem. Normalde Nexus Mutual'a yatırımcı olmak istediğinizde, havuzdan NXM satın alıyor ve tüm sistem risk ve getirisine ortak oluyorsunuz. Ancak staking yaptığınızda bu yatırımı ürün bazında ayrıştırmak mümkün oluyor. 

NXM satın alan dolayısıyla genel sisteme yatırım yapmış bir yatırımcı sonrasında dilerse bu NXM'i ile belli bir spesifik ürüne koyarak riskini daha da artırabiliyor. Böyle yaparak bu spesifik ürünü satın almış olanların ödedikleri primlerden bir kısmını havuzdan önce kazanma hakkına sahip oluyor. Risk tarafında ise üründe bir sorun çıkıp da zarar tazminat ödenmesi halinde koymuş olduğu NXM'i toptan kaybetme ihtimali de var. Bu nedenle, staking'in ekstra bir riskli bir yatırım olduğu unutulmamalı. 

Nexus Mutual'in ürünlerinin her biri için risk primi ve bir kota belirleniyor. Yatırımcılar bu oranlardan spesifik bir ürüne staking yapabiliyorlar.  Aslına bakarsanız, staking bir nevi spesifik Akıllı Kontratların risklerini anlayabilmek için güzel bir endikatör aynı zamanda. Riskleri (yani sigorta yapılmış tutarları) aynı olan iki Akıllı Kontrat'tan birine diğerinin iki katı kadar staking yapılmışsa, bu birinci kontratın genel olarak çok daha az riskli görüldüğü anlamına gelebilir. 

#### Bir sorun olduğunda ödeme yapılacağına kim karar veriyor?
Her ne kadar Akıllı Kontratlar var desek de, ödemeler henüz otomatik yapılacak seviyeye gelmiş değil. Bunu DeFi'nin emekleme aşamasında olmasına bağlayabilirsiniz - belki önümüzdeki dönemde orada da olabildiğince otomatize bir sistem olabilir. Bir sistem sorunu olduğu ve ödeme yapılması gerektiğine Nexus Mutual'a üye olanlar oylama ile karar veriyorlar. Eğer Nexus Mutual üyeleri (ellerinde NXM token tutanlar) sistemsel bir sorun olduğu ve ödeme yapılması gerektiği konusunda bir karar verirlerse işte o zaman Akıllı Kontratlar devreye girip ürün satın almış olan kullanıcılara tazminatlarını ödüyorlar. 

#### Nasıl hasar talep ediliyor?
Herhangi bir hasar olayı olduğunda, ilgili üründen koruma almış olanlar, Nexus Mutual sitesine başvuruyorlar. Yapılan talep bir kısım NXM sahibi tarafından değerlendiriliyor. Burada ilginç bir nokta var: Talebi değerlendirenler ellerindeki NXM'leri sisteme kilitliyorlar. Kararların %70 çoğunluk ile verilmesi gerekiyor[^1]. Çoğunluk ile oy kullananlar ekstra NXM kazanıyor. Karşı oy kullananların ise NXM'leri bir süreliğine kilitli kalmaya devam ediyor ve incelemeye tabi tutuluyor. İnceleme sonucu kötü niyetli oldukları saptanırsa NXM'leri yakılıyor. Gördüğünüz gibi hasar talep sisteminin değerlendirilmesi hâlâ manuel şekilde oluyor denebilir. Çoğunluğa karşı oy kullananları değerlendiren bir komite var beş üyeden oluşan - çok da merkeziyetsiz sayılmaz şu aşamada. 


#### Hiç hasar karşılama ödemesi yapmış mı Nexus Mutual?
Şimdiye kadar bir durumda ödeme yapılmış. 2020 Şubat ayında [bzX sistemindeki bir açıktan dolayı oluşan hasarda](https://bzx.network/blog/postmortem-ethdenver) Nexus Mutual üyeleri [iki adet koruma alan kullanıcının için toplam 35,000 ABD Doları'na yakın bir ödeme yapmışlar](https://medium.com/nexus-mutual/bzx-flash-loan-event-55753d19e52b). Şu ana kadar toplam 53 hasar talebi geldiğini ve sadece az önce bahsettiğimiz bZx hasarına ait üç talebin karşılandığını, 47 talebin reddedildiğini de hatırlatalım[^2]


### Sonuç
Birinci bölümünde genel olarak başladığımız bu yazıda ise daha teknik detaylarına girdiğimiz DeFi'da sigortacılık sistemi Nexus Mutual, şu ana kadar belli kısımları merkeziyetsizleşmiş gelecek vadeden bir proje. DeFi'nin büyümesi ve yeni ürünlerin ortaya çıkması ile birlikte büyümesi de yüksek bir ihtimal. Gelişimini yakından izleyeceğiz. 



---


[^1] Yapılan oylamada verilen karar %70 çoğunluk ile alınmalı - aksi takdirde tüm sistem tarafından bir oylama daha yapılıyor. 
[^2] Üç adet talep henüz değerlendirme aşamasında
[^3] (bu oranın adı MCR - minimum capital requirement oranı). 𝑇𝑃 = 𝐴 + (𝑀𝐶𝑅𝐸𝑇𝐻/𝐶)∙ 𝑀𝐶𝑅%4

---
Kaynaklar: 

https://cryptobriefing.com/defi-review-what-is-nexus-mutual-introduction-nxm/
https://cryptobriefing.com/nexus-mutual-just-ran-out-defi-coverage-heres-why/
https://tokentuesdays.substack.com/p/nexus-mutual
https://academy.ivanontech.com/blog/introduction-to-defi-insurance-and-nexus-mutual

---


#### Sigortacının havuzu başka olur... 

Havuzda 

Aslında sistemin klasik sigortacılıktan çok da farkı yok. Normalde sigorta şirketleri aldıkları toplam riskin tamamı değil bir kısmı kadar kapital tutarlar. Herhangi bir riskin gerçekleşmesi durumunda hasar bu kapitalden ödenir. Risklere karşı ödenen sigorta primleri de bu kapitale eklenir. Burada da yukarıda bahsettiğimiz havuz aslında Nexus sisteminin kapitali. Bu kapitali bireysel yatırımcılar sağlıyor. Zararlar yani hasarlar buradan ödeniyor. Sigorta primleri de kâr olarak bu havuza konuyor. 

Tabii bu havuzun klasik bankacılığa göre belli farklılıkları ve zorlukları var. Bunun en önemlisi havuzdaki kapital ile karşılanan risk oranında bir denge tutturabilmek. Zira, havuzda kapital az, ama risk fazla olursa sistemin çökme riski olabilir. Tam tersi bir durumda kapitalin çok fazla olması durumunda ise yeterli sigorta prim getirisi olmayacağı için kapitalin verimli kullanılamaması gibi bir durum söz konusu olabiliyor. 

Sistem çökme riski olmaması için havuzdaki kapitalin toplam riskin belli bir oranının altına inmemesi gibi bir kural var. Bu oran %30 olarak belirlenmiş. Eğer toplam kapital bu rakamın altına inerse, sistem yatırımcıların kapital çekme isteklerini karşılamıyor. 

Öte yandan sistemde ekstra kapital olması durumunda da, Nexus ekibi yeni ürünler çıkararak sistemi büyütme yoluna gidiyorlar. Yeni ürün çıkması, bu ürünleri kullanarak kendilerini sigortalamak isteyenlerin olması nedeniyle toplam riskin artması anlamına geliyor. Bu da minimum kapital rakamını (%30'u) yukarı çekiyor. Yani ekstra kapital yeni yatırım için kullanılmış oluyor. Ekstra kapital miktarı minimum kapitalden %30 fazla olacak şekilde belirlenmiş. 

Dolayısıyla, havuz öyle bir şekilde dizayn edilmiş ki, havuzdaki kapital minimum kapital ile onun %30 fazlası arasındaki bantta oynuyor. Nasıl dizayn etmişler bunu? Uniswap'ta olduğu gibi bir algoritma kullanıyorlar ama daha karmaşık bir algoritma. 

Buna göre eğer havuzdaki kapital miktarı minimum kapitale doğru yaklaşırsa NXM miktarını dramatik bir şekilde düşürüyorlar. Bu sayede, NXM'in fiyatının çok düştüğünü gören yatırımcılar ucuza alım fırsatı olduğunu düşünerek sisteme ETH koyuyorlar. 

Keza benzer şekilde eğer Nexus sistemindeki kapital çok artar ise o zaman da NXM'in fiyatı hızla yükseliyor. Bu da benzer şekilde yatırımcıların bu artışı değerlendirmek için NXM satmalarına neden oluyor - sistem yeniden dengeye geliyor.  
