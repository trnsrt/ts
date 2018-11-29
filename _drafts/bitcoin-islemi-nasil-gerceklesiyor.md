

Eğer kriptoparalara ve Bitcoin'e biraz ilgi duyduysanız ya da konuyu biraz araştırdıysanız mutlaka duymuşssunuzdur aşağıdaki söylemleri:

- Bitcoin işlemleri 10 dakika içinde bitiyor, dünyanın öbür ucuna 10 dakika içinde dijital bir varlığı gönderebiliyorsunuz
- Bitcoin, kişilerin ellerindeki varlığı birden fazla kez harcamasına olanak sağlamayan bir yapıda
- Bitcoin üzerindeki bütün işlemler görülebiliyor, öyle ki ilk yapılmış işlem olan 3 Ocak 2009 tarihli işleme kadar geriye gidip görebiliyorsunuz
- Bitcoin üzerindeki işlemler makineler tarafından teyid ediliyor, edilmez ise işlem geçersiz sayılıyor
- Eğer biri Bitcoin sistemindeki makinelerin çoğunu bile ele geçirse yapabileceği en tehlikeli iş en son 10 dakikada yapılmış bir işlemi geri çevirmek olur, kişilerin varlıklarına zarar veremez, hiçbir varlığın sahibinin haberi olmadan elden ele dolaşmasına da izin vermez

Kulağa ilginç ve hoş gelen söylemler. peki ama ne menem bir şeydir bu para transferi? Nasıl emin olabiliyoruz bu kadar? Gelin isterseniz gerçek bir Bitcoin işlemi nasıl oluyor bakalım ve ona göre hakikaten güvenli mi değil mi karar verelim. 

### Bir Bitcoin işlem özeti

Bitcoin işlem özünde herhangi bir miktarda Bitcoin'in sahipliğinin bir kişiden diğerine transfer edilmesi demek. Aşağıda bir Bitcoin işlemi görüyorsunuz (linkine [buradan](https://www.blockchain.com/btc/tx/f1cd43bc5be1309c8e76d4584a8f6dfbfca37399588416042f8a85603c5f4995) ulaşabilirsiniz). 


&nbsp;

