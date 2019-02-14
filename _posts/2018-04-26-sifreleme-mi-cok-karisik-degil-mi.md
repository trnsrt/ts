---
layout: post
title:  "Şifreleme mi? Çok karışık değil mi?"
date:   2018-04-26 07:45:15 +0300
categories: Genel
---

[Geçtiğimiz yazımızda](/genel/2018/04/25/sifreleme-ne-demek-neden-onemli.html) neden şifrelemenin Blockchain'in temel taşı olduğundan bahsetmiştik. 

Hatırlatmak gerekirse, şifreleme Blockchain'in temelini oluşturuyor, çünkü Blockchain dağınık bir sistemde çalışıyor, yani bilgi binlerce farklı, birbiri ile ilintili ama birbirini tanımayan makine üzerinde bulunuyor. Dağınık sistemlerin kontrolü olmadığı için bilginin düzgün ve değiştirilmemiş olması son derece önemli - bunu sağlayan da şifreleme sistemi. Yani şifreleme sayesinde herhangi bir bilgi Blockchain üzerindeki her nokta üzerinde hem aynı şekilde tutarlı hem de gizli olarak tutulabiliyor. 

Şifreleme teknik ve karmaşık görünse de onu daha iyi anlamak bize günlük hayatımızda Blockchain teknolojisini nasıl daha verimli olarak kullanırız konusunda farklı ipuçları verebilir. Eğer genel yapı olarak ne olduğunu anladıysak, biraz daha teknik olarak nedir şifreleme ona bakalım. 


### Şifreleme ve öğütme - iki önemli özellik

Dijital dünyada bir varlığı bir kişiden diğerine transfer ederken iki önemli konu var dikkat etmemiz gereken:

1. Birincisi, öncelikle varlığın transferi güvenli bir şekilde yapılmalı. Buradan kastedilen bu dijital varlık değiştirilmeden bir taraftan öbürüne geçmeli, ve geçtikten sonra bu işlem bir daha değiştirilememeli. Yani herkeste aynı bilgiler olmalı. Herkeste aynı bilgi olursa kimse "eyvah kandırılıyor muyum?" kaygısı yaşamaz, gece evinde rahat uyur. Bu  **öğütme** (hashing) sayesinde başarılıyor. 
2. . İkincisi, bana ait bir varlığı bir başkasına devredeceksem öncelikle bu varlığın bana ait olduğu ve bu varlığı kendim devretmek istediğim, yani bu işlemi başlatan kişinin gerçekten ben olduğum (orjinal/otantik olduğunun) teyit edilmeli. Ama bunu yaparken bir taraftan da bana ait özel bilgilerin gizliliği kalması da sağlanmalı. İşte bu da **şifreleme** (encryption/decryption) sayesinde başarılıyor. 

### Önce bir öğütelim... 

Kapalı bir kutu (belki de bir kağıt öğütücü) düşünün. Bir taraftan anlamlı bir sözcük veriyorsunuz, diğer taraftan rakam ve sayılardan oluşan anlamsız rastgele bir sayı/harf dizisi veriyor.  İşte buna öğütme deniyor. 

Bir örnek yapalım dilerseniz: 

&nbsp;

| ![ogutme-mekanizmasi.png](/assets/ogutme-mekanizmasi-v4.png) | 
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
| *Yatağın başından ucuna kadar uzanan mavi damalı yorganın engebeleri, gölgeli vadileri ve mavi yumuşak tepeleriyle örtülü tatlı ve ılık karanlıkta Rüya yüzükoyun uzanmış uyuyordu. Dışarıdan kış sabahının ilk sesleri geliyordu: Tek tük geçen arabalar ve eski otobüsler, poğaçacıyla işbirliği eden salepçinin kaldırıma konup kalkan güğümleri ve dolmuş durağının değnekçisinin düdüğü. Odada, lacivert perdelerin soldurduğu kurşuni bir kış ışığı vardı. Uyku mahmurluğuyla Galip, karısının mavi yorgandan dışarı uzanan başına baktı: Rüya'nın çenesi yastığın kuştüyüne gömülmüştü. Alnının eğiminde, o sırada aklının içinde olup biten harika şeyleri insana korkuyla merak ettiren gerçek dışı bir yan vardı. ‘Hafıza,’ diye yazmıştı bir köşe yazısında Celâl, 'bir bahçedir.’ 'Rüya'nın bahçeleri, Rüya'nın bahçeleri…’ diye düşünmüştü o zamanlar Galip, 'düşünme, düşünme, kıskanırsın!’ Ama Galip karısının alnına bakarak düşündü.* | *4144231a09b37be5e58def84d0773802240cb283a3a74dc840bc2d1ae454c723*  |

