---
layout: post
title:  "Ethereum Çatallanması Kullanıcı ve Geliştiriciler İçin Ne Getirir?"
date:   2022-09-07 17:17:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Bu yazımızda, Ethereum'un olası çatallanmasının uygulamalar ve kullanıcılar açısından ne gibi etkileri olabileceğine bakacağız.  

Geçtiğimiz haftaki yazıda, Tornado Cash sonrasında Ethereum'un protokol seviyesinde çatallanmasından bahsetmiştik. Hemen bir ayrıntıya dikkat çekelim: Bahsettiğimiz konu, Ethereum'un önümüzdeki günlerde hisse-kanıtı sistemine (ingilizcesi PoS - Proof of Stake) geçmesi sonrası, bu durumdan hoşnut olmayan iş-kanıtı (ingilizcesi PoW - Proof of Work) yanlısı ve başını madencilerin çektiği bir grubun çıkarmayı planladığı ETHPoW çatallanması değil. Şahsen, ETHPoW çatallamasının 'olmayacak duaya amin' demenin ötesinde bir etki yaratamayacağı için üzerinde durulmaya değer olduğunu düşünmüyorum. 

### Kısa bir hatırlatma: 

Geçmiş yazıyı çok kısa hatırlatmak gerekirse: Amerika Birleşik Devletleri'nde kara para önleme kurumlarından OFAC'ın Tornado Cash uygulamasını ve onunla ilişkilendirilen adresleri yasaklaması sonrası pek çok merkezi kurum (USDC, Aave, dYdX gibi) bu adreslere erişimi kesmişler idi. 

Web sitesi üzerinden erişimi kesmek aslına bakarsanız uygulamaları kullanmayı etkilemiyor. Zira, az bir teknik bilen herhangi biri akıllı kontrata Ethereum zinciri seviyesinde ulaşarak uygulamaları kullanmaya devam edebilir. Asıl sorun, Ethereum'a zincir seviyesinde ulaşımın engellenmesi ihtimali. 

Bu ihtimal, Ethereum'un hisse-kanıtı sistemine (muhtemelen 15 Eylül'de) geçmesi sonrası daha kuvvetlenebilir. Zira, Ethereum üzerinde rehin edilen ETH'lerin hatırı sayılır bir kısmı merkezi kurumlar üzerinden kilitlenmiş. Yarın öbür gün OFAC bu kurumlara "şu adreslerden gelen işlemleri blokzincire dahil etmeyin" diye bir 'ricada' bulunursa ne olacak? 

### İkiye bölünme ihtimali

İşte bu nedenle kamuoyunun ikiye bölünmesi ihtimal dahilinde. Bu yazıda bunun teknik anlamda nasıl yapılacağına değil gerçekleşmesi halinde uygulamalar ve kullanıcılar açısından getireceği komplikasyonlara değineceğiz. Bir ayrılma olması durumunda bu, ağırlığa sahip grubun kalması diğer grubun ise bir çatallanma ile ayrı bir zincire geçmesi şeklinde olacak.

