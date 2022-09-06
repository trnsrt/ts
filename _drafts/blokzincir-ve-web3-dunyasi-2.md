# Merkeziyetsiz sistemlerin (Web3) teknolojisi blokzincir 

Turan Sert [^1]

### Öz
Bu makalenin temel amacı, Web3 olarak adlandırılan merkeziyetsiz sistemlerin temelini oluşturan blokzincir teknolojisi konusunda okuru aydınlatmaktır. Sırasıyla blokzincir teknolojisinin geçmişini, felsefesini, teknik detaylarını, temel bileşenlerini, çeşitlerini ve kullanıcılara getirdiği faydaları özetlemeye çalışan makale, daha sonra kısaca bu teknolojinin hangi alanlarda uygulanabileceğini sorgulamış ve şu anda kadar kullanım alanının en yaygın olduğu finans sektöründeki uygulamaları incelemiştir. Makalenin son bölümünde ise özellikle finans alanında kullanıcıların yaşadığı risklere değinilmiştir. Son bölümde, blokzinciri temel alan merkeziyetsiz teknolojilerin henüz daha emekleme aşamasında olduğu, buna rağmen uzun vadede kullanıcıların önüne mevcut sistemlerin yanında farklı bir alternatif sunma potansiyeli taşıması nedeniyle ilgiye değer bulunduğu sonucuna yer verilmiştir. 

**Anahtar kelimeler:** Blokzincir, Blockchain, Web3, merkeziyetsiz finance, DeFi 

**JEL Sınıflandırması:** 033, O32


# Blockchain: The underlying technology in decentralized systems (aka Web3)

#### Abstract: 
This article focuses on blockchain, the underlying technology used in decentralized systems (later popularized with the term Web3). The technology has been used for thirteen years (since the introduction of Bitcoin in 2009) and is still in experimental phase. Nevertheless, decentralized systems represent the potential to be a credible alternative to existing centralized offerings.

**Keywords:** Blockchain, Web3, decentralized systems, DeFi, decentralized finance

**JEL Classification:** 033, O32


*[^1]: Araştırmacı, 'Sorularla Blockchain' ve 'Sorularla DeFi - Merkeziyetsiz Finans' kitaplarının yazarı* 

### 1. Blokzincir nedir? 
"Blokzincir nedir?". Hemen hemen herkesin farklı bir yorumunun olacağı bu soruya verilebilecek en temel yanıtlardan biri "Dijital dünyada, ikili her tür ilişkide aracılık yapanların elinde toplanan gücü biz kullanıcılara geri vermeyi hedefleyen felsefenin yarattığı teknoloji" olabilir. 

Blokzincirin temelinde yatan  bu felsefenin çıkış noktasına biraz daha detaylıca bakmakta fayda var: İşin özü aslında bir 'güç çekişmesi' ve kökü insanlık tarihinin başlangıcına kadar gidiyor. Çekişmenin bir tarafında 'birey' diğer tarafında ise 'bireyin sahip olduğu her tür varlık, hak ve özgürlükleri sınırlamaya (ya da onlara sahip olmaya) çalışan yapılar' var.

Yukarıdaki cümleyi okuyunca bu yapıların hareketlerini hemen 'haksız' bir sahiplenme olarak değerlendirmemek gerek.  Aslında bireyler, genelde gönüllü olarak ya da bilerek bu yapılara izin veriyorlar - sonuçta adı konulmamış bir "sosyal ya da ticari kontrat" var ortada. Örneğin, toplum içinde güvenli ve huzurlu yaşamak istiyorsanız gayet tabii varlığınızın bir kısmını vergi olarak vereceksiniz, sonuçta havadan gelecek değil bu hizmetler. Ya da bir işinizi hallederken arada bir aracı varsa gayet tabii o aracı bu hizmeti bir bedel karşılığı size sunacak. 

Dijital çağ öncesi analog çağda, yukarıda bahsedilen 'bireyin haklarının kısıtlanması' çok daha gözle görünür, ancak daha kısıtlı bir şekilde yapılıyordu; zira fiziki engeller vardı. Ancak dijital çağ, yavaş yavaş evrilen bu süreci bir anda hızlı çekime aldı ve bireyler bu hıza alışamadı. Alışamayınca da bu dünyadaki hakları eskisine oranla görülmemiş bir süratle ellerinden alındı. Hâlâ da tam olarak farkındalar mı tartışılır; küçük bir azınlık için bu sorunun cevabı 'evet' ama toplumun büyük bir kısmı için 'hayır'. 

### 2. Neden şimdilerde girdi hayatımıza?

İşte blokzincir, bireyin elindeki özgürlüklerin hızla elinden kaydığını fark edip bu durumu engellemek isteyen bir grup insan tarafından geliştirilen teknolojik bir devrim, daha doğrusu bir evrim. Gündeme oturma nedeni ise yeni milenyumun ilk on yılında yaşanan iki gelişme.

Bunlardan birincisi hayatın içine kendini hissettirmeden girip kullanıcılara ait bilgilere 'el koyan' dijital devlerin ileride büyük bir tehlike yaratacağının - kendilerine Şifrepunk (Cypherpunk) denen bir grup teknoloji delisi tarafından [^2] fark edilmesi. El koyma derken kastedilen, internete ayak basılan andan itibaren kullanıcının ne yaptığının, kimlerle ilişkiye girdiğinin an be an gözlenmesi, kayıt edilmesi ve kimi durumlarda kısıtlanması. 

