---
layout: post
title:  "Tornado Cash olayı DeFi'yi nasıl etkiler"
date:   2022-08-27 12:17:56 +0300
categories: Genel
tags: Yazılar, DeFi, CoindeskTR
---

Tornado Cash olayını incelediğimiz ikinci yazıda, kripto dünyasının bu olaya verdiği tepkileri ve bu dünya oyuncularını gelecekte nelerin beklediğini irdelemeye çalışacağız. 

Geçtiğimiz yazıda, önce Ethereum blokzinciri üzerindeki Tornado Cash isimli gizlilik uygulamasının ne olduğunu, neden otoritelerin tepkisini çektiğine bakmış, sonrasında kripto dünyasındaki merkezi oyuncuların bu yaptırım kararına nasıl uyduklarının örneklerini inceleyip, bu dünyanın temel oyuncularının görüşlerine değinmiştik. Şimdi ise önce kripto oyuncularının verdiği tepkileri sonrasında ise onları bundan sonra nasıl bir dünyanın beklediğine göz atalım. 

### Verilen tepkiler

Önceki yazımızda da değindiğimiz gibi, ilk tepkiler sansüre uyum gösteren ABD merkezli yapılardan gelmeye başladı.  Merkezi platformlar (Circle, GitHub, Infura, Alchemy gibi) ya da merkeziyetsizlik yolunda ilerleyen ama geliştici ekibi bu ülkede bulunan platformlar (dYdX, Aave, Uniswap, Balancer gibi) Tornado Cash ile ilgili hesaplara erişim konusunda kısıtlama getirmeye başladılar. 

