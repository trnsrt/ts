Merge sonrası Ethereum'da neler olacak?
Bu yazımızda Ethereum dünyasında bu hafta yaşanan merge olayına ve sırada nelerin olduğunu bakacağız. 

Ethereum dünyası, 15 Eylül'de çıkacak olan yeni versiyonu sonrasında geliştirmelere devam ediyor. Bundan sonrasında sırada neler var, gelin birlikte bakalım. Ama öncelikle duymamış birkaç kişi için 'merge' denilen bu hafta yaşanan olayı hatırlayalım. 

### Neydi 'Merge'
"Kripto dünyasında yer gök 'merge' ile inliyor - iyi güzel de nedir bu 'merge'?". Efendim, 'merge' yani Türkçesi ile 'birleşme' uzun zamandır planlanan büyük bir değişim. 

Değişimin temel nedeni, Ethereum topluluğunun Bitcoin ile birlikte ortaya çıkan, ağın korunması ve işler halde devam etmesi için kullanılan iş-kanıtı (ingilizcesi Proof-of-Work kısaca PoW) sistemini bırakıp daha yeni bir teknoloji olan hisse-kanıtı (ingilizcesi Proof-of-Stake kısaca PoS) sistemine geçmesi. 

'Merge' ile birlikte, bugüne kadar kullanılan Ethereum sisteminin PoW kısmı atılıyor ve bu sistem Aralık 2020'den beri aktif olarak PoS'u kullanan  yeni Ethereum'un içine katılıyor. 

PoS sisteminin PoW'dan en büyük farkı enerji tasarrufu sağlaması. Malum, geçtiğimiz hafta Beyaz Saray Bilim ve Teknoloji Komitesi tarafından yayınlanan [raporda](https://www.coindesk.com/policy/2022/09/08/crypto-mining-energy-implications-need-further-study-white-house-report-says/) kripto madenciliğinin çevresel etkinin en aza indirilmesi için kanuni denetim gelmesi tavsiye edildi ([full rapor - pdf](https://www.whitehouse.gov/wp-content/uploads/2022/09/09-2022-Crypto-Assets-and-Climate-Report.pdf)]. Anlaşılan medyada geçmişte kara para aklama ve terörist faaliyetler konusunda yoğunlaşan kripto karşıtı eleştirel söylem, yavaş yavaş yerini enerji harcama bazlı çevresel etkilere doğru kayacak. Ethereum PoS ile birlikte enerji harcamasının %99.5 azaltarak kendini bu tartışmalardan sıyırmış gibi görünüyor (ve hayır, Bitcoin PoS'e geçmeyecek). 

"PoW sisteminin PoS ile değiştiriyorlar işte, ne var bu kadar büyütülecek?" diyebilirsiniz ama işin bu aslında o kadar da kolay bir geçiş değil. Zira, böyle bir geçiş ile bütün bir madenci kitlesinin ekipmanlarını çöpe atıyor ve onları karşınıza alıyorsunuz. Her ne kadar madenciler PoW sistemini devam ettireceklerini söyleseler de (çatallanma yoluyla bu mümkün), yapılan hamlenin çok başarılı olayını söylemek zor. PoW sisteminden PoS sistemine geçiş aslında temel olarak Ethereum topluluğunun asıl karar vericisinin geliştiriciler olduğunu net bir şekilde gösteriyor. 