İkinci olay ise ekonomik: ABD Merkez Bankaları topluluğu FED'in 2008 krizine karşı sınırsız denecek kadar çok miktarda parayı finansal sisteme sokması ve bu paranın bireylerin değil krizi derinleştiren finans kurumlarının cebine gitmesi. Krizi yaymamak argümanıyla riskli yatırımların kurtarılmasının genel olarak 'risk/getiri dengesini' bozması. Bunun sonucu olarak uzun vadede, bu riskli yatırımların yarattığı hasarların bedelini yatırımı yapanların değil krizde bir suçu olmayan bireylerin ödemesi. 

### 3. Teknik olarak nedir?

İşte blokzincir teknolojisini kullanan ilk ürün olan Bitcoin, yukarıdaki iki gelişmeye tepki gösteren felsefenin ürünü. "Acaba dijital dünyada varlıklarıma hiçbir kısıtlama olmadan sahip olabilir miyim ve bu varlıkları istediğim kişiye istediğim şekilde herhangi bir aracıya gerek duymadan transfer edebilir miyim?" sorularından hareketle yapılan çalışmaların ortaya çıkardığı bir araç. 

Blokzincir temel olarak bir yazılım. Bu yazılım, bir kişi tarafından değil bir grup tarafından şeffaf bir şekilde geliştiriliyor. Burada 'açık kaynak' denen bir yöntem kullanılıyor. Geliştiriciler yazılım üzerinde yapılmasını istedikleri değişiklikleri topluluğa sunuyorlar. Topluluk eğer kabul ederse yazılım bu değişiklikler ile güncelleniyor. 

Blokzincirin bir başka özelliği ise bir 'açık defter' olması. Bunu muhasebe sistemlerindeki ikili defter tutmanın yerine üçlü defter tutma olarak adlandıranlar da var. Nasıl muhasebede gerçekleşen işlemler, işlemi gerçekleştirenler tarafından muhasebeleştiriliyor ise, burada bu işlem aynı zamanda bu açık deftere yazılıyor. 

Açık defter, adı üzerinde herkesin görebildiği şeffaf bir defter. Öyle ki, örneğin Bitcoin blokzincirinde yapılmış olan tüm işlemler sistemin kurulduğu 2009 yılından bu yana tek tek görülebiliyor.  Bu defter birbirinden bağımsız binlerce makinede senkronize bir şekilde tutuluyor. Bu defterin bir başka özelliği de sonradan tahsis ile geriye dönük düzeltilemiyor olması. 

Nasıl emin oluyoruz geriye doğru bir tahsis olmadığına? En basitinden Bitcoin sistemini ele alacak olursak, bu sistem üzerinden yapılan işlemler her on dakikada bir toplanıyor, doğru oldukları sistemdeki tüm bilgisayarlar tarafından otomatik olarak teyit ediliyor ve bir nevi balya gibi ağzı bağlanıp kilitleniyor. Kilidin anahtarı ise bir sonraki on dakikada toplanan işlem bilgilerinin bulunduğu balyanın içine atılıyor ve on dakika sonra o balya da kilitleniyor. Yani, siz geçmişte olan bir işlemde değişiklik yapmak istediğinizde, geriye doğru bu on dakikada bir toplanan her bir balyayı açmak ve içinden anahtarı alıp bir önceki balyaya geçmek zorundasınız.  

İşte bu herkese açık olma ve geriye doğru düzeltilememe özelliği sistemin kullanıcılara 'insan eli değmeden güven veriyor' olmasını sağlıyor. 

Blokzincir dünyasında bu yazılımı yazan geliştiriciler dışında iki temel öğe daha var. Bunlardan birincisi kullanıcılar. Kullanıcılar, blokzincir dünyasına sahip oldukları dijital cüzdanlar aracılığıyla giriyorlar. İyi de bu cüzdanlarda ne var? Temel olarak bu cüzdanların içinde dijital varlıklar var ancak bir farkla; bu varlıklar fiziki değil, ya da fizikiye çevrilemiyor.  Dijital varlık, sistem üzerindeki yani blokzincir açık defteri üzerinde kayıtlı olan sanal parayı ifade ediyor. Cüzdan ise blokzincirdeki kaydın kullanıcıya ait olduğunu kanıtlayan şifreleri (özel anahtar da deniyor bunlara) saklıyor. 

Peki sistemde işlem yapılan dijital varlıklar, yani kriptoparalar nasıl doğuyor? Burada da, blokzincir dünyasının yukarıda bahsettiğimiz temel öğelerinden diğeri işin içine giriyor. Dijital dünyada kurulu blokzincir sisteminin dış tehlikelere karşı korunması ve kullanıcılardan gelen işlemlerin kayıt altına alınıp doğruluğunun sağlanmasını binlerce makine yapıyor demiştik. İşte bu makinelere de madenci deniyor. Bu madenciler yaptıkları iş ve harcadıkları enerjinin karşılığı olarak belirli bir ödüle sahip oluyorlar. Bu ödüller esasında sistemin emisyon yaratımını sağlıyor. Örneğin Bitcoin sisteminde şu anda yaklaşık olarak her on dakikada bir 6.25 BTC çıkarılıyor. Belki de çoğu kişinin duyduğu ama anlamlandıramadığı 21 milyon rakamı işte bu en başından beri belirlenmiş olan toplam emisyon rakamı. Bu rakamın şu ana kadar yaklaşık %90'ı çıkarılmış durumda. Kalanı bundan sonraki dönemde çıkarılacak (2140 yılına kadar). 

