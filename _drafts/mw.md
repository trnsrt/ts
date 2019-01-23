# YAZI I


"Zamanında buralar hep dutluktu" diyenleri bilirsiniz. Benzer şekilde çoğumuz bundan on yıl önce ortaya çıkan Bitcoin'in ilk yıllarını maalesef kaçırdık. Peki bir sonraki Bitcoin'in çıkışının şu aralar, daha doğrusu 15 Ocak'ta gerçekleştiğini söylesek size? (İddialı bir söylem ve hiçbirimiz kesin olarak bilemeyiz bunu tabii ki). Bugünlerde kripto dünyasındaki yeni 'hip' konudan bahsedeceğiz bu yazıda. Nedir bu yeni dalga? MimbleWimble!.  Hadi bakalım, anlamamız gereken yeni bir terim daha. (Merak etmeyin olabildiğince yalın anlatmaya çalışacağız):

Teknik olduğu için bir parça karışık ama basitleştirmek gelin üç parçaya ayıralım anlatacağımızı: 
* Bu yazıda başlangıç seviyesinde işin teknik olmayan kısmına, felsefi ve ekonomik boyutuna MimbleWimble üzerinden bakacağız. 
* [İkinci yazımızda] MimbleWimble üzerine kurulan en heyecanlı uygulama olan Grin parasına değineceğiz.
* [Üçüncü yazıda] ise, işin teknik kısmına yani felsefi ve ekonomik olarak diğer iki yazıda bahsedilenler konuların teknolojik olarak 'nasıl' gerçekleştirildiğine göz atacağız. 

### Nereden çıktı bu MimbleWimble?

MibleWimble 2016 Ağustos ayında KriptoParalar üzerine uğraşan bir grup yazılımcının kendi aralarında yazıştıkları chat ortamına birden bire Tom Elvis Jedusor rumuzlu biri tarafından bırakılan bir tanıtım yazısı (White Paper) ile ortaya çıktı. 

&nbsp;

