Bu yazımızda DeFi dünyasındakilerin bilgi ihtiyacını karşılamaya yönelik, nispeten yeni ama önemli bir işlevi yerine getiren The Graph Protocol'den bahsedeceğiz. 

### Dış dünya ile bir köprü: Chainlink

Hatırlayanlar olacaktır, geçmişteki bir [yazımızda] Chainlink'ten bahsetmiştik. Bundan önceki pekçok yazımızda da DeFi'nin nasıl kendi başına bir dünya olduğuna dem vurduk. Herhangi bir DeFi ürünü üzerine kurulu olduğu DeFi platformlarının içinde güzel güzel yaşıyor. (Şu an ağırlıklı olarak Ethereum bu platform ancak rakipleri de geliyor). Ancak kimi zaman bu ürünlerinde kendi blokzincir dışı ile de irtibatı olması gerekiyor. 

Yine hatırlarsanız, DeFi ürünlerinin temelini akıllı kontratlar oluşturuyor. Akıllı kontrat aslında bir yazılım. Kendisine söyleneni otomatik olarak genellikle 'el değmeden' yapıyor. Harekete geçmesi için uygun koşulların oluştuğunu anlaması gerek. Eğer bu 'işlem yapmayı tetikleyici' bilgi blokzincir içinde ise işi nispeten kolay. Kontrat içinde yazılı bilgi kaynağına giderek bilgiyi alıyor. Ancak bilgi dışarıda ise o zaman işi zor. Bu bir nevi, kurulu bir oyuncak arabanın evin içinde dönüp dururken duvara toslayıp durması gibi. Kontratın bu bilgiyi alacağı bir yer yok. Bu bilginin ona sağlanması gerekiyor. İşte oracle dediğimiz bilgi kaynakları bu bilgiyi blokzincir dışı dış dünyadan alıp kontratın hazmedeceği bir hale getirip ona veriyorlar. Oracle'lar dış dünya ile blokzincir arasında bir köprü vazifesi görüyor adeta. Chainlink de bunların en ünlü ve büyük olanı. 

Bu yazımıda ise size blokzincirler ile dış dünya arasında köprü olarak işlev yapan bir başka önemli aracıdan bahsedeceğiz. The Graph. 

### Nedir Graph? Ne işe yarar? Kimler kullanır?
The Graph blokzincirlerin performansları hakkında bilgi sahibi olmak isteyenlerin çeşitli taleplerde bulundukları bir platform aslında. Yaptığı blokzincirlerin yarattığı verileri, toplamak, arama yapılacak bir şekilde sınıflandırmak (endekslemek) ve ihtiyaç duyanların hizmetine sunmak. 

Piyasada analiz yapan pek çok kurum ve analist var. Ancak bütün bunların hepsi merkezi yapılar. Merkezi yapı oldukları için güvenilirlikleri tartışmalı. Hangi bilgi kaynağını kullanıyorlar, o aşağı yukarı biliniyor ancak bilgiyi tam olarak kullanıyorlar mı, o bellli değil. Ne sıklıkla bilgi alıyorlar ve analizlerini ne sıklıkla tekrar ediyorlar? 

DeFi dünyası 7/24 çalışan bir dünya. Bilgiye nerede ise gerçek zamanlı ihtiyaç duyuyorsunuz. Size bu tip analizler için hazır araçlar sunan siteler de mevcut. Ama tam istediğiniz gibi bir analiz aracı hazırlayabiliyor musunuz? Peki o site, sizin istediğiniz yerden o bilgileri mi alıyor?

Bulamadığınız durumda yapmanız gereken, eğer bu bilgiye ihtiyaç duyan bir DeFi ürünü iseniz, kendi iç ekiplerinizi kullanıp ihtiyaç duyduğunuz araçları sıfırdan yaratmak yani yazmak. İyi de, bir DeFi ürünü olarak zamana karşı yarışıyorsunuz. Rakipler her gün yeni bir özellik sunuyorlar. İnsan kaynağı deseniz zaten kısıtlı. Bu kısıtlı kaynağı kendi öz ürününüzü geliştirmek için mi kullanmak istersiniz, yoksa bu tip bir ikincil ihtiyaç için mi?

İşte Graph sayesinde yatırım yapmak istediğiniz herhangi bir blokzincire ait bilgileri istediğiniz formatta alıp istediğiniz şekilde analiz etmeye yarayan bir platform. Üstelik istediğiniz zaman ya da sıklıkta yaptırıyor, kullandığınız kadar para ödüyorsunuz.  Tabii ki en büyük avantajı bunu merkeziyetsiz yani aracılar olmadan daha güvenilir bir şekilde gerçekleştiriyorsunuz. 

