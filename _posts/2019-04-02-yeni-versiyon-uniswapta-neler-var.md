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

İki yatırımcı ETH/USDC havuzuna para yatırıyor olsunlar. Ahmet eski sistemdeki gibi tüm havuza 10,000 dolar likidite sağlasın. Ayşe ise daha akıllı bir yatırımcı olarak yeni sistemden faydalansın ve daha az bir parayı (örneğin 2,000 ABD Dolarını) belli bir fiyat aralığına yatırsın (örneğin 1ETH=1,800-2000 USDC aralığına).. Eğer ETH değer olarak 1,900 dolar civarında seyreder ise, o zaman havuz sadece bu kısıma yatırılmış likiditeyi kullanacak. Bu kısıma yatırılmış likidite için de sistem hem Ahmet hem Ayşe'nin örneğin 1,500 dolarını kullanacak - ve komisyonları ikisi arasında eşit bölüştürecek. Gelen komisyonu almak için Ahmet 10,000 dolar yatırmış iken Ayşe sadece 2,000 dolarını bağlamış olacak. Dolayısıyla Ayşe çok daha az bir paraya Ahmet ile aynı komisyonu alacak!

<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/docsearch.js@2/dist/cdn/docsearch.min.js"></script>


Örneğin ETH-USDC havuzunda şu işlem göre fiyat 1 ETH=1.800 USDC ise, bir yatırımcı gelip parasını 1.300-1,400 aralığına koyabiliyor.. Normalde havuza eski sistemdeki gibi likidite koysa havuz koyduğu parayı ikiye bölüp eşit olarak ETH ve USDC koyacak idi (havuzların eşit sayıda iki paradan oluşması gerekiyor). Eğer işlem yapanlar gelip bolca ETH satarlarsa (ve örneğin havuzda 1 ETH = 1,400 USDC'ye geriler ise), yatırımcının parası da 1 ETH eşittir 1,400 USDC'ye düşecek idi.  

Halbuki yeni sistemde yatırımcının parası eski hali ile korunacak. Burada likidite sağlayıcı yatırımcının ETH'nin düşüşünü tahmin ettiği için böyle davrandığını söyleyebiliriz. Tabii, fiyatın düşmeyip 1 ETH = 1,800 USDC civarlarında kalma durumunda ise, yatırımcının parası hiçbir şekilde işlemlere konu olmayacağı için %0.3 miktarındaki komisyonu alamayacak olması da madalyonun öbür yüzü... 

Bu durum ne gibi bir imkan sağlıyor likidite sağlayıcıya? Eğer fiyatın düşeceğini düşünüyor ya da düşük fiyattan portföyünü artırmak istiyor ise strateji olarak sadece beklediği seviyelere likidite sağlayabilir. Fiyat istediği alana geldiğinde likiditesini kullandırır. Yok eğer fiyat yeniden yukarı çıkarsa o zaman likiditesi işlem görmez ve 

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

