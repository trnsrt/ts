DeFi üzerinde küçük ama hızla büyüyen opsiyon platformlarının en büyüğü olan [Hegic](https://www.hegic.co)'e bakıyoruz bu yazımızda... 

Bir önceki [yazıda](https://www.btchaber.com/defide-opsiyon-piyasalari/), opsiyonun temel özellikleri konusunda hafızamızı tazelemiş ve DeFi opsiyon piyasalarına göz ucuyla bakmıştık. Bu yazıda ise, şu an için bu alanın en büyüğü olan Hegic'i inceleyecek ve merkeziyetsiz opsiyon piyasalarının nasıl çalıştığının detayına gireceğiz.

### Hegic nedir?
Merkezi olmayan opsiyon borsalarından biri olan [Hegic](https://www.hegic.co) 2020 yılının Şubat ayında [0molly Wintermut3](@0mllwntrmt3) isimli anonim biri ya da birileri tarafından hayata geçirilmiş.

Burayı tekrar etmekte fayda var: Paranızı emanet edeceğiniz bir DeFi platformu ve kurucusu anonim bir 'hesap'. Üstüne üstlük finansal piyasaların en riskli ürünlerinden opsiyon piyasasında faaliyet gösteriyor. Böyle bir platforma paranızı neden yatırasınız ki? 

Birkaç nedeni olabilir aslında: Birincisi, hep söylediğimiz gibi, DeFi'de paranızı birine emanet etmiyorsunuz. Bu platformların çoğunda paranız sizin cüzdanınızda duruyor. Ama eğer likidite sağlıyor iseniz paranızı sisteme kilitliyorsunuz, ki o zaman güvenecek bir yer daha önemli bir hale geliyor.

Ama burada böyle bir sözüne güveneceğiniz bir şirket hadi onu geçtim bir kişi bile yok. Ne var peki? DeFi'nin ikinci kritik özelliğine geliyoruz: Burada kod kanun. Ve kod aynı kanunlar gibi herkese açık. Platform ne yapar, nasıl yapar, hem açıklaması var, hem de bunu gerçekleştiren kod bir başka deyişle akıllı kontratların içi herkese açık. Bunu denetleyenler var gayet tabii ama herhangi bir kullanıcı da içini açıp bakabilir. Bunun getirdiği güven, öyle karşınızda gördüğünüz kurum ya da kişiden çok daha öte. İşte bu nedenle bu platformlara ciddi paralar konuyor. 

Üstelik Hegic platformu, kurulduğu Şubat 2020'den bu yana iki badire de atlatmış durumda. Birincisinde [Nisan 2020'de opsiyon satanlar akıllı kontratın kodunda çıkan bir hatadan dolayı](https://decrypt.co/35038/hegics-molly-wintermute-im-paying-a-high-price-for-the-mainnet-first-approach-to-building) 30,000 ETH değerinde bir rakamın kilitli kalması nedeniyle zarara uğradılar. 0molly Wintermut3, hatayı kabul etti ve yatırımcıları ile birlik olarak [bu kişilerin zararlarını tazmin etti](https://twitter.com/HegicOptions/status/1258889995835842562). 

Mayıs ayında ise, bu sefer, bir kod hatası değil ama [sistem dizaynındaki bir problem](https://cryptobriefing.com/defi-options-platform-hegic-shuts-down-again/) nedeniyle akıllı bir satıcı, [ufak bir miktar ](https://twitter.com/Rewkang/status/1263435897954988033) haksız kazanç elde etmeyi başardı. 

Deneysel projelerde bu tip problemler oluyor gördüğünüz gibi. Ama sonrasında hem bu hataların giderilmesi hem de zaman içinde yeni hataların çıkmaması, anlaşılan yatırımcıların gözünde "seni öldürmeyen güçlendirir" imajı yaratmış olmalı ki, Hegic son aylarda ciddi bir büyüme yaşadı. 

### Nasıl bir sistem kullanıyor Hegic?

Normalde opsiyonlar da, opsiyonu kullanan (alan/tutan) ve satan (yazan) iki parti olur. Bu iki parti, hangi ürünü, ne zaman, kaç paradan alma/satma opsiyonu olacağını ve bu parametreler bazında opsiyonun değerinin ne olacağı konusunda anlaşırlar.  

#### Eşten eşe işlem yapmak çok zor. Neden?

Çoğu zaman birbiri ile eşleşen partiler bulmak zor olduğundan, bu işlemi yapan bir kurum, kendine ait parayı kullanarak, opsiyon satın almak isteyenler için karşı parti rolünü üstlenir. Bunu yaparken de, opsiyon fiyatını belirlemek için kompleks modellemeler kullanır, ki günün sonunda kâr elde edebilsin. 

DeFi ürünlerinde ise eşten eşe işlem gerçekleştirmek çok zor.  Çünkü, bir tavuk-yumurta kısır döngüsüne girme durumunuz var: İnsanlar işlem yapabilmek için opsiyonların makul ücretler ile fiyatlanmasını bekliyorlar. İyi fiyatlama olabilmesi için gerekli en temel girdi likidite. Zira, ancak likidite olduğunda, yani alım ve satım opsiyonu almak isteyen ile onların istedikleri bu opsiyonu satmayı kabul eden yeteri sayıda ve büyüklükte karşı parti olduğunda, sistem işleyebiliyor. DeFi protokollerde bu tip likiditeyi oluşturmak çok zor. Neden? Çünkü özünde DeFi protokolleri birer aracılar, kapital tutmuyorlar, para emanete almıyorlar. Böyle olunca da insanlar gelmiyorlar. 

#### Ve işte yine geldik DeFi'yi kurtaran havuz modeline... 

İşte DeFi piyasaları bu kısır döngüyü "havuz modeli" ile aştılar. Bu havuzların ilk örneklerinden biri Uniswap oldu: 

Kendi merkeziyetsiz kripto borsasında yeterince likidite sağlayamayınca, önce yatırımcılarının koyduğu para ile havuzlar kurdu. Havuzlar likidite sorununa bir parça çözüm oldular ancak büyüklüğü bir türlü istenen seviyelere gelmedi. Sonrasında, Compound'un başlattığı likidite sağlama karşılığı token verme hareketi, likidite sorununu çözme konusunda DeFi platformlara önemli bir eşik atlattı. Benzer modeli Uniswap da uyguladı ve bakın bir yılı aşkın süredir yerlerde sürünen likidite nasıl bir şekil aldı.: 

 | ![uniswap_tvl](/assets/uniswap_tvl_v5.png)|
|:--:| 
| *Uniswap için kilitlenen para miktarı Kaynak:[DeFiPulse](https://defipulse.com/)*|

Token yani teşvik verme başlangıçta "ama bu hormon vermek ile aynı!" şeklinde tepkiler ile karşılaştı. Bu tepkilerde bir parça haklılık payı olduğu Kasım ayında biten token teşviğinin bitmesi ile birlikte TVL'nin ciddi bir şekilde azalmasını getirdi. Ancak birkaç ay içinde bu likidite geri geldi. Yani, arabaya dışarıdan verilen kablo ile sağlanan itici güç, içeride duran atıl gücü çalışır hale getirdi. 

Options piyasasındaki oyunculardan Opyn, yukarıda bahsettiğimiz eşten eşe opsiyonlar ile oyuna başlamışken, Hegic, kendi opsiyon platformunu Uniswap gibi bir havuz şeklinde kurdu. Sonrasında da 2020 Eylül ayı içinde kendi platformuna likidite sağlayanlara yönelik HEGIC token çıkardı. Bu sayede, Hegic üzerindeki kilitli miktar ciddi bir artış kazandı: 

 | ![hegic_vs_opyn_TVL](/assets/hegic_vs_opyn_tvl_v3.png)|
|:--:| 
| *Hegic ve Opyn'da kilitlenen toplam miktar Kaynak:[DeFiPulse](https://defipulse.com/)*|

Yalnızca kilitli miktar değil ilgi çekici olan. Bu parayı havuzlara kilitleyenlerin aldıkları komisyon gelirleri de üç ay gibi kısa bir sürede ciddi bir rakama ulaştı: 

 | ![hegic_revenues](/assets/hegic_revenues.PNG)|
|:--:| 
| *Hegic 2020 yılı üç aylık gelirler Kaynak:[Messari](https://messari.io/)*|


#### Sistem nasıl çalışıyor?

Sistemde iki ana aktör var. 

Bunlardan birincisi, opsiyon satın almak isteyenler. Bunlara opsiyon alan/sahip olan (holder) deniyor. Ne satın alıyorlar?  ETH ya da BTC'yi herhangi bir vade için alma (call) ya da satma (put) hakkını. Nereden alıyorlar bu opsiyonu? Kendilerine fiyat veren bir akıllı kontrat var, bu kontratın arkasında da bir havuz (daha önce defalarca örneğini verdiğimiz havuzları hatırlarsınız, hatırlamayanlar [Uniswap](/genel/2020/09/15/nedir-bu-uniswap.html) ve [Synhetix](/genel/2020/08/28/Defi-turev-piyasasi-synthetix-nasil-calisiyor.html) havuzlarına bir göz atabilir dilerlerse). 

Bu kişiler, akıllı kontratın verdiği fiyatı beğenirler ise, istedikleri opsiyonu yaratıp satın alıyorlar. ([MakerDAO'nun sisteminde kullanıcının kredi yaratması](https://turansert.com/genel/2019/02/15/MakerDAO-kredi-kullaniminda-cigir-acar-mi.html) gibi, ki buna "mint" yani para basmak da deniyor)

İkincisi ise, yukarıdaki bu havuza likidite sağlayanlar. Yani, yukarıdaki opsiyonları satanlar, ki onlara da opsiyon yazan/çıkaran (writer) deniyor. Ancak bu kişiler, herhangi bir şekilde opsiyon yazmıyorlar. Yaptıkları sadece bu havuzun suyu olan likiditeyi koymak. Havuza likidite sağlayarak ne kazanç elde ediyorlar? Öncelikle, yukarıdaki satılan opsiyonların ücretlerini kazanıyorlar. Riskleri ise, opsiyonun kullanılması durumunda oluşan zarar...

Özet olarak, opsiyon fiyatları bir algoritma ile belirleniyor. Yukarıdaki birinci grup, opsiyon satın alırken prim ödüyor. Bu primler havuza gidiyor. Opsiyon satın alanlar opsiyonu kullanırlar ise, bunun ödemesini akıllı kontrat havuzdan alarak yapıyor. Havuzda kalan miktar, havuza likidite sağlayanlar arasında bölüşülüyor. 

### Hegic'in tokeni HEGIC
Hegic'in yarattığı HEGIC tokenın iki farklı kullanım aracı var, ki bu diğer DeFi projelere oldukça yakın: 

Birincisi, HEGIC tokenlar sisteme likidite sağlamak için 'rehin' edilebiliyor (staking). Bunun karşılığında, hem yukarıda bahsettiğimiz prim ödemelerinin içinden ödenen opsiyonlar sonrası ortaya çıkan kârı alıyorlar. Ayrıca, rehin vermeleri karşılığı Hegic tarafından ödül olarak verilen ekstra tokenları kazanma şansına sahipler.  

İkincisi ise bu tokenlar sayesinde ileride Hegic sisteminin yönetimine dahil olma şansına sahip olacaklar. Hegic kurucusu Wintermut, token sahibi aktif kullanıcı sayısının 100'ü aşması ile birlikte sistemin yönetimini yavaş yavaş token sahiplerine geçirmeyi planlıyor. 

### Hegic ve Opyn farkları
Merkeziyetsiz finans alanında faaliyet gösteren iki büyük oyuncu Hegic ile Opyn arasında birkaç temel fark var:

Öncelikle Hegic, yukarıda da bahsettiğimiz gibi opsiyonların vade tarihine kadar herhangi bir noktada kullanılmasına izin veriyor. Finans piyasasındaki jargonu ile Amerikan opsiyonu yönetimini kullanıyor. Opyn'de ise opsiyonları sadece vade sonunda kullanabiliyorsunuz. Buna ise Avrupa opsiyonu denmekte.  

Bunun yanında, Opyn havuz kullanmak yerine yukarıda bahsettiğimiz eşten-eşe modelini kullanıyor. Yani, opsiyon satın alanların yanında, opsiyon satanlar (yazanlar) var. Bu çok da pratik bir yöntem değil. Zira, opsiyonun içerdiği pek çok parametreyi (süre, oran, hedef fiyat, opsiyon prim değeri) satıcının belirlemesi gerekiyor. Bu hem zahmetli bir süreç, hem de alıcıların istediği parametreler ile uyumlu olmayabiliyor.

Bu iki temel fark, aslında neden Hegic platformunun daha geç başlamış olsa bile Opyn'e fark attığını anlatmaya yetiyor. Hegic, DeFi dünyasındaki son gelişmeleri yakından takip ederek daha geniş bir kitleye ulaşmış ve likidite anlamında rakibine üstünlük sağlamış görünüyor. 

### Sonuç 

DeFi dünyası 2020 yılı içinde önündeki engelleri yavaş yavaş aşmaya başladı.  Bu alana yeni girmiş olan Hegic, merkeziyetsiz finansın takas borsası ya da türev piyasalarındaki platformların geniş kesimlere yayılmak amacıyla kullandığı araçları hızlı bir şekilde sistemine kattı. Bunun sayesinde, yaşadığı türlü badirelere rağmen hızlı bir büyüme gösterdi. Bakalım, 2021 yılı içinde bu büyümeyi devam ettirebilecek mi? Hep birlikte yaşayarak göreceğiz. 



*Not: Hegic, Opyn ve diğer opsiyon sağlayıcılar ile ilgili daha derin bilgi için [şu Medium yazısına](https://medium.com/coinmonks/a-comparison-of-decentralized-options-platforms-140b1421c71c) ve o makalenin devamı niteliğinde güncellemeler de içeren [şu yazıya](https://medium.com/coinmonks/an-update-of-a-comparison-of-decentralized-options-platforms-91b14d3a6170) göz atabilirsiniz.*
