
---
layout: post
title:  "Bitcoin Uzlaşması Proof of Work"
date:   2018-11-01 10:03:34 +0300
categories: Genel
---

Geçtiğimiz iki yazıda, birbirinden bağımsız olan ve Blockchain sisteminde aktif rol oynayan oyuncuların nasıl olup da birlikte hareket ettiklerinin üzerinden geçmiştik. Önce işin sistematiği (mantığı) nasıl çalışıyor sorusunu geçmişte ortaya çıkmış birbirine güvenmeyen Bizans Generalleri'nin düşmana karşı nasıl ortak hareket ettiğine bakmış, sonra da bu problemin Blockchain özelinde nasıl çözüldüğüne göz atmıştık. 

Geçtiğimiz günlerde Ekim ayının sonunda 10. yılını kutladığımız Bitcoin'in yaratıcısı Satoshi Nakamoto'yu bir kez daha analım ve yaptığı devrim niteliğindeki yeniliğe bir kez daha dikkat çekelim.

### İşin özü

Bilmemiz gereken kritik nokta şu: Meşhur Satoshi Nakamoto aslında üç parçayı bir araya getirdi. Bu parçalardan ikisi zaten ortada idi. Satoshi, üçüncü kritik parçayı geliştirdi ve bu üç parçanın birbirleri ile sağlam ve durdurulamaz şekilde çalışmasını sağladı. Neydi bu üç parça?

Birincisi, internet. Internet sayesinde birbirinde uzakta ve bağımsız makineler birbirleri ile bağlantı kurabildiler. İkincisi ise şifreleme. Bu dağınık dünyadaki farklı parçaların birbiri ile güvenli iletişimi için Şifreleme (Kriptografi) geliştirildi. 

Bu ilk iki nokta zaten yaklaşık 20-30 yıllık bir süreç içinde geliştirilmişti. Eksik olan bu birbirinden uzakta makinelerin ortada bir aracı olmadan nasıl birlikte çalışacağı ve bu şekilde çalışabilmek için nasıl motive edilecekleri (ve nasıl ortak karara varacaklarını) idi. 

Satoshi Bitcoin adını verdiği fikrinde kurduğu sistemin altyapını işletecek oyuncuların bir arada çalışmasını sağlayan bir teşvik sistemi kurdu. İşte bu daha önce yapılmamış olan bulmacadaki eksik son parça idi. Nasıl dağınık yapıdaki parçalar ortada bir aracı olmadan bir arada çalışabilir - işte Bitcoin bu sorunu çözdü ve aracıya olan ihtiyacı kaldırdı.  Bu sayede Satoshi, herhangi bir otoritenin uhdesinde olmadan kendi kendine çalışan, dış tehditlere karşı kendini koruyan ve on yıldır sarsılmadan ayakta duran bir dijital para yarattı,

Bu üçüncü parçadan biraz daha bahsedelim. Nedir ona bakalım, başka ne tip alternatifleri var onlara da göz gezdirelim. 


### Bitcoin'in meşhur ettiği Proof-of-Work


![bitcoin-uzlasma.gif](/assets/bitcoin-uzlasma.gif)


Proof-of-Work (PoW) işte bu makinelerin nasıl çalışacağını (sisteme nasıl gireceğini ve sistemde iken neler yapması gerektiğini) belirleyen kurallar. Parçalar sistemin içindeyken de birlikte uyumlu bir şekilde çalışmaları gerek, bu da izledikleri bir uzlaşma mekanizması sayesinde oluyor. Nasıl bir mekanizma bu? Bu bahsettiğimiz parçaların, o an için oluşan Blockchain zincirlerinden en uzununa doğru evrilmesi ve o zincir üzerinde mutabakat sağlanması. Bunun otomatik olması ve bir aracıya ihtiyaç duyulmaması. 

Tabii, Blockchain bazlı dağıtık sistemlerin en meşhuru olan Bitcoin üzerinde bu ortak hareket etme temellerini belirleyen PoW sistemini anlatırken, bunun aslında çok enerji harcayan bir süreç olduğundan bahsetmiştik. Olaylara maalesef yüzeysel olarak bakan medya, bunu "[Bitcoin 159 ülkeden fazla enerji harcıyor](https://www.cnnturk.com/ekonomi/kripto-para/bitcoin-islemleri-159-ulkeden-fazla-enerji-tuketiyor)" ya da "[İzlanda finans bakanı Bitcoin'in ülkede yerleşim bölgelerindekinden fazla tüketimi olduğu konusunda uyarıda bulundu](https://www.wired.co.uk/article/bitcoin-mining-energy-consumption-new-york)" gibi başlıklar ile veriyor. Hakikaten nedir derseniz, [şu yazıda](https://www.ofnumbers.com/2018/08/26/how-much-electricity-is-consumed-by-bitcoin-bitcoin-cash-ethereum-litecoin-and-monero/#footnote_0_5656) detayları var. Özeti: Bitcoin [elektrik harcaması olarak dünyada 37. sıradaki Avusturya'dan daha fazla ](http://www.wikizero.co/index.php?q=aHR0cHM6Ly9lbi53aWtpcGVkaWEub3JnL3dpa2kvTGlzdF9vZl9jb3VudHJpZXNfYnlfZWxlY3RyaWNpdHlfY29uc3VtcHRpb24).  

Bitcoin'in sadık kullanıcıları böyle bir enerji harcamanın uzlaşma mekanizmasının işlemesi için değil ama bu işleyen mekanizmanın dışarıdan sistemi bozmak isteyecek bir tehdite karşı kendini savunma mekanizması olduğunu belirtiyorlar. Zira, uzlaşma mekanizmasının kilit noktası sistem üzerindeki parçaların %51'inin ortak bir kabul üzerinden ilerlemesi şeklinde. Nedir bu kabul? Son 10 dakikada gerçekleşen işlemlerin herkeste aynı şekilde tutulması, tutarlı ve aynı olması. 

Eğer sistemin %51'ini ele geçirmek sadece etrafa makine kurmak ve sisteme bağlanmak ile olsaydı (hatırlarsanız kimseye sormadan Blockchain sistemine bağlanıp siz de bir oyuncu olabilirsiniz), o zaman elinin altında (ya da kullanabileceği) büyük bir makine kapasitesi olan biri sistemi ele geçirebilirdi. Halbuki, Bitcoin'in oyunculara sorduğu bilmeceyi çözmek için ciddi bir enerji harcamak gerekiyor. Sistemi ele geçirmek isteyen "dış tehdit" için oldukça maliyetli bir durum bu. 

Bitcoin dışında aslında Bitcoin'in küçük kardeşleri diğer alternatif KriptoParalar'ın bir çoğu da PoW mekanizması kullanıyor. Ethereum (ki değiştirmek için çalışıyor), Litecoin, Monero gibi bütün büyük Bitcoin alternatifleri de PoW kullanıyor.

### Arkası yarın

Peki bu kadar enerji harcamaya gerek var mı? Başka başka yöntemlerle de makinelerin ortak hareket etmesi sağlanamaz mı? Bu konuda kafa yoranlar var tabii. Onların geliştirdiği alternatifler de var. İsterseniz bir sonraki yazıda da ona bir göz atalım. 
