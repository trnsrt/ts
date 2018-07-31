Bundan önceki pek çok yazıda güven ihtiyacı diye bir kavramdan bahsettik. Ne demek istemiştik? Güveni sağlamak için arada bir aracıya ihtiyaç var. Zira öbür türlü anlaşmazlıklar olduğunda kimin doğruyu söylediğini nereden bileceksiniz. 

Belki burada Bitcoin örneğinden yola çıkarak Blockchain üzerindeki güven konusunu biraz daha açmakta fayda var. Bu konu önemli ve şahsen konuyu anlattığım kişilerin bu konuya çok takıldıklarını, akıllarının yatmadığını ve bu nedenle konuya şüphe duymaya devam ettiklerini görüyorum. 

Bir parça size Bitcoin'in temelini anlatan Bitcoin [White Paper](https://nakamotoinstitute.org/bitcoin/)'i üzerinden konuyu anlatmaya çalışacağım. 

### Elektronik İşlemler

Bitcoin deyince biliyorsunuz konumuz elektronik para (yani sanal fiziki olmayan ve eletkronik ortamda transfer edilen bir para). 

Para, özellikleri itibariyle kendisine bir değer atfedilerek iki ana işe yarıyor: ya şu andaki değerinin karşılığı olarak başka bir 'şey' almak için yani "alım-satım aracı" olarak kullanılıyor, ya da hemen bir ihtiyaç yoksa gelecekte kullanılmak üzere "değer saklama aracı" olarak bir kenarda tutuluyor.  Dolayısıyla para şu an ya da gelecekte bir kişiden diğerine transfer edilmek için var. 

Fiziki ortamda bu iş kolay. Elinizdeki parayı aldığınız mal, hizmet her ne ise karşılığında karşıdaki kişiye veriyorsunuz. Dijital dünyaya gelince iş bir parça çetrefilleşiyor. 

Eletkronik para tanım olarak "dijital imzalardan oluşan bir zincir" demek. Pardon? Nereden çıktı şimdi bu? Anlatalım: 

Dijital bir paranız var diyelim (nasıl bu paraya sahip oldunuz, bu gerçekten bu sizin paranız mı ona birazdan geleceğiz). Bu parayı Ahmet'e geçirdiğiniz noktada yaptığınız bunu dünyaya ilan etmek "Ey dünya, bana Ayşe tarafından gönderilmiş olan bu parayı ben de Ahmet'e gönderiyorum). Burada üç tane parça var: 

1. Bana gönderilen herhangi bir dijital varlığı alabileceğim bir adres (buna Genel Anahtar diyorum, herkes bunu biliyor)
2. Benim bana ait bir parayı başkasına göndermem için kullandığım bir dijital imza (bunu da Özel Anahtarım ile yapıyorum ve kimseye söylemiyorum, çünkü söylersem biri bu imzayı kullanıp bana ait varlıkları alıp başklarına gönderebilir
3. Dijital varlık buradaki örnekte para (ki bu da aslında Ayşe'nin bana gönderdiği ve dünyaya ilan ettiği bir önceki mesaj idi, Ayşe'nin bana para gönderdiği işlemi gösteren bir belge var, hash olarak adlandırılan karmaşık bir rakam/harf bütünü. Bu konuda daha detaylı yazı [burada](http://ademimerkezi.com/genel/2018/04/26/sifreleme-mi-cok-karisik-degil-mi.html))

Dolayısıyla ne oldu? Ayşe bana para göndermiş ve bunu dünyaya ilan etmişti (bir hash ile). Bunu yaparken benim Genel Anahtarımı kullandı (ki tüm dünya bana ait olduğunu anladı). Ben de bu hash'i aldım, kendi Özel Anahtarımı kullandım (ki tüm dünya bana ait olduğunu bildiği bu parayı kullanmak istediğimi anladı), Ahmet'in Genel Anahtarını kullandım, yeni bir işlem yarattım ve parayı Ahmet'e gönderdim. Yani Ayşe'nin bana gönderdiği hash'e bir ekleme yaparak bir zincir oluşturdum. Baştaki tanımımıza gelirsek Ayşe'nin, benim ve Ahmet'in dijital imzalarından olşuan bir zincir yarattım. Para Ayşe'den bana, benden de Ahmet'e geçti.

Şimdi başta bahsettiğimiz konuya gelelim. Ben parayı Ayşe'den aldım, ama ya Ayşe bu parayı hem bana hem de başka birine gönderdiyse. Nereden bileceğim? İşte, tüm Blockchain teknolojisinin çözdüğü temel soruna geldik. Güven problemi derken kastettiğimiz ana soruna. Bu paranın Ayşe tarafından sadece bir kez harcandığını nereden bileceğiz? 

Normalde şu anki bankacılık sisteminde bu sorun şu şekilde çözülüyor. Ayşe parayı bana banka üzerinden gönderdiğinde banka parayı Ayşe'nin hesabından düşüp benim hesabıma ekliyor. Yani yukarıdaki elektronik zincir örneğinden gidersek, Ayşe dijital olarak zincir üzerindeki işlem ile parayı bankaya transfer ediyor, banka da dijital imzası ile zincire bir işlem daha ekleyerk parayı bana gönderiyor. Ayşe de ben de bankaya güvendiğimiz için bir sorun yok. Ayşe'ye ait para bankadaki hesabında idi ve harcandığı anda hesabında artık para yok. Sorun çözüldü. Ama arada banka yani güveni sağlayan bir aracı var. 

Güveni sağlayacak aracıyı kaldıralım ama bir yandan da bu tip "çifte harcamalar" olmasın. 

Ne yapıyor Bitcoin bunun için? Ortada bir tek banka olup tüm hesapları tutmasın. Ortada binlerce banka misali kayıt tutan makinelerin olduğu bir yapı olsun. Bütün işlemler şeffaf bir şekilde bütün bu makineler tarafından tutulsun. Bir para transferi yapıldığında işlem saati üzerinden bir damgalama yapılsın ve bu zaman damgası (time stamp) bütün makinelere iletilsin. Daha sonra da öyle bir sistem kuralım ki bütün bu sistemdeki makineler bu zaman damgası ile işlemin olduğu ilk 



Zaman damgalaması sisteminin işlemesi için kritik bir noktayı açıklamakta fayda var. Normal bir durumda dakikada onlarca yüzlerce işlem olduğunu düşünürsek, bu işlemlerin doğruluğunun bir şekilde teyid edilmesi gerek. Bu teyid işlemi yapılmalı ki

Peki ya birileri bu makineleri ele geçirmeye kalkarsa. Ya da çokça makineyi sistemin içinse sokmak isterse? Böyle bir sorun olmasın diye, sistem bütün makinelere bu işlemleri

Sistemin işleyişi şu şekilde oluyor
1. Bir işlem yapıldı ve tüm sisteme anons edildi
2. Bütün makineler bu işlemi alıp bir sayfa (blok) üstüne yazdılar
3. 10 dakikada bir sayfadaki tüm işlemlerin doğru olduğu konusunda (çifte harcama olmadığı) hem fikir olsunlar
4. 







Bu hizmeti karşılığı hem havale parası, hem hesap işlem ücreti altında para kesen bir aracı. Artı, güvenli olup olmadığı konusunda özellikle kriz zamanı soru işaretleri oluşan bir yapı. Sadece kriz zamanı değil kötü niyetin olduğu başka zamanları hatırlayın, örneğin [İmar Bankası'nın çifte hesap ile mevduatları yok ettiği zamanları](http://www.hurriyet.com.tr/ekonomi/yuzyilin-hayali-hesap-oyunu-38482858). 
