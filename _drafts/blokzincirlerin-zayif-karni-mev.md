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

# Yazı II Flashbots MEV sorununu çözebilecek mi?
Bu yazımızda, Ethereum protokolü oyuncularının en çok tercih ettiği yazılımın sahibi olan Flashbots ekibinin, MEV (Maximal Extractable Value) ve merkezileşme konularında şimdiye kadar yaptıklarını ve bundan sonraki hedeflerini gözden geçireceğiz. 

MEV (Maximal Extractable Value), Ethereum (ve Cosmos benzeri diğer blokzincirler) üzerindeki işlemlerin sıralarının değiştirilerek, işlem ücretlerini artırabilmek için yapılan her tür düzenlemeye verilen ad. Detaylarını ve bu konuda yaşananları bir [önceki yazımızda] bulabilirsiniz. 

Bu yazımızda, gelin önce MEV konusunda özellikle [Flashbots](https://www.flashbots.net/) tarafından geliştirilen önlemlere bakalım. Sonrasında ise Flashbots'un gelecek planlarına değinelim. 

### Flashbots MEV'ye nasıl çözümler getirdi?

MEV'nin kullanıcılara verdiği zararın ayyuka çıkması sonrası, farklı geliştirici grupları tarafından bu soruna çözüm bulunabilmesi amacıyla pek çok öneri ortaya atıldı. Bu çözüm önerileri içinde en çok tutulanı bir araştırma kuruluşu olan Flashbots'un geliştirmeleri oldu. Hızlıca neler yaptıklarına bir göz atalım:

Flashbots genel olarak MEV sorununu temelden çözmek yerine, yarattığı sorunları azaltmaya ya da idare edilebilir hale getirmeye odaklanan bir oluşum. Adlarını ilk olarak 2020 yılında çıkardıkları [MEV-Geth](https://github.com/flashbots/mev-geth) isimli Ethereum yazılımı ile duyurdular. Yazılımın temel fonksiyonu, madencilere gelen işlem emirlerini açık bir pazaryerinde ihaleye çıkararak daha görünür yapmak. MEV-Geth sayesinde madenciler kendilerine gelen bu emirleri  daha rahat işlemeye başladılar. Sonuçta hem sistem üzerindeki gereksiz işlem kalabalığı önlendi, hem de madencilerin kârları arttı[^3].

Yazılım o kadar başarılı oldu ki, Nisan 2021 itibariyle ETH üzerindeki işlemlerin %84'ünü gerçekleştiren madenci havuzları MEV-Geth yazılımını kullanır hale geldiler. 

### Merge sonrası neler değişti?

Ethereum'un 15 Eylül sonrası uygulamaya giren yeni versiyonunda artık madenciler yok. Onların yerini Ethereum sistemine ETH'lerini rehin etmiş (ingilizcesi stake) onaylayıcılar aldı. Yeni versiyonda işlemler şu şekilde yürüyor:

- Kullanıcı işlemini cüzdanı üzerinden imzalar ve genel işlem havuzuna gönderir (ya da bu iş için kurulan özel aracılara) 
- Araştırmacı/tarayıcı (ingilizcesi 'Searcher') kârlı işlemleri bir araya getirip, blok üreticilerine verir. 
- Blok üreticileri, blokları üretip onaylayıcıların onayına sunar. 
- Onaylayıcılar ise kendilerine sunulan bloklardan en kârlısını (en yüksek işlem ücreti önereni) onaylayarak blok oluşumuna izin verir

| ![Ethereum_sistemi_oyunculari](/assets/ethereum_sistem_oyunculari_v5.jpg)|
|:--:| 
| *Yeni Ethereum sistemindeki oyuncular. Eskiden madenciler hem blok üretimini hem de onaylamasını yapıyorlardı. Yeni sistemde, blok üretimi daha merkezi ve güçlü yapılarla, blokların onaylanması ise daha hafif ve merkeziyetsiz onaylayıcılar tarafından yapılacak*|

Ethereum geliştiricileri, özellikle bloğu oluşturanlar ile onaylayanları ayırarak adeta bir güçler ayrımı yapmaya çalışıyor. Zira, her iki işi bir arada yapabilmek oldukça zahmetli ve yüksek kapasite gerektiriyor. Her makine yüksek kapasite ile işlem yapamayacağı için ikisini bir arada yapmak sistemin merkezileşmesi tehlikesini doğuruyor. O nedenle, Ethereum blok üreticilerinin uzman haline gelip yüksek kapasite ile işlem yapmasına dolayısıyla merkezileşmelerine izin verirken, onaylayıcıların yüklerini hafif tutarak o tarafı merkeziyetsiz hale getirmeye çalışıyor. Yani bir nevi onaylayıcı tarafı için blok üretici tarafını feda ediyor. 

İdeal hedeflenen sistem işleyişi şu şekilde: Tarayıcılar, olabildiğince kârlı işlemleri demet haline getirip blok üreticilerine sunarlar. Blok üreticileri de bunlardan kendilerine en çok işlem ücreti ödeyen tarayıcıların demetlerini seçerler. Benzer şekilde blok üreticileri de, ürettikleri blokların kabul görüp işleme alınması için olabildiğince fazla kârı onaylayıcılara teklif ederler. Yani işlem ücretleri zincirin sonundaki onaylayıcılara doğru akar. 

Yeni durumda MEV ne olacak? Sistem, yukarıdaki tarayıcı, blok üreticileri arasındaki rekabeti artırarak ortaya çıkan MEV'yi olabildiğince onaylayıcı tarafına aktarmaya çalışıyor. 

### Flashbots cephesinde ne gibi gelişmeler oldu?

Ethereum'un yeni versiyonu ile birlikte, Flashbots eski sistemde kullandığı MEV-Geth yazılımının yerine Ethereum'un yeni sistemine hazırlık için [MEV-Boost](https://github.com/flashbots/mev-boost/) yazılımını uygulamaya aldı. 

Aslına bakarsanız MEV-Boost Ethereum'un gelecekteki yol haritasının önemli bir parçası ve sistem oyuncuları arasında 'kuvvetlerin ayrılığı' prensibini getirecek olan PBS (blok teklif edenler ile blok üreticilerin ayrılması İngilizce proposer-builder-separation) geliştirmesinin bir ön provası olarak görülebilir. Bu yazılım, gerek tarayıcılar gerekse blok üreticileri tarafından kullanılan şeffaf bir sistem. Blok üretim işini makinelerin tek başlarına yapmak yerine büyük blok üreticilerine devretmesini (outsource etmesini) sağlayan bu sistem, o kadar başarılı oldu ki, şu an [üretilen blokların %90'ında MEV-Boost yazılımı kullanıyor](https://explore.flashbots.net). 

Bu sefer de başka bir sorun ortaya çıktı. O da Flashbots'un işlem taleplerini tarayıcılardan blok üreticilerine ileten kendi aracıları (bunlara taşıyıcı da denebilir ingilizcesi relayer) üzerinden gelen işlemlere sansür uygulaması. Flashbots ABD'de kurulu bir şirket. ABD'nin kara para aklama ile ilgili iki kuruluşundan biri olan OFAC'ın Tornado Cash uygulamasını ve bu uygulamaya kullanan adresleri kara listeye aldığına [önceki bir yazımızda](/genel/2022/08/31/Ethereum-sansure-nasil-tepki-verecek.html) değinmiştik. İşte, Flashbots da bu yaptırımlara uyarak, kendine ait taşıyıcılara sansür uygulamaya başladı. 

Bunun sonucu olarak yeni versiyona geçtikten sonra Ethereum üzerindeki işlemlerin yaklaşık %72'si sansürlenmeye başladı. Aşağıdaki tabloda, 15 Eylül'den bu yana oluşan bloklardaki işlemleri görüyorsunuz.

| ![Ethereum_bloklar](/assets/ofac-compliant-blocks_v2_800.jpg)|
|:--:| 
| *Ethereum'un yeni versiyonu sonrası durumu. Oluşturulan blokların %90'ı Flashbots'a ait olan MEV-Boost'u kullanıyor. Tüm blokların %72'si ise OFAC ile uyumlu blok üreticileri tarafından oluşturulmuş. MEV-Boost kullananlardan %21'lik bir kesim ise Flashbots taşıyıcısı kullanmamış, yani sansür uygulamamış. %10'luk bir kısım ise MEV-Boost kullanmayanlar tarafından üretilmiş. Kaynak: [MEV Watch](https://www.mevwatch.info)*|

Tabloda, gördüğünüz gibi MEV-Boost kullanan blok üreticileri toplam blokların %90'ını üretmişler. Bunların içinde %72'si Flashbots taşıyıcı kullanmış. Burada hemen MEV-Boost yazılımı ile Flashbots taşıyıcının farkından bahsetmek gerekiyor. MEV-Boost bir yazılım ve isteyen herkes tarafından kullanılabiliyor. Flashbots bu yazılım ile birlikte otomatik gelen bir taşıyıcı ama isteyen bu taşıyıcıyı değiştirebilir. Aynı eskiden Windows bilgisayarlarda otomatik varsayılan tarayıcının Internet Explorer olması gibi. MEV-Boost en fazla kâr getiren yazılım olduğu için tarayıcı ve üreticiler tarafından en çok tercih edilen yazılım. Bu üreticilerden bir kısmı OFAC listesine uymak için Flashbots taşıyıcı kullanıyor, ufak bir kısmı (yukarıda sarı alanda gördükleriniz) ise MEV-Boost kullanmaya devam edip sansüre karşı olan başka taşıyıcılara geçmiş durumda. 

### MEV ve merkezilik önlenebilir mi?
"Bu sistem adil değil, MEV önlenemez mi?" diye soracak olursanız, buna Ethereum özelinde kesin bir cevap yok.  Burada temel hedeflenen, önce MEV'nin kullanıcıya olan etkisini minimuma indirmek, sonra da kalan MEV'nin tarayıcı ya da blok üreticilerine değil de, onaylayıcılara gitmesini sağlamak gibi görünüyor.  

Flashbots benzeri ürünler, MEV'nin azaltılmasını ve daha adil bölünmesini sağlıyorlar. İleride, Ethereum'un yeni sistemi oturduğu zaman, eğer hedeflenen rekabetçi yapı gerçekleşirse, MEV'in ağırlıklı bir kısmı sistemi koruyan onaylayıcılara gidecek. Onaylayıcılar, ETH stake ederek işlemleri onaylıyorlar ve sistemin güvenliğini sağlıyorlar. Böylece MEV bir nevi sistemin güvenlik bütçesine katkı yapmış olacak.[^4] 

Ethereum'un geliştirmeleri maalesef uzun zaman alıyor. Bu süre zarfında ne olacak peki? Burada Flashbots, geçtiğimiz günlerde [SUAVE isimli yeni çalışma yayınlayarak](https://writings.flashbots.net/the-future-of-mev-is-suave/) oluşan sorunlara çözüm bulmayı hedeflediğini açıkladı. Neler bunlar?

SUAVE'nin birkaç hedefi var. Bunlardan birincisi, MEV ile ortaya çıkan değerin kullanıcılara geri verilmesi - ki bu MEV'in kötü kullanımından kurtulmanın en büyük çözümü olabilir. Nasıl olacak bu? İşlemlerin gizlilik içinde sıralanması yoluyla. 

SUAVE'nin ikici hedefi, blok üreticilerine sadece Ethereum değil, diğer alternatif blokzincir ağlar (Cosmos, Avalanche gibi) ya da ikinci seviye altyapılar (Arbitrum, Optimum gibi) ile entegre olabilecekleri bir sistem sunmak. SUAVE yukarıda yazdığımız sıralama işlemini tüm ağlarda yaparak blok üreticilerine sunacak. Bu sayede blok üreticilerinin de SUAVE kullanımı özendirilecek. 

Üçüncü önemli nokta ise, çok güçlü ve sayıca az olan blok üreticilerinin arasındaki rekabetin artabilmesi için oluşturulan SUAVE'nin olabildiğince merkeziyetsiz bir hale getirilmesi.[^5]

Kısacası, Flashbots burada Ethereum'un yol haritasında yer alan güçlü blok üreticilerinin daha merkeziyetsiz olmasını sağlayacak ve bu sayede oluşan rekabet sonucu MEV'nin kullanıcılara geri verileceği bir çözüm vaadi ile geliyor. Bunu başarabilecekler mi, heyecanla izleyeceğiz. Şu ana kadar yaptıkları iki hamlede (MEV-Geth ve MEV-Boost) elde ettikleri pazar payı başarısı, üçüncü hamlenin yapılabilirliği konusunda bir referans sağlasa da, bu sefer altına girdikleri yükün çok daha ağır olduğunu belirtmek gerek. 

### Sonuç 
Flashbots, geliştirdiği MEV çözümleri ile madenciler (Ethereum'un eski versiyonunda), tarayıcılar ve blok üreticileri arasında şeffaflık sağlamaya başarırken, merkezilik ve sansür konularında tıkandı. Yeni çıkan SUAVE sürümü ile bu sorunlara da çözüm bulmak için uğraşıyorlar. Bunda başarılı olacaklar mı, hep birlikte göreceğiz. 

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

[^3]: "Bu iki problemi nasıl çözdüler?" diye soracak olursanız: Önceden kullanılan 'en yüksek parayı veren en yukarı çıkar' yönteminde tarayıcılar blokzincir üzerine emir göndererek işlemlerini önceliklendirmeye çalışırlardı. Bu da pek çok başarısız emir nedeniyle zincirin gereksiz yere dolmasına neden oluyordu. MEV-Geth ile işlemleri demetler (ingilizcesi bundle) haline getirip, zincir-dışı olarak göndermeye başladılar. Oluşturulan pazaryerinde tarayıcılar hazırladıkları demetleri gönderiyorlar ve MEV-Geth en kârlı olanları alıp işleme sokuyor. Böylece madencilerin de kârı artıyor. 

[^4]: Bu alanda merkeziyesizliği teşvik etmek için Flashbots'un Flashbots Builder isimli blok üreticisi yazılımı [açık kaynak haline getirdiğini](https://writings.flashbots.net/open-sourcing-the-flashbots-builder) de ekleyelim. 

[^5]: Blok üreticilerindeki merkezileşmeye en iyi örnek, Kasım ayının son bir haftasında [en büyük 5 üreticinin toplam blokların %85'ini üretmiş](https://www.relayscan.io/overview?t=7d) olması
