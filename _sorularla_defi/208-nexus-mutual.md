---
layout: book-section
kind: section
title: "Nexus Mutual: DeFi’nin Sigortası – Sorularla DeFi"
heading: "Nexus Mutual: DeFi’nin Sigortası"
chapter: 2
chapter_title: "DeFi Dünyasının Aktörleri"
order: 208
permalink: /Sorularla_DeFi/bolum-2/nexus-mutual/
description: "Nexus Mutual, DeFi platformlarına karşı koruma (coverage) satan, merkeziyetsiz bir sigorta girişimi. Üye, korunmak istediği platformu, süreyi ve miktarı seçip prim ödüyor; primler ve tazminatlar, sahipliği NXM tokeniyle gösterilen ortak bir havuz üzerinden işliyor. Hasar taleplerini NXM sahipleri değerlendiriyor, onaylanırsa akıllı kontrat tazminatı ödüyor."
---

[Nexus Mutual](https://nexusmutual.io/), DeFi dünyasına çok ihtiyaç duyulan sigortalamayı getirmeye çalışan girişimlerin en büyüğü. Gelin önce hep birlikte Nexus Mutual’a ekonomik ve potansiyel olarak bakalım sonra da teknik olarak sistem nasıl çalışıyor, tokeni [NXM](https://www.coingecko.com/en/coins/nexus-mutual) nasıl fiyatlanıyor konularına değiniriz.

## Merkeziyetsiz sigortacılık olur mu? {#merkeziyetsiz-sigortacilik-olur-mu}

Her ne kadar bildiğimiz klasik finans ile belli alanlarda kesişse de DeFi yani merkeziyetsiz finans kendi içinde ayrı bir dünya olmaya doğru hızla ilerliyor. DeFi aktörlerinin nihai hedefi de bu aslında. Ancak fiziksel dünya ile iletişimi kesebilmek için belli temel gereksinimlerin karşılanması gerekiyor. Bunların en önemlilerinden biri de sigorta. Üstelik DeFi alanında klasik finansa göre daha da kritik bu gereksinim. Neden?

<figure><a href="/assets/books/sorularla-defi/208-1.jpeg"><img src="/assets/books/sorularla-defi/208-1.jpeg" alt="Image by neo tam from Pixabay" width="1200" height="675" loading="lazy"></a><figcaption>Image by <a href="https://pixabay.com/users/neotam-11291643/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4510667">neo tam</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4510667">Pixabay</a></figcaption></figure>

Öncelikle, bundan önceki sayfalarda sıklıkla yazdığımız şu düsturu tekrar hatırlatalım: Klasik finans, emanet/velayet (İngilizce’de 'custodial') sistemi ile çalışır. Yani siz, müşteri olarak, işlem yapabilmek için finansal varlığınızı hizmet aldığınız kuruma kuzu kuzu verirsiniz. Zaten bu nedenle finans sektöründe çok sıkı kanun ve denetimler var. Kanuni otoriteler, halkın hakkını korumak için sektörü sıkı kontrol altında tutarlar. Başkasının varlığına sahip olmak sorumluluk gerektirir, ağır bir yük. Bununla da yetinmez kurumlar; kullanıcı hesapları ile ilgili çeşit çeşit sigortalar da isterler tüketiciyi korumak için. (Ülkemizde mevduatlara verilen 150,000 TL’ye kadar [garanti uygulanması](https://www.tmsf.org.tr/tr/Tmsf/Mevduat/mevduat.sss) gibi).

DeFi ise emanetsiz/velayetsiz (non-custodial) bir şekilde çalışıyor. DeFi oyuncuları kullanıcının varlığına dokunmazlar. Dijital varlık, sahibinin uhdesinde, yani cüzdanında durur. Kripto dünyasında varlıklarınıza tam anlamıyla sahipsiniz ama elinizden gittiğinde de “yandı gülüm keten helva”.

Emanetsiz/velayetsiz olma özelliği kullanıcılar için bir yandan finansal özgürlük getiriyor ama öte yandan onları büyük bir sorumluluk altına sokuyor. Zaten yeterince karışık ve teknik bir konuda böyle bir sorumluluk altına girmek kullanıcıları ciddi anlamda tedirgin ediyor. DeFi’nin geniş kesimlerce benimsenmesinin önündeki en büyük engellerden biri de bu.

Halbuki DeFi dünyasını teknik olarak bilenler ya da projeleri yakından takip edenler için gerçek anlamda risk, merkezi finansa göre çok daha düşük. Böyle olunca da alın size merkeziyetsiz bir iş modeli fikri:

Teknik olarak konuya aşina olmayan geniş kesimler, kendilerini güvende hissedebilmek için ufak bir ücret vermeye razı. İşin içine daha yeni girmiş olanlar ise ücreti karşılığı o riski almaya hazır. İki taraf, arada masraflı bir aracı olmadan bir araya gelirse, merkezi olmayan şahane bir model ortaya çıkabilir.

### DeFi’da sigorta sisteminin farkı ne? {#defida-sigorta-sisteminin-farki-ne}

DeFi alanındaki sigortacılık klasik sigortacılığa mantık olarak çok benziyor:

Bu alanın lideri Nexus Mutual örneğinden gidersek temel olarak yapmaya çalıştıkları, mevcut sigortacılık sektörü oyuncularının kullandığı risk-hasar parametrelerine sadık kalarak klasik sigortacılığın kullandığı kapital toplama, ürün çıkarma, risk primi yaratma, toplama ve hasar ödeme işlemlerini olabildiğince merkeziyetsiz hâle getirmek.

Uygulamada ise DeFi oyuncuları iki konuda mevcut sigortacılıktan farklılaşıyor:

Birincisi klasik sigortacılar henüz çok küçük oldukları için DeFi dünyasına özel ürünler sunmuyorlar. Başka alanlar için düşünülmüş ürünler ise DeFi piyasasının risklerini tam olarak karşılamıyor ya da çok pahalı kaçıyor. Merkeziyetsiz sigortacılık işte bu DeFi platformlarına özgü ürünlerde uzmanlaşıyor. İkincisi ise tabii ki sistemin katılımcılar bazında merkeziyetsiz olması.

Sigortacılığı belli bir ücret karşılığı bir risk alma ve sonrasında bu riski yatırımcılara aktarma (plase etme) olarak düşünürseniz, klasik sigortacılar bu riski büyük kurumsal fonlara satarlar. DeFi dünyasında ise bu riskleri satın alanlar, (aynı sigortayı yaptıranlar gibi) küçük yatırımcılar oluyor. Alıcı ile satıcı arasında ise merkezi bir ofisi olan bir sigorta şirketi yerine [kodları açık bir yazılım var](https://github.com/somish/NexusMutual).

DeFi’de pek çok işlemde olduğu gibi akıllı kontratlar burada da devrede. Ne diyoruz hep: Bu dünyada kod kanun. Hangi durumlarda sigortanın geçerli olduğu baştan belli ve taraflarca kabul edildikten sonra akıllı kontratın yaptığı, konu edilen olayın gerçekleşmesi durumunda zarar görene ödeme yapmak. Yatırımcılara da toplanan risk primlerinden gerçekleşen hasarlar düşüldükten sonra kalanını ödemek. Tabii bu teoride böyle. İşin detaylarına baktığınızda tam bir merkeziyetsiz yapıya ulaşmak için daha kırk fırın ekmek yenmesi gerektiğini açıkça görüyorsunuz. Gelin sisteme daha detaylı bakalım şimdi:

## Nexus Mutual nedir? {#nexus-mutual-nedir}

Merkeziyetsiz sigortacılık alanında ortaya çıkmış ve yaygınlaşmış en büyük girişim Nexus Mutual. Kurucusu uzun yıllar sigortacılık sektöründe çalışmış bir Avustralyalı, [Hugh Karp](https://twitter.com/HughKarp).

Kuruluş fikri, Ethereum’un ilk krizi olan “[The DAO hacki](https://medium.com/@iublocktech/ethereum-ve-dao-hack-daba3f215205)” sonrası ortaya çıkıyor. 2017 yılında ICO çılgınlığı sırasında kurulan girişim uzun süre kendine ait doğru bir iş modeli kurmak konusunda sıkıntı yaşamış, hatta bir kaç kere kapanmanın eşiğine kadar gelmiş. 2020 yılı başlarında ancak 1.5 milyon ABD Doları kadar bir koruma sağlanabilirken, Ekim aylarına geldiğimizde bu rakam 200 milyon ABD Doları’na kadar çıkıyor.

Bunun temel nedeni 2020 yazında hareketlenmeye başlayan DeFi piyasası. İngilizce’de FOMO (Fear-of-Missing-Out) olarak adlandırılan, “bir şeyleri kaçırıyorum” duygusunun da etkisi ile bu alana giren bireysel yatırımcılar sayesinde [DeFi pazarı katlanarak arttı](https://defipulse.com/). Piyasaya yeni giren yatırımcıların kendilerini teknik olarak yetersiz hissetmeleri, Nexus benzeri sigortalara olan ilgiyi tetikledi. Keza sonrasında getiri çiftçiliği olarak adlandırılan ‘yield farming’in Ağustos ve Eylül aylarından arşa çıkması sırasında varlıklarını DeFi platformlara emanet eden yatırımcıların duydukları tedirginlik Nexus ürünlerine talebi daha da artırdı.

## Nasıl çalışıyor Nexus sistemi? {#nasil-calisiyor-nexus-sistemi}

Temel olarak çalışma şekli; kullanıcıların Nexus Mutual sistemine üye olduktan sonra sigorta yaptırmak istedikleri DeFi platformunu (örneğin Compound), süreyi ve miktarı seçmeleri. Bunun karşılığı olarak sistem kendilerine bir prim rakamı veriyor. Kullanıcı da cüzdanını bağlayıp ETH ya da DAI kullanarak bu primi ödeyip kendini sigortalayabiliyor. (Bu arada Nexus Mutual’un sigorta sözcüğünden kaçınarak; onun yerine, ürünlerine kapsam/koruma (coverage) adını verdiğini de belirtelim).

### Nexus Mutual’da neler sigortalanıyor, neler sigorta dışı? {#neler-sigortalaniyor-neler-sigorta-disi}

Öncelikle şunu belirtmekte fayda var: Şu aşamada sigorta edilebilen riskler çok kısıtlı. Neler sigorta ediliyor derseniz, temel olarak sadece “token satın alan bir kullanıcının, yatırım yaptığı projedeki teknik risklerden dolayı oluşacak zararlar” diyebiliriz.

Nedir bunlar? Örneğin akıllı kontratın yazılımındaki bir hatadan dolayı dış dünyadan kimi aktörler sistemde kilitli olan tüm parayı çekebilir. Sigorta işte böyle bir durumda kullanıcının satın aldığı token kadar bir miktarı onun cüzdanına gönderiyor.

Şu aşamada Nexus sigortasının yaptığı sadece bu. Hep söylediğimiz gibi DeFi henüz emekleme aşamasında, bu alandaki ürünler de benzer şekilde yeni yeni ortaya çıkıyor. Nexus, farklı alanlarda farklı riskleri kapsayacak yeni ürünler üzerinden çalıştığını söylüyor. Neler olabilir bunlar dediğimizde yine Nexus’a kulak vermekte fayda var:

Özellikle kodun düzgün çalıştığı (kod hatası içermeyen) platformlarda çıkabilecek diğer sorunlar henüz kapsam dışı. Örneğin, sisteme bilgi veren dış kaynaklarda (İngilizcede ‘oracle’) oluşabilecek sorunlar yani dış kaynaktan sisteme yanlış bilgi gelmesi bir risk. Ayrıca yeni yeni oturmaya başlayan DeFi sistemlerinde çıkabilecek yönetimsel sorunlar da bir risk. Bir örnek daha verelim; platformların verdiği yönetimle ilgili teşvikleri kazanmak isteyen kimi kullanıcıların yaptığı hareketler, diğer kullanıcıların zarar etmesine neden olabilir. İşte bu tip koda dayanmayan hataları karşılayacak bir sigorta henüz yok. Nexus Mutual hangi riskleri kapsayacak ürünler çıkaracak, bekleyip göreceğiz.

### Ortaklıklar {#ortakliklar}

Nexus Mutual’un sigortasının başarısı diğer projelerin de ilgisini çekti ve ilginç ortaklıklar/ürünler de gelişmeye başladı.

Örneğin üç bölüm önce bahsettiğimiz merkeziyetsiz portföy yönetim platformu [Yearn](https://yearn.finance/), Nexus Mutual sigortalarını kullanarak yInsure adında bir ürün çıkardı. Benzer şekilde tekil tokenlerin bulunduğu [Rarible](https://rarible.com/) platformunda da yNFT denen NXM’e bağlı tokenler bir süreliğine işlem görmeye başladı - henüz deneme aşamasında olan farklı Nexus ürün ve vadeleri için farklı tokenler yaratıldı.

Ne işe yarıyor bu ürünler? NXM, sadece üyeleri tarafından alınıp satılabilen dolayısıyla KYC (know-your-customer, müşterini tanı) prosedürü uygulanan bir token. Halbuki merkeziyetsiz finans dünyası içinde, kişiler bilgilerinin mahremiyetini korumak konusunda hassas olan bir kesim var. Yukarıdaki iki ürün de [KYC olmadan sigorta alınabilmeye olanak sağlıyor](https://cryptobriefing.com/nexus-mutual-just-ran-out-defi-coverage-heres-why/).

### Havuz problemleri yine karşımızda… {#havuz-problemleri-yine-karsimizda}

Sistemin çalışması aslında bir havuz şeklinde. Evet, daha önceki Uniswap bölümünde bahsettiğimiz havuz sistemi burada da geçerli.

Hatırlarsak Uniswap’da iki bölmeli iki paradan oluşan havuzlar vardı. Alım satım yapanlar, havuzdaki almak istedikleri bir para yerine, orada bulunan diğer parayı bırakıyorlardı.

### Nexus’un havuzu diğerlerinden farklı… {#nexusun-havuzu-digerlerinden-farkli}

Nexus Mutual havuzunun çalışma prensipleri ise bir parça farklı. Gelin hızlıca bir göz atalım.

Nexus Mutual’in havuzu özünde sistem tarafından alınan risklere karşılık ödenebilecek kapital rakamının toplamından oluşuyor. Sigorta satın alanların ödedikleri tüm ücretler, havuzun içine girişleri, yapılan hasar ödemeleri ise havuzdan temel çıkışları oluşturuyor.

Havuzun sahibi tüm üyeler. Nasıl sahip oluyorlar bu havuza? Aynı hisse senedinde olduğu gibi havuzun sahipliğini gösteren sistemin parası NXM ile. Dolayısı ile NXM sahibi olmak, hem havuzun riskini hem de getirisini paylaşmak anlamına geliyor.

Peki başlangıçta sistem nasıl başladı? Havuz boş muydu? Hayır, bu alanda tecrübeli, riski bilen kişi ve kurumlar başlangıçta Ethereum sisteminin parası olan ETH koyup karşılığında NXM alarak havuza bir kapital sağladılar.

Havuzdaki para ETH olarak tutuluyor. Dolayısıyla Nexus Mutual dünyasının temeli en azından şimdilik ETH’ye dayanıyor. Bu da anlaşılır, zira koruma verdikleri DeFi platformlarının çoğunluğu da Ethereum üzerinde işlem yaptığı için risk ETH bazlı, o nedenle bu riske karşı fonları da ETH olarak değerlendirmek mantıklı.

### Kim niye NXM alsın? {#kim-niye-nxm-alsin}

Birkaç neden var.

Öncelikle sigorta yaptırmak, pardon 'Akıllı kontratlar’a karşı koruma satın almak' istiyorsanız bunu NXM ile yapıyorsunuz. Yaptırmak istediğiniz sigorta miktarı ve süresine bağlı olarak aldığınız korumanın yani poliçenin ücretini NXM olarak veriyorsunuz. Bir başka deyişle NXM yakıyorsunuz. NXM’i de havuzdan ETH ya da [stabil bir kriptopara olan DAI](https://turansert.com/genel/2018/07/20/Orasi-cok-dalgali-sakin-sulara-gel-sabitparalar.html) karşılığı alacaksınız.

İkincisi ise yatırım olarak almak. Sonuç olarak NXM aldığınızda havuzun bir parçasına sahip oluyorsunuz ve ödenen primlerin risklerden fazla olduğunu ve sistemin ileride büyüyeceğini tahmin ediyorsunuz. NXM değerini neler etkiliyor, hemen bir sonraki bölümde değerlendireceğiz.

Bunun dışında NXM sahibi olarak tazminat isteyenlerin taleplerini değerlendirmek, az sonra bahsedeceğimiz çeşitli ürünlere direkt olarak yatırım yapmak ya da NXM yönetim sisteminde söz sahibi olmak (örneğin yeni çıkarılacak ürünleri belirlemek için yapılan oylamalara katılmak) gibi Nexus Mutual’a özel belli para kazandırıcı aktivitelerde yer almak da mümkün.

Bu arada bir konuyu tekrarlamakta fayda var. Her ne kadar merkeziyetsiz bir sistem olsa da Nexus Mutual’ın belli alanlarda kısıtları olduğunu belirtmiştik. Örneğin, NXM yalnızca Nexus Mutual’un kendi kurduğu platformda işlem görüyor. NXM satın almak isteyenler Nexus Mutual sistemine üye olmak zorundalar. Üye olmak için de müşterini tanı (KYC - Know your customer) işleminden geçmek gerekiyor. KYC işlemlerini yapan ise İngiltere merkezli ve lisanslı bir şirket.

### NXM fiyatı neye göre belirleniyor? {#nxm-fiyati-neye-gore-belirleniyor}

İşte Nexus Mutual’ın diğer merkeziyetsiz sistemlerden bir farkı daha. Nexus’un tokeni NXM’in değeri serbest piyasadaki arz ve talebe göre belirlenmiyor, zira NXM kriptopara borsalarında işlem gören bir token değil. Bunun yerine NXM’in fiyatı bir algoritma ile hesaplanıyor. Nasıl bir hesaplama bu?

Hatırlarsanız, [Uniswap kendi içinde basit bir algoritma kullanarak al-sat yapmak isteyenlere bir fiyat veriyordu](https://turansert.com/genel/2020/09/15/nedir-bu-uniswap.html). Bunu yaparken algoritmanın temel hedefi, ne olursa olsun işlem yapmak isteyenlere bir fiyat vermek idi. **Nexus Mutual algoritması da benzer şekilde işlem yapmak isteyenlere otomatik bir fiyat veriyor. Ama bunu yaparken hem arz ve talebi, hem de Nexus Mutual havuzunun finansal sağlığını korumaya çalışıyor**.

Nexus’un havuzunun olmazsa olmazı, potansiyel hasarlara karşı ödeme yapabilmek. **Bu nedenle havuzun içinde talepleri belirli oranda karşılayabilecek kadar kapital bulunması birincil hedef**. Bu kapital rakamı Avrupa Birliği’nin yeterlilik standartlarına göre belirleniyor. Eğer havuzun içinde o belirlenen minimum oran kadar para yoksa; öncelikle hiç kimse NXM satıp, ETH alamıyor (bu oranın adı MCR - minimum capital requirement, 'minimum karşılık' olarak düşünülebilirsiniz)[^1].

Algoritmanın ikinci amacı ise gelişen arz ve talebe göre NXM fiyatını ayarlayarak sistemi sağlıklı tutmak. Bunu da otomatik bir formülle yapıyor. Temel olarak şu şekilde çalışıyor:

Eğer havuzda toplanan para, minimum rakamın %30’undan fazlasına ulaşırsa, formül NXM fiyatını hızlı bir şekilde yükseltmeye başlıyor. Bunun nedeni, fiyat yükseldiğinde yatırımcıların ellerinde tuttukları NXM’yi satıp havuzdan ETH çekmesini sağlamak. Neden böyle yapıyor? Çünkü havuzda değerlendirilmeden duran para, verimsizlik göstergesi.

Bu arada, Nexus Mutual yönetiminin elde fazla kapital olması durumunda alacağı bir aksiyon daha var. O da yeni sigorta ürünleri çıkarmak. Bu sayede sistemi büyütebilirler. Yeni ürünler çıkması bu ürünler için de karşılık ayrılmasını gerektireceği için minimum karşılık oranını yani MCR’yi yükseltecek.

Yine aynı şekilde eğer havuzdaki para minimum rakama doğru yaklaşmaya başlarsa formüle göre NXM fiyatı hızlı bir şekilde düşmeye başlıyor. Mantık aynı: Eğer NXM’nin fiyatı ucuzlarsa, o zaman yatırımcılar çok daha ucuza havuzdan pay sahibi olmak hakkını kaçırmak istemeyecekler ve havuza ETH koyup NXM satın alacaklar. Böylece havuzdaki kapital yani ETH miktarı artacak.

Özetle algoritma dediğimiz bu basit formül sayesinde hedeflenen, NXM fiyatı ile oynayarak havuzdaki kapital miktarının belli bir bant içinde oynamasını sağlamak. Bu bandın altı, minimum karşılık oranı olan MCR, üstü ise MCR’nin %30 fazlası.

### Nasıl sigorta yapıyor kullanıcılar? {#nasil-sigorta-yapiyor-kullanicilar}

Üye olduktan sonra aslında çok da karmaşık değil. Kullanıcı farklı ürünlerden hangisine karşı kendisini korumak istiyor ise onu seçiyor, kaç gün ve ne kadarlık bir miktar için korunma istediğini belirliyor. Sistem kendisine bir oran veriyor. Burada kullanıcı ödemeyi dilerse NXM dilerse de ETH ile yapabiliyor.

<strong><em>Peki sigorta oranını kim nasıl belirliyor?</em></strong>

Sigorta oranını aslında Nexus Mutual yatırımcıları belirliyor. Bunu da rehin verme işlemi (İngilizcede ‘staking’) ile yapıyorlar.

Staking daha fazla risk karşılığı daha da fazla getiri almak isteyenler için kurulmuş bir sistem. Normalde Nexus Mutual’a yatırımcı olmak istediğinizde, havuzdan NXM satın alıyor ve tüm sistemin risk ve getirisine ortak oluyorsunuz. Staking yaptığınızdaysa bu riski ürün bazında ayrıştırmak da mümkün oluyor.

<figure><a href="/assets/books/sorularla-defi/208-2.jpeg"><img src="/assets/books/sorularla-defi/208-2.jpeg" alt="Image by Sarah Lötscher from Pixabay" width="1200" height="794" loading="lazy"></a><figcaption>Image by <a href="https://pixabay.com/users/sarah_loetscher-4248505/">Sarah Lötscher</a> from <a href="https://pixabay.com/">Pixabay</a></figcaption></figure>

NXM satın alan dolayısıyla genel sisteme yatırım yapmış bir yatırımcı, sonrasında dilerse bu NXM’yi belli bir spesifik ürüne koyarak riskini daha da artırabiliyor. Böyle yaparak bu spesifik ürünü satın almış olanların ödedikleri primlerden bir kısmını havuzdan önce kazanma hakkına sahip oluyor. Risk tarafında ise üründe bir sorun çıkıp da zarar tazminat ödenmesi hâlinde koymuş olduğu NXM’yi toptan kaybetme ihtimali var. Bu nedenle, staking yapmanın ekstra riskli bir yatırım olduğu unutulmamalı.

Aslına bakarsanız, staking akıllı kontratların risklerini anlayabilmek için güzel bir ipucu. Risk tutarı aynı görünen iki akıllı kontrattan birine diğerinin iki katı kadar staking yapılmışsa, bu birinci kontratın genel olarak çok daha az riskli görüldüğü anlamına gelebilir.

<strong><em>Bir sorun olduğunda ödeme yapılacağına kim karar veriyor?</em></strong>

Her ne kadar akıllı kontratlar var desek de ödemeler henüz otomatik yapılacak seviyeye gelmiş değil. Bunu DeFi’nin emekleme aşamasında olmasına bağlayabilirsiniz. Belki önümüzdeki dönemde orada da olabildiğince otomatize bir sistem olabilir. Bir sistem sorunu olduğu ve ödeme yapılması gerektiğine Nexus Mutual’a üye olanlar oylama ile karar veriyorlar. Eğer Nexus Mutual üyeleri (ellerinde NXM token tutanlar) sistemsel bir sorun olduğu ve ödeme yapılması gerektiği konusunda bir karar verirlerse, işte o zaman akıllı kontrat devreye girip ürün satın almış olan kullanıcılara tazminatlarını ödüyor.

<strong><em>Nasıl hasar talep ediliyor?</em></strong>

Herhangi bir hasar olayı olduğunda, ilgili üründen koruma almış olanlar, Nexus Mutual sitesine başvuruyorlar. Yapılan talep bir kısım NXM sahibi tarafından değerlendiriliyor. Burada ilginç bir nokta var: Talebi değerlendirenler ellerindeki NXM’leri sisteme kilitliyorlar. Kararların %70 çoğunluk ile verilmesi gerekiyor.[^2] Çoğunluk ile aynı yönde oy kullananlar ekstra NXM kazanıyor. Karşı oy kullananların ise NXM’leri bir süreliğine kilitli kalmaya devam ediyor ve incelemeye tabi tutuluyor. İnceleme sonucu kötü niyetli oldukları saptanırsa NXM’leri yakılıyor. Gördüğünüz gibi hasar talep sisteminin değerlendirilmesi hâlâ manuel şekilde oluyor denebilir (zira çoğunluğa karşı oy kullananları değerlendiren bir komite var, beş üyeden oluşan), çok da merkeziyetsiz sayılmaz şu aşamada.

<strong><em>Hiç hasar karşılama ödemesi yapmış mı Nexus Mutual?</em></strong>

Şimdiye kadar bir tek olayda ödeme yapılmış. 2020 Şubat ayında bzX sistemindeki bir açıktan dolayı oluşan hasarda Nexus Mutual üyeleri [iki adet koruma alan kullanıcı için toplam 35,000 ABD Doları’na yakın bir ödeme yapmışlar](https://medium.com/nexus-mutual/bzx-flash-loan-event-55753d19e52b). Şu ana kadar toplam 53 hasar talebi geldiğini ve sadece az önce bahsettiğimiz bZx hasarına ait üç talebin karşılandığını, 47 talebin reddedildiğini de hatırlatalım[^3]

## Önümüzdeki dönemde Nexus’u neler bekliyor? {#onumuzdeki-donemde-nexusu-neler-bekliyor}

Nexus özünde DeFi için yaratılmış bir proje. Başarısı için DeFi pazarının büyümesi gerekli. Daha farklı platformlar için yeni ürünler çıkarmaya devam etmeleri şart. Yine de asıl büyüme, farklı riskleri de kapsama alanı içine almaları durumunda olacak. Sadece kontrat hatalarına karşı kullanıcıları koruyarak gidebileceğiniz yol kısıtlı, üstelik kullanıcıların mevcut platformlarda zaman geçirdikçe kendilerini daha rahat hissedip platform riskine para ödemeyi bırakmaları da söz konusu olabilir. Yearn benzeri yapacakları ortaklıklar onların daha geniş kitleler tarafından kullanılmasını sağlayabilir.

Bunun yanında Nexus Mutual’ın olası riskleri karşılamak için elinde tuttuğu bir kapital var. Bu 2020 Ekim aylarında 200 bin ETH (yaklaşık 75 milyon ABD Doları) seviyesinde. Nexus şu aşamada bu havuzu ekstra yatırımlar için kullanmıyor. Bunun temel nedeni bu kapitali riske etmeden yapılacak yatırımların yeterli olgunluğa ulaşmamış olması. ETH 2.0 ile birlikte gelecek olan Proof of Stake, yani Ethereum sisteminin güvenliğini sağlamak amacıyla fonların kilitlenmesi süreci başladığında, Nexus Mutual için elindeki ETH’yi buraya koyarak ekstradan gelir kazanma ihtimali de doğacak.

Öte yandan her ne kadar merkeziyetsiz finans ürünü olsa da Nexus Mutual pek çok açıdan hâlâ merkezi sayılabilir. Örneğin, az önce bahsettiğimiz gibi sisteme üye olmak için KYC prosedürlerinden geçmeniz gerekiyor. Sistemi yürüten Nexus, İngiltere’de kurulu bir şirket. Kullanıcılar sistemin tokeni olan NXM’i alıp satmayı şu aşamada sadece Nexus üzerinde yapabiliyorlar. Öte yandan hasar taleplerinin değerlendirilmesi merkeziyetsiz bir şekilde Nexus yatırımcıları tarafından yapılsa da, bu yatırımcıların kurallara uyup uymadığını denetleyen bir merkezi Danışma Kurulu var. Bütün bunlar, Nexus Mutual’ın merkeziyetsiz olma yolunda önünde çözmesi gereken pek çok konu olduğunu gösteriyor.

[^1]: (bu oranın adı MCR - minimum capital requirement oranı). 𝑇𝑃 = 𝐴 + (𝑀𝐶𝑅𝐸𝑇𝐻/𝐶)∙ 𝑀𝐶𝑅%4

[^2]: Yapılan oylamada verilen karar %70 çoğunluk ile alınmalı - aksi takdirde tüm sistem tarafından bir oylama daha yapılıyor.

[^3]: Üç adet talep henüz değerlendirme aşamasında
