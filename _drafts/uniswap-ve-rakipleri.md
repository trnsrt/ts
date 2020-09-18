Hatırlarsanız geçtiğimiz yazıda en büyük merkeziyetsiz borsa olan Uniswap'tan bahsetmiştik. Kısaca Uniswap, eşli (iki token sahibi) havuzlar aracılığıyla, işlem yapmak isteyenlere emre amade (istendiği anda) fiyat veren bir sistem. Klasik borsalara giriş yapamayan ya da yapmayı zahmetli bulan kullanıcılar, ve yine klasik borsalara giremeyen ya da girmek istemeyen tokenlar için adeta çölde vaha işlevi gördü. 

İşlem hacminin artmasına paralel havuzlara konan para yani likidite arttı (ki bu ikisi yumurta-tavuk gibi birbirinin artmasına yol açar). Popülerliği son zamanlarda o kadar arttı ki, kimi günler bir büyük merkezi kripto borsasından daha fazla işlem hacmi yaratmaya başladı. 

Tabii Uniswap'ın rakipleri de yok değil. Uniswap sisteminin belli özelliklerinden bahsederek hangi alanda nasıl rakipler çıktı bakabiliriz: 

### Nasıl farklılaştı rakipler?

#### Farklı algoritma kullanımı
Uniswap'ın özünde bir otomatik piyasa yapıcısı olduğundan bahsetmiştik [geçen yazımızda]. Bunun anlamı, sistemin işlem yapmak isteyenlere verdikleri fiyatlar otomatik olarak belirleniyor idi. Fiyat derken kastettiğimiz değiş-tokuş değeri. Havuzdaki bir tokeni almak için havuzdaki diğer tokeni oraya koymanız gerekiyor. 
Ne kadar token koyacağınız için ise basit bir formül var: Her bir havuzun iki tarafını oluşturan token adetlerinin çarpımının her zaman bir sabit sayıya eşit olacak. O kadar. Mantık basit aslında: Bir tokena talep varsa havuzdan çekilir, ve karşılığında diğer tokendan konur. Havuz büyüklüğü dediğimiz sabit sayıyı korumak için hauvzdaki azalan tokendan yeni bir tane almak için diğer tokendan eskisine göre daha fazla vermelisiniz. Basit bir arz-talep dengesi. 

Uniswap algoritmasının temel hedefi, her ne olursa olsun işlem yapmak isteyenlere sunulabilecek bir token bulundurmak. Bu nedenle kimi zaman bir tokena çok talep olunca o tokenın fiyatı (havuzdaki diğer token ile değişme oranı) saçma yerlere gelebiliyor. Ayrıca, işlem yapmadan önce sistemde bir alım-satım oranı görürken işlem yapmaya başladığınızda birden bunun değiştiğini görebiliyorsunuz - buna performans düşüklüğü (slippage) deniyor. Uniswap için bu iki sıkıntının da bir önemi yok - yeter ki ne pahasına olursa olsun işlem yapmak için gelmiş olan birini eli boş döndürmesin. 

Sonuçta Uniswap algoritması olarak bahsettiğimiz sabit sayı ve hesaplaması afaki - yani isteyen istediği şekilde bu hesaplamayı değiştirerek yeni bir algoritma oluşturabilir. Nitekim rakiplerin bir kısmı bu algoritmaları değiştirerek kendilerine farklılaştırıyorlar. 


#### Çoklu havuzlar
Uniswap'daki her bir havuzun iki bölmesi var demiştik - ve her bir bölmede de birer token. İllâ iki token mı olması lazım? Daha çok token koyulamaz mı? Olur tabii - neden olmasın? İşte rakip olarak çıkan kimi sistemler üç, dört hatta 8'e kadar sayıda token koydular sistemlerine. Böylece likidite sağlayıcılara birden fazla tokena aynı anda yatırım yapma imkanı vermiş oldular. 

#### Farklı havuz oranları
Uniswap'taki her havuzda iki bölme olmasının yanında algoritmaya göre her bir bölmede eşit değerde token olması gerekiyor. Yani bir havuzun bir tarafında 1000 ETH var ise, ve bir ETH de 300 USDC ise, havuzun diğer tarafından 300,000 USDC olmalı ki sistem dengede olsun. Peki bu oran %50-50 mi olmalı? Uniswap algoritması gereği öyle olabilir ama her zaman %50-50 olmasına gerek yok havuzların. Farklı ağırlıklı havuzlar da gayet rahat şekilde kurulabilir. Neden farklı havuzlara ihtiyaç var? Özellikle likidite sağlayanlar havuza likidite sağladıklarında havuzun her iki tarafına da yatırım yapıyorlar. O nedenle bu iki token ile ilgili beklentilerine göre  farklı ağırlıklarda yatırım yapmak isteyebilirler. Örneğin ETH'nin artacağı konusunda bir beklentisi var ise ETH/USDC havuzuna %50-50 katılmak yerine %80-20 katılmayı isteyebilirler. 

