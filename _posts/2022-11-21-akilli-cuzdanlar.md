---
layout: post
title:  "Akıllı cüzdanların gelişi"
date:   2022-11-21 17:17:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Bu yazımızda kripto dünyasının, geniş kesimlere ulaşmasının önündeki en büyük engellerden biri olan cüzdan kullanımı sırasında yaşanan problemleri nasıl aşabileceğinden bahsedeceğiz. 

### Cüzdanlar kaç çeşit? 

Ethereum dünyasında kullanılan cüzdanları temel olarak ikiye ayırmak mümkün[^1]. Birincisi, önceki yazımızda da bahsettiğimiz en çok kullanılan cüzdan çeşidi olan basit cüzdanlar. Teknik adıyla 'EOA Externally Owned Account' (haricen sahip olunan hesaplar) olarak adlandırılan bu cüzdanların içinde bir adet özel anahtar bulunuyor. 

İkinci bir çeşit ise 'akıllı kontrat cüzdanları' olarak karşımıza çıkıyor. Bu cüzdanlar, kullanıcı blokzincir ile temasa geçmeden önce belirli kurallar koyarak çok daha verimli bir kullanıcı deneyimi sunma hedefindeler. Bu hedefe ulaşma yolunda bazı sıkıntıları var. İşte bunları temelden çözmek için Ethereum sisteminde değişiklikler gerekiyor. (detayları aşağıda bir sonraki bölümde değineceğiz). Önce akıllı kontrat cüzdanların bize neler vaat ettiğinden bahsedelim. 

### Akıllı kontrat cüzdanlarının ne gibi faydaları var?

Akıllı kontrat cüzdanları programlanabilir olmalarından dolayı kullanıcıya kişiselleştirilmiş bir cüzdan deneyimi sunuyorlar. 

