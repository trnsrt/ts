---
layout: post
title:  "Ethereum sansüre nasıl yanıt verecek?"
date:   2022-08-31 17:17:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Geçtiğimiz yazılarda önce Tornado Cash'in yasaklanması sonrası blokzincirler üzerindeki uygulamaların getirdiği kısıtlamalardan [bahsetmiş](/genel/2022/08/20/tornado-cash-olayi.html), sonrasında ise DeFi dünyasını bundan sonra nelerin beklediğine [değinmiştik](/genel/2022/08/27/tornado-cash-olayi-defiyi-nasil-etkiler.html). 

Şu ana kadar yaşananlar daha çok üst tarafta kullanıcı seviyesinde yapılan engellemeler ve etkinlikleri oldukça kısıtlı. Asıl sıkıntı yaratabilecek konu Ethereum’un platform seviyesinde yaşanabilecek sıkıntılar. Neler olabilir gelin hızlıca bir göz atalım. 

### Ethereum seviyesinde sansür mü? O nasıl olabilir?

ABD'nin kara para aklama konusundaki otoritelerinden OFAC'ın Tornado Cash ve onunla ilişkili hesapları yasaklı listesine alması sonrası, pek çok DeFİ uygulamasının bu listede yer alan yasaklı hesaplara erişimi engellediğinden bahsetmiştik. 

