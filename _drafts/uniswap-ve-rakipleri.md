Hatırlarsanız geçtiğimiz yazıda en büyük merkeziyetsiz borsa olan Uniswap'tan bahsetmiştik. Kısaca Uniswap, eşli (iki token sahibi) havuzlar aracılığıyla, işlem yapmak isteyenlere emre amade (istendiği anda) fiyat veren bir sistem. Klasik borsalara giriş yapamayan ya da yapmayı zahmetli bulan kullanıcılar, ve yine klasik borsalara giremeyen ya da girmek istemeyen tokenlar için adeta çölde vaha işlevi gördü. 

İşlem hacminin artmasına paralel havuzlara konan para yani likidite arttı (ki bu ikisi yumurta-tavuk gibi birbirinin artmasına yol açar). Popülerliği son zamanlarda o kadar arttı ki, kimi günler bir büyük merkezi kripto borsasından daha fazla işlem hacmi yaratmaya başladı. 

Tabii Uniswap'ın rakipleri de yok değil. Uniswap sisteminin belli özelliklerinden bahsederek hangi alanda nasıl rakipler çıktı bakabiliriz: 

### Nasıl farklılaştı rakipler?

#### Farklı algoritma kullanımı
Uniswap'ın özünde bir otomatik piyasa yapıcısı olduğundan bahsetmiştik. Bunun anlamı, sistemin işlem yapmak isteyenlere verdikleri fiyatlar otomatik olarak belirleniyor idi. Fiyat derken kastettiğimiz değiş-tokuş değeri. Havuzdaki bir tokeni almak için havuzdaki diğer tokeni oraya koymanız gerekiyor. 
Ne kadar token koyacağınız için ise basit bir formül var: Her bir havuzun iki tarafını oluşturan token adetlerinin çarpımının her zaman bir sabit sayıya eşit olacak. O kadar. Mantık basit aslında: Bir tokena talep varsa havuzdan çekilir, ve karşılığında diğer tokendan konur. Havuz büyüklüğü dediğimiz sabit sayıyı korumak için hauvzdaki azalan tokendan yeni bir tane almak için diğer tokendan eskisine göre daha fazla vermelisiniz. Basit bir arz-talep dengesi. 

Sonuçta yukarıdaki bahsettiğimiz sabit sayı ve hesaplaması afaki - yani isteyen istediği şekilde bu hesaplamayı değiştirerek yeni bir algoritma oluşturabilir. Nitekim rakiplerin bir kısmı bu algoritmaları değiştirerek kendilerine farklılaştırıyorlar. 


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

Curve yukarıdaki Uniswap formülünü farklı bir şekilde uyguluyor. Ne olduğunun çok önemi yok bu yazı için. Biz kullanılar için bilmemiz gereken şu: Uniswap'da yapılan işlemlerde eğer havuzdaki tokenlardan birinin değeri hızlıca değişirse likidite sağlayanın bir kaybı oluyor. Eğer sonrasında tokenların değeri göreceli olarak eski haline dönerse bu kayıp yok oluyor - o yüzden bu zarara "geçici kayıp- impermanent loss" deniyor. Curve genel olarak  Curve kullandığı algoritma ile daha çok stabil paralara hitap ediyor. Örneğin ABD Doları'na bağlı olan iki stabil kripto paranın (örneğin Tether-USDT- ve USDC) olduğu havuzlar Curve'in algoritması çok daha iyi çalışıyor(1). 

Bunun dışında üç-dört stabil paradan oluşan havuzlar da kuruyor Curve - Uniswap gibi yalnız ikili havuzlar yok. Bunun nedeni, kullanıcıların farklı sabit paralarla işlem yapmak istemeleri, her bir paradan diğerine geçerken ayrı ayrı havuzları kullanmak yerine olabilecek tüm farklı işlem taleplerini bir havuzdan gerçekleştirebilmek. Böylece farklı paralarda alım-satım yapmak isteyen biri Uniswap'ta iki ayrı havuz kullanacağı için çifte komisyon verip, bir de potansiyel olarak daha sığ iki havuzda daha fazla kayganlık (slippage) yaşarken, Curve kullanan bu ekstra kayıplardan kaçınabilecek. 

