---
layout: post
title:  "Modüler ve monoblok zinciler - II: İkinci seviye çözümler"
date:   2024-03-20 18:17:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Yazı dizimizin bu bölümünde modüler blokzincir yapısına, Ethereum üzerine inşa edilmiş ikinci seviye ağlar üzerinden bakıyoruz. 

Geçtiğimiz [yazıda](https://www.btchaber.com/monoblok-ve-moduler-zincirler/) blokzincir ağlarının temel sıkıntısı olan ölçeklenme sorununa değinmiştik. Bu sorunu çözmeye yönelik olarak, eskiden beri süregelen monoblok (yani tek ya da yekpare) blokzincir yapısına karşı son dönemde ön plana çıkan modüler (yani legolar gibi birbirine kenetlenen farklı parçalardan oluşan) blokzincir yapılarını anlatmıştık. (Konuya uzak iseniz başlamadan önce [o yazıyı](/genel/2024/03/06/moduler-vs-monoblok-1.html) okumanızı tavsiye ederim)

Şimdi gelin hep birlikte, bu modüler yapıya akıllı kontrat platformlarının en büyüğü olan Ethereum'un üzerine inşa edilen ikinci seviye blokzincirlere bir göz atalım.  

### İkinci seviye çözümler 
Ethereum'un kısıtları konusunda da değindiğimiz gibi, üstüne gelen yoğun talebi karşılayamayan Ethereum sistemi, merkeziyetsizlikten ödün vermeden büyüyebilmenin yolunu kimi fonksiyonlarını dışarıya atmakta buldu. Burada ön plana çıkan konu ikinci seviye çözümler oldu. 

| ![house](/assets/house-1961182_800.jpg)|
|:--:| 
| *Image by [photosforyou](https://pixabay.com/users/photosforyou-124319/) from [Pixabay](https://pixabay.com/)*|

İkinci seviye çözümler, yukarıda saydığımız dört fonksiyon içinden Ethereum üzerinde en çok yer işgal eden 'işlem gerçekleştirme'yi Ethereum üzerinden almaya talip. Tam olarak ne demek bu? Açıklayalım: 

Ethereum diğer bütün ağlar gibi esasında bir yazılım. Bu ağ üzerinden bir uygulama geliştirmek ya da uygulamayı kullanmak istiyorsanız, sistemin kullandığı yazılım olan EVM'i işletmeniz gerekiyor. EVM'i çalıştırmak Ethereum ağını sürdüren makineleri en çok yoran, bir başka deyişle Ethereum'un sunduğu temel ürün olan blok alanını en çok kaplayan konu. Bu durum, Ethereum'un işleyebileceği işlem miktarını azaltıyor, talebi artırdığı için işlem ücretlerinin de artmasına neden oluyor. 

İkinci seviye çözümler, kullanıcıların yapmak istedikleri bu işlemleri kendi üzerlerine almayı talep eden ayrı birer blokzincir aslında. En basit haliyle anlatırsak, kullanıcıların istediği işlemleri toplu bir şekilde gerçekleştirip, sonuçlarını Ethereum üzerine yazıyorlar. Bir nevi, 'bilgisayarlarımızda yer kaplamasın diye on-yirmi dosyayı bir araya getirip zip yapmak' gibi düşünebilirsiniz. Bu da kullanıcı için ödediği işlem ücretlerinin dramatik şekilde düşmesi demek.  

Peki o zaman, diğer birinci seviye dediğimiz Solana, Avalanche gibi zincirlerden farkları ne? Onlar da kullanıcılarına Ethereum'a göre çok daha ucuza işlem yaptırıyorlar? Temel farkları, kullanıcının yaptığı işlemlerin doğru ve eksiksiz gerçekleştiği konusunda Ethereum'un kullanıcıya sunduğu güvencenin aynısını sunabilme avantajı. Nasıl oluyor bu? 

Efendim, Ethereum, Solana ya da Avalanche gibi ağlarda kullanıcı olarak işlem yaptığınızda işlemin doğruluğunu sağlayanlar o ağı işleten onaylayıcılar. Bu onaylayıcılar yaptıkları işlemin doğru olduğunun garantisini vermek için ellerinde tuttukları tokenleri (ETH, SOL ya da AVAX) sisteme rehin veriyorlar. Eğer bu onaylayıcılar 'yamuk' bir işe kalkışırlarsa koydukları tokenler yanıyor. Eğer siz kötü niyetli biri olarak sistemi ele geçirmek isterseniz, mevcut rehin edilmiş tokenlerin önemli bir kısmını elinde tutmanız gerekir (bu oran ağdan ağa değişiyor, %33, %51 ya da %66 olabiliyor). Ethereum'un piyasa değeri daha yüksek olduğu için, diğer küçük ağlara göre 'göreceli' daha güvenli olarak adlandırılıyor. 

İşte ikinci seviye çözümler, kendi başlarına yeni bir ağ çıkarmak yerine Ethereum'un verdiği bu güvenceyi kullanıyorlar. Peki tam olarak nasıl kullanıyorlar bu güvenceyi? Şöyle açıklamaya çalışalım. İkinci seviye çözümler kendilerini bir akıllı kontrat ile Ethereum ağına bağlıyorlar. Bu akıllı kontrat sayesinde, kullanıcı ikinci seviye çözümü kullansa bile, parası temelde Ethereum üzerinde duruyor. Yarın öbür gün, ikinci seviye çözüm durursa, kullanıcı parasını Ethereum üzerine çekebiliyor. Yani parası güvende. Diğer zincirlerde durma yaşandığında (Solana bir ara çok dururdu, şimdi biraz azaldı) kullanıcı parası sistemde takılı kalıyor.

Şunu unutmamakta fayda var. İkinci seviye çözümler, Ethereum güvencesini verseler de sonuç olarak farklı birer blokzincirler. Bunun avantajları ve dezavantajları var. Temel avantajı, farklı blokzincirler olarak kullanıcıya yeni ürün ya da hizmetleri hızlıca sunabilirler. Ethereum'un herhangi bir iyileştirme yapması, çok büyük ve çok yere dokunan bir zincir olduğu için kolay değil, yavaş oluyor. İkinci seviye çözümler bu konuda çok daha atak olabiliyorlar. 

Örneğin, son kullanıcılar için en büyük problemlerden bir tanesi, sahip oldukları cüzdanlarda sakladıkları ve blokzincirdeki varlıklarına ulaşmayı sağlayan özel anahtarları oluşturmada kullanılan 12 kelimeyi kaybetme riski. Kullanıcının 12 kelimeye ihtiyaç duymadan ve kaybolma riski taşımadan cüzdan sahibi olmasının teknik bir çözümü var.  Aralarında Türk gençlerinin kurduğu bir girişim olan [Clave](https://www.getclave.io/)[^10] de dahil olmak üzere pek çok cüzdan uygulaması bu konuda çalışıyor. Ne var ki, Ethereum'un bu temel çözümü getirmesi zaman alacak[^4]. Oysa ikinci seviye çözümler, örneğin zkSync ve Starknet bu çözümü hemen kendi temel sistemleri içine aldılar bile. 

Dezavantajlarına gelince, ikinci seviye çözümlerin kendileri de birer yazılım. Bu nedenle, ne kadar çok yazılım kullanırsanız, o kadar yazılımdan kaynaklanabilecek hatalara karşı korumasız hale geliyorsunuz. Bu da unutulmamalı. 

Peki ikinci seviye çözümler, aralarındaki rekabet sonucu işlem ücretlerini alternatif birinci seviyeler kadar ucuza gerçekleştirebilirler mi (örneğin Solana)? Bu kısa vadede çok da mümkün görünmüyor. Mart ayı içinde Ethereum'a gelen [yeni güncelleme](https://www.btchaber.com/dencun-yukseltmesi-ethereum-eth-ana-aginda-yayina-girdi/) işlem gerçekleştirme maliyetlerinde ciddi bir ucuzluk getirecek. Yine de işlem gerçekleştirmeyi kendi üzerlerine alsalar da, ikinci seviye çözümler diğer fonksiyonlar için hâlâ Ethereum'u kullanıyor ve bu da onların maliyetlerini yukarı çekiyor. Bu fonksiyonlar içinde en pahalısı olan (Ethereum blok alanı içinde en çok yer tutan) data yayınlama işinde alternatif kimi çözümler de yavaş yavaş gelişiyor. Bunlar içinde en öne çıkan [Celestia](https://celestia.org/) oldu. 

### Arkası yarın

Modüler yapının en uç örneklerinden biri olan Celestia, bir sonraki yazımızın konusu olacak. 

---

*Not 1: Bu yazı ilk olarak 20 Mart 2024'de [BTC Haber'de yayınlandı](https://www.btchaber.com/monoblok-ve-moduler-zincirler-ii-ikinci-seviye-cozumler/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Piyasada oluşacak ihtimalleri değerlendiren bu yazıyı, yatırım tavsiyesi olarak almamanızı rica ederiz. Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

---

[^1]: Meşhur 'çifte harcama' problemi, ingilizcesi double spending. Kişi aynı parayı A ve B kişine aynı anda göndermeye çalışabilir. Bunu yaptığında makinelerden bir kısmı A kişisine giden işlemi alır, kimileri ise B kişisine giden işlemi. Böyle bir durumda iki ayrı blok sisteme girer. Zaman içinde topluluk ya A kişine giden bloğun peşine takılır ya da B kişisine giden bloğun. Böylece konsensus oluşmuş olur. 
[^2]: 'Data publishing' olarak adlandırılan bu özellik, kimi zaman 'data availability' olarak yanlış adlandırılabiliyor. 'Data availability' geçmiş tüm işlemlerin saklanması olarak düşünülebilir  (bir başka deyişle ingilizcede data storage olarak adlandırılan kavram) - onun blokzincir üzerindeki tüm makinelerde saklanmasına gerek yok. Birkaç makine bütün geçmişi (ya da arşivi) saklayabilir. 
[^3]: Basitleştirmek için bu şekilde anlatıyorum, teknik arkadaşlar hemen çullanmasın. Aslında kastedilen, 'script' dediğimiz kodların çok kısıtlı olması. Taproot geliştirmesi ile birlikte özellikle ordinals üzerinden bu kısıt bir parça kırıldı ama hâlâ yeterli sayılmaz. Bitcoin üzerine ikinci seviye çözümler de geliştirilmeye çalışıyor ama bu çözümlerin tam layıkıyla çalışabilmesi için Bitcoin üzerinde yeni güncellemelerin gelmesi (bir nevi soft fork olması) gerekiyor ki bu tip güncellemeler Bitcoin'e üç-dört yılda bir ancak geliyor. Bu güncelleme gelene kadar Bitcoin üzerinde akıllı kontrat kullanımı için bir ara çözüm olan BitVM geliştiriliyor. İlgilenenler bu alanda çalışan Türk bir ekibin (Chainway) kurduğu Citrea çözümünü inceleyebilirler. 
[^4]: EIP 4337 denen bu çözümü kökten sisteme koyamayan Ethereum, bunu bir standart (ERC) olarak yavaş yavaş genele yaymayı planlıyor. 
[^5]: Örnekleri çoğaltmak mümkün. Örneğin, zero-knowledge bazlı ikinci seviye çözümlerin Ethereum sistemine gönderdiği kanıtları oluşturmak için kullandıkları sistemlere prover deniyor. Bunu zkSync gibi kendi mutfağında hazırlayanlar olduğu gibi RiscZero gibi hardware üzerinden optimize etmeye çalışanlar var. Ayrıca her geçen gün yeni bir projenin de bu alan içinde yarışa katıldığını söyleyebiliriz.
[^6]: Duran blokzincirler yok mu? Var tabii. Bu alanda sabıkası olan zincirler var ama onların henüz yeterince olgunlaşmamış olduğunu söyleyerek şimdilik istisna olarak görüp konumuz dışında bırakıyoruz. 
[^7]: Bunun uzun vadede sürdürülebilir bir strateji olup olmadığı konusunda tartışmalar mevcut. Bu haliyle Bitcoin sistemini sürdüren madencilerin ana gelir kaynağı yeni blok oluşturma sonrası verilen madencilik ödülleri. Bu ödül ise her dört yılda bir yarılanıyor. Madencilerin bir diğer gelir kalemi olan işlem ücretleri, Bitcoin sadece para transferi için kullanılırsa çok az kalıyor. Eğer Bitcoin üzerine yeni sistemler (örneğin DeFi kullanan ikinci seviye çözümler) olursa, o zaman işlem ücretleri ve madencilerin gelirleri de artacak. 
[^8]: Celestia'nın sunduğu diğer çözüm olan uzlaşma 'consensus' ise şu şekilde çalışıyor: Bir blokzincir işlemleri kendi sıralamak isterse, bunun için kendi onaylayıcıları olmak zorunda. Kendi onaylayıcıları olması için uygun bir altyapı kurması, sonra bu onaylayıcıları tutmak için bir token çıkarması, dahası bu token için bir ödül mekanizması sunmak zorunda. Bunlar hem zaman ve emek isteyen hem de uygun optimal bir token mekanizması gerektiren konular. Celestia şu an için bu hizmeti sunuyor olsa da aslında ön plana çıkardığı hizmet ilk bahsettiğimiz yani 'data publishing'. Uzlaşma  'data publishing' hizmeti verebilmek için gerekli bir fonksiyon - temel amacı bu. Ama dileyen olursa bu hizmeti ayrıca de Celestia'dan alabilir. Müşterilerin bu hizmeti kullanması için Celestia tokeni olan TIA'nın ciddi şekilde değerlenmesi gerekli.
[^9]: 'Data availability sampling' teriminin kısaltması olan DAS, erasure code olarak adlandırılan bir yöntem kullanıyor. Yöntem blokları oluşturan blok yapıcıların dürüst davranmasını sağlıyor. Normalde, tam donanımlı blok onaylayıcıları blok yapıcıdan gelen kanıtları kullanarak bloğu tekrar oluşturur ve doğruluğunu kontrol eder. Bu nedenler, blok yapıcı bloğa yanlış bir kanıt koyamaz, enselenir. Blok yapıcının yapabileceği tek kötülük kanıtların bir kısmına el koyarak bloğa koymamak olabilir. Böyle bir durumda, blok onaylayıcıları kanıtları görmediği için doğruluğunu kontrol edemez. Blok yayınlanır. Bir süre sonrasında blok yapıcı bloğun tamamını yayınladığından blok geçersiz hale gelir. Bu durumda zincirin geriye doğru getirilmesi gerekir ki, bu bir nevi felaket anlamına gelir. Bu durumdan korunmak için tam donanımlı blok yapıcıların yanında küçük (basit/hafif) onaylayıcılara da ciddi iş düşüyor. Hafif onaylayıcılar blok yapıcıdan blok içinden rastgele parçalar istiyorlar (data availability sampling). Gelen parçalar tam donanımlı onaylayıcı ile teyid ediliyor. 
[^10]: Clave'de ufak da olsa bir yatırımım olduğunu buraya 'disclaimer' olarak [koyalım]((https://blog.getclave.io/p/claves-breakthrough-16m-pre-seed)).  
