Bu yazımızda gelin, son dönemde DeFi dünyasının yeni sevgilisi olan OlympusDAO'ya bakalım. 

Geçtiğimiz yazımızda, DeFi'nin, büyüme sancılarının ilki olan likidite sıkıntısını nasıl aştığından bahsetmiş ancak çözüm olarak bulunan likidite madenciliğinin  yarattığı başkaca problemlere değinmiştik. Sonrasında yeni nesil DeFi protokollerinin bu sorunu çözmek için geliştirdikleri yollara değinmiştik. Bu yazımızda, bu yeni protokollerinden OlympusDAO'nun ortaya attığı yenilik ve bunun sonucu yaşadığı (şimdilik) müthiş başarıyı inceleyeceğiz. 

Öncelikle geçen yazımızın kısa bir özetini yapalım: 

### Neydi DeFi'nin sorunları ve nasıl çözüm bulunmuştu bunlara?

#### Para, para, para...
DeFi protokolleri ilk olarak kullanıcılara hizmet vermeye başladıklarında ciddi bir problem ile karşılaştılar: Likidite. Ne kadar çok kullanıcı bir protokolü kullanırsa orada ağ etkisi nedeniyle likidite oluyor, likidite oldukça da yeni kullanıcı geliyordu ancak makineye çalıştıracak başlangıç likiditesini bulmak kolay olmuyordu. Neden? Başta kullanıcı henüz gelmemişken sistem kullanılmadığı için konan likidite herhangi bir gelir (burada işlem yapılması sonrası alınan komisyon) kazanmıyordu.

