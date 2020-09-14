
### Nedir bu Uniswap?

Uniswap özünde bir merkeziyetsiz borsa - bu borsaların en eskilerinden. Ancak merkeziyetsiz denince eşten-eşe P2P olduğu düşünülmesin - çünkü öyle değil. Bu borsayı kullanan kullanıcılar, birbirleri ile değil bir havuz karşı işlem yapıyorlar. 

Temel olarak iki ana grup var Uniswap'ta. Kullancılar: Bunlar bildiğimiz anlamda işlem yani al-sat yapanlar. Bir de havuza likidite sağlayanlar: ki bunlara yatırımcı, ya da hissedar denebilir ama biz paydaş terimini kullanalım (bir önceki SNX yazımızda olduğu gibi)... 

Uniswap için borsa desek de aslında İngilizcesi market maket olarak adlandırılan piyasa yapıcı bir havuz aslında. Piyasa yapıcı, bir alım yapmak istediğinizde size istediğiniz ürünü satmak için hazırda bekleyen bir taraf demek. Yani bir işlem yapmak istediğinizde verdiğiniz emri mutlaka karşılayan bir servis sağlayıcı. Peki kimin ne işine yarar bu? Gelin önce kullanıcılar gözünden bakalım:

### Kim neden Uniswap’ta işlem yapar?

UniSwap’ın popüler olmasının birkaç temel nedeni var: 

Öncelikle UniSwap ağırlıklı olarak merkezi borsalara çıkmak istemeyen ya da çıkamayan küçük token’ların hızlı bir şekilde işlem görmesi ve değer belirlemesi için kullanılmaya başladı ve bu sayede popüler oldu.. Her ne kadar son zamanlarda Binance, FTX gibi borsalar da çok hızlı bir şekilde DeFi token’ları listelemeye başlasalar da, 2020 yılının ortalarına kadar bu o kadar kolay değildi. Merkezi borsalarda listelenmek için bu borsaların koyduğu kurallara uymak ve istedikleri prosedürleri uygulamanız ama daha da ötesi listelenmek için ciddi paralar ödemeniz gerekiyor idi. Uniswap, Blokzincir’in “izin gerektirmeyen (permissionless”) ruhuna uygun olarak isteyen herkesin listeleme yapabileceği bir pazar. (Belki de bu nedenle işlem yapmak isteyen kullanıcılar ekstra dikkatli olmak zorunda zira kopya/sahte token’lar ile işlem yapıp yapmadıklarına dikkat etmeliler). 

Bunun yanında emir defteri ile çalışan piyasa yapıcılar, verdikleri emir gerçekleşmeden önce pek çok emri yazıp sonra iptal ederler. DeFi dünyasında özellikle yoğunluğu bağlı olarak sistem kullanım ücretlerinin ([daha önce bahsettiğimiz gas ücretleri](/genel/2020/08/06/gelecekte-eth-nin-degerini-neler-etkileyecek.html)) yüksek olması piyasa yapıcıların bu tip emir yazma/iptal işlemlerinin maliyetlerini çok artırıyor. Bu nedenle Uniswap’ın özellikle likit havuzlarında işlem yapmak daha az maliyet çıkarabiliyor. 

