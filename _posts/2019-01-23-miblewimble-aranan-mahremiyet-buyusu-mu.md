---
layout: post
title:  "MimbleWimble aranan mahremiyet büyüsü mü?"
date:   2019-01-23 15:43:15 +0300
categories: Genel
---

"Zamanında buralar hep dutluktu" diyenleri bilirsiniz. Benzer şekilde çoğumuz bundan on yıl önce ortaya çıkan Bitcoin'in ilk yıllarını maalesef kaçırdık. Peki bir sonraki Bitcoin'in çıkışının şu aralar, daha doğrusu 15 Ocak'ta gerçekleştiğini söylesek size? (İddialı bir söylem ve hiçbirimiz kesin olarak bilemeyiz bunu tabii ki). Bugünlerde kripto dünyasındaki yeni 'hip' konudan bahsedeceğiz bu yazıda. Nedir bu yeni dalga? MimbleWimble!.  Hadi bakalım, anlamamız gereken yeni bir terim daha. (Merak etmeyin olabildiğince yalın anlatmaya çalışacağız):

Teknik olduğu için bir parça karışık ama basitleştirmek gelin üç parçaya ayıralım anlatacağımızı: 
* Bu yazıda başlangıç seviyesinde işin teknik olmayan kısmına, felsefi ve ekonomik boyutuna MimbleWimble üzerinden bakacağız. 
* [İkinci yazımızda](https://ademimerkezi.com/genel/2019/01/24/gelecegin-odeme-araci-grin-mi-olacak.html) MimbleWimble üzerine kurulan en heyecanlı uygulama olan Grin parasına değineceğiz.
* [Üçüncü yazıda](https://ademimerkezi.com/genel/2019/01/25/Grine-teknik-bakis.html) ise, işin teknik kısmına yani felsefi ve ekonomik olarak diğer iki yazıda bahsedilen konuların teknolojik olarak 'nasıl' gerçekleştirildiğine göz atacağız. 

### Nereden çıktı bu MimbleWimble?

MibleWimble 2016 Ağustos ayında KriptoParalar üzerine uğraşan bir grup yazılımcının kendi aralarında yazıştıkları chat ortamına birden bire Tom Elvis Jedusor rumuzlu biri tarafından bırakılan bir tanıtım yazısı (White Paper) ile ortaya çıktı. 

&nbsp;

| ![mimblewimble__400.png](/assets/mimblewimble__400.png) | 
|:--:| 
| *MimbleWimble White Paper - Kaynak: [Github](https://github.com/mimblewimble/docs/wiki/MimbleWimble-Origin)* |

&nbsp;

Tom Elvis Jedusor, o yazıyı bıraktıktan sonra kayıplara karıştı. Chat ortamındaki diğer yazılımcılar White Paper'ı incelediler,  bahsedilenlerin güvenirliğini, kripto olarak sağlamlığını test ettiler ve gerçekten yeni bir 'olay' ile karşılaştıklarını anladılar. 2016 yılının sonuna doğru Ignotus Peverell rumuzlu bir başka kullanıcı projenin liderliğini ele aldı ve o günden sonra gittikçe büyüyen bir yazılımcı ordusu etrafında MimbleWimble büyümeye ve gelişmeye başladı. En son 2019 yılının 15 Ocak tarihinde artık perdelerini dünyaya açar hale geldi MimbleWimble'in ilk uygulaması olan Grin.

### Ne garip isimler bunlar?
Gerçekten değil mi? Yukarıdaki paragrafta ismi geçen şahısların hiçbiri gerçek değil. Ama hepsinin bir ortak özelliği var. O da Harry Potter! Gelin kim kimdir bakalım:

- *MimbleWimble*: Yeni teknolojinin altyapısı olan protokolün adı. Harry Potter'ın [Deathly Hallows](https://en.0wikipedia.org/wiki/Harry_Potter_and_the_Deathly_Hallows) serisinde geçen bir büyü.  Amacı bir kişinin dilini bağlayarak büyü yapması için gerekli sözleri anlaşılır şekilde söylemesini önlemek. 

&nbsp;

| ![Tongue_Tying_Curse.png](/assets/Tongue_Tying_Curse.png) | 
|:--:| 
| *Harry Potter'daki 'Dil Bağlama Büyüsü'nün el işareti - [Kaynak](https://harrypotter.fandom.com/wiki/Tongue-Tying_Curse?file=Tongue-tying-curse.png)* |

&nbsp;

- *Tommy Elvis Jedusor*: MimbleWimble'in kurucusu. Harry Potter'daki kötü karakter Voldemort'un Fransızca karşılığı. 

&nbsp;

| ![Lordvoldemort-wikipedia.jpg](/assets/Lordvoldemort-wikipedia.jpg) | 
|:--:| 
| *Lordvoldemort - Kaynak: Wikipedia* |

&nbsp;

- *Grin*: MimbleWimble üzerine kurulu en tanınmış uygulama (detaylar bir sonraki [yazıda]). Yine Harry Potter öykülerinden birindeki Gringott's büyücülük bankasının adı.

![grin-400.png](/assets/grin-400.png)

- *Ignotus Peverell*: Grin projesinin lideri. Harry Potter'daki görünmezlik pelerinini üreten büyücü.

![ingotuspeverelaminoappscom-400.jpg](/assets/ingotuspeverelaminoappscom-400.jpg)

- *Luna Lovegood, Seamus Finnigan, Percy Weasley*: Grin projesindeki diğer kullanıcı isimleri. Hepsi Harry Potter ailesinden

![three_harry_potter_characters-400-2.jpg](/assets/three_harry_potter_characters-400-2.jpg)


### Nedir özünde MimbleWimble?
MimbleWimble özünde Bitcoin'in yaşadığı iki ana sıkıntıyı aşmak için yaratıldı: Gizlilik (mahremiyet) ve hantallık. 

#### Gizli

Daha önceki yazılarımızda bahsetmiştik: Bitcoin aslında mahrem bir sistem değil, sözde gizli demek daha doğru. Bitcoin ile yapılan bir işlemde gizli olan kısım sadece kullanıcı adları yerine adresler kullanılması. Ama gizli olmayan kısımları da alabildiğine şeffaf. Örneğin bir işlemde gönderilen para miktarı. 2009 yılında yapılmış bir işlemde bile ne kadar para transferi yapıldığını görebiliyorsunuz.

Ancak kullanıcı adlarının gizli olması aslında çok da mahremiyet yaratmıyor. Adreslerin yaptığı işlemler teknik olarak takip edilebiliyor, dolayısı ile kanunsuz biri ile bir alışveriş yapmanız durumunda hesabınızın mimlenme ihtimali var. Bunu sadece kanunsuz bir işlem olarak düşünmeyin. Baskıcı rejimlerde yaşayanların adreslerinin rejimler tarafından belirlenmesi ve o kişilerin rejim tarafından baskı altına alınması da olası. 

İşte Bitcoin üzerindeki bu sıkıntılar, bireylerin özgürlüğünü kendine şiar edinmiş yazılımcı kesiminin (bunlara cypherpunk da deniyor) tam mahremiyet sağlayacak bir protokol arayışına girmesine neden oldu. Bu şekilde ortaya çıkmış Monero, Dash, Zcash benzeri pekçok KriptoPara da var (bu paralara şu [yazımızda](https://ademimerkezi.com/genel/2018/06/07/token-dunyasina-devam-diger-kriptopalar-litecoin-monero-dash-zcash.html) bahsetmiştik). 

MimbleWimble, kuruluş amacı itibariyle tam bir gizlilik sağlamayı amaçlayan bir protokol. MimbleWimble protokolü ile yapılan işlemlerde işleme taraf olan alıcı ve satıcı ne de işlem miktarı belli. "Öyle olunca hile vs olmuyor mu?" diye soracak olursanız sizi işin teknik kısmını anlattığımız [yazımıza](https://ademimerkezi.com/genel/2019/01/25/Grine-teknik-bakis.html) bekleriz. 

#### Basit

Bunun dışında MimbleWimble'in diğer temel özelliği ise basit ve hafif bir program olması. Teknik olmayanları çok da ilgilendiren bir konu değil aslında ancak Bitcoin'de 2009 yılından bugüne yapılmış bütün işlemleri görebiliyorsunuz demiştik. Bu işlemlerin hepsi Bitcoin sistemindeki tüm makineler tarafından tutuluyor. Bu da her bir makine için GB'larca bilgi demek. Bu da sistemin hantallaşmasına sebep oluyor. MimbleWimble üzerine kurulan uygulamalar burada da güvenlikten ödün vermeden basit bir sistem kurmayı hedefliyorlar (detaylar teknik [yazımızda](https://ademimerkezi.com/genel/2019/01/25/Grine-teknik-bakis.html)). 


### Ne gibi uygulamaları var?
Yukarıda bahsederken iki uygulaması olduğundan bahsetmiştik. Bu iki uygulama Beam ve Grin. 

MimbleWimble başka diğer pek çok proje gibi açık kaynak bir yazılım. Açık kaynak yazılımların en önemli özelliği isteyenin istediği noktada projeyi istediği şekilde geliştirebilmesi. Burada da iki farklı grup projeyi birbirinden çok farklı yerlere götürmüş durumda. 

#### Beam

![beam-400.png](/assets/beam-400.png)

MimbleWimble üzerine çıkan iki projeden biri olan [Beam](https://www.beam.mw/), İsrailli bir girişimci olan [Alexander Zaidelson](https://twitter.com/azaidelson)'un CEO'luk yaptığı bir oluşum. 2018 sonbaharında 400 Bin ABD Doları yatırım alan proje, derli toplu bir şekilde MimbleWimble üzerine Beam adlı KriptoPara'yı kurmak için uğraşıyor. Dertli toplu derken, bir ekibe sahip olması, kendilerine çizdikleri bir yol planına sahip olması, yatırım alması, Beam parasını açtıklarında kurucular için kendilerine bir para ayırmaları gibi özellikler. Zcash benzeri ICO yapan bir KriptoPara'nın geçtiği tüm süreçlerin benzerini yapmaya çalışıyorlar. 


#### Grin
MimbleWimble'in belki de en ilginç uygulaması [Grin](https://grin-tech.org/). Yazı çok uzadı. Grin'i anlattığımız yazımızı [buradan](https://ademimerkezi.com/genel/2019/01/24/gelecegin-odeme-araci-grin-mi-olacak.html) okuyabilirsiniz. 


### Serinin devamı.. 

Yazımızın devamında Grin'e bakıyoruz - [buradan](https://ademimerkezi.com/genel/2019/01/24/gelecegin-odeme-araci-grin-mi-olacak.html) ulaşabilirsiniz..

---

&nbsp;

*Not: Yazdığımız 45+ yazının bir bütünlük içinde nelerden oluştuğuna bakmak isterseniz [Hakkımızda](http://ademimerkezi.com/about/) sayfasına göz atabilirsiniz.*