Yapılan işlemlerin kayıtlarının, hesaplara ait bakiyelerin, kullanılan yazılımların kaynak kodlarının tamamen açık olduğu bir dünyadan bahsettik şimdiye kadar. Peki, gizlilik nerede? Gizlilik temel olarak bu varlıklara sahip olanların kimlik bilgilerinde. Blokzincir adı üzerinde bir altyapı. Kaydını tuttuğu varlıkların sahiplerini bilmiyor. Sahipler bu varlıklara biraz önce de bahsettiğimiz gibi anahtarları vasıtasıyla giriyorlar. 


### 4. Temel bileşenleri neler?

Yine işin tarihçesine dönersek, blokzincir denen sistem öyle bir anda ortaya çıkmadı. Temel olarak üç kritik gelişmenin artık olgunlaşmaya başlaması sayesinde blokzincir ortaya çıktı. Gelin şimdi bu üç gelişmeye bakalım: 

Birincisi, aslında bize dijital hayatın nimetlerini de getiren internet. Internet önemli, zira "aracıları ortadan kaldırmak" derken aslında merkezi olan aracılara olan ihtiyacı gidermekten bahsediyoruz. Bunun yolu da bu aracılık hizmetini genele dağıtmak, tek bir elden çıkmasına (bir nevi tekel olmasına) engel olarak demokratikleştirmek. Dağıtılmış hizmeti verebilmesi için bu parçaların birbirleriyle iletişimde olması gerek, dolayısıyla bir ağın parçası olmalılar. Bunu da internet dediğimiz ağ sağlıyor bize. Yani, blokzincir teknolojisini 1950 yılında düşünmüş olsanız da gerçekleştirmeniz imkansızdı!

İkincisi, dijital dünyada bireyin kendine ait varlıkların sahipliğini kanıtlayabilmesi. Bunun için bireyin dijital varlıklarının tek, kopyalanamaz ve değiştirilemez olması gerek. Aynı zamanda bu varlıklar üzerinde yalnızca kendisinin hak iddia edebilmesi için dijital bir kimliği olmalı. İşte bunları sağlayabilmek için de 80'li yılların başından itibaren gelişmeye başlayan şifreleme teknolojilerinin olgunlaşması gerekiyordu. 

2000'li yıllara geldiğimizde artık gitgide olgunlaşmaya başlayan internet ve şifreleme teknolojilerinin üzerine Satoshi Nakamoto dediğimiz kişi/grup üçüncü kritik konuyu geliştirdi. Adeta yağ, süt, un ve şekeri bir araya getirip kıvamında bir helva sundu bizlere. Bu dahiyane fikir dağıtılmış bir şekilde birbirinden uzakta duran makinelerin ortak hareket edip karar verebilmesini sağlayan bir uzlaşma mekanizması idi. 

İşte yukarıdaki üç bileşen sayesinde  **binlerce makine herhangi bir merkezi otoriteden direktif almadan, tamamen serbest bir biçimde on üç yıldır tık demeden çalışan bir sistemi yürütüyorlar**. Blokzincir dediğimiz sistemin özü bu. 

### 5. Kaç çeşit blokzincir var? 

Blokzincir teknolojisinin dünyamızdaki ilk uygulaması Bitcoin ile oldu. Her ne kadar Satoshi Nakamoto denen kişi ya da kişiler tarafından ortaya çıkarılmış olsa da esasında bu teknolojinin ayağa kalkmasını sağlayan gönüllü kullanıcı ve geliştiriciler yani bir diğer deyişle topluluk oldu. 

Bitcoin topluluğu kendilerine hedef olarak 'kişilerin dijital dünyada hiçbir sansüre uğramadan ellerinde tutabilecekleri ve başkalarına aktarabilecekleri bir dijital para' olmak gibi bir hedef edindiler ve bugüne kadar da bu hedefe sıkı sıkı bağlı bir şekilde ilerliyorlar. 

Blokzincirin merkeziyetsiz yapısının sadece bir dijital para (dijital altın) olarak değil aslında çok farklı kullanım alanları olabileceğini savunan bir grup, Bitcoin'den ayrılarak bugün hâlâ ikinci büyük olan Ethereum blokzincirini kurdular.  Sonrasında da farklı topluluklar tarafından yüzlerce hatta binlerce blokzincir kullanıma sunuldu. 

Dolayısıyla burada blokzincirden blokzincire farklar da ortaya çıkmaya başladı. Bitcoin temel olarak dijital altın olmayı savunan bir sistem. Ethereum ise isteyen her geliştiricinin üzerine uygulama kurabileceği bir açık altyapı olmaya çalışıyor. Geliştiricilerin yazdığı bu uygulamalara 'Akıllı Kontrat' deniyor. Dolayısıyla, Ethereum ve onun izinden giden Solana, Avalanche, BNB Chain gibi blokzincirlere genel olarak Akıllı Kontrat Platformu adı veriliyor. Genelleme yapacak olursak Bitcoin'i dijital altın, Ethereum benzeri akıllı kontrat platformlarını telefonlarımızda kullandığımız iOS ve Android cinsi işletim sistemi, bu platformlar üzerine kurulu merkeziyetsiz finans ürünlerini (merkeziyetsiz borsalar gibi) telefonlarımızda kullandığımız uygulamalar olarak düşünebilirsiniz. 

