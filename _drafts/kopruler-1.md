Bu yazımızda, 2022 yılında çok konuşacağımız köprüler konusuna değiniyoruz. İlk yazımızda cevaplamaya çalışacağımız soru: Blokzincirlerde neden köprülere ihtiyaç duyuyoruz?

### Blokzincirler birer ada mı?

Sıkça kullandığım bir benzetme var: Yaşadığımız 'fiziki' dünyayı bir kıtaya benzetirsek, blokzincirler ana kara çevresine sıralanmış küçük adalar gibiler. Bizim bu adalara gidebilmemizi, yani itibari (fiat) paradan kriptoparaya geçişimizi genelde kripto alım-satım platformları sağlıyorlar. Peki bu adalar arasındaki gidip gelmek istersek? Bir blokzincirden öbürüne geçmek istersek? O zaman birkaç yol var ama önümüzdeki dönemde en sık konuşacağımız yol köprüler olacak gibi görünüyor. 

### Blokzincir ve köprü ilişkisi

Blokzincir dediğimiz esasında bir yazılım ve temel işlevi üzerine kurulu olan projelere altyapı olmak. Bunu yaparken, genelde blokzincirler kapalı bir dünya olarak kuruluyorlar. Ne yaparsanız, bu 'ada' içinde yapıyorsunuz.  Peki nasıl bir blokzincirden diğerine geçiş yapacağız? 

