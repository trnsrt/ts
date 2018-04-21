---
layout: post
title:  "Şifreleme mi? Çok karışık değil mi?"
date:   2018-04-04 14:25:15 +0300
categories: Genel
---

Şifreleme deyince aklımıza çok karışık anlaşılmaz konular geliyor değil mi? Normal. Aslında o kadar da zor değil ama anlayabilmek için biraz çaba sarfetmek lazım - her türlü konuda olduğu gibi. Peki neden önemli bu şifreleme?  Çünkü şifreleme bize pekçok kişiye dağılan bilginin doğru ve tam olduğunu anlamamızı sağlıyor. Peki ama ne demek şimdi bu?

Efendim, daha önce de belirtmiştik. Modern şifreleme teknolojisi aslında 1970'lerden beri var. Bunun yanında 1990'larda internet hayatımıza girdi ve bilginin yaygınlaşmasını ve kolayca iletilmesini sağladı. Tabii bilgiyi yayarsınız bir sorun yok - paylaştıkça çoğalır. Ancak herhangi bir varlığı internet üzerinden transfer etmeye kalktığınızda önümüze sorunlar çıkıyor. 

İsterseniz internet üzerinden transfer edilebilecek pekçok nesneden en aşina olduğumuz para üzerinden bir örnek verelim. 

### Para, para, para - varlığı bir dert... 

Para ilk zamanlarda fiziki olarak **kağıt** halinde bulunurken, 60-70'lerden sonra bilgisayarlar iletişin başlayınca kurumlar arasında kullanılan **elektronik para**'ya 90'lardan sonra internet çıkınca da kişiler arasında iletişim ile birlikte **dijital para**'ya evrildi. 

Ancak, bu paranın alışverişe layık olabilme niteliğini koruyabilmesi için hep bir merkezi otoriteye (merkez bankaları ya da bankalar) ihtiyaç duyuldu. İnsanların güven duyacağı birilerinin kontrol etmesi lazım bunu - normal. Öbür türlü dijital bir nesneyi sonsuz olarak üretebilirsiniz, gerçekten size me ait nereden bileceksiniz, yabancıların sözlerine nasıl güveneceksiniz. Olmaz. 

İşte tam bu sırada 90'ların sonunda Satoshi Nakamoto dediğimiz kişi(ler) bu iki konuyu yani şifreleme ile para transferi teknolojisini birleştirdi ve tek bir otoriteye bağlı kalmaksızın o güvenin yerini makinelerin aldığı bir yapı oluşturarak adeta bir devrim yarattı. Zira bu aradaki banka gibi kurumlara olan ihtiyaç neredeyse sıfıra indi - çünkü artık bu sisteme her giren makine bir banka!

Tekrar edelim para örneğini hep konuşulduğu için verdik. Konu sadece para ile sınırlı değil. Bu her tür dijital varlık olabilir örneğin noterlerde saklanan bilgi, bir dijital sanat eseri gibi. Bana ait olan, başkasının üzerinde hak iddia edemeyeceği, dijital olarak saklanabilen, istediğimde başka birine dijital olarak kısa sürede transfer edebileceğim her tür nesne. 

Şifreleme Blockchain'in temelini oluşturuyor, çünkü Blockchain dağınık bir sistemde çalışıyor, yani bilgi binlerce farklı, birbiri ile ilintili ama birbirini tanımayan makinede üzerinde bulunuyor. Dağınık sistemlerin kontrolü olmadığı için bilginin düzgün ve değiştirilmemiş olması son derece hayati - bunu sağlayan da şifreleme sistemi. Yani şifreleme sayesinde herhangi bir bilgi Blockchain üzerindeki her parça üzerinde hem aynı şekilde tutarlı hem de gizli olarak tutulabiliyor. Şifreleme teknik ve karmaşık görünse de onu daha iyi anlamak bize günlük hayatımızda Blockchain teknolojisini nasıl daha verimli olarak kullanırız konusunda farklı ipuçları da verebilir.  


### İki ana fark

Konuya öncelikle iki farklı noktadan bakmak gerekiyor. 

