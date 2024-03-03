#YAZI I

Blokzincir altyapıları konusunda en çok konuşulan ve üzerine kafa yorulan konulardan biri monoblok ve modüler blokzincir yapıları. Ne demek, ne işe yarar, gelin hep birlikte bakalım. 

### Blokzincir üzerindeki uygulamaların uyumu
Web3 dünyasının klasik dünyaya göre en önemli farklarından biri, oluşan standartlar sayesinde, kullanıcıya hizmet veren farklı oyuncuların birbirleri ile uyumlu (ahenk içinde) çalışabilmeleri. Gelin biraz daha açalım bu cümleyi:

Klasik dünyada, her bir girişim son kullanıcıya vereceği hizmeti (ya da ürünü) önce kurgular, sonra bazı kısımları geliştirir, bazılarını dışarıdan alır, en sonunda da bütün parçaları tek tek bir araya getirir ve kullanıcıya sunar. Bu durumun artısı kullanıcıya rahatlık ve kolaylık sağlaması. Temel eksisi ise, kullanıcının sadece hizmet verenin sunduğu paket ile yetinmek zorunda kalması.

Web 3 dünyasında ise durum farklı. Bu dünyada kullanıcı hizmeti (ya da ürünü) oluşturan her bir parçayı kendi seçebiliyor. Web3 dünyasındaki farklı girişimlerin ürettiği her bir parça, blokzincir üzerindeki standartlara uyarak birbirileri ile uyum içinde çalışabiliyor. Bunun temel avantajı, bir yanda parçaları geliştirenler arasından yaşanan rekabet diğer yanda tek bir parça üzerinde uzmanlaşmanın getirdiği inovasyon hızı. Bu dünyada girişimler sadece tek bir sorun ile uğraşıyorlar, diğer sorunları farklı girişimler zaten çözdüğü için hazır çözümleri kullanmak kendilerine zaman ve hız kazandırıyor.

Uygulamalar parça parça birbirileri ile uyumlu çalışıyorlar, çok güzel. Peki ya bu uygulamalara ev sahipliği yapan blokzincir altyapılarını da böyle parçalara bölerek daha rekabetçi ve hızlı hale getirebilir miyiz? 

Konuya aşina olmayanlar için bu soru başta garip gelebilir. Neden blokzincir altyapısını parçalara bölmek zorunda olalım ki? Bu soruyu hakkıyla cevaplamak için blokzincirin kısıtlarını anlamamız gerek. Zira ilk bakışta biz son kullanıcıları direkt olarak ilgilendirmiyor gibi görünen bu sorun, aslında cebimizden işlem ücreti olarak çıkan paranın artması nedeniyle direkt cebimizi de etkiliyor. 

#### Blokzincirlerin kısıtları

Blokzincirlerin temel işlevini kişiler arasında yapılan işlemlerin geri döndürülemez (değiştirilemez) bir biçimde kayıt edilmesi olarak tanımlayabiliriz. İşlemleri geri döndürülemez şekilde gerçekleştirebilmenin temel yollarından biri, bu kayıt defterini tutan makinelerin sayısını olabildiğince çok, bulundukları yerleri de olabildiğince dağıtık yapmak, ki bu sayede sistemi ele geçirmek imkansız (ya da çok pahalı) hale gelsin.

[Aslına bakarsanız, merkezi sistemler tek bir yerden yönetildikleri için blokzincire göre çok daha hızlı ve üstündürler. Bu merkezi sistemlerin zayıf karnı ise, bu tek yerin, dışarıdan gelecek saldırı ya da baskılara karşı koyamaması.  Özellikle saldırılara karşı sistemi 'kurşun geçirmez' yapabilirsiniz ama politik ya da toplumsal baskılara karşı koyabilmek teknik konulara göre çok daha karmaşık ve çözümü zor. Neticede sistemleri yönetenler de birer insan.][BU BURADA MI KALSIN YOKSA FOOTNOTE MU YAPAYIM KARAR VEREMEDİM]

Olabildiğince çok makine kullanmak için, blokzincirin kayıt defterini küçük tutmak zorundasınız. Bunu yapmazsanız, sistemi ancak kapasitesi yüksek makineler yürütebilir, bu da makine sayısının azalması (yani sistemin merkezileşmesine) sonucunu doğurur ve güvenlik riski doğar. 

