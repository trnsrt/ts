# Yazı II

Ethereum'un yeni hali ile ilgili olarak yorumları bir araya getirdiğimiz ilk yazımız sonrası, şimdi de işin derinine girmek isteyenler için  sisteme gelecek olan yeniliklerin üzerinden geçiyoruz. 

Geçtiğimiz yazıda, Ethereum'un yeni sisteminin getirdiği pek çok yenilik içinde temel olarak en önemli olanlarının, enerji tasarrufu sağlaması ve ölçeklenebilirlik olduğundan bahsetmiştik. Gelin şimdi bu iki önemli değişikliğe detaylıca bakalım: 

#### Sistem güvenliği (Pos) değişikliği
Enerji tasarrufu konusu gerek Bitcoin gerekse Ethereum'un zayıf karnı denebilir. Zamanında, Bitcoin tarafından başlatılan sonrasında Ethereum tarafından kopyalanan PoW (proof-of-work iş kanıtı) mekanizması, blokzincir üzerindeki güvenliğin sağlanabilmesi için sistemi yürüten onbinlerce makinenin belli bir enerji harcaması yapması esasına dayanıyor. Ethereum sonrası çıkan pek çok yeni blokzincir ise, bunun yerine PoS (proof-of-stake hisse kanıtı) başka bir mekanizma kullandılar. Bitcoin topluluğu felsefi olarak PoW'u bırakmayıp devam ederken Ethereum topluluğu bu PoS sistemini sevdi ve kendini o sisteme geçmek için hazırlamaya başladı. PoS sistemi sayesinde Ethereum'un enerji harcaması %99 oranında düşecek. Dolayısıyla bundan sonra bazı politikacıların kulaktan dolma bilgilerde çok sık kullandıkları 'ama blokzincir çok enerji harcıyor' argümanı ile bundan böyle sadece Bitcoin topluluğu muhatap olacak. 