| ![mimblewimble__400.png](/assets/mimblewimble__400.png) | 
|:--:| 
| *MimbleWimble White Paper - Kaynak: [Github](https://github.com/mimblewimble/docs/wiki/MimbleWimble-Origin)* |

&nbsp;

Tom Elvis Jedusor, o yazıyı bıraktıktan sonra kayıplara karıştı. Chat ortamındaki diğer yazılımcılar White Paper'ı incelediler,  bahsedilenlerin güvenirliğini, kripto olarak sağlamlığını test ettiler ve gerçekten yeni bir 'olay' ile karşılaştıklarını anladılar. 2016 yılının sonuna doğru Ignotus Peverell rumuzlu bir başka kullanıcı projenin liderliğini ele aldı ve o günden sonra gittikçe büyüyen bir yazılımcı ordusu etrafında MimbleWimble büyümeye ve gelişmeye başladı. En son 2019 yılının 15 Ocak tarihinde artık perdelerini dünyaya açar hale geldi MimbleWimble'in ilk uygulaması olan Grin.

### Ne garip isimler bunlar?
Gerçekten değil mi? Yukarıdaki paragrafta ismi geçen şahısların hiçbiri gerçek değil. Ama hepsinin bir ortak özelliği var. O da Harry Potter! Gelin kim kimdir bakalım:

- *MimbleWimble*: Yeni teknolojinin altyapısı olan protokolün adı. Harry Potter'ın [Deathly Hallows](https://en.0wikipedia.org/wiki/Harry_Potter_and_the_Deathly_Hallows) serisinde geçen bir büyü.  Amacı bir kişinin dilini bağlayarak büyü yapması için gerekli sözleri anlaşılır şekilde söylemesini önlemek. 

&nbsp;

| ![Tongue_Tying_Curse.png](/assets/Tongue_Tying_Curse.png) | 
|:--:| 
| *Harry Potter'daki 'Dil Bağlama Büyüsü'nün el işareti - [Kaynak](https://harrypotter.fandom.com/wiki/Tongue-Tying_Curse?file=Tongue-tying-curse.png)* |

&nbsp;

- *Tommy Elvis Jedusor*: MimbleWimble'in kurucusu. Harry Potter'daki kötü karakter Voldemort'un Fransızca karşılığı. 

&nbsp;

| ![Lordvoldemort-wikipedia.jpg](/assets/Lordvoldemort-wikipedia.jpg) | 
|:--:| 
| *Lordvoldemort - Kaynak: Wikipedia* |

&nbsp;

- *Grin*: MimbleWimble üzerine kurulu en tanınmış uygulama (detaylar bir sonraki [yazıda]). Yine Harry Potter öykülerinden birindeki Gringott's büyücülük bankasının adı.

![grin-400.png](/assets/grin-400.png)

- *Ignotus Peverell*: Grin projesinin lideri. Harry Potter'daki görünmezlik pelerinini üreten büyücü.

![ingotuspeverelaminoappscom-400.jpg](/assets/ingotuspeverelaminoappscom-400.jpg)

- *Luna Lovegood, Seamus Finnigan, Percy Weasley*: Grin projesindeki diğer kullanıcı isimleri. Hepsi Harry Potter ailesinden

![three_harry_potter_characters-400-2.jpg](/assets/three_harry_potter_characters-400-2.jpg)


### Nedir özünde MimbleWimble?
MimbleWimble özünde Bitcoin'in yaşadığı iki ana sıkıntıyı aşmak için yaratıldı: Gizlilik (mahremiyet) ve hantallık. 

#### Gizli

Daha önceki yazılarımızda bahsetmiştik: Bitcoin aslında mahrem bir sistem değil, sözde gizli demek daha doğru. Bitcoin ile yapılan bir işlemde gizli olan kısım sadece kullanıcı adları yerine adresler kullanılması. Ama gizli olmayan kısımları da alabildiğine şeffaf. Örneğin bir işlemde gönderilen para miktarı. 2009 yılında yapılmış bir işlemde bile ne kadar para transferi yapıldığını görebiliyorsunuz.

Ancak kullanıcı adlarının gizli olması aslında çok da mahremiyet yaratmıyor. Adreslerin yaptığı işlemler teknik olarak takip edilebiliyor, dolayısı ile kanunsuz biri ile bir alışveriş yapmanız durumunda hesabınızın mimlenme ihtimali var. Bunu sadece kanunsuz bir işlem olarak düşünmeyin. Baskıcı rejimlerde yaşayanların adreslerinin rejimler tarafından belirlenmesi ve o kişilerin rejim tarafından baskı altına alınması da olası. 

İşte Bitcoin üzerindeki bu sıkıntılar, bireylerin özgürlüğünü kendine şiar edinmiş yazılımcı kesiminin (bunlara cypherpunk da deniyor) tam mahremiyet sağlayacak bir protokol arayışına girmesine neden oldu. Bu şekilde ortaya çıkmış Monero, Dash, Zcash benzeri pekçok KriptoPara da var (bu paralara şu [yazımızda](https://ademimerkezi.com/genel/2018/06/07/token-dunyasina-devam-diger-kriptopalar-litecoin-monero-dash-zcash.html) bahsetmiştik). 

MimbleWimble, kuruluş amacı itibariyle tam bir gizlilik sağlamayı amaçlayan bir protokol. MimbleWimble protokolü ile yapılan işlemlerde işleme taraf olan alıcı ve satıcı ne de işlem miktarı belli. "Öyle olunca hile vs olmuyor mu?" diye soracak olursanız sizi işin teknik kısmını anlattığımız [yazımıza] bekleriz. 

#### Basit

Bunun dışında MimbleWimble'in diğer temel özelliği ise basit ve hafif bir program olması. Teknik olmayanları çok da ilgilendiren bir konu değil aslında ancak Bitcoin'de 2009 yılından bugüne yapılmış bütün işlemleri görebiliyorsunuz demiştik. Bu işlemlerin hepsi Bitcoin sistemindeki tüm makineler tarafından tutuluyor. Bu da her bir makine için GB'larca bilgi demek. Bu da sistemin hantallaşmasına sebep oluyor. MimbleWimble üzerine kurulan uygulamalar burada da güvenlikten ödün vermeden basit bir sistem kurmayı hedefliyorlar (detaylar teknik [yazımızda]). 


### Ne gibi uygulamaları var?
Yukarıda bahsederken iki uygulaması olduğundan bahsetmiştik. Bu iki uygulama Beam ve Grin. 

MimbleWimble başka diğer pek çok proje gibi açık kaynak bir yazılım. Açık kaynak yazılımların en önemli özelliği isteyenin istediği noktada projeyi istediği şekilde geliştirebilmesi. Burada da iki farklı grup projeyi birbirinden çok farklı yerlere götürmüş durumda. 

#### Beam

![beam-400.png](/assets/beam-400.png)

MimbleWimble üzerine çıkan iki projeden biri olan [Beam](https://www.beam.mw/), İsrailli bir girişimci olan [Alexander Zaidelson](https://twitter.com/azaidelson)'un CEO'luk yaptığı bir oluşum. 2018 sonbaharında 400 Bin ABD Doları yatırım alan proje, derli toplu bir şekilde MimbleWimble üzerine Beam adlı KriptoPara'yı kurmak için uğraşıyor. Dertli toplu derken, bir ekibe sahip olması, kendilerine çizdikleri bir yol planına sahip olması, yatırım alması, Beam parasını açtıklarında kurucular için kendilerine bir para ayırmaları gibi özellikler. Zcash benzeri ICO yapan bir KriptoPara'nın geçtiği tüm süreçlerin benzerini yapmaya çalışıyorlar. 


#### Grin
MimbleWimble'in belki de en ilginç uygulaması [Grin](https://grin-tech.org/). Yazı çok uzadı. Grin'i anlattığımız yazımızı [buradan] okuyabilirsiniz. 


### Serinin devamı.. 

Yazımızın devamında Grin'e bakıyoruz - [buradan] ulaşabilirsiniz..

# YAZI II
Bir önceki [yazımızda] en son ortaya çıkan 'hip' teknolojilerden MimbleWimble'a göz atmıştık. MibleWimble Bitcoin benzeri bir Blockchain. Asıl ilginç olan üzerine kurulu uygulamalar. aynı [yazıda] kısaca bu uygulamalardan Beam'e bakmıştık. Asıl ilginç uygulama [Grin](https://grin-tech.org/) ise bu yazımızda.


#### Grin
![grin-400.png](/assets/grin-400.png)

MimbleWimble'in çıktığı ikinci proje olan Grin, çıkış olarak Bitcoin' çok benziyor.  

Örneğin, lideri olan Ignotus Peverell'in kim olduğunu kesinlikle bilinmiyor. Ignotus Peverell geçtiğimiz yıl yapılan Grin konferansına text-to-speech teknolojisi ile katıldı. Katılımcıların sorularını yazdığı metni seslendiren bir yazılım aracılığı ile cevaplandırdı. 

&nbsp;

<iframe width="560" height="315" src="https://www.youtube.com/embed/k6tCnw6shgQ?start=107" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

&nbsp;

Bunun yanında Grin girişim sermayesi benzeri herhangi bir yatırım almadı, bundan sonra da sadece crowdfunding (kitlesel fonlama) ile yoluna devam etmeyi planlıyor. Bunu özellikle önemsiyorlar zira yatırım aldıklarında aslında gerçekten odaklanmaları gereken gizlilik ve kullanılabilirlik yerine yatırımcıya vaad ettiklerini gerçekleştirmek adına değer artırıcı konulara zaman ayırmak zorunda kalmaktan korkuyorlar. Zaten ne bir ofisleri var ne de bir organizasyonları, aynı Bitcoin'in ilk günlerindeki gibiler. 

Grin yaratıcıları, Bitcoin'in para saklama aracı olarak piyasanın ağır ağabeyi olarak hakimiyetini sürdüreceğini, kendi paraları olan Grin'in ise para ödeme aracı olarak kullanıcılara pratik ve tam gizlilik sağlayan bir mekanizma kuracağı düşünüyorlar. Bunu gerçekleştirebilmek için de Bitcoin gibi deflasyona yol açan (giderek azalan) bir para yaratım politikası yerine, enflasyonist (sabit olarak aynı hızda artan) bir [para yaratım politikası](https://www.tokendaily.co/blog/on-grin-mimblewimble-and-monetary-policy) sürdüreceklerini açıklıyorlar. 

Bu para politikası aslında ilginç bir detay: Sabit şekilde para arzı arttığında, ikinci yıl ilk yıl kadar para yaratılacak.  Üçüncü yıl o ana kadar yaratılmış toplam para stokunun %50'si, dördüncü yıl %33'ü, onuncu yıl 10%u olacak şekilde giderek azalan oranda. Bu nedenle ilk yıllarda para arzı çok fazla olduğu için insanlar parayı ellerinde tutmak yerine (paranın değer saklama özelliği) alışverişte kullanacaklar (paranın ödeme aracı özelliği). Ancak ilk 15-20 yıl sonrası arz mevcut para miktarına göre iyice azalınca parayı elde tutmak değerli hale gelecek. 

### Neden popüler oldu bu kadar?

Grin'in bu kadar popüler olmasının belki de en önemli nedeni yukarıda da bahsetmeye çalıştığımız Bitcoin benzeri cypherpunk köklere sahip olması. Zira cypherpunk'lar bireyin özgürlüğünü ve devlet benzeri otoritelere karşı bağımsızlığını savunurken, bunu bir organizasyon altında yapmaları durumunda otoritelerin uygulayacakları baskılar ile organizasyonları ezeceği, kişileri ise hapis de dahil türlü yaptırımlar ile yıldıracağı korkusu taşıyorlar. Kişilerin gizliliğini ve bağımsızlığını savunabilmek için kendilerinin de gizli olması gerektiğine inanıyorlar. (Bu nedenle Satoshi ismini gizli tuttu, Wikileaks aracılığıyla Bitcoin ortaya çıktığı anda sırra kadem bastı - tüm hikayesi [bu yazımızda](https://ademimerkezi.com/genel/2018/06/01/token-dunyasinin-ilk-oyuncusu-tanidik-bir-isim-bitcoin.html)). 

Örneğin, bu köklere sahip bir oluşum olarak başka KriptoParalar (Monero, Dash, Zcash) gibi kurucu ekibin kendine baştan bir pay ayırmaması onları kripto camiası içinde saygın bir yere koyuyor. Çünkü "[premine](https://www.cryptocompare.com/coins/guides/what-is-a-premine/)" ya da "founders' share" de denen bu tip bir uygulamanın adil bir paylaşım olmayacağına inanıyorlar. 
 
Bunun yanında Bitcoin'in başlangıcındaki hızlı gelişimi ve fırsatı kaçıran ciddi bir kesim de, şimdi yeni çıkan bu oluşuma erken katılarak oluşacak fırsatlardan olabildiğince çabuk faydalanma peşinde - ama bu kesimin bir sonraki kısmı okumasında fayda var. 

 ![halfin-vs-jlopp-900.png](/assets/halfin-vs-jlopp-900.png)

Ama sadece cypherpunk topluluğu değil Grin'i popüler yapan. Her ne kadar dışarıdan yatırım almasa da girişim sermayeleri bir şekilde projeye destek oluyorlar. Nasıl mı? Bir önceki yazımızda bahsettiğimiz değişen yatırımcılık kapsamında. Grin 15 Ocak itibari ile çalışmaya başladı ve işlemler karşılığı madencilere para yaratma hakkı verdi. İşte pek çok girişim sermayesi de şu anda para harcayıp makine satın alarak ve enerji harcayarak madencilik yapıyor. Amaçları Grin parasına rekabet artmadan erkenden sahip olabilmek. 

Yine de bu yatırımcıların, benzer şekilde para yaratımına başlamadan önce büyük sükse yapmış "mahremiyet" esaslı diğer paraların yaratılmaya başladıktan sonraki sürede değer değişimlerini iyi incelemelerinde fayda var. Bakın, Monero, Zcash ve Ravencoin, ilk çıkışlarından sonra değerlerini ne kadar kaybetmiş: 

&nbsp;

| ![monero-zcash-ravencoin.jpg](/assets/monero-zcash-ravencoin.jpg) | 
|:--:| 
| *Monero, Zcash ve Ravencoin ilk çıkış sonrası seyirleri - [Kaynak](https://twitter.com/ByteSizeCapital/status/1085155010495709184/photo/1)* |

&nbsp;


Bir başka hipotez ise şu:  Bitcoin artık para olarak değer taşıma (SoV- Store of Value) konusunda kendini kanıtladı. İnsanlar ona bir değer atfediyor. Üstelik arzı kısıtlı olması değerinin artacağı yönündeki beklentileri de artırıyor aynı zamanda. Ancak  teknik kısıtlarından ve yavaş gelişiminden dolayı paranın bir diğer önemli özelliği olan ödeme aracı (MoE- Medium of Exchange) olma konusunda ise geride kalıyor. (Lightning Network gibi bu alanda çalışan girişimler var tabii). Ancak pazarda özünde bir ödeme aracı olacak bir para ihtiyacı daha var. Grin de Bitcoin'e yakın felsefesi ve mahremiyet konusunda ön plana çıkan özellikleri ile bu boşluğu doldurmaya en büyük aday. 

### Neleri eleştiriliyor?
Grin ile ilgili eleştirilerin ana odak noktası, aslında övünerek bahsettikleri yatırım almama konusu. Bazıları, Grin yaratıcı ekibinin dış bir yatırım almaması nedeniyle kendisini baskı altında hissetmeyeceklerini ve bunun da koydukları hedefleri zamanında gerçekleştirmek için kendilerini zorlamayacaklarını düşünüyor. 

Bunun dışında eleştirilen konulardan biri de ekonomik: Grin'in para yaratım politikası. Bitcoin'in fiyatının artmasındaki en önemli konulardan biri zamanla kullanımı artarken yaratılan Bitcoin'in azalacak olması. Piyasadaki Grin miktarının sürekli artacak olması onu Bitcoin benzeri spekülatif bir değer artışına gitmesini engelleyebilir. Grin'in buna yanıtı şu: "Bitcoin'in başlangıcında fazla fazla yaratılan para, hasbelkader işi başında dalgayı yakalayanlara inanılmaz kazançlar sağladı ancak yaratılan değer ufak bir azınlığın elinde kaldı. Biz bu yaratılacak değeri daha geniş bir kitleye dağıtmak için daha egaliter bir yapı öngörüyoruz, bu nedenle para arzının sürekli olarak artıracağız"

Akla gelen soru işaretlerinden biri de gizlilik ile geniş kitleler tarafından adaptasyon arasındaki çelişki. Biliyorsunuz özellikle KriptoPara borsaları bu dünyaya adım atmanın en temel yollarından biri. Ancak merkezi çalışan KriptoPara borsaları otoritelerin denetimi altında olduğu için müşterilerinin gerçek bilinen kişiler olduğunu sıkı takip etmek zorundalar (AML/KYC prosedürleri ile). Grin gibi tam gizli olduğunu iddia eden bir para bu borsalarda nasıl işlem görecek? İşlem gördüğü durumda gizlilikten ödün vermiş olacak mı? Ya da hiçbir ödün vermeyecek ve geniş kitleler tarafından adapte edilmeyen, sadece baskı altındaki rejimlerde yaşayanlar tarafından kullanılan ufak (niş) bir para olarak mı kalacak? Grin yaratıcıları Bitcoin üzerine inşaa edilen Lightning Network gibi ikinci katman uygulamaların benzerlerinin Grin üzerine kurulabileceğini ve isteyenin bu uygulamalar ile KriptoPara borsalarında işlem yapabileceğini iddia ediyorlar. Gizlilik ile geniş kitle adaptasyonu bir arada nasıl yürüyecek göreceğiz. 

### Sonuç
KriptoPara dünyasında her gün yeni değişik bir ortaya çıkıyor. Her ne kadar ICO piyasalarının geçtiğimiz yılın ikinci yarısından bu yana popülerliğini kaybetmiş ve KriptoParalara ilgili bir kısım kitlenin hevesini kırmış olsa da, bu alanda çalışan girişimciler üzerinde çalıştıkları projeleri yavaş yavaş ayağa kaldırmaya devam ediyorlar. MimbleWimble ve özellikle Grin, bu alanda Bitcoin'in eksik olduğu düşünülen gizlilik alanında devrim yaratacağını düşünen, aynı Monero, Dash, Zcash benzeri yeni bir para. Ancak kimi teknik özellikleri ve kuruluş felsefesi onu diğer KriptoParalar'dan ayırıyor. 

Teknik olarak MimbleWimble ve Grin'i diğerlerinden ayıran nedir diye merak ederseniz yazımızın devamına [şuradan] ulaşabilirsiniz. 


# YAZI III
Geçtiğimiz iki yazıda [önce](https://ademimerkezi.com/genel/2019/01/23/miblewimble-aranan-mahremiyet-buyusu-mu.html) MimbleWimble denen Harry Potter dünyası karakterlerinin hakim olduğu ve gizlilik konusunda yeni bir çığır açan bir teknolojiden bahsetmiş, [sonra](https://ademimerkezi.com/genel/2019/01/24/gelecegin-odeme-araci-grin-mi-olacak.html) da özellikle cypherpunk dünyasında heyecan yaratan MimbleWimble üzerine kurulu Grin parasına değinmiştik.  Bu iki yazıyı teknik altyapısı olmayanlara tavsiye edebiliriz. Eğer işin teknik olarak daha detayına girmek isterseniz, aşağıdaki yazı ilginizi çekebilir. 

### MimbleWimble ve Grin: Bitcoin'e benziyor mu, farkları neler?


#### Gizlilik

Aslında MimbleWimble, Bitcoin'in üzerine kurulduğu teknolojiyi daha gizli hale getirmeye yarayan bir protokol. Ne kastediyoruz bakalım: 

MimbleWimble'da ne kullanıcılar ne de işlemler görünmeyecek. Bu nasıl gerçekleşecek? 
Öncelikle sistemde paranın gidip geleceği hesaplar olmayacak. Bunun yerine cüzdanlar kullanılacak. 

Normalde Bitcoin sisteminde hesaptan para 'input' olarak sisteme girer, input karşılığı da aynı miktarda output çıkardı (bu output'a UTXO denirdi). Sistemdeki makinalar çıkan bu UTXO'ları toplar ve değişmediğini gördüklerinde "tamam" derlerdi "sistemde çifte harcama yapılmamış" (şu [yazımızda] değinmiştik bu konuya)

Grin sisteminde ise input yok, çünkü input yaratacak adresler kullanılmıyor. Bunun yerine sistemde sadece output'lar yani UTXO'lar var. Bunlar da cüzdanlar aracılığı ile kullanılıyor. Sistem iki kullanıcının bir şekilde (on-line ya da off-line) kendi arasında ne tip bir işlem yapacağı konusunda iletişime geçip anlaşma yapması esasına dayanıyor. Yani Ayşe Bora'ya 100 Grin göndermek istiyorsa buna kendi aralarında karar verdikten sonra, kendi Özel Anahtarlarını kullanarak bir işlem yaratır. Bu işlemi yaratırken kendi özel anahtarı ile bir adres yaratır ve bunu Bora'ya gönderir. Bora'nın bu sırada online olmasına gerek yok. Bora Ayşe'nin gönderdiği işlemi kendi Özel Anahtarı ile şifreler. Sonrasında bu işlem sisteme girilir. Dolayısıyla sistem sadece iki kullanıcının kendi arasında anlaşarak bir işlem gerçekleştirdiğini görür. 

Bütün işlemlerin biraraya getirildiği bloklarda da Bitcoin'de olduğu gibi işlemler tek tek görülmüyor. Bunun yerine bütün işlemlerin bir toplamı var - dolayısı ile kim ne işlem yaptı [görmek mümkün değil](https://blockonomi.com/grin-mimblewimble/). Benzer şekilde karıştırma/toplamayı CoinJoin denen bir işlem ile Bitcoin üzerinde ikinci bir katman olarak yapmak da mümkün. MimblewWimble CoinJoin'i kendi ana sisteminin bir parçası yapıyor.  

Bitcoin'de adresler belli olduğu için para nereden geldi, nereye gitti biliniyor. Bu nedenle kullanıcıları bir şekilde takip etmek ya da paranın izini sürmek mümkün oluyor. Çünkü Bitcoin'de bir işlem yaptığınızda bunu Bitcoin ağındaki bir makineye (düğüm-node) gönderiyorsunuz o da tüm sisteme yayıyor. İlk gönderilen node'un biliniyor olması, sizin genelde bu node'u kullanmanız gibi teknik nedenler, aslında bu parayı izi sürülebilir bir hale getiriyor.  

Mimblewimble da ise öyle değil. Burada gizlilik çözümü olarak dandelion adı verilen bir protokol kullanılıyor. (Dandelion kara hindiba çiçeği demek, bu çiçeğin özelliği açmadan önce tek bir sap ve yapraktan oluşup açtıktan sonra serpilmesi). MW'de siz sisteme bir işlem gönderdiğinizde bunu alan makine rastgele bir başka makineye gönderiyor, o bir başkasına ve böyle böyle ilk gönderen makinanın izinin sürülemeyeceği bir "bozma (fluff)" sürecinden geçiliyor. 


#### Basitlik/Hafiflik

Bitcoin sisteminin teknik olarak sıkıntılarından biri sistem içindeki makinelerin (node-düğüm) işlemleri teyid etmek için kendi içlerinde tüm blockchain sistemini tutuyor olmaları. Bu data şu anda [200 GB civarında ve giderek artıyor](https://www.blockchain.com/en/charts/blocks-size) . Herhangi bir bilgisayarın sistemi girmesi için bu datayı yüklemesi oldukça uzun bir zaman. 

Grin sisteminde, bir bilgisayar tüm bu datayı tutmak yerine fast sink denen bir metod ile son 2000 bloğu güncelleme (sync) yaparak dakikalar içinde sistemi kullanabilir hale geliyor. 

Gizlilik aslında ölçeklendirme ile çelişkili bir kavram. Neden? Çünkü ne kadar gizlilik isterseniz o kadar işin içine şifreleme mekanizmaları giriyor. Ne kadar şifreleme mekanizması koyarsanız sistem üzerinde saklayacağınız bilgiyi o kadar artırıyorsunuz. Bu da sistemin ağırlaşmasına neden oluyor. Özellikle sistemi büyütmek ve geniş kitlelere yaymak istediğinizde ölçeklendirme (scaling) problemi yaşar hale geliyorsunuz. 

Bunun yanında Grin'in Bitcoin'e göre önemli bir eksikliği içinde ayrı bilgi (Scripting) sağlamaya izin vermemesi. Bitcoin'i genelde para transferi için kullanıyoruz ama aslında herhangi bir dijital varlık ya da bilginin transferi için de kullanabiliriz. Bunu sağlayan içindeki Scripting mekanizması. Ancak bu fonksiyon aynı zamanda ekstra yük getirip blokların büyüklüğünün artmasına ve sisteme yük bindirmesine yol açıyor. 

Grin bu tip Scripting mekanizması içermiyor. İşe yaradığı tek alan para transferi. Kendisini ödeme aracı olarak konumlandırdığı için daha hızlı olabilmek adına böyle bir farklılaşmaya gitmiş Grin yazılımcıları. 

#### Uzlaşma Mekanizması

Evet, aslında MimbleWimble teknik altyapı olarak Bitcoin'e benziyor. 

Örneğin, aynı Bitcoin gibi uzlaşma mekanizması olarak makinelerin enerji kullanması prensibinden hareket eden Proof-of-Work mekanizmasını kullanıyor (PoW'yi anlatan detaylı yazımız [burada]). 

Grin'in kullandığı PoW versiyonunun adı [Cuckoo Cycle](https://medium.com/codechain/cuckoo-cycle-c337e30c6c99). Bu versiyonun özelliği Bitcoin sistemini domine etmeye başlayan ASIC tipi madencilik yapan ihtisas makinelerinin etkisini azaltmak. Grin başlangıçta ASIC resistant denen sistemi kullanarak olabildiğince küçük bireysel madencinin sistemin içinde olmasını istiyor. Ancak uzun vadede bunun beyhude bir çaba olduğunu düşünüyorlar ve kademeli olarak ASIC tipi makinelerin de sisteme girmesine izin verecekler. 

Aynı zamanda Grin içindeki işlemleri gerçekleştirirken kullanılacak öğütme mekanizmasının ileride çok kuvvetli makinalar (quantum computers) tarafından kırılacağı iddia edilen bitcoin mekanizmalarına benzer akibeti yaşamamak için 'quantum resistant' denen çok güçlü mekanizmalar olması planlanıyor. 

Hız ve ölçeklenme konusunda avantajlı konumda olduğu iddia edilen Rust dilini kullanıyor Grin. 

Ayrıca dediğimiz gibi felsefi olarak Bitcoin'e şimdiye kadar en yakın görülen para (Bitcoin Cash, Bitcoin SV gibi paraları kayda değer bulmadığımız için görmezden geliyoruz). Bitcoin içindeki geliştirici kitlenin bir kısmı da bu projeye katkı veriyor. 

#### Bloklama ve zorluk dereceleri

Bitcoin sistemi içindeki madencilere sorduğu soruların zorluk derecesini iki haftada bir ayarlıyor. Bu zorluk ayarlamasını yaparken bulmacanın çözülme hızına bakıyor ve hızlı yani 10 dakikadan çabuk çözülüyor ise zorlaştırıyor eğer 10 dakikadan uzun sürüyor ise kolaylaştırıyor. Grin bu zorluk ayarlamasını çok daha hızlı bir şekilde yapacak. Aynı Bitcoin sonrası çıkan başka pek çok Blockchain sisteminin yaptığı gibi 

Bitcoin sisteminde işlemler 10 dakikada bir toplanıp blok oluşturulurken Grin'de bu dakikada bir olacak. Bitcoin şu anda 10 dakikalık blok oluşturma sonrası 12.5 BTC ödül verirken Grin dakikada bir 60 Grin verecek. Grin'de Bitcoin'de dört yılda bir yaşanan azalma da yok, dolayısı ile ileride eğer devam ederse piyasada bol miktarda Grin olacak. 

Peki MimbleWimble bir protokol olarak Lightning Network gibi Bitcoin üzerine ikinci bir katman olarak uyarlanamaz mıydı? Ayrı bir paraya ihtiyaç var mıydı?

#### Sorunları sıkıntıları

Grin'in izleyeceği enflasyon yaratan para politikası aslında gelecekte fiyatının çok değerlenmesinin önündeki en büyük engellerden. Peki neden böyle bir para politikası izliyor Grin?

1. bitcoin'in deflationary özelliği nedeniyle para ödeme aracı değil değer saklama aracı olarak kullanıldığı düşünülüyor. Grin sürekli olarak bir supply yaratarak ödeme aracı olarak kullanılmak istiyor
2. bitcoin örneğinde ilk madenciler sonrasındaki ciddi değer yükselmesinden dolayı inanılmaz paralar kazandılar (satoshinin kullanmasa bile [1 milyon BTC'si olduğu biliniyor](http://time.com/money/5002378/bitcoin-creator-nakamoto-billionaire/)). Grin, daha "adil" bir dağıtım süreci öngörüyor

İşlemlere hız katmak amacıyla scripting özelliğini yok etmesi ileride Grin'in sadece para transferi için kullanılacak bir araç olarak fonksiyonlarında sınırlamalar yaratabilir. Ancak üzerine inşaa edilebilecek ikinci seviye katmanlar ve ek yazılımlar ile bu sorun giderilebilir gibi görünüyor. 


### Sonuç



Tekrar hatırlatalım. Serimizin MimbleWimble'ı anlatan ilk yazısına [buradan], Grin üzerine yoğunlaşan ikinci yazısına [buradan] ulaşabilirsiniz. 

Bunun yanında, bir kısım Bitcoin geliştiricisinin yarın öbür gün Bitcoin'in başına bir 'şey' gelmesi (teknik konular vb) halinde kendilerine bir B planı aradığının ve Grin'in de bu alana önemli bir aday olduğunu düşündüklerini de belirtelim. 

Grin'i Bitcoin geliştiricileri arasında popüler olmasının bir nedeni de Bitcoin'in artık genel kabul gören ciddi bir yapı olması nedeniyle üzerine yapılan değişikliklerin çok yavaş olması. Grin o anlamda bir nevi Lightningn Network gibi hızlı gelişime imkan veren bir yapı içinde. 





https://www.theblockcrypto.com/2019/01/08/mimblewimble-history-technology-and-the-mining-industry/










- mible-wimble https://www.theblockcrypto.com/2019/01/08/mimblewimble-history-technology-and-the-mining-industry/
- Grin, Beam
- Farkları, özellikleri
- Critisim: Monetary policy
- Amaçları ne böyle bir para çıkarmanın?
-- Bitcoin'in bir gün vulnerable olacağını düşünmeleri mi? Güvenlik açısından?
-- Şu an yeterince private olmadığı için insanları bir gün çekmeyeceğini düşündükleri için?
-- Şimdiden erken bir projede yer alıp "voliyi vurmak"?
- Fair launch https://twitter.com/lopp/status/1085885684404019200
https://twitter.com/nic__carter/status/1085886693872492545
- Early adaptor olarak "Bitcoin'i kaçırdık başlangıcını, şimdi yeni bir oluşumun başından itibaren olalım" demek için 
- in terms of scaling?
- aynı lightning ya da liquid'de olduğu gibi bitcoin'in yavaş hareket etmesi mi?
-- çünkü bitcoin en popüler para olarak yavaş hareket etmek zorunda, muhafazakar bir yapısı var
- bitcoin maximalists, interested
-- completely decentralized project (as opposed to ICO)
-- technology interesting
--



-- para yaratım sürecinin bile dağıtık ve adil yapmaya çalışan
-- "teknik olarak exchange'ler ile kaynak yapacağız ama kimseye karşı bir zorunluluğumuz yok" diyebiliyorlar,
-- Aslında bir nevi FU şeklinde bir attitude'ları var


Ekip önündeki en kritik konulardan biri
- KYC/AML prosedürleri çok önemli hale gelmeye başladı
- Otoriteler özellikle exchange'leri bu konuda sorumlu tutuyorlar zira exchange'ler bu dünyaya ana giriş kapıları
- Geniş kesimlerin adaptasyonu için bu tip prosedürler gerekli olabilir
- Ama Grin özünde privacy özelliğini ön planda tutuyor, iki konu birbiri ile çelişiyor
- Ya privacy'den ödün verip KYC/AML ile geniş kitlelere yayılacak
- Ya da privacy'den ödün vermeden daha küçük ölçekli bir para olarak kalacak
- Kendilerinin söylediği blockchain'in kendisi privacy özelliğine sahip olacak ve isteyen buradan kullanacak
- Ama üzerine inşa edilecek olan ikinci seviye katmanlar ile KYC/AML gibi hükümetleri ilgilendiren konularda onları tatmin edecek çözümler yaratılabilir

Diğer bir eleştiri kaynağı ise para politikası
- Neden satoshi'nin yaptığı gibi belli ve biten enflasyon yaratmayan bir para kurmuyorsunuz diyenler var. 
- zira yatırım olarak bakıldığında Bitcoin'in değer atfedilmesi ve değerlenmesini sağlayan etmenlerden biri scarcity- yani arzının kısıtlı olması
- insanlar benzer şekilde Grin'e erken girmek ve az iken çok alıp sonrasında azalınca değerlenmesini istiyorlar
- Grin buna izin vermeyecek gibi görünüyor


- Diğer

Grin yaklaşık bir buçuk iki yıldır geliştirme halinde




solves two problems
- one is the kind of scaling side of the blocks, and the
- second appears to be privacy coming as default.
- to verify an output, you have to follow it all the way back to the beginning of a chain, basically, in order to verify it. This uses some mathematical tricks so that instead of having to verify the entire history of the chain, you can just verify instead that everything amounts to zero, so all the transactions and all the outputs and everything that goes into it just have to equal zero and then you know, you can validate it from there. you know that’s fine, and there was no new money created there. The inputs equal the outputs
- Well, there are no addresses. So everything happens kind of on the wallet side. So, on a Mimblewimble blockchain, since there’s no concept of address, all you have is a UTXO set that just has outputs in it. It’s basically outputs and outputs and outputs all the way down. The way a transaction works is you don’t kind of put an address in and send it off to the chain. You actually have to communicate with another wallet. So the two wallets will work together, use their private keys to build a valid transaction, and then afterwards that transaction can get sent to the chain. So there’s certain, there are no addresses in a cryptographic sense.
- the solution for this wallet exchange, it’s not a one size fits all solution. Some people will be very, very concerned about, you know, everything is extremely private, and want to kind of set up their own communication network to make sure that everything they do is extremely private. Other people might be happy enough using an intermediary service that actually does the matchups and the transaction building. So what we’re trying to do on Grin is just make sure that we can enable all of those possibilities.

*A lot of flexibility for performing a transaction, you have to find a transacting party then match and then result to be written in blockchain- so it is always an output and it is always a zero-sum game, so you do not need to validate the whole history*
a lot more flexibility then? This could be done over email, private chat groups. It can be done almost with anything? 
- Yes. We have somebody now working on sending exchanges over Keybase, which I think is a nice little solution there because you already have the communication going there. You have filed in place, you have the people building mobile wallets, it should be possible to go and bump your phones together to do the transaction. So there’s, there’s a lot of possibilities there, definitely.

*bitcoin maximalists love it. especially grin. just like bitcoin, no founder, all key developers are hidden. is it something developed by crypto anarchists, as a backup to bitcoin, in case bitcoin to become influenced by a government or a centralized power in that sense?*

*or they (maximalists) like it because the development is faster, or changing founding blocks of bitcoin is difficult? or they see a fundamental problem (flaw, architectural isseu) in bitcoin so they look for an innovative system*

*It is private becauase all the information including private keys and data amounts are hidden with something called perfect information hiding*
if putting transaction data amounts and hiding your private key into a form which nobody can … It’s called perfect hiding, perfect information hiding

*block size will be limited to improve efficiency. If you create anything that fills up the block you will be penalized (pay higher fees)
block size limits. There’s a waiting because on a Mimblewimble Blockchain outputs can be destroyed, which actually reduces the … When you send and output and spend it off, it reduces the size of the chain, basically. The amount of data that has to be sent around. So transactions are weighted in a certain way that if you’re creating a lot of outputs, you’re penalized. If you destroy a lot of outputs, you’re not penalized as much. Your fees are lower, we have a soft limit and a hard limit. We’re actually still in the middle of adjusting a little bit, but yes, we do have limits.

*teknik olarak tüm blockchain datasını (GB'lar süren) yüklemek yerine fast sink denen bir metod ile sisteme giren yeni bir kullanıcı (düğüm-node) son 2000 blok'u sync ederek, dakikalar içinde sistemi kullanabilir hale geliyor

*sistemin madencilere sorduğu bulmacanın zorluk derecesini bitcoin iki haftada bir ayarlıyor. Bu zorluk ayarlamasını yaparken bulmacanın çözülme hızına bakıyor ve hızlı yani 10 dakikadan çabuk çözülüyor ise zorlaştırıyor eğer 10 dakikadan uzun sürüyor ise kolaylaştırıyor. Grin bu zorluk ayarlamasını çok daha hızlı bir şekilde yapacak. Aynı Bitcoin sonrası çıkan başka pekçok Blockchain sisteminin yaptığı gibi

*bitcoin 10 dakikada bir blokları toplar iken Grin dakikada bir kere blok toplayacak

*bitcoin her bir 10 dakikada 12.5 BTC verirken Grin her bir dakikada 60 grin verecek. Bitcoin yaklaşık dört yılda bir 10 dakikada bir verdiği ödülü yarıya düşürürken, Grin'de böyle bir sistem yok. Sistem sonsuza kadar dakika 60 Grin vermeye devam edecek
* neden böyle bir (steady supply) durumu var?
*1. bitcoin'in deflationary özelliği nedeniyle para ödeme aracı değil değer saklama aracı olarak kullanıldığı düşünülüyor. Grin sürekli olarak bir supply yaratarak ödeme aracı olarak kullanılmak istiyor
*2. bitcoin örneğinde ilk madenciler sonrasındaki ciddi değer yükselmesinden dolayı inanılmaz paralar kazandılar (satoshinin kullanmasa bile 1 milyon BTC'si olduğu biliniyor - CHECK!!!!). Grin, daha "adil" bir dağıtım süreci öngörüyor
*3. 




-- mible-wimble
--- all the developers are harry potter subjects (fans)
---
