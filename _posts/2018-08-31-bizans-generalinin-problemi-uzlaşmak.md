---
layout: post
title:  "Bizans Generalinin Problemi: Uzlaşmak"
date:   2018-08-31 13:03:34 +0300
categories: Genel
---



Blockchain bazlı şifreli sistemlerin birbirine bağlı ancak birbirinden bağımsız binlerce makineden oluştuğundan daha önceki yazılarımızda bahsetmiştik. Peki bu makineler merkezi bir otorite olmadan nasıl hep birlikte aynı anda aynı kararı veriyorlar? Aralarında hiç sorun çıkmıyor mu? Eğer çıkıyorsa bu sorunları nasıl çözüp tekrar aynı yolda ilerliyorlar? Birileri sistemi manipüle etmek isterse ne olacak? Olamaz mı? Olur tabii ki... Sistemin mimarları buna karşı nasıl önlemler almış ona bir göz atalım şimdi. 

### Önce ufak bir hatırlatma... 


Konuya başlamadan önce Blockchain sistemini kısaca hatırlatmakta yarar var. Demiştik ki, Blockchain yapılan bir işlemin binlerce makinede kaydının tutulması ve belli aralıklar ile (örneğin Bitcoin'de on dakikada bir) bütün makinelerin ellerindeki kayıtların toplanıp tabiri caiz ise bir balya haline getirilmesi şeklinde çalışan bir sistem idi. Bir araya getirilen bu bilgilerin her makinede aynı şekilde bulunması gerekiyor ki, üzerine yeni bir balya işlem gelebilsin. Dolayısı ile altta kalan balyadaki bilgiler hem tutarlı olsun, hem sonradan değiştirilemesin (balya bağlandıktan sonra binlerce makineye dönüp işlem değişikliği yapamazsınız, imkansıza yakın bu). 

Peki ama yukarıda bahsettiğimiz bu on dakikada bir her makinede gerçekleşen işlemler nasıl aynı şekilde bulunuyor? Ya birileri ortama nifak tohumu ekmeye kalkar ve sahte işlem girmeye kalkarsa? Nasıl sağlanacak bu mutabakat? Öncelikle 'mutabakat' derken ne kastediyoruz ona bir bakalım: 

### Bir varmış bir yokmuş...

Efendim, ilginçtir, birbirinden bağımsız sistemlerin (bunlara dağıtık sistemler de deniyor) arasındaki ilişkiler ve çıkan anlaşmazlıklar literatüre "Bizans Generalleri Problemi" olarak girmiş. 

İlk olarak  Prof. Dr. Eralp Akkoyunlu ve ekibi tarafından 1975 yılında yazılan ["Some constraints in and trade-offs in the design of network communications"](http://hydra.infosys.tuwien.ac.at/teaching/courses/AdvancedDistributedSystems/download/1975_Akkoyunlu,%20Ekanadham,%20Huber_Some%20constraints%20and%20tradeoffs%20in%20the%20design%20of%20network%20communications.pdf) isimli bir araştırmada bu sorun ortaya atılmış. (New York Üniversitesi Bilgisayar Bölümü'nde kürsü başkanı olan ve 1987 yılında kendi elleri ile yaptığı on iki metrelik teknesi ile bir dünya seyahati gerçekleştiren [Prof. Dr. Akkoyunlu](http://www.wiki-zero.co/index.php?q=aHR0cHM6Ly90ci53aWtpcGVkaWEub3JnL3dpa2kvRXJhbHBfQWtrb3l1bmx1)'yu da bu vesile ile saygıyla analım). 

Sonrasında da 1982 yılında [Bizans Generalleri Problemi](https://www.microsoft.com/en-us/research/publication/byzantine-generals-problem/) adıyla geliştirilmiş. Peki nedir bu problem, kısaca anlatalım. 

&nbsp;

![bizans-generalleri.jpg](/assets/bizans-generalleri.jpg)

&nbsp;

Vakti zamanında Bizans Ordusu bir şehri kuşatır. Ancak şehrin etrafında vadiler ve dağlar olduğu için ordu parça parça birlikler halinde kuşatmıştır şehri. Birlikler birbirinden uzakta oldukları için aralarındaki haberleşmeyi ulaklar sağlamaktadır. Ancak ordunun asker sayısı oldukça sınırlı, savunmadaki şehir halkı da oldukça dişlidir. Ayrıca birliklerin başındaki generaller içinde (komutan da bunlara dahil) hainlerin bulunma ihtimali vardır. Kale ancak ordu dört bir yandan topluca birlikte hareket ederse alınabilecektir. Aksi takdirde, birliklerin bir kısmı hücum eder diğerleri hücuma katılmazsa saldıranların telef olacağı kuşatma, Bizans ordusunun hezimetiyle sona erecektir. 

Komutan ve birliklerin başındaki generallerin birbiri ile anlaşması ve "saat 10:00'da hücum" ya da "geri çekil" emrini ortak bir şekilde gerçekleştirmeleri nasıl sağlanabilir? Yani birbirine güvenmeyen (içlerinde hain ya da hatalı sinyaller verebilecek) parçaların ortak hareket etmesi nasıl sağlanır?   Nasıl bir "Mutabakat Mekanizması" olmalı ki aralarında beraberce hareket edebilirler? İşte Bizans Generalleri Problemi bu. 

Bu problemi çözmek için oluşturulan sistemin adı ise Bizans Hata Tolerans Sistemi. Bütün hava ulaşım araçlarının motorlarında ve nükleer santrallerde kullanılıyor.  Bu sistem, belli bir alana dağılmış ve birbirlerine sinyaller gönderen değişik parçaların gelen çelişkili sinyaller karşısında nasıl doğru hareket etmeleri gerektiğini belirliyor. 

Sistem aşağıdaki kurallara bağlı olarak çalışıyor: 

1. Oyuncuların en az 2/3'ü doğru çalışıyor olmalı (yalan söylemez);
2. Her bir parça kendisine gelen mesajlar içinde çoğunluğun gönderdiği mesajı uygular; 
3. Sistem oyuncuların çoğunluğunun ilerlediği şekilde ilerler. (Burada önemli olan "doğru" bir sonuç çıkması değil "tutarlı bir" sonuç çıkması, ortada bir kararsızlık kalmaması)

Örneğimizden devam edelim: 

Öncelikle şu basit duruma bakalım: Bir komutan ve üç general var. Ve bu generallerden biri hain (ya da hatalı bilgi veriyor). Bu durumda komutanın hücum emri vermesi durumunda nasıl bir sonuç çıkıyor aşağıda görelim:

&nbsp;

| ![bizans-general-problem-1-v3.png](/assets/bizans-general-problem-1-v3.png) | 
|:--:| 
| *İkinci General gözünden gelen mesajlar: Ne yapmalı bu general?* | 

&nbsp;

İki numaralı generalin perspektifinden bakalım: Kendisine üç mesaj geliyor. Bunlardan ikisi "hücum", biri "çekil" şeklinde. Bu durumda general, "hücum" emrini uygular, çünkü kendisine gelen hücum emirleri daha fazla. Bir numaralı general de aynı şekilde hareket eder. Üç numaralı hain general "çekil" emri gereği dursa bile  sonuçta iki general (yani çoğunluk) "hücum" emrini verdiği için sistem hücum eder. 

Peki ya kumandan hainse? Ve generallere farklı mesajlar yolluyor ise? Bu durumda olaylar şu şekilde gelişir: 

&nbsp;

| ![bizans-general-problem-2-v2.png](/assets/bizans-general-problem-2-v2.png) | 
|:--:| 
| *Komutan hain ise, generaller ne yaparlar?* | 

&nbsp;

Komutan bir emir veriyor, bu emir tüm generallere dağıtılıyor. Generaller de bu emri birbirileri ile paylaşıyorlar. Bu durumda her bir generale iki "hücum" ve bir "çekil" mesajı gelecek. Bu durumda da generaller "hücum" emrini uygulayacaklar. 



Konunun teknik açıklaması oldukça uzun ve matematiksel olarak incelemek isterseniz [şu harika yazıya](https://marknelson.us/posts/2007/07/23/byzantine.html) göz atabilirsiniz.


### Arkası yarına

Evet, Blockchain bazlı sistemler genel olarak yukarıda bahsedilen Bizans Hata Tolerans sistemine bağlı "Mutabakat Mekanizması"nı kullanarak kendi aralarında uzlaşma sağlıyorlar. Tabii yukarıdaki sistemin Blockchain'e uygulanması sırasında pek çok farklı işlem (örneğin Proof-of-Work) söz konusu. Çok uzattığımız için ona da bir sonraki yazımızda bakalım artık. 

&nbsp;



---


&nbsp;


*Not: Yazdığımız 25+ yazının bir bütünlük içinde nelerden oluştuğuna bakmak isterseniz [Hakkımızda](http://ademimerkezi.com/about/) sayfasına göz atabilirsiniz.* 
