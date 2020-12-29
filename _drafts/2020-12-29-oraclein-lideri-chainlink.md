---
layout: post
title:  "Oracle dünyasının lideri Chainlink"
date:   2020-12-29 16:47:56 +0300
categories: Genel
tags: Yazılar DeFi
---

Bir önceki yazımızda, Merkeziyetsiz Finans (DeFi) piyasasına bilgi sağlayan [oracle (uzman/kahin) servis sağlayıcılardan bahsetmiş](/genel/2020/12/22/definin-bilgi-kaynagi-oracle.html), bu piyasanın tartışmasız en büyüğü olan Chainlink'i ise bu yazımıza saklamıştık. Buyurun hep birlikte bakalım kısaca Chainlink'e... 

### Nedir bu Chainlink?

En basit şekliyle açıklamak istersek, Chainlink, her tür blokzincir ve DeFi platformuna hizmet veren bir ara yapı. Yaptığı, bu platformların kullandığı akıllı kontratların ihtiyaç duyduğu blokzincir dışı bilgileri bulup kontrata aktarmak. 

Normalde akıllı kontratlar blokzincir içinde bulunan bilgiyi çok rahat bir şekilde okuyup işleyebiliyor. Sıkıntı, blokzincir dışı bilgilerde. Bu bilgilerin, birileri tarafından alınıp, işlenip, akıllı kontratın anlayabileceği bir şekilde blokzincir içine, oradan da kontrata aktarılması gerekiyor. 

Chainlink işte bu hizmeti veren aracılar içinde en büyüğü. Bir DeFi platformu olarak bilgi ihtiyacınız var ise, bulunduğunuz blokzincir üzerinden bir akıllı kontrat ile Chainlink'e talepte bulunuyorsunuz. Sistem üyeleri (node/düğüm) bu hizmete talip oluyorlar. Chainlink, bu üyelerden birkaçını hizmeti vermek için seçiyor. Sonrasında, seçilen üyelerden dış dünyadan topladığı bilgiler Chainlink tarafından bulunduğunuz blokzincir üzerinden size aktarılıyor. Birçok kaynaktan birkaçının seçilmesi ve bilgilerin toplanarak sunulması, tek bir kaynaktan bilgi alımının doğurabileceği yanlış ya da çarpıtılmış bilgi ihtimalini en aza indirmeye yarıyor. 

### Chainlink'in hikayesi

