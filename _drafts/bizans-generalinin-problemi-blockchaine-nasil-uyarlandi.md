



Bir önceki yazımızda birbirinden bağımsız (dağıtık) ve çok da güvenmeyen oyuncuların nasıl uzlaşıp birlikte hareket ettiklerine bakmıştık. Kısaba bahsedersek, Bizans Hata Tolerans diye adlandırılan bir sistemi kullanan oyuncular, kendileri gelen mesajların içinde çoğunluğun söylediğ mesajı uygulayarak ilerliyorlar, böylece ortada kararsızlık söz konusu olmuyor idi. 

Peki Blockhain sistemine nasıl uyarlanıyor bu? Geçtiğimiz yazıda sorduğumuz soruları tekrar edelim: 


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