Blokzincirlerin temel olarak sattıkları 'şey' bu blok alanıdır. Kayıt defterini küçük tuttuğunuzda ise, bu sefer yüksek talebi karşılamakta zorluk çeker hale gelirsiniz. Blokzincirler (ideal olarak) yüksek talep geldiğinde durmazlar[^6], onun yerine işlem ücretlerini artırırlar ki, işi acil olmayanlar beklesin. Bu durum, bir noktaya kadar makul görünse de, yüksek işlem ücretleri kullanıcıları bir noktadan sonra alternatif arayışlara doğru itebilir.  

#### En büyük blokzincirlerden Ethereum'un sıkıntıları

İşte Ethereum uzun süredir böyle bir sorun ile karşı karşıya durumda. 2020-21 yılları arasında DeFi ve NFT alanındaki yoğun talep nedeniyle Ethereum işlem ücretleri inanılmaz derecede arttı. Ethereum geliştiricileri bu soruna hızlı bir çözüm bulmakta yetersiz kaldılar. 

Ethereum'u geliştiren topluluk başlangıçta, blokzinciri dikey olarak parçalara bölerek talebi karşılamak gibi bir hayale sahipti. (Bunu Ethereum bir ada ise, aynı işi yapan küçük küçük adacıklar olarak düşünebilirsiniz; bir adada DeFi bir başka adada NFT işlemlerinin yapılması gibi). Sonrasında bunun havadaki bir uçağın motorunu seyir halindeyken parçalara bölmekten daha zor bir iş olduğunu anlayan geliştiriciler, strateji değişikliğine gitmek zorunda kaldılar. Bu değişiklik sonrası, sistemleri üzerinde yük oluşturan parçaları dışarı vermeye (bir nevi 'outsource' etmeye) başladılar. 

### Blokzincirin parçaları neler?
Yukarıda yazdığımız gibi blokzincirin temel özelliği bir kayıt defteri olması. Blokzincirin kayıt tutarken gerçekleştirdiği dört temel fonksiyon var. Bu dört temel parçayı şu şekilde özetleyebiliriz: 

- **İşlemi gerçekleştirmek (execution)**: Aklınıza gelebilecek her tür işlemin yapılması. Bu bir kişiye para göndermekten, merkeziyetsiz bir borsada token alım-satımına, ya da NFT satın almaya kadar her tür işlemin bizzat yapılması. Biz son kullanıcılar için en tanıdık blokzincir fonksiyonu. 
- **Yapılan işlemi sıralamak (consensus)**: İşlem yapmak için emir verdiniz, çok güzel. Yapmak istediğiniz işlem hemen blokzincire yazılmıyor. Bir havuzda toplanıp sonra işleniyor. Toplama sırasında işlemlerin bir sıraya konması gerekiyor. Neden? Aynı anda iki kişi aynı işlemi yapmak isteyebilir. Bunlardan biri öne geçiyor (daha yüksek işlem ücreti veren). Ya da bir kişi aynı hesaptan iki işlem birden göndermek isteyebilir[^1]. İşte bu sorunları önlemek için makinelerin emirlerin hangi sırayla blokzincire işlenmesi gerektiği konusunda 'uzlaşması' gerekiyor. 
- **İşlem sonuçlarının bloğa yazılıp kesinleşmesi (settlement)**: İşlemler yapıldı, sıraya kondu. Şimdi sıra bunun sonucu olarak oluşan durumun blokzincire yazılmasına geliyor. Yani siz birine para gönderdiğinizde blokzincir sizin hesabınızın o para kadar azalması karşı tarafın hesabının ise aynı oranda artması gerekiyor. Bir önceki adımda, makineler (madenciler ya da onaylayıcılar) hangi işlemin hangi sıra ile gerçekleşeceği konusunda uzlaşıp blokları oluşturduktan sonra hesapların son hali blokzincir üzerinde kesinleştiriliyor.
- **İşlem sonuçlarının tüm sisteme anons edilmesi (data publishing)**: İşlemler yapıldı, sıraya kondu, bloğa kondu ve blokzincire işlendi (yani para el değiştirdi); şimdi sıra bunun tüm sisteme bildirilmesine geldi. Bu önemli bir konu, zira uygulamaların bundan sonra yapılacak işlemler için hesapların son durumunu kullanması gerekiyor. [^2]

### Monoblok ve modüler zincirler
Blokzincirin yukarıda saydığımız fonksiyonlarının nasıl gerçekleştirileceği konusunda iki farklı ekol var. Bunlardan bir tanesi yukarıda saydığımız bütün fonksiyonların tek bir elden yapılması (aynı Apple ekosistemi gibi), diğeri ise her bir işlemin farklı farklı oyuncular tarafından yürütülmesi (bir nevi android sistemler gibi).

