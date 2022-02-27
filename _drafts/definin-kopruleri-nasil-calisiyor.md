---
layout: post
title:  "DeFi'de Köprülere Neden İhtiyaç Var?"
date:   2022-03-01 17:47:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Bu yazımızda, blokzincirler arası köprüler ne demek, farklı köprü çeşitleri neler sorularına cevap vermeye çalışacağız. 

Geçtiğimiz yazımızda, blokzincirler üzerine köprülere neden ihtiyaç duyulduğunu anlamaya çalışmıştık. Özet olarak, kullanıcılar dijital varlıklarını farklı blokzincirler arasında taşımak isteyebiliyorlar. Bunun temel nedenleri arasında, ağırlıklı olarak Ethereum ağında tutulan varlıkların yüksek işlem ücreti nedeniyle istenildiği şekilde değerlendirilememesi ya da diğer ağlarda önerilen yüksek kazançlar var.  Bunun sonucu kullanıcılar ya Ethereum güvenliğini kullanan ikinci seviye çözümlere ya da onlara daha yüksek getiri ve ucuz işlem ücretleri vadeden alternatif ağlara köprüler aracılığıyla geçiyorlar.

### İyi de tam olarak ne yapar köprüler?
En basit haliyle ile bir köprünün temel işlevi, kullanıcının sahip olduğu dijital varlığı, bulunduğu ağ üzerinde kilitlemek ve bunun karşılığında kullanıcıya aynı miktarda değeri başka bir ağda sunmak. 

Şimdiye kadar hep değer transferi üzerinden örneklendirdiğimiz bu özellik aslına bakarsanız özünde, bilginin (verinin) bir ağda teyit edilip diğeri ağa gönderilmesi demek. Bu nedenle sadece dijital varlık (değer) değil, herhangi bir bilginin transferi için de kullanılabiliyor köprüler (eski bir yazımızda bahsettiğimiz blokzincire ağ dışında bilgi taşımaya yarayan oracle dediğimiz taşıyıcılar da aslına bakarsanız bir çeşit köprü sayılabilir). 

| ![river_bridge](/assets/river-6175173_800.jpg)|
|:--:| 
| *Image by [Tobias Brunner](https://pixabay.com/users/tobiasbrunner-13708887) from [Pixabay](https://pixabay.com/)*|

Kullanıcıya diğer ağda verilen değerin ne olduğu köprülerin temel dizayn farklılıklarına göre değişebiliyor. Örneğin elinizde Ethereum ağında bulunan ETH'niz var ise, bunu Avalanche ağına geçirdiğinizde köprü size WTHe adında değeri ETH'ye eşit başka bir token veriyor. Kimi ağlarda ise aynı merkeziyetsiz borsalarda olduğu gibi, bir ağın temel tokenini diğer ağın tokeni ile takas edebiliyorsunuz. Örneğin, Ethereum'da verdiğiniz ETH yerine Solana'ya geçip o ağın tokeni SOL'u alabiliyorsunuz. 

### Ne tip köprüler var?
Yukarıda da yazdığımız gibi, farklı köprülerin teknik olarak farklılıkları var. Bu yazımızda bu teknik farklılıklara girmek yerine kullancı perspektifinden üç temel köprü kategorisine değineceğiz. 

#### Farklı blokzincirler arası köprüler
Bir önceki ve bu yazımızdaki örneklerde ağırlıklı olarak bahsettiğimiz blokzincir-arası köprü çözümleri bu aralar en popüler olan kategori. Farklı iki zincir arasında değer ya da bilgi transferine yarayan bu köprü çözümlerinin birkaç çeşidi var.

Bu köprülerin ilk çıkanlarından bir tanesi, ***Bitcoin blokzincirinden Ethereum'a değer geçişini sağlayan WBTC, renBTC gibi köprüler***. Bu köprülerin özelliği sadece tek bir dijital varlığa (burada BTC'ye) odaklanmış olmaları. Ethereum üzerindeki DeFi uygulamalarının getirilerinden faydalanmak isteyen ama BTC'sinden de uzak kalamayan bir kitlenin bir zamanlar çok kullandığı bu köprüler üzerinden yaklaşık [14 milyar ABD Doları](https://btconethereum.com/) gibi bir tutar Ethereum'a aktarılmış durumda. Yeterli likiditeye sahip bu havuzlar sadece tek bir varlık üzerinden değer transferi yapmak isteyenler için ideal. 

