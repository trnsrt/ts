Blokzincirlerin zayıf karnı MEV

Bu yazımızda başta Ethereum olmak üzere hemen hemen tüm akıllı kontrat platformlarının zayıf karnı olarak adlandırılan MEV olayının üzerine gidiyoruz. 

Ethereum blokzinciri üzerinde son zamanlarda çok konuşulan ama teknik olduğu için anlaşılması zor konulardan biri de MEV. İlk olarak Miner Extractable Value olarak tanımlanan ama sonradan Maximal Extractable Value olarak değiştirilen bu kavram, kimilerine göre blokzinciri saran bir kangren, kimine göre ise faydalı bir enstrüman. Bu ilk bölümde gelin nedir, neye yarar, ona göz atalım: 

### Nedir MEV? 

MEV'nin ne olduğu anlamak için öncelikle Ethereum'da işlemler nasıl gerçekleşiyor, onu anlamak gerekli. 

Siz bir kullanıcı olarak işlem yapmak istediğinizde işleminizi Ethereum'da bekleyen işlemlerin olduğu havuz atıyorsunuz. Bunu yaparken cüzdanınızın bağlı olduğu bir bağlantı noktası (buna ingilizcede remote procedure call nodes kısaca RPC deniyor) kullanıyorsunuz. Havuzda toplanan işlemlerin derlenip toparlanıp bloklara yazılmasından eskiden madenciler sorumlu idi. Gelen işlemleri hangi sıra ile yazacaklarına madenciler karar veriyorlardı. Genelde de burada 'parayı basan blokzincirde yerini alır' prensibi geçerliydi (ki bu prensip hâlâ devam ediyor). 

#### Ne gibi sorunlar yaratıyordu?
Ethereum yoğun bir ağ ve içinde her bir bloğun üretiminin 12-15 saniye sürdüğü düşünülürse, bu sistemde biriken pek çok işlem emri demek. Havuzda bulunan bütün işlemler herkes tarafından görülebildiği için, gönderilen işlemlerin hangi öncelikle blokzincire yazılacağı konusunda ciddi bir manipülasyon yapılma şansı var. İşte işlemlerin sırasının yeniden düzenlenmesi yoluyla blokzincire ödenen işlem ücretlerini artırma olayına MEV deniyor. Peki kim neden yüksek işlem ücreti verir? Bu zararlı mıdır, yoksa yararlı mı? Birkaç örnek ile anlamaya çalışalım:

Yüksek işlem ücreti vermenin en temel nedenlerinden biri **arbitraj fırsatları**. Bu aslında oldukça basit şekliyle, farklı piyasalar arasındaki fiyat dengesizliğinden yararlanma demek. Diyelim ETH'nin fiyatı A merkeziyetsiz borsasında hızlı bir şekilde düştü. Bunu fırsat bilen bir arbitraj uzmanı, A borsasında ETH satın alıp,  aynı anda bu ETH'yi fiyatı daha yüksek olan B merkeziyetsiz borsasında satabilir. Riski çok az, kârı net bir işlem. Ama bunu yapabilmek için her iki borsada da herkesten önce işlem yapmalı, aksi takdirde başkaları bu fırsatı değerlendirebilir. Sırada öne geçmeyi ancak madenciye çok yüksek bir işlem komisyonu ödeyerek sağlayabilirsiniz. Bu tip bir arbitraj, farklı piyasalar arasındaki fiyat farkını en aza indirdiği için iyi niyetli olarak adlandırılabilir. Bu kadarla kalsa iyi ama tabii ki MEV işinde kötü niyetliler de var. 