Bitcoin ve Solana'nın başını çektiği ağlar, monoblok yapı dediğimiz birinci ekolu benimsediler. Bitcoin için bu yolu seçmek kolaydı, zira Bitcoin özünde tek bir uygulamaya bağlı bir ağ (ingilizcesi application specific). Bahsettiğimiz tek uygulama da Bitcoin parası olan BTC. Bitcoin üzerine uygulama kurmak mümkün değil, çünkü akıllı kontrat desteği yok[^3]. Bu nedenle, Bitcoin kendini basit tutarak ölçeklenme yoluna gitti[^7].

Solana ise, çok daha genele hitap eden, üzerinde akıllı kontrat çalışan bir ağ. Onlar ise, ölçeklenme problemini blokları büyüterek çözdüler. Bu durumun yan etkisi, sistemi yürüten makinelerin yüksek kapasite ihtiyacı, bunu karşılayacak makine sayısı az olduğu için sistemin merkezileşme riski. 

Yelpazenin öbür ucunda ise, yukarıda saydığımız fonksiyonları farklı farklı yapan yerler var. Örneğin, son birkaç yıldır en çok konuşulan konu Ethereum üzerine kurulu ikinci seviye çözümler. Gelin önce ikinci seviye çözümlerin mantığını anlamaya çalışalım. 

#YAZI II

### İkinci seviye çözümler 
Ethereum'un kısıtları konusunda da değindiğimiz gibi, üstüne gelen yoğun talebi karşılayamayan Ethereum sistemi, merkeziyetsizlikten ödün vermeden büyüyebilmenin yolunu kimi fonksiyonlarını dışarıya atmakta buldu. Burada ön plana çıkan konu ikinci seviye çözümler oldu. 

İkinci seviye çözümler, yukarıda saydığımız dört fonksiyon içinden Ethereum üzerinde en çok yer işgal eden 'işlem gerçekleştirme'yi Ethereum üzerinden almaya talipler. Tam olarak ne demek bu? Açıklayalım: 

Ethereum diğer bütün ağlar gibi esasında bir yazılım. Bu üzerinden bir uygulama geliştirmek ya da uygulamayı kullanmak istiyorsanız, sistemin kullandığı yazılım olan EVM'i işletmeniz gerekiyor. EVM'i çalıştırmak Ethereum ağını sürdüren makineleri en çok yoran bir başka deyişle Ethereum'un sunduğu temel ürün olan blok alanını en çok kaplayan konu. Bu durum, Ethereum'un işleyebileceği işlem miktarını azaltıyor, talebi artırdığı için işlem ücretlerinin de artmasına neden oluyor. 

İkinci seviye çözümler, kullanıcıların yapmak istedikleri bu işlemleri kendi üzerlerine almayı talep eden ayrı birer blokzincir aslında. En basit haliyle anlatırsak, kullanıcıların istediği işlemleri toplu bir şekilde gerçekleştirip, sonuçlarını Ethereum üzerine yazıyorlar. Bir nevi, 'bilgisayarlarımızda yer kaplamasın diye on-yirmi dosyayı bir araya getirip zip yapmak' gibi düşünebilirsiniz. Bu da kullanıcı için ödediği işlem ücretlerinin dramatik şekilde düşmesi demek.  

Peki o zaman, diğer birinci seviye dediğimiz Solana, Avalanche gibi zincirlerden farkları ne? Onlar da kullanıcılarına Ethereum'a göre çok daha ucuza işlem yaptırıyorlar? Temel farkları, kullanıcının yaptığı işlemlerin doğru ve eksiksiz gerçekleştiği konusunda Ethereum'un kullanıcıya sunduğu güvencenin aynısını sunabilme avantajı. Nasıl oluyor bu? 

Efendim, Ethereum, Solana ya da Avalanche gibi ağlarda kullanıcı olarak işlem yaptığınızda işlemin doğruluğunu sağlayanlar o ağı işleten onaylayıcılar. Bu onaylayıcılar yaptıkları işlemin doğru olduğunun garantisini vermek için ellerinde tuttukları tokenleri (ETH, SOL ya da AVAX) sisteme rehin veriyorlar. Eğer bu onaylayıcılar 'yamuk' bir işe kalkışırlarsa koydukları tokenler yanıyor. Eğer siz kötü niyetli biri olarak sistemi ele geçirmek isterseniz, mevcut rehin edilmiş tokenlerin önemli bir kısmını elinde tutmanız gerekir (bu oran ağdan ağa değişiyor, %33, %51 ya da %66 olabiliyor). Ethereum'un piyasa değeri daha yüksek olduğu için, diğer küçük ağlara göre 'göreceli' daha güvenli olarak adlandırılıyor. 

