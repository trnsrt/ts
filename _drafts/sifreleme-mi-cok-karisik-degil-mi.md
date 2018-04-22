---
layout: post
title:  "Şifreleme mi? Çok karışık değil mi?"
date:   2018-04-04 14:25:15 +0300
categories: Genel
---

Şifreleme deyince aklımıza çok karışık anlaşılmaz konular geliyor değil mi? Normal. Aslında o kadar da zor değil ama anlayabilmek için biraz çaba sarfetmek lazım - her türlü konuda olduğu gibi. Peki neden önemli bu şifreleme?  Çünkü şifreleme bize pekçok kişiye dağılan bilginin doğru ve tam olduğunu anlamamızı sağlıyor. Peki ama ne demek şimdi bu?

Efendim, daha önce de belirtmiştik. 1990'larda internet hayatımıza girdi ve her tür dijital bilgi ve verinin yaygınlaşmasını ve bir taraftan diğerine kolayca iletilmesini sağladı. Bu harika bir olay, çünkü masrafsız bir şekilde bilgiyi kopyalayabiliyor ve dağıtabiliyorsunuz. Eğitim, araştırma ve gelişme için bulunmaz nimet. Ancak herhangi bir dijital varlığı internet üzerinden transfer etmeye kalktığınızda önümüze sorunlar çıkıyor. Zira olur olmaz kopyalanmaması lazım, gerçek sahibinin kim olduğu biliniyor olmalı, o sahip gerçekten bu varlığı birine devretmek istiyor mu onu bilmeli gibi gibi.. 

İsterseniz internet üzerinden transfer edilebilecek pekçok dijital varlıktan en aşina olduğumuz para üzerinden bir örnek verelim. 

### Para, para, para - varlığı bir dert... 

Para ilk zamanlarda fiziki olarak **kağıt** halinde bulunurken, 60-70'lerden sonra bilgisayarlar ile iletişin başlayınca kurumlar arasında kullanılan **elektronik para**'ya, 90'lardan sonra internet yaygınlaşıp kişiler arasında iletişimin artması ile birlikte de **dijital para**'ya evrildi. 

Ancak, paranın alışverişe layık olabilme niteliğini koruyabilmesi için hep bir merkezi otoriteye (merkez bankaları ya da bankalar) ihtiyaç duyuldu. İnsanların güven duyacağı birilerinin kontrol etmesi lazım bunu - normal. Öbür türlü dijital bir nesneyi sonsuz olarak üretebilirsiniz, gerçekten size me ait nereden bileceksiniz, yabancıların sözlerine nasıl güveneceksiniz? Olmaz. 

İşte tam bu sırada 90'ların sonunda Satoshi Nakamoto dediğimiz kişi(ler) para transferi teknolojisini şifreleme ile birleştirdi ve tek bir otoriteye bağlı kalmaksızın, o otoritenin sağladığı güvenin yerini makinelerin aldığı bir yapı oluşturarak adeta bir devrim yarattı. Zira bu devrim ile işlemlerin arasında yer alan güven abidesi banka gibi kurumlara olan ihtiyaç neredeyse sıfıra indi - çünkü artık bu sistemdeki her makine kendi başına bir banka!

Tekrar edelim para örneğini hep konuşulduğu için verdik. Konu sadece para ile sınırlı değil. Bu her tür dijital varlık olabilir örneğin noterlerde saklanan bilgi, bir dijital sanat eseri gibi. Bana ait olan, başkasının üzerinde hak iddia edemeyeceği, dijital olarak saklanabilen, istediğimde başka birine dijital olarak kısa sürede transfer edebileceğim her tür varlık ya da nesne. 

Şifreleme Blockchain'in temelini oluşturuyor, çünkü Blockchain dağınık bir sistemde çalışıyor, yani bilgi binlerce farklı, birbiri ile ilintili ama birbirini tanımayan makine üzerinde bulunuyor. Dağınık sistemlerin kontrolü olmadığı için bilginin düzgün ve değiştirilmemiş olması son derece hayati - bunu sağlayan da şifreleme sistemi. Yani şifreleme sayesinde herhangi bir bilgi Blockchain üzerindeki her nokta üzerinde hem aynı şekilde tutarlı hem de gizli olarak tutulabiliyor. Şifreleme teknik ve karmaşık görünse de onu daha iyi anlamak bize günlük hayatımızda Blockchain teknolojisini nasıl daha verimli olarak kullanırız konusunda farklı ipuçları da verebilir.  


### Şifreleme ve öğütme - iki önemli özellik

