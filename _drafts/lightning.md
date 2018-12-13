Geçtiğimiz yazımızda, Bitcoin'in ileride değerli olup olmayacağının iki ana belirleyicisi olacağını belirtmiştik - hakikaten insanların işine yarayacak mı, ikincisi de geniş kesimler Bitcoin'i kullanabilecek mi? Bu iki soruya ne kadar olumlu cevap verebiliyorsak Bitcoin'in değerinin  de ileride o kadar çok olacağını düşünebiliriz. 

### Bitcoin'in geleceği

Her ne kadar teknoloji hızla gelişiyor olsa da Bitcoin için aynısını söylemek mümkün değil. Bitcoin yavaş gelişen bir sistem - kasıtlı olarak böyle aslında. Efendim, Bitcoin biliyorsunuz bir dijital para. İşin içine para girdiğinde konu ciddileşiyor. Bitcoin geliştiricileri de bu bilinç ile hareket ediyorlar. 

Bu geliştiriciler temel bir prensibi var "Acele işe şeytan karışır", yani ne kadar hızlı gider ve yeterince test ve deneme yapmazsanız hata çıkma ihtimali o kadar artar. O nedenle bu topluluk Bitcoin sistemini özellikle yavaş yavaş tabiri caizse sindire sindire geliştirme yolunu seçiyor. 

İkinci bir prensipleri daha var bu topluluğun "Bir ürüne ne kadar fonksiyon eklerseniz, o kadar güvenlik açığına davet çıkarırsınız" Konu para olunca güvenlik açığının yaratacağı sorunlar daha da dramatik hale gelebiliyor. O nedenle geliştiricilerin Bitcoin'e para dışında yeni fonksiyonlar eklemeleri oldukça zor. 

Peki ne olacak o zaman? Bitcoin bu şekliyle mi devam edecek. Tabii ki hayır. Olacak olan ana hatları ile şu. Bitcoin ana (baz)  katman olarak fonksiyonunu dijital para şeklinde sürdürecek. Bu ana katmanın üzerine inşa edilecek yeni katmanlar, geniş kitlelerin ihtiyacı olan yeni fonksiyonları sunacaklar. 

### Kahvenizi Bitcoin ile ödemek mi?

Bitcoin üzerinde yapılan yeniliklerin büyük kısmı işte bu iki alanda ilerleme sağlamaya yönelik çalışmalar. Neler bunlar? En meşhurları Lightning Newtork. Nedir bu Lightning kısaca bakalım:

Bitcoin ile kıtalararası para gönderme yapabiliyorsunuz diyoruz. Bunun yaparken de maliyetleriniz oldukça düşük. Özellikle yurtdışında yaşayanlar için çok iyi haber. Ama bu göreceli olarak küçük bir kitle ve sınırötesi para transferini ayda yılda bir yapıyorlar. Bitcoin'in geniş kitlelere yayılması için yeterli değil. 