| ![puzzle](/assets/problem-solving-g2de67c0d8_800.png)|
|:--:| 
| *Image by [Mohamed Hassan](https://pixabay.com/users/mohamed_hassan-5229782/) from [Pixabay](https://pixabay.com/)*|

Ne demek bu? Güvenlik isteyene, istediği kadar güvenlik, pratiklik isteyene pratiklik - 'seç beğen al'. Temel mantık kullanıcının hiçbir şekilde cüzdana erişimini kaybetmeyeceği, rahat kullanılan ve kullanıcının kafasında yer meşgul etmeyecek bir sistem[^2]. Gelin birkaç potansiyel kullanım alanına değinerek konuyu somutlaştıralım: 

Şu anki cüzdanların temel sorunu tek bir anahtar ile tek bir işlem yapılabilmeleri. Akıllı kontrat cüzdanları, hesabın tek anahtar boyunduruğundan kurtulmasını ve çoklu anahtar yaratımını sağlıyor. En temel özellikleri bu. Ne işe yarar bu özellik? 

En başta, sosyal olarak hesabı kurtarmaya (İngilizcede 'social recovery') yarar. Cüzdanınıza erişimi olan anahtarlar üretip farklı cihazlara dağıtabilir, bu anahtarları arkadaşlarınıza ya da güvendiğiniz kurumlara verebilirsiniz. Bu sayede, cüzdanınızı kaybetmeniz durumunda kurumun websitesine girerek oradan yeni anahtar üretebilirsiniz. 'İyi de, şimdi de kuruma güvenmek zorundayım, ya kurum paramı çalarsa?' diye düşünebilirsiniz. Bunun da çözümü var. Üç anahtar üretip ikisi ile imza yoluna giderseniz sorunu çözersiniz. Birini telefonunuzda, diğerini bir arkadaşınızda ya da kasada, üçüncüsünü ise bu kurumda tuttunuz. Telefonunuzu kaybederseniz, kurumun websitesine giderek onlarda bulunan anahtarı alabilirsiniz. Kurum, bu anahtar ile tek başına işlem yapamaz. 

İkincisi aynı cüzdan üzerinden çoklu imza atabilmek. Yani? Daha fazla güvenlik. Örneğin, baştan üç anahtar üretip, herhangi bir işlem yapabilmek için bunların iki tanesinin bir işlemi imzalamasını istemek. Kullanıcı bu üç anahtarı üç ayrı cihaza dağıtıp (örneğin cep telefonu, bilgisayar ve bir soğuk cüzdan) bunların ikisi olduğunda işlem yapabilmesi kuralını koyabilir. 

Öte yandan, rutin işlemlerde birden çok imza gerektiği durumlarda bu işlemlerdeki imzaları topluca yollayarak hızlı ve daha az masraflı işlem yapmak da mümkün olacak. 

Çoklu imza ve akıllı kontrat mantığı sayesinde binlerce faklı kombinasyon yapabilirsiniz.  Örneğin işlemlerin gerçekleşmesi için aşağıda sıraladığımız
belli kurallar/kısıtlar koyabilirsiniz; 
- miktara göre (100 doların altı işlemleri tek anahtar ile onaylayayım, üstü için iki anahtar onay versin), 
- cihaza göre (100 doların altını sadece cep telefonumdaki tek anahtar ile, üstünü evimde duran bilgisayarımdaki anahtar ile birlikte onaylayayım), 
- hizmete ya da işleme göre (her zaman kullandığım A uygulamasında işlemlerin hepsini bir anda yap, ama daha önce hiç kullanmadığım bir uygulama ise bütün adımları tek tek imzalamak istiyorum), ya da 
- süreye göre (önümüzdeki 24 saat için sadece tek imza geçerli olsun, sonra çoklu imza gereksin, ya da tam tersi)

Gördüğünüz gibi seçenekler sınırsız hale geliyor. Kullanıcı hem anahtar kaybetme korkusu olmadan geleneksel finanstakine benzer bir kullanıcı deneyimine, hem de merkeziyetsiz sistemlerin sunduğu rahatlık ve esneklik ile işlem yapabilme olanağına kavuşuyor. 

## İşin tekniğine bakalım biraz da... 

Gelin şimdi de cüzdan çeşitlerine, şu anki sorunlarına ve gelecekte Ethereum'un bu sorunlara nasıl çözüm bulacağına daha derinden bakalım. 


#### Cüzdanlar nasıl işlem yapıyor?

Kullanıcı bir işlem yapmak istediğinde bu işlemi özel anahtarı ile imzalıyor[^3]. İmzalanan işlem, bütün işlemlerin toplandığı bir havuza gidiyor. Burada işlem, avcılar tarafından bloklara aktarılıyor ve bu sırada işlemin doğru olup olmadığı kontrol ediliyor[^4]. Doğru işlemler bloğa konarak blokzincire kayıt ediliyor. 

#### Basit cüzdanların (EOA) sorunları

EOA dediğimiz şu an yaygın olarak kullanılan cüzdanlar artık yeni dönemin ihtiyaçlarına cevap vermiyor. Bu cüzdanlarda tek anahtar var ve anahtarı kaybetmesi durumunda kullanıcının hesaba erişimi kesiliyor. Üstelik bu anahtar ile, her seferinde sadece tek bir işlem onaylayabiliyorsunuz. Örneğin bir token alacaksınız, bunun için de elinizdeki USDT'yi kullanacaksınız. Öncelikle uygulamanın USDT'nize dokunmasına izin vermeniz gerekiyor. Sonrasında ise uygulamanın yapacağı her işlem için tek tek onay vermeniz zorunlu. Bu hem masraflı hem de bazen hızlı olmanız gereken yerlerde, iki onaydan dolayı fiyatın değişmesi nedeniyle sizi zarara uğratabiliyor.
 
#### Akıllı cüzdanlar bu sorunları nasıl çözüyor?

EOA denen cüzdanlarda yaşanan sorunları gören Argent ve Gnosis gibi birkaç uygulama, kullanıcılara bu sorunları aşabilecekleri yeni tip cüzdanlar geliştirdiler. İşte bu yeni cüzdan çeşidine akıllı kontrat cüzdanları deniyor. 

Bu cüzdanlar, kullanıcı ile hizmet verenin kendi cüzdanı arasına bir akıllı kontrat kurarak, blokzincir öncesi çeşitli kurallar aracılığıyla kullanıcının sorunlarına çare bulacak çözümler getiriyorlar.  Kullanıcıya sorun yaratan her tür durum, blokzincir öncesi (off-chain) ön komutlar ile çözülüyor, sonrasında bu cüzdanlara ait EOA cüzdanı işlemlerin sonunu blokzincire yazıyor. 

#### Şu anki akıllı cüzdanlar nerede yetersiz kalıyor?

Sorunun temelinde EOA cüzdanlarının kullandığı imzalama teknolojisinin eskiliği yatıyor. Ethereum üzerinde hâlâ bu sistem kullanıldığı için de böyle özel çözümlere başvuruluyor. Gördüğünüz gibi, aslında Argent ve Gnosis gibi akıllı cüzdanların yaptığı, bir soruna derme çatma bir çözüm bulmak. Burada da başka sorunlar ortaya çıkıyor: Her bir cüzdan kendine özel çözümler üretiyor, belirli bir standart yok. Ayrıca akıllı kontrat oldukları için ilk açıldıklarında Ethereum'a işlem ücreti ödenmesi gerekiyor. Öte yandan uygulamalara güven duymayı gerektirmesi, güncellemeler sırasında sorun çıkma ihtimali gibi problemleri de barındırıyorlar. Bu saydığımız nedenlerle ideal çözüm olmaktan henüz uzaktalar.

#### Sorunlara kökten bir çözüm bulmak mümkün mü?

Peki Ethereum üzerinde kökten bir çözüm üretilemez mi? Üretilebilir tabii ama önceki yazımızda da değindiğimiz gibi Ethereum geliştiricilerinin başka öncelikleri  (örneğin PoS'a geçiş) ve kısıtlı kaynakları olduğu için buraya odaklanmaları mümkün olmadı. Şimdi sıra bu alana gelmiş gibi görünüyor. Geçtiğimiz ay Kolombiya'nın başkenti Bogota'da yapılan Devcon (Ethereum gelişticileri) konferansında bu konuda bir panel düzenlendi ve uzun zamandır konuşulan ve adına Account Abstraction denen bir iyileştirme masaya yatırıldı[^5].

#### Karşınızda 'Account Abstraction'
Account abstraction yukarıdaki farklı cüzdanlar tarafından yaratılan derme çatma çözümleri Ethereum'un temelinden çözmeye verilen genel ad[^6]. Burada nasıl bir yol izleneceği henüz tam olarak belli değil. Vitalik'in önerdiği yöntem, kullanıcıların işlemleri öncelikle bir ön havuza göndermeleri, burada bu işlemlerin blok üreticiler tarafından toplanıp kontrol edilmesi ve tüm işlemlerin doğru olduğu anlaşıldıktan sonra tekrar kullanıcı ile temasa geçip kullanıcının onay vermesi şeklinde[^7]. Vitalik bu çözümün ideal olmadığının farkında ancak şu aşamada bununla ile başlanıp ileride daha kökten bir çözüme gidilmesini öneriyor[^8].

Öte yandan Ethereum şu an çok büyük bir yapı olduğu için Account Abstraction konusunu kökten çözemiyor ama bu durum şu anki ikinci seviye çözümler için geçerli değil. İkinci seviye çözümler, daha kapalı ve henüz geliştirme aşamasında oldukları için bu tip yenilikleri kendi altyapılarına 'temelden' dahil edebilirler. Bu sayede, aslında bu çözümlerin pratik olarak nasıl çalışacağını test etmek de mümkün olabilir. Bunu da aslında görmeye başladık: Argent kendi ürettiği derme-çatma çözümlerin Starknet ve zkSync gibi ikinci seviye sistemlerine temelden gömülmesi için bu sistemlerin geliştiricileri ile birlikte çalışıyor (bu iki sistemde Argent'in cüzdan çözümlerinin yaygın olarak kullanıldığını görebilirsiniz). 

### Sonuç

Akıllı kontrat cüzdanlarını ortaya çıkaracak olan 'Account Abstraction' özelliği, cüzdanların kullanımına büyük bir rahatlık getiriyor. Şu an bu konuda çalışan Argent, Gnosis gibi cüzdanların getirdiği kolaylıkların, tüm Ethereum altyapısına yayılması, geniş kitlelerin bu alana girmesinde kritik eşik (İngilizce'de çok kullanılan haliyle 'tipping point') olabilir. Geliştirme süreci maalesef yine yavaş işleyecek - Ethereum geliştiricilerinin en büyük açmazı bu. Bu nedenle ikinci seviye çözümlerin bu yarışta bayrağı almalarında fayda var. İkinci seviye çözümler son bir yılda araştırma-geliştirme anlamında oldukça başarılı işlere imza attılar. Burada da benzer performans göstermelerini beklemek mümkün. Gelişmeleri heyecanla izleyeceğiz.

---
[^1]: Yazımızda, Ethereum ve Ethereum ile uyumlu (EVM uyumlu) tüm blokzincirler (Polygon, Avalanche, FTM, BNB Chain gibi) içinde kullanılan cüzdanlardan bahsediyoruz (Solana, Near ve son zamanlarda moda olan Aptos benzeri blokzincirler konumuz dışı). 
[^2]: Bu konuda Vitalik'in yazdığı [şu makale](https://vitalik.ca/general/2021/01/11/recovery.html) ilginizi çekebilir
[^3]: Kullanıcı, işlemi ECDSA denen bir imzalama tekniği kullanarak onaylıyor. 
[^4]: Burada kontrol edilen üç temel konu var. İmza doğru mu (hesabın sahibi mi imzalamış), işlem sırası doğru mu (nonce denen işlem sırası, kullanıcının aynı anda iki işlem yaparak çifte harcama yapmasının önüne geçiyor) ve ağ doğru mu (kullanıcı doğru ağda mı işlem yapıyor, Ethereum, Avalanche, Polygon, BNB Chain gibi)?
[^5]: Panelin tamamının videosuna şu [linkten](https://www.youtube.com/watch?v=WsZBymiyT-8&t=3s) ulaşabilirsiniz. 
[^6]: Account Abstraction, temel olarak akıllı kontratların kullanım mantığının genişletilmesi demek. Şu an sadece blokzincir üzerinde yapılan işlemlerde geçerli olan akıllı kontrat mantığını işlem için ödenen ücretler ve işlemlerin onaylanması için de kullanmak anlamına geliyor. Bu konuda daha detaylı bilgi için Vitalik Buterin'in '[The Road to Account Abstraction](https://notes.ethereum.org/@vbuterin/account_abstraction_roadmap)' makalesine göz atabilirsiniz.
[^7]: Vitalik'in önerdiği çözüm ERC 4337 adında bir iyileştirme. İşlemlerin şu anda ve gelecekte nasıl şekilleneceği ile ilgili gerek Vitalik'in bir önceki dipnottaki yazısına ya da daha basit anlatımı için [şu Medium post](https://medium.com/nethermind-eth/ethereum-wallets-today-and-tomorrow-eip-3074-vs-erc-4337-a7732b81efc8)'una göz atabilirsiniz. 
[^8]: Vitalik'in önerdiği ERC 4337 aslında yavaş yavaş kullanılmaya başlanabilecek bir çözüm. Daha sonrasında bir EIP aracılığıyla protokol seviyesinde oluşan boşlukları kapatmayı düşünüyor. Burada, baştan neden EIP'ye gidilmediği sorulursa, hem EIP'nin bir çatallanma gerektirmesi, hem de oluşturma sürecinin daha uzun sürmesi cevabı verilebilir. 

---

*Not 1: Bu yazı ilk olarak 21 Kasım 2022'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/akilli-cuzdanlar/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*
