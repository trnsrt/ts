
Bu yazımızda gelin DeFi dünyasına özgü Flash Loan vakalarını, ne demek olduğunu anlamaya çalışalım.. 

Merkeziyetsiz finansın, klasik finansın mevcut sorunlarına çözüm bulma amacıyla yola çıktığından bahsetmiştik. İnsanların finansal dünyadaki ihtiyaçlarını daha özgür ve gücü ellerinde tutacak şekilde gidermelerini sağlamaya çalışan DeFi, bunu yapabilmek için temelden farklı bir şekilde kuruldu. Bunu da her bir farklı üründe gözler önüne seriyoruz.. 

### DeFi ile yeni açılımlar ve yeni sorunlar... 

Tabii kişilerin ihtiyaçlarını karşılarken ilk bakılan şu oldu? Kişinin ne ihtiyacı var ve klasik finans bunu nasıl karşılıyor? Biz benzer şekilde karşılayabilir miyiz? Bu çok normal insan tepkisi. Hiç bilmediğiniz bir alana girdiğinizde, eski bildiklerinizi çıkış noktası alırsınız. Bir nevi tutunacak bir dal ararsınız. DeFi'da ilk ortaya çıkan teknolojiler de bu şekilde yol aldılar başta. 

Sonrasında işin rengi yavaş yavaş değişmeye başladı. Öncelikle, DeFi'nin sunduğu farklı imkanları keşfeden insanlar daha talepkar oldular. DeFi, mevcut açık yapısı ile klasik finansın sunamadığı pek çok farklı servisi de insanların hizmetine sundu. Örneğin, bir token almak istiyorsunuz. DeFi dünyasının içinde ilk başlarda bunu yapmak için cüzdanınızı bir merkeziyetsiz borsaya bağlamanız ve fiyatları görmeniz gerekiyordu. Artık, cüzdanınızın içinden sekiz-on tane borsanın almak istediğiniz token fiyatlarını anında bulup işlem yapabiliyorsunuz. 

Bunlar işin güzel tarafı. Bir de madalyonun öbür tarafı var.. Bu kadar esneklik ve kolaylık bir taraftan da belli açıklar getirebiliyor.. Bu açıklar bir şekilde çözülüyor. Ancak bir de işin temeline dokunan boşluklar var ki, onları çözmek vakit alabilir.. İşte onlardan biri de son zamanlarda sık sık duymaya başladığımız flash loan hadisesi.. Gelin bir bakalım ne imiş flash loan, neler yaşanmış bu dünyada, ve nasıl bu boşluklar doldurulabilir:

### Olaylar, olaylar.. 

Efendim, 2020 yılının Şubat ayında bir haber ile sarsıldı DeFi dünyası: '[bZx hacklenmiş](https://cointelegraph.com/news/decentralized-lending-protocol-bzx-hacked-twice-in-a-matter-of-days)'.. Hemen arkasından iki gün sonra yeni haber 'bZx tekrar hacklenmiş'.. 

Sonra Ekim ayında bir haber daha duyduk.. '[Value DeFi flash loan atağı yemiş, 6 milyon ABD Doları zarar etmiş](https://news.bitcoin.com/defi-protocol-bragged-having-flash-loan-attack-prevention-hacked-6-million/#:~:text=Value%20Defi%20said%20it%20suffered,million%20in%20DAI%20from%20Uniswap.)' diye.. Allah Allah.. Ne ola ki bu flash loan'lar?.. Bak DeFi'nin de açığı çıkmış.. 

Sonra Kasım'da [bir daha](https://www.coindesk.com/value-defi-suffers-6m-flash-loan-attack)... Bir tane daha.. Artık kabak tadı vermeye başladı değil mi?.. Neler oluyor dostlar?.. Gelin bakalım neler olmuş...


### Nedir bu flash loan?... 

Normalde kredi aldığınızda karşılığında teminat verirsiniz. DeFi'daki kredi platformlarında da benzer şekilde işliyor:  Verdiğiniz teminatın değeri tipik bir DeFi işleminde aldığınız kredi tutarının yaklaşık 1.5 katı kadar olur... **Flash loan ise teminatsız kredi çekmek, yani herhangi bir teminat göstermeden çok kısa süreli kredi kullanmak demek** 

