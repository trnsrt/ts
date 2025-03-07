Bu yazımızda merkeziyetsiz yapay zeka projelerinin en eskilerinden olan Bittensor'u inceleyeceğiz. 

### Neden Bittensor'a bakıyoruz?
Bir önceki yazımızda bundan sonra Web3 ile yapay zekanın kesişimindeki projelere odaklanacağımızı belirtmiştik.  Bunlardan ilki, bu alanın en eski ve aynı zamanda piyasa değeri en büyük projelerinden olan [Bittensor](https://www.bittensor.ai/). 

Bittensor'u ilgi çekici yapan eski olması değil diğer bağımsız yapay zeka projelerine ev sahipliği yapması. Bu haliyle merkeziyetsiz yapay zeka alanının hem potansiyelini hem de zaaflarını içinde barındıran güzel bir örnek olması. Gelin önce ne iş yaptığından bahsederek konumuza başlayalım. 

### Nedir Bittensor?
Yapay zeka çok geniş ve farklı katmanları olan bir alan. Temel parçalarını (çok basite indirgeyerek); data yani verinin toplanması, işlenmesi, modellenmesi ve sonrasında aracılar tarafından son kullanıcıya sunulması olarak özetleyebiliriz. 

Bittensor, işte bu büyük alanın oldukça geniş bir kısmında aktif olan bir pazar yeri. Temel işlevi, veri modelleri üzerinde çalışan bağımsız girişimleri[^10], bu modelleri kullanacak uygulama ya da son kullanıcılar ile bir araya getirmek. 

Ne sağlıyor bu? Hatırlayacaksınız, Web3 dediğimiz dünya, Web 2.0'da yaşanan teknoloji devlerinin hegemonyasına alternatif olmak için [çıkmıştı](https://www.scalakitapci.com/sorularla-web3). Teknoloji dünyasında geçmişte yaşadığımız bu gelişmenin bir benzerini şimdi yapay zeka alanında da yaşıyoruz. Neredeyse sonsuz kapitale erişimi olan merkezi teknoloji devlerinin yapay zeka alanını parsellediğini görüyoruz[^2]. 

Bittensor, bu devlerin kontrolü altına girmek istemeyen bağımsız girişimler için 'çölde bir vaha' adeta. Girişimlere, ürün ve servislerine uygun müşteri bulmada yardımcı oluyor. Bunun yanında onlara diğer girişimler ile hem rekabet edebilecekleri hem de birlikte çalışabilecekleri bir ortak alan sunuyor. 

### Nasıl bir yapıya sahip?

Bittensor, ilk olarak 2021 yılında sadece 'yazı komutu üretme' (ingilizcesi 'text prompt') üzerine kurulu bir pazar yeri olarak hizmet vermeye başlamış. Sonrasında Ekim 2023'de büyük bir değişimden geçerek pazar yeri içinde farklı farklı 'özel alanların' kurulduğu bir ağ haline gelmiş.

Subnet adı verilen bu alanların sayısı başlangıçta 32 iken zamanla artarak [61'e çıkmış](https://www.bittensor.ai/subnets)[^4]. 

[Bittensor sistemi](https://tao.news/community-articles/bittingthembits/cosmic-odyssey-the-celestial-dance-of-decentralized-intelligence/)

Subnet'lerden kimileri gelişmiş yazı, görsel, video üretimine odaklanırken, kimileri de varlık fiyatlama ya da X-ray tanıma  ya da depolama gibi konularda uzmanlaşmış. Örneğin, şu aralar çok popüler olan Kaito AI tarafından geliştirilen 5 numaralı Subnet,  Web3 üzerindeki verileri daha akıllı bir şekilde arama ve analiz etmeyi sağlıyor.

[Subnet ekosistemi](https://cruciblelabs.com/report-state-of-bittensor-2024/)

Bittensor, sistemini bu alanların birbirleriyle rekabet etmesi üzerine kurmuş. Alanlar içinde kullanıcılar tarafından en çok ilgi görenler sistem tarafından ödüllendiriliyor, ilgi görmeyenlerin yerini ise yeni kurulan Subnet'ler alıyor. 

Gerek Subnet oluşturma, gerekse bu Subnet'lere iş üretme ya da bu hizmeti alma izne bağlı değil (yani 'permissionless')[^3]. Merkeziyetsiz bir yapıya sahip olan Bittensor'un aynı zamanda kendine ait Subtensor adında bir blokzinciri var[^5]. Yapılan işler ya da Subnet'lerin kendileri zincir dışı çalışsa da, değerlendirme ve ödül dağıtımları blokzincir üzerinde gerçekleşiyor.

İlk tohumları Jacob Steeves ve Ala Shaabana adlı iki yapay zeka uzmanı tarafından 2019 yılında atılan Bittensor, merkeziyetsizlik konusunda kendisine Bitcoin'i örnek alan ilginç bir girişim[^6]. Bunu sistemin parası olan TAO'da da görüyoruz. Gelin şimdi de onu inceleyelim:

### Bittensor sisteminin parası TAO
Bittensor ekosisteminin damalarında dolaşan kan, sistemin parası olan TAO. Bittensor kurucuları TAO'yu tasarlarken Bitcoin'den esinlenmişler:

Toplam TAO miktarı 21 milyon ile sınırlı. Az önce bahsettiğimiz Subnet'lere verilen ödüller aynı Bitcoin'in madencilere verdiklerine benziyor. Ödüller TAO sisteminin emisyonunu oluşturuyor ve her 12 saniyede bir 1 TAO olarak veriliyor (günde 7,200 TAO çıkıyor). Yine Bitcoin'de olduğu gibi bu miktar belirli aralıklarla yarıya iniyor. Örneğin herhangi bir aksilik olmazsa 19 Aralık 2025'de verilen ödül 0.5 TAO'ya [düşecek](https://taostats.io/tokenomics). 

Ödüllendirme yakın zamana kadar şu şekilde oluyordu: 

Her bir Subnet içinde madenci ('miner') denen hizmet sağlayıcılar bulunuyor. Örneğin, görsel üretime odaklanan Subnet içindeki madenciler kullanıcıların kendilerinden istediği görselleri üretiyorlar. 

Onaylayıcı (ingilizcesi 'validator') denen aktörler ise, yakın bir zamana kadar, madencilerin belirli bir süre içinde ürettiği çıktıları ne kadar tatmin edici olduklarına göre oyluyorlardu. Onaylayıcıların oylamaya katılmak için sisteme TAO rehin etmeleri gerekiyordu. Bittensor tarafından verilen ödül bütün bu rating'e göre Subnet'lere bölüştürülüyordu.

Bu yöntemin en sıkıntılı tarafı, en büyük 10 onaylayıcının toplam stake edilen tokenlerin %78'ine sahip olması. Böyle olunca bu onaylayıcıların istediği Subnet'ler yaşıyor, sevmedikleri ise ödüllerden mahrum kalarak ölüme terk ediliyordu. Bunun yanında gitgide artan Subnet sayısı nedeniyle onaylayıcıların hangi Subnet daha başarılı değerlendirmesi yapması da oldukça zorlaşıyordu. 

Şubat 2025'de uygulamaya konan yeni bir geliştirme ile ödül dağıtımının şekli değiştirildi. Dağıtım görevi, onaylayıcılardan alınarak piyasa mekanizmasına verildi.

Yeni plana göre her bir Subnet kendine özel bir token çıkarıyor[^8]. Onaylayıcılar eskiden Bittensor sistemine rehin ettikleri TAO'ları artık Subnet'e rehin ediyor, karşılığında Subnet'in tokenini alıyorlar. Daha fazla TAO'nun rehin edildiği Subnet'in tokeninin değeri artıyor. Sistem de token değeri artan Subnet'e daha fazla TAO token ödülü veriyor.

Bunun yanında TAO, Bittensor'un kendi blokzinciri üzerindeki işlemlerde kullanılacak bir para birimi işlevi de görüyor[^7]

### Bittensor'u gelecekte neler bekliyor?

Her şeyden önce merkeziyetsiz yapay zekanın büyümesinin önündeki tüm engellerin Bittensor için de geçerli olduğunu söylemeliyiz. 

Bittensor için en kritik konu, üzerinde verdiği hizmetlerin geniş kesimlerce kullanılıp kullanılmayacağı. Özellikle yapay zeka devleri yeni ürün ve hizmet yarışına girmişken Bittensor üzerinde yer alan girişimler onlarla nasıl yarışacak? Bırakın her haftayı her gün büyük oyunculardan birinin yeni bir özellikle ile yarışta öne çıktığı bir dünyada, bu hizmetler kendilerini yeterince farklılaştırabilecek mi?

Bir diğer konu ise Bittensor'un çok fazla alanı kucaklamaya çalışması. Nasıl merkeziyetsiz çözümler yapay zekanın her alanında olamayacaksa benzer bir durum Bittensor için de geçerli. Her ne kadar Subnet'ler için ödül paylaşımı yoluyla güçsüzün yok olacağı bir sistem kurulmuş olsa da bu uzun vadede ne kadar etkili hesaplamak zor. Belki de Bittensor'un daha niş (spesifik) alanlara (örneğin özel kişisel verilerin toplanması gibi) odaklanması sistemin başarı şansını daha çok artıracak.

Şu an için Bittensor'u ayakta tutan, sistem tarafından verilen TAO ödülleri. Nasıl Bitcoin için "madencilere verilen ödüller iyi hoş da, bunlar bitince ne olacak?" sorusu soruluyor, benzeri TAO için de geçerli. Halen günde 7,200 adet TAO ödül olarak veriliyor. Bu, bugünün fiyatları ile yılda 750 milyon ABD Doları bir ödül demek[^1]. Bu ödül 2026 yılında yarıya inecek. Uzun vadede Bittensor kullanımı artmalı ki TAO'ya talep olsun. Aksi halde bir 'ölüm sarmalı' riski var: Azalan ödüller mevcut girişimleri ürün geliştirmekten soğutur, tatmin olmayan kullanıcı platformdan uzaklaşır, kullanıcı ilgisinin düşmesinin yeni girişimlerin platforma katılma iştahını kırar gibi...

Bittensor için 2025 yılı oldukça kritik. Bunun birkaç nedeni var. 

Birincisi, Şubat ayında hayata geçen Subnet tokenlerinin TAO'ya olan etkisinin nasıl olacağını kestirmek henüz güç. Yeni sistem pazar dinamiklerini dikkate allıyor ama oldukça karışık. Token ödülü kazanabilmek için farklı senaryolarda ne tip manipülasyonlar olacağını deneyimlemek gerekiyor. 

Subnetlerin her biri farklı bir alanda uzmanlaşıyor. TAO sahiplerinin hangi Subnet'in Bittensor sistemine ne kadar katkı yapacağını nasıl değerlendirecekleri de bir başka soru işareti[^9]. Üstelik Bittensor merkeziyetsiz olsa da Subnet'lerin iç işleyişlerinin yeterince şeffaf olmadığı ile ilgili [ciddi eleştiriler de var](https://www.chainofthought.xyz/p/bittensor-flawed).

İkinci konu ise yukarıda belirttiiğimiz ve Aralık ayında gerçekleşecek olan yarılanma. Bu nedenle azalacak ödüllerin Bittensor üzerindeki girişimlerin heyecanını nasıl etkileceğini bilemiyoruz. 

### Sonuç

Özet olarak, Bittensor, gitgide merkezileşmeye başlayan yapay zeka dünyasında hayatta kalmaya çalışan bağımsız girişimleri bir araya getirmesi ve onlara ürünlerini sunacakları bir kanal yaratması açısından oldukça önemli bir proje. Merkeziyetsizlik konusunda yaptıklarıyla da örnek olabilecek bir deney. 

Bittensor önündeki engellerden dolayı belki de hedeflediği büyüklüklere ulaşamayacak. Yine de gerçekleştirdiği deneyler ile bu yolda ilerleyecek girişimlerin önünü açarak merkeziyetsiz yapay zeka alanına önemli katkılar verecek. Takipte kalacağız. 

---

[^1]: Yazı hazırlandığı sırada TAO fiyatı 285 ABD doları idi. 
[^2]: Üstelik bütün bu modeller kapalı yani içinde ne olduğunu ya da kullandıkları verinin nasıl işlendiğini görmek mümkün değil. En popüler ama kapalı bir model olan ChatGPT'yi çıkaran şirketin adının OpenAI olması da bir oksimoron. Neyse ki, eskinin Facebook yeni adıyla Meta'nın sahibi Mark Zuckerberg var da açık modellere erişim hâlâ söz konusu. Açık model demişken, onca eleştiriye rağmen Çin merkezli DeepSeek'in de sektörde deprem yarattığını belirtmek gerek. 
[^3]: İsteyen herkes Subnet kurabiliyor. Subnet'i kuran kişiler (ingilizcesi 'owner') Subnet'in teşvik mekanizmasını da belirliyorlar. Örneğin, verilen hizmeti daha hızlı, daha doğru verene daha fazla ödül dağıtılması gibi.
[^4]: Toplam sayı 64 olsa da üç tane Subnet şu an bağlantısı verilen listede aktif görünmüyor. Bu arada Subnet sayısının 1024'e çıkması gibi bir hedef de [bulunmakta](https://cryptolived.com/news/full-analysis-of-bittensor-s-34-subnets-and-development-trends-an-in-depth-perspective/). 
[^5]: Başlangıçta Polkadot ağı içinde bir zincir ('parachain') olarak başlayan Bittensor sonrasında kendine ait bir zincir kuruyor. 
[^6]: Tüm sistemin yönetim modeli iki kamaralı şekilde [gerçekleşiyor](https://docs.bittensor.com/governance). Yapılacak değişiklikler sistemin lokomotifi olan Opentensor Foundation tarafından öneri olarak hazırlanıyor ve elinde yüksek miktarda TAO tutan bir grup tarafından oluşturulmuş Senato tarafından onaylanırsa yürürlüğe giriyor.
[^7]: Geçtiğimiz yıl yapılan bir güncelleme ile Bittensor'un blokzincirine EVM (Ethereum işlemcisi) uyumu geldi. Bu sayede, Ethereum üzerine uygulama üreten programcılar bu uygulamaları Bittensor zinciri üzerinde de kurabilecekler. Bu sayede, Bittensor üzerinde örneğin merkeziyetsiz finans uygulamaları da gelişecek. TAO bu uygulamaların temel parası işlevi görecek. 
[^8]: Bu token serbest piyasada alınıp satılamıyor. 
[^9]: Bittensor bu değerlendirmeyi için Yuma Consensus adlı bir uzlaşma mekanizması kullanıyor ama bu mekanizma ne kadar şeffaf ya da anlaşılır, o biraz tartışmalı.
[^10]: Bu girişimler verinin depolanması, işlenmesi, model yaratılması gibi yapay zekanın geniş bir alanına dağılıyorlar. Detaylar yazının içinde. 
