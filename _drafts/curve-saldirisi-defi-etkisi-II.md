---
layout: post
title:  "Curve saldırısının DeFi'ye etkileri - 2"
date:   2023-09-14 18:17:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Geçtiğimiz hafta başladığımız Curve olayı konusuna, olayın DeFi'ye etkilerine bakarak devam ediyoruz. 

### Geçen haftanın kısa özeti
İki saat süren Türk dizilerinin bir sonraki hafta yayınlanan bir saatlik özeti gibi olmaması için hızlı bir şekilde [olayı](/genel/2023/09/06/curve-saldirisinin-defiye-etkisi.html) hatırlayalım.

DeFi'nin ağır toplarından merkeziyetsiz alım-satım platformu Curve, Temmuz ayı sonunda bir saldırıya uğramış ve dört ayrı Curve havuzundan 73 milyon ABD Doları çalınmıştı. Fonların % 73'ü ya saldırgandan önce onun önüne geçen botlar tarafından kurtarılmış ya da saldırgan tarafından iade edilmişti. Bu arada Curve'ün tokeni olan CRV'nin fiyatı 70 centlerden 50 centlere kadar düşmüştü. Bu düşüş, Curve'ün kurucusu Michael Egorov'un CRV'yi teminat göstererek almış olduğu kredilerin likide olma ihtimalini doğurmuştu. Egorov bu durumdan elindeki CRV tokenlerin bir kısmını şaibeli bir grup insana tezgah üstünde 40 centten satıp borçlarını kapatarak sıyrılabildi. 

Bu kısa özet sonrası gelin şimdi de bu olayın DeFi dünyasına etkilerine bakalım: 

### Olayın DeFi dünyasına etkileri

Aslına bakarsanız, yaşanan saldırının miktarı (fonlar geri gelmeden önce bile) DeFi alanındaki saldırılar arasında ilk 20'ye giremeyecek kadar küçük. ([DeFi Rekt](https://rekt.news/leaderboard/)'e göre 24. sırada). Konunun önemi rakamın büyüklüğünden öte, DeFi dünyasının belli zayıf noktalarını gözler önüne sermesinden geliyor. 

#### Akıllı kontrat riski

Öncelikle bu para nasıl çalındı? DeFi'de hack olaylarının nedenleri arasında ilk sırayı akıllı kontratlarda yaşanan sorunları alır. Akıllı kontratı yazan ekip kritik bir noktayı atlar, denetçiler bunu anlamaz (ya da anlayıp raporda yazsalar da ekip bunları düzeltmez ya da düzeltmekte geç kalır) sonrasında koddaki açığı keşfeden kişiler uygun bir zamanda (örneğin Pazar sabahı) bir anda saldırıya geçip paraları götürürler. Bu saldırıların ne kadar etik olduğu DeFi dünyasında tartışılıyor ama o konuyu bir başka yazıya bırakalıma. 

Curve'ün yaşadığı durum ise biraz daha farklı. Elbette burada da akıllı kontratta yaşanan bir sorun vardı ancak sorunun nedeni akıllı kontratı yazan Curve ekibi değildi. Sıkıntı, Curve ekibinin kullandığı programlama dilindeki bir hatadan kaynaklandı[^1]. 

