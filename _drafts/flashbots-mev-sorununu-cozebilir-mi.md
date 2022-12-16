# Yazı II Flashbots MEV sorununu çözebilecek mi?
Bu yazımızda, Ethereum protokolü oyuncularının en çok tercih ettiği yazılımın sahibi olan Flashbots ekibinin, MEV (Maximal Extractable Value) ve merkezileşme konularında şimdiye kadar yaptıklarını ve bundan sonraki hedeflerini gözden geçireceğiz. 

MEV (Maximal Extractable Value), Ethereum (ve Cosmos benzeri diğer blokzincirler) üzerindeki işlemlerin sıralarının değiştirilerek, işlem ücretlerini artırabilmek için yapılan her tür düzenlemeye verilen ad. Detaylarını ve bu konuda yaşananları bir [önceki yazımızda](/genel/2022/12/05/blokzincirlerin-zayif-karni-mev.html) bulabilirsiniz.

Bu yazımızda, gelin önce MEV konusunda özellikle [Flashbots](https://www.flashbots.net/) tarafından geliştirilen önlemlere bakalım. Sonrasında ise Flashbots'un gelecek planlarına değinelim. 


| ![lightning](/assets/lightning-gd2556cb2a_800.jpg)|
|:--:| 
| *Image by [Artem_Apukhtin](https://pixabay.com/users/artem_apukhtin-3343718/) from [Pixabay](https://pixabay.com/)*|

### Flashbots MEV'ye nasıl çözümler getirdi?

MEV'nin kullanıcılara verdiği zararın ayyuka çıkması sonrası, farklı geliştirici grupları tarafından bu soruna çözüm bulunabilmesi amacıyla pek çok öneri ortaya atıldı. Bu çözüm önerileri içinde en çok tutulanı bir araştırma kuruluşu olan Flashbots'un geliştirmeleri oldu. Hızlıca neler yaptıklarına bir göz atalım:

Flashbots genel olarak MEV sorununu temelden çözmek yerine, yarattığı sorunları azaltmaya ya da idare edilebilir hale getirmeye odaklanan bir oluşum. Adlarını ilk olarak 2020 yılında çıkardıkları [MEV-Geth](https://github.com/flashbots/mev-geth) isimli Ethereum yazılımı ile duyurdular. Yazılımın temel fonksiyonu, madencilere gelen işlem emirlerini açık bir pazaryerinde ihaleye çıkararak daha görünür yapmak. MEV-Geth sayesinde madenciler kendilerine gelen bu emirleri  daha rahat işlemeye başladılar. Sonuçta hem sistem üzerindeki gereksiz işlem kalabalığı önlendi, hem de madencilerin kârları arttı[^1].

Yazılım o kadar başarılı oldu ki, Nisan 2021 itibariyle ETH üzerindeki işlemlerin %84'ünü gerçekleştiren madenci havuzları MEV-Geth yazılımını kullanır hale geldiler. 

### Merge sonrası neler değişti?

Ethereum'un 15 Eylül sonrası uygulamaya giren yeni versiyonunda artık madenciler yok. Onların yerini Ethereum sistemine ETH'lerini rehin etmiş (ingilizcesi stake) onaylayıcılar aldı. Yeni versiyonda işlemler şu şekilde yürüyor:

- Kullanıcı işlemini cüzdanı üzerinden imzalar ve genel işlem havuzuna gönderir (ya da bu iş için kurulan özel aracılara) 
- Araştırmacı/tarayıcı (ingilizcesi 'Searcher') kârlı işlemleri bir araya getirip, blok üreticilerine verir. 
- Blok üreticileri, blokları üretip onaylayıcıların onayına sunar. 
- Onaylayıcılar ise kendilerine sunulan bloklardan en kârlısını (en yüksek işlem ücreti önereni) onaylayarak blok oluşumuna izin verir. 

| ![Ethereum_sistemi_oyunculari](/assets/ethereum_sistem_oyunculari_v5.jpg)|
|:--:| 
| *Yeni Ethereum sistemindeki oyuncular. Eskiden madenciler hem blok üretimini hem de onaylamasını yapıyorlardı. Yeni sistemde, blok üretimi daha merkezi ve güçlü yapılarla, blokların onaylanması ise daha hafif ve merkeziyetsiz onaylayıcılar tarafından yapılacak*|

Ethereum geliştiricileri, özellikle bloğu oluşturanlar ile onaylayanları ayırarak adeta bir güçler ayrımı yapmaya çalışıyorlar. Zira, her iki işi bir arada yapabilmek oldukça zahmetli ve yüksek kapasite gerektiriyor. Her makine yüksek kapasite ile işlem yapamayacağı için ikisini bir arada yapmak sistemin merkezileşmesi tehlikesini doğuruyor. O nedenle, Ethereum blok üreticilerinin uzman haline gelip yüksek kapasite ile işlem yapmasına dolayısıyla merkezileşmelerine izin verirken, onaylayıcıların yüklerini hafif tutarak o tarafı merkeziyetsiz hale getirmeye çalışıyorlar. Yani bir nevi onaylayıcı tarafı için blok üretici tarafını feda ediyor. 

İdeal hedeflenen sistem işleyişi şu şekilde: Tarayıcılar, olabildiğince kârlı işlemleri demet haline getirip blok üreticilerine sunarlar. Blok üreticileri de bunlardan kendilerine en çok işlem ücreti ödeyen tarayıcıların demetlerini seçerler. Benzer şekilde blok üreticileri de, ürettikleri blokların kabul görüp işleme alınması için olabildiğince fazla kârı onaylayıcılara teklif ederler. Yani işlem ücretleri zincirin sonundaki onaylayıcılara doğru akar. 

Yeni durumda MEV ne olacak? Sistem, yukarıdaki tarayıcı, blok üreticileri arasındaki rekabeti artırarak ortaya çıkan MEV'yi olabildiğince onaylayıcı tarafına aktarmaya çalışıyor. 

### Flashbots cephesinde ne gibi gelişmeler oldu?

Ethereum'un yeni versiyonu ile birlikte, Flashbots eski sistemde kullandığı MEV-Geth yazılımının yerine Ethereum'un yeni sistemine hazırlık için [MEV-Boost](https://github.com/flashbots/mev-boost/) yazılımını uygulamaya aldı. 

Aslına bakarsanız MEV-Boost Ethereum'un gelecekteki yol haritasının önemli bir parçası ve sistem oyuncuları arasında 'kuvvetlerin ayrılığı' prensibini getirecek olan PBS (blok teklif edenler ile blok üreticilerin ayrılması İngilizce proposer-builder-separation) geliştirmesinin bir ön provası olarak görülebilir. Bu yazılım, gerek tarayıcılar gerekse blok üreticileri tarafından kullanılan şeffaf bir sistem. Blok üretim işini makinelerin tek başlarına yapmak yerine büyük blok üreticilerine devretmesini (outsource etmesini) sağlayan bu sistem, o kadar başarılı oldu ki, şu an [üretilen blokların %90'ında MEV-Boost yazılımı kullanılıyor](https://explore.flashbots.net). 

Bu sefer de başka bir sorun ortaya çıktı. O da Flashbots'un işlem taleplerini tarayıcılardan blok üreticilerine ileten kendi aracıları (bunlara taşıyıcı da denebilir ingilizcesi relayer) üzerinden gelen işlemlere sansür uygulaması. Flashbots ABD'de kurulu bir şirket. ABD'nin kara para aklama ile ilgili iki kuruluşundan biri olan OFAC'ın Tornado Cash uygulamasını ve bu uygulamayı kullanan adresleri kara listeye aldığına [önceki bir yazımızda](/genel/2022/08/31/Ethereum-sansure-nasil-tepki-verecek.html) değinmiştik. İşte, Flashbots da bu yaptırımlara uyarak, kendine ait taşıyıcılara sansür uygulamaya başladı. 

Bunun sonucu olarak yeni versiyona geçtikten sonra Ethereum üzerindeki işlemlerin yaklaşık %72'si sansürlenmeye başladı. Aşağıdaki tabloda, 15 Eylül'den bu yana oluşan bloklardaki işlemleri görüyorsunuz.

| ![Ethereum_bloklar](/assets/ofac-compliant-blocks_221216_800.jpg)|
|:--:| 
| *Ethereum'un yeni versiyonu sonrası durumu. Oluşturulan blokların %88'i Flashbots'a ait olan MEV-Boost'u kullanıyor. Tüm blokların %68'i ise OFAC ile uyumlu blok üreticileri tarafından oluşturulmuş. MEV-Boost kullananlardan %20'lik bir kesim ise Flashbots taşıyıcısı kullanmamış, yani sansür uygulamamış. %12'lik bir kısım ise MEV-Boost kullanmayanlar tarafından üretilmiş. Kaynak: [MEV Watch](https://www.mevwatch.info)*|

Tabloda, gördüğünüz gibi MEV-Boost kullanan blok üreticileri toplam blokların %90'ını üretmişler. Bunların içinde %68'i Flashbots taşıyıcı kullanmış. Burada hemen MEV-Boost yazılımı ile Flashbots taşıyıcının farkından bahsetmek gerekiyor. MEV-Boost bir yazılım ve isteyen herkes tarafından kullanılabiliyor. Flashbots bu yazılım ile birlikte otomatik gelen bir taşıyıcı ama isteyen bu taşıyıcıyı değiştirebilir. Aynı eskiden Windows bilgisayarlarda otomatik varsayılan tarayıcının Internet Explorer olması gibi. MEV-Boost en fazla kâr getiren yazılım olduğu için tarayıcı ve üreticiler tarafından en çok tercih edilen yazılım. Bu üreticilerden bir kısmı OFAC listesine uymak için Flashbots taşıyıcı kullanıyor, ufak bir kısmı (yukarıda sarı alanda gördükleriniz) ise MEV-Boost kullanmaya devam edip sansüre karşı olan başka taşıyıcılara geçmiş durumda. 

Bir ara OFAC ile uyumlu blokların sayıları %80'e kadar çıkmışken, sonrasında bu rakam şu anki %68 seviyelerine geldi. Bunun birkaç nedeni var. Birincisi, Flashbots'un kendi taşıyıcısını açık kaynak yapması. İkincisi, taşıyıcıların sadece OFAC uyumlu blok üreticilerinden değil, tüm blok üreticileri ile çalışmaya başlaması. Üçüncüsü ise Flashbots tarafından uygulamaya konan [yeni bir uygulama](https://writings.flashbots.net/the-cost-of-resilience/). 

### MEV ve merkezilik önlenebilir mi?
"Bu sistem adil değil, MEV önlenemez mi?" diye soracak olursanız, buna Ethereum özelinde kesin bir cevap yok.  Burada temel hedeflenen, önce MEV'nin kullanıcıya olan etkisini minimuma indirmek, sonra da kalan MEV'nin tarayıcı ya da blok üreticilerine değil de, onaylayıcılara gitmesini sağlamak gibi görünüyor.  

Flashbots benzeri ürünler, MEV'nin azaltılmasını ve daha adil bölünmesini sağlıyorlar. İleride, Ethereum'un yeni sistemi oturduğu zaman, eğer hedeflenen rekabetçi yapı gerçekleşirse, MEV'in ağırlıklı bir kısmı sistemi koruyan onaylayıcılara gidecek. Onaylayıcılar, ETH stake ederek işlemleri onaylıyorlar ve sistemin güvenliğini sağlıyorlar. Böylece MEV bir nevi sistemin güvenlik bütçesine katkı yapmış olacak.[^2] 

Ethereum'un geliştirmeleri maalesef uzun zaman alıyor. Bu süre zarfında ne olacak peki? Burada Flashbots, geçtiğimiz günlerde [SUAVE isimli yeni bir çalışma yayınlayarak](https://writings.flashbots.net/the-future-of-mev-is-suave/) oluşan sorunlara çözüm bulmayı hedeflediğini açıkladı. Neler bunlar?

SUAVE'nin birkaç hedefi var. Bunlardan birincisi, MEV ile ortaya çıkan değerin kullanıcılara geri verilmesi - ki bu MEV'in kötü kullanımından kurtulmanın en büyük çözümü olabilir. Nasıl olacak bu? İşlemlerin gizlilik içinde sıralanması yoluyla. 

SUAVE'nin ikici hedefi, blok üreticilerine sadece Ethereum değil, diğer alternatif blokzincir ağlar (Cosmos, Avalanche gibi) ya da ikinci seviye altyapılar (Arbitrum, Optimum gibi) ile entegre olabilecekleri bir sistem sunmak. SUAVE yukarıda yazdığımız sıralama işlemini tüm ağlarda yaparak blok üreticilerine sunacak. Bu sayede blok üreticileri de SUAVE kullanmaya özendirilecek.

Üçüncü önemli nokta ise, çok güçlü ve sayıca az olan blok üreticilerinin arasındaki rekabetin artabilmesi için oluşturulan SUAVE'nin olabildiğince merkeziyetsiz bir hale getirilmesi.[^3]

Kısacası, Flashbots burada Ethereum'un yol haritasında yer alan güçlü blok üreticilerinin daha merkeziyetsiz olmasını sağlayacak ve bu sayede oluşan rekabet sonucu MEV'nin kullanıcılara geri verileceği bir çözüm vaadi ile geliyor. Bunu başarabilecekler mi, heyecanla izleyeceğiz. Şu ana kadar yaptıkları iki hamlede (MEV-Geth ve MEV-Boost) elde ettikleri pazar payı başarısı, üçüncü hamlenin yapılabilirliği konusunda bir referans sağlasa da, bu sefer altına girdikleri yükün çok daha ağır olduğunu belirtmek gerek. 

### Sonuç 
Flashbots, geliştirdiği MEV çözümleri ile madenciler (Ethereum'un eski versiyonunda), tarayıcılar ve blok üreticileri arasında şeffaflık sağlamayı başarırken, merkezilik ve sansür konularında tıkandı. Yeni çıkan SUAVE sürümü ile bu sorunlara da çözüm bulmak için uğraşıyorlar. Bunda başarılı olacaklar mı, hep birlikte göreceğiz. 

---

Kaynaklar:

[MEV in DeFi](https://etherworld.co/2022/04/05/mev-research-report/#section111) - araştırma raporu 

[The Future of MEV is SUAVE](https://writings.flashbots.net/the-future-of-mev-is-suave/)  - Flashbots post

[MEV Manifesto](https://members.delphidigital.io/reports/mev-manifesto) Delphi Digital raporu

MEV Markets Part 1 - "[PoW](https://mirror.xyz/0xshittrader.eth/WiV8DM3I6abNMVsXf-DqioYb2NglnfjmM-zSsw2ruG8)",  Part 2 - "[PoS](https://mirror.xyz/0xshittrader.eth/c6J_PCK87K3joTWmLEtG6qVN6BFXLBZxQniReYSEjLI)",  Part 3 - "[Payment for Order Flow](https://mirror.xyz/0xshittrader.eth/f2VSuoZ91vAbCv82MtWM-Gosyf_DeUXfPlDx3EYV3RM)" yazıları

Konuya daha fazla ilgi duyanlar, bu alandaki tüm önemli kaynakları bir araya toplayan [şu GitHub sayfasına](https://github.com/0xemperor/Awesome-MEV) da göz atabilirler. 


Dipnotlar:

[^1]: "Bu iki problemi nasıl çözdüler?" diye soracak olursanız: Önceden kullanılan 'en yüksek parayı veren en yukarı çıkar' yönteminde tarayıcılar blokzincir üzerine emir göndererek işlemlerini önceliklendirmeye çalışırlardı. Bu da pek çok başarısız emir nedeniyle zincirin gereksiz yere dolmasına neden oluyordu. MEV-Geth ile işlemleri demetler (ingilizcesi bundle) haline getirip, zincir-dışı olarak göndermeye başladılar. Oluşturulan pazaryerinde tarayıcılar hazırladıkları demetleri gönderiyorlar ve MEV-Geth en kârlı olanları alıp işleme sokuyor. Böylece madencilerin de kârı artıyor. 

[^2]: Bu alanda merkeziyesizliği teşvik etmek için Flashbots'un Flashbots Builder isimli blok üreticisi yazılımı [açık kaynak haline getirdiğini](https://writings.flashbots.net/open-sourcing-the-flashbots-builder) de ekleyelim. 

[^3]: Blok üreticilerindeki merkezileşmeye en iyi örnek, Kasım ayının son bir haftasında [en büyük 5 üreticinin toplam blokların %85'ini üretmiş](https://www.relayscan.io/overview?t=7d) olması