### Bir örnek mi versek?



### Graph'in fonksiyonu ne burada?
Graph'ı kuran ekip, sistemi olabildiğince merkeziyetsiz yapmak için oldukça çaba sarfetmiş. Örneğin Chainlink sisteminden bahsederken, her ne kadar müşterileri merkeziyetsiz DeFi platformları olsa da, sistemin oldukça merkezi olduğundan bahsetmiştik. 

The Graph'de ise daha merkeziyetsiz bir sistem görüyoruz. Sisteme giriş ve çıkış izne tabi değil herseyde önce. İşleyiş de olabildiğince kendi kendine oluyor. Graph ekibi birkaç yerde işin içinde:

Ortaya çıkarılan endeks ya da analizlerin, ihtiyaç sahiplerine düzgün bir şekilde tanıtılması için Graph Explorer isimli bir dApp kurmuş ekip. Bu oldukça kritik. Zira küratörler tarafından en kaliteli endeksler ortaya çıkarılmalı ki, bunlar talep sahipleri tarafından görülebilsin, kullanılsın ve küratör ve endeksçilere para kazandırsın. Bu endeks ve analizler şimdilik merkezi bir yerde tutuluyor. Gelecekte bu hizmetin merkeziyetsiz bir şekilde sunulması için çalışmalar sürüyor. 

Bunun yanında başlangıçta endeksçilerin hatalı bilgi verdiği gibi konularda karar verici olan ekip olsa da bu daha sonra protokolün yönetimine bırakılacak. 


### Rakipleri var mı? Gelecek nasıl görünüyor?

The Graph şu ana kadar endeksleme ve arama/sorgulama alanındaki merkeziyetsiz en bilinen model. Rakipleri merkezi yapılar. DeFi alanında bilinen en ünlü merkezi servisler Dune Analytics, Glassnode ve Nansen.  Bunun yanında Google BigQuery gibi genel arama hizmetleri de mevcut. 

Ancak bütün merkezi servislerde yukarıda bahsettiğimiz güvenirlilik sıkıntısının yanında istediğin hizmeti tam olarak alamama sorunu var. Blokzincirler inanılmaz bilgi/veri üretiyorlar ve doğru anlamlı veriye ulaşmak çok kritik. Merkezi servisler çok daha oturmuş veriler ile çalışırken, bir yatırımcı yeni ortaya çıkan bir blokzincir ile ilgili bir analiz yapmak istediğinde merkezi servislerde aradığını bulamıyor. Bu anlamda The Graph tam onların istediği gibi bir bilgi akışı ve analiz sağlayabiliyor. 

Bakalım bu alanda da her alanda olduğu gibi, merkezi platformların hızlı ve kullanıcı dostu arayüzleri ile merkeziyetsiz platformların daha az kullanışlı ama eğilip bükülebilir ve tarafsız yapısı arasındaki bu tatlı rekabette kim ön plana çıkacak. Şu an görünen her iki hizmetin de farklı alıcıları olacağı ve pazarda kendilerine yer bulacakları şeklinde.. 

### Sonuç
The Graph protokolü, merkeziyetsiz blokzincir dünyasının yarattığı bol veriyi, tarafsız bir şekilde tarayıp, endeksleyip, kullanıcıların sorgulamasına sunan ve bu dünyanın ruhuna uygun olarak merkeziyetsizleşmeyi kendine hedef seçmiş bir DeFi ürünü.. Şu an için Ethereum bazlı olarak çalışan protokol bakalım Chainlink benzeri vazgeçilmez bir DeFi hizmet sağlayıcı olabilecek mi?


--
### Sistem nasıl çalışıyor?

Graph tam bir oracle sayılmaz. Zira oracle hizmetine servis sağlayan dış aracılar (oracle düğümleri) dış dünyadan aldıkları bilgiyi akıllı kontrata aktarıyorlar. 

The Graph'ta ise köprü biraz daha farklı işliyor. Blokzincir içinden alınan bilgi, anlamlı bir hale getirildikten sonra hem zincir içi hem de zincir dışı ihtiyaç sahiplerine dağıtılıyor. 