Nasıl oluyor bu? Şu şekilde: Normalde klasik dünyada al-sat yapanlar gün içinde onlarca yüzlerce işlem yaparlar, gün sonunda da bunların hepsini bir araya getirir ve pozisyon kapatılar.. Yani işlemlerin nihayetlendirilmesi gün sonunda olur.. Hatta hesaplaşma (settlement) birkaç gün sürer.. 

DeFi'de ise her işlem çok hızlı.. Malum dijital dünyadayız.. Milisaniyeleri konuşuyoruz.. Buna paralel olarak hesaplaşma da  günler sürmüyor ama hemen belirtelim anlık da olmuyor: Yapılan işlemlerin kaydını bildiğiniz gibi blokzincirler tutuyor.. Blokzincir ise binlerce makinenin bir arada uyumlu çalışmasını gerektiren bir sistem.. Bu kayıtlar anlık olarak değil, bloklar halinde bir araya getirilip kesinlik kazandırılıyor.. Bu da Bitcoin'de 10 dakikada bir, Ethereum'da ise yaklaşık 15 saniyede bir oluyor.. 

Dolayısıyla, siz bir işlem yaptığınızda o işlemin gerçekleşmesi için en az 15 saniye gerekiyor (ki tam kesin olarak emin olmak için üzerinden ciddi sayıda blok geçmeli ki sonradan değiştirilemez hale gelsin - o ayrı bir konu)... Siz bir işlemi başlatır ancak 15 saniye içinde sonlandırmazsanız işlem geçersiz oluyor..  Klasik dünyada bir-iki gün süren hesaplaşma burada 15 saniye içinde gerçekleşiyor. 

İşte flash loan,  klasik dünyada gün içinde yapılan bir sürü işlemi DeFi dünyasında 15 saniyeye sığdırmayı sağlayan bir kredi. Şöyle yapıyor kullanıcı. Bir DeFi servisini kullanarak **kredi alıyor**, sonrasında bunu başka DeFi servislerinde **arbitraj işlemlerinde** kullanıyor, sonra 15 saniye içinde krediyi **geri ödüyor** (ekstra bir miktar faiz ve ücret ödeyerek).. Dolayısıyla işlem blokzincire yazılmaya gerek olmaksızın sonlanıyor.. Kullanıcının diğer arbitraj işlemlerinden kazandığı paralar yanına kâr kalıyor.. Zarar eden kim? Kullanıcının işlem yaptığı diğer DeFi hizmetlerine likidite sağlamış olan yatırımcılar.. En basit anlatımı bu şekilde (ki farklı daha karmaşık versiyonları da mevcut)... 

Peki ya kullanıcı işlemleri zamanında bitiremez ya da zarar ettiği için flash loan kredisini geri ödeyemez ise? O zaman büyük bir sorun yok. Zira henüz 15 saniye geçmeden kredi veren krediyi geri çağırıyor ve blokzincire işlemi yazmıyor.. 

Hemen hatırlatalım bu işlemleri yapanlar öyle elleri çok hızlı hareket eden al-sat'çılar değil. Bunlar daha çok, bu işlemleri hızlı ve koordineli bir şekilde yapmayı sağlayacak akıllı kontratları yazan geliştiriciler.. Hem finans hem de kodlama bilgisine sahip insanlar... 

