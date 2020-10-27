---
layout: post
title:  "DeFi'de sigortacılığa devam..."
date:   2020-10-27 18:47:56 +0300
categories: Genel
tags: Yazılar DeFi
---

Geçtiğimiz yazıda merkeziyetsiz bir sigorta sistemi olan [Nexus Mutual'ın hikayesine bakmıştık](/genel/2020/10/20/definin-sigortasi-nexus-mutual.html). Bu yazımızda ise işin biraz daha tekniğine girerek [Nexus Mutual](https://nexusmutual.io/) sistemi nasıl çalışır, sistemin tokeni NXM nasıl fiyatlanır ona bakacağız. Arkasından NXM tokenları ile yapılabilecek staking benzeri farklı işlemlerden de bahsedeceğiz. 

### Nasıl çalışıyor Nexus sistemi?
Nexus Mutual kendisine sigorta demiyor - bunun en önemli nedeni kanuni olarak sigorta mevzuatına takılmamak. Bunun yerine Akıllı Kontratlarda çıkabilecek açıklara karşı "koruma" sağladıklarını belirtiyorlar. 

#### Havuz problemleri yine karşımızda... 
Sistemin çalışması aslında bir havuz şeklinde. Evet, [daha önceki Uniswap yazımızda bahsettiğimiz havuz sistemi](/genel/2020/09/15/nedir-bu-uniswap.html) burada da geçerli. 

Hatırlarsak, Uniswap'da iki bölmeli iki paradan oluşan havuzlar vardı. Alım satım yapanlar havuzdaki bir paradan almak istedikleri yerine orada bulunan diğer parayı bırakıyorlardı. 

#### Nexus'un havuzu diğerlerinden farklı... 
Nexus Mutual havuzunun çalışma prensipleri ise bir parça farklı. Gelin hızlıca bir göz atalım:

Nexus Mutual'in havuzu özünde sistem tarafından alınan risklere karşılık ödenebilecek kapital rakamının toplamından oluşuyor. Sigorta satın alanların ödedikleri tüm ücretler havuzun içine girişleri oluşturuyor. Yapılan hasar ödemeleri ise temel çıkışları. 

Havuzun sahibi tüm üyeler. Nasıl sahip oluyorlar bu havuza? Aynı hisse senedinde olduğu gibi havuzun sahipliğini gösteren sistemin parası NXM ile. Dolayısı ile NXM sahibi olmak hem havuzun riskini hem de getirisini paylaşmak anlamına geliyor. 

Peki başlangıçta sistem nasıl başladı? Havuz boş muydu? Hayır, bu alanda tecrübeli, riski bilen kişi ve kurumlar başlangıçta Ethereum sisteminin parası olan ETH koyup karşılığında NXM alarak havuza bir kapital sağladılar. 

Havuzdaki para ETH olarak tutuluyor. Dolayısıyla Nexus Mutual dünyasının temeli ETH'e dayanıyor - en azından şimdilik. Bu da anlaşılır, zira koruma verdikleri DeFi platformlarının çoğunluğu da Ethereum üzerinde işlem yaptığı için risk ETH bazlı, o nedenle bu riske karşı fonları da ETH olarak değerlendirmek mantıklı. 

### Kim niye NXM alsın? 
Birkaç neden var. 

Öncelikle sigorta yaptırmak, pardon "Akıllı Kontratlar'a karşı koruma satın almak" istiyorsanız bunu NXM ile yapıyorsunuz.  Yaptırmak istediğiniz sigorta miktarı ve süresine bağlı olarak aldığınız korumanın yani poliçenin ücretini NXM olarak veriyorsunuz (bir başka deyişle NXM yakıyorsunuz). NXM'i de havuzdan ETH ya da [stabil bir kripto para olan DAI](/genel/2018/07/20/Orasi-cok-dalgali-sakin-sulara-gel-sabitparalar.html) karşılığı alacaksınız. 

İkincisi ise yatırım olarak almak. Sonuç olarak NXM aldığınızda havuzun bir parçasına sahip oluyorsunuz ve ödenen primlerin risklerden fazla olduğunu ve sistemin ileride büyüyeceğini tahmin ediyorsunuz. NXM değerini neler etkiliyor, hemen bir sonraki bölümde değerlendireceğiz. 

Bunun dışında NXM sahibi olarak tazminat isteyenlerin taleplerini değerlendirmek, az sonra bahsedeceğimiz çeşitli ürünlere direkt olarak yatırım yapmak, ya da NXM yönetim sisteminde söz sahibi olmak (örneğin yeni çıkarılacak ürünleri belirlemek için yapılan oylamalara katılmak) gibi Nexus Mutual'a özel belli para kazandırıcı aktivitelerde yer almak da mümkün. 

Bu arada bir konuyu tekrarlamakta fayda var: Her ne kadar merkeziyetsiz bir sistem olsa da Nexus Mutual'ın belli alanlarda kısıtları olduğunu belirtmiştik. Örneğin, NXM yalnızca Nexus Mutual'un kendi kurduğu platformda işlem görüyor. NXM satın almak isteyenler Nexus Mutual sistemine üye olmak zorundalar. Üye olmak için de müşterini tanı (KYC - Know your customer) işleminden geçmek gerekiyor.  KYC işlemlerini yapan ise İngiltere merkezli ve lisanslı bir şirket. 

### NXM fiyatı neye göre belirleniyor?

İşte Nexus Mutual'ın diğer merkeziyetsiz sistemlerden bir farkı daha. Nexus'un tokeni NXM'in değeri serbest piyasadaki arz ve talebe göre belirlenmiyor, zira NXM kripto para borsalarında işlem gören bir token değil. Bunun yerine NXM'in fiyatı bir algoritma ile hesaplanıyor. Nasıl bir hesaplama bu?

Hatırlarsanız, [Uniswap kendi içinde basit bir algoritma kullanarak al-sat yapmak isteyenlere bir fiyat veriyordu](/genel/2020/09/15/nedir-bu-uniswap.html). Bunu yaparken algoritmanın temel hedefi, ne olursa olsun işlem yapmak isteyenlere bir fiyat vermek idi. **Nexus Mutual algoritması da benzer şekilde işlem yapmak isteyenlere otomatik bir fiyat veriyor. Ama bunu yaparken hem arz ve talebi, hem de Nexus Mutual havuzunun finansal sağlığını korumaya çalışıyor**.

Nexus'un havuzunun temel amacı olası hasarlara karşı ödeme yapabilmek - bu sistemin olmazsa olması. **Bu nedenle havuzun içinde talepleri belirli oranda karşılayabilecek kadar kapital bulunması birincil hedef**. Bu kapital rakamı [Avrupa Birliği'nin yeterlilik standartlarına](https://www.eiopa.europa.eu/browse/solvency-ii/solvency-ii-background_en#Arisk-basedregulatoryframework) göre belirleniyor. Eğer havuzun içinde o belirlenen minimum oran kadar para yoksa öncelikle hiç kimse NXM satıp ETH alamıyor (bu oranın adı MCR - minimum capital requirement, minimum karşılık olarak düşünülebilirsiniz)[^3]. 

Algoritmanın ikinci amacı ise, gelişen arz ve talebe göre NXM fiyatını ayarlayarak sistemi sağlıklı tutmak. Bunu da otomatik bir formül ile yapıyor[^4]. Temel olarak şu şekilde çalışıyor: 

Eğer havuzda toplanan para minimum rakamın %30'undan fazlasına ulaşırsa, formül NXM fiyatını hızlı bir şekilde yükseltmeye başlıyor. Bunun nedeni fiyat yükseldiğinde, yatırımcıların ellerinde tuttukları NXM'i satıp havuzdan ETH çekmesini sağlamak. Neden böyle yapıyor? Çünkü havuzda değerlendirilmeden duran para, verimsizlik göstergesi. 

Bu arada, Nexus Mutual yönetiminin elde fazla kapital olması durumunda alacağı bir aksiyon daha var. O da yeni sigorta ürünleri çıkarmak. Bu sayede sistemi büyütebilirler. Yeni ürünler çıkması bu ürünler için de karşılık ayrılmasını gerektireceği için minimum karşılık oranını yani MCR'ı yükseltecek. 

Yine aynı şekilde eğer havuzdaki para minimum rakama doğru yaklaşmaya başlarsa formüle göre NXM fiyatı hızlı bir şekilde düşmeye başlıyor. Mantık aynı: Eğer NXM'in fiyatı ucuzlar ise, o zaman yatırımcılar çok daha ucuza havuzdan pay sahibi olmak hakkını kaçırmak istemeyecekler ve havuza ETH koyup NXM satın alacaklar. Böylece havuzdaki kapital yani ETH miktarı artacak. 

Özetle algoritma dediğimiz bu basit formül sayesinde hedeflenen, NXM fiyatı ile oynayarak, havuzdaki kapital miktarının belli bir bant içinde oynamasını sağlamak. Bu bandın altı minimum karşılık oranı olan MCR, üstü ise MCR'nin %30 fazlası. 

### Nasıl sigorta yapıyor kullanıcılar?
Üye olduktan sonra aslında çok da karmaşık değil. Kullanıcı farklı ürünlerden hangisine karşı kendisini korumak istiyor ise onu seçiyor, kaç gün için ve ne kadarlık bir miktar için korunma istediğini belirliyor. Sistem kendisine bir oran veriyor. Burada kullanıcı ödemeyi dilerse NXM dilerse de ETH ile yapabiliyor. 

#### Peki sigorta oranını kim nasıl belirliyor?
Bu sigorta oranının aslında Nexus Mutual yatırımcıları belirliyor. Bunu da staking dediğimiz rehin verme işlemi ile yapıyorlar. 

Staking daha fazla risk karşılığı daha da fazla getiri almak isteyenler için kurulmuş bir sistem. Normalde Nexus Mutual'a yatırımcı olmak istediğinizde, havuzdan NXM satın alıyor ve tüm sistemin risk ve getirisine ortak oluyorsunuz. Ancak staking yaptığınızda bu riski ürün bazında ayrıştırmak da mümkün oluyor. 

| ![semsiyeler](/assets/umbrella-3289996_640.jpg)|
|:--:| 
| *Image by [Sarah Lötscher](https://pixabay.com/users/sarah_loetscher-4248505/) from [Pixabay](https://pixabay.com/))*|

NXM satın alan dolayısıyla genel sisteme yatırım yapmış bir yatırımcı sonrasında dilerse bu NXM'i belli bir spesifik ürüne koyarak riskini daha da artırabiliyor. Böyle yaparak bu spesifik ürünü satın almış olanların ödedikleri primlerden bir kısmını havuzdan önce kazanma hakkına sahip oluyor. Risk tarafında ise üründe bir sorun çıkıp da zarar tazminat ödenmesi halinde koymuş olduğu NXM'i toptan kaybetme ihtimali var. Bu nedenle, staking yapmanın ekstra bir riskli bir yatırım olduğu unutulmamalı. 

Aslına bakarsanız, staking Akıllı Kontratların risklerini anlayabilmek için güzel bir endikatör aynı zamanda. Risk tutarı aynı görünen iki Akıllı Kontrat'tan birine diğerinin iki katı kadar staking yapılmışsa, bu birinci kontratın genel olarak çok daha az riskli görüldüğü anlamına gelebilir. 

#### Bir sorun olduğunda ödeme yapılacağına kim karar veriyor?
Her ne kadar Akıllı Kontratlar var desek de, ödemeler henüz otomatik yapılacak seviyeye gelmiş değil. Bunu DeFi'nin emekleme aşamasında olmasına bağlayabilirsiniz - belki önümüzdeki dönemde orada da olabildiğince otomatize bir sistem olabilir. Bir sistem sorunu olduğu ve ödeme yapılması gerektiğine Nexus Mutual'a üye olanlar oylama ile karar veriyorlar. Eğer Nexus Mutual üyeleri (ellerinde NXM token tutanlar) sistemsel bir sorun olduğu ve ödeme yapılması gerektiği konusunda bir karar verirlerse işte o zaman Akıllı Kontratlar devreye girip ürün satın almış olan kullanıcılara tazminatlarını ödüyorlar. 

#### Nasıl hasar talep ediliyor?
Herhangi bir hasar olayı olduğunda, ilgili üründen koruma almış olanlar, Nexus Mutual sitesine başvuruyorlar. Yapılan talep bir kısım NXM sahibi tarafından değerlendiriliyor. Burada ilginç bir nokta var: Talebi değerlendirenler ellerindeki NXM'leri sisteme kilitliyorlar. Kararların %70 çoğunluk ile verilmesi gerekiyor[^1]. Çoğunluk ile aynı yönde oy kullananlar ekstra NXM kazanıyor. Karşı oy kullananların ise NXM'leri bir süreliğine kilitli kalmaya devam ediyor ve incelemeye tabi tutuluyor. İnceleme sonucu kötü niyetli oldukları saptanırsa NXM'leri yakılıyor. Gördüğünüz gibi hasar talep sisteminin değerlendirilmesi hâlâ manuel şekilde oluyor denebilir - zira çoğunluğa karşı oy kullananları değerlendiren bir komite var beş üyeden oluşan - çok da merkeziyetsiz sayılmaz şu aşamada. 

#### Hiç hasar karşılama ödemesi yapmış mı Nexus Mutual?
Şimdiye kadar bir tek olayda ödeme yapılmış. 2020 Şubat ayında [bzX sistemindeki bir açıktan dolayı oluşan hasarda](https://bzx.network/blog/postmortem-ethdenver) Nexus Mutual üyeleri [iki adet koruma alan kullanıcının için toplam 35,000 ABD Doları'na yakın bir ödeme yapmışlar](https://medium.com/nexus-mutual/bzx-flash-loan-event-55753d19e52b). Şu ana kadar toplam 53 hasar talebi geldiğini ve sadece az önce bahsettiğimiz bZx hasarına ait üç talebin karşılandığını, 47 talebin reddedildiğini de hatırlatalım[^2]

### Sonuç
Birinci bölümünde genel olarak başladığımız bu yazıda ise daha teknik detaylarına girdiğimiz DeFi'da sigortacılık sistemi Nexus Mutual, şu ana kadar belli kısımları merkeziyetsizleşmiş gelecek vadeden bir proje. DeFi'nin büyümesi ve yeni ürünlerin ortaya çıkması ile birlikte büyümesi de yüksek bir ihtimal. Gelişimini yakından izleyeceğiz. 


---


- [^1] Yapılan oylamada verilen karar %70 çoğunluk ile alınmalı - aksi takdirde tüm sistem tarafından bir oylama daha yapılıyor.
- [^2] Üç adet talep henüz değerlendirme aşamasında
- [^3] (bu oranın adı MCR - minimum capital requirement oranı). 𝑇𝑃 = 𝐴 + (𝑀𝐶𝑅𝐸𝑇𝐻/𝐶)∙ 𝑀𝐶𝑅%4

---
Kaynaklar: 

- https://cryptobriefing.com/defi-review-what-is-nexus-mutual-introduction-nxm/
- https://cryptobriefing.com/nexus-mutual-just-ran-out-defi-coverage-heres-why/
- https://tokentuesdays.substack.com/p/nexus-mutual
- https://academy.ivanontech.com/blog/introduction-to-defi-insurance-and-nexus-mutual
- https://sci.smithandcrown.com/projects/nexus-mutual

---

---

*Not 1: Bu yazı ilk olarak 27 Ekim 2020'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/defide-sigortaciliga-devam/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

---
