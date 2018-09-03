


Blockchain bazlı şifreli sistemlerin birbirine bağlı ancak birbirinden bağımsız binlerce makineden oluştuğunu daha önceki yazılarımızda bahsetmiştik. Peki bu makineler nasıl hep birlikte aynı anda aynı kararı veriyorlar? Aralarında hiç sorun çıkmıyor mu? Eğer çıkıyorsa bu sorunları nasıl çözüp tekrar aynı yolda ilerliyorlar? Birileri sistemi manipule etmek isterse ne olacak? Olamaz mı? Olur tabii ki.. Sistemin mimarlari buna karşı nasıl önlemler almış ona bir göz atalım şimdi. 

### Önce ufak bir hatırlatma... 


Konuya başlamadan önce Blockchain sistemini kısaca hatırlatmakta yarar var. Demiştik ki, Blockchain yapılan bir işlemin binlerce makinede kaydının tutulması ve belli aralıklar ile (örneğin Bitcoin'de 10 dakikada bir) bütün makinelerin ellerindeki kayıtların toplanıp tabiri caiz ise bir balya haline getirilmesi şeklinde çalışan bir sistem idi. Bir araya getirilen bu bilgilerin her makinada aynı şekilde bulunması gerekiyor ki, üzerine yeni bir balya işlem gelebilsin. Dolayısı ile altta kalan balyadaki bilgiler hem tutarlı olsun, hem sonradan değiştirilemesin (balya bağlandıktan sonra binlerce makineye dönüp işlem değişikliği yapamazsınız, imkansıza yakın bu, ki buna "Mutabakat Mekanizması" (consensus mechanism) deniyor. 

Peki ama yukarıda bahsettiğimiz bu 10 dakikada bir her makinede işlemler nasıl aynı şekilde bulunuyor? Ya birileri ortama nifak tohumu ekmeye kalkar ve sahte işlem girmeye kalkarsa. Nasıl sağlanacak bu mutabakat?

### Bir varmış bir yokmuş...

Efendim, ilginçtir, bu anlaşmazlıklar için kullanılan terim "Bizans Generalleri Problemi" olarak biliniyor. İlk olarak  Prof. Dr. Eralp Akkoyunlu ve ekibi tarafından 1975 yılında yazılan ["Some constraints in and trade-offs in the design of network communications"](http://hydra.infosys.tuwien.ac.at/teaching/courses/AdvancedDistributedSystems/download/1975_Akkoyunlu,%20Ekanadham,%20Huber_Some%20constraints%20and%20tradeoffs%20in%20the%20design%20of%20network%20communications.pdf) isimli bir araştırmada ortaya atıldı. (New York Universitesi'nde Bilgisayar bölümünde kürsü başkanı olan ve 1987 yılında kendi elleri ile yaptığı on iki metrelik teknesi ile bir dünya seyahati gerçekleştiren [Prof. Dr. Akkoyunlu](http://www.wiki-zero.co/index.php?q=aHR0cHM6Ly90ci53aWtpcGVkaWEub3JnL3dpa2kvRXJhbHBfQWtrb3l1bmx1)'yu da bu vesile ile saygıyla analım). Sonrasında da 1982 yılında [Bizans Generallerinin Problemi](https://www.microsoft.com/en-us/research/publication/byzantine-generals-problem/) adıyla geliştirildi. Peki nedir bu problem, kısaca anlatalım. 

Vakti zamanında Bizans Ordusu bir şehri kuşatır. Ancak şehrin etrafında vadiler ve dağlar olduğu için ordu parça parça bölümler halinde kuşatmıştır şehri. Bölümler birbirlerinden uzakta oldukları için aralarındaki haberleşmeyi ulaklar sağlamaktadır. Ancak ordunun asker sayısı oldukça sınırlı, savunmadaki şehir halkı da oldukça dişlidir. Ayrıca Bizans ordusunun içindeki bölüklerin başındaki generaller içinde (komutan da bunlara dahil) hainlerin bulunma ihtimali vardır. Kale ancak ordu dört bir yandan topluca birlikte hareket ederse alınabilecektir. Aksi takdirde, bölümlerin bir kısmı hücum eder diğerleri hücüma katılmazsa hücum edenlerin telef olacağı kuşatma, Bizans ordusunun hezimetiyle sona erecektir. 

Komutan ve bölümlerin başaındaki generallerin birbiri ile anlaşması ve "saat 10:00'da hücum" ya da "geri çekil" emrini ortak bir şekilde gerçekleştirmeleri nasıl sağlanabilir? 

Bu problemi çözmeye yarayan sistemin adı. Bizans Hata Tolerans sistemi, Bütün hava ulaşım araçlarının motorlarında, nükleer santrallerde kullanılıyor.  Bu sistem, belli bir alana dağılmış ve birbirlerine sinyaller gönderen değişik parçaların gelen çelişkili sinyaller karşısında nasıl doğru hareket etmeleri gerektiğini belirliyor. 

Bu algoritmada iki temel kural var, o

1. Oyuncular kendilerine gelen mesajlar içinde çoğunluğun gönderdiği mesajı uygularlar. 
2. Oyuncuların çoğunluğunun ilerlediği şekilde sistem de ilerler. Burada önemli olan bir "doğru" sonuç çıkması değil "bir" sonuç çıkması, ortada bir kararsızlık kalmaması.

Örneğimizden devam edelim: 

Öncelikle şu basit duruma bakalım: 1 komutan ve üç general var. Ve bu generallerden biri hatalı bilgi veriyor (ya da hain). Bu durumda komutanın hücum emri vermesi durumunda nasıl bir sonuç çıkıyor, aşağıda görelim:


İki numaralı generalin perspektifinden bakalım: Kendisine üç mesaj geliyor. Bunlardan ikisi "Hücum", biri "Çekil" şeklinde. Bu durumda general, hücum taktiğini uygular. Diğer bütün generaller de benzer şekilde hareket ederler ve konsensus sağlanmış olur. 

Peki ya kumandan hainse? Ve generallere farklı mesajlar yolluyor ise?.. 





Komutan bir emir veriyor, bu emir tüm generallere dağıtılıyor. Generaller de bu emri birbirileri ile paylaşıyorlar. Böylece 



Şu şekilde de görebilirsiniz konuyu: 

Konunun teknik açıklaması oldukça uzun ve matematiksel olarak incelemek isterseniz [şu harika yazıyı]((https://marknelson.us/posts/2007/07/23/byzantine.html)) göz atabilirsiniz 

Yukarıdaki problem generaller arası iletişimin sözlü olarak yapıldığı durumlar için geçerli. Halbuki eğer bir şekilde haber gönderen kişilerin doğruluğu teyid edilebilse hayat çok daha kolay olurdu. İşte daha önce de bahsettiğimiz "öğütme" (hashing) bu konuda bize yardımcı olabilir. Nasıl mı?

Şöyle düşünün, öğütme makinası içine attığınız bir bilgiyi karmaşık rastgele bir sayı ve harf zincirine çeviriyor. Aynı bilgiyi verdiğinizde her seferinde aynı sayı/harf zincirini veren ama bilginin içindeki bir harfi bile değiştirseniz bambaşka bir sayı/harf zinciri çıkaran bir sistem. 

Buradaki püf noktası öğütme makinasına iki bilgiyi bir anda sokmak. Bu bilgilerden biri mesajımız "Çarşamba günü saat 10:00'da hücum edeceğiz" diğeri de generalin her bir birliğin başına önceden verdiği gizli bir rakam. General, her bir birliğe yazılı mesajı ve bu mesaj ile gizli rakamın birleşimi sonucu ortaya çıkan sayı/harf zincirini gönderir. Mesajı alan birlik başı mesajı ve kendinde de bulunan sayıyı öğütme mekanizmasına sokar, eğer çıkan sayı/harf zinciri ulağın getirdiği ile aynı ise o zaman mesajın komutandandan geldiğini anlar ve ona göre davranır. Eğer iki zincir tutmuyor ise o zaman saldırıya geçmez ve bekler. 




### Blockchain nasıl çözüm bulmuş bu soruna?


Bitcoin'e baz olan Blockchain bazlı sistemlerde de aynı şekilde, makinelerin doğru mesajı verdğini, arada bir hainin yanlış bilgiyi etrafa verip vermediğini nasıl anlayabiliriz? 

Yine generaller örneği üzerinden anlatırsak: Ancak öyle içimiz rahat eder. Peki Bitcoin bunu nasıl sağlıyor?

Efendim bunu anlayabilmek için öncelikle [Bitcoin şifrelemesi](http://ademimerkezi.com/genel/2018/05/08/Peki-Blockchain-sifrelemesi-nasil-calisiyor.html) konusundaki yazıya tekrar göz atmakta fayda var. 

Kısaca tekrar etmek gerekirse - Bitcoin ile yapılmış işlemleri sistemdeki bütün makineler bir araya toplayıp kendi defterlerine yazıyorlar.  Sonra da bu işlemleri toplayıp balya haline getiriyorlar. 

Peki nasıl bir işlem yapıyordu bu makineler? Hatırlarsanız bahsetmiştik daha önce. Yaptıkları aslında üç bilgiyi bir araya getirmek

1. en son yapılmış balyanın sonucunu al,
2. sonra son 10 dakikada yapılmış bütün işlemleri ekle
3. bir de eğer sonucu kazanırsan kendine bir ödül olacak (hani şu 50 Bitcoin ile başlayan ve şimdilerde 12.5 Bitcoin'e düşmüş olan), o ödülü de yaratılmış gibi ekle

Sonra bu üç bilgiyi al, ve sistemin sorduğu bulmacayı çözmeye çalış. Bu yaklaşık on dakika sürecek. Binlerce makine soruyu çözmeye çalışır ve bunun için de ciddi bir enerji harcar.  

Çözen makine anında bulmaca sonucunu tüm sisteme yayar. Sonucu alan diğer makineler ise yukarıdaki 3 bilgiyi bir araya getirir, bulmacaya bakar ve bu makinenin doğru sonucu bulduğuna ikna olurlar.  

Emin oldukları anda sistemdeki bütün makineler bu makinenin yarattığı sonucu alıp, yeni balyaya başlarlar yani yeni bir on dakika için yapılan işlemleri toplayıp yeni bulmacayı çözmeye başlarlar.

İsteyen her makine sisteme katılabilir. Ancak sisteme katılabilmek için enerji harcaman lazım. Eğer harcadığın enerji sonrası doğru işlem yaparsan çıkan sonuçtan ödül kazanmaya hakkın var. Eğer sistemi manipüle etmeye kalkarsan ödül kazanamazsın ve harcadığın enerji boşa gider. 

O nedenle "Bitcoin çok enerji harcadı, Bitcoin Sırbıstan kadar enerji harcıyor, boşa israf" gibi sözler doğru ancak işin doğasında bu var. Bitcoin sisteminin yaptığı bu kadar enerji harcayarak kendisini dışa tehditlere karşı korunaklı hale getirmek. Bunu boşa bir harcama değil bir güvenlik harcaması gibi düşünün. Kurulduğu 2009 yılından bu yana bir kez bile teklemeyen ve her tür dış tehdidi bertaraf etmiş olmanın bedeli.. 

Peki ya istisnalar olamaz mı? Olabilir. Bakalım ne olabilir ve çözümü var mı imiş?

* Örneğin, bir bulmacayı aynı anda iki makine çözerse ne olur? Bilgisayarlardan bahsettiğimiz için bu durum söz konusu değil. Milisaniye de olsa bir makine diğerinden önce çözer.. 

* Peki ya bir makine araya sahte bir işlem sokarsa, ona göre bulmacayı çözerse ve bunu dağıtmaya başlarsa? O zaman, yukarıdaki ikinci maddede yazdığı gibi, diğer makineler sahte işlemi aldıkları anda o işlem kendilerinde olmadığı için bu makinenin yazdığı sonucu kabul etmezler. Bu dediğimiz senaryonun tek istisnası, eğer bir gün bir grup tüm işlem gücünün %51'ini ele geçirir ve içeri bir sahte işlem sokup ondan sonra bu işlemi sistemdek makinelerin çoğunluğuna doğrulatır ise olabilir. Bu da çok ama çok büyük bir elektrik gücü harcaması demektir ve imkansız olmasa da çok ama çok güç bir durum. 

* Ya peki bir makine diğerinden 1 milisaniye sonra çözse bulmacayı ve her iki makine de sisteme kendi sonuçlarını verseler?. Dikkat edin, sonuçlar farklı çıkacak çünkü yukarıda yazdığımız 3. maddedeki ödülü her iki makine de kendisi için yazdı ve o bilgiyi bulmacaya soktu. Bu durumda sistem ve makineler, en uzun balya (zincir) mantığı ile çalışıyor. İki farklı dal ürüyor ve makineler ya birini ya ötekini seçiyor. Nihayetinde makineler bu dallardan birine doğru evrilmeye başlıyorlar ve o dal ana zincir haline geliyor, diğer daldaki makineler de o dalı bırakıp çoğunluğun olduğu bu dala geliyorlar (bulundukları dalı "öksüz" - orphan- bırakıyorlar. 