Bitcoin, Ethereum gibi blokzincirler 'açık/kamusal blokzincir' olarak adlandırılırlar. 'Açık' olmaktan kastedilen, dileyen herkesin bu ağları diledikleri zaman kullanabilmelerinden gelmekte. Herhangi bir merkezleri olmayan bu ağların kullanıcıları, geliştiricileri, ya da sistemin işleyişini sağlayan madencileri kendi kimliklerini deşifre etmeden istedikleri zaman kullanıp istedikleri katkıyı yapıp diledikleri zaman da ayrılabiliyorlar. 

Bunların yanında bir de 'izin' ile girilebilen 'kapalı/özel' blokzincirler bulunmakta. 2015-2019 yılları arasında oldukça rağbet gören kapalı blokzincirler, şu anda daha çok perde arkasında yol alıyorlar. Önümüzdeki dönemde özellikle merkez bankası dijital paralarının piyasaya girmeleri ile birlikte kapalı ya da yarı açık blokzincirleri daha fazla duymamız söz konusu olacak.

### 6. Blokzincirin faydaları neler?

Değişik sektörlerde blokzincir ile ilgili uygulamalara baktığımızda genel olarak ağırlık kazanan birkaç ortak tema görmek mümkün. Bunları maddelersek: 

- Merkezi otoritede yaşanan herhangi bir sıkıntının tüm sistemi etkilemesini (ya da durdurmasını) önlemek
- Aracıları ortadan kaldırarak yüksek komisyonları minimize etmek
- Bürokrasinin getirdiği zaman ve emek kaybını minimuma indirmek
- Geriye yönelik olarak doğru, tutarlı, değiştirilemez kayıt bilgisi oluşturmak
- Bireyler için dijital alanda tüm haklarını ellerinde tuttukları dijital kimlikler oluşturmak

### 7. Blokzincir teknolojisi her derde deva mıdır?

Blokzincirin aslında aslında pek çok dezavantajı var. Kısaca bakalım: 

- Bilginin binlerce makineye dağılması ve orada tutulması demek öncelikle oldukça yavaş ve hantal bir yapınız var anlamına geliyor. Veriler geliyor, tüm makinelere dağılıyor, makineler bunu kaydediyor, sonra belli aralıklar ile bunların tutarlı olup olmadığını kontrol ediyor. Zaman isteyen bir süreç, yani merkezi sistemlere göre daha yavaş bir sistem. 

- Aynı zamanda enerji bakımından maliyetli. Merkezi bir sistemde olsa tek bir makine için harcayacağınız elektrik masrafını düşünün, bir de binlerce makinenin aynı bilgiyi tutmasından dolayı gerekecek enerjiyi... 

- Bir yandan da oldukça geniş bir bilgi depolama alanına ihtiyacınız var. Veriyi bir makinede tuttuğunuzda gerekli olan depolama alanını düşünün, bir de aynı verinin binlerce makinada tutulduğunda gerekli olan alanı... 

- Binlerce makinayı içeren bir sistemi düşündüğünüzde sistemin yavaş gelişeceğini de kabul etmeniz lazım. Öncelikle sistemi kurarken çok ince elemeli ve sık dokumalısınız. Merkezi bir veritabanı kurarken gerekli olan önlemleri zaten almanız lazım. Ama üzerine bir de binlerce makinenin bağlanacağı bir merkezi olmayan sistemin getireceği sıkıntılara da göğüs gerecek bir sistem olmalı bu. 

- Keza, sistemi işletirken sonrasında yaptığınız yenilikler de sistem üzerindeki binlerce makina tarafından kabul edilmeli ve içselleştirilmeli. Sistem doğası gereği adem-i merkezi bir yapı olduğu için hiçbir makineye zorla bir dayatmada bulunamazsınız. Gönüllü olmalı bu iş. Dolayısıyla, yapacağınız her tür değişiklik geriye dönük olarak eski versiyonlarda da kullanılabilmeli. Bu da her yaptığınız değişikliğin tüm sistem tarafından toplu kabulünü oldukça yavaşlatan bir durum. 

### 8. Blokzincir hangi sektörlerde başarılı olur? Turnusol kağıdı var mı?