Ta tam! Bambaşka bir dizi ama yine 64 karakterli. Buraya isterseniz girdi olarak koca bir ansiklopedi koyun, sonuç yine 64 karakterli bir dizi olacak. 

--

Şimdi ilk örneğimize geri dönelim: Merhaba kelimesinin sonuna bir "!" işareti ekleyelim, bakalım ne olacak?

| Girdi  | Şifreli Sonuç  |
|---|---|
| *Merhaba!*  | *b1726b923349fd632fa7ce8b62a06c5a3f785be1db4f6a831eef58d70c7a45cc*  |

Yukarıdaki "Merhaba" da çıkan sonuç ile karşılaştırın bakalım. Tamamıyla değişti!. Bir harf ekledik ama ilk kelimeden tamamen farklı bir sonuç çıktı ortaya. Ama dikkat edin 64 karakterli yine. 

Çok güzel de, bu kadar girizgahı neden yaptın derseniz? Buraya kadar anlattıklarımızı biraz daha açalım. Aynı girdiler hep aynı sonucu veriyor. Ama girdide bir harf bile değiştirin, çıkan sonuç bambaşka oluyor.  Bu ne işe yarıyor? Bu girilen bilginin orijinal ya da otantik (değiştirilmemiş) olup olmadığını anlamamıza yarıyor. Eğer elinizde bir bilgi (girdi) ve bu bilgi sonucu ortaya çıkan şifreli bir sonuç da varsa, bu girdi hakikaten bu sonucu mu veriyor test edebiliyorsunuz. Girin ilk bilgiyi (girdiyi) şifrelemeye aynı sonucu bulacaksınız. 

Bu arada şunu da belirtmekte fayda var. Bu şifreleme mekanizmalarının özelliği şu: sonucu biliyor olmanız girdiyi de bildiğiniz anlamına gelmiyor. Yani, girdiyi biliyorsanız sonucu bulabiliyorsunuz ama sonuçtan geriye bilgiye gidemiyorsunuz. Yani, öğütücüden geçmiş kağıtlara bakarak kağıtta ne yazıyordu okuyamıyorsunuz. Ancak kağıdın orjinali varsa elinizde onu öğütücüden geçirip önceki öğütülmüş kağıt demetinin aynısını elde edebiliyorsunuz.

Bilginin tutarlı olduğunu bilmek ne işimize yarıyor? Yukarıda yazdığımız gibi bilgiyi dağıtıp tek bir noktada tutmadığınızda, bilginin dağınık olarak herkeste aynı şekilde durması, bilginin doğruluğu ve kişilerin bu bilgiye olan güvenini sağlayan en önemli etken. Öbür türlü kırk kişide kırk farklı bilgi olursa ona dedikodu denir, kimse de beş kuruş değer vermez. 

Harika. Ama yarın öbür gün ben bu mesajı değiştirsem "Yok, yahu ben öyle dememiştim, böyle demiştim" desem? Kusura bakmayın mümkün değil, çünkü mesajınız alındı, güzel bir şekilde öğütüldü ve tüm sistemdeki makineler üzerinde aynı şekilde tutulmaya başladı. 

Peki çok güzel. Ama ya bu mesajı ben değil de bir başkası yazdıysa? Onu da şifreleme hallediyor.Şimdi de şifrelemeye bakalım:


### Şifrelemeli mi, şifrelememeli mi? Şimdi şifreleyelim...

Şifreleme bir nevi kilitleme demek. Diyelim bir mesajınız var. Şifreleme derken, bir anahtar ve kilit düşünün, bu anahtar sizin mesajınızı alıyor ve kilidin içine koyup kilitliyor. 

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

Önce ikinciden başlayalım. Şöyle demiş bir akıllı bilim adamı. "Şu kilidin özelliğini bir parça değiştireyim - öyle bir hale getireyim ki, iki tane anahtarı olsun. Biri sadece kilidi kilitlemeye, öbürü de sadece açmaya yarasın. Kilidi açmaya yarayan anahtarı, tüm arkadaşlarıma vereyim. Ama kilitlemeye yarayan sadece bende olsun". İlginç bir mantık. Neye yarıyor peki? Şuna: Benim anahtarım kilidi kilitleyen tek anahtar olunca isteyen herkes benim dağıttığım diğer anahtar ile bu mesajı benim yazdığımı ve kilitlediğimi anlayacak.  