The Graph, şu aralar en mode olan Proof-of-Stake sistemini kullanıyor. Hemen bir parantez açalım: Yabancı olanlara hatırlatma: Bitcoin, Proof-of-Work denen güvenlik sistemini kullanıyor - hani şu en büyük eleştiri kaynağı olan "ama çok enerji harcıyor" sözünün müsebbibi olan madencilerin olduğu sistem. Ethereum da şu an aynı sistemi kullanmakla birlikte, önümüzdeki yıl içinde Proof-of-Stake mekanizmasına geçecekler. Bu sistemde sistemin güvenliğini sağlayanlar bunu kendi mal varlıklarını teminat göstererek garanti edecekler. Böylece eskiden kol gücü yani emek ile korunan sistem, artık zenginlik yani kapital ile korunmaya başlayacak. Ve parantezi kapatıp konumuza geri dönelim. 

The Graph sisteminde endeksçiler (indexers) ağın düğümlerini oluşturuyorlar.  Bu arkadaşlar blokzincirler hakkındaki bilgileri düzenli bir şekilde tutup, bu bilgiler ile ilgili arama yapıldığında hem endeksleme karşılığı ödül hem de arama yapma karşılığı da bir ücret almaya hak kazanıyorlar. 

Tabii önüne gelen endeksçi olamıyor. Bunun için bir miktar parayı (sistemin parası GRT) teminat göstermek gerekiyor. Ya paranız yoksa? Demokrasilerde ve blokzincirlerde çare tükenmez!. O zaman, yetkilendiriciler (delegators) imdadınıza yetişiyor. Bu kişiler, parası olan ancak endeksleme/arama gibi ağır işçilik yapmak istemeyen sermayedarlar. Paralarını işini iyi yapan endeksçilere veriyor, karşılığında yapılan iş karşılığı kazanılan ödül ya da ücretlerden bir kısmını alıyorlar. 

Bunun dışında, bir de Küratörler (Curators) var. Bunlar, akıllı sınıfı (!) temsil ediyorlar. Küratörlerin yaptığı, hangi bilgi kaynaklarında hangi analizlerin para yapacağını önceden kestirmek. Böyle bir 'cevher' bulduklarında, hemen analize para (yine sistemin parası olan GRT) kilitliyorlar. Eğer analiz tutarsa, getirinin bir kısmına hak kazanıyorlar. Burada, hızlı ve kaliteli analiz bulmak çok önemli, erken bulan kazanıyor. Zira öyle "analizi ben buldum kimseye kaptırmam" gibi bir münhasırlık yol. Bir analizin kaliteli ve potansiyel olduğunu gören herkes para yatırır, endeksçiler de daha ilgi gören analizler için iş yaparlar. İlk bulan ve para yatıran iyi getiriler elde ederken, daha sonradan katılanlar daha az gelir elde eder. 

Neden para konuyor peki? Sistem merkezi değil demiştik. Bu nedenle isteyen sisteme girip endeksçi, yetkilendirici ya da küratör olabiliyor. Peki ya bu kişiler kötü niyetli ise?  Özellikle endeks tutanlar, yanlış bilgi sağlamak ya da endekslemek söz konusu olursa koydukları paranın tümünü kaybedebiliyorlar. Hemen belirtelim teminatlarını uzun bir süreliğine koydukları için bilginin yanlış olduğu sonradan anlaşılsa bile cezayı yiyorlar. Küratör ve yetkilendiriciler bilgi sağlamadıkları için böyle bir ağır cezaya tabi değiller ama onlar da eğer yanlış ata oynar yani yanlış analiz ya da endeksçi seçerlerse, paralarını geri çekerken bir ücret ödüyorlar. 

Para konmasının ikinci bir nedeni de, önüne gelenin sisteme girip sistemi çöplük haline getirmesini önlemek için. Zira, böyle bir durumda kaliteli endeksleme yapanları bulmak zorlaşıyor ve genel sistem reputasyonu bozuluyor. 

Tabii bir de kullanıcılar var ki - bunlar genelde DeFi ürünleri oluyor. Örneğin DeFi dünyasının ağır topları Uniswap, Synthetix The Graph'in modellerini kullanıyorlar.  Nasıl belli bilgilerini depolamak için bulut üzerinde yer kiralıyorlar, benzer şekilde modellemeleri için The Graph'i tercih ediyorlar. Bu işi yapmak için ekip tutmak, server kiralamak yerine kullandıkça ödedikleri için onların da işine geliyor bu model açıkçası. Zira o ağır top [Uniswap'ın 2021 yılının Ocak ayında sadece 11 çalışanı olduğunu](https://twitter.com/haydenzadams/status/1346575665940860929) söylersek, neden böyle bir servise ihtiyaç duyacakları daha iyi anlaşılır. 

