---
layout: post
title:  "Ye"
date:   2019-04-02 09:47:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Geçtiğimiz yazıda DeFi dünyasının en büyük protokolü merkeziyetsiz takas borsası Uniswap'ın yaşadığı sıkıntılara bakmıştık. Bu yazımızda ise, Mayıs 2020'de çıkması planlanan yeni versiyonun bu sıkıntılara ne kadar çare olacağına ve yaratıcı ekibin Uniswap'ı nelere götürmeye çalıştığına değineceğiz... 

#### Çare: Konsantre likidite

Yeni versiyon ile birlikte Uniswap bir önceki yazıda bahsettiğimiz 'likiditenin tükenmemesi' ilkesini artık terkediyor. Bunun yerine, yeni getirdiği 'konsantre likidite' özelliği ile likidite sağlayıcıların verimlilik problemine çare olmayı tercih ediyor. Bu yeni özelliğe göre likidite sağlayıcı yatırımcılar, havuza koyacakları paranın hangi işlem aralığı içinde işlem görebileceğini belirleyebiliyorlar. Tam olarak ne demek bu? Ne işe yarıyor? Bir iki senaryo ile açıklayalım: 

İki yatırımcı ETH/USDC havuzuna para yatırıyor olsunlar. Ahmet eski sistemdeki gibi tüm havuza 10,000 ABD doları değerinde likidite sağlasın. Ayşe ise daha akıllı bir yatırımcı olarak yeni sistemden faydalansın ve bunun beşte biri gibi bir parayı (yani 2,000 ABD Dolarını) belli bir fiyat aralığına yatırsın (örneğin 1ETH=1,800-2,000 USDC aralığına).. Sonraki dönemde, ETH değer olarak 1,900-2,000 ABD Doları civarında seyreder ise, havuz sadece bu kısma ayrılmış likiditeyi alım-satım işlemlerinde kulandırır. Ahmet parasını tüm havuza yatırdığı için bu aralığa ufak bir kısmı, örneğin sadece 1,000 ABD Doları düşer. Ayşe de benzer şekilde parasının 1,000 ABD Doları kısmını kullandırır. Neden? Daha dar bir aralıkta parasını kullandırma izni verdiği ve daha isabetli bir seçim yaptığı için. Dolayısıyla komisyon olarak hem Ahmet hem de Ayşe eşit miktara hak kazanır. Halbuki Ayşe, Ahmet'in beşte biri kadar para koymuştu, dolayısıyla parasını çok daha verimli kullandı!

İşin özünde konsantre likidite aslında klasik anlamdaki emir defteri sistemi ile DeFi'de yeni çıkan otomatik para yapıcı sistemin hibrit bir karışımı. Bir başka deyişle, klasik borsalardaki al-sat emri olarak verilen fiyatların daha geniş bir aralık içinde verilmesi. Likidite ve verimliliği bir tahterevallinin iki ucu olarak düşünürsek, başlangıçtaki likidite sıkıntısı nedeniyle oluşturulmuş likidite odaklı otomatik para yapıcının yerine, verimliliğe biraz daha ağırlık veren dengede bir sistem bu. 

#### Uniswap da NFT dünyasına girmiş :) 

Tabii bu hibrit karışımın bir sıkıntısı var. O da eskiden havuza konan her tür para eşit olduğu için, konulan para karşılığı alınan havuz katılım tokenları (bir nevi hesap sertifikası gibi düşünebilirsiniz) da birbirine eşit paralar olarak görülürdü ve bu tokenlar başka platformlarda teminat olarak kullanılabilirlerdi. Bu sayede likidite sahipleri ekstra gelir elde edebilirlerdi. Şimdi artık, farklı fiyat aralıklarında likidite sağlanabileceği için aynı havuz için verilen sertifikalar birbirinin aynı olmayacak. Yani havuz tokenları birbirine benzer 'fungible token' yerine, tekil 'non-fungible token' yani NFT olacaklar. 

| ![hayden_adams_tablo](/assets/hayden_adams_tablo_800.jpg)|
|:--:| 
| *Kurucusu Haydan Adams'ın gözünden Uniswap. [Kaynak](https://twitter.com/haydenzadams/status/1370232241528377348)*|

İleride muhtemelen farklı NFT havuz tokenlarını değerlendiren yeni mekanizmalar göreceğiz..  Örneğin şu anda yatırımcıların mevduatlarını değişik stratejiler ile değerlendiren yearn.finance benzeri yapıların bu system içinde son derece aktif olacağını tahmin etmek zor değil. Bu yapılar, farklı fiyat aralıklarındaki havuz tokenlarını alıp farklı araçlarda değerlendirecek ve risk/kazanç anlamında optimum seçenekler oluşturup yatırımcıların beğenisine sunacaklar. 