| ![robot_human](/assets/brain-5814961_800.jpg)|
|:--:| 
| *Image by [Gerd Altmann](https://pixabay.com/users/geralt-9301/) from [Pixabay](https://pixabay.com/)*|

#### Suç Flash Loan'da mı?

Tabii, burada flash loan olayına odaklanmak aslında suçluyu başka yerde aramak oluyor. Asıl bakılması ve suçlanması gerekenler, böyle bir arbitraja imkan veren diğer DeFi servisleri. Nasıl arbitraj imkanı doğuyor? Kim bu diğer DeFi servisleri?. Her durum farklı ama bir örnek ile açıklayalım: 

Genelde size işlem yaptıracak olan DeFi servisleri işlem yapacağınız token ile ilgili olarak fiyat bilgisini bilgi sağlayıcı oracle servislerinden alırlar (bu konuda oracle nedir ile ilgili şu yazımızda, bu oracle hizmet verenlerin en büyüğü olan Chainlink ile ilgili de şu yazımızda daha detay bulabilirsiniz). 

Oracle servisleri manipülasyon olmaması için bilgiyi birçok farklı yerden alıp damıtır ve ihtiyaç sahibine verirler. Kimi DeFi servisleri ise gerek maliyet gerekse gerekli insan kaynağı olmadığı için bu oracle servislerini kullanmak yerine  bir-iki kaynaktan (örneğin bir merkeziyetsiz borsadan) bilgi alırlar. 

İşte arbitraj yapanlar böyle bir durum gördüklerinde aynı avını bekleyen kaplanlar gibi tetiğe geçerler. Likiditenin azaldığı manipülasyon yapılacak uygun zamanda flash loan aracılığıyla kredi çeker, bu kredi ile gider o borsada işlem yaparak token fiyatını oynatır, bu oynayan fiyatı referans olarak kullanan DeFi servisinde işlem yaparlar.. İstedikleri kârı elde ettikten sonra da ilk aldıkları krediyi kapatırlar Ve bütün bunları bir blok kapanmadan 15 saniye içinde bitirirler!.. (Karmaşık görünüyor ama dip not'ta Şubat 2020'de yaşanan olayı adım adım rakam ve borsa adları ile bulabilirsiniz). 

'Bir başka deyişle, flash loan isteyen herkesi bir balina haline getiriyor' - [Nikola Jankovic](https://www.bloomberg.com/news/articles/2021-02-07/flash-loans-are-providing-instant-cash-to-crypto-speculators) (DeFi Saver - flash loan sağlayıcısı bir servis). 

| ![flash](/assets/sea-4741178_800.jpg)|
|:--:| 
| *Image by [DarkmoonArt_de](https://pixabay.com/users/geralt-9301/) from [Pixabay](https://pixabay.com/)*|

Tabiri caiz ise: **Herhangi bir DeFi ürününde açık bulan biri, flash loan kullanarak, eline geçirdiği büyük güç ile bu üründeki açığı sonuna kadar sömürüyor**

2020 yılı içinde yaşanan onbeş DeFi saldırısının dokuz tanesinde flash loan kullanılmış, bunlardan beşinde yukarıdaki 'bilgi sağlayıcının manipüle edilmesi' yöntemi kullanılmış. (Detaylı listeyi TheBlock Crypto'nun hazırladığı [Digital Asset 2021 Outlook](https://www.theblockcrypto.com/post/88463/2021-digital-asset-outlook) raporunda bulabilirsiniz.) 

### Yasak mı Flash Loan'lar? Hayır, tam tersi bu hizmeti verenler var... 

Flash loan hizmeti veren en büyük DeFi servisi Aave.. 2020 yılı içinde 2 milyar ABD Doları'ndan fazla bir miktarı flash loan olarak veren Aave, bir keresinde tek işlemde bir kullanıcısına [200 milyon ABD Doları flash loan kredisi sağlamış](https://www.bloomberg.com/news/articles/2021-02-07/flash-loans-are-providing-instant-cash-to-crypto-speculators).. Bunun dışında daha kompleks flash loan işlemleri yapan [DeFi Saver](https://defisaver.com/) [Collateral Swap](https://collateralswap.com/) gibi servisler de mevcut. Hatta kodlama bilgisi olmayanlar için sürükle-bırak şeklinde akıllı kontrat yaratabilecekleri [Furucombo](https://furucombo.app/) adında bir servis bile bulunmakta. 

### Gerçekten önlemek gerekli mi?
Basında 'hack' olarak bahsedilen flash loan olayı, aslında piyasanın daha düzgün işlemesini sağlayan bir enstrüman. Zira, likidite azlığı ya da manipülasyon nedeniyle farklı borsalar arasında doğan fiyat farklarını azaltmaya yarayan bir arbitraj aracı aslında. 

Burada bu aracı kötü niyetli kullanan kişiler olabiliyor. Bu kişiler birbirinden bağımsız hareket eden ve koordineli çalışmayan borsalardaki düzensizliği fırsat bilip arbitraj yapmanın ötesinde, manipülasyon yaparak arbitrajı yaratıyorlar. Piyasada kendiliğinden oluşan bir arbitrajı değerlendirmek normal (herkes bunu alkışlar) ancak piyasaları manipüle ederek arbitrajı bizzat yaratmaya gelince orada görüşler farklılaşıyor. 

Buna "burası serbest piyasa, isteyen istediğini yapar, buna olanak veren platformların hatası" diye bakanlar da var, bunun piyasanın henüz emekleme aşamasında olmasını fırsat bilen piyasayı öldürmek pahasına fayda kazanmaya çalıştığı kötü niyetli hareketler olarak görenler de.. Karar sizin.. 

### Sonuç
Flash loan krediler, teminatsız kredi olanağı verdikleri için DeFi alanında çok farklı fırsatlar yaratabilirler. Bu fırsatları biz son kullanıcılardan daha çok kodlama ve finans alanındaki ekiplerin kullanması daha olası.. Arbitraj imkanı ile zararsız olarak kullanılanlar piyasaları daha efektif hale getireceği için faydalı olabilir. Zararlı olarak nitelendirebileceğimiz manipülatif hareketler ise emekleme aşamasındaki bu piyasalarda hizmet verenleri 'seni öldürmeyen güçlendirir' prensibi ile daha kurşun geçirmez hale getirebilirler. Klasik dünyada hiç göremeyeceğimiz farklı sorunlar ve fırsatlar DeFi ile önümüze geliyor. Yeni bir dünyanın kapıları önümüzde yavaş yavaş aralanıyor, bakalım arkasından neler çıkacak?.. 

--

*Teknik Dipnot:*
18 Şubat 2020 tarihinde BzX borsasında gerçekleşen işlem şu şekilde oldu 

1. Kullanıcı (ya da Hasım), bZx platformundan 7,500 ETH borç alır. 
2. Aldıkları bu borç para ile gidip Uniswap ve Kyber platformlarındaki sUSD/ETH havuzlarında yaklaşık 4,400 civarı ETH verir ve karşılığında 1.1 milyon sUSD satın alırlar. Sığ bir havuz olduğu için normalde diğer piyasalarda 268 olan ETH/sUSD kuru bu alım sonrası bu iki havuzda yaklaşık 107'e düşer.(BzX'in borç verme platformu platformu ETH/sUSD için referans olarak Uniswap ve Kyber borsalarının bu iki havuzunu kullanıyor)  
3. Sonra aldıkları sUSD'yi götürüp bZx'de teminat veriyorlar ve karşılığında 6,800 ETH flash loan borç alırlar (%150 teminat istendiği için 1 ETH = 107 x 1.5 = 163 sUSD kurundan).  
4. Gidip bu aldıkları borç ile ilk işlemdeki borçlarını öderler.  
5. Üçüncü işlemde aldıkları krediyi de ödemezler.   
6. Sonuç:  
- Hasım, aldığı kredinin 4,400 ETH'lık kısmını kullanıp karşılığında 6,800 ETH aldı. Kârı 2,400 ETH 
- BzX borsası üçüncü adımda verdiği krediden dolayı zarar etti. Zira, 1,1 milyon sUSD aldılar ama verdikleri kredi 6,800 ETH idi. Piyasaya gidip ETH almak istediklerinde 1.1 milyon /268 = 4,100 ETH alabilecekler.. Kalan 4,700 ETH'yi bZx'e para vermiş yatırımcılar zarar olarak yazıyorlar.  

Daha da detay arzu ederseniz [şu araştırma raporunun - pdf](https://arxiv.org/pdf/2003.03810.pdf) 8. Sayfasına bakabilirsiniz. 
