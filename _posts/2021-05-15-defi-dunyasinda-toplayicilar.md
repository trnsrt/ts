---
layout: post
title:  "DeFi dünyasının toplayıcıları"
date:   2021-05-15 17:47:56 +0300
categories: Genel
tags: Yazılar, DeFi, DeFi'ye Giriş
image: /assets/time-4559218_800.jpg
---


Bu yazımızda klasik dünyada alışık olmadığımız, daha çok DeFi dünyasının kullanıcılara sunduğu bir yenlik olan toplayıcılardan bahsedeceğiz. 

Bir önceki yazımızda DeFi'de yatırım yapmanın ilk adımlarından bahsederken kullanılabilecek iki yol olarak merkezi ve merkeziyetsiz borsalardan bahsetmiştik. 👇


İlk başta çok sık kullanılan bu iki yöntem sonrası farklı ve yeni pek çok ürün çıktı. Az sonra bu ürünlere bir göz atacağız. Ama önce, gelin DeFi'nin felsefesini tekrar hatırlayalım: 

### DeFi'nin girift yapısı
DeFi felsefesinin temel yapı taşlarından biri 'açık olmak'. Bu açık olmanın bir özelliği de, ürünlerin belli bir standart ile yaratılması ve birbirleri ile geçişkenli olarak kullanılabilmesi. Ne demek bu? 

Klasik dünyadan bir örnek üzerinden açıklayacak olursak; bankada tuttuğunuz mevduatı, bankaya sormadan teminat olarak gösterip başka bir kurumdan kredi almak, sonra da o kredi ile farklı bir aracı kuruma ait bir fona yatırım yapmak şeklinde düşünebilirsiniz 'açık olmak' özelliğini. "Olmaz öyle şey" diyebilirsiniz - haklısınız, klasik dünyada bu çok zor.. 

Ama DeFi için durum farklı. Neredeyse her ürün bir başkası ile birlikte kullanılabiliyor. Bu da kullanıcıya daha önce hiç tanışmadığı farklı yenilikler ve kolaylıklar sağlayabiliyor. 

Ancak bu yenilikler aynı zamanda kendi içinde belli komplikasyonları da beraberinde getiriyor. Gelin önce bu sıkıntılardan birinden, sonra da DeFi'nin buna karşı geliştirdiği çözümden bahsedelim.  

#### Merkeziyetsiz borsaların avantajı ve dezavantajı

Geçtiğimiz yazılarımızdan birinde, merkeziyetsiz borsalardan bahsetmiştik. Merkeziyetsiz borsalar tokenlarını elektronik cüzdanında tutan DeFi kullanıcıları için en rahat alım-satım platformları. 

DeFi kullanıcıları genelde merkezi borsalara gitmiyorlar. Neden? çünkü merkezi borsalara kayıt olmak ile uğraşmak var. Sonra başka bir merkezi borsaya geçmek istersen, ona da kayıt yaptırıyorsun. Sanki klasik dünyadaki bankaları andırıyor değil mi?

Kullanıcı bunun yerine merkeziyetsiz borsaları tercih edebiliyor. Zira, böyle bir borsayı kullanmak için yapması gerek tek hareket, ilgili siteye gitmek ve kendi elektronik cüzdanını bağlamak. O kadar. 

Bu olayın güzel tarafı. Ancak bunun da bir takım sorunları var. Ne mesela? 

En önemli konu, tabii ki işlem fiyatı. Her bir borsada arz ve talebin farklı olması nedeniyle fiyatlar farklılık gösterebiliyor. 

Öte yandan, borsada bulunan likidite de önemli. Zira likit olmayan bir token alımında, fiyatın ufak bir alım ya da satım hareketinde ciddi bir hareket göstermesi mümkün. 

Bir başka konu ise, kullanıcının alım yapmak istediği sırada başka alıcıların da işlem yapması sonucu fiyatın bir anda değişebilmesi. Burada kullanıcı ne kadarlık bir fiyat değişimine (ki buna slippage deniyor ingilizcede) izin vereceğini (genelde %1, %2 gibi seçilebiliyor) seçebiliyor. 

Son olarak, kullanıcının işlem yaparken ne kadar hızlı işlemi gerçekleştirmek istediği de önemli. Eğer çok hızlı bir şekilde işleminin gerçekleştirmek istiyorsa, o zaman blokzincir sırasında öne geçebilir ancak bunun ciddi bir maliyeti var. Ya da alternatif olarak 'benim işim acele ya da kritik değil' diye düşünerek daha düşük bir madenci işlem ücreti seçebilir.. Ama böyle bir durumda, hem gecikmeye razı olmalı hem de o işlem blokzincire yazılana kadar araya giren başkaları olabileceği için fiyatın değişme riskini göze almalı. 

#### Kullanıcı hangi borsayı kullanacağını nasıl seçecek? Toplayıcılar burada işin içine giriyor

İşte yukarıda saydığımız faklı senaryolardan dolayı tokenların fiyatı borsadan borsaya farklılık gösteriyor. Ne yapacak kullanıcı? Sekiz farklı borsa için ekranını açık tutup hangisi iyi ise ondan mı işlem yapacak?