İşte ikinci seviye çözümler, kendi başlarına yeni bir ağ çıkarmak yerine Ethereum'un verdiği bu güvenceyi kullanıyorlar. Peki tam olarak nasıl kullanıyorlar bu güvenceyi? Şöyle açıklamaya çalışalım. İkinci seviye çözümler kendilerini bir akıllı kontrat ile Ethereum ağına bağlıyorlar. Bu akıllı kontrat sayesinde, kullanıcı ikinci seviye çözümü kullansa bile, parası temelde Ethereum üzerinde duruyor. Yarın öbür gün, ikinci seviye çözüm durursa, kullanıcı yapmak istediği işlemi Ethereum üzerinde de gerçekleştirebiliyor. Yani parası güvende. Diğer zincirlerde durma yaşandığında (Solana bir ara çok dururdu, şimdi biraz azaldı) kullanıcı parası da sistemde takılı kalabiliyor.

Şunu unutmamakta fayda var. İkinci seviye çözümler, Ethereum güvencesini verseler de sonuç olarak farklı birer blokzincirler. Bunun avantajları ve dezavantajları var. Temel avantajı, farklı blokzincirler olarak kullanıcıya yeni ürün ya da hizmetleri sunabilirler. Ethereum'un herhangi bir iyileştirme yapması, çok büyük ve çok yere dokunan bir zincir olduğu için kolay değil, yavaş oluyor. İkinci seviye çözümler bu konuda çok daha atak olabiliyorlar. 

Örneğin, son kullanıcılar için en büyük problemlerden bir tanesi, sahip oldukları cüzdanlarda sakladıkları ve blokzincirdeki varlıklarına ulaşmayı sağlayan özel anahtarları oluşturmada kullanılan 12 kelimeyi kaybetme riski. Kullanıcının 12 kelimeye ihtiyaç duymadan ve kaybolma riski taşımadan cüzdan sahibi olmasının teknik bir çözümü var.  Aralarında Türk gençlerinden kurulu bir girişim olan Clave de dahil olmak üzere pek çok cüzdan uygulaması bu konuda çalışıyor. Ne var ki, Ethereum'un bu temel çözümü getirmesi zaman alacak[^4]. Oysa ikinci seviye çözümler, örneğin zkSync ve Starknet bu çözümü hemen kendi temel sistemleri içine aldılar bile. 

Dezavantajlarına gelince, ikinci seviye çözümlerin kendileri de birer yazılım. Bu nedenle, ne kadar çok yazılım kullanırsanız, o kadar içinde çıkabilecek hatalara karşı korumasız hale geliyorsunuz. Bu da unutulmamalı. 

Ethereum'un yavaş yavaş gitmeye çalıştığı modüler blokzincir alanının ön plana çıkan oyuncusu ise Celestia oldu. 

#[YAZI III]

### Celestia nedir?
Celestia, yukarıda saydığımız dört fonksiyondan iki tanesini yapmaya aday basitleştirilmiş bir altyapı blokzinciri. Bu iki fonksiyon, aslında son kullanıcıya çok da dokunmayan, yapılan işlemi sıralama (uzlaşma) ve işlem yayınlama (data publishing) fonksiyonları. 

Kripto alanının iki saygın ismi olan Nick White ve Mustafa Al-Bassam tarafından kurulan Celestia, kendisini diğer blokzincirlere hizmet veren bir altyapı (bir nevi B2B) olarak tanımlıyor. Hizmet verdikleri bu iki alandan özellikle 'işlem yayınlama', onlara göre blokzincirlere fazla değer katmayan, adeta yük olan bir fonksiyon. Neden? 

İşlem sonuçlarını yayınlama (data publishing) çok fazla blok alanı isteyen bir fonksiyon. Bu, kendi blokzinciriniz varsa çok büyük bir sorun olmayabilir ama eğer Ethereum üzerine kurulu ikinci seviye çözüm iseniz, işlemleri Ethereum üzerinde yayınlamanız gerekiyor. Mevcut Ethereum yoğunluğu içinde bu, ikinci seviye çözümler için çok ciddi bir külfet demek. Şu an ikinci seviye çözümlerin maliyetleri içinde en büyük kalem burası. Celestia ile bu maliyetleri 100'de birine indirmek mümkün. İşte Celestia'nın sunduğu temel çözüm bu[^8]. 

