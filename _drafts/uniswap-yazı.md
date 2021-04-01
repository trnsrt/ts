Bu yazımızda geçtiğimiz hafta içinde açıklanan merkeziyetsiz takas borsası Uniswap'ın yeni versiyonuna bakacağız hep birlikte: 

Uniswap, merkeziyetsiz finans dünyasının ağır toplarından. Daha önce kendisi ile ilgili iki yazı yazmıştık: Birincisi [Uniswap ve sahip olduğu havuz sistemini](https://turansert.com/genel/2020/09/15/nedir-bu-uniswap.html), ikincisi ise [rakiplerini ve farklarını](https://turansert.com/genel/2020/09/22/uniswap-rakipleri-curve-balancer-ve-sushiswap.html) anlatıyor. Önce gelin bu yazımızda hafızamızı tazeleyecek bir özet geçelim, şu anki sıkıntıları neymiş görelim, sonraki yazımızda da yeni versiyon neler getiriyor ona bakarız. 

### Neydi bu Uniswap?
Uniswap, klasik borsaların yaptığı hisse alım satım işlemlerini merkeziyetsiz bir şekilde gerçekleştiren bir DeFi protokolü. Sisteminin çalışması klasik borsalardan farklı: 

Klasik borsalarda her bir token ya da hisse senedi için işlem ekranları vardır. Alıcı ve satıcılar işlem yapmak istedikleri miktarları ve fiyatları yazarlar, sonrasında bu taleplerine bir karşılık bulurlarsa işlem gerçekleşir. Bunlara emir defteri işlemleri denir. 

Uniswap ise farklı bir şekilde çalışıyor: Merkeziyetsiz borsalar alım satım işlemleri için yeterince likidite bulamadığından çözüm olarak havuz sistemini kullanıyor. 

"Nedir bu havuz sistemi?" diye soracak olursanız: Bu sistemde her bir havuzun içinde iki adet token var. İşlem yapmak isteyenler bu ikili tokenlardan birini alıp diğerini koyuyor havuza, yani takas yapıyor. Dolayısıyla al-sat yapanlar birbirlerine karşı değil sürekli likidite barındıran bir havuza karşı işlem yapıyorlar.  

Peki havuza tokenları başta kim koymuştu? Likidite sağlayıcı dediğimiz yatırımcılar. Neden likidite sağlıyorlar bu insanlar? Çünkü havuzda takas yapanlar yaptıkları her işlem için komisyon veriyorlar (Uniswap'ta bu binde üç oranında).. İşte bu komisyonların neredeyse tamamı likidite sağlayıcılara gidiyor. 

### Neden başarılı oldu?
Uniswap'ın başarılı olmasının küçük büyük pek çok nedeni var. 

Birincisi basit ve şeffaf bir sistem.. Token fiyatları çok basit bir algoritma ile belirleniyor. Her bir havuzda iki token var ve %50-%50 havuzu paylaşıyorlar. Komisyon oranı her havuz için binde üç. Özellikle likidite sahipleri için, 'koy paranı havuza unut git, sonra komisyon gelirlerini topla' şeklinde adlandırılabilecek bir sistem. Al-sat yapanlar için de likidite sıkıntısı olmadan işlem yapabilecekleri bir borsa. 

İkincisi, tamamen merkeziyetsiz ve isteyenin istediği gibi havuz kurabildiği bir sistem.. Bu sayede eskiden finansman bulabilmek ya da tokenlarına likidite kazandırmak için kripto para borsalarının kapısı önünde dilenci gibi bekleyen DeFi ürünleri artık özgürce diledikleri anda halka açılma hakkı elde ettiler. Bu şekilde Uniswap'ta oluşmuş [150'nin üzerinde aktif havuz](https://info.uniswap.org/pairs) var. 

Son olarak, merkeziyetsiz DeFi platformu olarak 'müşterini tanı' yani KYC ilkelerinden uzak olmasının belli kesimleri Uniswap'a çektiğini söylemek de yanlış olmaz.

### Gelelim yeni versiyona

Unsiwap'ın yeni versiyonu (ki buna v3 yani üçüncü versiyon deniyor) 2021'in Mayıs ayı başında [piyasaya sunulacak](https://uniswap.org/blog/uniswap-v3/). Ethereum blokzinciri üzerinde olacak bu yeni versiyonun  hemen arkasından Mayıs ortası gibi de Optimism denen ikinci seviye çözüm devreye girecek. 

Üçüncü versiyonda temel olarak hissedilen, eskinin basit ve sadeliğinden uzaklaşan daha karmaşık bir yapının gelmekte olduğu. Bu değişim, farklı özellikler arayan al-sat işlemcileri ve büyük miktarda likidite sağlayanların işine gelecek ancak küçük hacimli likidite sağlayıcıların hayatları çok zorlaşacak. UNI token sahipleri de yeni özellikler sayesinde daha fazla gelir kazanma ihtimaline kavuşacaklar. Kısacası Uniswap,  DeFi dünyasını şu an oynadığı kum havuzundan daha büyük sahneye çıkarmak için uğraşıyor. Burada hemen  sonda yapacağımız yorumu da ekleyelim: eğer köklerini unutursa, oturduğu halının ayaklarının altından çekildiğini de görebilir her an.

Evet, dönelim Uniswap'ın mevcut sıkıntılarına ve yeni versiyonun neler getirdiğine:

### En büyük sorun: Sığ havuzlar.. 

Uniswap, sistemini dizayn ederken birinci temel ilkesini **havuzdaki likiditenin tükenmemesi** üzerine kurmuştu. Ne demek bu? Havuzu oluşturan iki token çeşidinden de her zaman bulunması ve bu tokenların hiçbir şekilde bitmemesi. Likidite bitmemesi güzel bir özellik ama pratikte belli sıkıntıları oluyor. Neler bunlar?

Birincisi, havuzun verimliliğini azaltıyor bu durum. Özellikle likidite sağlayıcılar için. Neden? Çünkü, bu ilke nedeniyle havuzda fiyat her ne olursa olsun alıcılara servis edilecek token bulundurması gerekiyor. Bu da 0'dan sonsuza kadar giden geniş bir aralık için emre amade token bulundurmak demek. 

Bir örnek ile açıklayalım. Geçtiğimiz iki buçuk yıl içinde 1 ETH'nin fiyatı 0.015BTC ile 0.045BTC arasında seyretmiş, bu aralığın dışına çıkmamış. Ama eğer yatırımcı Uniswap'taki ETH/WBTC havuzuna likidite sağlarsa bu para hem bu aralık için hem de aralığın dışı (örneğin 0.0005 BTC ya da 0.95 BTC) için de hazır bekletiliyor. Yani likidite sağlayıcı tarafında ciddi bir para işleme girmeden atıl kalıyor.  Neden atıl kalıyor? Hemen açıklayalım. 

Pratikte bu havuzda işlemler genelde 0.03-0.04 arasında hatta çok daha dar bir aralıkta gerçekleşiyor. Ama havuz parayı bu aralıkta tutmayıp her alana dağıttığından bu alana düşen likidite az kalıyor. Bir bidon suyu on metrekare havuza ya da 100 metrekare havuza döktüğünüz düşünün.  Havuz sığ kalınca, yüksek hacimli işlem olunca fiyatlar ani olarak düşüp yükselebiliyor. Bu hem likidite sağlayıcıya hem de işlem yapana sıkıntı yaratıyor:

Likidite sağlayıcı aslında havuzda para olmasına rağmen işlem yapılan alana yeterince para düşmediği için yapılan bir işlemin fiyata ani etki etmesi sonucu zarar ediyor (ki buna geçici kayıp ingilizcede impermanent loss adı veriliyor. Ne olduğunu ve nasıl çalıştığını [Uniswap yazımızda](/genel/2020/09/15/nedir-bu-uniswap.html) detaylıca anlatmıştık. Aşağıda dipnot olarak da verdik). Bu kayıp likidite sağlayacılar için kaçınılmaz bir şekilde var, ancak havuz sığ olduğunda etkisi daha vurucu oluyor. 

İşlem yapanlar ise, bir fiyattan almak için teklif verdiklerinde sıkıntı yaşıyorlar. Birincisi büyük bir emir verdiklerinde algoritma istedikleri fiyata çok az likidite bıraktığı için (likiditeyi tüm havuza paylaştırmak zorunda) yapılan işlemin fiyata ciddi bir etkisi oluyor (buna fiyat etkisi ya da 'price impact' deniyor). İkincisi ise havuzda çok sayıda işlem olması ama likiditenin sığ kalmasından dolayı, işlem emri verdiği sırada araya başka işlemler girdiği için verdiği emir fiyatı ile gerçekleşen fiyat arasında aleyhlerine bir fark olduğunu görüyorlar (ki buna ingilizcede slippage deniyor). 

### Başka ne sorunları var:

Uniswap'ın geçtiğimiz yaz aylarında yaşadığı büyük sıçramaya kısa süreli de sekte vuran gelişme, ürün kodlarını aynen kopyalayan Sushiswap'ın ciddi bir likiditeyi kendi platformuna çekmiş olmasıydı. Komisyon oranlarını benzer şekilde tutan Sushiswap likiditeyi kazanabilmek için kendi yönetim tokenini likidite sağlayıcılara vererek daha demokratik bir yapı olduğunu ilan etmişti. Bunun üzerine Uniswap da kendi tokenini çıkarıp dağıtmaya başladı ve likidite kanamasını bir nebze durdurmayı başardı. Token dağıtma bittikten sonra tekrar bir kayıp yaşasa da sonrasında  eski seviyelerine dönmeyi başardı. 

Uniswap - Sushiswap likidite rakamları


### Arkası Yarın
Uniswap DeFi dünyasının en ağır toplarından.. DeFi dünyasında altyapıyı sağlayan Ethereum sonrasında değeri en yüksek olan protokol.. Üstelik bu sıçramayı geçtiğimiz bir yıl içinde yaptı.. Bu nedenle yaptıkları ve yapamadıkları yakından izleniyor.. Başta da yazdığımız gibi yeni versiyon bu sıkıntılara çare bulmak amacını taşıyor. Neler bu çareler? Yazı uzadığı için onu bir sonraki yazımıza bırakıyoruz artık... 

--
*Dipnot: Geçici Kayıp (Impermanent Loss) nasıl çalışır?
Örneğin ETH/USDC gibi bir havuza para koymak isteyen likidite sağlayıcı düşünelim. Önünde iki seçeneği var. Ya parasını kenarda ETH ve USDC olarak tutacak ya da havuza likidite koyacak. Eğer ETH fiyatı aniden yükselirse, kenarda para tutmak havuza para koymaktan daha kârlı hale geliyor. Eğer ETH fiyatı geri eski seviyesi düşerse o zaman bu kâr ortadan kalkıyor, ve havuza likidite sağlamak kazanılan komisyon gelirleri nedeniyle daha avantajlı hale geliyor. Bu nedenle bu kâra geçici kayıp dense de eğer ETH'nin sürekli yükseleceğini düşünüyorsanız bu aslında kalıcı hale geliyor.*

---

# Yazı II

Geçtiğimiz yazıda DeFi dünyasının en büyük protokolü merkeziyetsiz takas borsası Uniswap'ın yaşadığı sıkıntılara bakmıştık. Bu yazımızda ise, Mayıs 2020'de çıkması planlanan yeni versiyonun bu sıkıntılara ne kadar çare olacağına ve yaratıcı ekibin Uniswap'ı nelere götürmeye çalıştığına değineceğiz... 

#### Çare: Konsantre likidite

Yeni versiyon ile birlikte Uniswap bir önceki yazıda bahsettiğimiz 'likiditenin tükenmemesi' ilkesini artık terkediyor. Bunun yerine, yeni getirdiği 'konsantre likidite' özelliği ile likidite sağlayıcıların verimlilik problemine çare olmayı tercih ediyor. Bu yeni özelliğe göre likidite sağlayıcı yatırımcılar, havuza koyacakları paranın hangi işlem aralığı içinde işlem görebileceğini belirleyebiliyorlar. Tam olarak ne demek bu? Ne işe yarıyor? Bir iki senaryo ile açıklayalım: 

Örneğin ETH-USDC havuzunda şu işlem göre fiyat 1 ETH=1.800 USDC ise, bir yatırımcı gelip parasını 1.300-1,400 aralığına koyabiliyor.. Normalde havuza eski sistemdeki gibi şu an likidite koysa havuz koyduğu parayı ikiye bölüp eşit olarak ETH ve USDC koyacak idi (havuzların eşit sayıda iki paradan oluşması gerekiyor). Eğer işlem yapanlar gelip bolca ETH satarlarsa (ve örneğin havuzda 1 ETH = 1,400 USDC'ye geriler ise), yatırımcının parası da 1 ETH eşittir 1,400 USDC'ye düşecek idi.  

Halbuki yeni sistemde yatırımcının parası eski hali ile korunacak. Burada likidite sağlayıcı yatırımcının ETH'nin düşüşünü tahmin ettiği için böyle davrandığını söyleyebiliriz. Tabii, fiyatın düşmeyip 1 ETH = 1,800 USDC civarlarında kalma durumunda ise, yatırımcının parası hiçbir şekilde işlemlere konu olmayacağı için %0.3 miktarındaki komisyonu alamayacak olması da madalyonun öbür yüzü... 

Bu durum ne gibi bir imkan sağlıyor likidite sağlayıcıya? Eğer fiyatın düşeceğini düşünüyor ya da düşük fiyattan portföyünü artırmak istiyor ise beklediği seviyelere likidite sağlayarak stratejisini uygulayabilir. Fiyat istedi alana geldiğinde likiditesini kullandırır ve eğer fiyat yeniden yukarı çıkarsa 

İşin özünde konsantre likidite aslında klasik anlamdaki emir defteri sistemi ile DeFi'de yeni çıkan otomatik para yapıcı sistemin hibrit bir karışımı. Bir başka deyişle, klasik borsalardaki al-sat emiri olarak verilen fiyatların daha geniş bir aralık içinde verilmesi. Likidite ve verimliliği bir tahterevallinin iki ucu olarak düşünürsek, başlangıçtaki likidite sıkıntısı nedeniyle oluşturulmuş likidite odaklı otomatik para yapıcının yerine, verimliliğe biraz daha ağırlık veren dengede bir sistem bu. 

#### Uniswap da NFT dünyasına girmiş :) 

Tabii bu hibrit karışımın bir sıkıntısı var. O da eskiden havuza konan her tür para eşit olduğu için, konulan para karşılığı alınan havuz katılım tokenları (bir nevi hesap sertifikası gibi düşünebilirsiniz) da birbirine eşit paralar olarak görülürdü ve bu tokenlar başka platformlarda teminat olarak kullanılabilirlerdi. Bu sayede likidite sahipleri ekstra gelir elde edebilirlerdi. Şimdi artık, farklı fiyat aralıklarında likidite sağlanabileceği için aynı havuz için verilen sertifikalar birbirinin aynı olmayacak. Yani havuz tokenları birbirine benzer 'fungible token' yerine, tekil 'non-fungible token' yani NFT olacaklar. İleride muhtemelen farklı NFT havuz tokenlarını farklı şekilde değerleyen yeni mekanizmalar çıkacak..  Örneğin aynı yatırımcıların mevduatlarını faklı stratejiler ile değerlendiren yearn.finance benzeri yapıların farklı değerlerdeki havuz tokenlarını alıp farklı araçlarda değerlendirerek risk/kazanç olarak en optimum seçenekler oluşturmaya başladığını göreceğiz muhtemelen. 

#### Farklı komisyon oranları

Uniswap ilk iki versiyonunda havuzlardaki işlemler için komisyon oranlarını hep sabit tuttu: Binde 3. Ancak bu durum kimi zaman rekabette onu zor durumda bıraktı.. Zira, özellikle stabil paralardan oluşan havuzlarda, paralar arasındaki fiyat farkı çok az olmakta. Örneğin bir USDC-DAI stabil para havuzunda 0.98-1.02 'den daha geniş bir aralık bulmak neredeyse imkansız.. Böyle bir durumda işlem yapmak isteyenlere binde 3 komisyon çok yüksek geliyor. Zaten bu nedenle stabil paralar odaklı olan Curve havuzları düşük komisyon verselerde işlem hacimlerinin yüksek olması nedeniyle likidite sağlayıcılarına hatırı sayılır bir komisyon geliri sağlayarak ciddi bir likiditeyi havuzlarında topladılar. 

İşte şimdi Uniswap komisyon oranlarını binde 0.5, binde 3 ve yüzde bir olarak üç ayrı seviyeye ayırdı. Mevcut piyasa fiyatlarına en yakın aralıklarda yapılan işlemlerde binde 1 veriyor. Bu da özellikle stabil paralarda Uniswap'a Curve ile mücadele etme imkanı veriyor ama avantaj hâlâ Curve'de. Zira Curve işlemler için binde 0.4 komisyon alıyor ve bu paranın yarısını Curve sahiplerine yarısını likidite sağlayıcılara vermekte. 

Uniswap işlemlerden aldığı binde 3 şu anda tamamınını likidite sahiplerine veriyor. UNI token tutanların bu komisyonun altıda birini (yani onbinde beşini) kendilerine alma hakkı var (ki kullanılmıyor idi). Şimdi yeni versiyon ile UNI token sahiplerine komisyon oranlarının onda biri ile dörde biri kadar bir miktarını kendilerine alma hakkı getirildi. 

#### Ethereum'un yüksek ücretleri 

2. Malum şu ara Ethereum dünyasındaki en büyük şikayetlerden bir tanesi yüksek işlem ücretleri.. Eskiden 5-10 dolar verilen basit işlemler için şimdi kapı en az 30-40 dolardan açılıyor.. Uniswap için bu durum ciddi bir sıkıntı. Zira normal bir günde Ethereum blokzinciri üzerindeki en fazla işlem yapan DeFi ürünü genelde Uniswap oluyor.. 

ethgasstation_210328.png

Ethereum üzerindeki DeFi ürünleri de bu konuda yavaş yavaş harekete geçiyorlar. Genel olarak tercih edilen tüm işlemlerin tek tek Ethereum blokzincirine işlenmesi yerine, bu işlemlerin bir araya getirilip, emek yoğun kısmın zincir dışı tamamlandıktan sonra sadece sonuçların blokzincire yazılması.. Roll-up çözümleri de denen bu işlem sonucu işlem maliyetleri düşüyor ancak işlem sonuçlarının blokzincirde yazılması zaman alabiliyor. 

Uniswap yeni versiyonda Optimistic Roll-up'ı kullanacağını açıkladı.. Maliyetlerin düşmesi açısından güzel bir gelişme olacak gibi görünüyor. Bir diğer DeFi devi olan sentetik türev piyasası Synthetix de Optimistic roll-up kullanacağını açıklamıştı. v3 ilanının hemen ertesi günü Optimistic ekibinin işleme girme tarihlerini Nisan'dan Temmuz'a revize etmeleri Uniswap'ı nasıl etkileyecek, onu hep birlikte göreceğiz. 

#### Beni kopyalama!... 

Geçtiğimiz yazıda detayını yazdığımız Sushiswap kopyalama olayından derin bir şekilde etkilenen Uniswap, yeni versiyonunda BSL denen farklı bir lisanslama kullandı. Buna göre başka platformlar bu kodları iki yıl süresince kopyalayamayacak. Sonrasında lisansın uzatılıp uzatılmayacağına ise Uniswap sahipleri karar verecekler. 

Klasik dünyanın kalıpları ile düşünürsek, "ne var bunda?, o kadar çalışmış uğraşmışlar, tabii ki haklarını koruyacaklar" diyebiliriz. Ancak bu hareketin DeFi dünyasının temel felsefesi ile çeliştiğini de söylemek gerek. Zira DeFi dünyası kökü çok daha eskilere dayanan açık kaynak felsefesine dayanır. Bu dünyada lisans, telif gibi enstrümanlar, yenilikçilik ve gelişmeyi engelleyici olarak görülürler. Zira az önce yukarıda Sushiswap'ın yaptığı direkt kopyalamayı yadırgasak da, Uniswap'ın sırf bu rekabetten dolayı kendi tokenlarını dağıtmasının biz son kullanıcılara ciddi fayda sağladığı gerçeğini yadsıyamayız. Dolayısıyla, şimdi yapılan bu hareket Uniswap ve yatırımcılarına kısa vadede fayda sağlayacak olsa da uzun vadede ekosistem için "acaba DeFi de klasik dünyaya mı dönüyor?" şeklinde soruları da getirebilir. Uniswap'ın hatırı sayılır bir girişim sermayesi yatırımı almış olması bu kuşkuların aslında çok da yersiz olmadığını bize gösteriyor sanki... 

#### Diğer ufak yenilikler
Bunun dışında daha önceki bir yazımızda bahsettiğimiz DeFi dünyasının oracle yani bilgi sağlayıcılarından biri olan Uniswap'ın artık daha tutarlı bilgi sağlayacak yenilikler yaptığını söyleyebiliriz. Bunun kulanıcılar açısından çok büyük bir faydası olmasa da, gerek bilgi ihtiyacı olan ekosistem oyuncuları gerekse bu bilgiyi satan Uniswap sistemi için faydalı olacağını söyleyebiliriz. 

Bunun dışında Uniswap ekibi artık geliştirme için neler yapacaklarını tamamen UNI token sahiplerine bırakacaklarını açıkladılar. Geçmişte UNI token sahipliğinin çok konsantre olduğu ile ilgili şikayetler olmuştu - bakalım merkeziyetsizlik hakikaten işleyecek mi, yoksa 'miş' gibi mi yapılacak hep birlikte göreceğiz.. 

### Sonuç ve yorumlar: 
Uniswap yeni versiyonu ile yeni stratejisinin ilk ipuçlarını veriyor. Neler bunlar?
Öncelikle artık hedef büyük merkezi borsalar ve mevcut rakipler. Eldeki atıl likidite kapasitesini konsantre likidite ile işlemlerin olduğu yere çekiyor ve merkezi borsaların emir defteri çözümlerine karşı verimliliği artıran bir model ortaya koyuyorlar. Bir yandan da Curve gibi rakiplerin kendilerinden tırtıkladığı stabil para havuzlarına ağırlık koymaya çalışıyorlar. 

İkincisi artık küçük likidite sağlayıcılar çok da umurlarında değil. Parasını alıp havuza eskisi gibi koymak artık iyice verimsiz hale geliyor. Bundan sonra devir, likiditesini sıkıca takip eden büyük likidite sağlayıcıların devri. Küçük yatırımcılar da 'belli komisyonlar' karşılığı yearn.finance benzeri aracılardan medet umabilirler. 

Üçüncüsü, Uniswap artık iyice kendisini destekleyen sermayeye teslim olmuş gibi görünüyor. Yukarıda açıklanana verimlilik benzeri süslü cümlelerin sonuna eklenen, özellikle yazılım kodunun iki yıl kullanılamayacak şekilde lisanslanması, bunun yanında likidite sağlayıcılara verdiği komisyonların daha büyük bir kısmının UNI token sahipleri tarafından alınma hakkı verilmesi endişe yaratıcı gelişmeler. İnsan, Web 2.0'daki herseyin bedava verildiği hizmetler sonrası giderek bilgilerimizin satıldığı ve kullanıcın ticari emtiaya dönüştürüldüğü o süreci hatırlamıyor değil. Umarız, yanlış yorumluyoruzdur... 