Bunun dışında özellikle diğer projeler ile çalışma anlamında ilginç birliktelikleri var Curve'in. Örneğin, ilk çıkardıkları USDC/DAI (her ikisi de sabit para) havuzundaki likiditeyi, bir borç verme platformu olan Compound'a koydular. Böylece Curve'e likidite sağlayanlar aynı zamanda Compound'da değerlendirilen para üzerinden faiz kazandı.  Bunun yanında geçtiğimiz bir yazımızda bahsettiğimiz kripto para türev borsası Synthetix ile ortak bir ürün çıkardılar ve yine ellerindeki likiditeyi Synthetix havuzlarına kullandırdılar. Karşılığında da Curve likid Synthetix tokenı olan SNX kazandılar.. 

Likiditenin DeFi ürünlerinde ne kadar önemli olduğunu görüyorsunuz değil mi? Gördüğünüz gibi Curve bir nevi likidite ticareti yapıyor. Likidite sağlayıcılardan aldığı parayı gerek sabit para al-sat yapmak isteyen kullanıcılara, gerekse kendi sistemini kuvvetlendirmek isteyen başka platformlara götürerek ekstra getiriler elde ediyor. 

Bitti mi? Hayır. Bu likidite oyununu giderek artırdı Curve. Compound ile ortak ürün çok güzel. Likidite sağlayan hem işlem üzerinden komisyon, hem CRV tokenı, hem Compound faizi, hem de COMP yönetim tokenı kazanıyor. Ancak ya faiz olarak Compound'un önerdiği faizler az ise? Öyle ya bir tek Compound yok kredi veren platformlar içinde.. Aave var, dYdX var. Ya onlar daha iyi faiz verirse? İşte o nedenle Curve, Yearn isimli bir nevi merkeziyetsiz portföy yönetimi yapan platform ile bir başka ürün daha çıkardı. Bu üründe, likidite sağlayıcı parayı koyuyor Curve sistemine, Yearn bu parayı en yüksek faiz veren kredi platformunda değerlendiriyor. Nasıl? DeFi ürünleri hakikaten akıl sınırlarını zorluyor, değil mi?

### Balancer
Balancer, Uniswap'a kullanıcı arayüzü olarak da çok benziyor olsa da, getirdiği yenilikler ile yatırımcılara farklı alternatifler sunuyor. İkili değil sekize tokena kadar ve %50-50 değil farklı oranlarda token konabilen havuzlar sağlıyor. Böylece likidite sağlayanlar kendi risk ve beklentilerine uygun olarak istedikleri türden bir endeks fonuna yatırım yapmış oluyorlar. Üstelik klasik bir endesk fonunda fon yöneticisine yönetim payı verirken, burada bunun yerine likidite sağladığı için paydaşlara Balancer'ın yönetim tokenı olan BAL dağıtılıyor. 


#### Uniswap rakiplerine nasıl cevap verecek?

Şu an için Uniswap'ın en büyük avantajı sahip olduğu havuzlardaki likidite ve bunun sağladığı ağ (network) etkisi. Ancak DeFi hızlı ilerlemesine rağmen henüz emekleme aşamasında olan bir sektör, o nedenle her an herşey değişebilir. Bu ağ etkisinin çok kalıcı olmadığını düşünenler de var. Öte yandan, TVL dediğimiz bu platformlara bağlanan paraların küçük yatırımcılardan çok ellerinde büyük miktarlarda kripto tutan balinalardan geldiği biliniyor. Ve bu balinalar hemen yer değiştirebiliyorlar. Baksanıza son üç ayda bu dört büyük platforma bağlanmış para miktarlarının değişkenliğine:

[Dört platform likidite miktarları]

Rakiplerin kendisine göre hız




[^1] Curve algoritması Uniswap algoritmasına göre birbirine yakın değerdeki iki tokenda arz ve talep sonucu ortaya çıkan farkı minimumda tutuyor. Eğer arz ve talep değişikliği çok yüksek oranlarda olursa o zaman Curve daha dezavantajlı hale geliyor. Ancak Curve havuzları genelde birbirine yakın ve hep 1 ABD Doları'na geri dönen stabil paralardan oluştuğu için Curve algoritması daha kullanışlı oluyor. 
