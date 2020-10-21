---
layout: post
title:  "DeFi'nin sigortası Nexus Mutual"
date:   2020-10-20 18:47:56 +0300
categories: Genel
tags: Yazılar DeFi
---

[Nexus Mutual](https://nexusmutual.io), DeFi dünyasına çok ihtiyaç duyulan sigortalamayı getirmeye çalışan girişimlerin en büyüğü. İki yazıdan oluşacak seriminizin ilkinde gelin hep birlikte Nexus Mutual'a ekonomik ve potansiyel olarak bakalım. Bir sonraki yazımızda ise teknik olarak sistem nasıl çalışıyor, tokeni [NXM](https://www.coingecko.com/en/coins/nexus-mutual) nasıl fiyatlanıyor konularına değiniriz.  

### Merkeziyetsiz sigortacılık olur mu?

Her ne kadar bildiğimiz klasik finans ile belli alanlarda kesişse de DeFi yani merkeziyetsiz finans kendi içinde ayrı bir dünya olmaya doğru hızla ilerliyor. DeFi aktörlerinin nihai hedefi de bu aslında. Ancak fiziksel dünya ile iletişimi kesebilmek için belli temel gereksinimlerin karşılanması gerekiyor. Bunların en önemlilerinden biri de sigorta. Üstelik DeFi alanında klasik finansa göre daha da kritik bu gereksinim. Neden? 

| ![yagmur_semsiye](/assets/umbrella-4510667_640.jpg)|
|:--:| 
| *Image by [neo tam](https://pixabay.com/users/neotam-11291643/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=4510667) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=4510667)*|

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

*Not 1: Bu yazı ilk olarak 20 Ekim 2020'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/defi-sigortasi-nexus-mutual/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

---