Buraya kadar yazdıklarımızın ötesinde daha net olarak içinde bulunduğunuz sektör için blokzincir gerekli mi sorusuna yanıt için aşağıdaki şemayı kullanabilirsiniz (Kaynak: Thomas Ferry - [To Blockchain or Not to Blockchain](https://medium.com/causys/to-blockchain-or-not-to-blockchain-aed05bf08150) [^3])

![blockchain-scheme-800.png](/assets/blockchain-scheme-800.png) 

### 9. Blokzincirin uygulama alanlarını nerelerde görüyoruz?

Blokzincirin uygulama alanlarının neler olabileceği konusunda pek çok yazı var. (Bu satırların yazarının bundan birkaç yıl önce yazdığı [sağlık](https://turansert.com/genel/2018/04/17/saglik-icin-blockchain.html)[^4], [seyahat](https://turansert.com/genel/2018/07/06/seyahat-icin-blockchain.html)[^5], [tedarik zinciri](https://turansert.com/genel/2018/08/17/tedarik-zinciri-icin-blockchain.html)[^6], [çevre](https://turansert.com/genel/2018/11/16/cevre-icin-blockhain.html)[^7] gibi farklı kullanım alanlarına göz atabilirsiniz). Ne var ki, yine 2015-2019 yılları arasında ortaya atılan bu vizyonlarda temel bir eksiklik var. O da, bahsedilen sektörlerin henüz daha tam olarak dijitalleşmemiş olması. **Halbuki, blokzincirin bir sektörde tam olarak kullanılabilmesi için o sektörün tamamen dijitalleşmiş olması gerekmekte**. 

İşte bu nedenle blokzincirin ilk uygulama alanının finans sektöründe olduğu görüldü. Zira, 1980 yıllarından itibaren yaşanmaya başlanan dijitalleşmeye ilk adapte olan sektör finans oldu. Şu an kullandığımız uygulamalardan tutun, kredi kartları ve online bankacılık ile birlikte finans sektöründe tam bir dijitalleşme yaşıyoruz. Diğer yandan, finans sektörünün temel fonksiyonu kişiler arasında eksik olan güven ihtiyacını karşılaması. Blokzincir de kendisinin temel işlevini güveni insanlardan alıp makinelere vermek olarak görüyor. 

Önümüzdeki dönemde de blokzincirin altyapı olarak kullanılımı hep dijitalleşmiş sektörlerde görülecek. Peki, hangi alanlar bunlar? 

Temel olarak Web3 olarak adlandırılan bu yeni alan kendisine merkeziyetsizliği temel alıyor. Yeni dünya aracılara ihtiyacın azaldığı ve bu dünyada kullanıcıların daha fazla güç ve kontrol istediği bir yer.  Bu nedenle, bu dünyada eski kavramların yenileri ile değiştiği gözlemleniyor. Bu dünyanın birkaç temel öğesi aşağıdaki şekilde sıralanabilir: 

* Para olarak itibari paraların yerini kriptoparalar alacak
* İnsanlar artık fiziki varlık tutmak yerine dijital dünyada varlıklarını NFT olarak tutacak
* Sosyal ilişkiler (iş ile ilgili ya da iş dışı) mevcut sosyal ağlar yerine metaverse ile yürütülecek
* Girişimler ve projeler bu yeni dünyada artık şirketler yerine DAO denilen merkeziyetsiz otonom yapılar aracılığıyla yürütülecek 
* Yukarıda saydığımız bu öğeler arasındaki finansal ilişkilerde ise merkeziyetsiz finans (DeFi) kullanılacak. 

Burada şunu özellikle vurgulamak gerekiyor. Yukarıda saydığımız Web3 dünyası ya da bu dünyanın öğelerinin şu an yaşadığımız dünyanın yerini alacağı gibi bir sav açıkçası hayalcilik olur. 

Yukarıdaki merkeziyetsiz yapıların temelinde, eskinin gücü elinde tutan merkezi yapılarının yerine bu gücün artık kullanıcılara geçtiği bir 'sahiplik ekonomisi' kavramı geliyor. Bu dünya herkese göre değil, ancak şu an görünen kadarıyla kullanıcıların eline çok güçlü bir opsiyon verecek. Bu bile başlı başına çok önemli ve üzerinde düşünülmesi gereken bir konu. 

### 10. Gerçek dünyaya uygun uygulamalar merkeziyetsiz finansta
Bir önceki bölümde de bahsettiğimiz gibi, Web3 dünyasının en ileri uygulamalarının merkeziyetsiz finans dünyasında olduğunu söyleyebiliriz. 

Finansın en temel alanlarından para transferi zaten Bitcoin ve benzeri onlarca kriptopara ile şu anda herhangi bir aracı olmadan gerçekleştirilir durumda. Merkeziyetsiz finans bunun ötesine geçme niyetinde. Şu an aktif olarak kullanılan ürünleri aşağıdaki gibi sıralayabiliriz: 

#### 10.1. Mevduat ve krediler
Bugün DeFi piyasasının içinde olan bir tüketici istediği noktada kredi alabiliyor. Ya ödememe riski? Tabii ki bu varlığın karşılığında dijital bir varlığı teminat olarak veriyor.  Bir örnek ile açıklayalım: 

[Compound](https://compound.finance)[^8] kişilerin kriptopara olarak mevduat yapıp, kredi alabildikleri bir sistem. Sistem ne demek? Bir yazılım. Açık kaynaklı. Geliştirmesini yapan bir elin parmaklarını geçmeyecek sayıda çalışandan oluşan bir ekip. Yazılımın yaptığı, kriptopara havuzları oluşturmak. 

İsteyen bu havuza para koyup faiz alıyor, isteyen ise belli bir teminat karşılığında havuzdan kredi alıp kendi ihtiyaçları için kullanıyor.  Faiz oranları değişken - arz ve talebe göre azalıp artıyor. Tüketici olarak değişken oranlarda kredi almaktan hoşlanmıyor musunuz? O zaman sizi bir başka girişim olan [Aave](www.aave.com)[^9]'ye alalım - orada faizler sabit. 

#### 10.2. Stabil paralar
Stabil para dediğimiz ABD Doları'na bire-bir bağlı kriptoparalar bu dünyanın en kullanılan ürünlerinden olmaya başladı. Kripto dünyasının içinde alım-satım yapan kişi ve kurumlar arada bir sattıkları kriptoparaların karşılığında itibari para dediğimiz ABD Doları gibi paraları tutabiliyorlar. Ancak bu paraları kriptopara borsasında tutmak riskli, kendi banka hesaplarına da çekmek hem maliyetli hem de uzun süren bir işlem. Sonrasında geri işlem yapmak istediklerinde tekrar borsaya göndermeye çalışırken fırsat kaçabilir. Stabil paralar bu anlamda hem kriptoparaların kendine has özelliklerine hem de ABD Doları gibi itibari para anlamında değer kayıplarını önleyen bir yapıya sahipler.  En çok kullanılanları sırasıyla [Tether](https://tether.to/)[^10] (USDT), [Circle](https://www.circle.com/en/usdc)[^11] (USDC), DAI. Bu arada TL'ye sabitlenmiş ülkemizde faaliyet gösteren [BiLira](https://www.bilira.co/)[^12] isimli bir Türk girişimimiz olduğunu da belirtelim. 

#### 10.3. Merkeziyetsiz borsalar
Sadece klasik mevduat-kredi ilişkisinde aracılık yapmıyor merkeziyetsiz finans. Borsa işine de girmiş durumdalar. Bireylerin kriptopara satın alabilmek için ilk uğrak yeri kriptopara borsaları oluyor. Bu borsalar son yıllarda gerek güvenlik gerekse kullanıcı dostu arayüzlerini ciddi şekilde geliştirerek hızlı bir büyüme kazandılar. 

Ancak merkeziyetsiz dünyanın ruhunu aykırı temel bir sıkıntıları var bu borsaların - o da kendilerinin merkezi yapılar olması. Bu yapılarından ötürü dijital dünyada dış tehlikelere açık ve korumasız olarak görülüyorlar. Çok da haksız sayılmaz bu eleştiriler. Hemen hemen her ay ayrı bir kriptopara borsası saldırısı ve para çalınması olayları yaşanıyor. 

İşte merkeziyetsiz borsalar bu anlamda kullanıcılara farklı bir alternatif sunuyor. Bu borsalar, aynı diğer DeFi ürünleri gibi kullanıcının dijital varlığına dokunmuyorlar. Kullanıcının yapması gereken tek aksiyon, borsanın web sitesine girdiğinde elektronik cüzdanını bağlamak ve alım-satıma başlamak. Bu alandaki en büyük girişimler ise [Uniswap](https://uniswap.org/)[^13], [Curve](https://www.curve.fi/)[^14] ve [Balancer](https://balancer.finance/) [^15] olarak ön plana çıkıyor.  

Hemen şunu da belirtmekte fayda. Mevcut merkezi kriptopara borsaları fiziki olarak kuruldukları ülkelerin kanun ve regülasyonlarına tâbiler - bu nedenle bu borsalarda işlem yapabilmek için kullanıcılar KYC (müşterini tanı) ve AML (kara paklama) prosedürlerini geçmek zorundalar.  Bu, devletler açısından yasa dışı yollardan para giriş çıkışını kontrol edebilmek için kritik.  Ancak oldukça zahmetli bu prosedürlerin kullanıcı adaptasyonunu bir parça engellediğini söylemek de mümkün.  DeFi alanındaki girişimler ise tamamen dijital bir dünyada oldukları için şu aşamada bu tip regülasyonlardan uzaktalar. 

DeFi'yi kullanabilmek için bireylerin öncelikle bu kriptoparalara sahip olmaları gerekiyor. On-ramp de denilen fiziki dünyada kullanılan itibari paralardan kriptoparalara geçiş için ülkelerin denetimlerine tabi olan kriptopara borsaları bu işlevlerini gelecekte de sürdürmeye devam edecek. Kriptopara borsasından kripto alarak bu dünyaya adım atan kullanıcılar, bu paraları kendi cüzdanlarına çektikten sonra DeFi dünyasında paralarını cüzdanlarından çıkarmadan işlem yapmaya başlayabiliyorlar. 

#### 10.4. Türev piyasaları
Keza alım satım alanında türev piyasalarının merkeziyetsiz olarak sunulduğunu da görüyoruz. Bu alandaki en büyük sistemler olan [Synthetix](https://synthetix.io/)[^16] ve [UMA](https://umaproject.org/)[^17], kullanıcılara kriptopara, altın ya da Apple benzeri hisse senetlerinin sentetik türevleri ile o ürünlere fiziki olarak olmadan risk ve getirilerinden pay alma imkanı veriyorlar. 

#### 10.5. Sigortacılık
Kripto dünyasına adım atan yatırımcıların ilk fark edecekleri, dijital varlığa tamamen sahip oldukları. Bu bir yandan finansal olarak özgürlük getirse de, diğer yandan büyük bir sorumluluk. DeFi yeni ve henüz emeklemekte olan bir sektör olduğu için kullanıcı arayüzleri o kadar gelişmiş değil. Keza, hızlı gelişim gösterdikleri için bu yazılımlarda sorun çıkma ihtimali yüksek. İşte bu alanda kullanıcıları korumak için yine merkeziyetsiz sigorta çözümleri de çıkmış durumda. [Nexus Mutual](https://nexusmutual.io/)[^18] bu alanda en ileri çözümlerden bir tanesi.  

### 11. Blokzincir dünyasının riskleri neler?

Kripto dünyasının daha henüz 13 yıllık bir geçmişe sahip olduğunu belirtmek gerekiyor. Bu dünyanın kullanıcılar tarafından kullanılan merkeziyetsiz finans uygulamaları ise geniş kesimlerce kullanılmaya 2020 yılında başladılar. Bu nedenle henüz emekleme aşamasında olan bu dünyada pek çok risk bulunmakta. Gelin bu riskleri madde madde yazmaya çalışalım. 

**Merkezi kurum riski:** Blokzincir temelinde merkeziyetsiz bir altyapı. Bu altyapı üzerine kurulan uygulamaların bir kısmı (Web3 ürünlerinde olduğu gibi) merkeziyetsiz olmaya çalışan girişimler. Bunun yanında bir de özellikle bu alana yatırım yapan ya da yatırımlara aracılık eden merkezi kurumlar olduğunu görüyoruz ki, bu dünyadaki en büyük risk faktör bu merkezi yapılar. 2022 yılı içinde UST (Luna sisteminin stabil parası olan USTerra parası)'nin çöküşü ile başlayan son kriz, sonrasında 3AC isimli iki kişi tarafından kurulu olan bir yapının iflası ile derinleşti. Bu derinleşmenin temel nedeni, 3AC'nin müşterilerinden kriptopara mevduat toplayan merkezi yapılardan aldığı krediler idi. Kaldıraçlı olarak yapılan bu işlemlerden tüm piyasalar etkilendi. Blokzincir dünyasının temeli şeffaflığa dayanıyor ve bu merkezi yapılar bu dünyada sadece birer oyuncu. Bu yazımızın içinde genel olarak regülasyonlardan bahsetmeyeceğiz ancak özellike küçük yatırımcıların korunması için bu tip merkezi yapıların mutlaka kanuni denetime tabi olmaları gerekli. Aksi takdirde bu tip krizlerin ileride tekrar yaşandığını görmemiz içten bile değil. 

**Akıllı kontrat riski:** Kripto üzerinde müşterilere sunulan projelerinin özünde birer akıllı kontrat olduğunu belirtelim. Bu akıllı kontratların ise özünde birer yazılım olduklarını daha önce belirtmiştik. Bu kontratları yazanlar birkaç geliştirici. Örneğin, bir sonraki bölümde bahsedeceğimiz DeFi alanındaki en büyük protokol olan Uniswap'ın kurucusunun, 6 Ocak 2021'de attığı bir [tweetten](https://twitter.com/haydenzadams/status/1346575665940860929?lang=en)[^19],  3 milyar ABD Doları piyasa değeri olan protokolün sahip olduğu ekip elemanı sayısının 11 olduğunu öğreniyoruz. Kodun içinde yazım hataları olması, kimi senaryo ve parametrelerin unutulmuş olması gayet olası. 

**Geliştirici ekip riski:** Blokzincir dünyasında kurulu  protokollerin getirdiği merkeziyetsizliğin aslında bir vizyon olduğunu da unutmamak gerek. Hemen hemen her proje merkezi başlar ve yavaş yavaş merkeziyetsiz hale gelir. Başlangıçta merkezi başlayan protokollerde, ürün geliştirmenin ufak bir ekip tarafından yapıldığını belirtelim. İyi niyetli hataların yanında, kimi durumlarda ekiplerin kullanıcı paralarını alıp kaçtığını da görebiliyoruz. Dolayısıyla, özellikle yeni ortaya çıkmış girişimlerden uzak durmakta fayda var. 

**Kriptoparaların inişli-çıkışlı olması riski:** Kriptoparaların ne kadar inişli-çıkışlı (ya da İngilizce'den dilimize geçmiş bozuk kelimelerden biri ile 'volatil') olduğunu söylemeye gerek yok sanırım. İşte bu iniş-çıkışlar kimi durumda yatırımcı ya da işlem yapanlara sıkıntılı zamanlar geçirtebiliyor. Özellikle borçlanma platformunu kullanırken, alınan kredi karşılığı teminat olarak kriptopara veriliyor. Genel olarak yüksek oranda (İngilizce'de 'over-collateralized') olarak verilen bu teminatlar, belli bir seviyenin altına düşerse, teminat likidite ediliyor. Kripto piyasasının 7/24 çalışması nedeniyle, olası ani inişlerde, teminat oranının üstünde kalmak zor olabiliyor. Burada yatırımcı hızlı hareket ederek; ya teminat verdiği kriptopara miktarını artırmalı ya da aldığı kredinin bir kısmını geri ödeyerek teminatının likidite olmasını önlemeli. 

**Dışarıdan alınan bilgilerin manipüle edilmesi riski:** Uygulamaların üzerine kurulu oldukları blokzincir altyapıları (örneğin; Ethereum), doğaları gereği akıllı kontratların zincirin dışıyla iletişim kurmasına olanak vermezler. Akıllı kontratların ise belli koşullar oluştuğunda harekete geçmeleri gerekir; ancak koşulların oluştuğu bilgisine ihtiyaçları var. Bu dışarıdan gelecek bilgiyi onlara 'oracle' denen bilgi kaynakları sağlar. Bu bilgi; başka DeFi projelerinden, başka blokzincirlerden ya da tamamen fiziksel hayattan bile gelebilir.  DeFi projeleri kimi zaman oracle kaynakları maliyetli olduğu için,  bilgiyi kendileri bir-iki blokzincir içindeki kaynaktan almayı seçebiliyorlar.  Bu kaynakların manipüle edilmesi nedeniyle projeye yanıltıcı bilgi gelmesi durumunda ise proje yatırımcıları zarara uğrayabiliyorlar. 

**Altyapı projelerinin ölçeklenememe riski:** Piyasada endişenin hakim olduğu ya da ufak çaplı krizlerin yaşandığı ortamda, blockchain  projelerinin üzerinde yer aldığı altyapı projelerine adeta bir hücum başlıyor. Bu da projelerin kimi durumlarda yüksek talebi karşılayamaz hâle gelmesine yol açabiliyor. 2021 yılının Mayıs ayında yaşanan krizde Ethereum projesi alnının akıyla krizden çıkarken, rakip birkaç projede ciddi sıkışmalar yaşandığını gördük. Öte yandan, Ethereum herhangi bir durma yaşamadan krizden çıkarken, işlem ücretlerinin arşa çıktığını da belirtelim. Böyle bir durumda maliyetlerin yüksekliğinin farkına varmayan yatırımcılar, düşük ücretler ile işlem yapmaya kalktıklarında saatlerce beklemek zorunda kaldılar.  Uzun vadede blokzincirler geniş kitleler tarafından kullanılacaklar ise bu ölçeklenme problemlerini aşmak zorundalar. Bunun için çalışmaların devam ettiğini söyleyelim. 

### 12. Sonuç 
Blokzincir, analog çağdan dijital çağa geçiş süreci içinde yaşadığımız sürecin son halkalarından biri. İlk bilgisayarlar sonrası ortaya çıkan internet ile başladığımız Web 1.0 olarak adlandırılan dönem, internetin ticarileşmesi ile birlikte Facebook, Google gibi devlerin ortaya çıkmasına yol açarak Web 2.0 dediğimiz döneme evrildi. Dijital hayatta gücün bu tip kurumların elinde toplanmasına tepki olarak doğan blokzincir, merkezi yapıların sahip oldukları gücü bireylere dağıtmak hedefinden ortaya çıktı ve Web3 olarak adlandırılan son dönemin perdesini açtı.  İlk kullanım örnekleri finans alanında görülmeye başladı. Yakın dönemde duymaya başladığımız NFT'ler, henüz belki de kısmen duyulan merkeziyetsiz otonom yapılar ve metaverse ile birlikte temeli merkeziyetsizliğe dayanan pek çok uygulamanın ileride hayatımıza girmesi söz konusu. 

Henüz 13 yıl önce kurulan bu yeni teknoloji daha emekleme aşamasında, bu nedenle uygulamalar geniş kitlelerin kullanımına hazır değil ve pek çok risk içeriyor. Yine de bu alandaki girişimlerin verdiği hizmetlerin bir hayalin ötesinde artık ileri seviye kullanıcılar tarafından gündelik hayatta kullanım aşamasına geçtiğini görüyoruz. İleride bu tip uygulamaların şu an içinde bulunduğumuz merkezi yapıların yerine geçeceğini düşünenler olsa da bunun gerçekçi olduğunu söylemek çok da mümkün değil. Yine de merkeziyetsiz yapıların kullanıcının önüne farklı bir alternatif olarak çıkması, merkezi yapıların kullanıcılara sundukları hizmeti daha iyiye götürmek yolunda daha fazla çaba göstermelerini sağlayacak. Sonuç ne olursa olsun, kazanan biz bireyler olacağız. 



[^2]: Eric Hughes'un A Cypherpunk's Manifesto'su' (https://www.activism.net/cypherpunk/manifesto.html) (Türkçe çevirisi: http://blog.bluzz.net/bir-sifrepunkun-manifestosu/) Şifrepunk'ları anlamak için yardımcı olabilir. 
[^3]: https://medium.com/causys/to-blockchain-or-not-to-blockchain-aed05bf08150 
[^4]: https://turansert.com/genel/2018/04/17/saglik-icin-blockchain.html 
[^5]: https://turansert.com/genel/2018/07/06/seyahat-icin-blockchain.html 
[^6]: https://turansert.com/genel/2018/08/17/tedarik-zinciri-icin-blockchain.html 
[^7]: https://turansert.com/genel/2018/11/16/cevre-icin-blockhain.html 
[^8]: https://compound.finance 
[^9]: http://www.aave.com 
[^10]: https://tether.to/ 
[^11]: https://www.circle.com/en/usdc 
[^12]: https://www.bilira.co/ 
[^13]: https://uniswap.org/ 
[^14]: https://www.curve.fi/ 
[^15]: https://balancer.finance/ 
[^16]: https://synthetix.io/ 
[^17]: https://umaproject.org/ 
[^18]: https://nexusmutual.io/ 
[^19]: https://twitter.com/haydenzadams/status/1346575665940860929?lang=en 
