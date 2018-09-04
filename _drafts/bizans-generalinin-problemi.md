


Blockchain bazlı şifreli sistemlerin birbirine bağlı ancak birbirinden bağımsız binlerce makineden oluştuğunu daha önceki yazılarımızda bahsetmiştik. Peki bu makineler merkezi bir otorite olmadan nasıl hep birlikte aynı anda aynı kararı veriyorlar? Aralarında hiç sorun çıkmıyor mu? Eğer çıkıyorsa bu sorunları nasıl çözüp tekrar aynı yolda ilerliyorlar? Birileri sistemi manipule etmek isterse ne olacak? Olamaz mı? Olur tabii ki.. Sistemin mimarlari buna karşı nasıl önlemler almış ona bir göz atalım şimdi. 

### Önce ufak bir hatırlatma... 


Konuya başlamadan önce Blockchain sistemini kısaca hatırlatmakta yarar var. Demiştik ki, Blockchain yapılan bir işlemin binlerce makinede kaydının tutulması ve belli aralıklar ile (örneğin Bitcoin'de 10 dakikada bir) bütün makinelerin ellerindeki kayıtların toplanıp tabiri caiz ise bir balya haline getirilmesi şeklinde çalışan bir sistem idi. Bir araya getirilen bu bilgilerin her makinada aynı şekilde bulunması gerekiyor ki, üzerine yeni bir balya işlem gelebilsin. Dolayısı ile altta kalan balyadaki bilgiler hem tutarlı olsun, hem sonradan değiştirilemesin (balya bağlandıktan sonra binlerce makineye dönüp işlem değişikliği yapamazsınız, imkansıza yakın bu). 

Peki ama yukarıda bahsettiğimiz bu 10 dakikada bir her makinede işlemler nasıl aynı şekilde bulunuyor? Ya birileri ortama nifak tohumu ekmeye kalkar ve sahte işlem girmeye kalkarsa. Nasıl sağlanacak bu mutabakat? Öncelikle 'mutabakat' derken ne kastediyoruz ona bir bakalım: 

### Bir varmış bir yokmuş...

Efendim, ilginçtir, birbirinden bağımsız sistemlerin (bunlara dağıtık sistemler de deniyor) arasındaki ilişkileri ve çıkan anlaşmazlıklar literatüre "Bizans Generalleri Problemi" olarak girmiş. 

İlk olarak  Prof. Dr. Eralp Akkoyunlu ve ekibi tarafından 1975 yılında yazılan ["Some constraints in and trade-offs in the design of network communications"](http://hydra.infosys.tuwien.ac.at/teaching/courses/AdvancedDistributedSystems/download/1975_Akkoyunlu,%20Ekanadham,%20Huber_Some%20constraints%20and%20tradeoffs%20in%20the%20design%20of%20network%20communications.pdf) isimli bir araştırmada bu sorun ortaya atıldı. (New York Universitesi'nde Bilgisayar bölümünde kürsü başkanı olan ve 1987 yılında kendi elleri ile yaptığı on iki metrelik teknesi ile bir dünya seyahati gerçekleştiren [Prof. Dr. Akkoyunlu](http://www.wiki-zero.co/index.php?q=aHR0cHM6Ly90ci53aWtpcGVkaWEub3JnL3dpa2kvRXJhbHBfQWtrb3l1bmx1)'yu da bu vesile ile saygıyla analım). 

Sonrasında da 1982 yılında [Bizans Generallerinin Problemi](https://www.microsoft.com/en-us/research/publication/byzantine-generals-problem/) adıyla geliştirildi. Peki nedir bu problem, kısaca anlatalım. 

&nbsp;

![bizans-generalleri.jpg](/assets/bizans-generalleri.jpg)

&nbsp;

Vakti zamanında Bizans Ordusu bir şehri kuşatır. Ancak şehrin etrafında vadiler ve dağlar olduğu için ordu parça parça bölümler halinde kuşatmıştır şehri. Bölümler birbirlerinden uzakta oldukları için aralarındaki haberleşmeyi ulaklar sağlamaktadır. Ancak ordunun asker sayısı oldukça sınırlı, savunmadaki şehir halkı da oldukça dişlidir. Ayrıca Bizans ordusunun içindeki bölüklerin başındaki generaller içinde (komutan da bunlara dahil) hainlerin bulunma ihtimali vardır. Kale ancak ordu dört bir yandan topluca birlikte hareket ederse alınabilecektir. Aksi takdirde, bölümlerin bir kısmı hücum eder diğerleri hücüma katılmazsa hücum edenlerin telef olacağı kuşatma, Bizans ordusunun hezimetiyle sona erecektir. 

Komutan ve bölümlerin başaındaki generallerin birbiri ile anlaşması ve "saat 10:00'da hücum" ya da "geri çekil" emrini ortak bir şekilde gerçekleştirmeleri nasıl sağlanabilir? Yani birbirine güvenmeyen (içlerinde hain ya da hatalı sinyaller veren) parçaların ortak hareket etmesi nasıl sağlanır?

Bu problemi çözmeye yarayan sistemin adı. Bizans Hata Tolerans sistemi, Bütün hava ulaşım araçlarının motorlarında, nükleer santrallerde kullanılıyor.  Bu sistem, belli bir alana dağılmış ve birbirlerine sinyaller gönderen değişik parçaların gelen çelişkili sinyaller karşısında nasıl doğru hareket etmeleri gerektiğini belirliyor. 

Sistem şu şekilde aşağıdaki kurallara bağlı olarak çalışıyor: 

1. Her bir parça kendisine gelen mesajlar içinde çoğunluğun gönderdiği mesajı uygularlar. 
2. Sistem oyuncuların çoğunluğunun ilerlediği şekilde ilerler. Burada önemli olan bir "doğru" sonuç çıkması değil "bir" sonuç çıkması, ortada bir kararsızlık kalmaması.

Örneğimizden devam edelim: 

Öncelikle şu basit duruma bakalım: 1 komutan ve üç general var. Ve bu generallerden biri hatalı bilgi veriyor (ya da hain). Bu durumda komutanın hücum emri vermesi durumunda nasıl bir sonuç çıkıyor, aşağıda görelim:

&nbsp;

| ![bizans-general-problem-1-v3.png](/assets/bizans-general-problem-1-v3.png) | 
|:--:| 
| *2. General'e gelen mesajlar. Ne yapmalı bu general?* | 

&nbsp;

İki numaralı generalin perspektifinden bakalım: Kendisine üç mesaj geliyor. Bunlardan ikisi "hücum", biri "çekil" şeklinde. Bu durumda general, "hücum" emrini uygular, çünkü kendisine gelen hücum emirleri daha fazla. Bir numaralı general de aynı şekilde hareket eder. 3 numaralı hain general "çekil" emri gereği dursa bile  sonuçta iki general (yani çoğunluk) "hücum" emrini verdiği için sistem hücum eder. 

Peki ya kumandan hainse? Ve generallere farklı mesajlar yolluyor ise?. Bu durumda olaylar şu şekilde gelişiar: 

&nbsp;

| ![bizans-general-problem-3.png](/assets/bizans-general-problem-3.png) | 
|:--:| 
| *Komutan hain ise, generaller ne yaparlar?* | 

&nbsp;

Komutan bir emir veriyor, bu emir tüm generallere dağıtılıyor. Generaller de bu emri birbirileri ile paylaşıyorlar. Bu durumda her bir generale iki "Hücum" ve bir "Çekil" mesajı gelecek. Bu durumda da generaller "Hücum" emrini uygulayacaklar. 



Konunun teknik açıklaması oldukça uzun ve matematiksel olarak incelemek isterseniz [şu harika yazıya](https://marknelson.us/posts/2007/07/23/byzantine.html)) da göz atabilirsiniz 


### Arkası yarına

Evet, Blockchain bazlı sistemler genel olarak yukarıda bahsedilen Bizans Hata Tolerans sistemine bağlı "Mutabakat Mekanizması"nı kullanarak kendi aralarında uzlaşma sağlıyorlar. Tabii yukarıdaki sistemin Blockchain'e uygulanması sırasında pek çok farklı işlem (örneğin Proof-of-Work) söz konusu. Yazımız çok uzadığı için ona da bir sonraki yazımızda bakalım artık. 

