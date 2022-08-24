---
layout: post
title:  "Ethereum sansüre nasıl yanıt verecek?"
date:   2022-09-29 17:17:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Bu yazımızda, önümüzdeki dönemde çok tartışılacak bir konuya, olası bir sansürün Ethereum dünyasında yaratacağı sarsıntılara değineceğiz. 

Bundan önceki birkaç yazıda önce Tornado Cash'in yasaklanması sonrası blokzincirler üzerindeki uygulamaların getirdiği kısıtlamalardan bahsetmiş, sonrasında ise DeFi dünyasını bundan sonra nelerin beklediğine değinmiştik. 

Şu ana kadar yaşananlar daha çok üst tarafta kullanıcı seviyesinde yapılan engellemeler ve etkinlikleri oldukça kısıtlı. Asıl sıkıntı yaratabilecek konu Ethereum’un platform seviyesinde yaşanabilecek sıkıntılar. Neler olabilir gelin hızlıca bir göz atalım. 

### Ethereum seviyesinde sansür mü? O nasıl olabilir?

ABD'nin kara para aklama konusundaki otoritelerinden OFAC'ın Tornado Cash ve onunla ilişkili hesapları yasaklı listesine alması sonrası, pek çok DeFİ uygulamasının bu listede yer alan yasaklı hesaplara erişimi engellediğinden bahsetmiştik. 

