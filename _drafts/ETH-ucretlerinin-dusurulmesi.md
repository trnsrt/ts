### ETH'nin yüksek işlem ücretleri
Ethereum üzerinde işlem yapıyorsanız, ki bunun için yüksek ihtimal DeFi ürünleri ya da NFT kullanıyorsunuzdur. Eğer öyleyse yüksek işlem ücretleri canınızı sıkıyor olmalı. 

| ![coinmetrics_eth_median_fees_1yr](/assets/eth_median_fees_coinmetrics_1yr.png)|
|:--:| 
| *2020 yılı ETH işlem ücretleri. Kaynak: [Coinmetrics](https://network-charts.coinmetrics.io)*|

### Neden yüksek bu ücretler?
Ethereum sistemi, başlangıçtan beri işlem ücretlerini belirleme işini madencilere bırakmış durumda. Her ne kadar kullanıcılar bu ücretleri teklif ediyor olsalar da, sistem müzayede şeklinde işlediği için, madencilerin hangi işlemi gerçekleştireceklerini seçme hakkı var. 

Bu da ücretlerin yükselmesine neden oluyor. Özellikle, 2020 yazında DeFi'nin sık kullanıldığı zamanlarda olduğu gibi. Kullanıcıların yaşadığı birkaç sorun var: İşleminizin ne zaman gerçekleşeceğini bilemiyorsunuz. Keza tam olarak ne ücret ödeyeceğinizi de. Kullandığınız cüzdanınız size bir tahmin veriyor ama o tahmin genelde tutmuyor. Fiyatı manuel olarak ayarlamak herkesin sıklıkla yaptığı ve sevdiği bir seçenek değil. 

### Çözüm ne? EIP 1559
Böyle bir sorunun yaşanacağı aslında çok öncesinden belli idi. Ethereum'un harika çocuğu Vitalik Buterin, 2018 yılında bunu bir makale haline getirmişti ([buradan bu çok teknik makalenin pdf'ine ulaşabilirsiniz](https://ethresear.ch/uploads/default/original/2X/1/197884012ada193318b67c4b777441e4a1830f49.pdf)). 

Sonrasında bu durumu Nisan 2019'da bir [iyileştirme önerisi olarak Ethereum sistemine sundular](https://eips.ethereum.org/EIPS/eip-1559). EIP 1559 no'lu bu öneride sorunları şu şekilde sıraladılar: 

- İşlem ücret seviyesi dalgalanması ile bunun sosyal maliyetleri arasındaki uyumsuzluk
- Kullanıcılar için gereksiz gecikmeler
- Müzayede sistemindeki verimsizliklerin kullanıcıların fazla ücret ödemesine neden olması
- Uzun vadede ödüllerin kalmadığı durumda sadece işlem ücreti alan madencilerin sistemde istikrarsızlık yaratması ihtimali

Çözüm önerilerini ise şu şekilde oldu: **Bir baz fiyat belirlenmesi, ve üzerine madencilere bahşiş verilmesi.** Gelin biraz açıklayalım bunu: 

Baz fiyat, sistemin yoğunluğuna göre azalıp artacak bir ücret olacak. Öncelikle sistem kapasitesi 18 milyon gas'a yükseltilecek ve bunun %50'si orta seviye olacak. Eğer işlem yoğunluğu artarsa, ücret de artacak. Ancak bu artış kademeli olacağı için, cüzdanlar kullanıcının ücretini daha rahat ve doğru tahmin etme imkanı bulacaklar.  Kullanıcı eğer isterse, şimdi olduğu gibi, işlemini daha hızlı yapabilmek için manuel olarak fiyat girebilecek. 

**En kritik konu ise bu baz ücretin madencilere ödenmeyip, ETH olarak yakılması olacak**. 

Peki madenciler? Onlar ne kazanacak? Sisteme göre, madenciler kullanıcıların yapılan işlemler karşılığı ödeyecekleri bahşişler ile iş yapmaya devam edecekler. 

#### Ne faydası olacak kullanıcılara?
Öncelikle kullanıcılar için birkaç faydayı hemen saymak mümkün: 
- Daha rahat tahmin edilebilir işlem ücretleri
- Fahiş işlem ücretlerinin azalması
- İşlem sürelerinin daha rahat tahmin edilebilmesi

#### Asıl büyük fayda Ethereum sistemine
Burada asıl büyük faydayı Ethereum sisteminin göreceğini hemen belirtelim. Zira, baz ücretin madencilere ödenmeyip ETH olarak yakılması, piyasadaki para miktarına ciddi bir etki yapacak.  Vitalik'in tahminlerine göre 2020 yılı içindeki DeFi ile hareketlenen pazardaki yoğunluğun devam etmesi durumunda, yıllık olarak 1 milyona yakın ETH'nin yakılması söz konusu olabilir bu iyileştirme sayesinde. 

Şu anda Ethereum sistemi yıllık olarak 4.7 milyon yeni ETH'yi ödül olarak madencilere dağıtıyor. Ethereum sisteminin 1.0'dan 2.0'a geçmesi ile birlikte bu ödül sistemi de değişiyor. Artık, ödül madencilere değil staking yapanlara verilecek. Buradaki miktarı staking yapanların sayısına göre değişse de 500 bin ile 1 milyon ETH arasında olması bekleniyor. 

Böyle bir durumda ETH içindeki parasal büyüklüğün 4.7 milyon artması yerine sabit kalması, hatta staking ödülleri eğer 1 milyonun altında kalırsa, yakılacak olan 1 milyon ETH sayesinde azalması bile beklenebilir. Bu da Ethereum'u Bitcoin'in azalan enflasyon rakamlarının ötesinde deflasyon yaratan bir konuma sokabilir. 

### Bir de roll-up çözümler gelecek
Yukarıdaki ücretler, Ethereum blokzincirine direkt olarak yazılmak isteyen, yani blok üzerinde bir alan almak isteyenler için söz konusu. Bunun yanında hem Ethereum geliştiricileri hem de DeFi platformları ana zincir üzerinde değil 2. katman dediğimiz bir üst seviyede çözümleri de teşvik ediyorlar. Örneğin [Synthetix böyle bir çözümü test ettiğini açıkladı bile](https://blog.synthetix.io/why-optimism/). 

Roll-up çözümlerde, yapılan işlemler tek tek blokzincire yazılmak yerine, toplanarak bir araya getiriliyor ve toplu olarak yazım işlemi gerçekleşiyor. Bu da Ethereum üzerinde daha az blok alanı işgal etmek demek. 

Tabii böyle çözümlerin yapılan işlemi nihayetlendirme anlamında gecikmelere yol açması söz konusu. Öte yandan, farklı DeFi platformlarının farklı çözümleri kullanması da sorun yaratabilir. Bu gibi teknik sorunlara çözümler yavaş yavaş geliştiriliyor. 

Ortada olan pek çok farklı roll-up çözümünden hangisi ya da hangilerinin ön plana çıkacağını göreceğiz. Bu çözümleri kullanan DeFi platformlarının işlem ücretleri konusunda müşterilere avantaj sağlayacağı da kesin. 

### Sonuç
EIP 1559 ve rollup çözümleri, Ethereum'daki işlem ücretlerinin düşmesi için gerekli iki insiyatif. Bu iki konunun bir an önce hayat geçmesi, Ethereum'un gün geçtikçe artan rakiplerine karşı kendini koruması için kritik. Süreç nasıl işleyecek hep birlikte göreceğiz. 