Bunun dışında merge ile birlikte gelecek en büyük değişiklik, Ethereum'un yeni emisyon (para yaratım) politikası. Zira onaylayıcılara yaptıkları iş karşılığı madencilere verilenin %15'i kadar [bir ödül verilecek](https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth-2.0-economics/#staking-rewards). Bir taraftan Ağustos 2021'den beri kullanıcılar tarafından ödenen fazla işlem ücretlerinin yakıldığını düşünürsek, yeni sistemde eğer [ETH üzerindeki ortalama işlem ücretleri](https://ycharts.com/indicators/ethereum_average_gas_price) yaklaşık olarak 15.7 Gwei'den [daha fazla olursa](https://twitter.com/TobbyKitty/status/1568498284532224000) piyasadaki ETH miktarı azalmaya başlayacak (bu rakam değişen bir hedef, ödül verilen onaylayıcı sayısı arttıkça az da olsa yükselebilir). 

### Merge aslında bir stratejinin önemli bir mihenk taşı 

Aslına bakarsanız, merge olarak tanımlanan bu birleşme başlangıçta çok daha farklı bir şekilde kurgulanmıştı. İlk yapılan kurguya göre, Ethereum kendisini 64 farklı parçaya bölerek (ya da çoklayarak) kapasitesini artıracaktı. 

Sonrasında hem çok karmaşık hem de riskli olacağı düşüncesiyle bu kurgudan vazgeçildi ve Ethereum üzerinden stratejik bir değişiklik yapıldı. Neydi bu değişiklik? Temel olarak, roll-up bazlı bir başka deyişle Ethereum üzerine kurulu ikinci seviye çözümlere bağlı gelecek düşünüldü. Ne demek bu? Gelin biraz açalım: 

Blokzincirler temel olarak herkese açık bir defter olarak çalışıyorlar. Ağ üzerindeki tüm transferler bu açık deftere yazılıyor. Ethereum'da sadece basit para transferleri değil, daha karmaşık finansal işlemlerin de yapılması söz konusu. İşte bu karmaşık işlemler, sistem üzerindeki yükü artırmaya başlıyor. 

Nasıl bir yük artması oluyor? Basitçe şöyle anlatalım: Şu anda Ethereum üzerindeki her bir makine (diğer teknik anlatımıyla düğüm ingilizcesi 'node'), blok üzerinde gerçekleşen tüm işlemleri tek tek yeniden hesaplıyor. Bunu yaparak tüm işlemlerin doğru olduğunu kontrol etmiş oluyor.  Ethereum sisteme çok fazla yük binmesin diye bu işlem hesaplaması kapasitesine bir sınır koyuyor. Bu nedenle çok talep olduğunda kapasitenin bu talebi karşılayamamasından dolayı işlem ücretleri artıyor (zamanında bir NFT alımı için 100 ABD Doları üzerindeki paralar kısıtlı kapasitede işlemleri önce yapabilmek için veriliyordu). 

Sistem üzerindeki yük artmasının ne sıkıntısı var? Yük arttıkça, düğümlerin sistemi yürütmesi zorlaşıyor. Basit bilgisayarlar yerine daha gücü ve kapasitesi yüksek bilgisayarlara ihtiyaç duyuluyor. Basit bilgisayarlar yerini güçlü bilgisayarların alması ise sistemin merkezileşmesine yol açıyor ki, Ethereum geliştiricilerinin en korktuğu konuların başında bu merkezileşme geliyor. **Merkezileşme demek, sistemin dış saldırılara ya da etkilere daha açık hale gelmesi demek.** (Örneğin Solana ağı yüksek işlem yapmaya ayarlı olduğu için nispeten daha pahalı makineleri düğüm olarak kullanmak zorunda kalıyor)

İşte bu nedenle, Ethereum kendisine stratejik olarak farklı bir yol çizmeye başladı. Çizdiği bu yolda, sistem üzerinde ağır yük yaratan herhangi bir finansal işlemin gerçekleşmesi işlevini kendi üzerinden roll-up denen (türkçesi 'sarma', 'dürüm' artık ne derseniz o!) ikinci seviye çözümlere doğru atmaya başladı. 

Roll-up çözümlerin birkaç özelliği var. Birincisi, bu çözümler Ethereum ile senkronize çalışıyorlar. Yani, kullanıcı olarak paranız Ethereum sistemi içinde kalıyor ve o sistem tarafından korunuyor. Kullanıcı, parasını otomatik köprüler aracılığıyla bu ikinci seviye çözümlere atıyor. İşlemlerini orada gerçekleştiriyor ve dilediği zaman geri Ethereum'a çekebiliyor. İkinci seviye çözümler üzerlerinde yapılan işlemlerin sonuçlarını Ethereum ağı üzerine belli aralıklarla atıyorlar.

İkinci temel özellik bu roll-up çözümler sayesinde Ethereum üzerinde yapılabilen işlem sayısı kat be kat artabiliyor. Zira, bu çözümler Ethereum'un kısıtlı kapasitesini kullanmıyorlar,; aynı anda onlarcası bir arada çalışabildiği için paralel olarak ölçeklenme sağlıyorlar. Kapasitenin artması, kullanıcı açısından daha ucuza işlem yapabilmeyi olanaklı hale getiriyor. 

Peki ya bu ikinci seviye çözümde bir sorun oldu ve çözüm çalışmamaya başladı? O zaman ne olacak? Çok büyük bir sorun yok, varlık Ethereum seviyesinde hâlâ kullanıcıya ait (bu özellik, alternatif birinci seviye blokzincirler ya da Polygon gibi yan-zincirlere köprüler aracılığıyla varlık transfer edenler için geçerli değil). 

### Önümüzdeki dönem nelere gebe?

Önümüzdeki dönemde Ethereum için yine en büyük öncelik ölçeklenme üzerinde olacak. Bunun için de roll-up çözümlü bir dünyaya doğru yol almaya devam edecekler. 

Zaten aslına bakarsanız, önümüzdeki birkaç yıl için tüm kripto dünyasının en çok konuşacağı konu modüler blokzincirler olacak. Ne demek tam olarak bu? Her işi kendi başına yapan blokzincir altyapıları yerine bu altyapının farklı katmanlarında uzmanlaşmış yapılar. Ne sağlayacak bu? Öncelikle blokzincirlerin rahatça ölçeklenebilmesini. Modüler demek, farklı katmanlarda farklı çözümlerin birbiri ile uyumlu bir şekilde çalışabilmesi demek. Dolayısıyla, eskinin tek blok (mono-blok) blokzincir çözümlerinin tıkandığı ya da işlemlerin yoğunluktan dolayı maliyetli hale geldiği noktalarda, alternatif çözümlerin devreye girerek bu dar boğazları aşabilmesi mümkün olacak. 

Bu alanda uzun süredir çalışmalarını sürdüren [Polkadot](https://polkadot.network/) ve [Cosmos](https://cosmos.network/intro/)'un yanında [Avalanche subnets](https://docs.avax.network/subnets), [Polygon Supernet](https://blog.polygon.technology/introducing-polygon-supernets-powered-by-polygon-edge-100m-ecosystem-fund/) birinci seviye çözümlerin birbirleri ile konuşması ve değer transferi konusunda çözümler ortaya koydular. Önümüzdeki dönemde ise [Celestia](https://celestia.org/), [Fuel](https://www.fuel.network/) ve [Polygon Avail](https://polygon.technology/solutions/polygon-avail/) benzeri modüler çözümler de adlarını sıkça duyuracaklar, zira bu çözümler farklı katmanlarda Ethereum ile uyumlu çalışabilme özelliğine sahipler. 

### Arkası yarın

Özet olarak, Ethereum'un merge olayı bittikten sonra önümüzdeki dönemde ikinci seviye çözümlerin yanında daha altyapı düzeyinde modüler blokzincirlerin çok konuşulacağını söyleyebiliriz. Ethereum'un da gerek ikinci seviye çözümlerin önünün açılması gerekse kendi altyapısı içinde ölçeklenmeyi sağlayıcı pek çok planı mevcut. Onları da önümüzdeki yazımızda konuşacağız. 

---
# Yazı II: Ethereum'un gelecek vizyonu ne?

Önceki yazımızda geçtiğimiz hafta yaşanan Ethereum yeni versiyona geçme süreci olan 'merge' nediri incelemiş ve önümüzdeki dönemin nelere gebe olduğuna bakmaya başlamıştık. Bu yazımızda Ethereum'un gelecek vizyonunu incelemeye devam ediyoruz. 

### Ethereum nasıl bir gelecek planlıyor?

Öncelikle Ethereum'un bir topluluk olduğunu ve gelecek ile ilgili kararların bu topluluk tarafından verileceğini belirtelim. Yine de bu konuda en çok kafa yoranlardan Ethereum'un kurucusu olan Vitalik Buterin'in geçtiğimiz yıl sonunda yazdığı [bir blog yazısı](https://vitalik.ca/general/2021/12/06/endgame.html) bize Ethereum'un vizyonu konusunda ipucu verebilir. Şöyle diyor Vitalik: 

***'İleride blok üretiminin merkezi olduğu bir zincir bizi bekliyor olacak. Ancak bu zincirde blokların onayı hayli merkeziyetsiz ve güvene ihtiyaç duymadan yapılacak ve özel (ihtisaslaşmış) sansür-karşıtı bir mekanizma (sihir) blok üretici sansürüne engel olacak'***

Hazmı zor bir cümle (Vitalik’in her blog yazısında olduğu gibi). Ethereum'un geleceğini anlamak için biraz açmakta fayda var bu cümleyi. 

Blokzincirlerin en büyük ölçeklenme sıkıntısı üretilen blok büyüklüğünün (yani kapasitesinin) sınırlı olması. Kapasite sınırlı tutuluyor zira  artırdığınız durumda blokzinciri çalıştıran makinelerin (düğümlerin) tüm işlemleri yapabilmesi için çok güçlü makineler gerekiyor. Ne kadar güç ihtiyacı o kadar basit makinenin devre dışı kalması demek. Bu da sistemin merkezileşmesi bir başka deyişle Ethereum geliştiricilerinin en büyük kabusu anlamına geliyor. 

İşte Ethereum sistemi olabildiğince makinenin sistem içinde olması yani sistemin olabildiğince merkeziyetsiz olabilmesi için, kendi sistemini bölmeye başlıyor. Öncelikle geçen yazımızda da bahsettiğimiz gibi, Ethereum ikinci seviye çözümler ile birlikte artık kendi onaylayıcıların üzerindeki yükü [^1] atmaya çalışıyor. Nasıl yapıyor bunu?

Öncelikle, işlem yapma (ingilizcesi 'execution') rolünü, ağırlıklı olarak ikinci seviye çözümlere paslıyor. Böylece, ağır işlemler ikinci seviye çözümler aracılığıyla gerçekleştiriliyor. İkinci seviye çözümler yaptıkları işlemlerin sonuçlarını ana Ethereum ağına yazıyorlar. Böylece ana Ethereum ağı ikinci seviye üzerindeki her işlemi tekrar yapmak zorunda kalmıyor.

İkinci olarak, ileride talebin çok fazla olması durumunda blok oluşturmanın yarattığı ağır yükü kaldırabilmek için blok üretimini güçlü ama sayıca az (dolayısıyla daha merkezi) bir grup üreticiye bırakıyorlar.  İşte merkezileşme tehlikesi burada beliriyor. Bunu tehlikeyi ortadan kaldırabilmek için, işlemlerin doğru olduğunu kontrol işlemini olabildiğince merkeziyetsizleştirme yoluna gidiyorlar.

Bu vizyonu gerçekleştirebilmek için paralel olarak devam eden beş teknik geliştirme var. Bunları İngilizce tabirleriyle The Merge ('birleşme'), The Surge ('sıçrama'), The Verge ('sınırlama'), The Purge ('arındırma') ve The Splurge ('hava atma') deniyor. Gelin şimdi de bu kafiyeli adlara sahip geliştirmelere bakalım kısaca (bu terimlerin hepsini tek bir diagramda görmek isterseniz Vitalik'in Aralık 2021'de attığı [şu tweete](https://twitter.com/vitalikbuterin/status/1466411377107558402) bakıp gözlerinizi kanatabilirsiniz :) ).  

#### The Merge (Birleşme): 

Bu hafta içinde olan meşhur birleşme. Birleşme denmesinin nedeni şu: Az önce bahsettiğimiz, işlemleri ikinci seviyeye yüklemenin bir parçası olarak, Ethereum kendisini iki katmana ayırıyor. İşlemleri gerçekleştiren 'execution' katmanı ve işlemleri onaylayan ve zincirin uzlaşı içinde ilerlemesini sağlayan 'consensus' katmanı. Execution katmanı bildiğimiz şu zamana kadar kullandığımız Ethereum aslında. Consensus katmanı ise PoS ile birlikte 2020 yılında hayata geçen 'yeni' Ethereum diğer adıyla eth2. Merge ile birlikte Execution katmanında bulunan PoW yok ediliyor ve bu katman eth2'de altında 'birleştiriliyor'. 

#### The Surge (Sıçrama):

The Surge , tamamen ikinci seviye çözümlerin ölçeklenebilmesi üzerine kurulu. 

Ethereum'un önümüzdeki dönemde artacak işlem talebini ikinci seviye çözümler karşılayacak.  Bu çözümler Ethereum ile sıkı-fıkı çalıştıkları için Ethereum'a ile aralarında çift yönlü bir bilgi akışları söz konusu. Onlarca çözümünün bilgi akışının olacağını düşünürsek, ileride Ethereum üzerindeki düğümler üzerindeki yük yine artmaya başlayacak. İşte böyle bir durumda yapılmakta olan birkaç geliştirme onaylayıcıları rahatlatacak. 

Öncelikle orijinal Ethereum planında olan 'sharding' (türkçeye parçalara bölme olarak çevirebiliriz) sayesinde onaylayıcılar tüm datayı değil belli bir parçasını onaylayacaklar.  İlk aşamada blok içindeki bir parçanın tamamını indirip kontrol edecekler (buna PDS proto-dank-sharding deniyor). Aslında bu bir ara çözüm ve arada bir duyabileceğiniz EIP-4844 geliştirmesi ile gelecek. 

Başlangıçta düğümler bunu yapabilirler ancak ileride talebin çok artması durumunda tüm veriyi indirmek düğümlere yine yük getirecek. Bu nedenle daha sonraki bir dönemde sunulacak iki yeni geliştirme sayesinde (DAS ve KZG[^2]) basit onaylayıcılar bile önlerine gelen blok parçalarının doğru ve eksiksiz bir biçimde oluşturulduğunu kontrol edebilecekler. Bunu yaparken tüm parçayı yüklemek zorunda kalmayıp, daha basit şekilde matematiksel olarak örnekleme yapacaklar. Bu sayede, onaylayıcıların işlem onaylama kapasitesi çok ciddi bir şekilde artacak.

Bir diğer önemli değişiklik, ikinci seviye çözümlerin Ethereum üzerinde çok fazla kapasite (gas) kullanması. İşte EIP-4844 ile gelen bir başka yenilik, bu fonksiyonların artık çok daha fazla verinin taşınabildiği ama kapasiteden o kadar yemeyen 'data blob' ('su baloncuğu' diye çevirsek yanlış olmaz sanırım) formatının gelmesi. Bu formatın özelliği hem ucuz olması hem de bir ay sonra sistemden silinmesi sayesinde geçmiş veriyi şişirmemesi. "Geçmiş veriyi kaybetmiyor muyuz bu durumda?" Çok değil, zira burada saklanan en kapsamlı veri, ikinci seviyede işlem bilgisinin doğruluk kanıtları. İşlem gerçekleşip aradan bir ay geçtikten sonra geriye dönüp bakmanın bir anlamı yok.[^3]

Bunların dışında kısa vadede yapılacak bir başka geliştirme ise, ikinci seviye çözümlerin Ethereum üzerindeki kapasite ihtiyacını azaltacak.[^4] EIP-4488 olarak adlandırılan bu geliştirme çok basit ve hızlıca kurulacak ve kısa vadedeki ihtiyaçları giderecek. 

#### The Verge (Sınırlandırma)
The Verge, temel olarak onaylayıcıların işlemeleri gereken bilgileri sınırlandırarak üstlerindeki yükü azaltmaya çalışıyor.  

Ethereum sistemi üzerinde bir işlem gerçekleştiği noktada, onaylayıcılar işlem öncesi durumu alıp, yapılan işlemi hesaplayıp, işlem sonrası durumu buluyor ve doğruluğunu onaylıyorlar. Bunun için ilk olarak işlem öncesi durumun (state) bilinmesi (ve elde olması) gerekiyor. Sorun şu ki, hesaplar ve işlemler arttıkça bu mevcut durumların olduğu liste büyümeye ve Ethereum üzerinde darboğaz yaratmaya başlıyor. 

Bu sıkıntının önüne geçilebilmesi için, onaylayıcılar blok başlamadan önce tüm Ethereum sisteminin mevcut durum tablosunu önlerine almak yerine, sadece o blokta gerçekleşen işlemlere ait mevcut durumlarını dikkate alacak. Bu sayede onaylayıcıların önündeki en büyük darboğazlardan biri yok edilecek [^5] Tüm sistemin mevcut durumu inşaatçılar tarafından tutulacak ama onlar zaten işin hamaliyesini yaptıkları için farketmeyecek. Burada önemli olan onaylayıcıların üzerindeki yükü azaltarak merkeziyetsizlikten feragat etmemek.

#### The Purge (Arındırma)
The Purge temel olarak sistem üzerindeki geçmiş datanın temizlenmesi ve onaylayıcıların ihtiyacı olan hard-disk kapasitesini azaltmayı hedefliyor. 

Ethereum blokzinciri üzerindeki onaylayıcılar tarafından kullanılan işlem arayüzlerinin (client) bloklara ait her tür datanın tarihçesini tutmaları gerekiyor. İşlemlerin ve sistemin doğruluğunu kontrol etmek isteyen bir kullanıcı, bütün bu datayı indirmek zorunda (ki bu yüzlerce GB büyüklüğünde). Yeni gelen bir geliştirme (EIP-4444) ile birlikte bir yıldan daha eski datanın tutulmasına gerek kalmayacak. "Nasıl yani? Tüm geçmiş silinecek mi?" diye soracak olursanız, cevap tabii ki hayır. Bu data, büyük data merkezleri tarafından (örneğin Etherscan) tutulmaya devam edecek. 

Bunun yanında bir önceki The Verge kısmında gördüğümüz, inşaatçılar tarafından tutulan 'tüm sistemin mevcut durumlarn' içinde bir ya da iki yıldan fazla süredir aktif olmayanlar silinecek, ki inşaatçılar rahat etsin (Yine bu verinin Etherscan benzeri yerlerde tutulmasına devam tabii)

#### The Splurge (Hava atma)
Son olarak ise merkeziyetsizlik için oldukça önemli yenilikler getiren The Splurge var. Bu sürecin sonu artık pastayı yaptıktan sonra üzerine konan çilek adeta. 

Ethereum eski sisteminde madenciler blokları oluşturur ve diğer madencilere onaya sunarlardı, yani her iki işi de madenciler yapardı. Eth2 ile birlikte madencilerin yerini onaylayıcılar alacak ve iki işi yapmaya devam edecekler. Ancak dediğimiz gibi ileride kapasitenin çok artması gerektiği durumlarda blok oluşturmak için güçlü makineler gerekecek. İşte bu nedenle, Ethereum bir güçler ayrılığına gidecek. Özel amaçlı inşaatçı makineler blokları oluşturacak, onaylayıcı olan bir başka grup ise bunları onaylayacak. [^6] (Bu ayrıma PBS proposer-builder separation deniyor). 

Burada önemli bir ayrıntı da şu. Blok oluşturanlar bazı işlemleri bloklarına almayarak sansüre kalkışabilirler.  Bunu önlemek için onaylayıcılar sansüre-dayanıklı listeler (Censorship resistance list) oluşturarak, bloklara girmeye uygun tüm işlemlerin bir listesinin yapacaklar. İnşaatçılar blokları oluştururken bu listeleri kullanmak zorunda kalacaklar. Yani, inşaatçılar emek ve güç yoğun ama işlemler üzerinde fazla bir söz hakkı olmayan oyuncular olacaklar. 


### Sonuç
Ethereum, geçen hafta yaşadığımız merge sonrası geçmişte yaşadığı darboğazları yaşamamak ve ileride her tür uygulamanın ihtiyacı olan altyapı hizmetine yetebilecek kapasitesi getirebilmek için nasıl bir yol haritası izlemesi gerektiğini belirlemiş durumda. Bunlar, üzerinde kurulu ikinci seviye çözümlerin ölçeklenmesini sağlayacak The Surge, sistemi yürüten onaylayıcıların yükünü hafifleten The Verge, sistem üzerinde ayakbağı oluşturan geçmişi temizleyecek olan The Purge ve son olarak merkeziyetsizlik konusunda iyileştirmeler getiren The Splurge, olarak karşımıza çıkıyor. 

Bütün bu işlemlerin özünde, Ethereum'u ileride sansüre karşı koruyacak olan merkeziyetsizlik prensibinden vazgeçmeden, yüksek hacimli işlem sayılarını başarıyla işlemek var. Plan karmaşık görünse de aslında Ethereum geliştiricilerinin kafasında oldukça net. Gerçekleşmesi ise uzunca bir süre alacak. Önümüzdeki dönemde aşama aşama hayata geçmeye başladığını hep birlikte göreceğimizi umuyoruz. 

—-

*Kaynaklar: 

*[The End Game](https://vitalik.ca/general/2021/12/06/endgame.html) - Vitalik Buterin*

*[The Hitchhiker's Guide to Ethereum](https://members.delphidigital.io/reports/the-hitchhikers-guide-to-ethereum/) - Delphi Digital*

*[The Complete Guide to Rollups](https://members.delphidigital.io/reports/the-complete-guide-to-rollups) - Delphi Digital*


[^1]: "Nedir bu yük?" diye soracak olursanız; tam donanımlı düğümlerin yaptığı iki temel iş var.
- Birincisi, blok içindeki her bir işlemin doğru olup olmadığını anlamak. Bunun için blok öncesi durumu alıyorlar (Ayşe'nin 10 ETH'si, Ali'nin 5 ETH'si var), istenen işlemi yapıyorlar (Ayşe, Ali'ye 1 ETH gönderdi), blok sonundaki durumu kontrol ediyorlar (Ayşe'nin 9 ETH'si, Ali'nin 6 ETH'si var).
- İkincisi ise, bu bloğa eklenen blokta bu işlemin ve son durumun doğru bir şekilde işlendiğini kontrol edip onaylıyorlar.

[^2]: Bu iki çözüm, oluşturulan blokların doğru oluşturulduğunu bulmaya yarayan DAS (data-availability-sampling) ve datanın tam olduğunu anlamaya yarayan KZG committments. KZG sistemi geçici bir çözüm, zira kuantum bilgisayarlar tarafından kırılabilirler ve kurucularına güvenmek zorundasınız. Uzun vadede KZG yerine ZK-proof denen sıfır-bilgi-kanıtı gerektiren STARK'ların kullanılması planlanabilir. Bunun için ZK-proof teknolojisinin daha geliştirilerek sisteme getirdiği hesaplama yükünün hafifletilmesi gerekiyor.

[^3]: İkinci seviye çözümler içinde Optimistic Rollup'lar, yapılan işlemlerin doğruluğuna itiraz için bir haftalık bir süre veriyor. O sürede itiraz olmaz ise işlem zaten onaylanıyor, dolayısıyla bir aylık süre fazlasıyla yeterli. Zk-roll up çözümlerde zaten böyle bir süreye gerek yok, işlemler anında gerçekleşiyor.

[^4]: EIP-4488 ile 2. Seviye çözümün en temel ihtiyacı olan calldata fonksiyonunun Ethereum üzerindeki gaz ihtiyacı 16 gas/byte'dan 3 gas/byte'a iniyor.

[^5]: Burada inşaatçı olan ağır işçi oyuncular yine tüm mevcut durumu almak zorundalar ama onlar zaten güçlü makinelere sahip oldukları için bu büyük bir problem yaratmayacak. Burada önemli olan merkeziyetsiz onaylayıcıların üzerindeki yükü olabildiğince azaltmak. Burada bir diğer nokta da, içeriye alınan işlemlere ait mevcut durumların Verkle tree denen daha verimli bir yöntem ile bloğa aktarılması.

[^6]: Burada, blokları oluşturan inşaatçılar, içeri bir an önce girmek isteyen kullanıcılardan 'bahşiş' alabilecekler. Bunun dışında, şu anda da olan ve MEV (miner-extractable-value) denen işlemlerin öncelik sırasında oluşan arbitraj fırsatları da bu inşaatçılar tarafından alınacak. Bunun karşılığında bu inşaatçılar, oluşturdukları bloklar kabul edilsin diye kazandıkları paranın bir kısmını onaylayıcılara verecekler. Düzgün çalışan bir piyasada, kullanıcıların verdiği ücretlerin ve MEV'lerin büyük kısmının inşaatçılar tarafından blokları kabul edilmesini sağlamak için onaylayıcılara verilmesi beklenir. Bu da, onaylayıcıların yani ETH stake edenlerin kazandıkları paranın (faiz gelirinin üzerine) artması anlamına gelir.:
