

Geçtiğimiz iki yazıda, birbirinden bağımsız olan ve Blockchain sisteminde aktif rol oynayan oyuncuların nasıl olup da birlikte hareket ettiklerinin üzerinden geçmiştik. Önce işin sistematiği (mantığı) nasıl çalışıyor sorusunu geçmişte ortaya çıkmış birbirine güvenmeyen Bizans Generalleri'nin düşmana karşı nasıl ortak hareket ettiğine bakmış, sonra da bu problemin Blockchain özelinde nasıl çözüldüğüne göz atmıştık. 

Geçtiğimiz günlerde Ekim ayının sonunda 10. yılını kutladığımız Bitcoin'in yaratıcısı Satoshi Nakamoto'yu bir kez daha analım ve yaptığı devrim niteliğindeki yeniliğe bir kez daha dikkat çekelim.

### İşin özü

Bilmemiz gereken kritik nokta şu: Meşhur Satoshi Nakamoto aslında üç parçayı bir araya getirdi. Bu parçalardan ikisi zaten ortada idi. Satoshi, üçüncü kritik parçayı geliştirdi ve bu üç parçanın birbirleri ile sağlam ve durdurulamaz şekilde çalışmasını sağladı. Neydi bu üç parça?

Birincisi, internet. Internet sayesinde birbirinde uzakta ve bağımsız makineler birbirleri ile bağlantı kurabildiler. İkincisi ise şifreleme. Bu dağınık dünyadaki farklı parçaların birbiri ile güvenli iletişimi için Şifreleme (Kriptografi) geliştirildi. 

Bu ilk iki nokta zaten yaklaşık 20-30 yıllık bir süreç içinde geliştirilmişti. Eksik olan bu birbirinden uzakta makinelerin ortada bir aracı olmadan nasıl birlikte çalışacağı ve bu şekilde çalışabilmek için nasıl motive edilecekleri (ve nasıl ortak karara varacaklarını) idi. 

Satoshi Bitcoin adını verdiği fikrinde kurduğu sistemin altyapını işletecek oyuncuların bir arada çalışmasını sağlayan bir teşvik sistemi kurdu. İşte bu daha önce yapılmamış olan bulmacadaki eksik son parça idi. Nasıl dağınık yapıdaki parçalar ortada bir aracı olmadan bir arada çalışabilir - işte Bitcoin bu sorunu çözdü ve aracıya olan ihtiyacı kaldırdı.  Bu sayede Satoshi, herhangi bir otoritenin uhdesinde olmadan kendi kendine çalışan, dış tehditlere karşı kendini koruyan ve on yıldır sarsılmadan ayakta duran bir dijital para yarattı,

Bu üçüncü parçadan biraz daha bahsedelim. Nedir ona bakalım, başka ne tip alternatifleri var onlara da göz gezdirelim. 


### Bitcoin'in meşhur ettiği Proof-of-Work

Proof-of-Work (POW) işte bu parçaların nasıl çalışacağını (sisteme nasıl gireceğini ve neler yapması gerektiğini) belirleyen kurallar. O nedenle önemli. Konsensus mekanizmasının çalışması ise, bu bahsettiğimiz makinelerin bu POW'ye göre sistemi girip birlikte çalışıp, o an için oluşan Blockchain zincirlerinden en uzununa doğru evrilmesi, o zincir üzerinde mutabakat sağlanması. Bunun otomatik olması, ve bir aracıya ihtiyaç duyulmaması. 