| ![no_entry](/assets/cabinets-283847_800.jpg)|
|:--:| 
| *Image by [Holger Langmaier](https://pixabay.com/users/holgersfotografie-47038/) from [Pixabay](https://pixabay.com/)*|

Buradaki bir ayrıntıyı tekrar hatırlatalım: DeFi uygulamaları (ya da protokolleri) yasaklı adreslerin kullanıcı ön yüzlerine ulaşımını engelliyorlar (yani kendilerine ait web sitelerine erişimi kapatıyorlar).  Bu protokollere ait akıllı kontratlar ise bir kez Ethereum zincirine yüklendikten sonra geliştiricinin elinden çıkmış oluyor. Dolayısıyla bir adres yasaklı bile olsa Ethereum blokzinciri ile direkt ilişikiye girerek akıllı kontratı yani DeFi uygulamasını kullanabiliyor.

Peki bir adres Ethereum ile nasıl ilişkiye giriyor? Bu gerek Ethereum gerekse Bitcoin üzerinde madenciler aracılığıyla oluyor. Kullanıcı isteğini Ethereum sistemine gönderdiğinde bu istekler bir havuzda birikiyor ve madenciler tarafından balya balya toplanıp işleniyor. Yakın zamanda (işler yolunda giderse 15 Eylül 2022'de) Ethereum'da bu madencilerin yerini onaylayıcılar alacak ve aynı işlevi madenciler yerine onlar yapacaklar (şu an kullanılan madencilerin olduğu sistemin adı iş kanıt İngilizcesi ile proof-of-work PoW, yeni sistemin adı ise ‘hisse kanıtı’ ingilizcesi ile ‘proof of stake’ -- PoS)

Kritik soru şu: **‘OFAC ya da benzeri bir kurum, madenci ya da onaylayıcılardan Tornado Cash ya da benzeri kara listedeki bir hesaptan gelen herhangi bir isteği havuzdan çekmemesini yani sansür uygulamasını isterse ne olacak?’** Aslına bakarsanız bu şu anda bile pratikte yaşanan bir durum: Geçmişte en büyük Bitcoin madencilerinden ABD bazlı Marathon Digital’ın yasaklı cüzdanlardan gönderilen paraları dahil etmeden yarattığı bloklar olmuştu[LINK] (Marathon Digital daha sonra bu uygulamadan vazgeçtiğini açıkladı[LINK]. Ethereum'da da en büyük madenci havuzu olan Ethermine'nın benzer şekilde OFAC yaptırımına dahil edilmiş mimli adreslerden gelen işlemleri bloklara almadığı [söylentileri dolaşıyor](https://twitter.com/takenstheorem/status/1560479290264883201).  Blokzincirin izin gerektirmeyen yapısından dolayı kimse kimseyi herhangi bir konu için ‘teknik’ olarak zorlayamıyor. 

Burada temel konu, madencilerin ya da onaylayıcıların ne kadarının böyle bir sansürü uygulayacağında kilitleniyor. Eğer bunlar ufak bir kısım ise büyük bir sorun yok; o madenci tarafından işlenmeyen istek bir başka madenci tarafından bir sonraki blokta işlenerek sorun kendi kendine çözülüyor. Blokzincirde temel varsayım, madencilerin temel motivasyonunun ekonomik olduğu ve yeterli seviyede bir işlem ücreti ödendiğinde o işlemin er ya da geç sistem tarafından onaylanacağı şeklinde. Ama eğer madencilerin ciddi bir kısmı bu şekilde sansüre başlar ise o zaman altyapı seviyesinde bir sansür kendiliğinden oluşuyor. 

Ethereum açısından bu varsayımsal durum, hisse kanıtı sistemine geçince daha yüksek bir ihtimal olarak ortaya çıktı. Zira, hisse kantı sisteminde onaylayıcı olmak için minimum 32 ETH yatırmak, sonra da işlemleri onaylamak için sürekli açık duran bir bilgisayar ile belli programları çalıştırmak gerekiyor (ve bunun karşılığında da hem yıllık [%4 civarı bır faiz](https://www.stakingrewards.com/earn/ethereum-2-0/) hem de onaylanan bloklar üzerinden komisyon alınıyor). Pek çok insan, bu zahmete girmemek için ellerindeki ETH'leri çok ufak bir ücret ödeyerek aracı kurumların idaresine veriyorlar. Bu kurumlar da her bir 32 ETH için bir node kurarak müşterilerin kendilerine verdiği paraları ETH sistemine kilitliyorlar. 

İşte bu aracılar genelde merkezi kurumlar (ağırlıkla kısmı kriptopara borsaları) ve bir çoğu da ABD merkezli. Yarın öbür gün OFAC bu kurumlara ‘hadi bakalım, şu adreslerden gelen işlem taleplerini görmezden gelin' derse ne olacak? İşte Tornado Cash olayı patlak verdiğinden beri Ethereum topluluğunun tartıştığı konu bu. 

Burada temel olarak birkaç soru sorup onları yanıtlamaya çalışalım dilerseniz: 

- Merkezi kurumlar kendilerine gelen sansür baskısı karşısında ne yapabilirler? 
- Sansürü kabul edenler ve etmeyenlerin olduğu bir sistem nasıl çalışır? Sansürü kabul edenler ile etmeyenler birbirinden ayrılabilir mi? Ayrılırsa bu nasıl olur?
- Eğer Ethereum ikiye ayrılırsa bu üzerindeki uygulamalar ve kullanıcılar için ne anlama gelir?

Gelin bu üç soruya cevap arayalım şimdi de: 

### Merkezi kurumlar sansür baskısı gelirse nasıl davranırlar? 
Şu an Ethereum PoS sisteminde ETH yatırmış onaylayıcılarının yaklaşık olarak %66.1'i kurumlardan oluşuyor. Aşağıdaki tabloda bu kurumların dağılımı görebilirsiniz:

| ![ETH_Stakers](/assets/Ethereum_stakers_800_v2.png)|
|:--:| 
| *Ethereum PoS onaylayıcıları (22 Ağustos 2022 itibariyle).  Kaynak: [Rated Network](https://www.rated.network/ )*|

Bu oldukça yüksek bir rakam. Bu kurumlar, OFAC tarafıdan bir yasaklı listesi yayınlanırsa ne yapacaklar? Tornado Cash sonrası pek çok DeFi platformunun hızlıca adres yasaklaması bize nasıl davranacakları konusunda bir ipucu veriyor. Yine de tabloda birkaç noktaya dikkat çekmekte fayda var:

En büyük kurum olarak görülen Lido Finance, aslına bakarsanız bir DAO ve esasında [29 adet onaylayıcıdan oluşuyor](https://mainnet.lido.fi/#/lido-dao/0x55032650b14df07b85bf18a3a3ec8e0af2e028d5/) Lido’nun bu 29 onaylayıcısından ellerindeki makineleri nasıl kullanacağı konusunda şu anda bir yaptırım gücü bulunmuyor. (Ethereum sisteminin rehin edilen tokenlerin çözülmesine izin verdiği noktada - ki bunun PoS başladıktan yaklaşık altı ay sonra olabileceği söyleniyor, DAO bu onaylayıcılardan belli isteklerde bulunabilir ve buna uymayanların ayrılıp kendi başlarına işlem yapmalarını isteyebilir). Diğer yandan yine büyüklerden Coinbase CEO'su Brian Amstrong ise bir [tweet mesajında](https://twitter.com/brian_armstrong/status/1560016827253551104) engelleme talebi gelmesini düşük bir ihtimal olarak gördüğünü, ama gerçekleşirse bu hizmetlerini kapatacaklarını belirtiyor (sansürü kabul etmek ile kapatmak arasında, kanuni yollara başvuracakları bir üçüncü yol olabileceğini ekleyerek).

Diğer kurumların ne yapacaklarını şu an bilemiyoruz. Ama yine de şu an ‘karara uymam, kapatırım’ diyen Brian Amstrong yarın kendisine ‘emir’ geldiğinde bunu gerçekten yapabilecek mi?  

### Sansürü kabul edenler ve etmeyenler olduğunda ne olacak? 
Peki ya Ethereum topluluğunun bir kısmı sansürü kabul eder diğer bir kısmı etmezse? Yani topluluk ikiye bölünürse? Olabilir mi böyle bir durum? İhtimal düşük gibi görünse de pek de olasılık dışı değil bu durum:

Şu anki ilk nabız yoklamaları bireysel olarak insanların böyle bir sansüre karşı olduklarını gösteriyor. Örnek olarak Ethereum topluluğunun önde gelen isimlerinden Eric Wall’un [Twitter üzerinden yaptığı bir kamuoyu yoklamasında](https://twitter.com/ercwl/status/1559265839723040769) %60’ın eğilimi bu yönde. Ethereum’un köklerinin Bitcoin’e dayandığı düşünülürse toplulukta hâlâ etkin olan isimlerin (bunlara kuruculardan Vitalik de dahil) böyle düşünmesi normal. “Dünyanın bilgisayarı” olarak isteyen herkesin “izin gerektirmeden” içine girebildiği bir ortam vaat ederken şimdi birilerinin iznine tabi olmayı istemek olayın temel felsefesine aykırı. 

Yine de unutmamak lazım ki, Ethereum topluluğu artık bu bireylerin çok ötesinde geçmiş durumda. Bu dünyada artık ciddi bir kurumsal ağırlığı var. Bu kurumların pek çoğu merkezi ve orada çalışanların bulundukları ülkelerin regülasyonlarına tâbi olduklarını unutmamak gerek. Kurumsal dünya içinde idealleri uğruna hapis yatmayı göze alacak ne kadar insan var sizce? Atalarımızın da dediği gibi ‘davulun sesi uzaktan hoş gelir’, ya da ‘bekara boşanmak kolaydır’ (Yoksa siz Hollanda’daki geliştiricinin gerçekten yasa dışı bir iş yaptığı için mi tutuklandığını düşündünüz?)

İşte bu nedenle kamuoyunun ikiye bölünmesi ihtimal dahilinde. Bu yazıda bunun teknik anlamda nasıl yapılacağına değil gerçekleşmesi halinde uygulamalar ve kullanıcılar açısından getireceği komplikasyonlara değineceğiz. Bir ayrılma olması durumunda bu, ağırlığa sahip grubun kalması diğer grubun ise bir çatallanma ile ayrı bir zincire geçmesi şeklinde olacak.

Böyle bir durumda özellikle sansüre karşı olan ekibin, karşı grubun rehin verdiği varlıkları dondurmaktan (oy vermesine engel olmak), bu varlıkların bir kısmını ya da tamamını yakmaya yani bir başka deyişle nükleer silah kullanmaya kadar verebileceği farklı tepkiler olabilir. (Bu son görüşü savunanlar, ABD’nin II. Dünya Savaşı’nda Japonya’ya atom bombası atmasından sonra bir daha 80 yıl boyunca nükleer silah kullanılmamasının, bu yöntemin ne kadar etkili olduğu gösterdiğini belirtiyorlar.)

### Ayrılma uygulamalar ve kullanıcılar açısından neler getirebilir?

Buradaki belirsiz nokta topluluğun diğer önemli paydaşı olan geliştiricilerin alacağı pozisyon. Zira bir çatallanma olursa her iki platformda ayrı birer uygulama olacak. Yazılımcılar kaynak ve eforlarını hangi zincire harcayacaklar? İlk gelen tepkiler yazılımcıların sansürsüz tarafı seçecekleri yönünde olsa da, geliştiricilerden kimlikleri belli olanlar regülasyonlara karşı çıkan zincirde yer alıp kariyerlerini ve hayatlarını riske edecekler mi? Bir diğer öngörü ise piyasaya pek çok ‘yeni ve anonim’ geliştiricinin gelmesini beklemek olacak. 

İkinci belirleyici nokta ise stabil para çıkaran kurumlar tarafında yaşanacak. Merkeziyetsiz dünyadaki stabil paraların [yaklaşık %90'ı](https://www.theblock.co/data/decentralized-finance/stablecoins) merkezi stabil paralar olan USDT, USDC ve BUSD üzerinde. Stabil para üreticileri her iki platformu da destekleyemez, zira ellerinde sadece bir paraya yetecek karşılık var. Bu kurumların merkezi olması nedeniyle sansürü kabul eden topluluğa yakın olma ihtimali daha yüksek. Ya da bir şekilde kullanıcılara iki taraftan birini seçmelerini sağlayacak bir çözüm yolu önerecekler. 

Kullanıcılar açısından da ilginç bir durum söz konusu. Eğer iki ayrı zincir olursa kullanıcıların varlıkları iki farklı zincirde çoklanacak. Burada iki varlıktan rağbet gören hangisi ise değer o tarafta yükselecek. Diğer zincirdeki varlıkların bir değeri kalabilir ya da sıfıra inebilir. Kullanıcılar hangisini seçecek? Nereden bakarsanız bakın karmaşık bir durum. 

Bu arada hemen belirtelim bu durum sadece Ethereum’u değil diğer tüm zincirleri de benzer şekilde etkileyebilir. Hatta iş kanıtı yöntemini kullanan Bitcoin’in madencilerinin %35’inin ABD’de olduğunu, üstelik bu madencilerin kurulu tesisleri olması nedeniyle bu gücü başka yere taşımanın çok daha güç olduğunu, dolayısıyla bu madencilerin de benzer bir risk altında olduğunu belirtelim. 

### Ama durun! Bütün bunlar bir olasılık aslında!
Buraya kadar yazdıklarımıza bakarak geleceğin oldukça karanlık olduğunu düşünebilirsiniz. Öyle ya, iki farklı zincir, ortalık toz duman, kim nerede ve ne tarafta belli değil. Karmakarışık bir dünya. 

Haklısınız ancak hemen iç karartmaya gerek yok. Öncelikle şu anda hükümetlerden gelen platform seviyesinde bir baskı henüz yok. Açıkçası OFAC’ın Tornado Cash hareketinin kamuoyuna “bakın aksiyon aldık” demekten öte bir etkisi olmadı. Kendilerinin bu dünyayı tam anladıklarını düşünmek fazla iyimser bir bakış açısı olur. OFAC tarafından yeni bir yaptırım gelene kadar kripto dünyası da haliyle karşı aksiyona geçecek (lobi faaliyeti, seçimlerde kripto dostu adayları destekleme gibi). 

Sansürü kabul edecek kurumsal yapılar olsa da, bu oyuncular enayi değiller. Elbette böyle bir durumun varlıkların değerine negatif etki yapacağının farkındalar. Dolayısıyla, hiç böyle bir bölünmeye girmeden fonlarında tuttukları kriptoparaları elden çıkarmayı düşünebilirler. Bu da en fazla ETH’nin fiyatında ciddi bir düşüş yaratır ama zincirin uzun vadeli sağlığına zarar vermez. 

Kaldı ki, dünya ABD’den ibaret değil. Bakalım onun koyduğu yaptırım listesini uygulayacak bir zinciri diğer ülkeler kabul edecekler mi?

Burada en önemli konu sosyal konsensusun nerede oluşacağı. Şu an görünen topluluğun Ethereum’un nötr bir altyapı olarak kalması yönünde bir eğilimi olduğu. Ayrıca sisteme gönderilen işlemlerin kimden geldiğinin gizlenmesi yoluyla onaylayıcıların sansür uygulamalarını imkansız kılacak geliştirmeler de söz konusu*. 

Dolayısıyla şahsi görüşüm, sosyal konsensus sayesinde ikiye ayrılmaya gidilmeden soruna bir çözüm bulunacağı yönünde. 

### Sonuç 
OFAC tarafından getirilen yasaklamalar Ethereum dünyasında büyük tartışmalar başlattı. Böyle tartışmaların şimdiden yapılması önemli, zira kafayı devekuşu gibi kuma gömmenin bir faydası yok (küresel iklim konusunda olduğu gibi). Soruna çare bulunana kadar zorlu bir yoldan geçilmesi bu sırada ETH’nin değerinde ciddi dalgalanmalar olması muhtemel. Yine de bir çözüm bulunduktan sonra Ethereum ve kripto dünyasının bu olaydan çok daha güçlenerek çıkacağını görmemiz çok olası. İzleyip göreceğiz. 

*Not 1: Burada özellikle madenciler konusunda yer alan ve işlemleri önerenler ile onaylayanların ayrılmasına yönelik halihazırda tartışılan [bir öneri](https://ethresear.ch/t/proposer-block-builder-separation-friendly-fee-market-designs/9725) de bulunmakta*

*Not 2: Bu yazı ilk olarak 29 Ağustos 2022'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı]()*

*Not 3: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

