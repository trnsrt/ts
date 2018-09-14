

Geçtiğimiz iki yazıda, birbirinden bağımsız olan ve Blockchain sisteminde aktif rol oynayan oyuncuların nasıl olup da birlikte hareket ettiklerinin üzerinden geçmiştik. Önce işin sistematiği (mantığı) nasıl çalışıyor sorusunu geçmişte ortaya çıkmış birbirine güvenmeyen Bizans Generalleri'nin düşmana karşı nasıl ortak hareket ettiğine bakmış, sonra da bu problemin Blockchain özelinde nasıl çözüldüğüne göz atmıştık. 

### Bitcoin'in meşhur ettiği Proof-of-Work

Tabii, Blockchain bazlı dağıtık sistemlerin en meşhuru olan Bitcoin üzerinde bu ortak hareket etme mekanizması olan Proof-of-Work (pOW)  sistemini anlatırken, bunun aslında çok enerji harcayan bir süreç olduğundan bahsetmiştik. Olaylara maalesef yüzeysel olarak bakan medya, bunu "[Bitcoin 159 ülkeden fazla enerji harcıyor](https://www.cnnturk.com/ekonomi/kripto-para/bitcoin-islemleri-159-ulkeden-fazla-enerji-tuketiyor)" ya da "[İzlanda finans bakanı Bitcoin'in ülkede yerleşim bölgelerindekinden fazla tüketimi olduğu konusunda uyarıda bulundu](https://www.wired.co.uk/article/bitcoin-mining-energy-consumption-new-york)" gibi başlıklar ile veriyor. Hakikaten nedir derseniz, [şu yazıda](https://www.ofnumbers.com/2018/08/26/how-much-electricity-is-consumed-by-bitcoin-bitcoin-cash-ethereum-litecoin-and-monero/#footnote_0_5656) detayları var. Özeti: Bitcoin [elektrik harcaması olarak dünyada 37. sıradaki Avusturya'dan daha fazla ](http://www.wikizero.co/index.php?q=aHR0cHM6Ly9lbi53aWtpcGVkaWEub3JnL3dpa2kvTGlzdF9vZl9jb3VudHJpZXNfYnlfZWxlY3RyaWNpdHlfY29uc3VtcHRpb24).  


Bitcoin'in sadık kullanıcıları böyle bir enerji harcamanın uzlaşma mekanizmasının işlemesi için değil ama bu işleyen mekanizmanın dışarıdan sistemi bozmak isteyecek bir tehdite karşı kendini savunma mekanizması olduğunu belirtiyorlar. Zira, uzlaşma mekanizmasının kilit noktası sistem üzerindeki parçaların %51'inin ortak bir kabul üzerinden ilerlemesi şeklinde. Nedir bu kabul? Son 10 dakikada gerçekleşen işlemlerin herkeste aynı şekilde tutulması, tutarlı ve aynı olması. 

Eğer sistemin %51'ini ele geçirmek sadece etrafa makine kurmak ve sisteme bağlanmak ile olsaydı (hatırlarsanız kimseye sormadan Blockchain sistemine bağlanıp siz de bir oyuncu olabilirsiniz), o zaman elinin altında (ya da kullanabileceği) büyük bir makine kapasitesi olan biri sistemi ele geçirebilirdi. Halbuki, Bitcoin'in oyunculara sorduğu bilmeceyi çözmek için ciddi bir enerji harcamak gerekiyor. Sistemi ele geçirmek isteyen "dış tehdit" için oldukça maliyetli bir durum bu. 

Bitcoin dışında aslında Bitcoin'in küçük kardeşleri diğer alternatif KriptoParalar'ın bir çoğu da PoW mekanizması kullanıyor. Ethereum (ki değiştirmek için çalışıyor, bir sonraki bölümde detaylandıracağız), Litecoin, Monero gibi bütün büyük Bitcoin alternatifleri de PoW kullanıyor.

Peki bu kadar enerji harcamaya gerek var mı? Başka başka yöntemlerle de makinelerin ortak hareket etmesi sağlanamaz mı? Bu konuda kafa yoranlar var tabii. Onların geliştirdiği alternatifler de var. İsterseniz kısaca bir göz atalım onlara. 

### Proof-of-Stake (PoS)

Proof-of-Stake yukarıda bahsettiğimiz Bitcoin'in Proof-of-Work mekanizmasına en ciddi rakip. 

Farkını anlatmak için PoW'nun ne yaptığını tekrar hatırlatalım. Siz eğer Bitcoin'i bozmak gibi bir çabaya girerseniz, tüm Bitcoin'in %51'ini ele geçirecek kadar yatırım ve enerji harcamadıkça yaptığınız çaba sonuçsuz kalır, ve yaptığınız tüm masraf boşa gider. Zira sistemin oyuncuları, sizin istediğinizi değil çoğunluğun yolunda giderler, siz de yaptığınız masraf ile geride kalırsınız. 

O zaman şöyle bir soru soruyor diğerleri: İyi çok güzel, bu tip mekanizma kurarak dış tehditleri önlüyorsunuz ama öte yandan iyi niyetli mevcut oyuncular da aynı şekilde bulmaca çözmek zorundalar ((Bitcoin kazanmak için gerekli çünkü), ve bu nedenle ortaya çok büyük bir enerji harcaması çıkıyor. Sistemi manipüle edecek birine çok maliyet getirecek ama düzgün çalışan uyumlu oyunculara masraf çıkarmayacak dolayısıyla büyük "israflar" oluşmayacak bir çözüm bulunamaz mı?

PoS işte bunun cevabını şu şekilde veriyor. Yapılan işlemlerin teyidi için bir bulmaca çözüp enerji harcamayalım onun yerine doğru olduğunu düşündüğümüz işlem listesi için elimizdeki tüm parasal değeri rehin olarak verelim. Elimizi taşın altına koyalım yani. Ne kadar çok varlık rehin edersek, sonundaki ödülü kazanmadaki şansımız da o kadar artsın. Eğer sistemi bozmaya çalışan bir dış tehdit isek, (ve eğer çoğunluğa sahip olamazsak) yaptığımız manipülasyon nihai olarak sonuçsuz kalacak ve ceza olarak sistem bizim tüm varlığımızı sıfırlayacak - sıkı bir caydırma durumu.. 

### Proof-of-Elapsed-Time (POET)

### Delegated-Proof-of-Stake (DPos)

### Leased-Proof-of-Stake (LPos)

### PracticalByzantineFaultTolerance (PBFT)

### SimplifiedByzantineFaultTolerance (SBFT)

### DeligatedByzantineFaultTolerance (DBFT)

### DirectedAcyclicGraphs (DAG)

### ProofofActivity (#POA)

### ProofofImportance (#POI) 

### ProofofCapacity (#PoC)

### ProofofBurn (#PoB)




### Hashgraph Protocol








Yeni teknolojiler ile ilgili hep söylediğimizi tekrar edelim. Bu tip teknolojilerin olgunlaşması zaman alıyor ama güzel tarafı, herhangi bir sistemde bir eksiklik görüldüğünde (ya da hissedildiğinde) hemen birilerin onun üzerinde çalışmaya başlıyorlar. Hatta eksiklik bir demeyelim "daha verimli, daha kolay" bir çözüm arayışı sürekli var. Bu da aslında bu sistemlerin gücü. Zira sürekli bir ilerleme ve gelişme var. Kırk yıldır kullanılan eski sistemlere göre ne kadar büyük bir rahatlık düşünsenize.. 











Not: Aslında enerji harcamanın dış tehditlere karşı korumak dışında önemli bir işlevi de var. "Para nedir, neden para değerli olur ya da değersizleşir?" sorularına yanıt ararken tarih boyunca gelişen örneklere baktığımızda, genelde iki önemli konu var. Birincisi, insanların elinde ne kadar para var. İkincisi, yeni ne kadar para yaratılabilir. Bu ikisi bir paranın değerini belirliyor. Neden? Çünkü insanlar belirsizlik sevmiyorlar - özellikle para ile ilgili konularda. Gelecekte de ellerindeki paranın kullanılabileceğini ve değerini koruyabileceğini bilmek istiyorlar. Bitcoin kendi içindeki mantığı gereği ne kadar stoğu olduğunu ve ne kadar daha yaratılacağını da tam olarak hesaplayabildiğimiz bir para. Bu da onu insanların gözünde değerli hale getiriyor. 
