---
layout: post
title:  "Blockchain nasıl uzlaşır?"
date:   2018-09-07 12:03:34 +0300
categories: Genel
---




Önceki [yazımızda](https://ademimerkezi.com/genel/2018/08/31/bizans-generalinin-problemi-uzla%C5%9Fmak.html) bağımsız (dağıtık), birbirine güvenmeyen oyuncuların nasıl uzlaşıp beraberce hareket ettiklerine bakmıştık. Kısaca bahsedersek, Bizans Hata Tolerans diye adlandırılan bir sistemi kullanan oyuncular, kendilerine gelen mesajların içinde çoğunluğun söylediğ mesajı uygulayarak ilerliyorlar, böylece ortada kararsızlık söz konusu olmuyor idi. 

### Sorular, sorular...

Geçtiğimiz yazının başlangıcında akla takılabilecek birkaç soru sormuştuk: 

> *Peki bu makineler merkezi bir otorite olmadan nasıl hep birlikte aynı anda aynı kararı veriyorlar? Aralarında hiç sorun çıkmıyor mu? Eğer çıkıyorsa bu sorunları nasıl çözüp tekrar aynı yolda ilerliyorlar? Birileri sistemi manipüle etmek isterse ne olacak? Olamaz mı? Olur tabii ki... Sistemin mimarları buna karşı nasıl önlemler almış ona bir göz atalım şimdi.*

Bu sorulardan yalnızca ilkine bir önceki yazımızda cevap verdik. Şimdi diğer soruların cevaplarını anlamak için bu sistem Blockchain'e nasıl uyarlanmış ona bakalım: 


### Blockchain nasıl çözüm bulmuş bu sorulara?

Bitcoin'in de içinde bulunduğu Blockchain bazlı sistemlerde de aynı şekilde, makinelerin doğru mesajı verdiğini, arada bir hainin yanlış bilgiyi etrafa verip vermediğini nasıl anlayabiliriz? 


#### Kısa hatırlatma: Blockchain nasıl çalışıyordu?

Efendim bunu anlayabilmek için öncelikle [Bitcoin şifrelemesi](http://ademimerkezi.com/genel/2018/05/08/Peki-Blockchain-sifrelemesi-nasil-calisiyor.html) ile ilgili yazıyı hatırlamakta fayda var. 

Kısaca tekrar etmek gerekirse: Bitcoin ile yapılmış işlemleri sistemdeki bütün makineler bir araya toplayıp kendi defterlerine yazıyorlar.  Sonra da bu işlemleri toplayıp balya haline getiriyorlar (yani madencilik "mining" yapıyorlar)

Peki nasıl bir işlem yapıyordu bu makineler? Hatırlarsanız bahsetmiştik daha önce: Yaptıkları aslında önce üç bilgiyi bir araya getirmek
1. en son yapılmış balyanın sonucunu al,
2. sonra son on dakikada yapılmış bütün işlemleri ekle
3. bir de eğer sonucu kazanırsan kendine bir ödül olacak (hani şu 50 Bitcoin ile başlayan ve şimdilerde 12.5 Bitcoin'e düşmüş olan), o ödülü de yaratılmış gibi ekle. 

Sonra bu üç bilgiyi kullanarak sistemin sorduğu bulmacayı çözmeye çalışmak. Bu yaklaşık on dakika süren bir çalışma (Nasıl bir bulmaca bu derseniz detayları bu kısmın başında bahsettiğimiz [yazımızda](http://ademimerkezi.com/genel/2018/05/08/Peki-Blockchain-sifrelemesi-nasil-calisiyor.html) bulabilirsiniz). 

Binlerce makine soruyu çözmeye çalışır ve bunun için de ciddi bir enerji harcar. Çözen makine anında bulmaca sonucunu tüm sisteme yayar. Bilgiyi alan diğer makineler de yukarıdaki üç bilgiyi bir araya getirip sonucu kontrol ederler (bulmacayı çözmek zor ama çözülmüş sonucu kontrol etmek çok basit). 

Kontrolün sonunda sonucun doğruluğuna emin oldukları anda sistemdeki bütün makineler bu kazananın sonucunu alıp, yeni balyaya başlar ve yukarıdaki işlemleri tekrar edip yeni bulmacayı çözmeye girişirler. Çoğunluğun üzerinde çalıştığı balya en uzun balya olarak takip edilen zincir olur. 

#### Blockchain üzerinde uzlaşma nasıl oluyor?

İşte bu makinelerin Mutabakat Mekanizması. Bizans Hata Toleransı'nın Blockchain'e uyarlanmış hali. Blockchain yukarıdaki Mutabakat Mekanizması'nı kullanarak, en son yapılan balya sonucunu kimin belirleyeceği (yani bir sonraki akında generalin kim olacağı) konusunda mutabakat sağlıyor. İşte buna Bitcoin özelinde Proof-of-Work deniyor.



### Peki bu sistem çok maliyetli değil mi?

Biliyorsunuz Blockchain üzerindeki en bilinen iki sistem Bitcoin ve Ethereum halka açık. Bu şu demek: İsteyen her makine sisteme katılabilir. Ancak sisteme katılabilmek için enerji harcaman lazım. Eğer harcadığın enerji sonrası doğru işlem yaparsan çıkan sonuçtan ödül kazanmaya hakkın var.  

Eğer bu makineler herhangi bir şekilde yukarıdaki gibi enerji harcayacakları bir çalışma içine girmeden ilerleme imkanına sahip olsalardı, o zaman kötü niyetli bir grup, sisteme olabildiğince makine sokup, manipüle edebilirdi. Halbuki belli bir maliyet olması ve sistemde çok fazla katılımcı olması nedeniyle bu çok maliyetli bir manipülasyon. 

O nedenle "Bitcoin çok enerji harcadı, Bitcoin Sırbistan kadar enerji harcıyor, boşa israf" gibi sözler doğru, ancak işin doğasında var bu. Bitcoin sisteminin yaptığı bu kadar enerji harcayarak kendisini dış tehditlere karşı korunaklı hale getirmek. Bunu boşa bir harcama değil bir güvenlik harcaması gibi düşünün. Kurulduğu 2009 yılından bu yana bir kez bile teklemeyen ve her tür dış tehdidi bertaraf etmiş olmanın bedeli...

### Diğer sorular:

Peki ya istisnalar olamaz mı? Olabilir. Bakalım ne olabilir ve çözümü var mı?

* Örneğin, bir bulmacayı aynı anda iki makine çözerse ne olur? Bilgisayarlardan bahsettiğimiz için bu durum söz konusu değil. Milisaniye de olsa bir makine diğerinden önce çözer...

* İyi de bir makine diğerinden 1 milisaniye sonra çözse bulmacayı ve her iki makine de sisteme kendi sonuçlarını verseler?. Sistemdeki oyunculardan bir kısmı bir makinenin sonucunu diğerleri ise diğerinin sonucunu önce aldılar (bu olabilir, sonuçta kablolar aracılığıyla dünyanın dört bir ucuna yayılan mesajlardan bahsediyoruz). Dikkat edin, sonuçlar farklı çıkacak çünkü yukarıda yazdığımız üçüncü maddedeki ödülü her iki makine de kendisi için yazdı ve o bilgiyi bulmacaya soktu.  Bu durumda sistem ve makineler, en uzun balya (zincir) mantığı ile çalışıyor. İki farklı dal ürüyor ve makineler ya birini ya ötekini seçiyor. Nihayetinde makineler bu dallardan birine doğru evrilmeye başlıyorlar ve o dal ana zincir haline geliyor, diğer daldaki makineler de o dalı bırakıp çoğunluğun olduğu bu dala geliyorlar (bulundukları dalı "öksüz" - orphan- bırakıyorlar)

* Peki ya bir makine araya sahte bir işlem sokarsa, ona göre bulmacayı çözerse ve bunu dağıtmaya başlarsa? O zaman, yukarıdaki ikinci maddede yazdığı gibi, diğer makineler sahte işlemi aldıkları anda o işlem kendilerinde olmadığı için bu makinenin yazdığı sonucu kabul etmezler. Bu dediğimiz senaryonun tek istisnası, eğer bir gün bir grup tüm işlem gücünün %51'ini ele geçirir ve içeri bir sahte işlem sokup ondan sonra bu işlemi sistemdeki makinelerin çoğunluğuna doğrulatır ise olabilir. Bu da çok ama çok büyük bir elektrik gücü harcaması demektir ve imkansız olmasa da çok ama çok güç bir durum. 

### Sonuç

"Nasıl oluyor da, kendilerine direktif veren bir yönetici olmadan birlikte hareket ediyor" dediğimiz binlerce makine, dışarıdan bakınca bilinmez ve karmaşık gelen ama içine girince matematiksel olarak planlanmış yukarıdaki sistemleri kullanarak Bitcoin örneğinde neredeyse on yıldır tıkır tıkır çalışıyorlar. Şu ana kadar bir sorun olmadı, olursa da teknoloji üzerine çalışanlar bir çözüm yolu bulurlar diye düşünmeden edemiyor insan... 


&nbsp;

---


&nbsp;


*Not: Yazdığımız 25+ yazının bir bütünlük içinde nelerden oluştuğuna bakmak isterseniz [Hakkımızda](http://ademimerkezi.com/about/) sayfasına göz atabilirsiniz.* 


