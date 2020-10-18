Bu yazımızda DeFi dünyasında sigorta sistemi nasıl olur, neleri kapsar, nasıl çalışır Nexus Mutual üzerinden bakmaya çalışalım. 


DeFi yani merkeziyetsiz finans kendi içinde bir dünya olmaya doğru hızla ilerliyor. Her ne kadar klasik finans dünyası ile belli alanlarda keşisse de, sistemin kendi içinde fiziksel dünyaya olan bağımlılığını en aza indirecek girişimler de hemen ortaya çıkıyor.

İşte bu gereksinimlerden en önemlilerinden biri de sigorta. Ne kastediyoruz sigorta derken? Öncelikle hep tekrar ettiğimiz şu düsturu unutmamak gerek: Klasik finans emanet (custodian) sistemi çalışır. Yani siz müşteri olarak finansal varlığınızı çalıştığınız kuruma kuzu kuzu verirsiniz. Zaten bu nedenle finans sektöründe çok sıkı regülasyonlar var - kanun koyucular halkın hakkını korumak için sektörü sıkı kontrol altında tutuyorlar. DeFi emanetsiz/velayetsiz (non-custodial) bir sistem ile çalışır. Yani, bu kripto dünyasında varlıklarınız tam anlamıyla sahipsiniz, ama elinizden gittiğinde de "yandı gülüm keten helva".. 

Emanetsiz/velayetsiz olma özelliği kullanıcılar için bir yandan finansal özgürlük getiriyor ama bir yandan da onları büyük bir sorumluluk altına sokuyor. Zaten yeterince karışık ve teknik olan bir konuda böyle bir sorumluluk riski aslında DeFi'nin geniş kesimlere adaptasyonunun önündeki en büyük engellerden bir tanesi. 

Halbuki DeFi sistemini teknik olarak anlayanlar için aslında bu dünyadaki risk, gerçek dünyadaki merkezi finansa göre daha az. İşte tam da bu noktada bir arbitraj ihtimali doğuyor. Teknik olarak olaya hakim olmayanlar bu riskleri almamak pahasına ekstra ücret ödemeye razı olabilir. Konuya hakim olanlar ise bu ekstra ücret karşılığı o riski almak isteyebilir. İşte sigortacılığın temel ilkesi - risk algısındaki fark ve riski dağıtma. 

### DeFi'da sigorta sisteminin mantığı nasıl?
DeFi dünyasındaki sigorta sisteminin aslında fiziki dünyadan çok da farkı yok. En basit anlatımı ile projelerdeki teknik riskleri almak istemeyen kullanıcıların alacakları sigorta karşılığında kendilerini sağlama almaları (sigorta alanlara kısaca "kullanıcılar" diyelim). Masanın öbür tarafında ise, bahsedilen riski almaya hazır "yatırımcılar" var. 

DeFi'da pekçok işlemin merkeziyetsiz yapılabilmesini sağlayan Akıllı Kontratlar burada da devrede. Ne diyoruz hep: Bu dünyada kod kanun. Hangi durumlarda sigortanın geçerli olduğu baştan belli ve taraflarca kabul edildikten sonra, Akıllı Kontrat'ın yaptığı konu edilen olayın gerçekleşmesi durumunda zarar görene ödeme yapmak. Olayın önceden belirlenen süre içinde gerçekleşmemesi durumunda da diğer partiye risk primini ödemek. 

#### Neler sigortalanıyor, neler sigorta dışı?

Belki burada şunu da belirtmekte fayda var. Neler sigorta ediliyor derseniz, temel olarak token satın alan bir kullanıcının, yatırım yaptığı projedeki teknik risklerden dolayı oluşacak zararlar diyebiliriz. Nedir bunlar? Örneğin, Akıllı Kontratın yazılımındaki bir hatadan dolayı dış dünyadan kimi aktörler sistemde kilitli olan tüm parayı çekebilirler. Sigorta işte böyle bir durumda kullanıcının satın aldığı token kadar bir miktarı onun cüzdanına gönderiyor. 