Konuya öncelikle iki farklı noktadan bakmak gerekiyor. 

1. Birincisi, bana ait bir varlığı bir başkasına devredeceksem öncelikle bu varlığın bana ait olduğunun ve benim bu varlığı devretmek istediğimin, yani bu işlemi başlatan kişinin gerçekten ben olduğumun (orjinal/otantik olduğunun) teyit edilmesi. Öte yandan işlemde bana ait özel bilgilerin de gizliliğinin sağlanması. İşte bu **şifreleme** (encryption/decryption) sayesinde başarılıyor. 
2. İkincisi ise, varlığı transfer ettikten sonra bu bilgilerin düzgün, bir daha değiştirilemez biçimde kaydedilmesi. Yani herkeste aynı bilgilerin olması. Herkeste aynı bilgi olursa kimse "eyvah kandırılıyor muyum?" kaygısı yaşamaz, gece evinde rahat uyur. İşte bu da **öğütme** (hashing) sayesinde başarılıyor. 

Şimdi dilerseniz gelin önce bir şifreleyelim ve nasıl olduğuna bakalım, sonra da bunu öğütürüz.. 


### Şifrelemeli mi, şifrelememeli mi? Önce şifreleyelim.. 

En basitinden başlayalım. Şifreleme bir nevi kilitleme demek. Diyelim bir mesajınız var. Bu mesajınız "Nasılsın?" olsun. Şifreleme dediğimiz, bir anahtar ve kilit düşünün, bu anahtar sizin mesajınızı alıyor ve kilidin içine koyup kilitliyor. 

&nbsp;

| ![sifreleme-mekanizmasi-lock.png](/assets/sifreleme-mekanizmasi-lock.png) | 
|:--:| 
| *Şifreleme Mekanizması* |

&nbsp;


Dolayısıyla sizin yazdığınız bu mesajı sadece anahtarı verdiğiniz kişiler görebiliyor. Buraya kadar güzel. Bu anahtarı bir kişiye verirsem bir sorun yok. Bir taraf mesaj yazar, anahtar ile kilitler, diğeri anahtarın kopyası ile açar mesajı okur, sonra yeni bir mesaj yazar ve anahtarı ile şifreler ve bu böyle sürüp gider. Ancak işin pratiğe geldiğimizde soru(n)lar ortaya çıkmaya başlıyor. 

Ya karşı taraf bu anahtarı başka birine daha verirse? O zaman ne olacak? O anahtarı verdiği üçüncü kişi bir mesaj yazarsa? Karşı tarafın bu mesajı yazdığını nereden bileceğim? Anahtarın kopyalanabildiği durumlarda sıkıntı var, mesajı kimin yazdığını anlamak zor. 

İşte bu "mesajı kim yazdı, kimler okudu sorununu çözmek için" 1976 yılında yeni bir şifreleme yöntemi ortaya atılmış. "Özel anahtar" ve " Genel Anahtar" kavramları çıkmış.  


#### "Özel Anahtar" ve "Genel Anahtar"

Yine yukarıdaki anahtar-kilit örneğinden devam edelim. Demiştik ki iki ana problem var. Birincisi benim yazdığım mesajın içeriğini anahtarı olan (ya da anahtarı alan) herkesin görüyor olması, ikincisi de herkesin bu mesajı benim yazdığımdan (kilidi benim kilitlediğimden) emin olması.

Önce ikincincisinden başlayalım. Şöyle demiş bir akıllı bilim adamı. "Şu kilidin özelliğini bir parça değiştireyim - öyle bir hale getireyim ki, iki tane anahtarı olsun. Biri sadece kilidi kilitlemeye, öbürü de sadece açmaya yarasın. Kilidi açmaya yarayan anahtarı, tüm arkadaşlarıma vereyim. Ama kilitlemeye yarayan sadece bende olsun". İlginç bir mantık - içgüdüsel olarak düşünmeyeceğiniz bir seçenek. Neye yarıyor peki? Şuna: Benim anahtarım kilidi kilitleyen tek anahtar olunca isteyen herkes benim dağıttığım diğer anahtar ile bu mesajı benim yazdığımı ve kilitlediğimi anlayacak.  

İşte bu iki anahtardan bana ait olana "Özel Anahtar", herkese verdiğime de "Genel Anahtar" deniyor. 

