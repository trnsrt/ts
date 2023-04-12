Bu yazımızda Euler Finance'in başına gelen 200 milyon ABD Doları tutarındaki hack ve sonrasında yaşanan heyecanlı sahneleri konuşacağız. 

Hızla gelişen DeFi dünyasında 'sürat felakettir' sözünün sıkça kullanmamıza neden olan 'hack' (Türkçesine 'sistemin zaafından yararlanma' diyebiliriz) olaylarından birini daha yaşadık geçtiğimiz ay içinde. Bu defa hikaye mutlu sonla bitse de, gerek olayın gelişimi gerekse de hack sonrası yaşananlar adeta bir polisiye filmi andırıyor. Gelin önce Euler Finance nedir ve nasıl 'hack' yedi onu anlayalım, sonrasında da peşi sıra gelişen olaylara bakalım.

### Ne iş yapar Euler Finance?
[Euler Finance](https://www.euler.finance/), bir kredi verme platformu. Bu alandaki diğer protokollerden farkı her tür kriptoparanın kredi olarak verimesini sağlayan yenilikçi ürünler sunması. (Hatırlayanlar olacaktır, DeFi'nin başlıca kredi verme platformları olarak [Aave'yi](/genel/2021/07/19/defi-de-kurumsallara-karsi-bos-degil.html) ve [MakerDAO'yu](/genel/2019/02/15/MakerDAO-kredi-kullaniminda-cigir-acar-mi.html) daha önce detaylıca incelemiştik)

En basitinden özetleyecek olursak, DeFi'de kredi alabilmek için, alacağınız krediden daha fazla teminatı protokol içine kilitlemeniz gerekiyor. Sonrasında aldığınız krediyi artık ihtiyaçlarınız için mi, yoksa spekülasyon için mi kullanırsınız, o size kalmış. Tek dikkat etmeniz gereken kural, teminatınızın aldığınız krediye oranının belli bir seviyenin altına düşmemesine dikkat etmek. Aksi takdirde sistem gözünüzün yaşına bakmaz, icra memuru da diyebileceğimiz bir akbaba (ingilizcesi 'liquidator') gelir teminatınızı güzel bir iskonto ile satın alır, borcunuzu öder ve aldığı iskontoyu da cebe atar. 

### Genel olarak nasıl bir risk var burada? 

Kredi alma, geri ödeme, likide olma gibi süreçlerin gerçekleşmesi ise, malumunuz akıllı kontrat dediğimiz küçük programlar aracılığıyla oluyor. Yukarıda anlattığımız her bir adım için bir akıllı kontratın çalışması gerekiyor ve en ciddi sorunlardan biri işte burada başlıyor. Akıllı kontrat içindeki birkaç adımın yanlış yazılması, hem kontratın zaafiyet vermesine yol açıyor, hem de bu durum onunla iletişime geçen diğer kontratları da etkiliyor. Bu da, DeFi'nin en büyük açıklarından biri olan 'kontrat riskini' doğuruyor.

Protokoller 'akıllı kontrat riskini' çözmek için bu kontratları genellikle dış denetimden geçiriyorlar. Ne var ki, kontratların değişik ihtiyaçlardan dolayı yenilendiği durumda, yeni güncellemeleri gerek maliyet gerekse denetçilerin iş yükünden dolayı ihmal edilebiliyor Ya da kimi zaman denetçiler bile yoğunluktan dolayı işlerini layıkıyla yerine getirmeyip kontrattaki hataları atlayabiliyorlar.  

### Olay nasıl patlamış?

İşte Euler Finance de, bu şekilde bir kombo problemler zinciri yaşamış. Problemin teknik detayına girmeden özeti şu şekilde: Euler üzerinde bundan sekiz ay önce Temmuz 2022'de uygulamaya aldığı bir [güncelleme](https://forum.euler.finance/t/eip-14-contract-upgrades/305) sırasında yapılan bir değişiklik akıllı kontratta bir açık yaratıyor. Denetimi yapan firma açığı atlıyor ve işin ilginç tarafı tam sekiz ay boyunca kimse bunu farketmiyor. 

Nihayet, Mart ayı başında bir hacker bu açığı buluyor ve sonuç: Sistemden tam 200 milyon ABD Doları kriptoparayı hesabına çekiyor! (Açık ve çalınan para ile ilgili teknik detayı en sonraki dipnotta bulabilirsiniz[^3]). 

### Sonrasında yaşananlar neler?
Tabii bu olay tüm DeFi dünyasında büyük bir şok etkisi yarattı. Hack, [DeFi'de yaşanan en büyük saldırılar tablosunda](https://rekt.news/leaderboard/) kendisine altıncı sıradan yer buldu. Euler'in tokeni [EUL](https://www.coingecko.com/en/coins/euler) yaklaşık %70 oranında değer kaybetti. 

Euler Finance, yaptığı yenilikler ile bilinen ve ekosistemde sevilen bir topluluk. Protokol aynı zamanda pek çok diğer protokolun parasını emanet ettiği bir yer. Yani olay sadece Euler, ve bireysel yatırımcılarını değil, ekosistemdeki diğer büyük oyuncuları da etkiler hale geldi. Buradan sonrası ise polisiye hikayenin başladığı yer aslında. 

Euler Finance ekibi, öncelikle hacker ile temasa geçtiler. Nasıl? Hımmm, düşünelim bakalım: Elimizde ne var? Açığı bulup parayı çeken [adres](https://etherscan.io/address/0xee009faf00cf54c1b4387829af7a8dc5f0c8c8c5). Başka ne var? Her tür işlemi gösteren, şeffaf bir blokzincir. Evet, bildiniz. [Ekip](https://etherscan.io/address/0xb66cd966670d962c227b3eaba30a872dbfb995db), 13 Mart'ta hacker'a blokzincir üzerinden aşağıdaki [mesajı](https://etherscan.io/tx/0x539c6fff0fce70e02dddd80a5534acf3df57deafbdc40f41abb20aa8f94a6d0d) [^1] gönderdi. 

| ![hacker_mesaj](/assets/euler-finance-to-hacker-280313_800.jpg)|
|:--:| 
| *Euler'in hackera yazdığı mesaj. En alttaki birinci dipnottaki adımları takip ederek mesajın orjinalini görebilirsiniz. Kaynak:[Etherscan](https://etherscan.io/tx/0x539c6fff0fce70e02dddd80a5534acf3df57deafbdc40f41abb20aa8f94a6d0d))*|

Çevirisi özetle: 'Hadi gel anlaşalım' olan bu mesaj sonrası hacker ile karşılıklı mesajlaşmalar başladı. Hacker ilk olarak 'eğer herhangi bir kanuni yaptırım uygulanmaz ise paranın %90'ını geri vereceğini ve %10'unu ödül olarak tutacağını' [yazdı](https://etherscan.io/tx/0xa7156a9e9031e4afecf8d48f8c54f1e4c9bdba5a4b91fe3087602351343ad888). Ne de olsa bu tip hack olaylarında, iyi niyetli hackerlara kanuni işlem yapılmamasının karşılığı olarak paranın %10'unu ödül (ingilizcesi 'bounty') olarak vermek adeta bir standart haline geldi. Bu mesaj paranın geri alınabileceği ile ilgili ümitleri yeşertse de Hacker'in 16 Mart tarihinde bir dizi [işlem](https://etherscan.io/tx/0xd7cc4f5305441c1ae773982d4813e48008b9fe2da10b86c6d96901e578ffffd6) ile Tornado Cash'e 1000 ETH göndermesi, paranın geri gelmeyeceğinin göstergesi olarak algılandığı için moraller bozuldu.  Bu arada hacker'in aynı gün kendisine [mesaj atıp](https://etherscan.io/tx/0xbe21a9719a4f89f7dc98419f60b247d69780b569cd8869c0031aae000f98cf17) 'tüm biriktirdiğim para 78 ETH idi, hayatım mahvoldu' yazan birine 100 ETH [göndermesi](https://etherscan.io/tx/0xcc8edbe70d22176e90027bb07047b5cc7541b169ef9ef71ae6d6793f344b8bc5) bir anda insanların hackerı mesaj yağmuruna tutmasına neden oldu. Bir gün sonra hacker hesabından geçtiğimiz yılın en büyük DeFi hack'i olan Axie Infinity'e ait Ronin köprü kazasının faili Kuzey Koreli grubun 'mimli' hesabına 100 ETH [aktarılması](https://etherscan.io/tx/0x202a67d3a1d52e4dd5e1eebe49da511164b6e4a1ebe717dcf4674dd83a2bd457) ise kafaları iyice karıştırdı. Acaba hacker Kuzey Koreli korsan grubu mu idi?

Buradan sonrası karşılıklı mesajlaşmalar ve 'parayı verecek, vermeyecek' git gelleri içinde geçti. 25 Mart'ta Euler ekibine geri gönderilen  57 bin ETH (87 milyon ABD Doları) ile süreç bir anda çözülme yoluna girdi ve paralar yavaş yavaş gelmeye başladı. Nihayet 4 Nisan günü Euler ekibi yayınladığı bir [blog yazısı](https://forum.euler.finance/t/special-announcement/900) ile geri alınabilecek bütün paranın alındığını söylediler. Hacker ilk başta kendisine söz  olarak verilmiş çalınan miktarın %90'ı olan 20 milyon ABD Doları'nı da almadı (Bunun yerine elinde Tornado Cash'e gönderilen 1000 ETH kaldı - bir de Kuzey Koreli ekibe gönderilen 100 ETH var).

### Çıkarılacak dersler
İşin magazinsel yanına baktığınızda hackerin profesyonel biri olduğunu söylemek oldukça zor. Muhtemelen Euler Discord kanalında insanların 'mahvolduk' mesajlarını da takip eden hackerın tanımadığı kişiye 100 ETH göndermesi (kişinin zararı 78 ETH iken) ve özellikle çözülme sürecinde son gönderdiği [mesaj](https://etherscan.io/tx/0xedd8102ca037abaeb75ce6a1afe951d2953258392d891ff23510276993a5437c) (ismini verip 'ben Jacob, büyük hata yaptım, insanların parası ve hayatlarını mahvettim, beni affedin' yazması) bu tesbiti doğrular nitelikte. Tabii bütün bunların asıl nedeninin suyu bulandırmak olduğu, 'at izini, it izine karıştırmak' için yapıldığı ve Kuzey Koreli hackerlara para gönderilmesinin arkasında da aynı nedenin yattığını söyleyenler de var. 

Ne olursa olsun, özellikle DeFi'nin şeffaf dünyasında hackerların işlerinin giderek zorlaştığını söylemek mümkün. Özellikle zincir-üstü analizler sayesinde izinizi bıraktığınız anda enselenmeniz an meselesi. Burada da hacker muhtemelen yakalanacağını anladığı için %10 ödülü bile almadan elindeki 1000 ETH ile yetinmek zorunda kaldı. Görünen o ki, hack etmek kolay ama sonra çalınan parayı (hele ki bu kadar büyük bir miktar ise) saklamak daha zor. 'Minareyi çalan, kılıfı hazırlar' sözü DeFi'de çok geçerli değil gibi görünüyor. Böyle durumlarda hackerlar için en iyi öneri 'hata mı buldun, al %10 ödülünü, kenara çekil' demek belki de :) 

Burada en büyük alkışı gerek zincir-üstü analizler gerekse zincir-dışı aksiyonlar[^2] ile hackeri köşeye sıkıştıran kripto camiası hak ediyor. Ekosistem, bu olayda kötü aktörlere karşı birleşip onları sistem dışına itebildiğini gayet güzel göstermiş durumda. Aynı övgüleri Euler Finance ekibi için söylemek zor. Ekip, kodlarındaki hata ve süreç içinde topluluk ile yeterli iletişim kuramadığı için [ciddi eleştiriler](https://uniqpath.com/euler/?v=1) alıyor. Topluluk onlardan hem süreç ile ilgili öz eleştiri hem de kaybolan 1000 ETH'nin nasıl yerine konulacağı konusunda bir açıklama bekliyor. 

### Sonuç 

Her ne kadar büyüklük olarak 2021 yıllarındaki eski günlerini arıyor olsa da, çıkan yeni ürünler ile hızlı bir şekilde gelişmeye devam eden DeFi ekosistemi, hızın getirdiği yol kazalarını yaşamaya devam ediyor. Bu kazalardaki kayıplar, topluluğun kenetlenmesi sayesinde son dönemde daha az hissedilmekte. Bu böyle devam edecek mi? Tahmin etmek zor. Zira, her hacker Euler olayında olduğu gibi amatör olmayabilir. Üstelik kaygı verici olan, Euler'deki açığın sekiz ay boyunca fark edilmemiş olması. DeFi protokollerinin riski minimuma indirmesi için yemeleri gereken 'kırk fırın ekmeğin' büyük bir kısmı hâlâ önlerinde duruyor gibi görünüyor.

Dipnotlar: 
[^1]: Mesajı siz de görebilirsiniz. [Şu](https://etherscan.io/tx/0x539c6fff0fce70e02dddd80a5534acf3df57deafbdc40f41abb20aa8f94a6d0d) işlem adresine girin. Aşağı doğru ilerleyin 'gaz fiyatının' ('gas price') hemen altında 'daha fazla detay' ('more details') diye bir yer göreceksiniz. '+' işaretine basarak orayı açın. 'Veri girişi'('input data') kısmına gelin. Karmakarışık rakamlar yazdığını göreceksiniz. Alttaki 'datayı izleme şekli' ('View input as') menüsünden 'UTF-8'i seçin (not: yazıyı görebilmek için etherscan'e ücretsiz kayıt olmanız gerekiyor). 

[^2]: Örneğin, a16z'den geçtiğimiz yıl ayrılıp kendi fonu olan Haun Ventures'ı kuran Kathryn Haun'un eski bir anayasa mahkemesi çalışanı olduğunun ve ekibinin hackerı enselemek konusunda ciddi bir çaba gösterdiğini belirtelim. 

[^3]: Euler denetçilerinden birinin yazdığı [rapora](https://medium.com/@omniscia.io/euler-finance-incident-post-mortem-1ce077c28454) göre detaylar şu şekilde: Öncelikle, sorunun temeli, Euler'in hesabına para gönderildiğinde, sistemin bunu gönderenin mali durumuna bakmadan kabul etmesi. Ne gibi bir problem yaratıyor bu? Gönderen para gönderdiği için teminatı kredinin altında kalırsa likide olmak durumunda kalıyor. Akbabalar gönderenin teminatını likide ederken %20 iskonto alıyorlar. İşte saldırgan kredi aldığı hesaptan büyük miktarlarda parayı teminat gösterip, hesabı iflas durumuna sürüklüyor. Diğer yandan akbaba gibi davranıp teminatı ucuzdan çözerek parayı cebe atıyor. Burada kaybeden kim? Protokol. Adımlar şu şekilde  
i) Saldırgan, iki farklı hesap açıyor. Birine kredi alan, öbürüne akbaba hesabı diyelim. 
ii) Sonra gidip aave'den 30 milyon DAI flash loan alıyor ve bu parayı krediyi alacak hesaba yatırıyor. 
iii) Kredi alan hesap 20 milyon dolar DAI'yi mevduat olarak yatırıyor. 
iv) Bu sayede 195 milyon eDAI (Euler'in DAI karşılığı parası) yaratıp kendisini 200 milyon DAI borçlandırıyor (20 milyon mevduatı da teminat olarak gösteriyor). 
v) Sonra elinde kalan 10 milyon DAI ile 200 milyon DAI'lik borcunu 190 milyona indiriyor.
vi) Ardınan yukarıdaki işlemleri bir kez daha tekrarlıyor
vii) En son kredi veren hesabından Euler rezerv hesabına 100 milyon DAI bağış yapıyor
viii) Sonuç olarak kredi hesabının elinde 310 milyon eDAI ve 390 milyon borç ile baş başa kalıyor - yani açığa düşüyor
ix) Burada akbaba hesap devreye giriyor. Kredi alan hesabın 310 milyon eDAI'sinin %25 oranında iskonto (ve bir miktar masraf ile birlikte) 259 milyon DAI borcunu üstüne alıyor
x) Akbaba hesap, 259 milyon DAI borcu elindeki eDAI'ler ile ödüyor. Geriye kalan paranın tamamını çekebilir ama havuzda 38.9 milyon DAI var. Bu DAI'nin tamamını çekiyor ve gidip aave'ye olan 30 milyon DAI borcunu ödüyor. Böylece aradaki fark (38.9-30) olan 8.9 milyon DAI yanına kar kalıyor. 
xii) Saldırgan aynı işlemi diğer kredi havuzları için de uyguluyor. Böylece 141 milyon ABD Doları wstETH, 34 milyon ABD Doları USDC, 26 milyon ABD Doları wbtc, 15 milyon ABD Doları wETH, ve 7 milyon ABD Doları stETH olmak üzere bugünün parasıyla toplam 232 milyon ABD Dolarını 'iç' ediyor. 

