---
layout: post
title:  "Sigorta için Blockchain"
date:   2018-10-26 10:03:34 +0300
categories: Genel
---


Geçtiğimiz yazılarda Blockchain bazlı dağıtık sistemlerin faydalı olabileceği alanlardan [sağlık](https://ademimerkezi.com/genel/2018/04/17/saglik-icin-blockchain.html), [sanat](https://ademimerkezi.com/genel/2018/04/06/sanat-icin-blockchain.html), [seyahat](https://ademimerkezi.com/genel/2018/07/06/seyahat-icin-blockchain.html) sektörleri ile [hayır işleri](https://ademimerkezi.com/genel/2018/03/29/Iyilik-icin-blockchain.html), [tahmin piyasaları](https://ademimerkezi.com/genel/2018/07/13/gelecegi-tahmin-icin-blockchain.html) ve [tedarik zincirlerine](https://ademimerkezi.com/genel/2018/08/17/tedarik-zinciri-icin-blockchain.html) bakmıştık.  Şimdi gelin finansal piyasalara daha yakın olan sigorta sektörüne bakalım. 

![water-975728_640.jpg](/assets/water-975728_640.jpg)




### Sigorta sektörü için Blockchain

Blockchain'in şu ana kadar en göz önünde olan faydası güvene olan ihtiyacı ortadan kaldırması (ve o ihtiyacı sağlayan kurumların etkisini azaltması) ve bürokrasiyi azaltarak para, zaman, emek tasarrufu sağlaması idi. Ama her derde deva olmadığını da [şu yazımızda](https://ademimerkezi.com/genel/2018/08/03/blockchain-her-derde-deva-mi.html) belirtmiştik. 

Bu anlamda güven ihtiyacı sağlayan kurumların etkisinin azalacağından bahsettik. Finansal kurumların ana görevinin güven sağlamak olduğunu varsayarsak, bu sektördekilerin [geceleri uykularının kaçması normal](https://ademimerkezi.com/genel/2018/03/01/Geceleri-uykunuzu-ne-kaciriyor.html).

Sigorta sektörü için durum bir miktar farklı. Uzun vadede dağıtık sistemler sektöre zarar verir mi tartışılır ancak sigorta sektörünün ihtiyacı olan güveni sağlaması açısından bu sistemlerin kısa vadede yarar sağlayacağı çok aşikar görünüyor. Nedir bu faydalar? Bir kaç örnek üzerinden bakalım dilerseniz:

### Afet sigortası ve Akıllı Kontratlar

Sigortacılığın en büyük parçalarından biri Afet Sigortası. Hiçbirimiz istemeyiz ama doğal afetler maalesef hayatın bir parçası, üstelik küresel ısınma ve benzeri çevresel bozulmalardan dolayı sıklığı giderek artan hayatın gerçekleri... Bireysel kaza ve benzeri durumların aksine bu tip doğal afetler daha az yaşanıyor (ve bazen uzun süre yaşanmıyor) ama yıkım genele yayıldığı için oluşan zarar sigorta şirketleri için karşılanamaz olabiliyor. Bu nedenle, sigorta şirketlerinin bu tip riskleri "satma"sı sektörün en temel uygulamalarından biri. 

Afet sonrası hasarın tespiti, bir kısmının riski satın almış partilere devredilmesi, oldukça uzun ve zahmetli bir süreç. Hele irili ufaklı pek çok olayın (sel baskını vb.) getirdiği operasyonel yükler çok daha yüksek. Peki bu süreç otomatikleştirilemez mi? Daha önceki bir yazımızda bahsettiğimiz [Akıllı Kontratlar](https://ademimerkezi.com/genel/2018/06/29/bu-kontratlar-cok-akilli-ethereum-ve-akilli-kontratlar.html) ile aslında mümkün. 

Akıllı Kontratlar aslında adı ile çelişir şekilde, akıllı olmaktan ziyade oldukça basit şekilde işleyen ve belli olaylar gerçekleştiğinde (tetikçi olay diyelim) otomatik olarak aktive olan işlemler idi. Şimdi bunu aşağıdaki senaryoda Blockchain sistemi içine uyarlamaya çalışalım: 

* Sigorta şirketi Akıllı Kontrat oluşturur: Bu kontratın içinde olma ihtimali olan olay, bu olayın hakikaten gerçekleştiğini teyit edecek bir üçüncü parti (buna oracle - kahin deniyor), gerçekleştiği durumda zarar gören parti için verilecek rakam başta olmak üzere tüm gerekli bilgiler girilir. 

* Akıllı Kontrat, Blockchain üzerine işlenir. Neden? Blockchain'in temel faydalarından yararlanmak için. Bağımsız olması, geçmişe yönelik olarak değiştirilememesi...

* Sigorta şirketi bu Akıllı Kontratları ilgilenen yatırımcılara satar. Kim bunlar? Böyle bir afetin olmayacağını düşünen ve buna göre pozisyon alan kurumsal/bireysel yatırımcılar. 

* Afetin gerçekleşmesi durumunda, Blockchain üzerindeki Akıllı Kontrat, gerçekleştiği konusunda önceden belirlenmiş kahinlerden (oracle) teyit alır, koşulları işletir ve ilgili partilere zararın miktarını gönderir. 

* Afetin gerçekleşmemesi durumunda, Akıllı Kontrat, satın alan yatırımcısına yaptığı yatırım ve faizini öder. 

Tabii ki yukarıdaki senaryoda Akıllı Kontrat içindeki koşulların oluşturulması aşamasında ciddi bir çaba sarfedilmesi gerekecek - dışarıdan çok kolay görünmesine rağmen ayrıntılar çok fazla. Yine de çok özel durumlar dışında pek çok alanda bu kullanılabilir. 

### Rutin olaylar ve tazmin talepleri

Keza şunu düşünün: Sigorta şirketleri, yukarıdaki afet, kaza, yağmur vb. pek çok durumda hakikaten olayın gerçekleştiğini öğrenmek için bile ciddi miktarda para harcıyorlar (eksper tutma, olay yerine gönderme gibi). Bunun yerine, bu tip olayları o bölgedeki insanlar otomatik olarak bildirse (ve bunun karşılığı bir miktar kazanç elde etseler)? Sigorta şirketleri de ortak bir Blockchain veritabanından bu bilgileri alsa... Sektör oyuncuları için güzel bir tasarruf olabilir. 

### Peki Blockchain gerekli mi bunun için?

Hep sorduğumuz şu soruyu da sormamazlık etmeyelim: Peki bütün bunları yapmak için ortak bir veri tabanı kullanılamaz mı? İlla ki Blockchain'e ihtiyaç var mı bunun için? Tabii ki bunu sigorta şirketlerinin ortak oluşturduğu bir veri tabanı ile yapabilirsiniz.   Sigorta sektörünün büyümesinin önündeki engellerden birinin müşterilerin şirketlere olan güven erozyonu olduğu düşülürse, Blockchain bazlı tarafsız ve şeffaf bir sistemin sigortalanan gözündeki değerinin daha yüksek olacağı kesin. Ayrıca birbirinden farklı sistemlerin birbiri ile çalışması ciddi bir yatırım - bunun yerine ortak yeni bir Blockchain'e entegre olmak nispeten daha kolay. Birlikte çalışmak için gerekli olan güven konusunu Blockchain üzerindeki sistemlere bıraktığınızda sektör oyuncuları olarak çok daha rahat hareket edebilir, çok daha paylaşımcı olabilirsiniz. 

Nitekim, küresel anlamda büyük oyuncuların yarısı önümüzdeki iki yıl içinde Blockchain bazlı sistemler ile entegre olmayı bekliyor ve %84'ü de Akıllı Kontrat ve Blockchain bazlı dağıtık sistemlerin sektörün yeni ortaklar ile iş yapma şekillerini değiştireceğini [belirtiyor](https://insuranceblog.accenture.com/ultimate-guide-to-blockchain-in-insurance).

### Sonuç

İçinde bulunduğumuz ekonomik koşullarda, yukarıda anlattıklarım hayal gibi gelebilir. Daha önceki yazılarımızda da belirttiğimiz gibi bu bir vizyon ve dünyanın dört bir yanında, mevcut sigorta oyuncuları, girişimciler, yazılımcılar bu vizyona ulaşabilmek için çalışıyorlar. Vizyonu gerçekleştirmek vakit alacak orası kesin, ama düşündüğünüzden erken olabilir, hazırlıklı olmak ve sigortanızı şimdiden yaptırmakta fayda var. 
