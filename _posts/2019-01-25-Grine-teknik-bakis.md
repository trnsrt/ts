---
layout: post
title:  "Grin'e teknik bakış"
date:   2019-01-25 9:42:29 +0300
categories: Genel
---

Geçtiğimiz iki yazıda [önce](https://ademimerkezi.com/genel/2019/01/23/miblewimble-aranan-mahremiyet-buyusu-mu.html) MimbleWimble denen Harry Potter dünyası karakterlerinin hakim olduğu ve gizlilik konusunda yeni bir çığır açan bir teknolojiden bahsetmiş, [sonra](https://ademimerkezi.com/genel/2019/01/24/gelecegin-odeme-araci-grin-mi-olacak.html) da özellikle cypherpunk dünyasında heyecan yaratan MimbleWimble üzerine kurulu Grin parasına değinmiştik.  Bu iki yazıyı teknik altyapısı olmayanlara tavsiye edebiliriz. Eğer işin teknik olarak daha detayına girmek isterseniz, aşağıdaki yazı ilginizi çekebilir. 

### Gizlilik

Aslında MimbleWimble, Bitcoin'in üzerine kurulduğu teknolojiyi daha gizli hale getirmeye yarayan bir protokol. Ne kastediyoruz bakalım: 

MimbleWimble'da ne kullanıcılar ne de işlem miktarları görünecek. Nasıl olacak bu? 

#### Adres yok yaşasın cüzdanlar

Öncelikle sistemde paranın gidip geleceği hesaplar olmayacak. Bunun yerine cüzdanlar kullanılacak. 

Normalde Bitcoin sisteminde hesaptan para 'input' olarak sisteme girer, input karşılığı da aynı miktarda output çıkardı (bu output'a UTXO denirdi). Sistemdeki makinalar çıkan bu UTXO'ları toplar ve değişmediğini gördüklerinde "tamam" derlerdi "sistemde çifte harcama yapılmamış" (şu [yazımızda](https://ademimerkezi.com/genel/2018/11/30/bitcoin-islemi-nasil-gerceklesiyor.html) değinmiştik bu konuya)

Grin sisteminde ise input yok, çünkü input yaratacak adresler kullanılmıyor. Bunun yerine sistemde sadece output'lar yani UTXO'lar var. Bunlar da cüzdanlar aracılığı ile kullanılıyor. Sistem iki kullanıcının bir şekilde (on-line ya da off-line) kendi arasında ne tip bir işlem yapacağı konusunda iletişime geçip anlaşma yapması esasına dayanıyor. 

Örnek ile açıklayalım: Ayşe Bora'ya 100 Grin göndermek istiyorsa iki taraf kendi Özel Anahtarlarını kullanarak bir işlem yaratıyor. Biraz daha açalım: Ayşe bu işlemi başlatırken kendi Özel Anahtarı ile bir adres yaratır ve bunu Bora'ya gönderir. Bora'nın bu sırada online olmasına gerek yok. Bora Ayşe'nin gönderdiği işlemi kendi Özel Anahtarı ile şifreler. Sonrasında bu işlem sisteme girilir. Dolayısıyla sistem sadece iki kullanıcının kendi arasında anlaşarak bir işlem gerçekleştirdiğini görür. 

#### Blok içinde detay bilgi yok

Bütün işlemlerin biraraya getirildiği bloklarda da Bitcoin'de olduğu gibi işlemler tek tek görülmüyor. Bunun yerine bütün işlemlerin bir toplamı var - dolayısı ile kim ne işlem yaptı [görmek mümkün değil](https://blockonomi.com/grin-mimblewimble/). Benzer şekilde karıştırma/toplamayı CoinJoin denen bir işlem ile Bitcoin üzerinde ikinci bir katman olarak yapmak da mümkün. MimblewWimble CoinJoin'i kendi ana sisteminin bir parçası olarak kullanıyor.  

#### IP adresleri de gizleniyor

Bitcoin'de adresler belli olduğu için para nereden geldi, nereye gitti biliniyor. Bu nedenle kullanıcıları bir şekilde takip etmek ya da paranın izini sürmek mümkün oluyor. Çünkü Bitcoin'de bir işlem yaptığınızda bunu Bitcoin ağındaki bir makineye (düğüm-node) gönderiyorsunuz o da tüm sisteme yayıyor. İlk gönderilen node'un biliniyor olması, sizin genelde bu node'u kullanmanız gibi teknik nedenler, aslında bu parayı izi sürülebilir bir hale getiriyor.  

Mimblewimble da ise öyle değil. Burada gizlilik çözümü olarak dandelion adı verilen bir protokol kullanılıyor. (Dandelion kara hindiba çiçeği demek, bu çiçeğin özelliği açmadan önce tek bir sap ve yapraktan oluşup açtıktan sonra serpilmesi). MW'de siz sisteme bir işlem gönderdiğinizde bunu alan makine rastgele bir başka makineye gönderiyor, o bir başkasına ve böyle böyle ilk gönderen makinanın izinin sürülemeyeceği bir "bozma (fluff)" sürecinden geçiliyor. 


### Basitlik/Hafiflik

#### Tam güncelleme vs kısmi güncellemeye

Bitcoin sisteminin teknik olarak sıkıntılarından biri sistem içindeki makinelerin (node-düğüm) işlemleri teyid etmek için kendi içlerinde tüm blockchain sistemini tutuyor olmaları. Bu data şu anda [200 GB civarında ve giderek artıyor](https://www.blockchain.com/en/charts/blocks-size) . Herhangi bir bilgisayarın sisteme girmesi için bu datayı yüklemesi oldukça uzun bir zaman. 

Grin sisteminde, bir bilgisayar tüm bu datayı tutmak yerine fast sink denen bir metod ile son 2000 bloğu güncelleme (sync) yaparak dakikalar içinde sistemi kullanabilir hale geliyor. 

#### Gizlilik vs hafiflik (ve dolayısıyla ölçeklenmeye)

Gizlilik aslında ölçeklendirme ile çelişkili bir kavram. Neden? Çünkü ne kadar gizlilik isterseniz o kadar işin içine şifreleme mekanizmaları giriyor. Ne kadar şifreleme mekanizması koyarsanız sistem üzerinde saklayacağınız bilgiyi o kadar artırıyorsunuz. Bu da sistemin ağırlaşmasına neden oluyor. Özellikle sistemi büyütmek ve geniş kitlelere yaymak istediğinizde ölçeklendirme (scaling) problemi yaşar hale geliyorsunuz. 

#### Hız vs fonksiyon

Bunun yanında Grin'in Bitcoin'e göre önemli bir eksikliği içinde ayrı kod yazımına (scripting) izin vermemesi. Bitcoin'i genelde para transferi için kullanıyoruz ama aslında herhangi bir dijital varlık ya da bilginin transferi için de kullanabiliriz. Bunu sağlayan içindeki scripting mekanizması. Ancak bu fonksiyon aynı zamanda ekstra yük getirip blokların büyüklüğünün artmasına ve sisteme yük bindirmesine yol açıyor. 

Grin bu tip scripting mekanizması içermiyor. İşe yaradığı tek alan para transferi. Kendisini ödeme aracı olarak konumlandırdığı için daha hızlı olabilmek adına böyle bir farklılaşmaya gitmiş Grin yazılımcıları. 

### Uzlaşma Mekanizması

Aslında MimbleWimble teknik altyapı olarak Bitcoin'e oldukça benziyor. 

Örneğin, aynı Bitcoin gibi uzlaşma mekanizması olarak makinelerin enerji kullanması prensibinden hareket eden Proof-of-Work mekanizmasını kullanıyor (PoW'yi anlatan detaylı yazımız [burada](https://ademimerkezi.com/genel/2018/11/01/Bitcoin-uzlasmasi-proof-of-work.html)). 

Grin'in kullandığı PoW versiyonunun adı [Cuckoo Cycle](https://medium.com/codechain/cuckoo-cycle-c337e30c6c99). Bu versiyonun özelliği Bitcoin sistemini domine etmeye başlayan ASIC tipi madencilik yapan ihtisas makinelerinin etkisini azaltmak. Grin başlangıçta ASIC resistant denen sistemi kullanarak olabildiğince küçük bireysel madencinin sistemin içinde olmasını istiyor. Ancak uzun vadede bunun beyhude bir çaba olduğunu düşünüyorlar ve kademeli olarak ASIC tipi makinelerin de sisteme girmesine izin verecekler. 

### Öğütme (Hashing)

Aynı zamanda Grin içindeki işlemleri gerçekleştirirken kullanılacak öğütme mekanizmasının, ileride çok kuvvetli makinalar (quantum computers) tarafından kırılacağı iddia edilen bitcoin mekanizmalarına benzer akibeti yaşamamak için 'quantum resistant' denen çok güçlü mekanizmalar olması planlanıyor. 


### Bloklama ve zorluk dereceleri

Bitcoin sistemi içindeki madencilere sorduğu soruların zorluk derecesini iki haftada bir ayarlıyor. Bu zorluk ayarlamasını yaparken bulmacanın çözülme hızına bakıyor ve hızlı yani 10 dakikadan çabuk çözülüyor ise zorlaştırıyor eğer 10 dakikadan uzun sürüyor ise kolaylaştırıyor. Grin bu zorluk ayarlamasını çok daha hızlı bir şekilde yapacak. Aynı Bitcoin sonrası çıkan başka pek çok Blockchain sisteminin yaptığı gibi 

Bitcoin sisteminde işlemler 10 dakikada bir toplanıp blok oluşturulurken Grin'de bu dakikada bir olacak. Bitcoin şu anda 10 dakikalık blok oluşturma sonrası 12.5 BTC ödül verirken Grin dakikada bir 60 Grin verecek. Grin'de Bitcoin'de dört yılda bir yaşanan azalma da yok, dolayısı ile ileride eğer devam ederse piyasada bol miktarda Grin olacak. 

### Grin neden Lightning gibi Bitcoin üzerine kurulan ikinci bir katman değil de ayrı bir para?

Peki MimbleWimble bir protokol olarak Lightning Network gibi Bitcoin üzerine ikinci bir katman olarak uyarlanamaz mıydı? Ayrı bir paraya ihtiyaç var mıydı? Buna teknik olarak verilen cevap ikinci bir katman olarak yapılacak bir yazılımın geriye dönük olarak da uyumlu olması için çok fazla çalışma gerekeceği. Yine de çok tatmin edici bir açıklama değil. 

Bir neden bir kısım Bitcoin geliştiricisinin yarın öbür gün Bitcoin'in başına bir 'şey' gelmesi (teknik konular vb) halinde kendilerine bir B planı aramasın ve Grin'in de bu alana önemli bir aday olarak görmeleri. 

Bir başka neden de Bitcoin'in artık genel kabul gören ciddi bir yapı olması nedeniyle üzerine yapılan değişikliklerin çok yavaş olması. Grin yeni bir teknoloji olduğu için (Rust dilinde yazılıyor) hızlı gelişime imkan veren bir yapısı var. 

### Sorunları sıkıntıları

Grin'in izleyeceği enflasyon yaratan para politikası aslında gelecekte fiyatının çok değerlenmesinin önündeki en büyük engellerden. Peki neden böyle bir para politikası izliyor Grin?

1. Bitcoin'in azalan emisyon özelliği nedeniyle para ödeme aracı değil değer saklama aracı olarak kullanıldığı düşünülüyor. Grin sürekli olarak bir supply yaratarak ödeme aracı olarak kullanılmak istiyor
2. Bitcoin örneğinde ilk madenciler sonrasındaki ciddi değer yükselmesinden dolayı inanılmaz paralar kazandılar (satoshinin kullanmasa bile [1 milyon BTC'si olduğu biliniyor](http://time.com/money/5002378/bitcoin-creator-nakamoto-billionaire/)). Grin, daha 'adil' bir dağıtım süreci öngörüyor ve kendi emisyon hacimlerinin altına benzeyeceğini iddia ediyor. Grafik bu söylemi doğruluyor. 

&nbsp;

| ![btc-gold-grin-800.png](/assets/btc-gold-grin-800.png) | 
|:--:| 
| *Bitcoin, Altın ve Grin emisyon hacimleri % olarak [Kaynak](https://plot.ly/~Bobby_Digital/1/#/)* |

&nbsp;

İşlemlere hız katmak amacıyla scripting özelliğini yok etmesi ileride Grin'in sadece para transferi için kullanılacak bir araç olarak fonksiyonlarında sınırlamalar yaratabilir. Ancak üzerine inşaa edilebilecek ikinci seviye katmanlar ve ek yazılımlar ile bu sorun giderilebilir gibi görünüyor. 


### Sonuç

Tekrar hatırlatalım. Serimizin MimbleWimble'ı anlatan ilk yazısına [buradan](https://ademimerkezi.com/genel/2019/01/23/miblewimble-aranan-mahremiyet-buyusu-mu.html), Grin üzerine yoğunlaşan ikinci yazısına [buradan](https://ademimerkezi.com/genel/2019/01/24/gelecegin-odeme-araci-grin-mi-olacak.html) ulaşabilirsiniz. 

Teknik olarak Grin, yıllardır Bitcoin geliştiricilerinin yaşadıkları sıkıntılara çözüm bulma amacı taşıyan, gizlilik özellikleri ile diğer KriptoParalar'a benzeyen, basitliği ile geleceğin ödeme aracı olmayı planlayan yeni bir para. Teknik olarak kuvvetli bir kökten geliyor. Bakalım uzun vadede bu kök kuvvetli bir ağaç yeşermesine olanak verecek mi?
