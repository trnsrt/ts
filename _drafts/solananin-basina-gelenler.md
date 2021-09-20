Bu yazımızda Solana'nın durması olayı üzerinden blokzincir dünyasındaki kritik konulara değineceğiz. 

Geçtiğimiz hafta içinde kripto dünyasının son zamanlarında adından sıkça söz edilen Solana blokzincirinin yaklaşık 10 saat durmasını, nedenlerini ve üzerinde durulması gereken kritik konuları konuşacağız.

### Ne olmuştu?
14 Eylül Türkiye saati ile 15:00 sularında, Solana blokzinciri üzerinden sıkıntı yaşanmaya başladı. Neydi sıkıntı? Yapılan işlemler Solana blokzinciri üzerine yazılamıyordu. 

Bir blokzincirin en önemli görevi, üzerinde bulunan uygulamaların yaptığı işlemleri kayıt altına almak. Bunu yapamadığınız durumda sisteminiz durmuş, bir başka deyişle 'kalbiniz atmıyor' demektir. 

| ![heart-pulse](/assets/pulse-3530383_800.jpg)|
|:--:| 
| *Image by [Gerd Altmann](https://pixabay.com/users/geralt-9301/) from [Pixabay](https://pixabay.com/)*|

Olayın başlamasından 45 dakika sonra Solana resmi hesabından sistemde sıkıntı olduğu ve mühendislerin konu üzerinde çalıştığı tweeti [atıldı](https://twitter.com/SolanaStatus/status/1437757547235131396). 

Maalesef, konu üzerinde çalışan mühendisler, sorunu çözmekte başarısız olunca, çare olarak sistem yeniden başlatılıldı. Ertesi gün saat 9:00 sularında atılan tweet ile sistemin tekrar başarı ile çalışmaya başladığı [duyuruldu](https://twitter.com/SolanaStatus/status/1438020110451609603). 

### Neden olmuştu?

Sistemin durma nedeni olarak da, kaynakların tüketilmesi gösterildi. Normalde saniyede 60,000 işlem yapma kapasitesine sahip olmakla övünen Solana sistemine bir anda 400,000 işlem talebi geldi. Bu da sistemi tıkadı (Bir karşılaştırma olarak Ethereum blokzinciri saniyede 13 işlem yapabilme kapasitesine sahip)

Bir parça teknik detaya girersek: Sistem gelen işlemleri önceliklendirme özelliğine sahip olmadığı için sıraya alınan işlemler tıkanma yarattı.  Bunun üzerine sistem kendi kendini çatalladı ve bu çatallama daha da fazla işlem hafızası ihtiyacı doğurdu. Yeterli işlem hafızasına sahip olmayan blokzincir düğümleri ise çalışamaz hale geldi ve sistemin stabilitesi bozuldu. 

Buraya kadar takip eden okuyucularımızın aklına, 'hani blokzincirler çok sağlamdı, nasıl böyle bir olay oluyor, Ethereum'da saniyede 13 işlem yapılabiliyor ise, o da böyle bir sorun yaşamaz mıydı?' şeklinde bir soru gelebilir. 

Buna verilecek en basit cevap, blokzincirleri tek tip olarak düşünmemek gerektiği olabilir. Zira, yazılım mimarisi olarak, Solana blokzinciri ile Ethereum ya da örneğin Avalanche blokzinciri çok farklı. Ethereum'da sistem üzerinde işlem gönderebilmek hem masraflı, hem de sistem gelen talepleri bir ön havuzda tutuyor ve en yüksek ücreti kim verdiyse onu öne alıyor. Yani eğer benzer şekilde 400,000 adet talep Ethereum'a gelseydi, sistem üzerinde ücretler arşa çıkacak, normal kullanıcılar işlem yapamayacaktı, ancak sistem işlemeye devam edecekti. Solana da ise mimari tercihler gereği sistem durdu. 

### Nasıl tepkiler geldi?

Solana'nın bu durma ve tekrar çalışmasına değişik kesimlerden değişik tepkiler geldi. Bunların ağırlığını, rakip bir ağ olan Avalanche'ın kurucusu Emin Gür Sürer Hoca'nın nezaket göstererek Solana ekibine attığı 'bu süreçte henüz yolun başındayız ve bu tip sorunlar olabilir. Solana ekibine güç diliyorum' mealindeki [tweet](https://twitter.com/el33th4xor/status/1437888512221716484)'inde olduğu gibi destek mesajları oluştursa da eleştiriler de yok değildi. 

En büyük eleştiri kaynağı, Solana sisteminin ve ekibin başındaki [Anatoly Yakovenko](https://twitter.com/aeyakovenko)'nun attığı bir tweet üzerine geldi. Bu tweet mesajında Yakovenko 'aynı şey zamanında Ethereum'un da başına gelmişti' yazdı](https://twitter.com/aeyakovenko/status/1437778676804984852). Anatoly'nin Ethereum'u örnek göstererek kendi sorununu küçültmeye çalışması Ethereum camiasını kızdırdı. Zira, olay bir dış atak (DDOS atak olması) nedeniyle benzese de, Ethereum o atak sırasında çalışmaya devam etmişti (Hudson Jameson iki olayın karşılaştırmasını [şu tweet selinde](https://twitter.com/hudsonjameson) net olarak yazmış. Bu arada, Türkiye'de Ethereum camiasının önemli isimlerinden [TobbyKitty](https://twitter.com/TobbyKitty)'nin Anatoly ile olan atışmasını da [şuraya ekleyelim](https://www.hizliresim.com/f2zrxa1))

Sonrasında Anatoly'in Bloomberg'e verdiği [demeçte] 'ne olacak ki, büyüme sancıları' minvalinde sözler kullanması ve Solana'nın en büyük yatırımcılarından olan Kyle Samani'nin 'zaten beta versiyonu, bekleniyordu' şeklinde [tweet](https://twitter.com/KyleSamani/status/1437882572801970177?s=20) atması, üzerinde onlarca proje olan, yaklaşık 10 milyar ABD dolarından fazla yatırımcı parası [kilitlenmiş](https://defillama.com/chain/Solana) ve 46 milyar ABD Doları piyasa değerine [sahip](https://www.coingecko.com/en/coins/solana) bir altyapı projesine açıkcası çok da yakışmıyor.

Aslına bakarsanız bu işin magazinsel yanı. Asıl kritik konu, Yakovenko'nun Solana sistemini yürüten onaylayıcıları (validatörler) discord kanalına çağırıp, onlarla birlikte sistemin restart etmesi kararını vermesi. 'Ne var bunda, sorunu çözmüşler işte' diyebilirsiniz, ancak bu Solana sisteminin ne kadar merkeziyetsiz olduğu konusunda ciddi soru işaretleri barındırıyor. Sistemi yeniden çalıştırabilmek için ağda rehin edilen paranın %80'nine sahip olan onaylayıcıların olumlu oyu gerekiyor. 

İki yönden karşılaştırma yapalım: Solana üzerinde 1000 tane [onay veren düğüm var](https://solanabeach.io/validators) ve bunların ilk yirmisi toplam onay için rehin edilen paranın %33'üne sahipler. Ethereum'un önümüzdeki yıl geçeceği aynı sistem için şu anda 240,000 [onaylayıcı var](https://mainnet.beaconcha.in/). Bu onaylayıcıların her biri en az 32 ETH rehin etmek zorundalar, ama güç konsantrasyonu olmasın diye daha fazla koysa bile yine de tek bir oy hakları var. Bu nedenle Ethereum'un onay mekanizmasında merkezileşme diğer sistemlere daha zor.  

Bir başka açıdan ise, Solana üzerindeki düğümleri kullanabilmeyi sağlayan sadece tek bir yazılım (client) var, bu da merkezilik yaratıyor. Örnek olarak Ethereum'da şu an aktif olan 3568 düğümü yöneten [altı tane farklı yazılım bulunmakta](https://www.ethernodes.org/).

Bugün bu olay için bir araya gelen onaylayıcılar, yarın kullanıcıların aleyhine bir konuda bir araya gelirlerse o zaman ne olacak? Ethereum'un bu kadar işlem yoğunluğuna ve bu kadar yüksek işlem ücretlerine karşın hâlâ kurumların ve kişilerin DeFi için ilk tercih ettiği adres olmasının arkasında yatan en önemli nedenlerden biri uzun süredir tıkır tıkır çalışıyor olması ise, bir diğeri de, herhangi bir zümrenin etkisi altında olmadığı için 'nötr' bir altyapı sağlayıcı olarak görülmesi. 

### Sonuç 

Blokzincirler için merkeziyetsizlik, hem dış ataklara karşı korunma açısından hem de blokzincirin gideceği yolu belirlemek açısından hayati. Hep söylediğimizi tekrar edelim şimdi. Merkeziyetsizlik uzun ince bir yol. Solana bu anlamda bu yolun henüz başında. Merkeziyetsiz bir yapı olduğunu söylemek neredeyse imkansız, ama bu da şu an için normal. Ondan beklenen yavaş yavaş merkeziyetsiz olma yolunda ilerlemesi. Dileriz bu konuda hızla yol alırlar. 