İşte bu iki anahtardan bana ait olana "Özel Anahtar", herkese verdiğime de "Genel Anahtar" deniyor. 


&nbsp;

| ![ozel-genel-anahtar-800.png](/assets/ozel-genel-anahtar-800.png) | 
|:--:| 
| *Özel ve Genel Anahtarlar* |

&nbsp;

Özel Anahtar ve Genel Anahtarı bana ait birbirlerinin aynı olan iki anahtar gibi düşünebiliriz. Aradaki tek fark, Özel Anahtarın  sadece benim bildiğim (hiç kimse ile paylaşmadığım) bir anahtar olması. Genel Anahtar ise yine bana ait, ama herkes ile paylaştığım tüm dünyanın görebileceği bir anahtar. İlişkileri ise şu: Benim Özel Anahtarım ile kapadığım kapıyı (şifrelediğim mesajı) Genel Anahtarı bilen herkes açabiliyor (şifreyi açıp mesajı görebiliyor).   

&nbsp;

| ![sifreleme-mekanizmasi.png](/assets/sifreleme-mekanizmasi.png) | 
|:--:| 
| *Şifreleme Mekanizması* |

&nbsp;

İşte yukarıdaki ilk sorunu çözdük. Mesajın benden geldiğini herkes gördü. İyi de yazının içeriğini tüm dünya görmüş oldu, ben içeriği bilinsin istemiyordum, şimdi ne olacak? İşte burada ilk bölümde anlattığımız öğütme mekanizması ortaya giriyor ve sizin yazınızı okunamaz bir hale getiriyor. Güzel değil mi, hem sizden geldiği anlaşılıyor hem de içeriğini kimse okuyamıyor. 

Para ya da başka dijital varlığın Blockchain ile aktarılmasında da işte yukarıdaki sistem kullanılıyor. Özel anahtar ile bana ait olan bir varlığı bir başkasına gönderiyorum, paranın benim bakiyemde olduğu ve bu gönderdiğim paranın miktarını herkes görüyor. Öğütme sayesinde ise bu bakiyenin bana ait olduğunu gizleyebiliyorum. 


### Sonuç

İşte dijital dünyada devrim yaratan şifreleme mekanizması bu şekilde çalışıyor. Bu mekanizma sayesinde dijital varlıkların (örneğin paranın) herhangi bir aracıya ihtiyaç doğmaksızın güvenli bir şekilde bir taraftan öbürüne taşınması sağlanıyor. Dijital olarak bana ait olan her tür varlığı bu şekilde bir başkasına transfer edebilirim bu teknoloji ile. Seçenekler ve ihtimaller sınırsız - gerisi hayal gücünüze kalmış...

Bir sonraki yazımızda Bitcoin özelinde şifreleme ne işe yarıyor sorusuna bakacağız..


--
&nbsp;

Geçmişte nelerden bahsettik bakmak isterseniz: 
- Blockchain teknolojisinin nasıl çıktığını merak ediyorsanız, "[Geceleri uykunuzu ne kaçırıyor](/genel/2018/03/01/Geceleri-uykunuzu-ne-kaciriyor.html)" ve "[Sahi nedir bu Blockchain Allah aşkına?](/genel/2018/03/02/Sahi-nedir-bu-blockchain-allah-askina.html) yazılarımıza, 
- Bu teknolojinin şu anda en olgun şekilde kullanılan uygulamalarından Bitcoin'e ilginiz varsa "[Bitcoin ne tam olarak?](/genel/2018/03/13/Bitcoin-ne-tam-olarak.html), "[Bitcoin para mı gerçekten?](/genel/2018/03/22/Bitcoin-para-mi-gercekten.html)" ve "[Bütün bunlar bir balon mu?](/genel/2018/03/05/Butun-bunlar-bir-balon-mu.html)" yazılarımıza, 
- Blockchain'in değişik alanlarda getirdiği potansiyel yenilikler için, insanı yardım'da [İyilik için Blockchain](/genel/2018/03/29/Iyilik-icin-blockchain.html), sanatta [Sanat için Blockchain](/genel/2018/03/29/Iyilik-icin-blockchain.html) ve sağlıkta [Sağlık için Blockchain](/genel/2018/04/17/saglik-icin-blockchain.html) yazılarımıza
göz atabilirsiniz