Şu aşamada Nexus sigortasının yaptığı sadece bu. Hep söylediğimiz gibi DeFi henüz emekleme aşamasında, bu alandaki ürünler de benzer şekilde yeni yeni çıkıyor ortaya. Nexus, farklı alanlardaki riskleri kapsayacak farklı ürünler üzerinden çalıştığını söylüyor. Neler olabilir bunlar dediğimizde yine [Nexus'a kulak vermekte fayda var](https://bankless.substack.com/p/how-to-assess-the-risk-of-lending). 

Dış riskler: Özellikle kodun düzgün çalıştığı (kod hatası içermeyen) ancak yine de sistemin sorun çıkarabileceği alanlar. Örneğin, sisteme bilgi veren dış kaynaklarda (oracle da dediğimiz) oluşabilecek sorunlar, daha detaya girersek dış kaynaktan sisteme yanlış bilgi gelmesi. Ya da DeFi sistemlerinin yönetim yapıları yeni yeni oturmaya başlıyor, burada çıkabilecek sorunlar. Bir başkası, platformların verdiği yönetim ile ilgili teşviklerin kimi kullanıcılar için özendirici olurken bu kullanıcıların aldığı aksiyonların diğer başka kullanıcılar için en uygun çözüm olmaması gibi. İşte bu tip koda dayanmayan hataları karşılayacak bir sigorta henüz yok. 


### Peki nasıl çalışıyor Nexus sistemi?
Nexus Mutual kendisine sigorta demiyor - bunun en önemli nedeni kanuni olarak sigorta mevzuatına takılmamak. Bunun yerine Akıllı Kontratlarda çıkabilecek açıklara karşı "koruma" sağladıklarını belirtiyorlar. 

#### Havuz problemleri yine karşımızda... 

Sistemin çalışması aslında bir havuz şeklinde. Evet, [daha önceki Uniswap yazımızda bahsettiğimiz havuz sistemi](/genel/2020/09/15/nedir-bu-uniswap.html) burada da geçerli. Hatırlarsak, Uniswap'da iki bölmeli iki paradan oluşan havuzlar vardı. Alım satım yapanlar havuzdaki bir paradan aldıklarında yerine orada bulunan diğer parayı bırakıyorlardı. Buradaki havuzun çalışma prensipleri ise bir parça farklı. 

Öncelikle Nexus Mutual'in havuzu, aslında alınan risklere karşılık ödenebilecek kapital rakamını gösteriyor. Havuzda para ETH olarak tutuluyor. Dolayısıyla Nexus Mutual dünyasının temeli ETH'e dayanıyor, en azından şimdilik. Bu da anlaşılır, zira koruma verdikleri ürünlerin çoğunluğu da Ethereum üzerinden işlem yaptıkları için risk ETH, bu riske karşı fonları da ETH değerlendirmek mantıklı. 

Havuzun sahibi tüm üyeler. Nasıl sahip oluyor bu havuza? Aynı hisse senedinde olduğu gibi havuzun sahipliğini gösteren sistemin parası NXM ile. Dolayısı ile NXM sahibi olmak hem havuzun riskini hem de getirisini paylaşmak demek. 

Peki NXM fiyatı nasıl belirleniyor?

#### Kim niye NXM alsın? 
Birkaç neden var. 

Öncelikle sigorta yaptırmak, pardon "Akıllı Kontratlar'a karşı koruma satın almak" istiyorsanız bunu NXM ile yapıyorsunuz.  Yaptırmak istediğiniz sigorta miktarı ve süresine bağlı olarak aldığınız korumanın ücretini NXM olarak veriyorsunuz (burada NXM yakıyorsunuz). Yani sigorta primi ödemenin benzeri. Koruma yaptırmak için NXM'niz olacak, NXM'i de havuzdan ETH karşılığı alacaksınız, yani primi bir nevi ETH ile ödüyorsunuz. 

İkincisi ise yatırım olarak almak. Sonuç olarak NXM aldığınızda havuzdan sahiplik alıyorsunuz. Havuzdan koruma almak için havuza ETH koyup NXM almak ve NXM yakmak gerekiyor demiştik, dolayısıyla poliçe almak havuzdaki ETH'yi çoğaltıp, havuzun sahipliği olan NXM'i azaltmış oluyor, bunun da MXM fiyatına pozitif etkisi oluyor. 

#### NXM fiyatı neye göre belirleniyor?

İşte Nexus Mutual'ın diğer merkeziyetsiz sistemlerden bir farkı daha. Nexus'un tokeni NXM'in değeri serbest piyasadaki alım satıma göre belirlenmiyor, zira NXM merkezi ya da merkezi olmayan borsalarda işlem gören bir token değil. Bunun yerine NXM'in fiyatı bir algoritma ile belirleniyor. 

Hatırlarsanız, Uniswap kendi içinde basit bir algoritma kullanarak al-sat yapmak isteyenlere bir fiyat veriyordu. Bunu yaparken algoritmanın temel hedefi, ne olursa olsun işlem yapmak isteyenlere bir fiyat vermek idi. Nexus Mutual algoritması da benzer şekilde işlem yapmak isteyenlere otomatik bir fiyat veriyor. Ama bunu yaparken hem arz ve talebi, hem de Nexus Mutual havuzunun finansal sağlığını korumaya çalışıyor. Gelin nasıl oluyor biraz daha detaylı bakalım: 

Nexux'un havuzunun temel amacı olası hasarlara karşı ödeme yapabilmek - bu sistemin olmazsa olması. Bu nedenle havuzun temel amacı içinde talepleri belirli oranda karşılayabilecek kadar kapital bulunması birinci hedef. Eğer havuzun içinde o belirlenen minimum oran kadar para yoksa öncelikle hiç kimse NXM satıp ETH alamıyor (bu oranın adı MCR - minimum capital requirement, mininum karşılık olarak düşünülebilir)[^3]. 

Sonrasında ise algoritmanın amacı, NXM fiyatını gelişen arz ve talebe göre sistemi sağlıklı tutacak şekilde ayarlamak. Bunu da otomatik bir formül ile yapıyor[^4]. Bu da şu şekilde oluyor: 

Eğer havuzda toplanan para minimum rakamın %30'dan fazlasına ulaşırsa, formül NXM fiyatını hızlı bir şekilde yükseltmeye başlıyor. Bunun nedeni yüksek NXM fiyatı olduğunda, elinde NXM tutan yatırımcıların NXM satıp havuzdan ETH çekmesini sağlamak. Neden böyle yapıyor? Çünkü havuzda değerlendirilmeden duran para, verimsizlik göstergesi. 

Bu arada, Nexus Mutual yönetiminin elde fazla kapital olması durumunda alacağı bir aksiyon daha var. O da yeni sigorta ürünleri çıkarmak. Bu sayede sistemi büyütebilirler. Yeni ürünler çıkması insanların bu ürünler için de karşılık ayrılmasını gerektireceği için minumum karşılık oranını yükseltecek. 

Yine aynı şekilde 


Havuzdaki toplam değere ETH cinsinden bakılıyor. Dolayısıyla Nexus Mutual dünyasının temeli ETH'e dayanıyor, en azından şimdilik. Bu da anlaşılır, zira koruma verdikleri ürünlerin çoğunluğu da Ethereum üzerinden işlem yaptıkları için risk ETH, bu riske karşı fonları da ETH değerlendirmek mantıklı. 

#### Sigortacının havuzu başka olur... 

Havuzda 

Aslında sistemin klasik sigortacılıktan çok da farkı yok. Normalde sigorta şirketleri aldıkları toplam riskin tamamı değil bir kısmı kadar kapital tutarlar. Herhangi bir riskin gerçekleşmesi durumunda hasar bu kapitalden ödenir. Risklere karşı ödenen sigorta primleri de bu kapitale eklenir. Burada da yukarıda bahsettiğimiz havuz aslında Nexus sisteminin kapitali. Bu kapitali bireysel yatırımcılar sağlıyor. Zararlar yani hasarlar buradan ödeniyor. Sigorta primleri de kâr olarak bu havuza konuyor. 

Tabii bu havuzun klasik bankacılığa göre belli farklılıkları ve zorlukları var. Bunun en önemlisi havuzdaki kapital ile karşılanan risk oranında bir denge tutturabilmek. Zira, havuzda kapital az, ama risk fazla olursa sistemin çökme riski olabilir. Tam tersi bir durumda kapitalin çok fazla olması durumunda ise yeterli sigorta prim getirisi olmayacağı için kapitalin verimli kullanılamaması gibi bir durum söz konusu olabiliyor. 

Sistem çökme riski olmaması için havuzdaki kapitalin toplam riskin belli bir oranının altına inmemesi gibi bir kural var. Bu oran %30 olarak belirlenmiş. Eğer toplam kapital bu rakamın altına inerse, sistem yatırımcıların kapital çekme isteklerini karşılamıyor. 

Öte yandan sistemde ekstra kapital olması durumunda da, Nexus ekibi yeni ürünler çıkararak sistemi büyütme yoluna gidiyorlar. Yeni ürün çıkması, bu ürünleri kullanarak kendilerini sigortalamak isteyenlerin olması nedeniyle toplam riskin artması anlamına geliyor. Bu da minimum kapital rakamını (%30'u) yukarı çekiyor. Yani ekstra kapital yeni yatırım için kullanılmış oluyor. Ekstra kapital miktarı minimum kapitalden %30 fazla olacak şekilde belirlenmiş. 

Dolayısıyla, havuz öyle bir şekilde dizayn edilmiş ki, havuzdaki kapital minimum kapital ile onun %30 fazlası arasındaki bantta oynuyor. Nasıl dizayn etmişler bunu? Uniswap'ta olduğu gibi bir algoritma kullanıyorlar ama daha karmaşık bir algoritma. 

Buna göre eğer havuzdaki kapital miktarı minimum kapitale doğru yaklaşırsa NXM miktarını dramatik bir şekilde düşürüyorlar. Bu sayede, NXM'in fiyatının çok düştüğünü gören yatırımcılar ucuza alım fırsatı olduğunu düşünerek sisteme ETH koyuyorlar. 

Keza benzer şekilde eğer Nexus sistemindeki kapital çok artar ise o zaman da NXM'in fiyatı hızla yükseliyor. Bu da benzer şekilde yatırımcıların bu artışı değerlendirmek için NXM satmalarına neden oluyor - sistem yeniden dengeye geliyor.  

Bu arada bir konuyu aydınlatmakta fayda var: Her ne kadar merkeziyetsiz bir sistem olsa da Nexus Mutual'ın belli alanlarda kısıtları olduğunu belirtelim. Örneğin, NXM yalnızca Nexus Mutual'un kendi kurduğu platformda işlem görüyor. NXM satın alabilmek için Nexus Mutual sistemine üye olmak zorundasınız. Üye olmak için de müşterini tanı (KYC - Know your customer) işleminden geçmeniz gerekiyor.  KYC işlemlerini yapan Nexus Mutual kurucularının girişimi İngiltere merkezli ve lisanslı bir şirket. 

#### Nasıl sigorta yapıyorsunuz?
Üye olduktan sonra aslında çok da karmaşık değil. Kullanıcı farklı ürünlerden hangisine karşı kendisini korumak istiyor ise onu seçiyor, kaç gün için ve ne kadarlık bir miktar için korunma istediğini belirliyor. Sistem kendisine bir oran veriyor. Burada kullanıcı ödemeyi dilerse NXM dilerse ise ETH ile yapabiliyor. 

Peki bu oranı kim nasıl belirliyor?


Bir sorun olduğunda ödeme yapılacağına kim karar veriyor?
Her ne kadar Akıllı Kontratlar var desek de, ödemeler henüz otomatik yapılacak seviyeye gelmiş değil. Bunu DeFi'nin emekleme aşamasında olmasına bağlayabilirsiniz - belki önümüzdeki dönemde orada da olabildiğince otomatize bir sistem olabilir. Bir sistem sorunu olduğu ve ödeme yapılması gerektiğine Nexus Mutual'a üye olanlar oylama ile karar veriyorlar. Eğer Nexus Mutual üyeleri (ellerinde NXM token tutanlar) sistemsel bir sorun olduğu ve ödeme yapılması gerektiği konusunda bir karar verirlerse işte o zaman Akıllı Kontratlar devreye girip ürün satın almış olan kullanıcılara tazminatlarını ödüyorlar. 


### Başka ne özellikler var?

### Staking

Başka pek çok platformda da gördüğümüz tokenlarını rehin verme işlemi Nexus Mutual'da da var. Staking daha fazla risk karşılığı daha da fazla getiri almak isteyenler için kurulmuş bir sistem. Normal Nexus Mutual'a yatırımcı olmak istediğinizde, havuzdan NXM satın alıyor ve tüm sistem risk ve getirisine ortak oluyorsunuz. Ancak staking yaptığınızda bu yatırımı ürün bazında ayrıştırmak mümkün. NXM satın alan genel sisteme yatırım yapmış bir yatırımcı sonrasında dilerse bu NXM'i ile belli bir spesifik ürüne koyarak riskini daha da artırabiliyor. Böyle yaparak bu spesifik ürünü satın almış olanların ödedikleri primlerden bir kısmını havuzdan önce kazanma hakkına sahip oluyor. Risk tarafında ise üründe bir sorun çıkıp da zarar tazminat ödenmesi halinde koymuş olduğu NXM'i toptan kaybetme ihtimali de var. Bu nedenle, ekstra bir riskli ürün olduğu unutulmamalı. 

Aslına bakarsanız, staking bir nevi spesifik Akıllı Kontratların risklerini anlayabilmek için güzel bir endikatör aynı zamanda. Riskleri (yani sigorta yapılmış tutarları) aynı olan iki Akıllı Kontrat'tan birine diğerinin iki katı kadar staking yapılmışsa, bu birinci kontratın genel olarak çok daha az riskli görüldüğü anlamına gelebilir. 


Basitçe çalışma bu şekilde. Gelin Nexus Mutual özelinde sistem nasıl çalışıyor daha detaylı bakalım: 

#### Nasıl hasar talep ediliyor?

Herhangi bir hasar olayı olduğunda, ilgili üründen koruma almış olanlar, Nexus Mutual sitesine başvuruyorlar. Yapılan talep bir kısım NXM sahibi tarafından değerlendiriliyor. Burada ilginç bir nokta var: Talebi değerlendirenler ellerindeki NXM'leri sisteme kilitliyorlar. Kararların %70 çoğunluk ile verilmesi gerekiyor[^1]. Çoğunluk ile oy kullananlar ekstra NXM kazanıyor. Karşı oy kullananların ise NXM'leri bir süreliğine kilitli kalmaya devam ediyor ve incelemeye tabi tutuluyor. İnceleme sonucu kötü niyetli oldukları saptanırsa NXM'leri yakılıyor. Gördüğünüz gibi hasar talep sisteminin değerlendirilmesi hâlâ manuel şekilde oluyor denebilir. Çoğunluğa karşı oy kullananları değerlendiren bir komite var beş üyeden oluşan - çok da merkeziyetsiz sayılmaz şu aşamada. 


#### Hiç hasar karşılama ödemesi yapmış mı Nexus Mutual?

Şimdiye kadar bir durumda ödeme yapılmış. 2020 Şubat ayında [bzX sistemindeki bir açıktan dolayı oluşan hasarda](https://bzx.network/blog/postmortem-ethdenver) Nexus Mutual üyeleri [iki adet koruma alan kullanıcının için toplam 35,000 ABD Doları'na yakın bir ödeme yapmışlar](https://medium.com/nexus-mutual/bzx-flash-loan-event-55753d19e52b). Şu ana kadar toplam 53 hasar talebi geldiğini ve sadece az önce bahsettiğimiz bZx hasarına ait üç talebin karşılandığını, 47 talebin reddedildiğini de hatırlatalım[^2]




#### yEarn ve NFT'ler
Nexus Mutual'un sigortasının başarısı diğer projelerin de ilgisini çekti. Örneğin bu satırlarda sıkça bahsettiğimiz merkeziyetsiz portföy yönetim platformu yEarn, Nexus Mutual sigortalarını kullanarak [yinsure](https://yinsure.finance/) adında bir ürün çıkardı. Benzer şekilde tekil tokenların bulunduğu Rarible platformunda da yNFT denen NXM'e bağlı tokenlar işlem görmeye başladı - farklı Nexus ürünleri ve farklı vadeler için farklı tokenlar yaratıldı.  Benzer şekilde [daha önce bir yazımızda bahsettiğimiz ETC pazarlarında işlem gören BTC](https://turansert.com/genel/2020/07/09/eth-gorunumlu-btc-olur-mu.html)'lerde olduğu gibi ETH tokeni gibi işlem gören WNXM'ler de çıkarıldı. 

Yukarıdaki üç örneğin de çıkış sebebi aslında basit: NXM üyeleri tarafından alınıp satılabilen dolayısıyla KYC prosedürlerine sahip bir token. Merkeziyetsiz Finans dünyasının kullanıcıların gizliliği konusunda hassas olan kesimlerine hitap edemiyor. Bu ürünler [KYC olmadan sigorta alınabilmeye olanak sağlıyor](https://cryptobriefing.com/nexus-mutual-just-ran-out-defi-coverage-heres-why/). 


-- 


### Nexus Mutual başarısı

Nexus Mutual 2020 yılı başlarında yaklaşık 1.5 milyon ABD Doları bir koruma sağlarken, Ekim aylarına geldiğimizde bu rakam 200 milyon ABD Doları'nı geçmiş durumda. Bunun temel nedeni doğal olarak 2020 yazında hareketlenmeye başlayan DeFi piyasası. İngilizce'de FOMO (Fear-of-Missing-Out) olarak adlandırılan, bir şeyleri kaçırıyor duygusunun da etkisi ile bu alana giren bireysel yatırımcılar sayesinde katlanarak artan pazar. Piyasa yeni giren yatırımcıların teknik olarak yetersiz olmaları Nexus benzeri sigortalara olan ilgiyi artırdı. Keza sonrasında getiri çiftçiliği olarak adlandırılan 'yield farming'in Ağustos ve Eylül aylarından arşa çıkması, tokenlarını platformlara emanet eden yatırımcıların duydukları tedirginlik Nexus ürünlerine talebi tetikledi. 

#### Nexus'un önümüzdeki dönemde başarılı olması için neler gerekli?

Nexus'un özünde DeFi için yaratılmış bir proje. Başarısı için DeFi pazarının büyümesi gerekli. Daha farklı platformlar için yeni ürünler çıkarmaya devam etmeleri gerekiyor. Ama asıl büyümeyi, farklı riskleri de kapsama alanı için almaları durumunda olacak - yalnızca kontrat hatalarına karşı kullanıcıları koruyarak gidebileceğiniz yol kısıtlı - üstelik mevcut platformların kullanım süreleri arttıkça kullanıcılar daha rahat edip, platform riskine para ödemeyip üzerlerine almak isteyebilirler. 

Bunun yanında Nexus Mutual'ın olası risklere karşılamak için elinde tuttuğu bir kapital vaar demiştik - bu 2020 Ekim aylarında  200 bin ETH civarinda - yaklaşık 70 milyon ABD Doları seviyesinde. Nexus şu aşamada bu havuzu ekstra yatırımlar için kullanmıyor. Bunun temel nedeni bu kapitali riske etmeden yapılacak yatırımların yeterli olgunluğa ulaşmamış olması. ETH 2.0 ile birlikte gelecek olan Proof of Stake, yani Ethereum sisteminin güvenliğini sağlamak amacıyla fonların kilitlenmesi süreci başladığında, Nexus Mutual için ellerindeki ETH koyarak ekstradan gelir kazanma ihtimali de doğacak. 

Öte yandan yEarn benzeri yapacakları ortaklıklar da onların daha geniş kitleler tarafından tanınmasını sağlayacak. 


---


[^1] Yapılan oylamada verilen karar %70 çoğunluk ile alınmalı - aksi takdirde tüm sistem tarafından bir oylama daha yapılıyor. 
[^2] Üç adet talep henüz değerlendirme aşamasında
[^3] (bu oranın adı MCR - minimum capital requirement oranı). 𝑇𝑃 = 𝐴 + (𝑀𝐶𝑅𝐸𝑇𝐻/𝐶)∙ 𝑀𝐶𝑅%4

---
Kaynaklar: 

https://cryptobriefing.com/defi-review-what-is-nexus-mutual-introduction-nxm/
https://cryptobriefing.com/nexus-mutual-just-ran-out-defi-coverage-heres-why/