Peki ya gündelik hayatta mikro ödemeler için Bitcoin kullanımı. İşte orada da Bitcoin'in kendi iç kısıtlamaları söz konusu. Bitcoin'in saniyede yapabileceği işlem sayısı 7 ile kısıtlanmış. Ethereum için bu sayı 20 işlem. Paypal'in saniyede 450, Visa'nın ise 56.000 işlem yapma kapasitesi olduğunu [söylersek](https://altcointoday.com/bitcoin-ethereum-vs-visa-paypal-transactions-per-second/) Bitcoin'in neden mikro ödemeler için kullanılamayacağını anlayabiliriz sanırım. 


&nbsp;

| ![queue.gif](/assets/queue.gif) | 
|:--:| 
| *Mikro ödemeleri Bitcoin üzerinden yapmaya kalkarsak* |

&nbsp;



Aslında işlem kısıtının ötesinde başka sorunlar da var mikro ödemeler için, o da hız. Normalde Bitcoin transferi yaptığınızda işlem madenciler tarafından alınıyor ve o anki en son bloğun içine işleniyor. Peki ya bloğun hacminden daha fazla işlem yapıldı ise. O zaman işlem bir sonraki bloğa atılıyor. Her bir blok 10 dakikada bir toplanıp bağlandığı için bu işleminizin gerçekleşmesini 10 dakika sonraya atıyor. Peki neye göre işleminizin o bloğa ya da sonraki bloğa gireceğine karar veriyor madenciler? O yaptığınız için verdiğiniz işlem ücretine. İşlem ücretiniz ne kadar yüksek ise o kadar erken işleminiz gerçekleşiyor. Mikro ödemeler zaten kendileri ufak rakamlar oldukları için işlem ücretleri de çok düşük olmak zorunda, bu nedenle de geç gerçekleşme ihtimalleri yüksek. 


### Lightning Network

Aslında bir mikro ödemenin gerçekleşmesi için tüm Bitcoin network'ünün kullanılmasına çok da gerek yok. Çünkü biliyorsunuz Bitcoin ile bir işlem yapıldığında bu binlerce makineye bu işlem yazılıyor. Bir kafeye girip satın aldığınız bir kahvenin işlemi neden binlerce makinede yazılsın ki? 

İşte bu felsefeden yola çıkan geliştiriciler Bitcoin üzerinde mikro işlem yapabilmek için ikinci bir katman yarattılar. Buna da Lightning network adını verdiler. 

Lightning'in ana prensibi Bitcoin üzerindeki işlemlerin zincir üzerinden (yani bloklara yazılması yerine) zincir dışına çıkarılması demek. Nasıl çalışıyor peki bu? Bir örnek üzerinden anlatalım. 

İki kişi üzerinden başlayalım. 

* Ali ve Ayşe ticaret ile uğraşıyor ve birbirlerine sık sık para gönderiyorlar. Bu ikili öncelikle beraberce bir kilitli sandık yaratıyorlar (aslında kanal deniyor ama şimdilik anlaşılabilmesi için sandık örneğini kullanıyoruz) Bu sandığa her ikisi de bir miktar Bitcoin koyuyorlar (diyelim 5 BTC). İlk para koyduklarında bu işlem Bitcoin network'üne işleniyor. 
* Diyelim bir gün Ali Ayşe'ye 1 BTC gönderiyor, ertesi gün de Ayşe Ali'ye 2 BTC. Bu iki işlemi de Bitcoin network'üne binlerce makineye göndermek yerine kendi aralarındaki bu sandık üzerinde hesaplaşıyorlar. İki gün sonunda Ali'nin sandıktaki hakkı 6 BTC, Ayşe'ninki ise 4 BTC oldu. Sandık orada, iki taraf da kendi bakiyelerini biliyorlar. 
* Eğer iki günün sonunda Ali ya da Ayşe'den biri parayı kendi hesabına çekmek isterse sandığı iptal ediyor, ve her bir tarafın bakiyesi kendi hesaplarına geri aktarılıyor. Bu durumda Ali 6 BTC Ayşe ise 4 BTC alıyor. 

İki kişi üzerinden basit ama böyle ikili ticaret eden kaç kişi var ki? Peki denkleme bir kişi daha ekleyelim: Örneğin Ayça. Ayça'nın Ayşe ile ortak bir sandığı olsun ancak Ali ile herhangi bir para alışverişi bulunmasın. Ayça Ali'ye para (örneğin 0.5 BTC) gönderebilir mi? Gayet tabii. Ayça Ali'ye parayı Ayşe aracılığı ile gönderir. Ayça'dan 0.5 BTC alırsınız, Ayşe'nin Ayça ile olan sandığında 0.5 BTC'si artar, Ali ile olan sandıktaki 0.5 BTC'si azalır, ve o 0.5 BTC Ali'nin olur. 

Peki şimdi bu tip sandıklardan (kanallardan) binlerce kişi ve kurumun açtığını düşünün. Binlerce işlemin Bitcoin üzerinden Blockchain bloklarına yazılmadan güvenli bir şekilde gerçekleştirildiği ikinci bir katman yarattık işte. 