Celestia, son kullanıcı ile blokzincirlerin temel fonksiyonun işlem gerçekleştirme (execution) olduğuna, bu nedenle blokzincirlerin bu alana odaklanması gerektiğine inanıyor. Özellikle ikinci seviye çözümler için temel değer önerileri şu şekilde: 'Kullanıcının parası, Ethereum zinciri üzerinde güvende. Sen son kullanıcının istediği geliştirmeleri yap, ona odaklan. Beni kullanarak işlemlerini çok daha ucuza yayınlayabilirsin.2 

Bu arada şunu hemen belirtelim. Celestia'nın bu işlemi Ethereum'a göre çok ucuza yapmasının iki temel nedeni var. Birincisi, Ethereum'un blok alanına olan yoğun talebin getirdiği yüksek maliyetin Celestia'da olmaması. Daha önemli olan ikinci neden ise, Celestia'nun Ethereum'a göre teknik bir üstünlüğü. Bu ikinci konuyu biraz daha açalım:

İşlem sonuçlarını yayınlama konusunda, çıkabilecek en büyük problem, işlemlerin toplandığı bloğu oluşturan onaylayıcının bir kısım işlemi göstermemesi (saklaması) olabiliyor. Ethereum üzerinde böyle bir sorun yaşanmaması için, bütün onaylayıcılar blok üzerindeki tüm işlemler yayınlanmış mı her bloğu tek tek inceliyorlar. Bu da çok büyük bir yük getiriyor onaylayıcılara. Ethereum'un buna Protodanksharding denen bir çözümü var ama bunun hayata geçmesi 2026 yılını bulabilir. Basit olarak, bloğun içinden rastgele parçalar alarak bloğun eksiksiz olduğunu anlama olarak adlandırabiliriz bu yöntemi. Bu sayede, onaylayıcıların tüm bloğun üzerinden geçmesine gerek kalmıyor. Bu da, basit onaylayıcılar ile çok sayıda işlemi onaylayabilme imkanı getiriyor. İşte Celestia, Ethereum'un ağırlığı nedeniyle hemen uygulayamadığı bu yeniliği hayata geçiriyor. 

Şimdiden birçok çözümün Celestia kullanmaya başladığını söyleyebiliriz. Celestia, kendine ait bir zinciri olduğu ve bu zincirde uzlaşma da yaptığı için sistemi yürütmek için onaylayıcılara ihtiyaç duyuyor. Bu onaylayıcıları besleyebilmek için de kendilerine ait TIA tokeni çıkarmış durumdalar. Celestia'nın çözümü çok ucuz olduğu için onaylayıcılara şu aşamada çok fazla bir komisyon geliri gelmiyor. Bu durumu öngördükleri için ekip, ilk dönem için %16 gibi oldukça yüksek bir staking geliri veriyor onaylayıcılarına. 

Peki rakipleri var mı Celestia'nın? Elbette var. En önemli iki rakibi EigenlayerDA ve Avail. EigenlayerDA, Ethereum üzerinde çok moda olan Ethereum güvenliğini başka zincirlerde de kullanmaya yarayan ve restaking olarak adlandırılan yeniliği bulan ekibin çıkardığı ilk ürün. Avail ise Polygon blokzincirini geliştiren ekibin içinden ayrılanların oluşturduğu bir girişim. Her iki girişim de şu anda geliştirme aşamasında. 

### Başka neler var?
Modüler dünyada her bir parça için farklı farklı çözümlerin hızlı bir şekilde ortaya çıktığını görüyoruz. Örneğin, yukarıda saydığımız fonksiyonlardan işlemleri sıralama konusuna odaklanmış espresso bunlardan biri. Ya da ikinci seviye blokzincirler arasında hızlı data aktarımı sağlamayı amaçlayan Hyperlane ya da Axelar gibi projeler var. Ya da, anahtar teslimi ikinci seviye çözüm sunan Dymension, Conduit gibi hizmet sağlayıcılar yarış halindeler [^5]. 

Celestia sıfıra gidecek mi?
İkinci seviye çözümler Solana kadar tucuz olacak mı?