Bu alanda sevilmeyen işlemlere baktığımızda bunların en başında '**sandviç atak**' geliyor. Sandviç atak, temel olarak, birinin verdiği yüklü bir emrin önüne ve arkasına emirler koyup (adeta orijinal emri sandviç yaparak) o kişinin kârından bir parçayı cebe atmak demek. Örneğin, bir kişi, merkeziyetsiz bir havuzdan yüklü miktarda ETH satın almak istedi. Genelde böyle bir durumda alıcı, havuzdaki sığlıktan dolayı alım yaptığında o anki fiyatın biraz yükselebileceğini kabul ederek işleme girer (ingilizcede slippage denen örneğin %1'lik bir değişim). Alıcının verdiği emir, emirlerin toplandığı havuza düştüğünde (ki emirlerin havuza düştüğünde herkes tarafından görülebildiğini az önce belirtmiştik) bunu gören bir kullanıcı, madenciye yüksek işlem ücreti ödeyip bu işlemin önüne geçer. Yani? Henüz düşük fiyattaki ETH'yi satın alır, sonrasında büyük alıcının işlemi gelip, ETH fiyatını yükselttikten sonra elindeki ETH'yi yükselmiş fiyattan satar.

#### Ne kadar önemli?
MEV'nin buna benzer başka pek çok örneği var, ama yukarıdaki iki konu bu alandaki gelirin büyük bir kısmını oluşturuyor[^1]. Peki çok önemli bir konu mu bu?  MEV ile şu ana kadar [682 milyon ABD Doları değerin elde edildiğini](https://explore.flashbots.net) söylersek olayın büyüklüğünü kavrayabiliriz belki[^2]. Kimin cebinden çıkıyor peki bu MEV? Kullanıcıların cebinden. 

| ![mev-over-time](/assets/mev-over-time_v3_800_.png)|
|:--:| 
| *MEV'nin zaman içinde değişimi. Gördüğünüz gibi başlangıçta çok daha fazla iken zaman içinde azalıyor. Kaynak [Flashbots](https://explore.flashbots.net)*|

Bu arada sorunun sadece işlemi gerçekleşmeyen ya da verdiği emirde yüksek fiyattan işlem yapmak zorunda kalan kullanıcılar ile sınırlı olmadığını belirtelim. Hedefledikleri bloklarda işlemlerin yer almasını isteyen kişiler, işlemlerin gerçeklemesini sağlayabilmek için adeta emir üzerine emir yağdırarak, hem blokların dolmasına hem de genel olarak işlem ücretlerinin artmasına neden oluyorlar. Bu nedenle sizin masum işlemleriniz hem geç hem de daha yüksek bir maliyetle gerçekleşiyor. 

### MEV çözülebilir mi, çözmek gerekli mi?

Blokzincirler üzerinde MEV problemine henüz kökten bir çözüm getirildiği söylenemez. Önce şu ana kadar yapılanlara bakalım, sonra da yönümüzü geleceğe çeviririz:

#### MEV konusunda şimdiye kadar neler yapıldı?

Şu ana kadar bu alanda yapılan geliştirmeler içinde en çok tutulan çözüm MEV'nin etkilerini azaltmayı hedefleyen araştırma kuruluşu [Flashbots](https://www.flashbots.net/) tarafından geliştirilen [MEV-Geth](https://github.com/flashbots/mev-geth) ve [MEV-Boost](https://github.com/flashbots/mev-boost/) uygulamaları oldu. Bu yazılımlar temel olarak, kullanıcıdan blokzincire uzanan zincir üzerindeki tüm oyunculara şeffaf bir oyun alanı getirerek, sistem üzerindeki verimsizlikleri ortadan kaldırdılar ve neredeyse [oyuncuların %90'ı tarafından kullanılır](https://explore.flashbots.net) oldular. 

#### Flashbots iyi güzel ama sorunları var

Flashbots tarafından geliştirilen yazılımlar ve bunları kullanan taşıyıcılar, başarılı olmasına oldu ama bu sefer de, Ethereum ekosisteminde bir başka sorun ortaya çıktı. Yazılımı geliştiren ABD'li ekip, işlemler üzerinde sansür uygulamaya başladı (ABD'de Tornado Cash ile başlayan sansür konusunu daha önceki [şu yazımızda](/genel/2022/08/31/Ethereum-sansure-nasil-tepki-verecek.html) detaylıca anlatmıştık). 

#### Sorun kökten çözülemez mi?
Sorunu temelden halledebilecek iki çözüm geliyor akla: Birincisi, işlemleri emir verildiği zaman sırasına göre dizecek bir altyapı (böylece daha fazla para veren öne geçemeyecek). Bu her ne kadar bir çözüm gibi görünse de, gerçekten yapılmalı mı tartışmalı. Zira, MEV içinde piyasaları düzelten arbitraj gibi 'iyi huylu' olanlar da var. Eğer bir kullanıcı arbitraj fırsatı değerlendirmek istiyorsa ve bunun için daha fazla işlem ücreti ödemeye razıysa, neden onu engelleyesiniz ki? Bırakın, daha yüksek ücret versin, böylece sistemi yürütenler kazansın. 

