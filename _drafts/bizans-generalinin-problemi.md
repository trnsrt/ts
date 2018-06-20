


Blockchain bazlı şifreli sistemlerin birbirine bağlı ancak birbirinden bağımsız binlerce makineden oluştuğunu daha önceki yazılarımızda bahsetmiştik. Peki bu makineler nasıl hep birlikte aynı anda aynı kararı veriyorlar? Aralarında hiç sorun çıkmıyor mu? Eğer çıkıyorsa bu sorunları nasıl çözüp tekrar aynı yolda ilerliyorlar? Birileri sistemi manipule etmek isterse ne olacak? Olamaz mı? Olur tabii ki.. Sistemin mimarlari buna karşı nasıl önlemler almış ona bir göz atalım şimdi. 

### Önce ufak bir hatırlatma... 


Konuya başlamadan önce Blockchain sistemini kısaca hatırlatmakta yarar var. Demiştik ki, Blockchain yapılan bir işlemin binlerce makinede kaydının tutulması ve belli aralıklar ile (örneğin Bitcoin'de 10 dakikada bir) bütün makinelerin ellerindeki kayıtların toplanıp tabiri caiz ise bir balya haline getirilmesi şeklinde çalışan bir sistem idi. Bir araya getirilen bu bilgilerin her makinada aynı şekilde bulunması gerekiyor ki, üzerine yeni bir balya işlem gelebilsin. Dolayısı ile altta kalan balyadaki bilgiler hem tutarlı olsun, hem sonradan değiştirilemesin (balya bağlandıktan sonra binlerce makineye dönüp işlem değişikliği yapamazsınız, imkansıza yakın bu, ki buna "Mutabakat Mekanizması" (consensus mechanism) deniyor. 

Peki ama yukarıda bahsettiğimiz bu 10 dakikada bir her makinede işlemler nasıl aynı şekilde bulunuyor? Ya birileri ortama nifak tohumu ekmeye kalkar ve sahte işlem girmeye kalkarsa. Nasıl sağlanacak bu mutabakat?

### Bir varmış bir yokmuş...

Efendim, ilginçtir, bu mimari anlaşmazlıklar için kullanılan terim "Bizans Generalleri Problemi" olarak biliniyor. Nedir bu, kısaca anlatalım. 

Vakti zamanında Bizans Ordusu bir kaleyi kuşatır. Kale dört bir yandan kısım kısım bölükler tarafından sarılmıştır. Bölükler birbirlerinden uzakta oldukları için aralarındaki haberleşmeyi ulaklar sağlamaktadır. Ancak ordunun asker sayısı oldukça sınırlı, kaledekiler de oldukça dişlidir. Ayrıca Bizans ordusunun içinde de (özellikle ulaklar arasında) hainler bulunmaktadır. Kale ancak ordu dört bir yandan topluca birlikte hareket ederse alınabilecektir. Aksi takdirde, bölüklerin yarısından azı hücum eder diğerleri hücüma katılmazsa hücum edenlerin telef olacağı kuşatma, Bizans ordusunun hezimetiyle sona erecektir. 

Bölükler arasında doğru saatte hücum edileceği konusunda nasıl bir birlik sağlanabilir?. 

Sorunun çözümü oldukça zor - özellikle iki 

### Bitcoin nasıl çözüm bulmuş bu soruna?

Peki nasıl bir işlem yapıyordu bu makineler? Hatırlarsanız bahsetmiştik daha önce. Yaptıkları aslında üç bilgiyi bir araya getirmek

1. en son yapılmış balyanın sonucunu al,
2. sonra son 10 dakikada yapılmış bütün işlemleri ekle
3. bir de eğer sonucu kazanırsan kendine bir ödül olacak (hani şu 50 Bitcoin ile başlayan ve şimdilerde 12.5 Bitcoin'e düşmüş olan), o ödülü de yaratılmış gibi ekle

Sonra bu üç bilgiyi al, ve sistemin sorduğu bulmacayı çözmeye çalış. Bu yaklaşık on dakika sürecek. Binlerce makine soruyu çözmeye çalışır ve bunun için de ciddi bir enerji harcar.  Çözen makine anında bulmaca sonucunu tüm sisteme yayar. Sonucu alan diğer makineler ise yukarıdaki 3 bilgiyi bir araya getirir, bulmacaya bakar ve bu makinenin doğru sonucu bulduğuna ikna olurlar.  Emin oldukları anda sistemdeki bütün makineler bu makinenin yarattığı sonucu alıp, yeni balyaya başlarlar yani yeni bir on dakika için yapılan işlemleri toplayıp yeni bulmacayı çözmeye başlarlar.

İsteyen her makine sisteme katılabilir. Ancak sisteme katılabilmek için enerji harcaman lazım. Eğer harcadığın enerji sonrası doğru işlem yaparsan çıkan sonuçtan ödül kazanmaya hakkın var. Eğer sistemi manipüle etmeye kalkarsan ödül kazanamazsın ve harcadığın enerji boşa gider. 

O nedenle "Bitcoin çok enerji harcadı, Bitcoin Sırbıstan kadar enerji harcıyor, boşa israf" gibi sözlere kanmayın. Bitcoin sisteminin yaptığı bu kadar enerji harcayarak kendisini dışa tehditlere karşı korunaklı hale getirmek. Boşa bir harcama değil bir güvenlik harcaması gibi düşünün. Kurulduğu 2009 yılından bu yana bir kez bile teklemeyen ve her tür dış tehdidi bertaraf etmiş olmanın bedeli.. 


Peki ya istisnalar olamaz mı? Olabilir. Bakalım ne olabilir ve çözümü var mı imiş?

* Örneğin, bir bulmacayı aynı anda iki makine çözerse ne olur? Bilgisayarlardan bahsettiğimiz için bu durum söz konusu değil. Milisaniye de olsa bir makine diğerinden önce çözer.. 

* Peki ya bir makine araya sahte bir işlem sokarsa, ona göre bulmacayı çözerse ve bunu dağıtmaya başlarsa? O zaman, yukarıdaki ikinci maddede yazdığı gibi, diğer makineler sahte işlemi aldıkları anda o işlem kendilerinde olmadığı için bu makinenin yazdığı sonucu kabul etmezler. Bu dediğimiz senaryonun tek istisnası, eğer bir gün bir grup tüm işlem gücünün %51'ini ele geçirir ve içeri bir sahte işlem sokup ondan sonra bu işlemi sistemdek makinelerin çoğunluğuna doğrulatır ise olabilir. Bu da çok ama çok büyük bir elektrik gücü harcaması demektir ve imkansız olmasa da çok ama çok güç bir durum. 

* Ya peki bir makine diğerinden 1 milisaniye sonra çözse bulmacayı ve her iki makine de sisteme kendi sonuçlarını verseler?. Dikkat edin, sonuçlar farklı çıkacak çünkü yukarıda yazdığımız 3. maddedeki ödülü her iki makine de kendisi için yazdı ve o bilgiyi bulmacaya soktu. Bu durumda sistem ve makineler, en uzun balya (zincir) mantığı ile çalışıyor. İki farklı dal ürüyor ve makineler ya birini ya ötekini seçiyor. Nihayetinde makineler bu dallardan birine doğru evrilmeye başlıyorlar ve o dal ana zincir haline geliyor, diğer daldaki makineler de o dalı bırakıp çoğunluğun olduğu bu dala geliyorlar (bulundukları dalı "öksüz" - orphan- bırakıyorlar. 