1. Birincisi, benim (ve diğer herkesin) verdiği bilgilerin gerçekten bana ait olduğunun (orjinal/otantik olduğunun) teyit edilmesi. Ama bir taraftan da bu bilgilerin bir kısmının gizli tutulması (benim hakkımdaki her bilginin herkes tarafından bilinmesini istemem). İşte bu **şifreleme** (encryption/decryption) sayesinde başarılıyor. 
2. İkincisi ise, bütün bu değişik kişllerden gelen bilgilerin kayıt edildikten sonra bir daha değiştirilemez biçimde kaydedilmesi ve üstü üste (ya da arka arkaya) dizilmesi. Yani herkeste aynı bilgilerin olması. Herkeste aynı bilgi olursa kimse "eyvah kandırılıyor muyum?" kaygısı yaşamaz, gece evinde rahat uyur. İşte bu da **öğütme** (hashing) sayesinde başarılıyor. 

Şimdi dilerseniz gelin önce bir şifreleyelim ve nasıl olduğuna bakalım, sonra da bunu öğütürüz.. 


### Şifrelemeli mi, şifrelememeli mi?

En basitinden başlayalım. Şifreleme bir nevi kilitleme demek. Diyelim bir mesajınız var. Bu mesajınız "Merhaba" olsun. Şifreleme dediğimiz, bir anahtar düşünün, bu anahtar sizin mesajınızı alıyor ve şifreleyip yerine rastgele sayı ve harflerden oluşan bir sözcük dizisi veriyor. 

&nbsp;

| ![sifreleme-mekanizmasi-lock.png](/assets/sifreleme-mekanizmasi-lock.png) | 
|:--:| 
| *Şifreleme Mekanizması* |

&nbsp;


Dolaysıyla sizin yazdığınız bu mesajı anahtarı verdiğiniz herkes açıp görebiliyor. Sadece anahtarı olanlar. Buraya kadar güzel. Bu anahtarı bir kişiye verirsem bir sorun yok. Bir taraf mesaj yazar, anahtar ile şifreler, diğeri aynı anahtar ile açar mesajı okur, sonra yeni bir mesaj yazar ve aynı anahtar ile şifreler ve bu böyle sürüp gider.  Ancak pratiğe geldiğinde soru(n)lar ortaya çıkmaya başlıyor. 

Ya karşı taraf bu anahtarı başka birine daha verirse? O zaman ne olacak? Benim yazdığım mesajı birden fazla insan okuyabilir ve haberim olmaz. Aynı zamanda, o anahtarı verdiği kişi bir mesaj yazarsa? Karşı tarafın bu mesajı yazdığını nereden bileceğim? Dolayısıyla, anahtarın kopyalanabildiği durumlarda sıkıntı var, mesajı kimin yazdığını anlamak zor. 

İşte bu "mesajı kim yazdı, kimler okudu sorununu çözmek için" 1976 yılında yeni bir şifreleme yöntemi ortaya atılmış. "Özel anahtar" ve " Genel Anahtar" kavramları çıkmış.  


### "Özel Anahtar" ve "Genel Anahtar"

Şifreleme yapabilmek için gerekli olan önemli bir parçaya geldi sıra: "Özel Anahtar" ve "Genel Anahtar". Sizin, benim ve herkesin yaratabileceği her bireyin kendine ait bir "Özel Anahtar" bir de "Genel Anahtar" var. Bunu bir nevi Şifreleme Mekanizmasını çalıştırmak için bana gerekli olan anahtarlar olarak da hayal edebilirsiniz. 

Özel Anahtar ve Genel Anahtarı bana ait birbirlerinin aynı olan iki anahtar gibi düşünebiliriz. Aradaki tek fark, Özel Anahtarın  sadece benim bildiğim (hiç kimse ile paylaşmadığım) bir anahtar. Genel Anahtar ise yine bana ait, ama herkes ile paylaştığım tüm dünyanın görebileceği bir anahtar olması. İlişkileri ise şu: Bemim Özel Anahtarım ile kapadığım kapıyı (şifrelediğim mesajı) Genel Anahtarı bilen herkes açabiliyor (şifreyi açıp mesajı görebiliyor).   

