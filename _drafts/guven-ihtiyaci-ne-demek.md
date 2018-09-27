Bundan önceki pek çok yazıda güven ihtiyacı diye bir kavramdan bahsettik. Ne demek istemiştik? Güveni sağlamak için arada bir aracıya ihtiyaç var. Zira öbür türlü anlaşmazlıklar olduğunda kimin doğruyu söylediğini nereden bileceksiniz. 

Belki burada Bitcoin örneğinden yola çıkarak Blockchain üzerindeki güven konusunu biraz daha açmakta fayda var. Bu konu önemli ve şahsen konuyu anlattığım kişilerin bu konuya çok takıldıklarını, akıllarının yatmadığını ve bu nedenle konuya şüphe duymaya devam ettiklerini görüyorum. 

Bir parça size Bitcoin'in temelini anlatan Bitcoin [White Paper](https://nakamotoinstitute.org/bitcoin/)'i üzerinden konuyu anlatmaya çalışacağım. 

### Elektronik İşlemler

Bitcoin deyince biliyorsunuz konumuz elektronik para (yani sanal fiziki olmayan ve elektronik ortamda transfer edilen bir para). 

Para, özellikleri itibariyle kendisine bir değer atfedilerek iki ana işe yarıyor: ya şu andaki değerinin karşılığı olarak başka bir 'şey' almak için yani "alım-satım aracı" olarak kullanılıyor, ya da hemen bir ihtiyaç yoksa gelecekte kullanılmak üzere "değer saklama aracı" olarak bir kenarda tutuluyor.  Dolayısıyla para şu an ya da gelecekte bir kişiden diğerine transfer edilebilmek için var. 

Fiziki ortamda bu iş kolay. Elinizdeki parayı aldığınız mal, hizmet her ne ise karşılığında karşıdaki kişiye veriyorsunuz. Dijital dünyaya gelince iş bir parça çetrefilleşiyor. 

Eletkronik para tanım olarak "dijital imzalardan oluşan bir zincir" demek. Pardon? Nereden çıktı şimdi bu? Anlatalım: 

Dijital bir paranız var diyelim (nasıl bu paraya sahip oldunuz, bu gerçekten bu sizin paranız mı ona birazdan geleceğiz). Bu parayı yine dijital dünyada Ahmet'e geçirdiğiniz noktada yaptığınız bunu dünyaya ilan etmek "Ey dünya, bana Ayşe tarafından gönderilmiş olan bu parayı ben de Can'a gönderiyorum). Bunu yapabilmek için üç parçaya ihtiyacınız var: 