#### Farklı komisyon oranları

Uniswap ilk iki versiyonunda havuzlardaki işlemler için komisyon oranlarını hep sabit tuttu: Binde 3. Ancak bu durum kimi zaman rekabette onu zor durumda bıraktı.. Zira, özellikle stabil paralardan oluşan havuzlarda, paralar arasındaki fiyat farkı çok az olmakta. Örneğin bir USDC-DAI stabil para havuzunda 0.98-1.02 'den daha geniş bir aralık bulmak neredeyse imkansız.. Böyle bir durumda işlem yapmak isteyenlere binde 3 komisyon çok yüksek geliyor. Zaten bu nedenle stabil paralar odaklı olan Curve havuzları düşük komisyon verselerde işlem hacimlerinin yüksek olması nedeniyle likidite sağlayıcılarına hatırı sayılır bir komisyon geliri sağlayarak ciddi bir likiditeyi havuzlarında topladılar. 

İşte şimdi Uniswap komisyon oranlarını binde 0.5, binde 3 ve yüzde bir olarak üç ayrı seviyeye ayırdı. Mevcut piyasa fiyatlarına en yakın aralıklarda yapılan işlemlerde binde 1 veriyor. Bu da özellikle stabil paralarda Uniswap'a Curve ile mücadele etme imkanı veriyor ama avantaj hâlâ Curve'de. Zira Curve işlemler için binde 0.4 komisyon alıyor ve bu paranın yarısını Curve sahiplerine yarısını likidite sağlayıcılara vermekte. 

Uniswap işlemlerden aldığı binde 3 komisyonun şu anda tamamınını likidite sahiplerine veriyor. UNI token tutanların bu komisyonun altıda birini (yani onbinde beşini) kendilerine alma hakkı var (ki kullanılmıyor idi). Şimdi yeni versiyon ile UNI token sahiplerine komisyon oranlarının onda biri ile dörde biri kadar bir miktarını kendilerine alma hakkı getirildi. Bunun yanında her bir havuzun yukarıdaki üç orandan hangisini kullanacağına da UNI token sahipleri karar verecek. 

#### Ethereum'un yüksek ücretleri 

Malum şu ara Ethereum dünyasındaki en büyük şikayetlerden bir tanesi yüksek işlem ücretleri. Eskiden 5-10 dolar verilen basit işlemler için şimdi kapı en az 30-40 ABD Dolarından açılıyor. Uniswap için bu durum ciddi bir sıkıntı. Zira normal bir günde Ethereum blokzinciri üzerindeki en fazla işlem yapan DeFi ürünü genelde Uniswap oluyor.. 