Ethereum'da PoS'e geçiş sadece teoride kalmış değil, uzunca bir süredir pratik olarak yol almış durumda. PoW mekanizmasında sistemi yürüten madenciler, PoS'da yerlerini sisteme para kilitleyerek koruyacak olan onaylayıcılara bırakıyorlar. Aralık 2020'den itibaren PoS hazırlık olarak insanlar (ya da kurumlar) ellerindeki ETH'yi belli bir faiz oranı karşılığında rehin etmeye ve onaylayıcı olmaya başladılar. Şu ana kadar [11 milyon ETH](https://beaconcha.in/) yani [toplam dolaşımdaki ETH'nin](https://etherscan.io/stat/supply) %9.3'ü sisteme kilitlenmiş durumda. 

[ETH kililtlenen para miktarı]

Bu değişiklik aslında bakarsanız son aşamasında gelmiş durumda ve planlandığı gibi gidiyor. Asıl büyük değişimlerden geçen ve sancılı süreç diğer değişiklik olan ölçeklenebilme konusunda yaşandı.  

#### Ölçeklenebilme (Sharding)
Ethereum'un 2020 ve 2021 yıllarında yaşadığı yoğunluk sonrası işlem ücretleri arşa çıktı. Niye bu kadar büyük bir yoğunluk yaşandı? Yaşanan sorun hızlı bir şekilde çözülemez miydi? 

Sorunun arkasında yatan neden, blokzincirlerin aslında çok kısıtlı bir kapasiteye sahip olması. Daha önceki yazılarımızda da belirtmiştik, blokzincirler öyle çok üstün süpersonik teknolojiler değiller. Üstelik yapıları gereği çok verimli de çalışmıyorlar. Aslına bakarsanız evinizde kullandığınız son model bir bilgisayarın işlem gücü blokzincirin yapabileceğinden çok daha üstün. Neden blokzincire ihtiyaç duyuyoruz o zaman? 

##### Neden blokzincire ihtiyaç duyarız?
Blokzincir aslında bize çok da farklı bir hizmet sunuyor, o da 'kimseye güven duymak zorunda olmamak'. Blokzincirin yaptığı işi çok daha verimli olarak bir sunucuda duran bilgisayar ile yapabilirsiniz. Gayet de güzel olur. Sorun ne peki?  Sorun o bilgisayarın sahibinin kim olduğu ve içindekileri değiştirip değiştiremeyeceği. İşte blokzincir, kendi sisteminin birbirinden bağımsız binlerce makinede yürüterek herhangi bir kişi ya da kurumun sistemi kendi nüfuzu altına almasına engel oluyor. İyi de gerçekten ihtiyaç var mı buna? 

Bunu kestirmek oldukça zor. Gündelik hayatımızda bugün çok ihtiyaç duymayabiliriz, ama yarın her an durum değişebilir. İsterseniz, Donald Trump'a bir sorun bunu. Bir gecede Twitter'daki 80 milyon takipçisini kaybettiğinde 'sesini kaybetmiş' gibi hissetti mi? Ya da Facebook üzerine oyun geliştirip ekmek parası kazanmayı uman geliştiriciler bir gece ansızın aldıkları bir mesaj ile platformdan atılmaları durumunda neler yaşadılar acaba? Ya da Rusya Merkez Bankası'na sorun bakalım, batıda tuttukları 400 milyar dolarlarına el konulduğu gece uyuyabildiler mi?

İşte blokzincirler bu güveni verebilmek için binlerce makineye ihtiyaç duyarlar. Binlerce makinenin sistemi yürütebilmesi için ise, sistemi ve işlenecek bilgileri olabildiğince ufak tutmaları gerekir. Bilginin ufak tutulması demek işlem yapılacak alanın küçük olması ve yoğun talep olduğunda arz-talep dengesi gereği sistemin pahalanması demek. 

Neden bilginin yazılacağı alanı genişletip kullanıcıları rahatlatmıyorlar? Böyle bir durumda birkaç sorun çıkıyor ortaya. Blokzincirde yaptığınız her işlemin işlenmesi ve kaydedilmesi gerekiyor. Hem de bu onbinlerce makine tarafından. Eğer siz bilginin yazılacağı alanı genişletirseniz (yani her bir bloğu büyütürseniz) bunu işleyecek ya birbirleri ile eş şekilde güncelleyecek makine sayısı azalır (sonuçta bilgisayarların bir kapasitesi var), sadece yüksek performanslı makineler kalır ortada. Böyle olunca merkeziyetsizlikten ödün vermiş olursunuz, bu da sistem güvenliğini tehlikeye atabilir. Sonuç olarak bin makineyi ele geçirmek on bin makineyi ele geçirmekten daha kolay olur. 

İşte bu nedenle, Ethereum zinciri merkeziyetsizlikten ödün vermemek adına, sistemi daha geniş kapasiteli yapma yoluna gitmediler. Bunun yerine farklı çözümler denediler. 

#### Ethereum'un ölçeklenme sorunu hikayesi
Ethereum'un ölçeklenme sorunu için bulduğu çözüme değinmeden önce Ethereum'un nasıl çalıştığına bir parça daha değinmekte fayda var. 

Ethereum bir 'akıllı kontrat platformu'. Bu ne demek? Üzerinde akıllı kontratların çalıştığı bir işletim sistemi (telefonunuzdaki iOS ya da Android gibi). Akıllı kontratlar da aslında telefonunuzdaki uygulamalar. Bu uygulamalar, blokzincire yazılıyorlar ve sonrasında işlem yapmak istediğinizde Ethereum blokzinciri üzerinde çalışarak işleminizi gerçekleştiriyorlar. Bu sayede yaptığınız işlemi blokzincirin şeffaf yapısı sayesinde tam olarak izleyebiliyorsunuz. 

Sorun da aslında burada başlıyor. Yukarıda daha fazla makinenin sistemi yürütebilmesi için blokların ufak tutulması gerektiğini söylemiştik. Bu akıllı kontratlar ise özellikle karmaşık işlemler olduğunda bu bloklarda çok yer tutuyorlar. Böyle olunca bloklar hızlı doluyor ve işlem ücretleri arşa çıkmaya başlıyor. 

Ethereum ekibi başlangıçta bu sorunu çözmek için, Ethereum'u 64 ayrı blokzincire bölerek kapasitesini artırmak gibi bir yola gittiler. Böyle bir durumda işlemler ayrı blokzincirlerde yapılacak ve sonra bir ana zincir üzerinde toplanacaktı. Her ne kadar kapasiteyi artırsa da bir süre sonra bu çözümün de yeterli olmayacağı aşikar idi. İşte o nedenle geçtiğimiz aylarda yavaş yavaş bu planı da değiştirmeye başladılar. Nasıl bir yola girdiler? Birbiri ile bağlantılı iki uygulamaya ağırlık verdiler. 

##### İkinci seviye çözümler (bir diğer deyişle dürüm yani 'roll-up' sistemler)
Ethereum geliştiricileri başta Vitalik olmak üzere geçtiğimiz yıl içinde hararetle ikinci seviye çözümleri ön plana çıkarmaya başladılar. 

İkinci seviye çözümler, Ethereum ekibi tarafından değil, bağımsız geliştiriciler tarafından geliştiriliyorlar. Temel olarak yaptıkları bizim bilgisayarlarda kullandığımız 'zip' dosyalardan farklı değil. 'Zip' dosyaları bilirsiniz; on tane Excel dosyasını bir zip dosyası haline getirirseniz, boyutunu aşağı yukarı onda birine indirirsiniz. İşte ikinci seviye çözümler de yapılan onlarca işlemin Ethereum üzerinde değil, kendi ikinci seviye üzerinde yapılmasını sağlayıp, sadece sonuçlarını Ethereum üzerine yazıyorlar. Bu sayede yüzlerce işlemi biraz büyükçe tek bir işlem gibi yazabilme imkanı doğuyor bu da işlem maliyetlerini ciddi bir şekilde azaltıyor. 

İkinci seviye çözümler güvenli mi? Güvenirlik oldukça göreceli bir kavram. Öncelikle, paranızın güvende olup olmadığı perspektifinden bakıyorsanız, evet. Zira paranız Ethereum blokzinciri tarafından korunuyor. Başka yan zincirlerde örneğin Polygon'da paranızı o zincir koruyor, o zincirde bir sorun olursa paranız tehlikeye girebilir. Ya da Polygon zinciri durdu, paranıza erişemezsiniz (Solana'da çok sık yaşanan bir durum bu). İkinci seviye çözümlerde ise çözümde bir sorun olsa bile siz paranızı Ethereum üzerinde tutuyorsunuz ve başka çözümler kullanarak işletebilirsiniz. İkinci seviye çözümlerin getirebileceği yazılım kodundaki olası riskler olabildiğince minimize edilmiş olmalı ki, Vitalik sahip Ethereum ekibi rahatlıkla bu çözümleri kullanıcılara önerebiliyorlar.  