| ![transaction-sample-640-b.png](/assets/transaction-sample-640-b.png) | 
|:--:| 
| *28 Kasım 2018 tarihli gerçek bir [işlem](https://www.blockchain.com/btc/tx/f1cd43bc5be1309c8e76d4584a8f6dfbfca37399588416042f8a85603c5f4995)* |

&nbsp;

Önemli olan satırlara kısaca bakalım daha iyi anlamak için bu işlemi. 

İşlem numarası (Transaction ID): Yapılan her işlemin kendine ait bir numarası var. Yukarıda turuncu ile taranmış alan. Tek bir numara ve sadece bu işlem için kullanılıyor. Ve bu numarayı alın herhangi bir Bitcoin kaydını tutan siteye girin ve o işlem ile ilgili resimde gördüğünüz tüm bilgilere ulaşabilirsiniz. 

Örneğin f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16 no'lu hash'i bir siteye (www.blockchain.info) girin, karşınıza Bitcoin ile yapılmış ilk işlem (2009 Ocak ayından) çıkacak. Boşuna dememişler Bitcoin ile yapılan her işlem kayıt altında diye. Gördüğünüz gibi 2009 yılından itibaren yapılan her işlem tek tek görülebiliyor bu şekilde. Hani hep deniyor ya, bütün bilgisayarlar yapılan işlemlerin tüm kaydını tutuyor diye. İşte bu o. 

Alıcının adresi: Gönderdiğiniz parayı alanın adresi. Yukarıda pembe renk ile gördüğünüz alan. Gönderilen Bitcoin her zaman bir adrese gider. Burada iki adres görüyorsunuz. Neden? Bunun nedenine az sonra değineceğiz. 

Gönderici adresi: Aldığınız Bitcoin bir adrese gelir ama siz onu birisine göndermek isterseniz bunu cüzdanınızı kullanırsınız. Adres size ait posta kutusu iken, cüzdan size ait Özel Anahtarların olduğu ve bu sayede bu parayı sizin harcamanıza olanak veren sistem. Aşağıdaki örnekte biraz daha anlatacağız bunu. 

Kullanılan para (Total input): Bu işlemde alıcıdan cüzdanından gönderilen toplam para miktarı - yeşil renk ile gösterilen yer. 

Çıkan (yaratılan) para (Total output): Alıcılara gönderilen toplam para. Yukarıdaki kullanılan paradan bir miktar daha az, çünkü işlemi gerçekleştiren makinelere ödenen bir komisyon var (Total input'un hemen alt satırında görüyorsunuz) 

### Bitcoin işleminin temel mantığı

Bir Bitcoin işlemi gerçekleşirken temel birkaç mantık var. Gelin onlara bir parça değinelim. 

Bitcoin'in karışmaması, herhangi bir şekilde rahat takip edilebilmesi için temel kurallar. 
1. Öncelikle size gelen Bitcoin'ler her zaman ayrı ayrı dururlar. Hiçbir zaman birbirleri ile karışmazlar. 
2. Sonra, her Bitcoin yalnızca bir kez kullanılır. Evet, yanlış duymadınız. Her Bitcoin miktarı ne olursa olsun, bir kez kullanılır. 

Örnek verelim: Diyelim size Ali'den 0.5 BTC (Bitcoin) ve Ayşe'den de 0.4 BTC geldi. Cüzdanınızda bu iki para ayrı ayrı durur. Birbirine karıştırılmaz.  Ve diyelim ki siz şimdi Barış'a 0.2 BTC göndereceksiniz. 

![Bitcoin-transaction-example-b.png](/assets/Bitcoin-transaction-example-b.png) 

Sistem şöyle çalışır: Ali'den gelmiş 0.5 BTC alınır. Sonrasında bu paranın 0.2 BTC'si Barış'a gönderilir, kalan 0.3 BTC benim adıma yaratılan yeni bir Bitcoin adresine gönderilir (ve benim cüzdanıma geri döner). Yani bir nevi elimde 0.5 BTC bütün banknot var, Barış'a 0.3 BTC verdim, kalan 0.2 BTC de "paranın üstü" olarak bana geri döndü. 

Bu ortaya çıkan iki paraya (0.3 BTC ve 0.2 BTC) UTXO Unspent Transaction Amount denir. Yani benim cüzdanımda duran 0.5 BTC yok edildi, yerine ben de ve Barış'ta iki parça halinde 0.5 BTC (eksi komisyon) yaratıldı. İşte bu yüzden yukarıdaki ilk orijinal örnekte de paranın gittiği iki adres görüyosunuz pembe renkte. Üstteki pembe renkli olan alıcının, alttaki ise gönderici için yaratılan yeni adres. Artık cüzdanımda Ayşe'den gelen 0.4 BTC ve Barış'a gönderdiğim paradan geri dönen 0.2 BTC toplam 0.6 BTC var (yine ayrı ayrı duruyorlar). 

Bu UTXO kavramı önemli. Çünkü bütün UTXO'ları toplarsanız o ana kadar oluşmuş bütün Bitcoin toplamına ulaşıyorsunuz. Bu da birilerinin sahte para ortaya çıkarmasını önlüyor. Bütün makineler bu UTXO'lara bakarak yapılan işlemlerin doğru olduğunu anlıyorlar. Hani deniyor ya, "Ya birisi çıkar da bütün makinelere ele geçirirse? Kendisine para yaratırsa?" Nasıl yaratacak ki? Bir anda sıfırdan para yaratmak isteseniz yaratamazsınız çünkü para bir adresten gelmek zorunda. Şimdiye kadar yaratılmış bütün paralar belli, hangi adreslerde olduğu belli. O adreslerden o paraları ancak o adresin sahipleri kendi Özel Anahtarları ile çıkarabilirler. 

Yarın öbür gün biri çıkar da makinelerin birlikte uzlaşma ile çalıştıkları sistemi makinelerin %51'ini ele geçirerek sahiplenirse yapabileceği tek hamle, harekete geçtiği anda yapılmış olan son işlemleri red etmek olabilir. O nedenle zaten hep söylenen bir kural vardır. Birinden bir Bitcoin alsanız bile onu hemen kendinizin bilmeyin. İşlem önce bir bloğa yazılsın. O blok sistemdeki makineler tarafından doğru kabul edilsin. Üzerine birkaç yeni blok daha konsun. Ancak ondan sonra gönül rahatlığı içinde o para benim diyebilirsiniz. 

### Sonuç

İşte böyle. Bir Bitcoin işleminin nasıl gerçekleştiğini görmek eğer içinizde "ya param yarın öbür gün birileri tarafından iç edilirse" korkusu varsa bunu bertaraf etmek için önemli. Bitcoin aslında sahibi olduğuna emin olabileceğiniz belki de tek varlık. Elinizde banknot varsa sahte çıkabilir. Keza altın varsa da öyle. Gerçek olup olmadığını anlamak için testten geçirmeniz gerekir. Bitcoin için öyle değil. Gönderin birine parayı sistem reddetmiyor ise gerçektir. Bitcoin'e sahipseniz yapmanız gereken tek kritik konu Özel Anahtarınızı kaybetmemek. Ona sahip oldukça o para siz istediğiniz sürece sizin olacak - merak etmeyin. 









https://www.ccn.com/bitcoin-transaction-really-works/
