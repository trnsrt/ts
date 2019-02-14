---
layout: post
title:  "MakerDAO kredi kullanımında çığır açar mı?"
date:   2019-02-15 12:42:56 +0300
categories: Genel
---



Önceki [yazımızda](/genel/2019/02/14/Blockchain-finans-dunyasini-nasil-etkileyecek.html) finans dünyasında yeni başlayan DeFi hareketine değinmiş ve para transferi ile başlayan aracılık hizmetlerinin makinelere aktarılması işinin daha başka hangi alanlara yayılabileceğine değinmiştik. İşte karşınızda bu alanlardan ilki olan kredili işlemlerin en yaygın kullanılanı MakerDAO.. 

### MakerDAO nedir?


![makerdao-dai.png](/assets/makerdao-dai.png) 


MakerDAO kişilerin ellerinde duran KriptoParaları teminat verip bu teminat karşılığı sistemin parası olan DAI'yi yaratmalarına olanak veren bir dağıtık bir sistem. Ethereum üzerinde kurulu Akıllı Kontratları kullanılıyor bunu yapmak için. 

Dai nedir peki? Dai bir ABD Dolarına eşit olan bir SabitPara. SabitParaların ne olduklarına şu iki yazımızda ("[Orası çok dalgalı, sakin sulara gel](https://ademimerkezi.com/genel/2018/07/20/Orasi-cok-dalgali-sakin-sulara-gel-sabitparalar.html)" ve "[SabitParalara devam](https://ademimerkezi.com/genel/2018/07/27/sabitparalara-devam-digerleri.html)") değinmiştik. (Dai kelime anlamı olarak Çince'de [borç para vermek](https://www.reddit.com/r/MakerDAO/comments/5q98b1/%E8%B2%B8_dai/) anlamı taşıyor bu arada)

#### Nasıl çalışıyor? 
Elinizdeki KriptoPara'yı (şu an için yalnız Ethereum parası ETH geçerli) teminat olarak gösteriyorsunuz, buradaki deyişiyle ETH'lerinizi sistem içine kilitliyorsunuz. Gönderdiğiniz her 150 birim para için 100 birime kadar Dai yaratabiliyorsunuz. Sonrasında bu DAI'yi istediğiniz noktada borsada bire bire yakın bir değerden ABD Doları'na çeviriyor ve kullanıyorsunuz. Bu para için bir maliyet ödüyorsunuz, sonrasında ise dilediğiniz noktada tekrar Dai satın alarak yok ediyor ve ETH'nize geri kavuşuyorsunuz. 

#### Neden insanlar kullanıyor? 
Diyelim ani olarak paraya ihtiyacınız var, mevcut paranızı da ETH'ye yatırdınız. ETH'nin yükseleceğini düşünüyorsunuz ya da başka herhangi bir nedenle ETH'lerinizden ayrılmak istemiyorsunuz. Bu sistemi kullanarak hem nakit ihtiyacınızı karşılayabilir hem de ETH'nin getireceği kardan yararlanabilirsiniz. 

#### Kredi maliyeti ne? 
Şu anda inanılmaz ucuz. Yıllık 0.5% bir faiz maliyeti var (buna stabilize ücreti deniyor ve bu ücreti ayrı bir para ile ödüyorsunuz ama şu aşamada çok da gerekli değil bunu bilmek - en altta notta teknik detayı var). 

&nbsp;

| ![money-exchange.gif](/assets/money-exchange.gif) | 
|:--:| 
| *Yıllık %0.5 maliyet mi? Ver, hepsini ver...  (Kaynak: [Giphy](https://media.giphy.com/media/6nXIRmdkjett6/giphy.gif))* |

&nbsp;

#### Ya ETH çok düşer de teminatımın altına inerse? 
Buna dikkat etmek gerekiyor işte. Zira ETH'nin değeri düşerse ekstra ETH yüklemeniz yapmanız lazım. Ya da baştan ihtiyacınız olan nakitten daha fazla ETH koymakta fayda var. Aksi takdirde sistem ETH'nizi "bozuyor" ve %13 gibi bir ceza sonrası kalan paranızdan borcunuzu düşüp size geri veriyor. 

Şu anda sistemde kilitli tutulan teminat rakamının kullanılan krediye oranının yaklaşık %200 olduğunu görüyoruz. Yani insanlar gerekli minimum limit olan %150'nin üzerine bir %50'lik bir ekstra teminat koymuşlar kullandıkları krediler için.

#### Kim borç veriyor bu sisteme?
Aslında kimse kimseye borç vermiyor. Siz elinizdeki ETH'yi teminat gibi kullanıp Dai yaratıyorsunuz. Buradaki soru şu olabilir? Dai'yi satıp ABD Doları aldınız. Kime satıyorsunuz Dai'yi? Genel olarak SabitPara kullanmak isteyen insanlara (ya da daha önce kredi almış ve şu anda borcunu kapatmak için Dai almak isteyenlere). Neden SabitPara kullanmak ister insanlar konusunu daha detaylı önceki yazılarımızda [incelemiştik]((https://ademimerkezi.com/genel/2018/07/20/Orasi-cok-dalgali-sakin-sulara-gel-sabitparalar.html)). 

#### Dai parası nasıl sabit kalıyor peki?
Dai, bir ABD dolarına sabitlenmiş. Ama alım satım yapıldığı borsada baktığınızda fiyatı aşağı ya da yukarı gidebiliyor. MakerDAO yaratıcıları fiyatın iniş ve çıkış olduğu durumda tekrar 1 ABD dolarına gelmesinin otomatik olacağını düşünüyorlar. Şöyle ki:

Diyelim, Dai fiyatında bir düşüş oldu. Böyle bir durumda geçmişte Dai yaratıp borç almış olanlar, aldıkları borcu yine Dai ile ödeyecekleri için kredilerini ucuza kapatma fırsatı bulabilecekler ve Dai satın alacaklar. 

Aynı şekilde Dai fiyatında bir artış olduğunda (1 ABD dolarından daha yüksek bir fiyata geldiğinde) insanlar ellerindeki ETH'leri sisteme gönderip 1 ABD doları karşılığı olacak şekilde Dai yaratacak ve bu Dai'yi piyasada 1 ABD Doları'nın üzerinde bozdurma şansı yakalayacaklar.  Bu da piyasada 1 Dai'nin 1 ABD Doları'na yaklaşmasını sağlayacak. 

![DAI_ETH_karsilastirma_USD.png](/assets/DAI_ETH_karsilastirma_USD.png)

Bunun yanında Dai fiyatında ekstrem bir düşüş olduğu durumlar için de acil durum senaryoları hazırlanmış ama şu aşamada çok teknik kaldığı için ilgilenenleri [White Paper]((https://makerdao.com/en/whitepaper/))'ı okumaya davet ederek konuyu kapatıyoruz. 

### Peki başarılı olmuş mu MakerDAO?

MakerDAO tamamen otomatik bir sistem. Arada herhangi bir aracı yok. Karmaşık anlaşmalar yok - kağıt imza vs yok. Sistem tamamen kodlanmış makineler aracılığıyla işliyor. Teminatınızı koyuyorsunuz, paranızı alıyorsunuz. Teminatınız %150'nin altına düşerse de ETH'niz bozduruluyor ve kredi borcunuzun üzerindeki teminatınız hesabınıza yatıyor. Bu nedenle kredi vermenin getirdiği kağıt ve bürokrasi masrafından kurtulma sistemin en önemli avantajlarından biri. 

Şu ana kadar iyi gittiklerini söylemek mümkün. Zira halihazırda iki milyon ETH'e yakın miktar MakerDAO sistemi üzerinden borçlandırılmış (CDP - Collaterized Debt Positions). ETH'nin şu aralar 120 ABD Doları civarında olduğu düşünülürse yaklaşık 240 Milyon ABD doları bir rakama denk geliyor bu. Ethereum'un kullanım olarak en işlevsel platformlarından biri MakerDAO. 

Sistem şu ana kadar sıkıntı yaşamadan ilerledi. ETH sene içinde çok ciddi değer kaybetti ama buna rağmen Dai'de ciddi bir sıkıntı olmadı. Bu ileride de olmayacak anlamına gelmiyor tabii. O da bunun riski. ETH'nin aniden %33'değer kaybetmesi durumunda 150 birimlik teminatlar 100 birime düşebilir ve sistem bu ETH'leri satana kadar kredi miktarının altına da inebilir. (şu an %200 olması biraz daha sistemi rahatlatsa da). Şu an için MakerDAO sistemi daha çok küçük - ama çok daha büyümesi durumunda tüm ETH değerini bile etkileyecek hale gelebilir olası ani düşüşler. 

### MakerDAO her derde deva mı?

![swiss-army-knife-400.jpg](/assets/swiss-army-knife-400.jpg)

Tabii ki hayır. Ancak, bir ürünü ne kadar basit ve istisnaları dışarıda bırakarak şekillendirirseniz o kadar otomatik (insan eli değmeden) yürütebilirsiniz tezine güzel bir örnek. Şu anki rakamlar cesaret verici olsa da ileride gerçekten finans piyasalarını sarsıcı bir devrim haline dönüşür mü? Bunu şimdiden tahmin etmek oldukça zor. Neden?

Öncelikle, kriz anlarında test edilmiş bir ürün değil. Test edebilmenin tek yolu da ancak bir kriz yaşamaktan geçiyor - tabii ki stres test benzeri çalışmalar var ama hiçbiri kriz anında ne olacağını tam gösteremiyor. Yukarıda da yazdığımız gibi ETH 2019 yılında değer kaybetti ve MakerDAO'ya hiç bir sıkıntı yaratmadı bu durum. Peki ya ani düşüşler?

En büyük konulardan biri de teminat miktarı. Oldukça yüksek. Ama başta da yazdığımız gibi kredi sisteminin en masraflı ve karmaşık yonlerinden biri kredi derecelendirme ve geri ödememe oranları. Basitlik en başta bu iki özelliği budamaktan geliyor. Tabii ki bunun bir karşı maliyeti olacak, o da yüksek teminat oranları. 

### MakerDAO için sonraki adımlar neler?

MakerDAO özelinde baktığımızda sonraki adımlarda, sistemin organik olarak büyümesi var. Halihazırda tüm ETH miktarının %2'si MakerDAO sistemine kilitlenmiş durumda - bu da onu Ethereum sisteminin en büyük oyuncularından biri yapıyor. Ancak MakerDAO sadece ETH ile işler diye bir kural yok. Başlangıç noktaları bu ancak diğer altyapı protokolleri ile de çalışabilmek onları daha geniş kitlelere yayacak. 

Bunun yanında sistemin daha geniş kitlelere yayılması için aslında farklı yatırımcıların ihtiyaçlarına hitap edecek çözümler üst seviye olarak ortaya çıkabilir (bir nevi Bitcoin üzerine ödemeleri hızlandırmak için kurulan Lightning Network gibi). Örneğin kredi derecelendirmesi gibi daha karmaşık çözümler. Ve bu çözümler merkezi yapılar da olabilir - zira karmaşık çözümler için merkezi yapılar daha efektif olabiliyor. Dolayısıyla altta merkezi olmayan ve bunun getirdiği kolaylıklardan yararlanan ama üstte daha karmaşık isteklere hitap eden merkezi yapılar (DeFi -Decentralized Finance- üzeri CeFi -Centralized Finance-)  ilginç açılımlar getirebilir. Tanner Hoban'ın şu [yazısı](https://medium.com/@tehoban/defi-constructing-the-foundation-of-a-new-microeconomy-cb7f21f1c6dd) bu anlamda çok daha detaylı bilgi veriyor ilgi duyanlara. 

### Sonuç

MakerDAO kısa sürede kat ettiği aşama ile büyük bir potansiyel gösteriyor. Büyümesi sürerken yol üzerinde ufak tefek kazalar geçirmesi de olası - ancak ilk yıllarını kazasız bir şekilde atlattılar. Merkezi bir aracıya ihtiyaç duymadan finans dünyasının farklı bir alanında gösterdikleri başarı onları uzun vadede dikkatle izlenmesi gereken girişimlerden biri yapıyor. 

---

&nbsp;

Not: Teknik olarak çok detaya girmedik ancak DAI dışında MakerDAO'nun bir parası daha var o da MKR. DAI'yi sistemin parası, MKR'yi ise sistemin sermayesi (equity) olarak düşünebiliriz. Para alışverişleri DAI ile yapılırken ve DAI ABD Dolarına sabitlenmiş bir para iken, bu para üzerindeki faiz MKR üzerinden ödeniyor. MKR sahibi olanlar aynı zamanda sistemin yönetiminde söz sahibi oluyorlar - örneğin teminat oranlarının belirlenmesi ya da sistemdeki ani düşüşlerde çalıştırılacak mekanizmaların prensiplerinin belirlenmesi gibi. Bu arada olası bir kriz durumunda MKR bir nevi acil durumda kırılacak cam gibi de çalışıyor. Eğer teminat rakamları kredi rakamlarını karşılamaz ise o zaman açık MKR bozularak karşılanıyor - bu da MKR için olumsuz bir durum. Dolayısıyla MKR sahipleri ellerindeki değer azalmasın diye teminat oranı vb rakamlarda olabildiğince konservatif davranmak zorundalar. Bir nevi sistem bu alanda da bir otokontrol getiriyor. 

---

&nbsp;

*Not: Yazdığımız 45+ yazının bir bütünlük içinde nelerden oluştuğuna bakmak isterseniz [Hakkımızda](http://ademimerkezi.com/about/) sayfasına göz atabilirsiniz.*