#### Yönetim tokenı
Uniswap'ta likidite sağlayıcıların  Eylül 2020 başına kadar gelirleri yalnızca sağladıkları likiditeye karşılık yapılan işlemlerden aldıkları komisyonlar idi. Halbuki rakip projeler, bu komisyonlar dışında kullanıcılara ve likidite sağlayıcılara kendi tokenlarını veren teşvik mekanizmaları geliştirdiler. İşte geçtiğimiz haftaki yazının hemen ardından Uniswap da benzer bir tokenı kendi paydaşlarına dağıtmaya başladı. Üstelik oldukça demokratik bir biçimde, geçtiğimiz dönemde (1 Eylül 2020'ye kadar) Uniswap kullanıp işlem yapmış her bir hesaba 400 UNI tokenı bedava veriyorlar. 

#### Diğer projeler ile uyumluluk
DeFi projelerinin klasik projelere göre en önemli farklarından biri, farklı projelerin birbirleriyle uyumlu çalışabilmesi. Buna "money lego" diyenler de var. İşte, Uniswap rakibi projeler başka başka projeler ile iletişim içinde yeni, kazancı daha yüksek ürünler çıkarabiliyorlar. 

#### Fiyat
Uniswap her bir işlem için al-sat yapan kullanıcılardan %0.3 komisyon alıyor. Bu oldukça yüksek bir rakam - her ne kadar kendisi üzerinden 1 Eylül 2020 tarihine kadar kendisi üzerinden işlem yapmışlara 400 UNI token vererek bu komisyonların bir kısmını kullanıcılara geri vermiş olsa da.  Uniswap likidite sağlayıcılara gelir olarak yapılan işlemlerden komisyonları önerdiği için rakamı çok da düşüremiyor idi. Ancak son açıklanan, UNI token ile likidite sağlayıcılar ciddi bir ekstra gelir kazanıyorlar. O nedenle bir sonraki Uniswap versiyonunda (v3) bu komisyonların düşmesi beklenebilir. 


### Curve

Curve yukarıdaki Uniswap algoritmasını farklı bir şekilde uyguluyor. Rakamsal olarak ne olduğunun çok önemi yok bu yazı için. Kullanıcıların bilmesi gereken, Uniswap algoritması her ne olursa olsun kullanıcılara işlem yapabilecek bir token sunmak iken, Curve algoritması yukarıda Uniswap için bahsettiğimiz işlem yaparken al-sat yapanın yaşadığı performans düşüklüğünü engellemek.

Curve'un kullandığı bu algoritma, yüksek hacimli ve fiyatı fazla oynamayan ikililerde çok daha avantajlı oluyor al-sat yapanlar kullanıcılar için. Örneğin ABD Doları'na bağlı olan iki stabil kripto paranın (örneğin Tether-USDT- ve USDC) olduğu havuzlar Curve'in algoritması çok daha iyi çalışıyor(1). 

Bunun dışında üç-dört stabil paradan oluşan havuzlar da kuruyor Curve - Uniswap gibi yalnız ikili havuzlar yok. Bunun nedeni, kullanıcıların farklı sabit paralarla işlem yapmak istemeleri, her bir paradan diğerine geçerken ayrı ayrı havuzları kullanmak yerine olabilecek tüm farklı işlem taleplerini bir havuzdan gerçekleştirebilmek. Böylece farklı paralarda alım-satım yapmak isteyen biri Uniswap'ta iki ayrı havuz kullanacağı için çifte komisyon verip, bir de potansiyel olarak daha sığ iki havuzda daha fazla kayganlık (slippage) yaşarken, Curve kullanan bu ekstra kayıplardan kaçınabilecek. 

Bunun dışında özellikle diğer projeler ile çalışma anlamında ilginç birliktelikleri var Curve'in. Örneğin, ilk çıkardıkları USDC/DAI (her ikisi de sabit para) havuzundaki likiditeyi, bir borç verme platformu olan Compound'a koydular. Böylece Curve'e likidite sağlayanlar aynı zamanda Compound'da değerlendirilen para üzerinden faiz kazandı.  Bunun yanında geçtiğimiz bir yazımızda bahsettiğimiz kripto para türev borsası Synthetix ile ortak bir ürün çıkardılar ve yine ellerindeki likiditeyi Synthetix havuzlarına kullandırdılar. Karşılığında da Curve likid Synthetix tokenı olan SNX kazandılar.. 

