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

En basitinden başlayalım. Şifreleme bir nevi kilitleme demek. Diyelim bir mesajınız var. Şifreleme dediğimiz, bir anahtar ve kilit düşünün, bu anahtar sizin mesajınızı alıyor ve kilidin içine koyup kilitliyor. 

&nbsp;

| ![sifreleme-mekanizmasi-simetrik-v2.png](/assets/sifreleme-mekanizmasi-simetrik-v2.png) | 
|:--:| 
| *Basit (simetrik) Şifreleme* |

&nbsp;


Dolayısıyla sizin yazdığınız bu mesajı sadece anahtarı verdiğiniz kişiler görebiliyor. Buraya kadar güzel. Bu anahtarı bir kişiye verirsem bir sorun yok. Bir taraf mesaj yazar, anahtar ile kilitler, diğeri anahtarın kopyası ile açar mesajı okur, sonra yeni bir mesaj yazar ve anahtarı ile şifreler ve bu böyle sürüp gider. Ancak işin pratiğe geldiğimizde soru(n)lar ortaya çıkmaya başlıyor. 

Ya karşı taraf bu anahtarı başka birine daha verirse? O zaman ne olacak? O anahtarı verdiği üçüncü kişi bir mesaj yazarsa? Karşı tarafın bu mesajı yazdığını nereden bileceğim? Anahtarın kopyalanabildiği durumlarda sıkıntı var, mesajı kimin yazdığını anlamak zor. 

İşte bu "mesajı kim yazdı, kimler okudu sorununu çözmek için" 1976 yılında yeni bir şifreleme yöntemi ortaya atılmış. "Özel anahtar" ve " Genel Anahtar" kavramları çıkmış.  


#### "Özel Anahtar" ve "Genel Anahtar"

Yine yukarıdaki anahtar-kilit örneğinden devam edelim. Demiştik ki iki ana problem var. Birincisi benim yazdığım mesajın içeriğini anahtarı olan (ya da anahtarı alan) herkesin görüyor olması, ikincisi de herkesin bu mesajı benim yazdığımdan (kilidi benim kilitlediğimden) emin olması.

Önce ikincincisinden başlayalım. Şöyle demiş bir akıllı bilim adamı. "Şu kilidin özelliğini bir parça değiştireyim - öyle bir hale getireyim ki, iki tane anahtarı olsun. Biri sadece kilidi kilitlemeye, öbürü de sadece açmaya yarasın. Kilidi açmaya yarayan anahtarı, tüm arkadaşlarıma vereyim. Ama kilitlemeye yarayan sadece bende olsun". İlginç bir mantık - içgüdüsel olarak düşünmeyeceğiniz bir seçenek. Neye yarıyor peki? Şuna: Benim anahtarım kilidi kilitleyen tek anahtar olunca isteyen herkes benim dağıttığım diğer anahtar ile bu mesajı benim yazdığımı ve kilitlediğimi anlayacak.  

İşte bu iki anahtardan bana ait olana "Özel Anahtar", herkese verdiğime de "Genel Anahtar" deniyor. 


&nbsp;

| ![ozel-genel-anahtar-800.png](/assets/ozel-genel-anahtar-800.png) | 
|:--:| 
| *Özel ve Genel Anahtarlar* |

&nbsp;

Özel Anahtar ve Genel Anahtarı bana ait birbirlerinin aynı olan iki anahtar gibi düşünebiliriz. Aradaki tek fark, Özel Anahtarın  sadece benim bildiğim (hiç kimse ile paylaşmadığım) bir anahtar. Genel Anahtar ise yine bana ait, ama herkes ile paylaştığım tüm dünyanın görebileceği bir anahtar olması. İlişkileri ise şu: Bemim Özel Anahtarım ile kapadığım kapıyı (şifrelediğim mesajı) Genel Anahtarı bilen herkes açabiliyor (şifreyi açıp mesajı görebiliyor).   

&nbsp;

| ![sifreleme-mekanizmasi.png](/assets/sifreleme-mekanizmasi.png) | 
|:--:| 
| *Şifreleme Mekanizması* |