| ![fork](/assets/threshold-6036413_800.jpg)|
|:--:| 
| *Image by [Paul Henri Degrande](https://pixabay.com/users/paul_henri-6735189/) from [Pixabay](https://pixabay.com/)*|

Böyle bir durumda özellikle sansüre karşı olan ekibin, karşı grubun rehin verdiği varlıkları dondurmaktan, bu varlıkların bir kısmını ya da tamamını yakmaya yani bir başka deyişle nükleer silah kullanmaya kadar verebileceği farklı tepkiler olabilir. (Bu son görüşü savunanlar, ABD’nin II. Dünya Savaşı’nda Japonya’ya atom bombası atmasından sonra bir daha 80 yıl boyunca nükleer silah kullanılmamasının, bu yöntemin ne kadar etkili olduğunu gösterdiğini belirtiyorlar.)

### Ayrılma, uygulamalar ve kullanıcılar açısından neler getirebilir?

Buradaki belirsiz olan nokta, topluluğun diğer önemli paydaşı olan geliştiricilerin alacağı pozisyon. Zira bir çatallanma olursa her tür akıllı kontrat yani uygulama her iki platformun içinde de olacak. 

Böyle bir durumda yazılımcılar kaynak ve eforlarını hangi zincire harcayacaklar? İlk gelen tepkiler yazılımcıların sansürsüz tarafı seçecekleri yönünde olsa da, geliştiricilerden kimlikleri belli olanlar regülasyonlara karşı çıkan zincirde yer alıp kariyerlerini ve hayatlarını riske edecekler mi? Bir diğer öngörü ise piyasaya pek çok ‘yeni ve anonim’ geliştiricinin gelmesini beklemek olacak. 

İkinci belirleyici nokta ise stabil para çıkaran kurumlar tarafında yaşanacak. Merkeziyetsiz dünyadaki stabil paraların [yaklaşık %90'ı](https://www.theblock.co/data/decentralized-finance/stablecoins) merkezi stabil paralar olan USDT, USDC ve BUSD üzerinde. Stabil para üreticileri her iki platformu da destekleyemez, zira ellerinde sadece bir paraya yetecek karşılık var. Bu kurumların merkezi olması nedeniyle sansürü kabul eden topluluğa yakın olma ihtimali daha yüksek. Ya da bir şekilde kullanıcılara iki taraftan birini seçmelerini sağlayacak bir çözüm yolu önerecekler. 

Kullanıcılar açısından da ilginç bir durum söz konusu. Eğer iki ayrı zincir olursa kullanıcıların varlıkları iki farklı zincirde çoklanacak. Burada iki varlıktan rağbet gören hangisi ise değer o tarafta yükselecek. Diğer zincirdeki varlıkların bir değeri kalabilir ya da sıfıra inebilir. Kullanıcılar hangisini seçecek? Nereden bakarsanız bakın karmaşık bir durum. 

Bu arada hemen belirtelim bu durum sadece Ethereum’u değil diğer tüm zincirleri de benzer şekilde etkileyebilir. Hatta iş kanıtı yöntemini kullanan Bitcoin’in madencilerinin %35’inin ABD’de olduğunu, üstelik bu madencilerin kurulu tesisleri olması nedeniyle bu gücü başka yere taşımanın çok daha güç olduğunu, dolayısıyla bu madencilerin de benzer bir risk altında olduğunu belirtelim. 

### Ama durun! Bütün bunlar bir olasılık aslında!
Buraya kadar yazdıklarımıza bakarak geleceğin oldukça karanlık olduğunu düşünebilirsiniz. Öyle ya, iki farklı zincir, ortalık toz duman, kim nerede ve ne tarafta belli değil. Karmakarışık bir dünya. 

Haklısınız ancak hemen iç karartmaya gerek yok. Öncelikle hükümetlerden gelen platform seviyesinde bir baskı henüz yok. Açıkçası OFAC’ın Tornado Cash hareketinin kamuoyuna “bakın aksiyon aldık” demekten öte bir etkisi olmadı. Kendilerinin bu dünyayı tam anladıklarını düşünmek fazla iyimser bir bakış açısı olur. OFAC tarafından yeni bir yaptırım gelene kadar kripto dünyası da haliyle karşı aksiyona geçecek (lobi faaliyeti, seçimlerde kripto dostu adayları destekleme gibi). 

Sansürü kabul edecek kurumsal yapılar olsa da, bu oyuncular enayi değiller. Elbette böyle bir durumun varlıkların değerine negatif etki yapacağının farkındalar. Dolayısıyla, hiç böyle bir bölünmeye girmeden fonlarında tuttukları kriptoparaları elden çıkarmayı düşünebilirler. Bu da en fazla ETH’nin fiyatında ciddi bir düşüş yaratır ama zincirin uzun vadeli sağlığına zarar vermez. 

Kaldı ki, dünya ABD’den ibaret değil. Bakalım onun koyduğu yaptırım listesini uygulayacak bir zinciri diğer ülkeler kabul edecekler mi?

Burada en önemli konu sosyal konsensusun nerede oluşacağı. Şu an görünen topluluğun Ethereum’un nötr bir altyapı olarak kalması yönünde bir eğilimi olduğu. Ayrıca sisteme gönderilen işlemlerin kimden geldiğinin gizlenmesi yoluyla onaylayıcıların sansür uygulamalarını imkansız kılacak geliştirmeler de söz konusu*. 

Dolayısıyla şahsi görüşüm, sosyal konsensus sayesinde ikiye ayrılmaya gidilmeden soruna bir çözüm bulunacağı yönünde. 

### Sonuç 
OFAC tarafından getirilen yasaklamalar Ethereum dünyasında büyük tartışmalar başlattı. Böyle tartışmaların şimdiden yapılması önemli, zira kafayı devekuşu gibi kuma gömmenin bir faydası yok (küresel iklim konusunda olduğu gibi). Soruna çare bulunana kadar zorlu bir yoldan geçilmesi bu sırada ETH’nin değerinde ciddi dalgalanmalar olması muhtemel. Yine de bir çözüm bulunduktan sonra Ethereum ve kripto dünyasının bu olaydan çok daha güçlenerek çıkacağını görmemiz çok olası. İzleyip göreceğiz. 

---

*Not 1: Burada özellikle madenciler konusunda yer alan ve işlemleri önerenler ile onaylayanların ayrılmasına yönelik halihazırda tartışılan [bir öneri](https://ethresear.ch/t/proposer-block-builder-separation-friendly-fee-market-designs/9725) de bulunmakta*

*Not 2: Bu yazı ilk olarak 8 Eylül 2022'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/ethereum-catallanmasi-kullanicilari-nasil-etkileyebilir/)*

*Not 3: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*