Yukarıda dedik Şifreleme Mekanizması'nın sonucu bilirseniz girdiyi bulamıyorsunuz. Peki

Dilerseniz bir örnek ile anlatalım: Tüm dünya ile paylaşmak istediğim bir mesaj var. Örneğin "Yarın New York'a gideceğim!". İki önemli ihtiyacım var: 1. Bu bilginin benden geldiğinin bilinmesi (otantik olması) 2. Mesajın içeriğinin herkese doğru ulaşması (yolda bir başkası tarafından değiştirilememesi). 

Eğer ben  "Yarın New York'a gideceğim" yazısını kendi Özel Anahtarım ile karıştırıp dünyaya yayınlarsam (yani şifrelersem), çıkan sonuca bakan biri, benim Genel Anahtarımı alıp bu ortaya çıkan şifreli sonucu ile birleştirirse (yani şifreyi çözerse) sonuçta benim tarafımdan gelen, benim imzaladığım mesajı görür.  


&nbsp;

| ![ozel-genel-anahtar-vertical.png](/assets/ozel-genel-anahtar-vertical.png) | 
|:--:| 


&nbsp;

Peki bunu tüm dünyaya değil de sadece arkadaşıma göndermek istersem? O zaman? Burada birkaç koşulun doğru olduğuna emin olmamız gerekiyor
- Ben bilgiyi yazarken bu bilgiyi sadece sizin okuyabileceğine emin olmam gerekiyor
- Siz, bu bilginin benden geldiğine emin olmak istiyorsunuz
- Aynı zamanda hem ben hem siz bu bilginin benden size gelirken yolda değiştirilmemiş olduğuna emin olmamız gerekiyor

&nbsp;

| ![ozel-genel-anahtar-iki-kisi-vertical.png](/assets/ozel-genel-anahtar-iki-kisi-vertical.png) | 
|:--:| 


&nbsp;


Bunu bir örnek üzerinden anlatmaya çalışalım: 

Diyelim yukarıdaki gibi bir bilgiyi e-posta olarak gönderiyorsunuz. İlk olarak ne yapıyorum? Kendi e-postama giriyor ve sizin email'inizi yazıyorum, sonra mesaji yazıyorum ve gönder tuşuna basıyorum. Aynı olayı yukarıdaki gibi şifreleme işlemine tabi tutalım. Yaptığım işler şu şekilde: 

1. Mesajı yazıyorum. Şimdi bu mesajı bana ait sadece benim bildiğim "Özel Anahtar" ile birleştiriyorum. Ortaya bir sonuç çıkıyor. 
2. Bu sonuç Benzer şekilde burada da, "Genel Anahtar" benim email adresim, "Özel Anahtar" da bu mesajı yazanın ben olduğunu gösteren bana ait "Dijital İmza".  













Peki çok güzel yukarıda yazılanlar sayesinde, bu mesajın benim tarafımdan gönderildiğini tüm dünya görmüş oldu. Harika. Ya yarın öbür gün ben bu mesajı değiştirmek istersem? Kusura bakmayın mümkün değil, çünkü mesajınız alındı, güzel bir şekilde öğütüldü ve tüm sistemdeki makineler üzerinde aynı şekilde tutulmaya başladı. Nasıl mı? Anlatalım: 


### Değirmen gibi öğütelim.. 

Kapalı bir kutu (belki de bir kağıt öğütücü) düşünün. Bir taraftan anlamlı bir sözcük veriyorsunuz, diğer taraftan rakam ve sayılardan oluşan anlamsız rastgele bir sayı/harf dizisi veriyor.  İşte buna öğütme deniyor. 

Bir örnek yapalım dilerseniz: 

&nbsp;

| ![sifreleme-mekanizmasi.png](/assets/sifreleme-mekanizmasi.png) | 
|:--:| 
| *Şifreleme Mekanizması* |

&nbsp;