1. Bana gönderilen herhangi bir dijital varlığı alabileceğim bir **adres** (buna Genel Anahtar diyorum, bu adresi herkes biliyor)
2. Benim bana ait bir parayı başkasına göndermem için kullandığım bir **dijital imza** (bunu da Özel Anahtarım ile yapıyorum ve kimseye söylemiyorum, çünkü söylersem biri bu imzayı kullanıp bana ait varlıkları alıp başklarına gönderebilir
3. Ve bir **dijital varlık** buradaki örnekte para (ki bu da aslında Ayşe'nin bana gönderdiği ve dünyaya ilan ettiği bir önceki mesaj idi. Dijital olduğumuz için fiziki herhangi bir varlık yok ortada. Ne var? Sadece Ayşe'nin bana para gönderdiği işlemi gösteren ve hash olarak adlandırılan karmaşık bir rakam/harf bütünü. Bu konuda daha detaylı yazı [burada](http://ademimerkezi.com/genel/2018/04/26/sifreleme-mi-cok-karisik-degil-mi.html))

Dolayısıyla ne oldu? Ayşe bana para göndermiş ve bunu dünyaya ilan etmişti (bir hash ile). Bunu yaparken benim Genel Anahtarımı kullandı (ki tüm dünya bana ait olduğunu anladı). Ben de bu hash'i aldım, kendi Özel Anahtarımı kullandım (yani imzaladım - ki tüm dünya bana ait olduğunu bildiği bu parayı harcamak istediğimi anladı), Can'ın Genel Anahtarını kullandım ve böylece yeni bir işlem yaratarak parayı Can'a gönderdim. Yani Ayşe'nin bana gönderdiği hash'e bir ekleme yaparak bir zincir oluşturdum. Baştaki tanımımıza gelirsek Ayşe'nin, benim ve Can'ın dijital imzalarından oluşan bir zincir yarattım. Para Ayşe'den bana, benden de Can'a geçti.

Şimdi başta bahsettiğimiz konuya gelelim. Ben parayı Ayşe'den aldım, ama ya Ayşe bu parayı hem bana hem de başka birine gönderdiyse. Nereden bileceğim? 

Yani Ayşe bana para gönderdikten sonra aynı parayı başka bir yere neden göndermesin? Banka gibi ortada işlemleri kaydeden bir merkez yok aslında? Olan şu: Ayşe'ye gelmiş elinde bulunan bir dijital varlık var. Bunu alıp Ahmet'e gönderdi. Herhangi bir yerde bir hesabı sıfırlanmadı. Ya iki dakika sonra yine aynı parayı Alper'e göndermeye kalkarsa? Alper Ayşe'den böyle bir işlem aldığında bunun doğru olduğunu nereden bilecek?

Normalde şu anki bankacılık sisteminde bu sorun şu şekilde çözülüyor. Ayşe parayı bana banka üzerinden gönderdiğinde banka parayı Ayşe'nin hesabından düşüp benim hesabıma ekliyor. Yani yukarıdaki elektronik zincir örneğinden gidersek, Ayşe dijital olarak zincir üzerindeki işlem ile parayı bankaya transfer ediyor, banka da dijital imzası ile zincire bir işlem daha ekleyerk parayı bana gönderiyor. Ayşe de ben de bankaya güvendiğimiz için bir sorun yok. Ayşe'ye ait para bankadaki hesabında idi ve harcandığı anda hesabında artık para yok. Sorun çözüldü. Ama arada banka yani güveni sağlayan bir aracı var. 

İşte, tüm Blockchain teknolojisinin çözdüğü temel soruna geldik. Güven problemi derken kastettiğimiz ana soruna. Bu paranın Ayşe tarafından sadece bir kez harcandığını nereden bileceğiz? . Güveni sağlayacak aracıyı kaldıralım ama bir yandan da bu tip "çifte harcamalar" olmasın. 

Makinelerin iik işlemi dikkate alıyorlar. 

Sistem ilk gönderilen işlemi esas alıyor. Yani bir işlem gerçekleşiyor ve Ayşe bunu tüm dünyaya ilan ediyor ise, bütün makineler bunu alıp işliyorlar. Sonrasında yeni işlem gelmesi durumunda makinelerin bunu reddetmesi gerekiyor. 

Ne yapıyor Bitcoin bunun için? Ortada bir tek banka olup tüm hesapları tutmasın. Ortada binlerce banka misali kayıt tutan makinelerin olduğu bir yapı olsun. Bütün işlemler şeffaf bir şekilde bütün bu makineler tarafından tutulsun. Bir para transferi yapıldığında işlem saati üzerinden bir damgalama yapılsın ve bu zaman damgası (time stamp) bütün makinelere iletilsin. Daha sonra da öyle bir sistem kuralım ki bütün bu sistemdeki makineler bu zaman damgası ile işlemin olduğu ilk an


Zaman damgalaması sisteminin işlemesi için kritik bir noktayı açıklamakta fayda var. Normal bir durumda dakikada onlarca yüzlerce işlem olduğunu düşünürsek, bu işlemlerin doğruluğunun bir şekilde teyid edilmesi gerek. Bu teyid işlemi yapılmalı ki

Peki ya birileri bu makineleri ele geçirmeye kalkarsa. Ya da çokça makineyi sistemin içinse sokmak isterse? Böyle bir sorun olmasın diye, sistem bütün makinelere bu işlemleri

Sistemin işleyişi şu şekilde oluyor
1. Bir işlem yapıldı ve tüm sisteme anons edildi
2. Bütün makineler bu işlemi alıp bir sayfa (blok) üstüne yazdılar
3. 10 dakikada bir sayfadaki tüm işlemlerin doğru olduğu konusunda (çifte harcama olmadığı) hem fikir olsunlar
4. 







Bu hizmeti karşılığı hem havale parası, hem hesap işlem ücreti altında para kesen bir aracı. Artı, güvenli olup olmadığı konusunda özellikle kriz zamanı soru işaretleri oluşan bir yapı. Sadece kriz zamanı değil kötü niyetin olduğu başka zamanları hatırlayın, örneğin [İmar Bankası'nın çifte hesap ile mevduatları yok ettiği zamanları](http://www.hurriyet.com.tr/ekonomi/yuzyilin-hayali-hesap-oyunu-38482858). 



Not: Aslında enerji harcamanın dış tehditlere karşı korumak dışında önemli bir işlevi de var. "Para nedir, neden para değerli olur ya da değersizleşir?" sorularına yanıt ararken tarih boyunca gelişen örneklere baktığımızda, genelde iki önemli konu var. Birincisi, insanların elinde ne kadar para var. İkincisi, yeni ne kadar para yaratılabilir. Bu ikisi bir paranın değerini belirliyor. Neden? Çünkü insanlar belirsizlik sevmiyorlar - özellikle para ile ilgili konularda. Gelecekte de ellerindeki paranın kullanılabileceğini ve değerini koruyabileceğini bilmek istiyorlar. Bitcoin kendi içindeki mantığı gereği ne kadar stoğu olduğunu ve ne kadar daha yaratılacağını da tam olarak hesaplayabildiğimiz bir para. Bu da onu insanların gözünde değerli hale getiriyor. 