Likiditenin DeFi ürünlerinde ne kadar önemli olduğunu görüyorsunuz değil mi? Gördüğünüz gibi Curve bir nevi likidite ticareti yapıyor. Likidite sağlayıcılardan aldığı parayı gerek sabit para al-sat yapmak isteyen kullanıcılara, gerekse kendi sistemini kuvvetlendirmek isteyen başka platformlara götürerek ekstra getiriler elde ediyor. 

Bitti mi? Hayır. Bu likidite oyununu giderek artırdı Curve. Compound ile ortak ürün çok güzel. Likidite sağlayan hem işlem üzerinden komisyon, hem CRV tokenı, hem Compound faizi, hem de COMP yönetim tokenı kazanıyor. Ancak ya faiz olarak Compound'un önerdiği faizler az ise? Öyle ya bir tek Compound yok kredi veren platformlar içinde.. Aave var, dYdX var. Ya onlar daha iyi faiz verirse? İşte o nedenle Curve, Yearn isimli bir nevi merkeziyetsiz portföy yönetimi yapan platform ile bir başka ürün daha çıkardı. Bu üründe, likidite sağlayıcı parayı koyuyor Curve sistemine, Yearn bu parayı en yüksek faiz veren kredi platformunda değerlendiriyor. Nasıl? DeFi ürünleri hakikaten akıl sınırlarını zorluyor, değil mi?

### Balancer
Balancer, Uniswap'a kullanıcı arayüzü olarak da çok benziyor olsa da, getirdiği yenilikler ile yatırımcılara farklı alternatifler sunuyor. Neler bunlar hızlıca bakalım: 

İkili değil sekize tokena kadar ve %50-50 değil farklı oranlarda token konabilen havuzlar sağlıyor öncelikle. Ne işe yarar bu? Böylece likidite sağlayanlar kendi risk ve beklentilerine uygun olarak istedikleri türden bir endeks fonuna yatırım yapmış oluyorlar. Adeta kişiye özel bir yatırım fonu! Üstelik klasik bir endesk fonunda fon yöneticisine yönetim payı verirken, burada bunun yerine likidite sağladığı için paydaşlar hem yapılan işlem üzerinden komisyon hem de Balancer'ın yönetim tokenı olan BAL almaya hak kazanıyor.

Öte yandan Balancer üzerinde kurulan havuzların içinde yapılan işlemlerden alınan komisyon oranları Uniswap gibi sabit değil. Her bir havuz kurucusu farklı bir komisyon belirleyebiliyor. Likidite sağlarken komisyon oranlarını incelemekte fayda var. Bunun yanında kimi likidite sağlayıcılar kurdukları havuzu özel tutup, başka para almıyorlar. Neden böyle yapıyorlar tartışılır - bir örnek olarak, normal şirketler hisse senetlerini geri almak (buy-back) suretiyle dolaşımdaki paralarını kontrol etmek isterler. Burada da kimi girişimler dolaşımda olan tokenlarının emisyonunu kontrol edebilmek için karmaşık hesaplar, yeni token basma ya da token yakma yerine, Balancer üzerindeki havuzlarını kullanıp, genel emisyon rakamları ile oynamak isteyebilirler. Hatta, böyle bir durumda, havuzda manipülasyon yapılmasın diye yüksek işlem komisyonu (örneğin %5) belirleyip ancak çok yüksek fiyat değişikliklerinde son çare olarak havuzlarının kullanılmasını isteyebilirler. Görüyorsunuz, bu tip ürünlerde amaç ve isteğe göre ne kadar farklı senaryo ve alternatif çıkabiliyor.. 


### Sushiswap

Yukarıda bahsettiğimiz gibi, özünde Uniswap çok basit bir algoritma. Bir DeFi platformu olarak aynı zamanda açık kaynak vizyonu ile çalışıyor - yani ürün (yani kod) tamamen açık. Dolayısıyla, Uniswap'ın kodunu çatallayıp (forklamak) benzer bir ürünü çıkarmak o kadar zor değildi, nitekim Sushiswap bu şekilde Uniswap kopyası bir ürün çıkardı. Üzerine tek bir ekleme yaptı, o da parayı kendilerinde tutanlar için Sushi token vaad etti.. Bir anda ciddi bir likidite (ki bunlar ellerinden büyük miktarda token tutan balinalar) Sushiswap'a kaydı. 

