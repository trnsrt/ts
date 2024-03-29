---
layout: post
title:  "DeFi'de Köprülere Neden İhtiyaç Var?"
date:   2022-02-16 17:47:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

İki yazıdan oluşacak mini serimizde, 2022 yılında çok konuşacağımız köprüler konusuna değiniyoruz. İlk yazımızda cevaplamaya çalışacağımız soru "Blokzincirlerde neden köprülere ihtiyaç duyuyoruz?" olacak. 

### Blokzincirler birer ada mı?

Sıkça kullandığım bir benzetme var: Yaşadığımız 'fiziki' dünyayı bir kıtaya benzetirsek, blokzincirler ana kara çevresine sıralanmış küçük adalar gibiler. Bizim bu adalara gidebilmemizi, yani itibari (fiat) paradan kriptoparaya geçişimizi genelde kripto alım-satım platformları sağlıyorlar. Peki bu adalar arasında gidip gelmek istersek? Bir blokzincirden öbürüne geçmek istersek? O zaman birkaç yol var ama önümüzdeki dönemde en sık konuşacağımız yol köprüler olacak gibi görünüyor. 


| ![island_bridge](/assets/road-2360545_800.jpg)|
|:--:| 
| *Image by [Lennart Demes](https://pixabay.com/users/struffelproductions-589546/) from [Pixabay](https://pixabay.com/)*|


### Blokzincir ve köprü ilişkisi

Blokzincir dediğimiz esasında bir yazılım ve temel işlevi üzerine kurulu olan projelere altyapı olmak.Blokzincir genelde kapalı bir dünya olarak kurulur, üzerindeki uygulamalar da esasında dış dünyaya erişimi olmayan akıllı kontratlardır. Ne yaparsanız, bu ‘ada’ içinde yapıyorsunuz. 

Peki, o zaman bir blokzincirden diğerine nasıl geçiş yapılabilir? Örneğin, bir kullanıcı Ethereum üzerindeki kriptoparasını Avalanche ağına nasıl geçirebilir? 

| ![L1_ecosistemi](/assets/Layer-1-Ecosystem-Map_1600_v3.jpg)|
|:--:| 
| *Blokzincir Dünyası. Kaynak: [Blockchain Comparison](https://blockchain-comparison.com/blockchain-protocols/)*|

Bunun iki temel yolu var. Birincisi, bir kriptopara borsası kullanabilir. Bunun oldukça zahmetli bir yöntem olduğunu belirtelim. Yukarıdaki örnekten devam edelim: Kullanıcının elinde Ethereum ağında tuttuğu bir ETH var ve bunu Avalanche ağına geçirmek istiyor. ETH'sini bir borsada bulunan hesabına aktaracak. Sonra o ETH'yi satacak (muhtemelen USDT ya da USDC gibi en likit stabil paralardan biri aracılığı ile). Arkasından aldığı stabil para ile AVAX satın alacak. En sonunda ise satın aldığı bu AVAX'ı borsadaki hesabından Avalanche üzerindeki cüzdanına çekecek. Tam dört adım. Boşa zaman üstüne üstlük para kaybı; Ethereum ve Avalanche üzerinde transfer için ödeyeceği işlem ücretinin üzerine bir de kriptopara alım-satımı sırasında kayıp yaşayacak.

İkinci yol ise bu iş için bir köprü kullanmak. Köprüler sayesinde kullanıcı, bir blokzincir üzerindeki kriptoparasını diğer blokzincir üzerindeki hesabına direkt olarak aktarabilir. Hangisi kulağa daha kolay geliyor? Teoride ikincisi tabii ama pratiğe gelince henüz orada değiliz. 

### Neden ihtiyaç duyuyoruz köprülere?
"Daha yeni blokzincirlere alışmaya başlamıştık, bu köprüler nereden çıktı? Ne gerek var şimdi buna?" diye sorabilirsiniz. Gelin kısaca bir bakalım: 

#### Ethereum'un yüksek işlem ücretleri
Öncelikle sorunun temeli, 2020 yılı ortalarından beri hayatımıza giren DeFi yani merkeziyetsiz finans ürünleri ile geçtiğimiz yıl piyasayı sarsan NFT'lere dayanıyor. Gerek DeFi gerekse NFT'lerin ağırlıklı olarak ortaya çıktığı ağ Ethereum oldu. Neden? Çok basit. Para yani değer Ethereum blokzincirinde toplanmıştı ve girişimler için ilk adres hep Ethereum oldu.

Ne yazık ki, özellikle geçtiğimiz yıl içinde Ethereum'un DeFi ve NFT'ler tarafından gelen yoğun talebi karşılayamadığını gördük. İşlemler hiçbir zaman durmadı ancak oldukça pahalandı. Makul fiyatlar ile işlem yapmak isteyenlerin saatlerce beklemek zorunda kaldığını gördük. Bu duruma hâlâ net bir çözüm bulunabilmiş değil. Kendimden bir örnek vereyim, son birkaç aydır yüksek işlem ücretleri nedeniyle Ethereum üzerinde neredeyse hiç işlem yapmadım.

Bunu fırsat bilen Ethereum rakibi blokzincirler hızlı ve ucuz işlem önerisi ile ciddi bir yatırımcı kitlesini kendilerine çektiler. 2021 yılı başlarında 'tüm DeFi Ethereum üzerinde döner' diye konuşurken son zamanlarda bunun böyle olmadığını görmeye başladık (bir paragraf aşağıdaki tablo bunu rakamlar ile gözler önüne seriyor).

#### Alternatif zincirler tarafından verilen teşvikler
Tabii kitleleri diğer blokzincirlere yönlendiren sadece düşük işlem ücretleri değil. Herhangi bir blokzincirde özellikle finans alanında bir işlem yapmak isteyen yatırımcının baktığı iki temel kriter var: Birincisi getiri, ikincisi ise likidite. Ethereum üzerine kurulan DeFi protokollerinin likidite yaratabilmek için 2020 yılı yaz aylarında nasıl teşvikler verdiğinden daha önce birkaç kez bahsetmiştik. İşte alternatif blokzincirleri de benzer yöntemi kullanarak, Ethereum üzerindeki yoğunluk nedeniyle gidecek başka yer arayan likiditeyi çekebilmek için kendi tokenlerini verdikleri teşvik programları açıkladılar. 

| ![TVL_on_L1s](/assets/TVL_on_L1s_800.jpg)|
|:--:| 
| *Ekosistem üzerinde kilitli değerin blokzincirler arasındaki dağılımı. Kaynak: [Coingecko Kriptopara Raporu 2021](https://www.coingecko.com/buzz/2021-yearly-cryptocurrency-report) Sayfa 32*|

#### Ethereum üzerine kurulu ikinci seviye çözümler
Ethereum geliştiricilerinin, kullanıcılara ait varlıkların kendi ağlarında kalması için gösterdikleri yoğun bir çaba var, ancak bu çalışmaların meyve vermesi oldukça zaman alacak gibi görünüyor. Bunlardan birincisi Ethereum'un yeni versiyonu - başlangıçta Ethereum 2.0 olarak adlandırılan ama yakın zamanda 'Execution Layer' olarak isim değiştiren ve bir blokzincir yerine 64 blokzincirden oluşacak olan yeni yapı. Bu yapı, Ethereum'un kapasitesini ciddi bir şekilde artırmaya yarayacak ancak tam anlamıyla işlerlik kazanmasının 2022 yılına yetişmesi oldukça zor görünüyor. O zamana kadar Ethereum geliştiricilerinin önerdiği diğer çözüm ise ikinci seviye dediğimiz çözümler. Bu çözümleri kullanabilmek için kullanıcıların aynı alternatif zincirlerde olduğu gibi köprüleri kullanmaları gerekiyor. 

### Arkası yarın
Bir sonraki yazımızda, 'köprü tam olarak ne demek, farklı köprü çeşitleri neler ve geçtiğimiz günlerde duyduğumuz köprü kazalarında ne yaşandı' sorularına yanıt arayacağız.


---

*Not 1: Bu yazı ilk olarak 16 Şubat 2022'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/kopruler-neden-onemli/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*