Burada ikinci ve asıl konu sandviç atak gibi durumlarıda ortaya çıkan 'kötü huylu' MEV'leri engellemekte. Bunu yapabilmenin yolu da işlem havuzuna düşen emirlerin görünürlüğünü engellemek. Böylece emrin önüne ve arkasına işlem konulamasın. Peki bu nasıl sağlanabilir? Tüm işlem emirlerini şifreleyerek işlemler üzerindeki manipülasyonu önlemek yoluyla.  

Yukarıdaki iki çözümden özellikle ikincisi, daha önce [bir yazımızda detaylıca anlattığımız](/genel/2022/09/30/ethereumun-gelecek-vizyonu-ne_v2.html) Ethereum'un önündeki yol haritasında net olarak ortaya konmuş durumda. Hatta bu konu o kadar önem kazandı ki, başlangıçta, yol haritasında beş grup çözüm sıralanmışken, sonradan yapılan [bir güncelleme](https://twitter.com/VitalikButerin/status/1588669782471368704?s=20&t=RqSWeroAk4yBbkp4hm85Hw) ile MEV yeni bir grup çözümü olarak (ceza/kamçılamak ingilizcesi 'The Scourge') eklendi.


#### Kökten çözüm gelene kadar Flashbots'un yeni önerileri var
Sorun şu ki, Ethereum'un ana geliştiricilerinin bu çözümleri yürürlüğe koyabilmeleri için daha bir hayli vakte ihtiyaçları var. İşte burada devreye yine Flashbots girme niyetinde. Şu ana kadar sorunları çözme konusunda Ethereum'a bir hayli yardımcı olan Flashbots geliştiricileri, geçtiğimiz hafta içinde [SUAVE adını verdikleri yeni versiyonda](https://writings.flashbots.net/the-future-of-mev-is-suave/), hem MEV'lerin etkisini azaltma hem de Ethereum'daki sansür sorununa çözüm olabilecek daha merkeziyetsiz bir sistem önerisinde bulunuyorlar.  Flashbots konusuna önümüzdeki hafta devam edeceğiz. 

### Arkası Yarın

MEV, Ethereum başta olmak üzere blokzincirlerin çözmeleri gereken önemli bir sorun. Bu alanda yaptığı geliştimeler  ile bir dereceye kadar başarılı olan Flashbots ekibinin çözümleri şimdilerde sansür nedeniyle zorlanıyor. Ethereum'un ana geliştiricilerinin de sorunlara çözüm bulmak için zamana ihtiyaçları var. Bu süre zarfında Flashbots'un yeni sürümü SUAVE sorunlara ne kadar çözüm olabilecek hep birlikte yakından izleyeceğiz. MEV bir süre daha gündemi meşgul etmeye devam edecek gibi görünüyor. 

---

Kaynaklar:

[MEV in DeFi](https://etherworld.co/2022/04/05/mev-research-report/#section111) - araştırma raporu 

[The Future of MEV is SUAVE](https://writings.flashbots.net/the-future-of-mev-is-suave/)  - Flashbots post

[MEV Manifesto](https://members.delphidigital.io/reports/mev-manifesto) Delphi Digital raporu

MEV Markets Part 1 - "[PoW](https://mirror.xyz/0xshittrader.eth/WiV8DM3I6abNMVsXf-DqioYb2NglnfjmM-zSsw2ruG8)",  Part 2 - "[PoS](https://mirror.xyz/0xshittrader.eth/c6J_PCK87K3joTWmLEtG6qVN6BFXLBZxQniReYSEjLI)",  Part 3 - "[Payment for Order Flow](https://mirror.xyz/0xshittrader.eth/f2VSuoZ91vAbCv82MtWM-Gosyf_DeUXfPlDx3EYV3RM)" yazıları

Konuya daha fazla ilgi duyanlar, bu alandaki tüm önemli kaynakları bir araya toplayan [şu GitHub sayfasına](https://github.com/0xemperor/Awesome-MEV) da göz atabilirler. 


Dipnotlar:

[^1]: Genelde bu sorunlar sandwich attack (front running+back running), time-bandit/uncle-bandit attacks, liquidations olarak adlandırılabilir. Genelde arbitrage MEV'lerin %90'ına denk. Bu konuda daha detaylı bilgilere [şu yazıdan](https://etherworld.co/2022/04/05/mev-research-report/) ulaşabilirsiniz. 

[^2]: Bu oluşan değerin %64'ü madencilere işlem ücreti olarak ödendi, kalanı ise bu işlemi yapanlar tarafından cebe atıldı. Tüm detaylı istatistiklere [şu bağlantıdan](https://explore.flashbots.net) ulaşabilirsiniz. 
