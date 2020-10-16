Bu yazımızda DeFi dünyasında sigorta sistemi nasıl olur, neleri kapsar, nasıl çalışır Nexus Mutual üzerinden bakmaya çalışalım. 


DeFi yani merkeziyetsiz finans kendi içinde bir dünya olmaya doğru hızla ilerliyor. Her ne kadar klasik finans dünyası ile belli alanlarda keşisse de, sistemin kendi içinde fiziksel dünyaya olan bağımlılığını en aza indirecek girişimler de hemen ortaya çıkıyor.

İşte bu gereksinimlerden en önemlilerinden biri de sigorta. Ne kastediyoruz sigorta derken? Öncelikle hep tekrar ettiğimiz şu düsturu unutmamak gerek: Klasik finans emanet (custodian) sistemi çalışır. Yani siz müşteri olarak finansal varlığınızı çalıştığınız kuruma kuzu kuzu verirsiniz. Zaten bu nedenle finans sektöründe çok sıkı regülasyonlar var - kanun koyucular halkın hakkını korumak için sektörü sıkı kontrol altında tutuyorlar. DeFi emanetsiz/velayetsiz (non-custodial) bir sistem ile çalışır. Yani, bu kripto dünyasında varlıklarınız tam anlamıyla sahipsiniz, ama elinizden gittiğinde de "yandı gülüm keten helva".. 

Emanetsiz/velayetsiz olma özelliği kullanıcılar için bir yandan finansal özgürlük getiriyor ama bir yandan da onları büyük bir sorumluluk altına sokuyor. Zaten yeterince karışık ve teknik olan bir konuda böyle bir sorumluluk riski aslında DeFi'nin geniş kesimlere adaptasyonunun önündeki en büyük engellerden bir tanesi. 

Halbuki DeFi sistemini teknik olarak anlayanlar için aslında bu dünyadaki risk, gerçek dünyadaki merkezi finansa göre daha az. İşte tam da bu noktada bir arbitraj ihtimali doğuyor. Teknik olarak olaya hakim olmayanlar bu riskleri almamak pahasına ekstra ücret ödemeye razı olabilir. Konuya hakim olanlar ise bu ekstra ücret karşılığı o riski almak isteyebilir. İşte sigortacılığın temel ilkesi - risk algısındaki fark ve riski dağıtma. 

### DeFi'da sigorta sisteminin mantığı nasıl?
DeFi dünyasındaki sigorta sisteminin aslında fiziki dünyadan çok da farkı yok. En basit anlatımı ile projelerdeki teknik riskleri almak istemeyen kullanıcıların alacakları sigortalar karşılığında kendilerini sağlama almaları. Masanın öbür tarafında ise, bu riskleri almak isteyen kullanıcıların çıkarılan sigorta primlerini alabilmek için ekstra risklerin altına girip olası riskin gerçekleşme ihtimaline karşı belli teminatlar vermeleri. 

DeFi'da pekçok işlemin merkeziyetsiz yapılabilmesini sağlayan Akıllı Kontratlar burada da devrede. Ne diyoruz hep: Bu dünyada kod kanun. Hangi durumlarda sigortanın geçerli olduğu baştan belli ve taraflarca kabul edildikten sonra, Akıllı Kontrat'ın yaptığı konu edilen olayın gerçekleşmesi durumunda zarar görene ödeme yapmak. Olayın önceden belirlenen süre içinde gerçekleşmemesi durumunda da diğer partiye risk primini ödemek. 

#### Neler sigortalanıyor, neler sigorta dışı?

Belki burada şunu da belirtmekte fayda var. Neler sigorta ediliyor derseniz, temel olarak token satın alan bir kullanıcının, yatırım yaptığı projedeki teknik risklerden dolayı oluşacak zararlar diyebiliriz. Nedir bunlar? Örneğin, Akıllı Kontratın yazılımındaki bir hatadan dolayı dış dünyadan kimi aktörler sistemde kilitli olan tüm parayı çekebilirler. Sigorta işte böyle bir durumda kullanıcının satın aldığı token kadar bir miktarı onun cüzdanına gönderiyor. 

Şu aşamada Nexus sigortasının yaptığı sadece bu. Hep söylediğimiz gibi DeFi henüz emekleme aşamasında, bu alandaki ürünler de benzer şekilde yeni yeni çıkıyor ortaya. Nexus, farklı alanlardaki riskleri kapsayacak farklı ürünler üzerinden çalıştığını söylüyor. Neler olabilir bunlar dediğimizde yine [Nexus'a kulak vermekte fayda var](https://bankless.substack.com/p/how-to-assess-the-risk-of-lending). 

Dış riskler: Özellikle kodun düzgün çalıştığı (kod hatası içermeyen) ancak yine de sistemin sorun çıkarabileceği alanlar. Örneğin, sisteme bilgi veren dış kaynaklarda (oracle da dediğimiz) oluşabilecek sorunlar, daha detaya girersek dış kaynaktan sisteme yanlış bilgi gelmesi. Ya da DeFi sistemlerinin yönetim yapıları yeni yeni oturmaya başlıyor, burada çıkabilecek sorunlar. Bir başkası, platformların verdiği yönetim ile ilgili teşviklerin kimi kullanıcılar için özendirici olurken bu kullanıcıların aldığı aksiyonların diğer başka kullanıcılar için en uygun çözüm olmaması gibi. İşte bu tip koda dayanmayan hataları karşılayacak bir sigorta henüz yok. 


### Peki nasıl çalışıyor Nexus sistemi?
Nexus Mutual kendisine sigorta demiyor - bunun en önemli nedeni kanuni olarak sigorta mevzuatına takılmamak. Bunun yerine Akıllı Kontratlarda çıkabilecek açıklara karşı "koruma" sağladıklarını belirtiyorlar. 

Sistemin çalışması aslında bir havuz şeklinde. Evet, [daha önceki Uniswap yazımızda bahsettiğimiz havuz sistemi](/genel/2020/09/15/nedir-bu-uniswap.html) burada da geçerli. Hatırlarsak, Uniswap'da iki bölmeli iki paradan oluşan havuzlar vardı. Alım satım yapanlar havuzdaki bir paradan aldıklarında yerine orada bulunan diğer parayı bırakıyorlardı. Buradaki havuzun çalışma prensipleri ise bir parça farklı. 

Nexus Mutual havuzu da şimdilik iki paradan oluşuyor. Bunlardan biri Nexus'un kendi parası NXM, diğeri ise Ethereum'un parası ETH. 




Basitçe çalışma bu şekilde. Gelin Nexus Mutual özelinde sistem nasıl çalışıyor daha detaylı bakalım: 






-- 

Riskler sınırlı
