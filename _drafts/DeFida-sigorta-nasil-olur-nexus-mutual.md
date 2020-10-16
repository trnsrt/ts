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

Nexus Mutual havuzu da şimdilik iki paradan oluşuyor. Bunlardan biri Nexus'un kendi parası NXM, diğeri ise Ethereum'un parası ETH. Bu havuz risklerin ve getirilerin paylaşıldığı bir havuz aslında. Öncelikle, NXM'iniz yok ise, gelip bu havuza ETH koyup NXM almalısınız. 

Kim niye NXM alsın? İki neden var. Öncelikle sigorta yaptırmak, pardon Akıllı Kontratlar'a karşı koruma satın almak istiyorsanız, NXM'iniz olmalı [BUNU KONTROL EDELİM!!!!]. Yaptırmak istediğiniz sigorta miktarı ve süresine bağlı olarak NXM yakmanız gerekiyor. Yani sigorta primi ödemenin benzeri. Koruma yaptırmak için NXM'niz olacak, NXM'i de havuzdan ETH karşılığı alacaksınız, yani primi ETH ile ödüyorsunuz. 

Diğer bir neden ise NXM'i yatırım olarak almak. Sigorta yaptırmak isteyenler gelip bu havuzdan satın alacaklar - bu da NXM'e olan talebi ve fiyatını artıracak. 

#### Sigortacının havuzu başka olur... 

Aslında sistemin klasik sigortacılıktan çok da farkı yok. Normalde sigorta şirketleri aldıkları toplam riskin tamamı değil bir kısmı kadar kapital tutarlar. Herhangi bir riskin gerçekleşmesi durumunda hasar bu kapitalden ödenir. Risklere karşı ödenen sigorta primleri de bu kapitale eklenir. Burada da yukarıda bahsettiğimiz havuz aslında Nexus sisteminin kapitali. Bu kapitali bireysel yatırımcılar sağlıyor. Zararlar yani hasarlar buradan ödeniyor. Sigorta primleri de kâr olarak bu havuza konuyor. 

Tabii bu havuzun klasik bankacılığa göre belli farklılıkları ve zorlukları var. Bunun en önemlisi havuzdaki kapital ile karşılanan risk oranında bir denge tutturabilmek. Zira, havuzda kapital az, ama risk fazla olursa sistemin çökme riski olabilir. Tam tersi bir durumda kapitalin çok fazla olması durumunda ise yeterli sigorta prim getirisi olmayacağı için kapitalin verimli kullanılamaması gibi bir durum söz konusu olabiliyor. 

Sistem çökme riski olmaması için havuzdaki kapitalin toplam riskin belli bir oranının altına inmemesi gibi bir kural var. Bu oran %30 olarak belirlenmiş. Eğer toplam kapital bu rakamın altına inerse, sistem yatırımcıların kapital çekme isteklerini karşılamıyor. 

Öte yandan sistemde ekstra kapital olması durumunda da, Nexus ekibi yeni ürünler çıkararak sistemi büyütme yoluna gidiyorlar. Yeni ürün çıkması, bu ürünleri kullanarak kendilerini sigortalamak isteyenlerin olması nedeniyle toplam riskin artması anlamına geliyor. Bu da minimum kapital rakamını (%30'u) yukarı çekiyor. Yani ekstra kapital yeni yatırım için kullanılmış oluyor. Ekstra kapital miktarı minimum kapitalden %30 fazla olacak şekilde belirlenmiş. 

Dolayısıyla, havuz öyle bir şekilde dizayn edilmiş ki, havuzdaki kapital minimum kapital ile onun %30 fazlası arasındaki bantta oynuyor. Nasıl dizayn etmişler bunu? Uniswap'ta olduğu gibi bir algoritma kullanıyorlar ama daha karmaşık bir algoritma. 

Buna göre eğer havuzdaki kapital miktarı minimum kapitale doğru yaklaşırsa NXM miktarını dramatik bir şekilde düşürüyorlar. Bu sayede, NXM'in fiyatının çok düştüğünü gören yatırımcılar ucuza alım fırsatı olduğunu düşünerek sisteme ETH koyuyorlar. 

Keza benzer şekilde eğer Nexus sistemindeki kapital çok artar ise o zaman da NXM'in fiyatı hızla yükseliyor. Bu da benzer şekilde yatırımcıların bu artışı değerlendirmek için NXM satmalarına neden oluyor - sistem yeniden dengeye geliyor.  

Bu arada bir konuyu aydınlatmakta fayda var: Her ne kadar merkeziyetsiz bir sistem olsa da Nexus Mutual'ın belli alanlarda kısıtları olduğunu belirtelim. Örneğin, NXM yalnızca Nexus Mutual'un kendi kurduğu platformda işlem görüyor. NXM satın alabilmek için Nexus Mutual sistemine üye olmak zorundasınız. Üye olmak için de müşterini tanı (KYC - Know your customer) işleminden geçmeniz gerekiyor.  

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






-- 


### Nexus Mutual başarısı

Nexus Mutual 2020 yılı başlarında yaklaşık 1.5 milyon ABD Doları bir koruma sağlarken, bugün bu rakam 