| ![L1_ecosistemi](/assets/Layer-1-Ecosystem-Map_800_v3.jpg)|
|:--:| 
| *Blokzincir Dünyası Kaynak: [Blockchain Comparison](https://blockchain-comparison.com/blockchain-protocols/)*|

Bunun iki temel yolu var. Birincisi, bir kriptopara borsası kullanabilirsiniz. Bunun oldukça zahmetli bir yöntem olduğunu belirtelim. Bir örnek ile açıklayalım: Elinizde Ethereum ağında tuttuğunuz bir ETH var ve bunu Avalanche ağına geçirmek istiyorsunuz. ETH'nizi bir borsada bulunan hesabınıza aktaracaksınız. Sonra o ETH'yi satacaksınız (muhtemelen en likit olan bir stabil para örneğin USDT ile). Arkasından aldığınız stabil para ile AVAX satın alacaksınız. En sonunda da bu AVAX'ın borsadaki hesabınızdan Avalanche üzerindeki cüzdanınıza çekeceksiniz. Tam dört adım. Boşa zaman kaybının yanında bir de para kaybı: Ethereum ve Avalanche üzerinde  transfer için ödeyeceğiniz ücretin üzerine üzerine bir  de al-sat sırasında uğrayabileceğiniz kayıplar. 

İkinci yol ise bu iş için bir köprü kullanmak. Köprüler sayesinde bir blokzincir üzerindeki cüzdanınızdan paranızı direkt olarak diğer blokzincir üzerindeki hesabınına aktarabilmek. Hangisi kulağa daha kolay geliyor? Teoride ikincisi tabii ama pratiğe gelince henüz orada değiliz. 

### Neden ihtiyaç duyuyoruz köprülere?
"Daha yeni blokzincirlere alışmaya başlamıştık, bu köprüler nereden çıktı? Ne gerek var şimdi buna?" diye sorabilirsiniz. Gelin kısaca bir bakalım: 

#### Ethereum'un yüksek işlem ücretleri
Öncelikle sorunun temeli 2020 yılı ortalarından beri hayatımıza giren DeFi yani merkeziyetsiz finans ve geçtiğimiz yıl piyasayı sarsan NFT'lere dayanıyor. Gerek DeFi gerekse NFT'lerin ağırlıklı olarak ortaya çıktığı ağ Ethereum oldu. Neden? Çok basit. Para yani değer Ethereum blokzincirinde toplanmıştı ve girişimler için ilk adres hep Ethereum oldu. 

Burada unutulmaması gereken temel nokta blokzincirlerin her ne kadar yeni teknolojiler olsalar da en ileri teknoloji ürünler olmamaları. Hep söylüyoruz, merkeziyetsizlik blokzincirler için olmazsa olmaz. Öte yandan bu durumun getirdiği belli dezavantajlar var. Sisteminizi  ne kadar dağıtık tutmaya çalışırsanız, o kadar basit ve küçük olmak zorundasınız. Aksi takdirde, karmaşık ve çok yer/işlemci kapasitesine ihtiyaç duyan blokzincirleri yürütebilecek makine bulmakta zorlanırsınız ve bunun sonucu olarak konsantrasyon olur ve merkeziyetsizlikten ödün vermiş olursunuz. 

Ethereum da kendisine öncelik olarak merkeziyetsizliği seçtiği için, DeFi ve NFT'ler tarafından gelen yoğun talebi karşılamada çaresiz kaldı. İşlemler hiçbir zaman durmadı ancak oldukça pahalandı. Makul fiyatlar ile işlem yapmak isteyenlerin saatlerce beklemek zorunda kaldığını gördük. Bu duruma hâlâ net bir çözüm bulunabilmiş değil. Kendimden bir örnek vereyim, son birkaç aydır yüksek işlem ücretleri nedeniyle Ethereum üzerinde neredeyse hiç işlem yapmadım. 

Bunun fırsat bilen Ethereum rakibi blokzincirler hızlı ve ucuz işlem önerisi ile ciddi bir yatırımcı kitlesini kendilerine çektiler. 2021 yılı başlarında 'tüm DeFi Ethereum üzerinde döner' diye konuşurken son zamanlarda bunun böyle olmadığını görmeye başladık: 

| ![TVL_on_L1s](/assets/TVL_on_L1s_800.jpg)|
|:--:| 
| *Blokzincirler üzerinde kilitli değerin blokzincirlere göre dağılımı. Kaynak: [Coingecko Kriptopara Raporu](https://www.coingecko.com/buzz/2021-yearly-cryptocurrency-report) Sayfa 32*|

#### Alternatif zincirler tarafından verilen teşvikler
Tabii sadece düşük işlem ücretleri değil kitleleri diğer blokzincirlere yönlendiren. Zira, herhangi bir blokzincirde özellikle finans alanında bir işlem yapmak istediğinizde iki temel kriter var yatırımıcının baktığı. Birincisi getiri ikincisi ise likidite. DeFi üzerindeki protokollerin likidite yaratabilmek için 2020 yılı yaz aylarında nasıl teşvikler verdiklerinden bahsetmiştik. İşte Ethereum'un üzerindeki yoğunluk sonucu gidecek yer arayan likiditeyi çekmeye çalışan alternatif blokzincirlerin, 2021 yılı içinde kendi üzerine ürün geliştirmeleri için DeFi protokollerine çok ciddi teşvikler verdiğini gördük. 

#### Ethereum üzerine kurulu ikinci seviye çözümler
Ethereum geliştiricilerinin değerin kendi ağlarında kalması için gösterdikleri yoğun bir çaba var ancak bu çalışmaların meyve vermesi oldukça zaman alacak gibi görünüyor. Bunlardan birincisi Ethereum'un yeni versiyonu - başlangıçta Ethereum 2.0 olarak adlandırılan ama yakın zamanda 'Execution Layer' olarak isim değiştiren ve bir blokzincir yerine 64 blokzincirden oluşacak olan yeni yapı. Bu yapı Ethereum'un kapasitesini ciddi bir şekilde artırmaya yarayacak ancak tam anlamıyla işlerlik kazanması 2022 yılına yetişecek mi, oldukça zor görünüyor. O zamana kadar Ethereum geliştiricilerinin önerdiği diğer çözüm ise ikinci seviye dediğimiz çözümler. Bu çözümleri kullanabilmek için kullanıcıların aynı alternatif zincirlerde olduğu gibi köprüleri kullanmaları gerekiyor. 

### Arkası yarın
Bir sonraki yazımızda, köprü tam olarak ne demek, farklı köprü çeşitlerine neler ve geçtiğimiz günlerde yaşanan köprü kazalarında neler oldu konularına değineceğiz. 