[^1]: Meşhur 'çifte harcama' problemi, ingilizcesi double spending. Kişi aynı parayı A ve B kişine aynı anda göndermeye çalışabilir. Bunu yaptığında makinelerden bir kısmı A kişisine giden işlemi alır, kimileri ise B kişisine giden işlemi. Böyle bir durumda iki ayrı blok sisteme girer. Zaman içinde topluluk ya A kişine giden bloğun peşine takılır ya da B kişisine giden bloğun. Böylece konsensus oluşmuş olur. 
[^2]: 'Data publishing' olarak adlandırılan bu özellik, kimi zaman 'data availability' olarak yanlış adlandırılabiliyor. 'Data availability' geçmiş tüm işlemlerin saklanması olarak düşünülebilir  (bir başka deyişle ingilizcede data storage olarak adlandırılan kavram) - onun blokzincir üzerindeki tüm makinelerde saklanmasına gerek yok. Birkaç makine bütün geçmişi (ya da arşivi) saklayabilir. 
[^3]: Basitleştirmek için bu şekilde anlatıyorum, teknik arkadaşlar hemen çullanmasın. Aslında kastedilen, 'script' dediğimiz kodların çok kısıtlı olması. Taproot geliştirmesi ile birlikte özellikle ordinals üzerinden bu kısıt bir parça kırıldı ama hâlâ yeterli sayılmaz. Bitcoin üzerine ikinci seviye çözümler de geliştirilmeye çalışıyor ama bu çözümlerin tam layıkıyla çalışabilmesi için Bitcoin üzerinde yeni güncellemelerin gelmesi (bir nevi soft fork olması) gerekiyor ki bu tip güncellemeler Bitcoin'e üç-dört yılda bir ancak geliyor. Bu güncelleme gelene kadar Bitcoin üzerinde akıllı kontrat kullanımı için bir ara çözüm olan BitVM geliştiriliyor. İlgilenenler bu alanda çalışan Türk bir ekibin (Chainway) kurduğu Citrea çözümünü inceleyebilirler. 
[^4]: EIP 4337 denen bu çözümü kökten sisteme koyamayan Ethereum, bunu bir standart (ERC) olarak yavaş yavaş genele yaymayı planlıyor. 
[^5]: Örnekleri çoğaltmak mümkün. Örneğin, zero-knowledge bazlı ikinci seviye çözümlerin Ethereum sistemine gönderdiği kanıtları oluşturmak için kullandıkları sistemlere prover deniyor. Bunu zkSync gibi kendi mutfağında hazırlayanlar olduğu gibi RiscZero gibi hardware üzerinden optimize etmeye çalışanlar var. Ayrıca her gün yeni yeni projelerin de bu alanlar içinde yarışa katıldığını söyleyebiliriz.
[^6]: Duran blokzincirler yok mu? Var tabii. Bu alanda sabıkası olan zincirler var ama onların henüz yeterince olgunlaşmamış olduğunu söyleyerek şimdilik istisna olarak görüp konumuz dışında bırakıyoruz. 
[^7]: Bunun uzun vadede sürdürülebilir bir strateji olup olmadığı konusunda tartışmalar mevcut. Bu haliyle Bitcoin sistemini sürdüren madencilerin ana gelir kaynağı yeni blok oluşturma sonrası verilen madencilik ödülleri. Bu ödül ise her dört yılda bir yarılanıyor. Madencilerin bir diğer gelir kalemi olan işlem ücretleri, Bitcoin sadece para transferi için kullanılırsa çok az kalıyor. Eğer Bitcoin üzerine yeni sistemler (örneğin DeFi kullanan ikinci seviye çözümler) olursa, o zaman işlem ücretleri ve madencilerin gelirleri de artacak. 
[^8]: Celestia'nın sunduğu diğer çözüm olan uzlaşma 'consensus' ise şu şekilde çalışıyor: Bir blokzincir işlemleri kendi sıralamak isterse, bunun için kendi onaylayıcıları olmak zorunda. Kendi onaylayıcıları olması için uygun bir altyapı kurması, sonra bu onaylayıcıları tutmak için bir token çıkarması, dahası bu token için bir ödül mekanizması sunmak zorunda. Bunlar hem zaman ve emek isteyen hem de uygun optimal bir token mekanizması gerektiren konular. Celestia şu an için bu hizmeti sunuyor olsa da aslında ön plana çıkardığı hizmet diğeri yani 'data publishing'. Uzlaşma  'data publishing' hizmeti verebilmek için gerekli bir fonksiyon - temel amacı bu. Ama dileyen olursa bu hizmeti ayrıca de Celestia'dan alabilir. Müşterilerin bu hizmeti kullanması için Celestia tokeni olan TIA'nın ciddi şekilde değerlenmesi gerekli. 