Sonrasında DeFi büyük krizlerinden birini yaşadı. Sushiswap'ın kurucusu (ismi bilinmeyen) olan geliştirici, kendine ciddi bir miktarda token alıp piyasalarda bunu bozdurdu. Bunun üzerine büyük bir fırtına koptu ve sonrasında bu kişi o tokenları iade etti. Sinek küçük ama mide bulandırır tarzı bir hareket oldu bu. Sushiswap yoluna devam ediyor - zira gerek kullanıcı gerekse likidite sağlayıcılar aldıkları komisyon ve Sushi token ödüllerine bakıyorlar. Ancak bu olay klonların imajını ciddi şekilde sarstı. 

Her ne kadar "kod" olarak aynı olsalar da, geliştirici ekip ve etrafında kümelenmiş ciddi bir topluluk olmadıkça, Sushiswap benzeri klonların uzun vadede Uniswap'tan geri kalacağını beklemek çok da yanlış bir beklenti olmaz. Yalnız para ile saadet olmuyor maalesef. 


#### Uniswap rakiplerine nasıl cevap verecek?

Şu an için Uniswap'ın en büyük avantajı sahip olduğu havuzlardaki likidite ve bunun sağladığı ağ (network) etkisi. Ancak DeFi hızlı ilerlemesine rağmen henüz emekleme aşamasında olan bir sektör, o nedenle her an herşey değişebilir. Bu ağ etkisinin çok kalıcı olmadığını düşünenler de var. 

Klasik pazarlarda strateji ve pazarlama alanında şirketler ve müşterileri konuşulurken, en önemli maddelerden biri müşteri bağlılığı (customer stickiness) olarak geçer. Müşteriyi nasıl kendinize bağlarsınız? Klasik finans sistemi oyuncuları maalesef daha çok kendi sistemlerinden çıkmayı zorlaştırarak müşterilerini bağlıyorlar. Ancak DeFi'da öyle değil - zira varlık platformda değil, kullancının elinde. Al-sat işlemini bugün sizden yapar - yarın daha iyi fiyat bulursa ya da daha az komisyon veriyorsa anında gidip rakip platformdan yapar. Hatta farklı platformlara bakmasına bile gerek yok. [1inch] gibi hizmet sağlayıcılar onun adına hangi platform daha uygun fiyat veriyor anında gidip bulur. 

Likidite sağlayıcılar için de benzer durum. Likiditeyi bugün burada tutar - daha iyi bir imkan bulursa anında çeker, başka bir yere gider. 

Öte yandan, TVL dediğimiz bu platformlara bağlanan paraların küçük yatırımcılardan çok ellerinde büyük miktarlarda kripto tutan balinalardan geldiği biliniyor. Ve bu balinalar hemen yer değiştirebiliyorlar. Baksanıza son üç ayda bu dört büyük platforma bağlanmış para miktarlarının değişkenliğine:

[Dört platform likidite miktarları]

Rakiplerin kendisine göre hızla yol almalarına karşı Uniswap da belli hareketlerde bulunmaya başladı. Örneğin Eylül başında çıkardığı UNI token esas olarak kendi klonu olan Sushiswap'a karşı gösterdiği bir reaksiyon. Uniswap likidite sağlayıcılara gelir olarak yapılan işlemlerden komisyonları önerdiği için işlemlerden aldığı %0.3 ücreti yüksek olmasına rağmen düşüremiyor idi. Ancak UNI token ile likidite sağlayıcılar ciddi bir ekstra gelir kazanacaklar. 

Yakında çıkması planlanan Uniswap 3.0 versiyonda, al-sat komisyon ücretlerinin (UNI sayesinde artan diğer gelirler ile birlikte) azalması beklenebilir. Bunun yanında ikili havuzlar yerine çoklu havuzları da uygulamaya alabilir Uniswap. 


[^1] Curve algoritması Uniswap algoritmasına göre birbirine yakın değerdeki iki tokenda arz ve talep sonucu ortaya çıkan farkı minimumda tutuyor. Eğer arz ve talep değişikliği çok yüksek oranlarda olursa o zaman Curve daha dezavantajlı hale geliyor. Ancak Curve havuzları genelde birbirine yakın ve hep 1 ABD Doları'na geri dönen stabil paralardan oluştuğu için Curve algoritması daha kullanışlı oluyor. 