| ![ethgasstation](/assets/ethgasstation_210328_800.png)|
|:--:| 
| *ETH sistemi üzerindeki en büyük yük sahipleri - 28 Mart 2020 son 30 gün ortalaması. [Kaynak](https://ethgasstation.info/index.php)*|

Ethereum üzerindeki DeFi ürünleri de bu konuda yavaş yavaş harekete geçiyorlar. Genel olarak tercih edilen tüm işlemlerin tek tek Ethereum blokzincirine işlenmesi yerine, bu işlemlerin bir araya getirilip, emek yoğun kısmın zincir dışı tamamlandıktan sonra sadece sonuçların blokzincire yazılması. Roll-up çözümleri de denen bu işlem sonucu işlem maliyetleri düşüyor ancak işlem sonuçlarının blokzincirde yazılması zaman alabiliyor. 

Uniswap yeni versiyonda Optimistic Roll-up'ı kullanacağını açıkladı.. Maliyetlerin düşmesi açısından güzel bir gelişme olacak gibi görünüyor. Bir diğer DeFi devi olan sentetik türev piyasası Synthetix de Optimistic roll-up kullanacağını açıklamıştı. v3 ilanının hemen ertesi günü [Optimistic'in genel kullanıma açılma tarihinin Nisan'dan Temmuz'a ertelenmesi](https://optimismpbc.medium.com/optimistically-cautious-767a898f90c8) Uniswap'ı nasıl etkileyecek, onu hep birlikte göreceğiz. 

#### Beni kopyalama!... 

Geçtiğimiz yazıda detayını yazdığımız Sushiswap kopyalama olayından derin bir şekilde etkilenen Uniswap, yeni versiyonunda BSL denen farklı bir lisanslama kullandı. Buna göre başka platformlar bu kodları iki yıl süresince kopyalayamayacak. Sonrasında lisansın uzatılıp uzatılmayacağına ise Uniswap sahipleri karar verecekler. 

Tam olarak ne gibi bir etkisi olacak bunun? Artık rakipler Uniswap'ın kodunu kopyalayıp kullanamayacaklar. Kullanırlarsa ne olacak? Uniswap rakiplerini dava edebilecek mi? Nerede? Ticari mahkemelerde. Peki ya rakipler DeFi protokolü ise, sahipleri belli değil ise? O zaman Uniswap'ın o protokole karşı yapabileceği bir aksiyon yok ancak o protokolü kullanan ve sahipleri belli uygulamalara karşı dava açabilir. 

Klasik dünyanın kalıpları ile düşünürsek, "ne var bunda?, o kadar çalışmış uğraşmışlar, tabii ki haklarını koruyacaklar" diyebiliriz. Ancak bu hareketin DeFi dünyasının temel felsefesi ile çeliştiğini de söylemek gerek. Zira DeFi dünyası kökü çok daha eskilere dayanan açık kaynak felsefesine dayanır. Bu dünyada lisans, telif gibi enstrümanlar, yenilikçilik ve gelişmeyi engelleyici olarak görülürler. Zira az önce yukarıda Sushiswap'ın yaptığı direkt kopyalamayı yadırgasak da, Uniswap'ın sırf bu rekabetten dolayı kendi tokenlarını dağıtmasının biz son kullanıcılara ciddi fayda sağladığı gerçeğini yadsıyamayız. Dolayısıyla, şimdi yapılan bu hareket Uniswap ve yatırımcılarına kısa vadede fayda sağlayacak olsa da uzun vadede ekosistem için "acaba DeFi de klasik dünyaya mı dönüyor?" şeklinde soruları da getirebilir. Uniswap'ın hatırı sayılır bir girişim sermayesi yatırımı almış olması bu kuşkuların aslında çok da yersiz olmadığını bize gösteriyor sanki... 

#### Diğer ufak yenilikler
Bunun dışında [daha önceki bir yazımızda bahsettiğimiz DeFi dünyasının oracle yani bilgi sağlayıcılarından](/genel/2020/12/22/definin-bilgi-kaynagi-oracle.html) biri olan Uniswap'ın artık daha tutarlı bilgi sağlayacak yenilikler yaptığını söyleyebiliriz. Bunun kulanıcılar açısından çok büyük bir etkisi olmasa da, gerek bilgi ihtiyacı olan ekosistem oyuncuları gerekse bu bilgiyi satan Uniswap sistemi için faydalı olacağını söyleyebiliriz. 

Bunun dışında Uniswap ekibi artık geliştirme için neler yapacaklarını tamamen UNI token sahiplerine bırakacaklarını açıkladılar. Geçmişte UNI token sahipliğinin çok konsantre olduğu ile ilgili şikayetler olmuştu - bakalım merkeziyetsizlik hakikaten işleyecek mi, yoksa 'miş' gibi mi yapılacak hep birlikte göreceğiz.. 

### Sonuç ve yorumlar: 
Uniswap yeni versiyonu ile yeni stratejisinin ilk ipuçlarını veriyor. Neler bunlar?
Öncelikle artık hedef büyük merkezi borsalar ve stabil paralara odaklanmış mevcut rakipler. Eldeki atıl likidite kapasitesini konsantre likidite ile işlemlerin olduğu yere çekiyor ve merkezi borsaların emir defteri çözümlerine karşı verimliliği artıran bir model ortaya koyuyor. Bir yandan da Curve gibi rakiplerin kendilerinden tırtıkladığı stabil para havuzlarına yeniden ağırlık koymaya çalışıyor. 

İkincisi artık küçük ve tembel likidite sağlayıcılara yavaş yavaş güle güle diyor Uniswap. Parayı alıp havuza olduğu gibi koymak artık iyice verimsiz hale geliyor. Bundan sonra devir, likiditesini sıkıca takip eden büyük likidite sağlayıcıların devri. Küçük yatırımcılar da 'belli komisyonlar' karşılığı yearn.finance benzeri aracılardan medet umabilirler. 

Üçüncüsü, Uniswap artık iyice kendisini destekleyen sermayeye teslim olmuş gibi görünüyor. Yukarıda açıklanan verimlilik benzeri süslü cümlelerin sonuna eklenen, özellikle yazılım kodunun iki yıl kullanılamayacak şekilde lisanslanması endişe verici. Aynı şekilde UNI token sahiplerin likidite sağlayıcılara verdiği komisyonların daha büyük bir kısmını kendilerine alabilme hakkı verilmesi de. İnsan, Web 2.0'daki 'bedava sunulan hizmetler karşılığında giderek kişisel bilgilerin satıldığı ve kullanıcının ticari emtiaya dönüştürüldüğü' o süreci hatırlamıyor değil. Umarız, kaygılarımız yersiz çıkar ve Uniswap DeFi dünyasının açık kaynak merkeziyetsiz çözüm lideri olarak yoluna devam eder.. 