Siz de [deneyebilirsiniz bu link üzerinden](http://www.xorbin.com/tools/sha256-hash-calculator) - aynı sonucu bulacaksınız (bu sonuca teknik olarak **hash** deniyor). 

| Girdi  | Sonuç  |
|---|---|
| *Merhaba*  | *7fdc9f4717c5fe66df286c700fab969b4d6209d03aa84624c5f8f58c17c9c058*  |



İşte işin özü bu. Değişik şifreleme mekanizmalarından en popüler olan SHA-256 şifreleme böyle çalışıyor. Girin herhangi bir SHA-256 [şifreleme sitesine](http://www.xorbin.com/tools/sha256-hash-calculator) "Merhaba" yazın, yukarıdaki sonucun aynısını verecek size: 64 karakterli bir dizi. 

-- 

Peki buraya uzunca bir paragraf koymak istesek ne olur? Mesela, 

| Girdi  | Şifreli Sonuç  |
|---|---|
| *Ey Türk Gençliği! Birinci vazifen, Türk istiklâlini, Türk Cumhuriyetini, ilelebet, muhafaza ve müdafaa etmektir. Mevcudiyetinin ve istikbalinin yegâne temeli budur. Bu temel, senin, en kıymetli hazinendir. İstikbalde dahi, seni bu hazineden mahrum etmek isteyecek, dahilî ve haricî bedhahların olacaktır. Bir gün, İstiklâl ve Cumhuriyeti müdafaa mecburiyetine düşersen, vazifeye atılmak için, içinde bulunacağın vaziyetin imkân ve şerâitini düşünmeyeceksin! Bu imkân ve şerâit, çok nâmüsait bir mahiyette tezahür edebilir. İstiklâl ve Cumhuriyetine kastedecek düşmanlar, bütün dünyada emsali görülmemiş bir galibiyetin mümessili olabilirler. Cebren ve hile ile aziz vatanın, bütün kaleleri zaptedilmiş, bütün tersanelerine girilmiş, bütün orduları dağıtılmış ve memleketin her köşesi bilfiil işgal edilmiş olabilir. Bütün bu şerâitten daha elîm ve daha vahim olmak üzere, memleketin dahilinde, iktidara sahip olanlar gaflet ve dalâlet ve hattâ hıyanet içinde bulunabilirler. Hattâ bu iktidar sahipleri şahsî menfaatlerini, müstevlilerin siyasi emelleriyle tevhit edebilirler. Millet, fakr ü zaruret içinde harap ve bîtap düşmüş olabilir.  Ey Türk istikbalinin evlâdı! İşte, bu ahval ve şerâit içinde dahi, vazifen; Türk İstiklâl ve Cumhuriyetini kurtarmaktır! Muhtaç olduğun kudret, damarlarındaki asil kanda mevcuttur!* | *c369b0a6ca659b4d370ff8b0a54ad582d49d7cb1d42125059658ed8d94996276*  |

Viola! Bambaşka bir dizi ama yine 64 karakterli. Buraya isterseniz girdi olarak koca bir ansiklopedi koyun, sonuç yine 64 karakterli bir dizi olacak. 

--

Şimdi ilk örneğimize geri dönelim: Merhaba kelimesinin sonuna bir "!" işareti ekleyelim, bakalım ne olacak?

| Girdi  | Şifreli Sonuç  |
|---|---|
| *Merhaba!*  | *b1726b923349fd632fa7ce8b62a06c5a3f785be1db4f6a831eef58d70c7a45cc*  |

Gördünüz mü? Herşey değişti. Bir harf ekledik ama ilk kelimeden tamamen farklı bir sonuç çıktı ortaya. Ama dikkat edin 64 karakterli yine. 

Bu önemli, o yüzden biraz daha açalım. Aynı girdiler hep aynı sonucu veriyor. Ama girdi de bir harf bile değiştirin, çıkan sonuç bambaşka oluyor.  Bu ne işe yarıyor? Bu girilen bilginin orjinal ya da otantik (değiştirilmemiş) olup olmadığını anlamamıza yarıyor. Eğer elinizde bir bilgi ve bu bilgi sonucu ortaya çıkan şifreli bir sonuç da varsa, bu girdi hakikaten bu sonucu mu veriyor test edebiliyorsunuz. Girin ilk bilgiyi şifrelemeye aynı sonucu bulacaksınız. 

Bu arada şunu da belirtmekte fayda var. Bu şifreleme mekanizmalarının özelliği şu:; sonucu biliyor olmanız girdiyi de bildiğiniz anlamına gelmiyor. Yani, girdiyi biliyorsanız sonucu bulabiliyorsunuz ama sonuçtan geriye bilgiye gidemiyorsunuz

--


Bilginin tutarlı olduğunu bilmek ne işimize yarıyor? Yukarıda yazdığımız gibi bilgiyi dağıtıp tek bir noktada tutmadığınızda dağınık duran herkeste aynı bilginin olması, bilginin doğruluğu kişilerin bu bilgiye olan güvenini sağlayan en önemli etken. Öbür türlü kırk kişide kırk bilgi olursa ona dedikodu denir, kimse de beş kuruş değer vermez. 




### Peki Bitcoin şifrelemesi nasıl çalışıyor?

Hatırlar mısınız, önceki bir yazımızda şunu demiştik: "Blockchain sisteminde yükü çeken makinelerin bu yaptıkları işlemleri kayıt etme, daha sonra da teyid etme işlemi sonucu aldıkları ödüle (ya da lotarya) Bitcoin deniyor. Neden lotarya deniyor? Zira, bu on dakikada bir yapılan teyit işlemi aslında çok zor bir bulmaca. Bir nevi Sudoku oyunu gibi düşünün"

Şimdi dilerseniz bu bulmaca konusunu biraz daha açalım. Ortada tabii ki bir bulmaca yok ama bir şifreleme işlemi var. Aynı yukarıda olduğu gibi "input" ve "output" kısmı olan bir SHA şifrelemesi. 

Input'un iki parçası var 
- Belli bir süre içinde gerçekleşen tüm işlemlerin bir dökümü 
- Bir de bir sayı

Output ise yukarıdaki gibi 64 karakterli bir şifre. 

Sistem söyle çalışıyor. 
1. Her 10 dakikada bir Bitcoin ile yapılan bütün işlemler toplanıyor biraraya ve makinelere gönderiliyor
2. Sonra sistem bütün makinelere şunu söylüyor: *"Ey makineler, işlemlerin toplam dökümünü aldınız, şimdi bu işlem dökümünü alın yanına öyle bir sayı ekleyin ki, şifrelemeye koyduğunuzda çıkan output dört tane sıfır ile başlasın"*
3. Makineler bu çıktıyı alıyor ve sırayla rakamları denemeye başlıyorlar. Önce 1 ekliyor, çıkan sonuca bakıyor, yok olmadı "370ff8b0.." ile başlayan bir output verdi. Sonra 2 ekliyor, yine bakıyor bu sefer "58ed8d94.." diye başlayan bir sayı verdi.. Böyle böyle sırayla tüm sayılar deneniyor. Ta ki bir sayı (diyelim "25264") bize "0000..." ile başlayan bir sonuç verene kadar!
4. "0000.." ile başlayan sonucu ilk bulan makine "Buldum!" diyerek bu sonuca ulaştıran sayıyı "25264" diğer makinelere haber veriyor. 
5. Sonucu gören makineler, işlem dökümünü 25264 sayısı ile birlikte şifreye sokuyorlar, bakıyorlar hakikaten çıkan sonuç "0000.." ile başlıyor, "tamam" diyorlar, "sonuç doğru" ve bir sonraki 10 dakika için yapılan işlemlere geçiyorlar. 
6. 25264 rakamını bulan makine işte bu ödülü (şu anda 12.5 Bitcoin yani 100,000 ABD Doları civari bir rakam) kazanıyor!

### Bu kadar mı?

Evet, aslında işin özü bu kadar basit. Zaten diyoruz ya, Bitcoin üzerindeki bütün işlemler görülebiliyor diye. Yapılan bütün işlemler hangi partiden geliyor hangi partiye gidiyor, ne kadar işlem yapılıyor hepsi görülüyor. Ancak görülmeyen ne? Hangi partiden gelip hangi partiden gittiği de sistem üzerinde şifreli olarak görülüyor. Mesela örnek bir işlem bakalım: 