| ![brain_money](/assets/head-6848580_800.png)|
|:--:| 
| *Image by [mohamed Hassan](https://pixabay.com/users/mohamed_hassan-5229782/) from [Pixabay](https://pixabay.com/)*|

#### Likidite madenciliği ile geçici çözüm
DeFi ürünleri bu problemi, protokollere likidite sağlayanlara ekstra teşvikler vererek çözdüler. Normalde protokoller likidite sağlayanlara sağladıkları para karşılığı kazandıkları komisyonun bir kısmını veriyorlardı. Bir de üzerine daha çok likidite çekmek için kendi yönetim tokenlerini teşvik olarak verdiler. Kullanıcı az olduğu için komisyon geliri az olsa da, likidite sağlayıcılar bu aldıkları yönetim tokenlerini piyasada satarak iyi getiriler elde ettiler.  

#### Likidite madenciliğinin problemi
Buradaki sorun verilebilecek teşviklerin yani tokenlerin bir sınırının olması. Ödül olarak dağıtılan tokenler azalmaya başlayınca, likidite sahipleri ellerindeki parayı daha yüksek getiri sağlayan başka platformlara taşıdılar. Öyle ki on-chain analiz şirketi nansen'in yaptığı bir [araştırmaya](https://www.nansen.ai/research/all-hail-masterchef-analysing-yield-farming-activity) göre, MasterChef kodu kullanan 28 havuzda, likidite sağlayıcıların yaklaşık %50'si havuza girdikten sonra 15 gün içinde ayrılıyor, uzun vadede ise sadece %13'ü havuzlarda kalmaya devam ediyor.

|![TVL](/assets/Nansen_arastirma_800.png)|
|:--:| 
| *28 MasterChef bazlı yeni açılan havuzda 33.883 adres tarafından gerçekleştirilen 40,477 likidite sağlama işleminin süresi. %36.41'inde para konduktan sonraki 5 gün içinde çekilmiş.Kaynak [Nansen](https://www.nansen.ai/research/all-hail-masterchef-analysing-yield-farming-activity)*|

Yukarıdaki tablonun temel nedeni, başlangıçta kimse yokken verilen teşviklerden dolayı getiriler çok iyi iken sonradan bu teşviklerin etkisinin azalıyor olması. Örneğin A protokolü, sahip olduğu ATOKEN'a likidite sağlamak için kurduğu ATOKEN-ETH havuzuna para koyanlara yüksek oranda teşvik veriyor (teşvik ATOKEN olarak veriliyor). Bu yüksek oranda teşviği görenler havuza para sağlamak için hemen gidip ATOKEN satın alıyorlar, bu da ATOKEN'nin değerini artırıyor. ATOKEN değeri artınca havuza ilk likidite sağlayanların geliri daha da artmaya başlıyor.

Müthiş güzel bir sarmal. Ta ki, ödül verilen tokenlerin azalmaya başlayıp bu ödülü almaya çalışan havuzun gittikçe genişlemesi, bunun da getirileri düşürmeye başlamasına kadar. Yatırım dediğiniz aslında beklentidir. Bir noktada getirilerin düşeceğini öngören yatırımcılar havuzdan likidite çekmeye başlıyorlar. Likidite çekilip alınan tokenlar satılmaya başlayınca fiyat da azalıyor ve bu sefer negatif sarmala giriyorsunuz.

Bu sarmalı Messari'nin aşağıdaki [tablosu](https://messari.io/article/olympus-pro-protocol-owned-liquidity-as-a-service?referrer=grid-view) çok güzel açıklıyor: 

|![TVL](/assets/messari_pool_liquidity_800.png)|
|:--:| 
| *Verilen teşvikler kısa vadede likidite sağlasa da, uzun vadede projelere zarar verebiliyor. Kaynak: [Messari Crypto Theses for 2022](https://messari.io/crypto-theses-for-2022)*|

Sonuç olarak, geçici süreliğine token vererek dışarıdan likidite kiralamak, başlangıçta protokolleri ayağa kaldırmak için güzel bir yöntem olsa da uzun vadede ürünlere ciddi bir ayak bağı olmaya başladı.

#### Yeni protokoller bu sorunu nasıl çözüyor?

Yeni DeFi protokolleri (ki kimileri bunlara DeFi 2.0 diyor) bu sorunu kısa vadeli likidite madenciliğini daha uzun vadeli hale çekerek çözdüler. Bunu yaparken de genelde bireysel yatırımcılar üzerinden likidite madenciliği (yani kiralama yapmak yerine) başka DAO'lar ile anlaşarak onların hazinelerindeki likiditeyi uzun vadeli kullanma yoluna geçtiler. Bu yazımızın konusu olan Olympus DAO ise bunu farklı bir şekilde yapıyor. Gelin şimdi onların yaptıklarına göz atalım hep birlikte.

### OlympusDAO kendini nasıl fonluyor ?
OlympusDAO, likidite çekebilmek için uzun vadeli ve kısa vadeli iki çözümü var.

Bunlardan ilki staking dediğimiz token rehin etme yoluyla para kazanma yöntemi. Bu yöntemin aslına bakarsanız benzer platformlarda yapılanlardan çok da bir farkı yok. OlympusDAO'nun farkı, sisteme uzun vadeli stake yapanlara çok yüksek miktarda faiz sözü vermiş olması. Sisteme stake yapmak için projenin değer yaratacağına inanmak gerekiyor, aksi takdirde değeri azalan bir tokenden getiri alsanız ne işe yarar ki? Staking'in uzun vadeli bir yatırım aracı olduğunu söylemeye gerek yok sanırım.

İkinci yöntem ise OlympusDAO'ya özel. Burada, OlympusDAO diğer protokollerin yaptığı gibi likiditeyi kiralamak yerine likiditeyi satın alıyor. Ne demek bu? Kısaca açıklayalım:

OlympusDAO, bir nevi bono ihraç ediyor yani piyasadan borç satın alıyor. Bunun yöntemi ise şu: 
- OlympusDAO, ihraç etmek istediği bonoları ve fiyatı ilan ediyor. 
- Kişiler, ellerinde bulunan ETH, DAO ya da Sushiswap'da bulunan OHM/DAI benzeri havuzlara katılım paylarını OlympusDAO'nun hazinesine veriyorlar, karşılığında da OlympusDAO tokeni OHM'yi alıyorlar. 
- Yalnız burada özel bir durum var - aldıkları OHM'yi piyasa değerinden daha iskontolu biçimde alıyor ve beş gün gibi bir süre satamıyorlar. 
- İskonto oranını serbest piyasa belirliyor. Ne kadar ilgi varsa, iskonto o kadar düşük oluyor. 
- Unutulmaması gereken, bu mekanizmayı kullananlar OlympusDAO hazinesine yukarıdaki varlıkları (Yani ETH, DAI ya da havuz katılım tokenlerini) veriyor, karşılığında ise OHM alıyor. Yani esas olarak hazineye bu varlıkları OHM karşılığı satmış oluyorlar. 

İşte, OlympusDAO'nun kendi likiditesini satın alma şekli.

### Başarılı mı?
Başarının pek çok tanımı var. OlympusDAO şu aşamada kendi hedeflerine ulaşmış görünüyor. Örneğin, OHM tokenlerin işlem gördüğü en büyük havuz olan Suhsiswap'ta bulunan [OHM-DAI likidite havuzunun](https://analytics.sushi.com/tokens/0x64aa3364f17a4d01c6f1751fd97c2bd3d7e7f1d5) %99.99 [sahibi şu anda OlympusDAO hazinesi](https://app.olympusdao.finance/#/dashboard). OlympusDAO'nun elinde bu havuz tokenleri de içeren yaklaşık 700 milyon ABD Doları token mevcut. 

|![Olympus_DAO_Hazinesi](/assets/OlympusDAO_Hazinesi_800.png)|
|:--:| 
| *OlympusDAO hazinesinin sahip olduğu tokenler ve miktarları -  Kaynak: [Dune Analytics](https://dune.xyz/shadow/Olympus-(OHM))*|

Bunun yanında piyasada bulunan OHM'lerin %90'ı OHM'ye stake edilmiş durumda. Dolayısıyla, stabil bir fonlama sağlama konusunda OlympusDAO şimdilik başarılı olmuş gibi görünüyor. 

### Arkası yarın
Bu haftalık burada bırakalım. Önümüzdeki hafta OlympusDAO nedir, neler yapar, başarısı ve sıkıntılarının detaylarına bakalım. 