Özel Anahtar ve Genel Anahtarı bana ait birbirlerinin aynı olan iki anahtar gibi düşünebiliriz. Aradaki tek fark, Özel Anahtarın  sadece benim bildiğim (hiç kimse ile paylaşmadığım) bir anahtar. Genel Anahtar ise yine bana ait, ama herkes ile paylaştığım tüm dünyanın görebileceği bir anahtar olması. İlişkileri ise şu: Bemim Özel Anahtarım ile kapadığım kapıyı (şifrelediğim mesajı) Genel Anahtarı bilen herkes açabiliyor (şifreyi açıp mesajı görebiliyor).   

İşte yukarıdaki ilk sorunu çözdük. Mesajın benden geldiğini herkes gördü. Şimdi ikinci soruna ve çözümü olan öğütme (hashing) kısmına geçelim. 


### Şimdi de değirmen gibi öğütelim.. 

Yukarıdaki örnekten devam edelim. Mesajı yazdım ve herkes de mesajın benden geldiğini gördü. İyi de yazının içeriğini tüm dünya görmüş oldu, ben içeriği bilinsin istemiyordum, şimdi ne olacak? İşte burada öğütme mekanizması ortaya giriyor ve sizin yazınızı okunamaz bir hale getiriyor. Güzel değil mi, hem sizden geldiği anlaşılıyor hem de içeriğini kimse okuyamıyor. 

Harika. Ama yarın öbür gün ben bu mesajı değiştirsem "Yok, yahu ben öyle dememiştim, böyle demiştim" desem? Kusura bakmayın mümkün değil, çünkü mesajınız alındı, güzel bir şekilde öğütüldü ve tüm sistemdeki makineler üzerinde aynı şekilde tutulmaya başladı. Nasıl mı? Anlatalım: 

Kapalı bir kutu (belki de bir kağıt öğütücü) düşünün. Bir taraftan anlamlı bir sözcük veriyorsunuz, diğer taraftan rakam ve sayılardan oluşan anlamsız rastgele bir sayı/harf dizisi veriyor.  İşte buna öğütme deniyor. 

Bir örnek yapalım dilerseniz: 

&nbsp;

| ![sifreleme-mekanizmasi.png](/assets/sifreleme-mekanizmasi.png) | 
|:--:| 
| *Şifreleme Mekanizması* |

&nbsp;