İşte bu da DeFi'deki temel sıkıntılardan biri. DeFi'deki protokoller genelde açık kaynaklı olarak yazılıyorlar. Bu protokolleri geliştiren yazılımcılar da ürün geliştirirken daha önce açık kaynak ile yazılmış araç ve dilleri kullanıyorlar.  Dolayısıyla ortaya birbirine geçmiş lego parçalarından oluşan projeler çıkıyor. Protokollerin akıllı kontratları denetimden geçiyor, zaten Curve ekibi de bu anlamda en sağlam iş çıkaran yerlerden biri. Burada sorun, akıllı kontratın yazıldığı dilin (Curve'un kullandığı versiyonlarında) bir sorun çıkması. Sonuçta yazılımcılar yazdıkları kodun işleyip işlemediğini kontrol ediyorlar ama kullandıkları dili sorgulamak kimsenin aklına gelmiyor[^2].

| ![legos](/assets/duplo-1981724_800.jpg)|
|:--:| 
| *Image by [Bruno](https://pixabay.com/users/bru-no-1161770/) from [Pixabay](https://pixabay.com/)*|

Yazılımlarda ya da dillerde hata olması beklenebilir, zira  sonuçta hepsi insanlar tarafından kurgulanıyor. DeFi'nin şanssızlığı (ya da belki de şansı) bu tip olayların zincir üzerinde olması nedeniyle herkes tarafından anında görülebiliyor olması. Büyük şirketlerin ve ekiplerinin kullandığı yazılımlarda da benzer hatalar oluyor ancak bu hatalar bir şekilde anında çözülüp, hasır altı ediliyor. DeFi'de ise kontratları yazdıktan sonra gerekli testleri yapıp ortalığa salıyorsunuz. Bu kontratlarda problem çıktığında kontratı geri çağırmak mümkün değil. Kontratı güncellenebilir yapabilirsiniz ama o zaman da kimse yarın öbür gün parametreleri değiştirilebilecek bir kontrat ile iş yapmak istemiyor. Çare ne o zaman? Çare, her zaman olduğu gibi bu alandaki kontratların bu tip saldırılar sonrası 'kurşun geçirmez' hale gelecek kadar olgunlaşmasını beklemek. 

#### Beyaz şapkalı hacker ve botlar nereye kadar işin içine girmeli?
Saldırının ortaya çıkması sonrası, pek çok farklı saldırgan da aynı yöntemi kullanarak Curve üzerindeki havuzlara saldırmaya başladı. 

İşte bu sırada iyi niyetli ve kötü niyetli hackerlar arasında ilginç bir savaş da yaşandı. Ethereum üzerinde yapmak istediğiniz işlemler bir havuzda toplanıyor ve bu işlemler blok yapıcılar tarafından sıraya konup işleniyor. Sıraya konmada en büyük kriter blok yapıcıya verilecek işlem ücreti. Saldırganların işlemi havuzda toplanıp gerçekleştirilmek üzere sıra beklerken, başka saldırgan ya da beyaz şapkalı hackerlar bu işlemi aynen kopyalayıp daha yüksek işlem ücreti ödeyerek ilk işlemin önüne geçebiliyor[^3]. Nitekim bu savaşlardan dolayı MEV’de (basitçe işlem sıralama için ödenen komisyon miktarı) Ethereum tarihinin en yüksek ikinci günü yaşandı. İşlemlerini öne geçirmek isteyenler 30 Temmuz 2023 günü tam 6 bin ETH harcadılar. 

| ![mev-vs-gas](/assets/mev-gaz-ucreti_800.png)|
|:--:| 
| *Ethereum üzerinde sisteme ve madencilere ödenen günlük ücretlerde 30 Temmuz günü tarihin en yüksek rakamlarından biri görüldü.. Kaynak: [MevBoost Dashboard](https://mevboost.pics/)*|

Bu tip front-running yapan botlar DeFi üzerinden fazlasıyla eleştiri alıyorlar. Zira normalde masumane bir şekilde kâr almak için kafa patlatıp yaptığınız bir işlem ile alacağınız kâr, bir bot tarafından anında kopyalanıp elinizden kaçabiliyor. Belki de ilk kez bu olayla birlikte bu botların 'hayırlı bir iş' için kullanıldığını gördük. c0ffeebabe.eth isimli bir bot operatörü saldırganın önüne geçip tam 5.4 milyon ABD Dolarına eş parayı eline geçirdi ve Curve'e [geri gönderdi](https://www.theblock.co/post/242136/mev-bot-runner-c0ffeebabe-eth-returns-5-4-million-amid-curve-exploit).

Çalınma olayı olduğu için botun devreye girmesi güzel. Burada açık kalan soru, bu botların hareketlerinin ne zaman 'makul' ne zaman 'haddini aşar' olarak değerlendirileceği ve çizginin nereden çekileceği?

Burada eklenebilecek bir başka nokta da, DeFi dünyasının bu tip saldırılar karşısında bir bütün haline gelip sistemi ve düzgün aktörleri korumaya çalışması. Bu oldukça değerli bir özellik. Nitekim bu olay sonrası, DeFi dünyasında pek çok açığı ortaya çıkaran samczun başta olmak üzere bir grup güvenlik uzmanı ve beyaz şapkalı hacker; protokollerin herhangi bir saldırı ile karşılaştıklarında kendilerine direkt olarak ulaşabileceklerini bir yardım hattı [kurdu](https://twitter.com/samczsun/status/1688613385565528064). Bu tarz insiyatifler, sektör içinde ortaya çıkacak olan kendi kendini regülasyon standartları ve blokzincirin şeffaf yapısı sayesinde olası riskleri en aza indirebilir. 

#### Salgın riski

Curve'de yaşanan sorunun, özellikle kurucusu Michael Egorov'un sahip olduğu CRV tokenlerini farklı kredi platformlarında teminat olarak kullanmasının Aave platformunu nasıl sıkıntıya soktuğuna bir önceki yazımızda değinmiştik. 

İşte DeFi'deki önemli problemlerden biri de bu platformlar arasındaki müthiş iletişim. Benzer riskler geleneksel piyasalarda yok mu? Var tabii. Bazen bir ülkede bir kriz çıkıyor ve bakıyorsunuz diğer büyük ülkelerin merkez bankaları bir anda ortak hareket ederek krizi önlüyorlar. DeFi'de işte böyle bir 'büyük abi' yok. Gerek var mı? Bana sorarsanız yok, zira DeFi'nin amacı 'küçük TradFi' olmak değil ki! 

Peki nasıl çözülecek bu sorun? Piyasanın bu olaylardan gereken dersler çıkarmasıyla. Mesela, Egorov'un elinde bu kadar büyük bir CRV tutuyor olması kimseyi ilgilendirmez ama Aave platformunda bu kadar büyük montanlı işlem yapıyor olması engellenebilirdi. Aave kendini 'biz yeterli miktarda teminat aldık' şeklinde avutmak isteyebilir ancak burada da klasik kredi dünyasından alacağı belli dersler var. Siz kendinize yeterli miktarda teminat aldığınızı düşünebilirsiniz; ancak o piyasada o teminatı bozdurmaya yetecek kadar likidite yoksa, satmaya kalktığınızda tokenin değeri sıfıra kadar düşer, sizin de teminatınız pula döner. Nitekim bu durum birkaç ay önce Aave forumlarında [dillendirilmiş](https://governance.aave.com/t/gauntlet-recommendation-to-freeze-crv-and-set-crv-ltv-0-on-aave-v2/13644) ancak bu konuda verilen önlem önerisi Aave DAO'su tarafından [reddedilmişti](https://app.aave.com/governance/proposal/246/). Burada belki de üzerinde durulması gereken konu,  borç verme platformlarındaki verilen krediler için istenecek teminat oranının DAO üyeleri tarafından mı, yoksa bu alanda uzmanlaşmış özel ekipler tarafından mı belirlenmesi gerektiği[^4].

#### Ve diğer ufak tefek sorular:
Bunun yanında ufak tefek sorular da 'sinek küçük' misali mide bulandırabiliyor. Örneğin, Egorov'un hareketleri. Büyük ihtimalle vergiden kaçmak için 100 milyon ABD Dolarından fazla miktarda CRV'yi teminat gösterip borçlanması. Sonra da gidip bununla Avustralya'da iki malikane alması. Piyasada serbest dolaşan (kilitlenmemiş) CRV'lerin (son satış öncesi) %50'sine sahip olması ([iddiası](https://twitter.com/apes_prologue/status/1669121532356902913)). Kurucusu olduğu yapının tokenlerini 'şaibeli' yatırımcılara satması.  Öte yandan merkeziyetsiz (aracısız) dünyanın bayraktarlığını yapan Curve'ün, başı sıkışınca saldırganın gerçek ismini ortaya çıkarmak (İngilizce de doxxed olarak geçer) için ödül koyması ve kendisi ile mahkemede hesaplaşacağını [açıklaması](https://etherscan.io/tx/0xc45e47f6e7d3e74763032e2fb991fa9a003d8ed55c13c93c6a5368ff322d7742). 

### Sonuç 
Curve saldırısı DeFi tarihine kara bir leke olarak geçecek. Yine de, bu olayı 'aman DeFi bitti' şeklinde okumak yerine, gerekli dersleri çıkararak yola devam etmek en mantıklısı gibi görünüyor. Bundan üç yıl önce DeFi hakkında yazmaya başlarken, büyüme sancıları ile birlikte pek çok yol kazası olacağını belirtmiştim. Açıkçası şimdiye kadar gerçekleşen kazalar şahsi beklentimin çok altında kaldı (tabii bunun bir nedeni DeFi yazından sonra gelen uzun kış ayları olabilir). Bundan sonra da krizler olmaya devam edecek (örneğin bir noktada stabil paralardan kaynaklanan büyük bir kriz de bekliyorum ama kanıtlayamam 😁) DeFi, içinde barındırdığı sağlam oyuncuların ayakta kalması, protokollerin gerekli standartları yavaş yavaş oturtmaya başlaması ve  yaşadığı krizlere topluluğun birlikte tepki vermesi sayesinde bu olaylara 'beni öldürmeyen güçlendirir' şeklinde bakarak yoluna devam etmeli. 

[^1]: Biraz daha tekniğe girersek. Ethereum üzerindeki akıllı kontratlar genelde Solidity diliyle yazılıyor ancak Solidity kullanılan tek dil değil. Başka rakip diller de var ve bunların arasında en çok kullanılanı Viper. Curve ekibi de akıllı kontratlarını Viper ile yazıyorlar. Viper yazılımının kimi versiyonlarında tekrar giriş saldırısı (ingilizcesi re-etnrancy attack) denilen bir saldırıya karşı güvenlik önleminin çalışmadığı anlaşılmış. Bu atak genelde şu şekilde çalışıyor. Yazılıma 'hesabımda duran şu parayı bana gönder' demenizin ardından size para geldikten hemen sonra, hesabınız güncellenmeden tekrar yazılımdan para istiyorsunuz. Normalde yazılımın bu durumu engellemesi gerekir ancak Viper da bu çalışmadığı için saldırgan hesabı güncellenmeden tekrar tekrar istekte bulunarak havuzdaki tüm parayı çekmiş. Burada dikkat çeken bir nokta da, her ne kadar Curve ekibi 'bu bizim suçumuz değil' dese de, Curve'ün Viper dil geliştirmesinin en sıkı destekçilerinden biri olması, üstüne üstlük yukarıda bahsettiğimiz 'açığa neden olan kodun' olduğu versiyonun github'a yüklenmesinin (canlıya geçmesi olarak da düşünebilirsiniz) Viper'da gönüllü çalışan bir Curve ekibi üyesi tarafından yapılmış olması. 

[^2]: Burada Viper'daki hatanın Temmuz 2021'de yayınlanan bir sürümde yaşandığını ve bu hatanın Ağustos 2021'de yapılan bir güncelleme ile düzeltildiğini hatırlatalım. Peki Curve'deki sorun? Curve'ün akıllı kontratının tam bu bir aylık sürede oluşturulup Ethereum sistemine yüklenmiş olması!

[^3]: Bu tip havuzda bekleyen işlemlerin önüne geçmek (ingilizcede 'frontrunning') denen olay, klasik piyasalarda da sık karşılaşılan bir sorun aslında. Ethereum sistemi bu tip hareketlerin önüne geçebilmek için havuzlara gönderilen işlemlerin şifreleyecek belli çözümler için uğraşıyorlar ama henüz net bir gelişme yok. 

[^4]: Aslına bakarsanız, Aave'nin yeni üçüncü versiyonunda bu tip borçlanmalara bir sınır getiriliyor. Burada sorun bu borçlanmanın Aave'nin ikinci versiyonunda yapılmış olması. Çözüm borç verenlerin eski kontratı değil yeni kontratı kullanmaları olabilirdi.

---

*Not 1: Bu yazı ilk olarak 14 Eylül 2023'de [BTCHaber'de yayınlandı]()*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

