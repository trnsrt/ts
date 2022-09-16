---
layout: post
title:  "Ethereum 'The Merge' ve sonrası"
date:   2022-09-16 12:17:56 +0300
categories: Genel
tags: Yazılar, DeFi, CoindeskTR
---

Bu yazımızda Ethereum dünyasında bu hafta yaşanan merge olayına ve sırada nelerin olduğunu bakacağız. 

Ethereum dünyası, 15 Eylül'de çıkan yeni versiyonu sonrasında geliştirmelere devam ediyor. Bundan sonrasında sırada neler var, gelin birlikte bakalım. Ama öncelikle duymamış birkaç kişi için 'merge' denilen bu hafta yaşanan olayı hatırlayalım. 

### Neydi 'The Merge'?
"Kripto dünyasında yer gök 'merge' ile inliyor - iyi güzel de nedir bu 'The Merge'?". Efendim, 'merge' yani Türkçesi ile 'birleşme' uzun zamandır planlanan büyük bir değişim. 

Değişimin temel nedeni, Ethereum topluluğunun Bitcoin ile birlikte ortaya çıkan, ağın korunması ve işler halde devam etmesi için kullanılan iş-kanıtı (ingilizcesi Proof-of-Work kısaca PoW) sistemini bırakıp, daha yeni bir teknoloji olan hisse-kanıtı (ingilizcesi Proof-of-Stake kısaca PoS) sistemine geçmesi. 

'Merge' ile birlikte, bugüne kadar kullanılan Ethereum sisteminin PoW kısmı atılıyor ve bu sistem Aralık 2020'den beri aktif olarak PoS'u kullanan  yeni Ethereum'un içine katılıyor. 

| ![splash](/assets/puzzle-g9d8d2944d_800)|
|:--:| 
| *Image by [DPIRO](https://pixabay.com/users/piro4d-2707530/) from [Pixabay](https://pixabay.com/)*|

PoS sisteminin PoW'dan en büyük farkı enerji tasarrufu sağlaması. Malum, geçtiğimiz hafta Beyaz Saray Bilim ve Teknoloji Komitesi tarafından yayınlanan [raporda](https://www.coindesk.com/policy/2022/09/08/crypto-mining-energy-implications-need-further-study-white-house-report-says/) kripto madenciliğinin çevresel etkisinin en aza indirilmesi için kanuni denetim getirilmesi tavsiye edildi ([full rapor - pdf](https://www.whitehouse.gov/wp-content/uploads/2022/09/09-2022-Crypto-Assets-and-Climate-Report.pdf)]. Anlaşılan medyada geçmişte kara para aklama ve terörist faaliyetler konusunda yoğunlaşan kripto karşıtı eleştirel söylem, yavaş yavaş yerini enerji harcama bazlı çevresel etkilere doğru kayacak. Ethereum, PoS ile birlikte enerji harcamasının %99.5 azaltarak kendini bu tartışmalardan sıyırmış gibi görünüyor (ve hayır, Bitcoin PoS'e geçmeyecek). 

"PoW sisteminin PoS ile değiştiriyorlar işte, ne var bu kadar büyütülecek?" diyebilirsiniz ama işin aslı bu o kadar da kolay bir geçiş değil. Zira, böyle bir geçiş ile bütün bir madenci kitlesinin ekipmanlarını çöpe atıyor ve onları karşınıza alıyorsunuz. Her ne kadar madenciler PoW sistemini devam ettireceklerini söyleseler de (çatallanma yoluyla bu mümkün), yapılan hamlenin çok başarılı olduğunu söylemek zor. PoW sisteminden PoS sistemine geçiş aslında temel olarak Ethereum topluluğunun asıl karar vericisinin geliştiriciler olduğunu net bir şekilde gösteriyor. 

