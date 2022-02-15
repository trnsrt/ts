Bu yazımızda, 2022 yılında çok konuşacağımız köprüler konusuna değiniyoruz. İlk yazımızda cevaplamaya çalışacağımız soru: Blokzincirlerde neden köprülere ihtiyaç duyuyoruz?

### Blokzincirler birer ada mı?

Sıkça kullandığım bir benzetme var: Yaşadığımız 'fiziki' dünyayı bir kıtaya benzetirsek, blokzincirler ana kara çevresine sıralanmış küçük adalar gibiler. Bizim bu adalara gidebilmemizi, yani itibari (fiat) paradan kriptoparaya geçişimizi genelde kripto alım-satım platformları sağlıyorlar. Peki bu adalar arasında gidip gelmek istersek? Bir blokzincirden öbürüne geçmek istersek? O zaman birkaç yol var ama önümüzdeki dönemde en sık konuşacağımız yol köprüler olacak gibi görünüyor. 

### Blokzincir ve köprü ilişkisi

Blokzincir dediğimiz esasında bir yazılım ve temel işlevi üzerine kurulu olan projelere altyapı olmak. Bunu yaparken, genelde blokzincirler kapalı bir dünya olarak kuruluyorlar. Ne yaparsanız, bu 'ada' içinde yapıyorsunuz.  Peki nasıl bir blokzincirden diğerine geçiş yapacağız? 

| ![L1_ecosistemi](/assets/Layer-1-Ecosystem-Map_1600_v3.jpg)|
|:--:| 
| *Blokzincir Dünyası Kaynak: [Blockchain Comparison](https://blockchain-comparison.com/blockchain-protocols/)*|

Bunun iki temel yolu var. Birincisi, bir kriptopara borsası kullanabilirsiniz. Bunun oldukça zahmetli bir yöntem olduğunu belirtelim. Bir örnek ile açıklayalım: Elinizde Ethereum ağında tuttuğunuz bir ETH var ve bunu Avalanche ağına geçirmek istiyorsunuz. ETH'nizi bir borsada bulunan hesabınıza aktaracaksınız. Sonra o ETH'yi satacaksınız (muhtemelen en likit olan bir stabil para örneğin USDT ile). Arkasından aldığınız stabil para ile AVAX satın alacaksınız. En sonunda ise satın aldığınız bu AVAX'ı borsadaki hesabınızdan Avalanche üzerindeki cüzdanınıza çekeceksiniz. Tam dört adım. Boşa zaman üstüne üstlük para kaybı; Ethereum ve Avalanche üzerinde transfer için ödeyeceğiniz işlem ücretinin üzerine bir de kriptopara alım-satımı sırasında uğrayabileceğiniz kayıplar. 

İkinci yol ise bu iş için bir köprü kullanmak. Köprüler sayesinde bir blokzincir üzerindeki kriptoparanızı cüzdanınızdan direkt olarak diğer blokzincir üzerindeki hesabınıza aktarabilmek. Hangisi kulağa daha kolay geliyor? Teoride ikincisi tabii ama pratiğe gelince henüz orada değiliz. 

### Neden ihtiyaç duyuyoruz köprülere?
"Daha yeni blokzincirlere alışmaya başlamıştık, bu köprüler nereden çıktı? Ne gerek var şimdi buna?" diye sorabilirsiniz. Gelin kısaca bir bakalım: 

#### Ethereum'un yüksek işlem ücretleri
Öncelikle sorunun temeli 2020 yılı ortalarından beri hayatımıza giren DeFi yani merkeziyetsiz finans ürünleri ve geçtiğimiz yıl piyasayı sarsan NFT'lere dayanıyor. Gerek DeFi gerekse NFT'lerin ağırlıklı olarak ortaya çıktığı ağ Ethereum oldu. Neden? Çok basit. Para yani değer Ethereum blokzincirinde toplanmıştı ve girişimler için ilk adres hep Ethereum oldu. 

Ancak Ethereum DeFi ve NFT'ler tarafından gelen yoğun talebi karşılayamadı. İşlemler hiçbir zaman durmadı ancak oldukça pahalandı. Makul fiyatlar ile işlem yapmak isteyenlerin saatlerce beklemek zorunda kaldığını gördük. Bu duruma hâlâ net bir çözüm bulunabilmiş değil. Kendimden bir örnek vereyim, son birkaç aydır yüksek işlem ücretleri nedeniyle Ethereum üzerinde neredeyse hiç işlem yapmadım.

Bunu fırsat bilen Ethereum rakibi blokzincirler hızlı ve ucuz işlem önerisi ile ciddi bir yatırımcı kitlesini kendilerine çektiler. 2021 yılı başlarında 'tüm DeFi Ethereum üzerinde döner' diye konuşurken son zamanlarda bunun böyle olmadığını görmeye başladık: 

#### Alternatif zincirler tarafından verilen teşvikler
Tabii kitleleri diğer blokzincirlere yönlendiren sadece düşük işlem ücretleri değil. Herhangi bir blokzincirde özellikle finans alanında bir işlem yapmak isteyen yatırımcının baktığı iki temel kriter var: Birincisi getiri, ikincisi ise likidite. Ethereum üzerine kurulan DeFi protokollerinin likidite yaratabilmek için 2020 yılı yaz aylarında nasıl teşvikler verdiğinden daha önce birkaç kez bahsetmiştik. İşte alternatif blokzincirleri de benzer yöntemi kullanarak, Ethereum üzerindeki yoğunluk nedeniyle gidecek başka yer arayan likiditeyi çekebilmek için kendi tokenlerini verdikleri teşvik programları açıkladılar. 

| ![TVL_on_L1s](/assets/TVL_on_L1s_800.jpg)|
|:--:| 
| *Ekosistem üzerinde kilitli değerin blokzincirler arasındaki dağılımı. Kaynak: [Coingecko Kriptopara Raporu 2021](https://www.coingecko.com/buzz/2021-yearly-cryptocurrency-report) Sayfa 32*|

#### Ethereum üzerine kurulu ikinci seviye çözümler
Ethereum geliştiricilerinin, kullanıcılara ait varlıkların kendi ağlarında kalması için gösterdikleri yoğun bir çaba var, ancak bu çalışmaların meyve vermesi oldukça zaman alacak gibi görünüyor. Bunlardan birincisi Ethereum'un yeni versiyonu - başlangıçta Ethereum 2.0 olarak adlandırılan ama yakın zamanda 'Execution Layer' olarak isim değiştiren ve bir blokzincir yerine 64 blokzincirden oluşacak olan yeni yapı. Bu yapı Ethereum'un kapasitesini ciddi bir şekilde artırmaya yarayacak ancak tam anlamıyla işlerlik kazanması 2022 yılına yetişecek mi, oldukça zor görünüyor. O zamana kadar Ethereum geliştiricilerinin önerdiği diğer çözüm ise ikinci seviye dediğimiz çözümler. Bu çözümleri kullanabilmek için kullanıcıların aynı alternatif zincirlerde olduğu gibi köprüleri kullanmaları gerekiyor. 

### Arkası yarın
Bir sonraki yazımızda, 'köprü tam olarak ne demek, farklı köprü çeşitleri neler ve geçtiğimiz günlerde duyduğumuz köprü kazalarında ne yaşandı' sorularına yanıt arayacağız.