Tabii, Blockchain bazlı dağıtık sistemlerin en meşhuru olan Bitcoin üzerinde bu ortak hareket etme temellerini belirleyen olan Proof-of-Work (pOW)  sistemini anlatırken, bunun aslında çok enerji harcayan bir süreç olduğundan bahsetmiştik. Olaylara maalesef yüzeysel olarak bakan medya, bunu "[Bitcoin 159 ülkeden fazla enerji harcıyor](https://www.cnnturk.com/ekonomi/kripto-para/bitcoin-islemleri-159-ulkeden-fazla-enerji-tuketiyor)" ya da "[İzlanda finans bakanı Bitcoin'in ülkede yerleşim bölgelerindekinden fazla tüketimi olduğu konusunda uyarıda bulundu](https://www.wired.co.uk/article/bitcoin-mining-energy-consumption-new-york)" gibi başlıklar ile veriyor. Hakikaten nedir derseniz, [şu yazıda](https://www.ofnumbers.com/2018/08/26/how-much-electricity-is-consumed-by-bitcoin-bitcoin-cash-ethereum-litecoin-and-monero/#footnote_0_5656) detayları var. Özeti: Bitcoin [elektrik harcaması olarak dünyada 37. sıradaki Avusturya'dan daha fazla ](http://www.wikizero.co/index.php?q=aHR0cHM6Ly9lbi53aWtpcGVkaWEub3JnL3dpa2kvTGlzdF9vZl9jb3VudHJpZXNfYnlfZWxlY3RyaWNpdHlfY29uc3VtcHRpb24).  

Bitcoin'in sadık kullanıcıları böyle bir enerji harcamanın uzlaşma mekanizmasının işlemesi için değil ama bu işleyen mekanizmanın dışarıdan sistemi bozmak isteyecek bir tehdite karşı kendini savunma mekanizması olduğunu belirtiyorlar. Zira, uzlaşma mekanizmasının kilit noktası sistem üzerindeki parçaların %51'inin ortak bir kabul üzerinden ilerlemesi şeklinde. Nedir bu kabul? Son 10 dakikada gerçekleşen işlemlerin herkeste aynı şekilde tutulması, tutarlı ve aynı olması. 

Eğer sistemin %51'ini ele geçirmek sadece etrafa makine kurmak ve sisteme bağlanmak ile olsaydı (hatırlarsanız kimseye sormadan Blockchain sistemine bağlanıp siz de bir oyuncu olabilirsiniz), o zaman elinin altında (ya da kullanabileceği) büyük bir makine kapasitesi olan biri sistemi ele geçirebilirdi. Halbuki, Bitcoin'in oyunculara sorduğu bilmeceyi çözmek için ciddi bir enerji harcamak gerekiyor. Sistemi ele geçirmek isteyen "dış tehdit" için oldukça maliyetli bir durum bu. 

Bitcoin dışında aslında Bitcoin'in küçük kardeşleri diğer alternatif KriptoParalar'ın bir çoğu da PoW mekanizması kullanıyor. Ethereum (ki değiştirmek için çalışıyor, bir sonraki bölümde detaylandıracağız), Litecoin, Monero gibi bütün büyük Bitcoin alternatifleri de PoW kullanıyor.

Peki bu kadar enerji harcamaya gerek var mı? Başka başka yöntemlerle de makinelerin ortak hareket etmesi sağlanamaz mı? Bu konuda kafa yoranlar var tabii. Onların geliştirdiği alternatifler de var. İsterseniz kısaca bir göz atalım onlara. 

### Proof-of-Stake (PoS)

Proof-of-Stake yukarıda bahsettiğimiz Bitcoin'in Proof-of-Work mekanizmasına en ciddi rakip. 

Farkını anlatmak için PoW'nun ne yaptığını tekrar hatırlatalım. Siz eğer Bitcoin'i bozmak gibi bir çabaya girerseniz, tüm Bitcoin'in %51'ini ele geçirecek kadar yatırım ve enerji harcamadıkça yaptığınız çaba sonuçsuz kalır ve yaptığınız tüm masraf boşa gider. Zira sistemin oyuncuları, sizin istediğinizi değil çoğunluğun yolunda giderler, siz de yaptığınız masraf ile geride kalırsınız. 

O zaman şöyle bir soru soruyor diğerleri: İyi çok güzel, bu tip mekanizma kurarak dış tehditleri önlüyorsunuz ama öte yandan iyi niyetli mevcut oyuncular da aynı şekilde bulmaca çözmek zorundalar ((Bitcoin kazanmak için gerekli çünkü), ve bu nedenle ortaya çok büyük bir enerji harcaması çıkıyor. Sistemi manipüle edecek birine çok maliyet getirecek ama düzgün çalışan uyumlu oyunculara masraf çıkarmayacak dolayısıyla büyük "israflar" oluşmayacak bir çözüm bulunamaz mı?

PoS işte bunun cevabını şu şekilde veriyor. Yapılan işlemlerin teyidi için bir bulmaca çözüp enerji harcamayalım onun yerine doğru olduğunu düşündüğümüz işlem listesi için elimizdeki tüm parasal değeri rehin olarak verelim. Elimizi taşın altına koyalım yani. Sistem de bu rehin edenler içinde birine piyango ile yeni blok yaratma ayrıcalığı versin. Ne kadar çok varlık rehin edersek, o kadar çok piyango biletimizin olsun ve sonundaki ödülü kazanmadaki şansımız da o kadar artsın. Ama eğer sistemi bozmaya çalışan bir dış tehdit isek, (ve eğer çoğunluğa sahip olamazsak) yaptığımız manipülasyon nihai olarak sonuçsuz kalacak ve ceza olarak sistem bizim tüm varlığımızı sıfırlayacak - sıkı bir caydırma durumu.

Bu konuda tartışmalar halen devam etmekte. Proof-of-Stake'i kullanacak olan Ethereum geliştiricileri konu üzerinde çalışmaya devam ediyorlar. Bunun dışında Cardano, OmiseGo, QTUM, Ardor PoS kullanıyorlar. Bir de PoS ile PoW'yi karışık şekilde kullananlar var (Decred, Dash, Stratis, HShare, Pivx gibi)

### Ve diğerleri:

Blockchain gibi değişik bazlı parçaların birbiri ile nasıl çalışacaklarına ilişkin çalışmalar sadece PoW ve PoS ile sınırlı değil tabii.. Teknoloji alanında bir sorun olduğunda onlarca çözüm ortaya çıkar.. Neler onlar derseniz, sadece isimlerini ve kimlerin kullandığını belirtelim: 

- Delegated-Proof-of-Stake (DPos) - BitShares, Steemit (sahipleri aynı bu ikisinin), EOS
- DeligatedByzantineFaultTolerance (DBFT) - NEO
- ProofofActivity (PoA) - Digital Note, Vechain
- ProofofCapacity (PoC) - Burstcoin
- ProofofBurn (PoB) - Slimcoin
- ProofofRun (PoR) - Runcoin
- ProofofAssignment - IOTW

ve diğerleri: DirectedAcyclicGraphs (DAG), ProofofImportance (POI), Proof-of-Elapsed-Time (POET), Leased-Proof-of-Stake (LPos), PracticalByzantineFaultTolerance (PBFT), SimplifiedByzantineFaultTolerance (SBFT)

### Sonuç

Yeni teknolojiler ile ilgili hep söylediğimizi tekrar edelim. Bu tip teknolojilerin olgunlaşması zaman alıyor ama güzel tarafı, herhangi bir sistemde bir eksiklik görüldüğünde (ya da hissedildiğinde) hemen birilerin onun üzerinde çalışmaya başlıyorlar. Hatta eksiklik bir demeyelim "daha verimli, daha kolay" bir çözüm arayışı sürekli var. Bu da aslında bu sistemlerin gücü. Zira sürekli bir ilerleme ve gelişme var. Kırk yıldır kullanılan eski sistemlere göre ne kadar büyük bir rahatlık düşünsenize.. 