| ![no_entry](/assets/cabinets-283847_800.jpg)|
|:--:| 
| *Image by [Holger Langmaier](https://pixabay.com/users/holgersfotografie-47038/) from [Pixabay](https://pixabay.com/)*|

Buradaki bir ayrıntıyı tekrar hatırlatalım: DeFi uygulamaları (ya da protokolleri) yasaklı adreslerin kullanıcı ön yüzlerine ulaşımını engelliyorlar (yani kendilerine ait web sitelerine erişimi kapatıyorlar).  Bu protokollere ait akıllı kontratlar ise bir kez Ethereum zincirine yüklendikten sonra geliştiricinin elinden çıkmış oluyor. Dolayısıyla bir adres yasaklı bile olsa Ethereum blokzinciri ile direkt ilişikiye girerek akıllı kontratı yani DeFi uygulamasını kullanabiliyor.

Peki bir adres Ethereum ile nasıl ilişkiye giriyor? Bu gerek Ethereum gerekse Bitcoin üzerinde madenciler aracılığıyla oluyor. Kullanıcı isteğini Ethereum sistemine gönderdiğinde bu istekler bir havuzda birikiyor ve madenciler tarafından balya balya toplanıp işleniyor. Yakın zamanda (işler yolunda giderse 15 Eylül 2022'de) Ethereum'da bu madencilerin yerini onaylayıcılar alacak ve aynı işlevi madenciler yerine onlar yapacaklar (şu an kullanılan madencilerin olduğu sistemin adı 'iş kanıtı' ingilizcesi ile proof-of-work PoW, yeni sistemin adı ise ‘hisse kanıtı’ ingilizcesi ile ‘proof of stake’ -- PoS)

Kritik soru şu: **‘OFAC ya da benzeri bir kurum, madenci ya da onaylayıcılardan Tornado Cash ya da benzeri kara listedeki bir hesaptan gelen herhangi bir isteği havuzdan çekmemesini yani sansür uygulamasını isterse ne olacak?’** 

Aslına bakarsanız bu şu anda bile pratikte yaşanan bir durum: Geçmişte en büyük Bitcoin madencilerinden ABD bazlı Marathon Digital’ın yasaklı cüzdanlardan gönderilen paraları dahil etmeden yarattığı bloklar [olmuştu](https://www.coindesk.com/tech/2021/05/07/marathon-miners-have-started-censoring-bitcoin-transactions-heres-what-that-means/) (Marathon Digital daha sonra bu uygulamadan vazgeçtiğini [açıkladı](https://www.nasdaq.com/articles/bitcoin-mining-company-marathon-will-stop-censoring-transactions-start-signaling-for). Ethereum'da da en büyük madenci havuzu olan Ethermine'nın benzer şekilde OFAC yaptırımına dahil edilmiş mimli adreslerden gelen işlemleri bloklara almadığı [söylentileri dolaşıyor](https://twitter.com/takenstheorem/status/1560479290264883201).  Blokzincirin izin gerektirmeyen yapısından dolayı kimse kimseyi herhangi bir konu için ‘teknik’ olarak zorlayamıyor. 

Burada temel konu, madencilerin ya da onaylayıcıların ne kadarının böyle bir sansürü uygulayacağında kilitleniyor. Eğer bunlar ufak bir kısım ise büyük bir sorun yok; o madenci tarafından işlenmeyen istek bir başka madenci tarafından bir sonraki blokta işlenerek sorun kendi kendine çözülüyor. Blokzincirde temel varsayım, madencilerin temel motivasyonunun ekonomik olduğu ve yeterli seviyede bir işlem ücreti ödendiğinde o işlemin er ya da geç sistem tarafından onaylanacağı şeklinde. Ama eğer madencilerin ciddi bir kısmı bu şekilde sansüre başlar ise o zaman altyapı seviyesinde bir sansür kendiliğinden oluşuyor. 

Ethereum açısından bu varsayımsal durum, hisse kanıtı sistemine geçince daha yüksek bir ihtimal olarak ortaya çıktı. Zira, hisse kanıtı sisteminde onaylayıcı olmak için minimum 32 ETH yatırmak, sonra da işlemleri onaylamak için sürekli açık duran bir bilgisayar ile belli programları çalıştırmak gerekiyor (ve bunun karşılığında da hem yıllık [%4 civarı bir faiz](https://www.stakingrewards.com/earn/ethereum-2-0/) hem de onaylanan bloklar üzerinden komisyon alınıyor). Pek çok insan, bu zahmete girmemek için ellerindeki ETH'leri çok ufak bir ücret ödeyerek aracı kurumların idaresine veriyorlar. Bu kurumlar da her bir 32 ETH için bir node kurarak müşterilerin kendilerine verdiği paraları ETH sistemine kilitliyorlar. 

İşte bu aracılar genelde merkezi kurumlar (ağırlıkla kısmı kriptopara borsaları) ve bir çoğu da ABD merkezli. Yarın öbür gün OFAC bu kurumlara ‘hadi bakalım, şu adreslerden gelen işlem taleplerini görmezden gelin' derse ne olacak? İşte Tornado Cash olayı patlak verdiğinden beri Ethereum topluluğunun tartıştığı konu bu. 

Burada temel olarak birkaç soru sorup onları yanıtlamaya çalışalım dilerseniz: 

- Merkezi kurumlar kendilerine gelen sansür baskısı karşısında ne yapabilirler? 
- Sansürü kabul edenler ve etmeyenlerin olduğu bir sistem nasıl çalışır? Sansürü kabul edenler ile etmeyenler birbirinden ayrılabilir mi? Ayrılırsa bu nasıl olur?
- Eğer Ethereum ikiye ayrılırsa bu üzerindeki uygulamalar ve kullanıcılar için ne anlama gelir?

Gelin bu üç soruya cevap arayalım şimdi de: 

### Merkezi kurumlar sansür baskısı gelirse nasıl davranırlar? 
Şu an Ethereum PoS sisteminde ETH yatırmış onaylayıcılarının yaklaşık olarak %66.1'i kurumlardan oluşuyor. Aşağıdaki tabloda bu kurumların dağılımını görebilirsiniz:

| ![ETH_Stakers](/assets/Ethereum_stakers_800_v2.png)|
|:--:| 
| *Ethereum PoS onaylayıcıları (22 Ağustos 2022 itibariyle).  Kaynak: [Rated Network](https://www.rated.network/ )*|

Bu oldukça yüksek bir rakam. Bu kurumlar, OFAC tarafıdan bir yasaklı listesi yayınlanırsa ne yapacaklar? Tornado Cash sonrası pek çok DeFi platformunun hızlıca adres yasaklaması bize nasıl davranacakları konusunda bir ipucu veriyor. Yine de tabloda birkaç noktaya dikkat çekmekte fayda var:

En büyük kurum olarak görülen [Lido Finance](https://lido.fi/), aslına bakarsanız bir DAO ve esasında [29 adet onaylayıcıdan oluşuyor](https://mainnet.lido.fi/#/lido-dao/0x55032650b14df07b85bf18a3a3ec8e0af2e028d5/). Lido'nun, bu 29 onaylayıcısı üzerinde ellerindeki makineleri nasıl kullanacakları konusunda şu anda bir yaptırım gücü bulunmuyor. (Ethereum sisteminin rehin edilen tokenlerin çözülmesine izin verdiği noktada - ki bunun PoS başladıktan yaklaşık altı ay sonra olabileceği söyleniyor, DAO bu onaylayıcılardan belli isteklerde bulunabilir ve buna uymayanların ayrılıp kendi başlarına işlem yapmalarını isteyebilir). Diğer yandan yine büyüklerden Coinbase CEO'su Brian Armstrong ise bir [tweet mesajında](https://twitter.com/brian_armstrong/status/1560016827253551104) engelleme talebi gelmesini düşük bir ihtimal olarak gördüğünü, ama gerçekleşirse bu hizmetlerini kapatacaklarını belirtiyor (sansürü kabul etmek ile kapatmak arasında, kanuni yollara başvuracakları bir üçüncü yol olabileceğini ekleyerek).

Diğer kurumların ne yapacaklarını şu an bilemiyoruz. Ama yine de şu an ‘karara uymam, kapatırım’ diyen Brian Armstrong yarın kendisine ‘emir’ geldiğinde bunu gerçekten yapabilecek mi?  

### Sansürü kabul edenler ve etmeyenler olduğunda ne olacak? 
Peki ya Ethereum topluluğunun bir kısmı sansürü kabul eder diğer bir kısmı etmezse? Yani topluluk ikiye bölünürse? Olabilir mi böyle bir durum? İhtimal düşük gibi görünse de pek de olasılık dışı değil bu durum:

Şu anki ilk nabız yoklamaları bireysel olarak insanların böyle bir sansüre karşı olduklarını gösteriyor. Örnek olarak Ethereum topluluğunun önde gelen isimlerinden Eric Wall’un [Twitter üzerinden yaptığı bir kamuoyu yoklamasında](https://twitter.com/ercwl/status/1559265839723040769) %60’ın eğilimi bu yönde. Ethereum’un köklerinin Bitcoin’e dayandığı düşünülürse toplulukta hâlâ etkin olan isimlerin (bunlara kuruculardan Vitalik de dahil) böyle düşünmesi normal. “Dünyanın bilgisayarı” olarak isteyen herkesin “izin gerektirmeden” içine girebildiği bir ortam vaat ederken şimdi birilerinin iznine tabi olmayı istemek olayın temel felsefesine aykırı. 

Yine de unutmamak lazım ki, Ethereum topluluğu artık bu bireylerin çok ötesine geçmiş durumda. Bu dünyada artık ciddi bir kurumsal ağırlığı var. Bu kurumların pek çoğu merkezi ve orada çalışanların bulundukları ülkelerin regülasyonlarına tâbi olduklarını unutmamak gerek. Kurumsal dünya içinde idealleri uğruna hapis yatmayı göze alacak ne kadar insan var sizce? Atalarımızın da dediği gibi ‘davulun sesi uzaktan hoş gelir’, ya da ‘bekara boşanmak kolaydır’ (Yoksa siz Hollanda’daki geliştiricinin gerçekten yasa dışı bir iş yaptığı için mi tutuklandığını düşündünüz?)

### Arkası yarın
Dolayısıyla, Ethereum topluluğunun ikiye bölünmesi düşük de olsa bir ihtimal. Önümüzdeki yazımızda bu durumun geliştiriciler ve kullanıcılar açısından ne ifade edeceğine bakacağız. 


*Not 1: Bu yazı ilk olarak 31 Ağustos 2022'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/ethereum-sansure-nasil-yanit-verecek/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*
