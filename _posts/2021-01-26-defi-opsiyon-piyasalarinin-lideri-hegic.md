---
layout: post
title:  "DeFi opsiyon piyasalarının lideri Hegic"
date:   2021-01-26 17:47:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

DeFi üzerinde küçük ama hızla büyüyen opsiyon platformlarının en büyüğü olan [Hegic](https://www.hegic.co)'e bakıyoruz bu yazımızda... 

Bir önceki [yazıda](/genel/2021/01/05/defi-opsiyon-piyasalari.html), opsiyonun temel özellikleri konusunda hafızamızı tazelemiş ve DeFi opsiyon piyasalarına göz ucuyla bakmıştık. Bu yazıda ise, şu an için bu alanın en büyüğü olan Hegic'i inceleyecek ve merkeziyetsiz opsiyon piyasalarının nasıl çalıştığının detayına gireceğiz.

### Hegic nedir?
Merkezi olmayan opsiyon en büyüğü olan [Hegic](https://www.hegic.co) 2020 yılının Şubat ayında [0molly Wintermut3](@0mllwntrmt3) isimli anonim biri ya da birileri tarafından hayata geçirilmiş.

Burayı tekrar etmekte fayda var: Paranızı emanet edeceğiniz bir DeFi platformu ve kurucusu anonim bir 'hesap'. Üstüne üstlük, finansal piyasaların en riskli ürünlerinden biri olan opsiyon piyasasında faaliyet gösteriyor. Böyle bir platforma paranızı neden yatırasınız ki? 

Birkaç nedeni olabilir aslında: Birincisi, hep söylediğimiz gibi, DeFi'de paranızı birine emanet etmiyorsunuz. Bu platformların çoğunda paranız sizin cüzdanınızda duruyor.

Ama eğer likidite sağlıyor iseniz paranızı sisteme kilitliyorsunuz, ki o zaman güvenilir yer konusu daha da önemli bir hale geliyor. Oysa burada böyle bir sözüne güveneceğiniz bir şirket, hadi onu geçtik, bir kişi bile yok. Ne var peki? 

İşte DeFi'nin ikinci kritik özelliği: Biz insanlar duygusal varlıklarız, söz verip yapmayabiliriz. Ama kod için öyle bir durum yok. Kod, eğer düzgün yazılmış ise, ne söylenirse onu yapar.

DeFi dünyasında sık kullanılan bir sözü tekrarlayalım: “Burada kod, kanundur”. Hem bu platformları çalıştıran kodlar, hem de platformu kullananların yaptıkları işlemleri gerçekleştiren Akıllı Kontrat dediğimiz yazılımlar herkesin görebileceği şekilde açık. Yani 'bu platform, neyi nasıl yapar?' sorusunun hem açıklaması var, hem de bunu gerçekleştiren kod şeffaf bir şekilde ortada. Biraz kodlamadan anlayan biri bakıp görebilir. 

Kodlamadan anlamayan biz kimi faniler için, bu yazılımların birçoğunun dış denetlemesi de yapılıyor bu arada. Böyle bir şeffaflığın getirdiği güven, öyle karşınızda gördüğünüz bir kurum ya da kişiye duyacağınızdan çok daha öte. İşte bu nedenle bu platformlara ciddi paralar konduğunu görüyoruz.

Üstelik Hegic platformu, kurulduğu Şubat 2020'den bu yana iki badire de atlatmış durumda. Birincisinde, [Nisan 2020'de opsiyon satanlar akıllı kontratın kodunda çıkan bir hatadan dolayı](https://decrypt.co/35038/hegics-molly-wintermute-im-paying-a-high-price-for-the-mainnet-first-approach-to-building) 30,000 ETH değerinde bir rakamın kilitli kalması nedeniyle zarara uğradılar. 0molly Wintermut3, hatayı kabul etti ve yatırımcıları ile birlik olarak [bu kişilerin zararlarını tazmin etti](https://twitter.com/HegicOptions/status/1258889995835842562). 

Mayıs ayında ise, bu sefer, bir kod hatası değil ama [sistem dizaynındaki bir problem](https://cryptobriefing.com/defi-options-platform-hegic-shuts-down-again/) nedeniyle akıllı bir satıcı, [ufak bir miktar ](https://twitter.com/Rewkang/status/1263435897954988033) haksız kazanç elde etmeyi başardı. 

Deneysel projelerde bu tip problemler oluyor gördüğünüz gibi. Ama sonrasında hem bu hataların giderilmesi hem de zaman içinde yeni hataların çıkmaması, anlaşılan yatırımcıların gözünde "seni öldürmeyen güçlendirir" imajı yaratmış olmalı ki, Hegic son aylarda ciddi bir büyüme yaşadı. 

### Nasıl bir sistem kullanıyor Hegic?

Normalde opsiyonlarda, opsiyonu kullanan (alan/tutan) ve satan (yazan) iki parti olur. Bu iki parti, hangi ürünü, ne zaman, hangi fiyattan alma/satma opsiyonu olacağını ve bu parametreler bazında opsiyonun değerinin ne olacağı konusunda anlaşırlar.  

#### Eşten eşe işlem yapmak çok zor. Neden?

DeFi ürünlerinde ise eşten eşe işlem gerçekleştirmek çok zor.  Zira, bir tavuk-yumurta kısır döngüsüne girme durumunuz var: 

İnsanlar işlem yapabilmek için opsiyonların makul ücretler ile fiyatlanmasını bekliyorlar. İyi fiyatlama olabilmesi için gerekli en temel girdi ise likidite. Likidite olmayınca insan gelmiyor, insan gelmeyince likidite olmuyor. Bunu aşmanın yolu, başlangıçta tekeri döndürecek bir likidite koymak. Bu da sisteme kapital enjekte etmek ile oluyor. Merkezi bir yapı iseniz bir yerden yatırım alıp bunu koyarsınız ama DeFi ürünleri birer aracı; kapital tutmuyorlar ve para emaneti almıyorlar. 

Bu durum, opsiyon piyasalarında çok daha fazla sıkıntı yaratıyor. Bunun nedeni, opsiyonların bir hisse senedi ya da tokena göre çok daha fazla değişken barındırması. Hisse senedinde yalnızca hissenin değeri üzerinden bir alım ya da satım emri veriyorsunuz - tek değişken o. Halbuki opsiyon dediğinizde işin içine vade giriyor. Böyle olunca, bir token için bir fiyat üzerinden pazarlık olurken, onun opsiyonu için değişik vadelerde onlarca farklı fiyat olabiliyor. Eşten eşe işlem yapmaya çalıştığınızda, onlarca farklı fiyat için alıcı ve satıcı bulmaya çalışmanın ne kadar zor olabileceğini tahmin edebilirsiniz.

Yukarıdaki temel sorun nedeniyle genelde DeFi piyasası ürünleri, ama özelde de opsiyon piyasası platformları, uzunca bir süre ıssız sokaklar gibiydiler. Peki nasıl çözdüler bu problemi?

#### Ve işte yine geldik DeFi'yi kurtaran havuz modeline... 

İşte DeFi piyasaları bu kısır döngüyü "havuz modeli" ile aştılar. Bu havuzların ilk örneklerinden biri Uniswap oldu. Hikayesini tekrar hatırlayalım:

Uniswap, kendi merkeziyetsiz kripto borsasında yeterince likidite sağlayamayınca, önce yatırımcılarının koyduğu para ile havuzlar kurdu. Havuzlar, likidite sorununa bir parça çözüm oldular ancak büyüklüğü bir türlü istenen seviyelere ulaşmadı. Tam o sıralarda [Compound](https://compound.finance/)'un başlattığı likidite sağlama karşılığı token verme hareketi, likidite sorununu çözme konusunda DeFi platformlara önemli bir eşik atlattı. Benzer modeli Uniswap da uyguladı ve bir yılı aşkın süredir yerlerde sürünen likidite bakın nasıl bir şekil aldı: 

 | ![uniswap_tvl](/assets/uniswap_tvl_v5.png)|
|:--:| 
| *Uniswap için kilitlenen para miktarı. Kaynak:[DeFiPulse](https://defipulse.com/)*|

Token yani teşvik verme, başlangıçta "ama bu hormon enjekte etmek ile aynı!" şeklinde tepkiler ile karşılaştı. Bu tepkilerde bir parça haklılık payı olduğu, Kasım ayında  token teşviğinin sona ermesi ile birlikte sisteme kitlenen paranın ciddi bir şekilde azalması ile anlaşıldı. Ancak birkaç ay içinde bu likidite geri geldi. Yani, arabaya dışarıdan verilen kablo ile sağlanan itici güç, içeride duran atıl gücü çalışır hale getirdi. 

Opsiyon piyasasının bir başka oyuncusu olan [Opyn](https://opyn.co/#/), yukarıda bahsettiğimiz eşten eşe opsiyonlar ile oyuna başlamışken, Hegic, kendi opsiyon platformunu Uniswap gibi bir havuz şeklinde kurdu. Sonrasında da, 2020 Eylül ayı içinde kendi platformuna likidite sağlayanlara yönelik HEGIC tokenı çıkardı. Bu sayede, Hegic üzerine kilitlenen para miktarı ciddi bir artış kazandı:

 | ![hegic_vs_opyn_TVL](/assets/hegic_vs_opyn_tvl_v3.png)|
|:--:| 
| *Hegic ve Opyn'da kilitlenen toplam miktarı. Kaynak:[DeFiPulse](https://defipulse.com/)*|

Hemen dikkatinizi çekmek isterim: Opyn yukarıdaki grafikte yerlerde sürünen kırmızı çizgi, yani eşten eşe sistemi gerçekten çalışmıyor. Yalnızca kilitli miktar değil ilgi çekici olan: Bu parayı havuzlara kilitleyenlerin aldıkları komisyon gelirleri de üç ay gibi kısa bir sürede ciddi bir rakama ulaştı: 

 | ![hegic_revenues](/assets/hegic_revenues.PNG)|
|:--:| 
| *Hegic 2020 yılı üç aylık gelirler. Kaynak:[Messari](https://messari.io/)*|


#### Sistem nasıl çalışıyor?

Sistemde iki ana aktör var. 

Bunlardan birincisi, **opsiyon satın almak isteyenler**. Bunlara opsiyon alan/sahip olan (holder) deniyor. Ne satın alıyorlar?  ETH ya da BTC'yi herhangi bir vade için alma (call) ya da satma (put) hakkını. Nereden alıyorlar bu opsiyonu? Kendilerine fiyat veren bir akıllı kontrat var, bu kontratın arkasında da bir havuz (daha önce defalarca örneğini verdiğimiz havuzları hatırlarsınız, hatırlamayanlar dilerlerse [Uniswap](/genel/2020/09/15/nedir-bu-uniswap.html) ve [Synhetix](/genel/2020/08/28/Defi-turev-piyasasi-synthetix-nasil-calisiyor.html) havuzlarına bir göz atabilirler). 

Bu kişiler, akıllı kontratın verdiği fiyatı beğenirler ise, istedikleri opsiyonu yaratıp satın alıyorlar. ([MakerDAO'nun sisteminde kullanıcının kredi yaratması](/genel/2019/02/15/MakerDAO-kredi-kullaniminda-cigir-acar-mi.html) gibi, ki buna "mint" yani para basmak da deniyor)

İkincisi ise, yukarıdaki **bu havuza likidite sağlayanlar**. Yani, yukarıdaki opsiyonları satanlar, ki onlara da opsiyon yazan/çıkaran (writer) deniyor. Ancak bu kişiler, herhangi bir şekilde opsiyon yazmıyorlar. Yaptıkları sadece bu havuzun suyu olan likiditeyi koymak. 

Havuza likidite sağlayarak ne kazanç elde ediyorlar? Öncelikle, yukarıdaki satılan opsiyonların ücretlerini kazanıyorlar. Riskleri ise, opsiyonun kullanılması durumunda oluşan zarar...

Özet olarak, opsiyon fiyatları bir algoritma ile belirleniyor. Yukarıdaki birinci grup, opsiyon satın alırken prim ödüyor. Bu primler havuza gidiyor. Opsiyon satın alanlar opsiyonu kullanırlar ise, bunun ödemesini akıllı kontrat havuzdan alarak yapıyor. Havuzda kalan miktar, havuza likidite sağlayanlar arasında bölüşülüyor. 

### Hegic'in tokeni HEGIC
Hegic'in yarattığı HEGIC tokenın iki farklı kullanım aracı var, ki bu diğer DeFi projelere oldukça yakın: 

Birincisi, HEGIC tokenlar sisteme likidite sağlamak için 'rehin' edilebiliyor (staking). Bunun karşılığında, hem yukarıda bahsettiğimiz prim ödemelerinin içinden ödenen opsiyonlar sonrası ortaya çıkan kârı alıyorlar. Ayrıca, rehin vermeleri karşılığı Hegic tarafından ödül olarak verilen ekstra tokenları kazanma şansına sahipler.  

İkincisi ise bu tokenlar sayesinde ileride Hegic sisteminin yönetimine dahil olma şansına sahip olacaklar. Hegic kurucusu Wintermut, token sahibi aktif kullanıcı sayısının 100'ü aşması ile birlikte sistemin yönetimini yavaş yavaş token sahiplerine geçirmeyi planlıyor. 

### Hegic ve Opyn farkları
Merkeziyetsiz finans alanında faaliyet gösteren iki büyük oyuncu Hegic ile Opyn arasında birkaç temel fark var:

Öncelikle Hegic, yukarıda da bahsettiğimiz gibi opsiyonların vade tarihine kadar herhangi bir noktada kullanılmasına izin veriyor. Finans piyasasındaki jargonu ile 'Amerikan opsiyonu' yönetimini kullanıyor. Opyn'de ise opsiyonları sadece vade sonunda kullanabiliyorsunuz. Buna ise 'Avrupa opsiyonu' denmekte.  

Bunun yanında, Opyn havuz kullanmak yerine yukarıda bahsettiğimiz eşten-eşe modelini kullanıyor. Yani, opsiyon satın alanların yanında, opsiyon satanlar (yazanlar) var. Bu çok da pratik bir yöntem değil. Zira, opsiyonun içerdiği pek çok parametreyi (süre, oran, hedef fiyat, opsiyon prim değeri) satıcının belirlemesi gerekiyor. Bu hem zahmetli bir süreç, hem de alıcıların istediği parametreler ile uyumlu olmayabiliyor.

Bu iki temel fark, aslında neden Hegic platformunun daha geç başlamış olsa da Opyn'e fark attığını anlatmaya yetiyor. Hegic, DeFi dünyasındaki son gelişmeleri yakından takip ederek daha geniş bir kitleye ulaşmış ve likidite anlamında rakibine üstünlük sağlamış görünüyor. 

### Sonuç 

DeFi dünyası 2020 yılı içinde önündeki engelleri yavaş yavaş aşmaya başladı. Bu alana yeni girmiş olan Hegic, merkeziyetsiz takas borsası ya da türev piyasası platformlarının geniş kesimlere yayılmak amacıyla kullandığı araçları hızlı bir şekilde sistemine kattı. Bunun sayesinde, yaşadığı türlü badirelere rağmen hızlı bir büyüme gösterdi. Bakalım, 2021 yılı içinde bu büyümeyi devam ettirebilecek mi? Hep birlikte yaşayarak göreceğiz.


*Not: Hegic, Opyn ve diğer opsiyon sağlayıcılar ile ilgili daha derin bilgi için [şu Medium yazısına](https://medium.com/coinmonks/a-comparison-of-decentralized-options-platforms-140b1421c71c) ve o makalenin devamı niteliğinde güncellemeler de içeren [şu yazıya](https://medium.com/coinmonks/an-update-of-a-comparison-of-decentralized-options-platforms-91b14d3a6170) göz atabilirsiniz.*

---

*Not 1: Bu yazı ilk olarak 26 Ocak 2021'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/defi-opsiyon-piyasalarinin-lideri-hegic/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*