Bunun dışında merge ile birlikte gelecek en büyük değişiklik, Ethereum'un yeni emisyon (para yaratım) politikası. Zira onaylayıcılara yaptıkları iş karşılığı madencilere verilenin %15'i kadar [bir ödül verilecek](https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth-2.0-economics/#staking-rewards). Bir taraftan Ağustos 2021'den beri kullanıcılar tarafından ödenen fazla işlem ücretlerinin yakıldığını düşünürsek, yeni sistemde eğer [ETH üzerindeki ortalama işlem ücretleri](https://ycharts.com/indicators/ethereum_average_gas_price) yaklaşık olarak 15.7 Gwei'den [daha fazla olursa](https://twitter.com/TobbyKitty/status/1568498284532224000) piyasadaki ETH miktarı azalmaya başlayacak (bu rakam değişen bir hedef, ödül verilen onaylayıcı sayısı arttıkça az da olsa yükselebilir - farklı senaryoları [şuradan inceleyebilirsiniz](https://ultrasound.money/)).

### Merge aslında bir stratejinin önemli bir mihenk taşı 

Aslına bakarsanız, merge olarak tanımlanan bu birleşme başlangıçta çok daha farklı bir şekilde kurgulanmıştı. İlk yapılan kurguya göre, Ethereum kendisini 64 farklı parçaya bölerek (ya da çoklayarak) kapasitesini artıracaktı. 

Sonrasında hem çok karmaşık, hem de riskli olacağı düşüncesiyle bu kurgudan vazgeçildi ve Ethereum üzerinden stratejik bir değişiklik yapıldı. Neydi bu değişiklik? Temel olarak, 'roll-up bazlı' bir başka deyişle Ethereum üzerine kurulu ikinci seviye çözümlere bağlı bir gelecek düşünüldü. Ne demek bu? Gelin biraz açalım: 

Blokzincirler temel olarak herkese açık bir defter olarak çalışıyorlar. Ağ üzerindeki tüm transferler bu açık deftere yazılıyor. Ethereum'da sadece basit para transferleri değil, daha karmaşık finansal işlemlerin de yapılması söz konusu. İşte bu karmaşık işlemler, sistem üzerindeki yükü artırmaya başlıyor. 

Nasıl bir yük artması oluyor? Basitçe şöyle anlatalım: Şu anda Ethereum üzerindeki her bir makine (diğer teknik anlatımıyla düğüm ingilizcesi 'node'), blok üzerinde gerçekleşen tüm işlemleri tek tek yeniden hesaplıyor. Bunu yaparak tüm işlemlerin doğru olduğunu kontrol etmiş oluyor.  Ethereum sisteme çok fazla yük binmesin diye bu işlem hesaplaması kapasitesine bir sınır koyuyor. Bu nedenle çok talep olduğunda kapasitenin bu talebi karşılayamamasından dolayı işlem ücretleri artıyor (zamanında bir NFT alımı için 100 ABD Doları üzerindeki paralar kısıtlı kapasitede işlemleri önce yapabilmek için veriliyordu). 

Sistem üzerindeki yük artmasının ne sıkıntısı var? Yük arttıkça, düğümlerin sistemi yürütmesi zorlaşıyor. Basit bilgisayarlar yerine daha gücü ve kapasitesi yüksek bilgisayarlara ihtiyaç duyuluyor. Basit bilgisayarlar yerini güçlü bilgisayarların alması ise sistemin merkezileşmesine yol açıyor ki, Ethereum geliştiricilerinin en korktuğu konuların başında bu merkezileşme geliyor. **Merkezileşme demek, sistemin dış saldırılara ya da etkilere daha açık hale gelmesi demek.** (Örneğin Solana ağı yüksek işlem yapmaya ayarlı olduğu için nispeten daha pahalı makineleri düğüm olarak kullanmak zorunda kalıyor)

İşte bu nedenle, Ethereum kendisine stratejik olarak farklı bir yol çizmeye başladı. Çizdiği bu yolda, sistem üzerinde ağır yük yaratan herhangi bir finansal işlemin gerçekleşmesi işlevini kendi üzerinden roll-up denen (türkçesi 'sarma', 'dürüm' artık ne derseniz o!) ikinci seviye çözümlere doğru atmaya başladı. 

Roll-up çözümlerin birkaç özelliği var. Birincisi, bu çözümler Ethereum ile senkronize çalışıyorlar. Yani, kullanıcı olarak paranız Ethereum sistemi içinde kalıyor ve o sistem tarafından korunuyor. Kullanıcı, parasını köprüler (güven ihtiyacını en aza indiren akıllı kontratlar) aracılığıyla bu ikinci seviye çözümlere atıyor. İşlemlerini orada gerçekleştiriyor ve dilediği zaman geri Ethereum'a çekebiliyor. İkinci seviye çözümler üzerlerinde yapılan işlemlerin sonuçlarını Ethereum ağı üzerine belirli aralıklarla atıyorlar.

İkinci temel özellik bu roll-up çözümler sayesinde Ethereum üzerinde yapılabilen işlem sayısı kat be kat artabiliyor. Zira, bu çözümler Ethereum'un kısıtlı kapasitesini kullanmıyorlar,; aynı anda onlarcası bir arada çalışabildiği için paralel olarak ölçeklenme sağlıyorlar. Kapasitenin artması, kullanıcı açısından daha ucuza işlem yapabilmeyi olanaklı hale getiriyor. 

"Peki ya, bu ikinci seviye çözümde bir sorun olur ve çözüm çalışmamaya başlarsa?" O zaman ne olacak? Çok büyük bir sorun yok, varlık Ethereum seviyesinde hâlâ kullanıcıya ait (bu özellik, alternatif birinci seviye blokzincirler ya da Polygon gibi yan-zincirlere köprüler aracılığıyla varlık transfer edenler için geçerli değil). 

### Önümüzdeki dönem nelere gebe?

Önümüzdeki dönemde Ethereum için yine en büyük öncelik ölçeklenme üzerinde olacak. Bunun için de roll-up çözümlü bir dünyaya doğru yol almaya devam edecekler. 

**Zaten aslına bakarsanız, önümüzdeki birkaç yıl için tüm kripto dünyasının en çok konuşacağı konu modüler blokzincirler olacak.** Ne demek tam olarak bu? Her işi kendi başına yapan blokzincir altyapıları yerine bu altyapının farklı katmanlarında uzmanlaşmış yapılar. Ne sağlayacak bu? Öncelikle blokzincirlerin rahatça ölçeklenebilmesini. Modüler demek, farklı katmanlarda farklı çözümlerin birbiri ile uyumlu bir şekilde çalışabilmesi demek. Dolayısıyla, eskinin tek blok (mono-blok) blokzincir çözümlerinin tıkandığı ya da işlemlerin yoğunluktan dolayı maliyetli hale geldiği noktalarda, alternatif çözümlerin devreye girerek bu darboğazları aşabilmesi mümkün olacak. 

Bu alanda uzun süredir çalışmalarını sürdüren [Polkadot](https://polkadot.network/) ve [Cosmos](https://cosmos.network/intro/)'un yanında [Avalanche subnets](https://docs.avax.network/subnets), [Polygon Supernet](https://blog.polygon.technology/introducing-polygon-supernets-powered-by-polygon-edge-100m-ecosystem-fund/) gibi yenilikler, birinci seviye çözümlerin birbirleri ile konuşması ve değer transferi konusunda çeşitli çözümler ortaya koydular. Önümüzdeki dönemde ise [Celestia](https://celestia.org/), [Fuel](https://www.fuel.network/) ve [Polygon Avail](https://polygon.technology/solutions/polygon-avail/) benzeri modüler çözümler de adlarını sıkça duyuracaklar, zira bu çözümler farklı katmanlarda Ethereum ile uyumlu çalışabilme özelliğine sahipler. 

### Arkası yarın

Özet olarak, Ethereum'un merge olayı bittikten sonra önümüzdeki dönemde ikinci seviye çözümlerin yanında daha altyapı düzeyinde modüler blokzincirlerin çok konuşulacağını söyleyebiliriz. Ethereum'un da gerek ikinci seviye çözümlerin önünün açılması gerekse kendi altyapısı içinde ölçeklenmeyi sağlayacak birçok planı mevcut. Onları da önümüzdeki yazımızda konuşacağız. 

---

*Not 1: Bu yazı ilk olarak 16 Eylül 2022'de [Coindesk Türkiye](https://www.coindeskturkiye.com/))'de [yayınlandı](https://www.coindeskturkiye.com/yazarlar/turan-sert/ethereum-the-merge-ve-sonrasi-1984)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*