&nbsp;

İşte yukarıdaki ilk sorunu çözdük. Mesajın benden geldiğini herkes gördü. Şimdi ikinci soruna ve çözümü olan öğütme (hashing) kısmına geçelim. 


### Şimdi de değirmen gibi öğütelim.. 

Yukarıdaki örnekten devam edelim. Mesajı yazdım ve herkes de mesajın benden geldiğini gördü. İyi de yazının içeriğini tüm dünya görmüş oldu, ben içeriği bilinsin istemiyordum, şimdi ne olacak? İşte burada öğütme mekanizması ortaya giriyor ve sizin yazınızı okunamaz bir hale getiriyor. Güzel değil mi, hem sizden geldiği anlaşılıyor hem de içeriğini kimse okuyamıyor. 

Harika. Ama yarın öbür gün ben bu mesajı değiştirsem "Yok, yahu ben öyle dememiştim, böyle demiştim" desem? Kusura bakmayın mümkün değil, çünkü mesajınız alındı, güzel bir şekilde öğütüldü ve tüm sistemdeki makineler üzerinde aynı şekilde tutulmaya başladı. Nasıl mı? Anlatalım: 

Kapalı bir kutu (belki de bir kağıt öğütücü) düşünün. Bir taraftan anlamlı bir sözcük veriyorsunuz, diğer taraftan rakam ve sayılardan oluşan anlamsız rastgele bir sayı/harf dizisi veriyor.  İşte buna öğütme deniyor. 

Bir örnek yapalım dilerseniz: 

&nbsp;

| ![ogutme-mekanizmasi2.png](/assets/ogutme-mekanizmasi2.png) | 
|:--:| 
| *Öğütme Mekanizması* |

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


### Sonuç

İşte dijital dünyada devrim yaratan şifreleme mekanızması bu şekilde çalışıyor. Bu mekanizma sayesinde dijital varlıkların (örneğin paranın) herhangi bir aracıya ihtiyaç doğmaksızın güvenli bir şekilde bir taraftan öbürüne taşınması sağlanıyor. Dijital olarak bana ait olan her tür varlığı bu şekilde bir başkasına transfer edebilirim bu teknoloji ile. Seçenekler ve ihtimaller sınırsız - gerisi hayal gücünüze kalmış..

Bir sonraki yazımızda Bitcoin özelinde şifreleme ne işe yarıyora bakacağız..


--
Geçmişte nelerden bahsettik bakmak isterseniz: 
- Blockchain teknolojisinin nasıl çıktığını merak ediyorsanız, "[Geceleri uykunuzu ne kaçırıyor](http://ademimerkezi.com/genel/2018/03/01/Geceleri-uykunuzu-ne-kaciriyor.html)" ve "[Sahi nedir bu Blockchain Allah aşkına?](http://ademimerkezi.com/genel/2018/03/02/Sahi-nedir-bu-blockchain-allah-askina.html) yazılarımıza, 
- Bu teknolojinin şu anda en olgun şekilde kullanılan uygulamalarından Bitcoin'e ilginiz varsa "[Bitcoin ne tam olarak?](http://ademimerkezi.com/genel/2018/03/13/Bitcoin-ne-tam-olarak.html), "[Bitcoin para mı gerçekten?](http://ademimerkezi.com/genel/2018/03/22/Bitcoin-para-mi-gercekten.html)" ve "[Bütün bunlar bir balon mu?](http://ademimerkezi.com/genel/2018/03/05/Butun-bunlar-bir-balon-mu.html)" yazılarımıza, 
- Blockchain'in değişik alanlarda getirdiği potansiyel yenilikler için, insanı yardım'da [İyilik için Blockchain](http://ademimerkezi.com/genel/2018/03/29/Iyilik-icin-blockchain.html), sanatta [Sanat için Blockchain](http://ademimerkezi.com/genel/2018/03/29/Iyilik-icin-blockchain.html) ve sağlıkta [Sağlık için Blockchain](http://ademimerkezi.com/genel/2018/04/17/saglik-icin-blockchain.html) yazılarımıza
göz atabilirsiniz