| ![splash](/assets/coffee-1973549_800.jpg)|
|:--:| 
| *Image by [David Mark](https://pixabay.com/users/12019-12019/) from [Pixabay](https://pixabay.com/)*|

Bunun yanında, alınan önlemin kripto dünyasının ruhuna aykırı olduğunu gösterebilmek amacıyla, pek çok ünlü kişinin hesabına Tornado Cash üzerinden 0.1 ETH [para atıldı](https://www.coindeskturkiye.com/politika/birisi-tornado-cashten-eth-gondererek-unluleri-trolluyor-1446) (Buna ingilizcede 'dusting' yani 'tozlama' adı veriliyor). Öyle ya, Tornado Cash bir yazılım. Parayı havuza gönderen birileri var ve bu birileri Tornado Cash'e 'parayı şu hesaba gönder' dediklerinde hesap sahibinin alabileceği bir önlem yok. Dolayısıyla Coinbase'in sahibi Brian Armstrong'dan ünlü sunucu Jimmy Fallon'a kadar pek çok ünlünün hesabı şu anda 'lekelenmiş' durumda. 

### Protokoller açısından uzun vadede neler bekleniyor?

Bunlar kısa vadeli reaksiyoner alınan önlemler. OFAC'ın bu hareketlerinin uzun vadede de ciddi etkileri olması beklenmekte. Burada DeFi protokolleri kendilerine politikalar belirlemek, hatta stratejilerini gözden geçirmek durumundalar. Örneğin, DeFi dünyasının en büyüklerinden MakerDAO, teminat havuzlarında tuttuğu [USDC'leri ETH'ye dönüştürmeyi tartışıyor](https://cryptobriefing.com/makerdao-should-seriously-consider-preparing-for-dai-depeg-founder/). Konuşulan rakam az değil 3,5 milyar ABD Doları. Circle'in kişilere ait hesaplardaki USDC'leri dondurmuş olması MakerDAO'nun gözünü korkutmuş durumda; yarın öbür gün Circle'in aynı hareketi kendilerine yapmayacağının garantisini kim verebilir? Her ne kadar bu hareketin çılgınca olacağını iddia eden Vitalik Buterin ve Compound kurucusu Josh Lerner gibi ağır toplar olsa da Maker bu konuda nasıl bir aksiyon alacak göreceğiz.

#### DeFi dünyası ikiye mi bölünecek?

Bu hareketin DeFi uygulamalarını (bir diğer deyişle protokollerini) ikiye bölmesi de kuvvetle muhtemel. Bir yanda, kanuni otoritelere uyumlu olmaya çalışan protokoller, bu tip yasaklamalara uyarak gerekli kısıtlamaları yapacaklar. Bu tip kısıtlamaların, otoritelerin desturu alındığı için protokollerin daha geniş bir kitleye hitap edebilmesine katkı sağlayabileceği söylenebilir. Ancak unutulmaması gereken, otoritelerin konuya vakıf olmadıkları için alınmasını istedikleri önlemlerin protokoller açısından uygulamada ciddi sıkıntı yaratma ihtimali. Yarın öbür gün istenen kısıtlamalar protokollerin ellerini ayaklarını bağlayabilir; bunun somut örneklerini klasik finansta her gün yaşıyoruz. Örneğin, klasik finans dünyasında 'paranın kaynağının nereden geldiği önemli bir konudur'. Bugün ETH üzerinden Tornado Cash kullananlar toplam hesapların %0.03'ü olmasına rağmen bu kullancıların iletişime geçtiği birinci derece hesaplar toplam ağın %2,36'sı, onların ilişkiye geçtiği ikinci derece hesaplar ise toplam [Ethereum ağının neredeyse yarısına denk geliyor](https://twitter.com/ElBarto_Crypto/status/1558428428763815942)! Bu durum, klasik finansa alternatif olarak gösterilen DeFi'nin aslında yavaş yavaş klasik finanslaşması anlamına gelir ki, uzun vadede bu tip yapıların böyle hibrit bir şekilde kullanıcılarına nasıl bir değer önerisi sunabilecekleri tartışma konusu olabilir. 

|![TC ilişkili hesaplar](/assets/TC_iliskili-hesaplar_800.png)|
|:--:| 
| *Tornado Cash kullanan hesaplar ve o hesapların ilişkilde olduğu hesaplar. Kaynak: [Twitter @elbarto capital](https://twitter.com/ElBarto_Crypto/status/1558428428763815942)*|

#### Merkeziyetsizleşme hızlanabilr mi?
Diğer yandan, bu durum protokollerin gittikçe daha hızlı bir şekilde merkeziyetsizleşmesine de yol açabilir. Geliştirici ekipler herhangi bir kanuni sorumluluk altına girmemek için kendilerini dağıtarak, tüm gelişmeyi DAO'lar aracılığıyla topluluğa vermek isteyebilirler. Alternatif olarak, ekiplerin merkezlerini ABD'den daha teknoloji dostu ülkelere (örneğin son dönemde Birleşik Arap Emirlikleri bu anlamda ön plana çıkmaya başladı) taşımaları da söz konusu olabilir. Bu son konu, yani ABD'nin uygun bir kanuni altyapı sağlayamadığı için bu alandaki liderliğini kaybetmesi ihtimali, ülkedeki kanun koyucular için oldukça hassas bir nokta. İnovasyon yarışını kaybetme tehlikesi, OFAC benzeri ofislerin yapacağı müdaheleleri kısıtlamak için gerekli kanuni altyapının hazırlanması konusunda ciddi bir motivasyon kaynağı olabilir. 

#### Tornado Cash kapanıp Mornado Cash açılırsa ne olacak?
Öte yandan, Tornado Cash'in engellenmesinin uzun vadede kalıcı sonuçları olacak mı, açıkcası o da belirsiz. Açık kaynak kodlu olması nedeniyle Tornado Cash'in kopyalanarak benzerlerinin çıktığını görebiliyoruz. Buradaki kritik nokta, Tornado Cash'ın büyüklüğü sayesinde karıştırıcı özelliğinin oldukça etkili olmasıydı (her ne kadar [Elliptic](https://hub.elliptic.co/) benzeri takip firmaları farklı yöntemler ile kirli parayı belirli ölçülerde [ayıklayabildiklerini açıklasalar](https://hub.elliptic.co/analysis/the-100-million-horizon-hack-following-the-trail-through-tornado-cash-to-north-korea/) da). Bir başka uygulama Tornado Cash kadar etkili olabilecek mi, onu kestirebilmek zor. 

#### Ön yüz ve altyapı farkı
Bir diğer önemli konu ise kısıtlamaların önemli bir kısmının ön yüzler tarafında olması. Ne demek bu? DeFi protokolleri temel olarak blokzincir üzerine yüklenmiş akıllı kontratlar. Bir kez akıllı kontratı sisteme yükledikten sonra (eğer güncellenebilir şekilde yapılandırmazsanız) artık geliştiricinin kontrolünden çıkıyor. Genelde kullanıcılar protokollerin web sayfaları üzerinden akıllı kontrat ile etkileşime girebiliyorlar. İşte bu web sayfaları geliştirici ekibe ait ve dış yaptırıma tabi olabiliyorlar. Bu nedenle, ön yüz dediğimiz bu sayfalara erişim kısıtlanabiliyor. Arka tarafta blokzincire ulaşan kullanıcılar protokolün sunduğu akıllı kontratı kullanmaya devam ediyorlar. Ne var ki bu tip direkt blokzincir üzerinden ulaşım teknik bir bilgi gereksinimi gerektiriyor. Karşımızda daha henüz cüzdan kullanmakta bile zorlanan bir kitle olduğunu göz önüne aldığımızda, bu tip direkt kullanımın hayli düşük seviyede olacağını düşünebiliriz.

Gelecekte yeni çıkacak merkeziyetsiz girişimler, kullanıcıların bu protokollerin akıllı kontratlarına direkt blokzincir seviyesinde erişime yarayacak araçlar çıkaracaklar. Yine de kısıtlamaların kullanıcı adaptasyonunu yavaşlatacağını söylemek mümkün.

### Peki ya geliştiriciler açısından?

Hollanda otoriteleri tarafından Tornado Cash geliştiricilerinden birinin tutuklanması, her ne kadar bu dünyadaki geliştiricilere bir gözdağı olarak algılansa da, açıkcası uzun vadede otoritelere çok da fayda sağlamayacak. Tam tersine, geliştiricilerin kimliklerini açıklamak yerine anonim kalmalarını teşvik edecek, onlara anonim kalma konusunda ciddi bir bahane getirecek bir uygulama bu. Kısacası bu tutuklamanın oldukça talihsiz bir hareket olduğunu söylemeye gerek yok. 

### Olayın bir de akıllı kontrat boyutu var!
Öte yandan, son günlerde tartışılmaya başlanan bir başka nokta da birinci seviye akıllı kontrat platformlarının geleceği ile ilgili. Birinci seviye platformların güvenliği ağırlıklı olarak hisse kanıtı sistemi ile sağlanıyor (ingilizcesi Proof-of-Stake/PoS olan bu sistemi kısaca kullanıcıların ellerindeki platforma ait paraları sisteme kilitlemesi ve karşılığında belirli bir ücret karşılığı işlemlerin doğruluğunu onaylaması olarak adlandırabiliriz). Bir aksilik olmazsa Eylül ayı içinde Ethereum ağı da bu sisteme geçecek. 

Onaylayıcı olma, kişilerin kendi başlarına yürütebilecekleri bir işlem olmasına rağmen herkese göre değil. Kullanıcının belli başlı birkaç uygulama indirip bilgisayar başında saatlerini harcayarak sistemi kurması, sonrasında da bilgisayarını uzun süreli aktif tutması gerekiyor. Bundan kaçınmak isteyen kullanıcılar, ellerindeki ETH'leri bu işi yapmak için uzmanlaşmış kurumlara emanet ederek işin 'hamaliye' kısmından kaçınabiliyorlar. Bu uzmanlaşmış kurumlardan Coinbase, Kraken ve Binance şu anda tüm Ethereum sistemine emanet edilmiş [ETH'lerin %27'sine sahipler](https://coinmarketcap.com/alexandria/article/glassnode-and-coinmarketcap-on-chain-analytics-issue-one). 

Peki ya önümüzdeki günlerde OFAC ya da benzeri bir kurum, bu merkezi yapılardan 'mimlenmiş' adreslerden gelen işlemleri onaylamamalarını isterse ne olacak? Bu merkezi yapılar buna uyacaklar mı? Onaylayıcıların, geçerli bir işlemi tarafsız olarak onaylamaları gerekiyor. Kasti olarak onaylamadıkları durumda (ve bunu sürekli yapmaları halinde) sistem tarafından rehin koydukları paranın budanması tehlikesi var (ingilizcede buna 'slashing' deniyor). Merkezi yapılar açısından iki ucu keskin bir bıçak tutma tehlikesi ortaya çıkacak: Ya otoritenin dediğini uygulamayıp yaptırımlara maruz kalacaklar ya da dediğini uygularlarsa müşterilere ait ETH'leri kaybetme riskleri ortaya çıkacak. Bakalım, merkezi kurumlar burada nasıl bir aksiyon alacaklar?

### İleride kripto dünyası neler yapabilir?

Peki önümüzde duran konuya akılcı yaklaşım nasıl olabilir? Öncelikle, ABD'nin tepkisini azımsamak ya da yasakçı bulmak işin kolayına kaçmak olur. Kendileri açısından tehlikeli gördükleri bir düşmanın desteklediği bu harekete tepki vermeleri gayet normal.  Tepkinin şiddeti ya da şekli ise kişisel özgürlükleri kısıtladığı için ölçüsüz ve muhtemelen kanuni sınırları zorladığı için yargıdan dönecek, ancak bu dönüşün bir kaç yıl süreceği düşünüldüğünde kısa vadede yargının bir çözüm olacağını öne sürmek zor. 

Kripto dünyasının tepkisinin birkaç yönden olacağını düşünüyorum. [Coincenter](https://www.coincenter.org/) benzeri düşünce kuruluşları ve merkezi yapılar Washington DC'deki lobi faaliyetleri aracılığıyla kamuoyu yaratma konusunda ağırlıklarını ortaya koyacaklar. Burada da temel konu yine yapılan hareketlerin bu alanda çalışan ekipleri ülke dışına kaçırması nedeniyle ABD'nin inovasyon konusunda geri kalacağı korkusu olacak muhtemelen. Öte yandan, demografinin değişmesi ile birlikte yaklaşan seçimlerde adayların temsilciler meclisi ve senatoya seçilebilmek için daha kripto dostu yaklaşımlar göstereceğini tahmin etmek de mümkün.

DeFi dünyasında yukarıda bahsettiğim ikiye ayrılma konusunda topluluğun büyük bir kısmının merkeziyetsizlik tarafında kalacağını öngörmeli. Klasik finansı DeFi ile birleştirmeye çalışan uygulamalar yine sahnede olacaklar ancak artan regülasyonlarla birlikte bu alandaki heves bir parça azalabilir. Diğer yandan, Aave Pro benzeri merkeziyetsiz servis sağlayıcılar tarafından kurumsal dünyaya hitap edecek steril ürünlerin arttığı da görülebilir. Bir taraftan da, artan kamuoyu baskısı ile birlikte otoritelerin de DeFi protokollerini anlamak için daha fazla çaba sarfedeceği ve otoriter rejim tarzı toplu yasaklama yerine daha hassas terazide ölçülmüş yaptırımlar getirmeleri de olasılık dahilinde.

### Sonuç 
Tornado Cash olayı, merkezi otoritelerin haklı gerekçelerle olsa bile kripto dünyasına attıkları talihsiz bir adım oldu. Görünen o ki, bu alanda yeni olan herkesin yaşadığı öğrenme eğrisini onlar da yaşayacaklar. Kripto dünyası içinde ise şu an alınan bu önlemin genelleştirilerek korku senaryoları çizildiğini görüyoruz. Umarım gerçek, bu olayın aslında kriptoya karşı alınan hasmane bir tavırdan öte, otoritenin kendine düşman olarak gördüğü Kuzey Kore'ye yönelik aldığı bir aksiyon olduğudur. Eğer böyle ise ileride oluşturulacak kamuoyu ve DeFi ürünlerinin daha iyi tanınmasıyla birlikte kısıtlamaların kapsamının daha da daraltılacağını görebiliriz. Aksi takdirde, otoriteler ile DeFi arasında yaşanacak gereksiz gerilimin DeFi'nin geniş kitlelere yayılmasının önündeki en büyük engel olacağını söylemek hiç de zor değil. 



---

*Not 1: Bu yazı ilk olarak 27 Ağustos 2022'de [Coindesk Türkiye](https://www.coindeskturkiye.com/))'de [yayınlandı](https://www.coindeskturkiye.com/yazarlar/turan-sert/tornado-cash-olayi-defiyi-nasil-etkiler-1700)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