Siz de [deneyebilirsiniz bu link üzerinden](http://www.xorbin.com/tools/sha256-hash-calculator) - aynı sonucu bulacaksınız (bu sonuca teknik olarak **hash** deniyor). 

| Girdi  | Şifreli Sonuç  |
|---|---|
| *Merhaba*  | *7fdc9f4717c5fe66df286c700fab969b4d6209d03aa84624c5f8f58c17c9c058*  |



İşte işin özü bu. Değişik öğütme mekanizmalarından en popüler olan SHA-256 böyle çalışıyor. Girin herhangi bir SHA-256 [şifreleme sitesine](http://www.xorbin.com/tools/sha256-hash-calculator) "Merhaba" yazın, yukarıdaki sonucun aynısını verecek size: 64 karakterli bir dizi. 

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

Yukarıdaki "Merhaba" da çıkan sonuç ile karşılaştırın bakalım. Tamamıyla değişti!. Bir harf ekledik ama ilk kelimeden tamamen farklı bir sonuç çıktı ortaya. Ama dikkat edin 64 karakterli yine. 

Bu önemli, o yüzden biraz daha açalım. Aynı girdiler hep aynı sonucu veriyor. Ama girdi de bir harf bile değiştirin, çıkan sonuç bambaşka oluyor.  Bu ne işe yarıyor? Bu girilen bilginin orjinal ya da otantik (değiştirilmemiş) olup olmadığını anlamamıza yarıyor. Eğer elinizde bir bilgi ve bu bilgi sonucu ortaya çıkan şifreli bir sonuç da varsa, bu girdi hakikaten bu sonucu mu veriyor test edebiliyorsunuz. Girin ilk bilgiyi şifrelemeye aynı sonucu bulacaksınız. 

Bu arada şunu da belirtmekte fayda var. Bu şifreleme mekanizmalarının özelliği şu: sonucu biliyor olmanız girdiyi de bildiğiniz anlamına gelmiyor. Yani, girdiyi biliyorsanız sonucu bulabiliyorsunuz ama sonuçtan geriye bilgiye gidemiyorsunuz. Yani,  öğütücüden geçmiş kağıtlara (ya da una, artık ne geçiriyorsunuz) bakarak kağıtta ne yazıyordu okuyamıyorsunuz. Ancak kağıdın orjinali varsa elinizde onu öğütücüden geçirip aynı şekilde önceki gibi bir bulamaç elde edebiliyorsunuz.

--


Bilginin tutarlı olduğunu bilmek ne işimize yarıyor? Yukarıda yazdığımız gibi bilgiyi dağıtıp tek bir noktada tutmadığınızda, dağınık duran herkeste aynı bilginin olması bilginin doğruluğunu ve kişilerin bu bilgiye olan güvenini sağlayan en önemli etken. Öbür türlü kırk kişide kırk farklı bilgi olursa ona dedikodu denir, kimse de beş kuruş değer vermez. 




### Peki Bitcoin şifrelemesi nasıl çalışıyor?

Bitcoin (ve diğer benzer Blockchain sistemleri) yukarıda yazdığımız her iki durumu (şifreleme ve öğütme) kullanarak kendi sistemlerinin otomatik güvenli hale getiriyorlar (ya da tek bir kişiye duyulan güven ihtiyacını sıfıra indiriyorlar). 

#### Şifrele ki senden geldiğini anlasınlar

Önce şifreleme kısmına bakalım. Efendim, biliyorsunuz Blockchain sistemi bir dijital varlığın bir kimseden diğerine geçmesini sağlıyor. Varsayalım benim bir dijital varlığım, örneğin 1 Bitcoin'im var. Öncelikle, demiştik ki, bütün Blockchain işlemleri aynı şekilde tüm makineler tarafından tutuluyor. Dolayısıyla sistemdeki bütün makineler bu 1 Bitcoin'in bende olduğunu biliyor. Şimdi ben bu parayı Ayşe'ye göndereceğim. Sistem üzerindeki makinelere diyorum ki "Ey ahali, ben 1 Bitcoin'imi Ayşe'ye gönderiyorum". Sistemde "ben" diye bahsettiğim bana ait bir adres. Ayşe de aynı şekilde bir adres. Dolayısı ile diyorum ki, "ben bu adresin sahibi kişi şu adrese bu kadar parayı gönderiyorum". Sistem üzerinden görülen bana ait hesap numarası, karşı tarafa ait hesap numarası ve ne kadar para gönderildiği. Merak ediyorsanız nasıl bir şeydir bu diye, işte bir örnek aşağıda: Bunu da kaydedip internet üzerinde [yayınlıyorlar](https://blockchain.info/block/0000000000000000001c2fa26ad4d4850fe94e688cfccf812c4fbe6d245761eb)


&nbsp;

| ![Transaction_Bitcoin_Block _519273.png](/assets/Transaction_Bitcoin_Block_519273.png) | 
|:--:| 
| *Bitcoin İşlem Örneği* |

&nbsp;

Yukarıdaki işlemi yazarken aslında iki küçük ekleme yapıyorum işleme. Birincisi, işlemi sisteme kendi Özel Anahtarım ile kaydediyorum. Böylece herkes bana ait olduğunu anlıyor bu paranın. İkicisi de, Ayşe'nin Genel Anahtarını da kaydediyorum. Böylece paranın Ayşe'ye gittiğini de anlıyor herkes. Ve bu parayı sadece Ayşe kullanabilir, çünkü bu Genel Anahtara karşılık gelen Özel Anahtar sadece Ayşe'de var. 

Eğer Ayşe bu parayı bir gün Mehmet'e göndermek isterse, benzer şekilde kendi Özel Anahtarı'nı kullandığında sistem bakacak "Hah tamam bu para zamanından Ayşe'nin Genel Anahtarı kullanılarak gönderilmişti, yani Ayşe'nin malı, şimdi Ayşe Özel Anahtarını kullanarak bu malın kendi sahipliğini ve Mehmet'in Genel Anahtarını kullanarak bu sahipliği Mehmet'e geçirdiğini söylüyor, o zaman yapalım bu transferi" diyecek. 

#### Öğüt ki, sonsuza kadar kaydedilsin

Hatırlar mısınız, önceki bir yazımızda şunu demiştik: "Blockchain sisteminde yükü çeken makinelerin bu yaptıkları işlemleri kayıt etme, daha sonra da teyid etme işlemi sonucu aldıkları ödüle (ya da lotaryaya) Bitcoin deniyor. Neden lotarya deniyor? Zira, bu on dakikada bir yapılan teyit işlemi aslında çok zor bir bulmaca. Bir nevi Sudoku oyunu gibi düşünün"

Şimdi dilerseniz bu bulmaca konusunu biraz daha açalım. Ortada tabii ki bir bulmaca yok ama bir öğütme işlemi var. Aynı yukarıda olduğu gibi "girdi" ve "çıktı" kısmı olan bir SHA şifrelemesi. 

Input'un iki parçası var 
- Belli bir süre içinde gerçekleşen tüm işlemlerin bir dökümü 
- Bir de bir sayı

Output ise yukarıdaki gibi 64 karakterli bir şifre. 

Sistem söyle çalışıyor. 
1. Her 10 dakikada bir Bitcoin ile yapılan bütün işlemler toplanıyor biraraya ve makinelere gönderiliyor
2. Sonra sistem bütün makinelere şunu söylüyor: *"Ey makineler, işlemlerin toplam [dökümü](https://blockchain.info/block/0000000000000000001c2fa26ad4d4850fe94e688cfccf812c4fbe6d245761eb) elinize geçti, şimdi bu işlem dökümünü alın yanına öyle bir sayı ekleyin ki, öğütmeye koyduğunuzda çıkan output dört tane sıfır ile başlasın"*
3. Makineler bu çıktıyı alıyor ve sırayla rakamları denemeye başlıyorlar. Önce 1 ekliyor, çıkan sonuca bakıyor, yok olmadı "370ff8b0.." ile başlayan bir output verdi. Sonra 2 ekliyor, yine bakıyor bu sefer "58ed8d94.." diye başlayan bir sayı verdi.. Böyle böyle sırayla tüm sayılar deneniyor. Ta ki bir sayı (diyelim "25264") bize "0000..." ile başlayan bir sonuç verene kadar!
4. "0000.." ile başlayan sonucu ilk bulan makine "Buldum!" diyerek bu sonuca ulaştıran sayıyı "25264" diğer makinelere haber veriyor. 
5. Sonucu gören makineler, işlem dökümünü 25264 sayısı ile birlikte şifreye sokuyorlar, bakıyorlar hakikaten çıkan sonuç "0000.." ile başlıyor, "tamam" diyorlar, "sonuç doğru" ve bir sonraki 10 dakika için yapılan işlemlere geçiyorlar. 
6. 25264 rakamını bulan makine işte bu ödülü (şu anda 12.5 Bitcoin yani 100,000 ABD Doları civari bir rakam) kazanıyor!

İşte bu kadar. Yukarıdaki süreç her 10 dakikada bir tekrar ediyor ve her 10 dakikada bir 12.5 Bitcoin yaratılarak sisteme sokuluyor. Şu ana kadar (Nisan 2017 itibariyle) 17 Milyon Bitcoin yaratıldı. Önümüzdeki 100 yıl boyunca yaklaşık 4 milyon Bitcoin daha yaratılacak bu sistemle. Nasıl oldu da 9 yılda 17 Milyon yaratılırken bundan sonraki 100 yılda 4 Milyon'a düşecek derseniz, Bitcoin yaratıcıları para enflasyona yenik düşmesin diye her dört yılda bir verilen ödülü yarıya düşürüyorlar. İlk dört yıl 10 dakikada bir 50 Bitcoin verilirken, sonra bu 25'e düştü, şu an 12.5'da, 2021'de 6.25'e inecek. 

Peki bu madenciler bu ödül ile yaşıyorlar, ödül miktarı düşerse madencilik yapmayı bırakmazlar mı diye akla bir soru gelebilir. Olabilir tabii ama bu yeni para yaratımı ile ilgili bir konu. Madenciler bir de aynı zamanda, yapılan transferler üzerinden bir komisyon almaya devam ediyorlar. Eğer Bitcoin kişiler arası para transferinde sık kullanılmaya devam ederse ya da değeri şimdiki gibi yüksek olursa bir sorun olmaz. Çok düşerse o zaman bir kısım madenci sahneden çekilir, kalanlara pastadan daha büyük bir dilim düşer ve onlar çalışmaya devam ederler. 

### Bu kadar mı?

Evet, aslında işin özü bu kadar basit. Genel Anahtar aracılığı ile zamanında bana gönderilmiş olan bir varlığı, Özel Anahtarımı kullanarak şifreleyip bir başkasına gönderiyorum. Sistem de bu işlemleri 10 dakikada bir toplayıp öğütüp bir paket haline getiriyor. Şifrelemeyi kullanarak bana ait olduğunu kanıtladığım bir dijital varlığı öğütücü sayesinde bir başkasına kati olarak transfer ediyorum - bunun için de hiç kimsenin onay vermesine ihtiyaç duymuyorum. 

Para örneğinden yola çıktık ama tekrar edelim. Dijital olarak bana ait olan her tür varlık ve bilgiyi bu şekilde bir başkasına transfer edebilirim bu teknoloji ile. Seçenekler ve ihtimaller sınırsız - gerisi hayal gücünüze kalmış..  