| ![time_money](/assets/time-4559218_800.jpg) | 
|:--:| 
| *Image by [mohamed Hassan](https://pixabay.com/users/mohamed_hassan-5229782/) from [Pixabay](https://pixabay.com/)*|

İşte DeFi burada kullanıcının imdadına yetişiyor. Toplayıcı (ingilizcesi aggregator) dediğimiz merkeziyetsiz hizmet sağlayıcılar, kullanıcının işlem yapmak istediğinde, hemen bütün merkeziyetsiz borsalar ile iletişim kuruyor, token için en iyi fiyat vereni buluyor ve kullanıcının önüne getiriyor. 

Bunun yanında toplayıcıların şöyle bir avantajı da bulunuyor: Kullanıcı normalde elinde bulunan bir tokeni bir merkeziyetsiz borsada satmak isterse öncelikle o tokunda işlem yapabilme hakkını o borsaya vermesi gerekiyor. Nasıl oluyor bu? Çok basit: İşlem yapmaya karar verdiğinde kullandığı elektronik cüzdan ondan iki konuda izin istiyor. Birincisi o borsanın parasını kullanması konusunda ikincisi de o fiyattan satabilmesi konusunda. Bu da blokzincire işlenecek iki farklı işlem demek. Ethereum blokzincirinin yoğunluğunu düşünürseniz, birinci işlem (parayı kullanmaya izin verme) nereden baksanız 5-10 ABD Doları tutuyor.. 

Düşünün, bir kullanıcı borsalara teker teker bakacak, uygun fiyatlısını bulacak, sonra borsa parasını kullanabilsin diye izin verecek (komisyon ödeyecek) en sonunda da işlemin fiyatına onay verecek..  Hem zaman hem de para kaybı.. 

Bunun yerine toplayıcıya parasını kullanma konusunda izin verdiğinde sonrasında toplayıcı bunu hangi borsada kullanırsa kullansın tekrar bir izin vermesine gerek yok.. Bu da kullanıcı için ekstra işlem maliyetinden kaçınması demek. 

### Kimler var bu piyasada?
2020 yılının Nisan ayı itibariyle piyasada üç büyük toplayıcı bulunuyor. Bunlar [1inch](https://1inch.exchange/#/), [Matcha](https://matcha.xyz/), ve [ParaSwap](https://paraswap.io/). 

| ![dexes](/assets/Dex_islem_hacimleri_800.jpg) | 
|:--:| 
| *Merkeziyetsiz işlem toplayıcı hacimleri Kaynak: [TheBlock](https://www.theblockcrypto.com/data/decentralized-finance/dex-non-custodial/dex-aggregator-trade-volume)* | 

2020 yılının Mayıs ayında başlayan DeFi piyasasındaki canlamanın biraz gecikmeli olarak toplayıcılara geldiğini söylemek yanlış olmaz. Bunun birkaç nedeni var. Öncelikle piyasalarda böyle bir ihtiyaç olduğu geç anlaşıldı. Öte yandan bu piyasanın lideri olan 1inch, 2020 Aralık ve 2021 Şubat aylarında yaptığı iki airdrop ile geniş kitlelerin kendisini kullanmasını sağladı (airdrop kullanıcılara platformu kullanmaları için verilen teşvikler).. 

1inch bunun yanında 2020 Mart ayı içinde Ethereum blokzinciri yanında daha önce de bahsettiğimiz rakip [Binance Smart Chain](https://www.binance.org/en/smartChain) için de toplayıcılık hizmeti vermeye başladı.. Bu da kullanım alanını genişletmek konusunda 1inch'e ekstra avantaj veriyor. 

1inch arayüz olarak kimi kullanıcılara farklı ve anlaşılmaz gelebilir. 1inch rakiplerinden Matcha ise temiz arayüzü ile bu anlamda farklılaşıyor. 

Öte yandan hem 1Inch hem de Matcha, piyasa emirleri dışında limitli emir verebilme imkanı da sunuyorlar. Limitli emir ile emir yapmak istediğiniz fiyatı belirliyor ve fiyat oraya geldiğinde işlem izni veriyorsunuz. Normalde merkeziyetsiz borsalar, örneğin Uniswap havuz sistemleri dolayısıyla limitli işlemlere değil. Kullanıcıların limit işlem kullanırken ödedikleri ücretlere ve işlemlerin gerçekleşmeme ya da çok geç gerçekleşme ihtimali olduğunu unutmamaları gerekiyor. 

1inch ile ilgili geçtiğimiz aylarda ortaya çıkan bir konuya da yer vermekte fayda var. Yukarıda 'slippage' olarak bahsettiğimiz kullanıcının işlem emri vermesiyle işlemin gerçekleşmesi sırasında araya girenlerden dolayı fiyatın negatif etkilenmesinden bahsetmiştik. Kimi zaman bunun tersi de olabiliyor. Kullanıcı bir tokeni almak için teklif yaptığında, başka birileri aynı tokeni satmak için işlem yaptıkları için token fiyatı ucuzlayabiliyor. 1inch böyle bir durumda 'positive slippage' denen bu farkı kullanıcıya vermeyip cebine atıyor. Etik mi? Kullanıcı istediği fiyattan aldığı için bir sorun yok gibi görünüyor ama yine de ağızda hoş bir tat bırakmadığı kesin. 

### Cüzdanlar da artık bu işi yapıyorlar
Daha önceki yazılarımızda bahsettiğimiz elektronik cüzdanlar da artık cüzdan içinden farklı borsalarda işlem yapabilme imkanı veriyorlar. Burada DeFi alanının en büyüğü olan Metamask ön plana çıkıyor. Cüzdan içinden doğrudan alım satım yapabilmek büyük rahatlık ancak kulanıcıların ödedikleri komisyonları takip etmelerinde fayda var. 

### Sonuç 
Teklif toplayıcılar DeFi sisteminde kullanıcılara kolaylık sağlayan hizmetlerden bir tanesi.. İleride daha da büyüyecekleri neredeyse kesin gibi.. Bakalım bu yarışın kazananı kim olacak... 

*Not 1: Bu yazı ilk olarak 15 Mayıs 2021'de [BlockchainIST Center](https://medium.com/blockchainist-center)'da [yayınlandı](https://medium.com/blockchainist-center/definin-toplay%C4%B1c%C4%B1lar%C4%B1-964b4b4e7fc7)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.* 