Popüler köprülerden bir diğeri, ***iki blokzincir arasında değer transferi için blokzincirin kendisi tarafından kurulan köprüler.*** Genelde bu tip çözümler Ethereum ile alternatif ağ üzerinde oluşturuluyor. Ethereum Avalanche arasında kurulan [Avalanche Bridge](https://bridge.avax.network/) bu örneklerinden bir tanesi. 

Bir diğer köprü çeşidi ise, ***herhangi bir uygulama tarafından o uygulamaya özel çıkarılan köprüler.*** Bu köprüler, kullancılara kendi uygulamaları üzerinden birden fazla blokzincir üzerinde değer transferi sağlayabiliyor. Bunun en bilinen örneği ise DeFi üzerindeki en büyük kredi verme protokolü olan Compound tarafından geliştirilen [Gateway](https://compound.cash/). Bunun bir benzerini Aave  yakın zamanda çıkaracağı [3. versiyonunun içinde bulunan Portals](https://docs.aave.com/developers/getting-started/v3-overview) özelliği ile kullanıcılara sunuyor.  Bu tip köprüler, belli bir maksat ile (burada kredi ve teminat için) özellikle varlıkları daha verimli kullanmak amacıyla faydalı olsa da, kullanıcılara sadece o uygulamada kullanım sağladıkları için alanları oldukça kısıtlı. 

Son olarak, ***birden fazla blokzincir arasında birden fazla tokenin transfer edilebilmesini sağlayan, genel kullanım maksatlı köprüler*** de bulunmakta. Bu tip köprülerin kullanımlarının gün geçtikçe arttığını görüyoruz. Tek bir adres üzerinden farklı zincirlere ulaşım büyük kolaylık olsa da, bu tip köprülerin kullanıcı açısından en büyük sıkıntısı yeterli likiditeye sahip olmamaları. Genel olarak en büyük likidite stabil paralarda oluyor ve kullanıcılar USDT, USDC gibi paraları bir ağdan diğerine geçirmek için bu köprüleri kullanıyorlar. 

#### Aynı blokzincir içinde ikinci seviye çözümlere geçiş için köprüler
Yukarıda bahsettiğimiz farklı blokzincirlere geçişin yanında özellikle Ethereum üzerine kurulu [Arbitrum](https://bridge.arbitrum.io/), Optimistic Roll-up gibi ikinci seviye çözümlerin de köprüleri bulunmakta. Bu köprülerin bir önceki bölümde bahsettiğimiz köprülerden işlev olarak fazla bir farkı yok. 

Farklı oldukları konu, kullanıcının varlıklarını korudukları yer olarak beliriyor. Farklı blokzincirlerde değer transferi yaptığınızda, sahip olduğunuz değerin korumasını değiştirmiş oluyorsunuz. Ethereum'dan Solana'ya bir değer geçirdiğinizde değerinizi artık Ethereum blokzinciri koruması altında değil, onun yerine paranızı eti ve kemiğiyle birlikte Solana'ya emanet ediyorsunuz. 

İkinci seviye çözümlere gönderdiğiniz paranız ise yine Ethereum blokzinciri koruması altında. Yarın öbür gün ikinci seviyede bir sorun olduğunda, paranızı hâlâ kullanabiliyorsunuz. Oysa Solana geçtiğimiz aylarda 14 saat kapalı kaldığında, varlığınıza ulaşma imkanınız yok. Bu arada bu durumun L2 seviye Optimistic ve zkRollup çözümleri için geçerli olduğunu belirtelim. Polygon gibi kendi koruma kalkanına sahip yan-zincirler bir önceki paragrafta bahsettiğimiz farklı blokzincirler kategorisine giriyorlar. 

####  0-seviye (Layer 0) köprü çözümleri
Yukarıda bahsettiğimiz köprülerin yanında, blokzincirler arası değer transferini doğal bir şekilde yapmaya aday 0 seviye dediğimiz daha temel çözümler de mevcut. Üstelik birlikte çalışılabilirlik olarak adlandırılan bu çözümler için uzun süredir geliştirme yapılıyor (2019 yılında bu konuda yazılmış [şu](https://medium.com/turansert/bir-blockchain-di%C4%9Feri-ile-konu%C5%9Fur-mu-180866895f83) ve [şu](https://medium.com/turansert/blockchainler-i%C3%A7in-b%C3%BCy%C3%BCmenin-yolu-kar%C5%9F%C4%B1l%C4%B1kl%C4%B1-konu%C5%9Fup-payla%C5%9Fmak-d1fe44cdd45c) yazılara göz atabilirsiniz). Farklı blokzincirleri birbirine bağlayan [Polkadot](https://polkadot.network/) ve [Cosmos](https://cosmos.network/) bunların en ünlüleri. Keza, Ethereum'un yeni versiyonu da aslına bakarsanız benzer şekilde kendi ağına dahil 64 blokzinciri arasında değer transferini hızlı bir şekilde gerçekleştirecek. 

### Sıkıntıları neler?
Köprüler ile ilgili en büyük sıkıntı, sonuçta bu araçların da birer akıllı kontrat olmaları. Bu nedenle akıllı kontratların yazım hatalarından dolayı oluşabilecek sıkıntılar burada da yaşanıyor. 

Bir diğer konu, köprülerin genelde merkeziyetsiz olmamaları nedeniyle değer transferi yapan aracıların kullanıcılara getirdiği riskler. Az sayıda aracının olması merkezilik ve bunun sonucunda kötü niyetli oyuncuların sistemi ele geçirmesi gibi bir risk barındırıyor. Hep söylüyoruz: Merkeziyetsizlik uzun ince bir yol. Bu alanda ortaya çıkan tüm girişimler gibi köprüler de merkezi olarak başladılar ve yavaş yavaş merkeziyetsizliğe doğru yol alıyorlar. 

Bunun yanında fonksiyon anlamında köprülerin henüz yolun başında olduğunu söyleyebiliriz. Kullanım kolaylığı, yapılan transferlerin gerçekleşme hızı, işlemlerin gerçekleşebilmesini sağlayacak gerekli likidite, farklı amaçlar için kullanılabilme gibi köprülerin gelişmeleri gereken pek çok alan var. Önümüzdeki dönemde bu alanlarda yeni yeni pek çok yeniliğin biz kullanıcılara sunulacağını söyleyebiliriz.  

---

*Not 1: Konu ile ilgili daha teknik bilgi sahibi olmak isteyenler şu [Medium makalesine](https://medium.com/1kxnetwork/blockchain-bridges-5db6afac44f8) göz atabilirler.*

*Not 2: Bu yazı ilk olarak 1 Mart 2022'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı]()*

*Not 3: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*
