---
layout: post
title:  "Bitcoin yarılandı, sırada ne var?"
date:   2024-04-22 12:17:56 +0300
categories: Genel
tags: Yazılar, DeFi
---


Bu yazımızda, geçtiğimiz günlerde yaşanan Bitcoin yarılanması sonrası Bitcoin ekosistemini bekleyen önemli gelişmelerden biri olan Runes standardından bahsedeceğiz. 


### Önce bir 'yarılanma' nedir ona bakalım
Bitcoin sistemi uzun süredir konuşulan yarılanma olayını 19 Nisan'ı 20 Nisan'a bağlayan gece yaşadı. Neydi olay, kısaca özetlersek: Bitcoin yazılımı, ağın devam etmesi için çalışan madencileri emekleri karşılığı ortalama olarak her 10 dakikada bir ödüllendiriyor. Bu ödül aynı zamanda yeni bitcoinlerin yaratılması, yani dolaşımda var olan bitcoinin artması demek (bir başka deyişle Bitcoin'in enflasyonu). Satoshi Nakamoto, başlangıçta daha fazla kullanıcıyı özendirmek amacıyla bitcoinleri bol bol ödül olarak vermiş (blok başına 50 BTC). Planı, bitcoin arzını yıllar içerisinde kademeli olarak azaltmanın bitcoin değerini yükseltmesine dayanıyordu. Verilen ödül dört yılda bir yarıya iniyor ve bu durum 'yarılanma' olarak adlandırılıyor (ingilizcesi 'halving'). İşte geçtiğimiz hafta yaşadığımız bu yarılanmaların dördüncüsü idi ve her on dakikada bir verilen ödül miktarı 3,125 BTC'ye düştü.

Bu neden önemli ve bu kadar çok konuşuldu? Temel nedeni, geçmiş yarılanmalarda bitcoin fiyatının büyük değişiklikler göstermiş olması. 'Tarih tekerrürden ibarettir' diyenler bu olaya büyük önem atfediyorlar. Teknik olarak yarılanmanın getirdiği tek farklılık, piyasaya girecek yeni bitcoin miktarının azalıyor olması. Madenciler verilen ödülü kazanabilmek için büyük bir enerji sarfediyorlar ve bu enerji maliyetini karşılayabilmek için kazandıkları BTC'leri satmak zorunda kalıyorlar. Bu da sistem üzerinde sürekli bir satış baskısı oluşturuyor. Ödülün yarıya düşmesi, satış baskısının da azalması anlamına geliyor. 

Şahsi fikrimi soracak olursanız, 'yarılanma' artık yavaş yavaş magazinsel bir olay haline gelerek önemini yitirmeye başlıyor. Neden? Birincisi, eski yarılanmalarda hem piyasaya çıkan yeni bitcoin miktarı hem de yarılanma ile azalan rakam çok büyük idi (En başta yıllık 2.6 milyon olan BTC artışı son yarılanma sonrası yıllık 0.16 milyon BTC’ye düşüyor). İkincisi, yarılanma sırasında dolaşımda olan yani etkilenen miktar. İlk yarılanma öncesi piyasada sadece 10.5 milyon BTC vardı. Şimdi ise son yarılanma öncesi piyasada 19.4 milyon BTC var (Başka bir deyişle toplam 21 milyon BTC'nin %93.7'i zaten çıkmış durumda). Yani artık hem havuz daha büyük hem de havuza giren yeni para miktarı daha küçük, dolayısıyla etki daha sınırlı. Bu durum, gelecek yarılanmalarda daha da küçülmeye doğru gidecek. Zaten 2038 yılında toplam Bitcoin'in %99'u çıkmış olacağı için herhalde çok daha az kişi 'yarılanma' olayından bahsediyor olacak. 

Yarılanma olayı en çok madencileri etkiliyor. Öyle ya, aldıkları ödüller bir anda yarıya iniyor. Peki madenciler isyan edip işi bırakırlarsa? Merak etmeyin. Böyle bir durum söz konusu olmaz. Azalan ödüller nedeniyle özellikle yüksek maliyetli madencilerin sayısında bir azalma olabilir. Bu normal ve Bitcoin sistemini etkilemez. Sistem, kendi içinde zorluk derecesini azaltır, kalan madenciler daha fazla bitcoin kazarlar ve bir yerde tekrar denge bulunur. Diğer bir konu ise, verilen ödüller madencilerin para kazanmasının sadece bir yolu. Bir diğer yol ise, Bitcoin sisteminin üzerindeki işlemler üzerinden komisyon kazanmak. Bitcoin ağı daha fazla kullanıldıkça madencilerin gelirleri de aynı oranda artıyor. 

İşte bugünkü asıl konumuz, Bitcoin sisteminin daha fazla kullanılmasını ve daha fazla madenci geliri yaratılmasını sağlayacak olan yeni bir standart üzerine olacak: Runes. 


### Nedir Runes?

Runes, Bitcoin üzerinde token yaratabilme olanağı tanıyan yeni bir standart. Ne demek tam olarak bu? Gelin farklı örneklere bakarak anlamaya çalışalım. 

Geçmiş dönemde, Bitcoin topluluğu 'sansür edilemeyen bir dijital para (ya da dijital altın)' olmaya odaklanıp başka her tür yeniliğe sırt çevirince, bu alandaki liderlik bayrağını Ethereum topluluğu almıştı. Ethereum üzerindeki projeler, kendilerine ait payları topluluk ile paylaşmak için token çıkarmaya başladılar. Ethereum sistemini işleyen makinelerin bu tokenleri anlayabilmesi için belirli bir standart içermesi gerekiyordu. İşte bu anlamda aynı bir para gibi birbiri ile değiştirilebilen (ingilizcesi 'fungible') tokenler için ERC-20 adında bir standart yaratıldı. Buna paralel, birbirine benzemeyen tokenler (bir başka deyişle NFT'ler) için ise farklı standartlar oluşturuldu (ERC-721- ERC-1155 gibi). 

Peki Bitcoin üzerinde benzer standartlar kurulamaz mıydı? Kurulabilirdi tabii. Sonuçta Bitcoin izin gerektirmeyen bir ağ. İsteyen bir cüzdan ile ağa bağlanabilir. Sorun şu ki, siz isteseniz bile teknik olarak Bitcoin, Ethereum gibi üzerinde geliştirme yapılmaya olanak veren bir ağ değil. 

İşte, Bitcoin'in bu durağan yapısından sıkılan bir kişi, geçtiğimiz yıl son Bitcoin güncellemesi olan Taproot'u kullanarak Bitcoin'i tekrar eğlenceli hale getirmeyi başardı. Ordinals adı verilen bir standart ile, Bitcoin ağı üzerine NFT yazılması ve bu NFT'lerin alınıp satılmasını sağladı. Ordinals oldukça başarılı bir standart olarak, Bitcoin üzerindeki işlem gelirlerini ciddi bir oranda artırdı. 

| ![bitcoin-islem-ucretleri](/assets/bitcoin-ordinals-islem-ucretleri.png)|
|:--:| 
| *Bitcoin sisteminde ödenen işlem ücretleri (kırmızı ve gri olanlar ordinals standardı kullanılarak yapılan işlemlere ödenen ücretler). Normal transferler hâlâ yüksek olsa da, kimi dönemlerde BRC-20 işlemlerin ciddi artış gösterdiği görülüyor. Kaynak: [Dune Analytics @cryptokoryo](https://dune.com/cryptokoryo/brc20)*|

Ordinals'ın başarısı sonrası, aslında NFT'ler için yaratılmış bu standardı değiştirilebilir tokenlere uyarlayan bir dizi standart daha ortaya çıktı. Bunlar içinde en tutulanı Ethereum'un ERC-20'sinden esinlenerek isimlendirilen BRC-20 standardı oldu. Oldu olmasına ama bu standartlar henüz çok kabul görmüş değiller. Bunun iki temel nedeni var: Birincisi, Ordinals'ın NFT'ler için tasarlanmış olması ve normal tokenler için kullanıldığında işlem maliyetlerinin yüksek olması. İkincisi ise, BRC-20 standardını ortaya çıkaran kişinin konuyu bir taslak olarak ortaya atıp bırakması ve devamını getiren kişilerin farklı farklı versiyonlar üretmesi nedeniyle gerçek bir standardizasyon sağlanamaması.

İşte yukarıda saydığımız tüm bu olayların ardından, Ordinals protokolünü yazan kişi sadece değiştirilebilir tokenlerin kullanımına uygun sıfırdan yeni bir standart yazarak topluluğun hizmetine sundu. Casey Rodarmor isimli bu geliştiricinin yarattığı Runes standardı, Bitcoin'in yarılanması ile birlikte dolaşıma girdi. 

Şimdi gelin teknik olarak Runes nedir, nasıl çalışır, Ordinals ve BRC-20 standardın farkı nedir konularına bakalım. (Teknik olarak nasıl çalıştığına ilgi duymuyorsanız, bir sonraki bölümde ne gibi açılımlar getirdiği konusuna atlayabilirsiniz.) 

### Peki teknik olarak Runes nedir? Nasıl çalışır?
Runes'un nasıl çalıştığını anlayabilmek için önce Ordinals'ın nasıl çalıştığına bakmak gerekiyor. 

#### Ordinals
Ordinals, Bitcoin üzerinde herhangi bir güncelleme gerektirmeden NFT yaratılmasını sağlayabilen bir standart. Nasıl çalıştığını anlayabilmek için Bitcoin'in çalışma sistemini bilmek gerekiyor. Bitcoin sistemi, daha çok bilinen Ethereum sisteminden farklı bir şekilde çalışıyor. 

Ethereum hesap sistemi ile çalışır. Kullanıcıların sahip olduğu hesaplar ve bu hesaplarda duran token bakiyeleri Ethereum sisteminde tutulur. Bir kullanıcı diğerine bir token transfer ettiğinde, her iki hesabın da bakiyeleri değişir ve sisteme işlenir. Bu ve benzeri daha pek çok işlem, Ethereum sisteminin akıllı kontratlar dediğimiz küçük kod parçacıklarını çalıştırması sayesinde olur. 

Bitcoin sisteminde ise akıllı kontrat yok, onun yerine bitcoin parası BTC ve onun en küçük hali olan satoshiler var (her bir BTC içinde 100 milyon satoshi var). Sistem sadece bu paraların bakiye toplamı ve transferine odaklanmış. Bir örnek verelim. Klasik bir cüzdan içinde bulunan banknotları düşünelim. Diyelim 23 TL'lik bir ödeme yapacaksınız. Cüzdanınızda ise bir 20 TL bir de 10 TL var. Satıcıya bu iki banknotu verir ve geriye 7 TL alırsınız. Bitcoin'de de herhangi bir transfer yapmak istediğinizde, sisteme cüzdanınızda bulunan bu banknotlardan (teknik terimi UTXO, İngilizce 'Unspent Transaction Output' yani harcanmamış işlem çıktısı) bir kısmını gönderirsiniz. Sistem bu banknotların tümünü yakar, göndermek istediğiniz para kadar banknot yaratıp karşı tarafın adresine, paranın üstünü ise sizin adresinize gönderir. 

Ordinals sistemi, Bitcoin üzerindeki en küçük para birimi olan satoshilerin her birine tekil bir ID numarası vermek yöntemi ile çalışıyor. Böylece, aslında paranın doğal bir niteliği olan birbiri ile değiştirilebilir olması özelliğini değiştiriyor. Bunu, banknotun parasal karşılığının yanında seri numaralarına da bakmak gibi düşünebilirsiniz. 

Siz elinizde tuttuğunuz bir satoshiyi başkasına devrederek onun sahipliğini de devretmiş oluyorsunuz. OK, çok güzel, ama satoshinin içinde ne var ki devrediyoruz? 

İşte burada, Bitcoin üzerinde yapılan son güncelleme olan Taproot devreye giriyor. Normalde, Bitcoin üzerinde herhangi bir işlem yaparken, yaptığınız işlem emrinin içine çok kısıtlı miktarda bilgi girebiliyordunuz. Bu verdiğiniz emir ve içindeki bilgi, bir daha değiştirilemez şekilde ağ üzerinde sonsuza dek saklanıyor. Taproot (ve bir başka güncelleme olan Segwit) güncellemesi içindeki bir açık sayesinde emir içine konabilecek bilgi miktarı 4 MB'e kadar çıktı. İşte bu güncelleme sayesinde, tüm bir bitcoin bloğunu kaplayabilecek kadar veriyi örneğin bir jpeg dosyasını Bitcoin ağı üzerinde saklayabiliyorsunuz. 

Ordinals NFT'leri de işte bu mantık ile çalışıyor. Yaratılan bir NFT'nin her bir parçası veri olarak birer satoshi içine gömülüyor (ingilizcede buna inscribe deniyor, gömülen dataya da inscription adı veriliyor). Ordinals sistemi her bir satoshi için tekil bir ID numarası yaratıyor. Sonra bu ID'leri içeren satoshilerin transfer edilmesi ile Ordinals NFT'leri de el değiştirebiliyor.

Ordinals sisteminin sadece NFT'ler için geliştirilmiş bir sistem olduğunu yukarıda belirtmiştik. Bu nedenle klasik anlamda para olarak görülen değiştirilebilir tokenler için kullanıma uygun değil. Ordinals üzerine yazılan BRC-20 gibi standartlar onu para için kullanılabilir hale getirmeye çalıştılar. Gelin şimdi de BRC-20'ye bakalım: 

#### BRC-20
BRC-20, ordinals standardını değiştirilebilir token olarak uyarlamaya çalışan bir standart. Nasıl çalıştığını anlamak için öncelikle nasıl yaratıldığını anlayalım: 

BRC-20, çok basit olarak bir token yaratılması için gerekli olan üç temel fonksiyonu standardize ediyor. Bunlar i) tokenin bilgilerinin (ticker'i ne, kaç adet basılacak gibi) ilk olarak sisteme yüklenmesi (İngilizce deploy), ii) tokenin yaratılması (ingilizcesi mint) ve iii) tokenin transfer edilmesi. Bu üç fonksiyon belirlendikten sonra satoshi transferi içindeki işlem emirlerine yazılarak işlemler gerçekleştiriliyor. 

Yukarıdaki üç işlemden “transfer işlemi” en çok kullanılanı, o nedenle bunu biraz daha açmakta fayda var. Diyelim elinizde BRC-20 standardıyla yaratılmış bir token olan ORDI tokenden 300 tane var ve bunun 100 tanesini bir arkadaşınıza göndermek istiyorsunuz. Bunun için iki tane bitcoin (ya da satoshi) transfer işlemi yapmanız gerekiyor. Birincisi, ORDI transfer işlemini bir satoshi transfer emri içine yazmak. İkincisi ise bu yazdığımız satoshiyi arkadaşımıza göndermek. Neden iki tane işlem yaptık? Ordinals sistemi üzerindeki özel tarayıcılar tek tek tüm bitcoin (satoshi) transfer emirlerini tarayarak yukarıdaki BRC-20 standardına uygun yazılmış işlem emri içindeki bilgileri bulup, hesaplardaki bakiye değişikliğini yapıyorlar. 

Aslına bakarsanız BRC-20 standardının pek çok handikapı var.  Öncelikle, BRC-20 gibi  farklı bir çok standart var, bu da özellikle Ordinals tarayıcılarının işlerini zorlaştırıyor. Diğer yandan, her bir BRC-20 token transfer işlemi için gereksiz büyüklükte verileri Bitcoin'e yazmak ve iki tane bitcoin transfer işlemi yapmak sistemi gereksiz yere meşgul etmek demek. Bu durum özellikle Bitcoin'in sadece ucuz para transferleri için kullanılması gerektiğini düşünen Bitcoin maksimalistlerinin tepkisini çekiyor. Haksız da sayılmazlar, sonuçta sistem üzerindeki yük ne kadar artarsa maliyetler de o kadar artıyor (Ethereum kullanıcıları bunu çok iyi bilirler). Üstelik BRC-20 transferi fazla sayıda UTXO yaratıyor ve Bitcoin sistemi için gereksiz yük oluyor. 

#### ...ve Runes

BRC-20 benzeri standartların zaaflarını gören ve bu standartların üzerine kurulu olduğu Ordinals'ı yazan Casey Rodarmor, para niteliğinde değiştirilebilir tokenlerın kullanılabilmesi için sıfırdan yepyeni bir standart kurdu.  Runes adını verdiği bu standart aslında Bitcoin'in yukarıda bahsettiğimiz banknot (UTXO) sistemi üzerine geliştirildi. 

Bu sistemde Runes standardı ile bir token yarattığınızda bu tokeni BRC-20'de olduğu gibi bir satoshi transfer işlem emri içine yazıyorsunuz. 

Runes sisteminin BRC-20 benzeri standartlardan temel farklılığı Ordinals standardını kullanmaması. Bunun birkaç avantajı var. Birincisi yukarıda bahsettiğimiz, işlemleri tek seferde bitirmenin getirdiği basitlik ve çöp banknotlar ortaya çıkmasını önlemek. İkincisi, Runes UTXO kullandığı için Runes bakiyeleri de Bitcoin UTXO içinde yazılı, dolayısıyla bu sistemi kullanan Bitcoin ölçeklenme çözümü Lightning Network ile de tümüyle uyumlu.

BRC-20'de her transfer için önce transfer edilebilir bakiyeyi yazacağınız bir bitcoin işlemi, arkasından da o bakiyeyi göndermek için ikinci bir bitcoin işlemi yapıyordunuz. Runes'da bunu tek işlemde gerçekleştiriyorsunuz. Tek bitcoin işleminde nasıl elinizdeki banknotu yakıp yerine yeni bir banknot alıyorsanız, Runes'da da o işlem içinde elinizdeki tokeni yakıp yerine yenisini alıyorsunuz. 

Öte yandan Runes ile Bitcoin üzerinde token transferleri BRC-20’ye kıyasla yaklaşık 4 kat daha az alan kaplıyor. Daha düşük alan kullanımı ve işlemlerin daha ucuza gelmesi Runes'u özellikle para niteliği taşıyan token transferinde daha kullanışlı hale getiriyor. 

Runes'un BRC-20'ye göre belki de tek ciddi dezavantajı token transferlerinde bir hata yapılması durumunda ortaya çıkıyor. Böyle bir durumda Runes'da kullanıcı tokenlerini kaybediyor, BRC-20'de ise transfer geçersiz oluyor ve tokenlar sahibinde kalıyor. Yine de bu durum özellikle Runes bir süre sonra daha oturmuş hale geldiğinde ortadan kalkacağı için o kadar da büyük bir handikap değil. 

### Peki ne işe yarayacak bu Runes?
Runes, bir standart olarak Bitcoin üzerinde token yaratılmasını sağlıyor olacak. Bu tokenlerin ne işe yarayacağını şu andan kestirebilmek zor. Tek bildiğimiz Bitcoin üzerinde çok ciddi bir değer tutulmakta ancak bu değer atıl olarak duruyor.  

| ![bitcoin-islem-potansiyeli](/assets/bitcoin-token-potansiyel.png)|
|:--:| 
| *Bitcoin üzerinde çok ciddi bir değer dururken, üzerinde bulunan tokenlerin değeri Ethereum ve Solana’ya göre neredeyse yok denecek kadar az. Kaynak: [Franklin Templeton Digital Assets](https://twitter.com/FTI_DA/status/1779979775651561691)*|

Runes'un başarılı olması ve bir standart haline gelmesi durumunda, buna uygun yaratılmış tokenler, Bitcoin üzerinde merkeziyetsiz finans benzeri sistemlerin kurulmasını hızlandırabilir. Yine de bunun olabilmesi için Bitcoin üzerinde farklı çözümlerin oluşması gerekiyor ki, bunun vakit alacağını söyleyebiliriz. 

Bu gerçekleşene kadar, Bitcoin üzerindeki topluluğun en azından spekülatif olarak yaratılacak tokenlere ilgi göstermesi olası. Bu da bizi memecoin denen tokenlere götürüyor. Önümüzdeki dönemde, Runes standardı ile yaratılmış tonlarca memecoin göreceğimize emin olabilirsiniz. Gerçek bir değer ifade etmediği için pek çoğumuz tarafından tu-kaka görünüyor olsa da, spekülatif doğası gereği memecoin'in hayatımızda bundan sonra da olacağı gerçeğini kabul etmek gerekiyor sanırım. 

Runes benzeri standartların gelişmesi, Bitcoin üzerindeki aktiviteyi artıracak, bu da madencilerin gelirlerinin artmasına ve Bitcoin sisteminin sürdürülebilir bir şekilde işlemesine olanak sağlayacak. Bu da, belki de Bitcoin ağı için en büyük kazanç olacak. 

Sonuç olarak, tutması halinde Runes, Bitcoin sistemini daha da canlandıracak ve sonrasında farklı çözümlere ilginin artmasına neden olacak olumlu bir gelişme olarak görülmeli. Gelişmeleri heyecanla bekliyor olacağız. 

---


*Not 1: Bu yazı ilk olarak 22 Nisan 2024'de [BTC Haber'de yayınlandı]()*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Piyasada oluşacak ihtimalleri değerlendiren bu yazıyı, yatırım tavsiyesi olarak almamanızı rica ederiz. Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

