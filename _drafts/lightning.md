Geçtiğimiz yazımızda, Bitcoin'in geniş kitlelerce kullanımının önündeki en büyük engelin teknik olarak kısıtlı kapasitesi olduğundan bahsetmiştik. Basitçe tekrarlarlarsak: yapılan her işlem Blockchain üzerine yazılıyor, bunu madenciler yapıyor ve işlem binlerce makineye yazıldığı ve 10 dakikada bir balya haline getirilip onaylandığı için saniyede maksimum 7 işlem yazılabiliyor. 

Ama eğer biz her işlemi Blockchain üzerine yazmak yerine bunları toplayıp bir araya getirip o şekilde yazarsak, yani Blockchain'in zinciri üzerine değil zincir dışı işlem yaparsak o zaman bu teknik kısıtlardan kurtulabiliriz. Peki ama, biri bana bir Bitcoin yollarsa benim bu Bitcoin'e sahip olduğumu kanıtlamamın tek yolu bu paranın Bitcoin Blockchain'ine işlenmiş olması değil miydi? Nasıl şimdi emin olacağım Bitcoin'in benim olduğuma eğer Blockchain zincirini kullanmaz isek? İşte Lightning Network dediğimiz sistem hem her işlem için değil ama yapılan onlarca/binlerce işlemin sadece sonuçlarının yazıldığı bir yol öneriyor. 

### Nedir bu Lightning Network?

Önceki yazımızda da belirttiğimiz gibi Lightning Network esasında Bitcoin üzerine kurulmuş ikinci bir katman. 

Lightning'in ana prensibi Bitcoin üzerindeki işlemlerin zincir üzerinden (yani bloklara yazılması yerine) zincir dışına çıkarılması. 

Özündeki prensip ise şu: 
* İşlemleri yapmak için ayrı kanallar kuralım. 
* Bu kanallar baştan Bitcoin sistemine para yatırsınlar, bir nevi depozito koysunlar. 
* Sonrasında bu koydukları parayı geçmemek kaydıyla Bitcoin sistemi dışında kişiler arası para transferi yapılmasına aracılık etmeye yetkili olsunlar (ve aracılık ettikleri bu işlemlerden cüzi bir işlem ücreti alsınlar). 
* Birinden alsınlar öbürüne versinler, ama yaptıkları işlemlerin sonundaki net bakiye başta koydukları depozitoyu hiçbir şekilde geçmesin. 
* Böylece madencileri kullanmadan işlemlere aracılık etsinler, dolayısıyla masrafları çok daha az olsun ve bunun sonucunda da sistemi kullananan kullanıcılardan komisyon olarak çok cüzi rakamlar isteyebilsinler. 

### Nasıl çalışıyor peki bu Lightning Network?

Basit bir örnek ile başlayalım sonra detaylandıralım: 

* Ali ve Ayşe ticaret ile uğraşıyor ve birbirlerine sık sık para gönderiyorlar. Bu ikili öncelikle beraberce bir kilitli sandık yaratıyorlar. Bu sandığa her ikisi de bir miktar Bitcoin koyuyorlar (örneğin her biri 5 BTC). İlk para koyduklarında bu işlem Bitcoin Blockchain üzerine işleniyor.

![lightning-1a-640.png](/assets/lightning-1a-640.png)
* Diyelim bir gün Ali Ayşe'ye 1 BTC gönderiyor, ertesi gün de Ayşe Ali'ye 2 BTC. Bu iki işlemi de Bitcoin network'üne binlerce makineye göndermek yerine kendi aralarındaki bu sandık üzerinde hesaplaşıyorlar. İki gün sonunda Ali'nin sandıktaki hakkı 6 BTC, Ayşe'ninki ise 4 BTC oldu. Sandık orada, iki taraf da kendi bakiyelerini biliyorlar. 
![lightning-1b-640b.png](/assets/lightning-1b-640b.png)
* Eğer iki günün sonunda Ali ya da Ayşe'den biri parayı kendi hesabına çekmek isterse sandığı iptal ediyor, ve her bir tarafın bakiyesi kendi hesaplarına geri aktarılıyor. Bu durumda Ali 6 BTC Ayşe ise 4 BTC alıyor.
![lightning-1c-640.png](/assets/lightning-1c-640.png)

İşte iki kişi bir sandık yaratınca aslında aralarında bir kanal yaratmış oluyorlar. Sandıktaki para da bu kanalın Bitcoin üzerindeki depozitosu, yani bu kanalı kullanacakların güvencesi. 

İki kişi üzerinden basit ama böyle ikili ticaret eden kaç kişi var ki? Peki denkleme bir kişi daha ekleyelim: Örneğin Ayça. Ayça'nın da Ayşe ile ortak bir sandığı olsun ancak Ali ile daha önce hiçbir para ilişkisi olmasın. Ayça Ali'ye para gönderebilir mi (örneğin 0.5 BTC)? Gayet tabii. Ayça Ali'ye parayı Ayşe aracılığı ile gönderebilir. Ayça'nın Ayşe ile ortak sandığından 0.5 BTC'sini Ayşe'nin yaparsınız, Ayşe'nin Ali ile olan sandığındaki 0.5 BTC'sini de Ali'nin. 

![lightning-2a-640.png](/assets/lightning-2a-640.png)

Peki şimdi bu tip sandıklardan (kanallardan) binlerce kişi ve kurumun açtığını düşünün. Bir kahve zincirisiniz. Ali ile Ayşe içtikleri kahve için size ödeme yaptılar. Siz de bu ödemeleri alıp size kahve çekirdeğı satın almada kullandınız. Size çekirdeği satan firma dijital reklamlarının dizaynını yapan Ayça'ya bu para ile ödeme yaptı. Ayça da Ali'den aldığı internet hosting hizmeti için kendisine bir miktar para yolladı. İşte tüm sistemi Lightning Network üzerinden döndürebilirsiniz.  Binlerce işlemin Bitcoin üzerinden Blockchain bloklarına yazılmadan güvenli bir şekilde gerçekleştirildiği ikinci bir katman yarattık işte. 

### Sonuç

Bitcoin sanal dünyadaki şifreli paralar içinde en kullanılanı. Ancak şu anda hala kısıtlı bir kitle tarafından kullanılıyor. Eğer hakikaten bir değer elde edecek ise faydalarının geniş kitlelere yayılması gerekiyor. Bitcoin geliştiricileri hızlı davranıp Bitcoin'i 'bozma' riski almamak için geniş kitlelerin ihtiyacı olan değişiklikleri çabucak yapmayacaklar. Bunu Lightning Network gibi ikinci katmanlar yapacak. Başarılı olup olmayacaklarını zaman gösterecek ancak şimdiden söyleyebileceğimiz doğru yolda oldukları. 