Hikaye aslında oldukça eskilere (blokzincir zamanından bahsediyoruz!), 2014 yıllarına dayanıyor. Smartcontract.com (şimdiki adıyla [Chainlink Labs](https://chainlinklabs.com)) o yıl, açık blokzincirler ile dış dünya verileri arasında köprü kurmak amacıyla kurulan bir şirket. Merkezi Cayman adalarında. 

Bu işin nasıl becerilebileceği konusuna uzunca bir süre kafa yoran ve deneysel çalışmalar yapan şirket yönetimi, 2017 yılında yaşanan ICO rüzgarından yararlanarak geliştirdiği Chainlink projesine özgü bir token yaratıyor. LINK adı verilen bu tokenin %35'lik kısmı bu ICO ile halka satılarak 32 milyon ABD Doları toplanıyor. Tokenların %35'lik kısmı Chainlink sistemine üye bilgi toplayıcılar ve sistemin gelişimine katkı sağlayacak paydaşlara verilmek üzere bir kenara ayrılıyor. Kalan %30 oranındaki token ise kurucu Chainlink Labs'de kalıyor. 

ICO sonrasında da devam eden ürün ve platform geliştirme sürecinin devamında, Chainlink nihayet 2019 yılı Mayıs ayında kullanıcılara sunuluyor. 

Her ne kadar hizmet verdiği sektör ağırlıklı olarak Merkeziyetsiz Finans olsa da, Chainlink için merkeziyetsiz bir platform demek doğru değil. Kendine ait bir ağa sahip olup, bu ağ üyeleri dağıtık bir şekilde görev yapıyor olsa da, diğer alanlarda sıkı bir merkezilik söz konusu. Örneğin, LINK tokenlarının herhangi bir yönetim hakkı yok. Zaten, bu tokenların ciddi bir kısmı halen Chainlink Labs kasasında. Ağın yönetimi de elbette Chainlink ekibinin elinde. 

### Chainlink tokeni LINK

Chainlink tarafından yapılan ICO ile hayata geçirilen LINK esasında iki ana işe yaramakta: 

Birincisi, bilgiye ihtiyacınız var ve bunu Chainlink'ten sağlamak istiyorsanız, bu bilgiyi sağlayan Chainlink ağının üyelerine hizmetleri karşılığı ödemeyi LINK ile yapıyorsunuz.

İkincisi ise, Chainlink ağına üye iseniz ve hizmet vermek istiyorsanız, elinizdeki LINK tokenları rehin etmeniz gerekiyor. Üstelik ne kadar çok rehin ederseniz, Chainlink ağını yönetenlerin size hizmet verme ihtimali o kadar yükseliyor. Hemen belirtelim rehin verme (staking) henüz başlamadı. 

### LINK ile ilgili eleştiriler

LINK ile ilgili birkaç eleştiri var.  Dilerseniz, gelin onlara kısaca göz atalım: 

##### LINK tutmak gerekli mi?

Kripto alanının önemli araştırma şirketlerinden [Messari](https://messari.io)'den [Ryan Selkis](https://twitter.com/twobitidiot)'in şu eleştirilerine önemli: 

*"LINK bir ödeme tokeni olduğu için, Chainlink üyelerine ödeme yapmak dışında elde tutmak ve ona bir değer yüklemek anlamsız. Ödemeler için Chainlink kullanıyorsanız, elde daha likit başka tokenları tutup, ihtiyacınız olduğunda bu daha az likit ve kullanışsız LINK tokenına dönebilirsiniz.*

*Konu Chainlink güvenliğini sağlamak için LINK rehin etmek ise, mevcut ücret modeli ne stabil ne de ölçeklenebilir. İşlem başına ücretleme şeklinde bir öneri var, ancak böyle bir uygulama Chainlink hizmetlerini kullanılamayacak kadar pahalı bir hale getirir."[^1]*

##### Chainlink XRP ile aynı akıbeti paylaşır mı?
İçinde bulunduğumuz ay içinde, gündemi takip ettiyseniz XRP tokenin başına gelenleri okumuşsunuzdur. Kaçıranlar için hatırlatalım: 

XRP, Ripple adlı bir teknoloji şirketi tarafından 2013 yılında yaratılmış bir token. Aslında Ripple'in başı ABD'nin sermaye piyasası denetleyici kurumu SEC ile uzun zamandır dertte idi ama geçtiğimiz günlerde SEC, Ripple yönetimine [ciddi suçlamalarda bulundu](https://www.sec.gov/news/press-release/2020-338). Özetle, Ripple'in XRP için ICO yaparak aslında izinsiz bir halka arz yaptığını belirterek iki üst düzey Ripple yöneticisine dava açtı. 

Şu aralar SEC'in Chainlink (daha doğrusu kurucusu Chainlink Labs) için de benzer şekilde suçlamalar getirebileceği konuşuluyor. Zira, Chainlink Labs da 2017 yılında aynı Ripple benzeri bir ICO yaptı ve halen LINK'in %35'ine sahip. Son günlerde bu [dedikoduların arttığını](https://twitter.com/bit_gossip/status/1343214669201371138) da söyleyelim.

##### Chainlink fazla PR mı kullanıyor?

Öte yandan, kripto dünyasında hem Chainlink hem de Ripple için getirilen ortak bir eleştiri var ki, o da her iki yapının kullandığı yoğun reklam, pazarlama ve halkla ilişkiler kampanyaları. 

Ripple, XRP kullanımı ile ilgili hangi banka ile "test sürümü" deney yapsa, bunu o banka ile partner/ortak olduğu şeklinde yoğun bir PR bombardımanı ile piyasaya sunardı. 

Chainlink de aynı şekilde, hangi platform ile hizmet sağlayıcı olarak anlaşsa bunu çok yoğun bir PR faaliyeti ile sunuyor. Ayrıca hem XRP hem de LINK'in, bu tokenlara 'gönülden bağlı' sosyal medya takipçi orduları var.

Bu benzerliklerden dolayı Chainlink Ripple'a, tokeni LINK XRP'ye benzer mi? Gayet tabii hayır. Ancak, böyle yoğun PR faaliyetleri, bu platformların merkeziyetsiz olmaktan çok, arkada ipleri elinde tutan firmalar bulunduğu ve bu yapıların aslında merkezi platformlar olarak değerlendirilmesi gerektiği algısını güçlendiriyor. 

#### LINK fazla mı değerli?

Değer konusu oldukça subjektif. Bu yazımızın ana konusu da değil. Ancak, yine yukarıda bahsettiğimiz Ryan Selkis'in bir başka eleştirisini de dikkate almakta fayda var: 

Şu an için LINK tokenin toplam değerinin, tüm DeFi'nin üzerine kurulu olduğu ETH sisteminin değerinin yaklaşık %6'sı olduğunu görüyoruz. LINK tokenın toplam değeri yaklaşık 5 milyar ABD Doları seviyesinde. Görevi ekosisteme bilgi sağlamak olan bir hizmetin tek bir oyuncusunun değeri bu kadar eder mi, değerlendirmesi siz sevgili okuyucunun. 

#### Chainklink kötü niyetli mi?

Chainlink için [Zeus Capital](https://zeus-capital.com) isimli bir yatırım fonunun 2020 Temmuz'unda yayınladığı rapor ([pdf](https://zeus-capital.com/assets/The_Chainlink_Fraud_Exposed.pdf)) oldukça ilgi çekti. 

Hemen baştan belirtelim, rapora göz attığınızda ve Zeus Capital'in [websitesini](https://zeus-capital.com) incelediğinizde, yazılanların bir çoğunun ve Zeus Capital'in kendisinin de şaibeli olabileceği izlenimine kapılıyorsunuz. O nedenle bu kısımda yazılanları büyük bir soru işareti ile değerlendirmekte fayda var:

Temel olarak bahsedilen, Chainlink'in hizmet sağlayıcı seçiminin şeffaf olmadığı, mevcut hizmet sağlayıcıların ağırlıklı olarak Chainlink ile ilişkili kişiler olduğu ve sistemin, ağ üyelerinden müşterilere hizmet verecek olanları seçerken bu kişileri kayırdığı şeklinde. 

İddialardan bir başkası da, bir DeFi platformu olan bZx'in 2020 başında [yaşadıği iki hack olayının](https://cointelegraph.com/news/decentralized-lending-protocol-bzx-hacked-twice-in-a-matter-of-days) arkasında  Chainlink olduğu yönünde. Hack olayının ana nedeninin bZx'nin tek bir bilgi kaynağı ile çalışması gösterilmişti. Olayın duyulması ile birlikte LINK tokenin fiyatı ciddi bir şekilde arttı. Daha sonrasında da bZx [Chainlink ile çalışmaya başladı](https://coingape.com/bzx-hack-update-exchange-add-chainlink-protocol/). 

Keza, bu yazıya karşı olarak büyük ihtimal ile Chainlink kaynaklı yayınlanan [bir başka Medium yazısı](https://smartcontentpublication.medium.com/debunking-the-zeus-capital-disinformation-report-on-chainlink-7313d9e1801#e581) olayın bir PR tiyatrosuna dönmüş olduğu izlenimini uyandırıyor. 

Son zamanlarda çıkan "Link, XRP gibi mi olacak?" söylentilerinin arkasında da Zeus Capital'in attığı bir [tweet](https://twitter.com/ZeusCapitalLLP/status/1341759410884857856?s=20) olduğunu söylersek sanırım şaşırmazsınız. 

Dolayısıyla, yukarıdaki Zeus Capital iddialarını, "çamur at izi kalsın" mı yoksa "ateş olmayan yerden duman çıkmaz" mı şeklinde değerlendirmeli, karar siz okuyucuya kalmış durumda.  

### Sonuç
Chainlink, merkeziyetsiz finans platformlarının kritik ihtiyaçları içinde sayabileceğimiz 'dış dünyadan bilgi sağlama' görevini yerine getiren oracle servis sağlayıcıların lideri. Kurucusu, şu ana kadar daha çok geleneksel bir dünya şirketi gibi hareket etti. Bu hareketler, LINK token denen sistem parasına son birkaç yılda ciddi bir değer kazandırdı. Ancak uzun vadede bu tip geleneksel hareketler gerek kanuni otoriteler gerekse merkeziyetsizlik felsefesi ile yetişen yeni DeFi girişimlerinin eleştiri ve tepkisine yol açabilir. 

Her konuda olduğu gibi bu alanda da sağlıklı bir rekabetin olması, ekosistemin gelişmesi için önemli. Önümüzdeki dönemde bu alanın nasıl gelişeceğini, rakiplerin pastadan daha büyük pay kapmak, Chainlink'in ise mevcut payını kaptırmamak için ne gibi hamleler yapacağını hep birlikte göreceğiz. 

[^1] messari-report-crypto-theses-for-2021.pdf Sayfa 67

---

*Not 1: Bu yazı ilk olarak 23 Aralık 2020'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/definin-bilgi-kaynagi-oracle/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