##### Ethereum 2.0'in değişimi
İkinci önemli değişiklik ise Ethereum'un yeni versiyonunda oldu. Herhangi bir kullanıcının Ethereum üzerinde tüm işlemleri yapması şeffaflık açısından olumlu olsa da, işlemin yüksek yer tutması açısından blokzinciri tıkıyordu. Yeni Ethereum her ne kadar kapasiteyi 64 katına çıkarsa da yine de yetmeyecekti. Bu nedenle, Ethereum geliştiricileri, kapasiteyi yine 64 kata çıkardılar ama önemli bir değişik ile. O da işlemleri artık blokzincir üzerinde yapmak yerine ikinci seviye çözümlere yönlendirecekler. Bunun yerine yeni sistemde işlemlerin hesaplanmasını değil, işlemlerin sonuçlarını blokzincire yazacaklar. Bu yer işgali anlamında muazzam bir tasarruf demek. 

### Sonuç
Ethereum, PoW mekanizmasından PoS'e geçmeye uzun süredir hazırlanıyor ve bu alanda önemli bir sıkıntı görülmüyor. Asıl değişikliklerin yaşandığı ve 'kervanın yolda düzüldüğü' ölçeklenme konusunda, yolun başına göre artık çok daha rahat bir durumdalar. Bakalım, son dakika golleri olmadan rahat bir şekilde maçı bu yıl içinde tamamlayabilecekler mi?