Son olarak özellikle yeni kullanmaya başlayanlar için Uniswap (ya da genel olarak DeFi) kullanmanın önemli bir nedeni daha önceki yazılarda da belirttiğimiz [kullanım kolaylığı](/genel/2020/07/23/DeFi-yeni-ICO-cilginligi-mi.html). Herhangi bir şekilde hiç bir yere kayıt, evrak vs gönderip başvuru sonucu beklemeye gerek yok.  Uniswap’ı kullanmak isteyen birinin tek ihtiyacı olan bir kripto cüzdan. Kullanıcı Uniswap [sitesine](https://app.uniswap.org/#/swap) girdikten sonra sağ üst tarafta bulunan butona basıp cüzdanını bağladığı anda sistemi kullanmaya saniyeler içinde başlayabiliyor. 

### Peki nasıl çalışıyor sistem?

UniSwap aslında robot (otomatik) bir piyasa yapıcı. Robot denmesinin nedeni fiyatların çok basit bir algoritma ile otomatik olarak “el değmeden” belirlenmesi. Gelin bakalım nasıl çalışıyor bu otomatik sistem: 

Uniswap’ta bütün işlemler için çift bölmeli bir havuz var, yani iki token’dan oluşan. Siz kullanıcı olarak havuzdan bir token almak istiyorsanız, karşılığında havuza diğer tokenı bırakmak zorundasınız.  Yani alım-satım dediğimiz aslında bir swap (bir tokenı diğeri ile değiştirme) işlemi oluyor. 

Havuz ilk kurulurken iki tarafının piyasa değeri birbirine eşit. Her bir bölme içine ne kadar gerekiyorsa o kadar token ile dolduruluyor. Sonrasında bu token adetleri çarpılarak sabit bir toplam havuz büyüklüğü bulunuyor. İşte bu sabit havuz büyüklüğü sayısı kritik, çünkü tüm sistem hesaplamaları bu sayıya dayanıyor. 

Dilerseniz bir örnek ile anlatalım: 

Diyelim bir havuz oluşturulacak. Bir bölüme ETH, diğerine ise USDC (bir çeşit sanal ABD Dolarına çıpalı bir stabil para) konacak. 

- İlk başlangıçta kurulurken bu iki havuzun piyasa değerleri eşit olmalı ki işe doğru bir şekilde başlansın.  Basit olması için başlangıçta havuzu doldururken piyasalarda 1 ETH’nin değeri 300 USDC varsayalım. ETH havuzuna diyelim 100 ETH kondu, o zaman USDC havuzuna da 30,000 USDC konacak. 
- Şimdi gelelim temel prensibe: “İki havuzdaki para adedinin (değer değil ADET) çarpımı her zaman sabit olacak”. Kulağa saçma geliyor değil mi? Haklısınız, ama örneğimizden devam edelim: Burada 100 adet ETH ve 30.000 adet USDC olduğu için toplam havuz katsayımız bu iki sayının çarpımı olan 3.000.000. Bu sayı hep sabit. [1]
- İşlem yapmak isteyen biri havuza geldiğinden ETH satmak istiyorsa karşılığında havuzdan bunun karşılığı USDC alacak, eğer ETH almak istiyorsa bunun karşılığı kadar USDC koyacak. Peki bu “karşılık” nasıl belirlenecek? İşte orada temel prensibimize geri dönüyoruz. Yani sabit sayımıza. Örneğe bakalım:
Diyelim biri gelip 1 adet ETH satmak istiyor. Bu durumda ETH havuzu bir adet artıp 101 ETH’ye çıkıyor. Sabit sayımız 3,000,000 idi ve bu sayı ETH adedi ile USDC adedinin çarpımına eşit olacaktı. O zaman USDC havuzunun büyüklüğü 3,000,000/101=29.702 adet olmalı. Yani ETH alan kişiye havuzdaki ETH’lerin 30,000-29,702=298 adedi gönderilir. (Ama fiyat 300 USDC olacak idi, neden 298 alıyorum? Çünkü likit olmayan bir piyasada büyük bir işlem yaptınız ve piyasayı hareket ettirdiniz. Buna slippage (kaygan düşüş-performans düşüşü) deniyor. Eğer çok büyük bir havuzda küçük işlem yapanlar için böyle büyük bir fark çıkmaz)
Peki biri daha gelip bir ETH daha satmak isterse? Aynı işlem tekrarlanır. Yani ETH sayısı 102’ye çıkar, USDC rakamı ise 3.000.000/102=29,412 adede inmeli. Havuzda 29,702 adet var. İkisinin farkı 290 adet USDC kişiye gönderilir. Birinci satan ile ikinci satanın aldıkları USDC farkının ne kadar büyük olduğunu görüyorsunuz değil mi?
Peki üçüncü bir işlem olarak biri gelir ve bu sefer satmak yerine 1 ETH almak isterse? Farketmişsinizdir sistem hep ne koyacağınıza bakıyor. ETH almak istiyorsunuz o zaman USDC koymak zorundasınız. Diyelim 300 USDC getirdiniz sisteme. O zaman USDC havuzu 29,412’den 29,712’ye çıkıyor. Katsayımızın 3,000,000’u yeni USDC havuzu olan 29,712’ye böldüğümüzde bize yeni ETH havuzunun 100,97 olması gerektiğini söyler. Havuzda geçen işlem sonrası 102 ETH kalmıştı, farkı olan 1.03 ETH alıcıya gönderilir. Farkı görüyorsunuz değil mi? Piyasada 300 USDC’ye 1 ETH alabilecek iken daha önce iki kişi ETH sattığı için şimdi 1.03 ETH alabiliyor bir alıcı. 

Üç işlemin sonuçları tablo olarak!!!!

Sistemin kritik noktaları: 

Sistemdeki kritik nokta ani fiyat artışlarında ortaya çıkabiliyor. Eğer piyasalarda ETH fiyatı aniden 400 USDC’ye çıkarsa, UniSwap robot sistem olduğu için ani tepki veremiyor. Bunun ne gibi zararı var? Bir kısım arbitraj yapanlar, anında UniSwap havuzuna USDC koyup ETH’leri ucuzdan (karşılığında 400 USDC verilmesi gereken noktaya kadar) çekebiliyorlar. 

Böyle bir durumda havuza başlangıçta para koymuş birinin durumunu düşünelim. Diyelim havuzun bir tarafına 10 ETH diğer tarafına ise 3,000 USDC koydu. ETH fiyatı 400 USDC’ye çıktı ve al-sat’çılar işlem yaparak havuzu da bu orana çektiler. Havuzda şimdi 86.6 ETH ve 34,641 USDC olacak. (Neden derseniz ayrıntılı işlemi dipnotta) [5]. Likidite olarak bu kişinin parası 8.66 ETH ve 3,464 USDC’ye denk geliyor. Bu da USDC cinsinden 8.66 ETH x400=3,464 artı 3,464 ETH toplam 6,928 USDC olur. Halbuki bu kişi elinde 10 ETH’yi tutsaydı USDC cinsinden 10 ETH x 400=4,000 artı 3,000 USDC toplam 7,000 USDC olacaktı. Aradaki para nereye gitti? Sistemde fiyatların ani artışını değerlendiren al-sat’cılara. Buna “geçici kayıp” (impermanent loss) deniyor, zira bir noktada ETH tekrar 300’e gelirse o zaman havuza likidite koyanın zararı ortadan kalkıyor. 


Kim neden havuza para koyar?

Peki kim havuza bu parayı koyuyor? Yatırımcılar ya da likidite sağlayıcılar dediğimiz kişiler. 
Neden koyuyorlar bu parayı? İşlem yapıldığında belli bir komisyon ücreti ortaya çıkıyor (Uniswap için şu anda %0.3 oranında), onu alıyorlar. 

“Peki kim neden getirir de havuz kurar?”. Sistemin temelinin işlem hacmine dayandığını söylemek gerek. Yani eğer piyasada alıcı ve satıcılar çok ise ve bunlar işlem yaptıkça UniSwap her bir işlemden %0.3 komisyon alıyor. Bu komisyonlardan kazanılan para şimdiye kadar ani değişikliklerden kaybedilen paranın önüne geçmiş ama bu ileride de böyle olacağı anlamına gelmiyor. Yani likidite koyanlar ciddi bir risk taşıyorlar. 

[Uniswap içinde USDC koyanların getirisi] [Kaynak](https://zumzoom.github.io/analytics/uniswap/roi/)

Havuzların ani ve kalıcı fiyat değişikliklerinden etkilendiği düşünüldüğünde havuzlar içinde en kârlı olanları aslında değerlerinin tekrar eski haline döneceğini bekleyeceğiniz ikililerin olduğu çiftler. Nedir bunlar derseniz, stabil para havuzları. Örneğin USDC/DAI benzeri havuzlar. Stabil paralar genelde 1 ABD Doları’nın etrafında gezinir dururlar. Bazen üzerine çıkar, bazen altına inerler. Ancak iniş çıkışlar da az rakamlar olur. O nedenle böyle havuzlar likidite koyucular için çok kârlı olabilir. Tabii, madalyonun öbür tarafında bu çiftlerinde işlem yapan çok olur ancak marjların az olduğu bir yerde bir de UniSwap’a 0.3% komisyon vermek ister mi al-sat yapanlar? Tabii ki hayır ve işte bu nedenle stabil paraların ikili havuzlarını yaratan Curve çok popüler oldu. 

Rakipler kimler? 

Curve: 
Curve daha çok sabit paralar üzerine uzmanlaşmış bir sistem. Zira Curve’un komisyonlar UniSwap’un aksine 0.04% oranında ve işlemlerde kullandığı algoritma UniSwap’a nazaran özellikle stabil paralar için daha uygun. O nedenle işlemler ciddi şekilde Curve’e kaymış durumda. [4]

Balancer: 
UniSwap’tan bahsederken temel bir özelliğin havuzun iki bölmesine eşit değerde iki para koymak olduğunu belirtmiştik. Balancer temel olarak burada sistemi bir adım öteye götürerek, havuza iki bölmesine konan paraların 50%-50% değil istenen oranlarda olmasına imkan tanıyor. 



[1]Basitleştirmek için böyle yazıldı. İki istisnası var havuz büyüklüğünü değiştiren: 
Birincisi havuza başka yatırımcılar para koyarsa havuzun toplam büyüklüğü değişiyor normal olarak. Örnek olarak bir yatırımcı gelip 10 ETH ve 350 USDC koyarsa, havuzun toplam büyüklüğü 350,000’den 423,500’e (110 ETH x 3,850 USDC) çıkıyor. 
İkincisi ise işlem yapanlardan alınan komisyonlar (Uniswap için %0.3) bu havuza ekleniyor, dolayısıyla havuz büyüklüğü otomatik yükseliyor. 

[2] Daha da karışmasın diye basitleştirdik. Bunun için de havuz büyüklüğü sabit sayısının satın alınan token adedine bölünmesi, havuzda ne kadar Dolayısıyla havuzda 99 ETH kalacağı için 1 ETH alan kişinin koyması gereken para 3,500,000/99=35,354 USDC olması lazım. 35,000 adet USDC olduğuna göre koyacağı rakam 354 USDC olacak. Havuz sığ olduğu için 354 ile 350 arasındaki gibi büyük bir fark çıkıyor. Havuz büyük olsaydı bu rakam 350’ye çok yakın olacaktı. Sistem fiyat olarak 350 demesine rağmen kullanıcının işlemi 354 yapması nedeniyle oluşan aradaki farka Price Slippage (fiyat kayması) deniyor. Havuz ne kadar büyük ve işlem havuz büyüklüğüne göre ne kadar küçük ise fiyat kayması o kadar az oluyor. 

[3] Havuzdaki fiyat nereye kadar izin veriyorsa (bu örnekte USDC/ETH’nin 450’ye ve toplam miktarın 3,500,000’e eşit olmasını sağlayacak rakamlara, ki burada 12 ETH satışı ile ulaşılır. 12 ETH satışı 12x350= 4.130 USDC getirir. USD miktarı 35,000’den   39,130’a çıkar

[4] Curve’in özelliği stabil paralara uyacak bir algoritma içermesi. Uniswap havuz değeri için A ve B token’larının çarpımını sabit tutarken, Curve A ve B tokenlarının toplamını sabit tutuyor. Böyle olunca, birbirine yakın ve fiyatları genelde çok ayrışmayan (burada stabil paralar gibi 1 ABD Doları’na yakınsayan) paralarda değer çok daha yavaş değişip işlem olduğunda büyük fiyat farkları oluşmuyor. Ama eğer çok büyük hacimler olur ve iki token arasında fiyat farkları oluşursa o zaman Uniswap daha gerçekçi fiyatlar veriyor. 

[5] Matematiksel olarak havuzun içindeki ETH fiyatı USDC adedinin ETH adedine bölünmesi ile ortaya çıkıyor. USD adedi ile ETH adedinin çarpılması ise havuzun sabitini veriyor. O zaman ETH fiyatı ile havuz sabitini çarpımının karekökü USDC adedini verir. 
Bu işlemi yaparsanız USDC adedi 34,641’i verir. Bu sayıyı toplam havuz değerine bölersek ETH adedi olan 86.6025’e ulaşırız.  Sağlama için USDC adedini (34,641) ETH adedine (86.6025) bölersek ETH fiyatı olan 400 çıkar. 
