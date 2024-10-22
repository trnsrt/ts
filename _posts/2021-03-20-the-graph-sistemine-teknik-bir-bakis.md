---
layout: post
title:  "The Graph sistemine teknik bir bakış"
date:   2021-03-20 09:47:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Merkeziyetsiz bir servis sağlayıcı olan The Graph protokolünde, sistemi yürüten aktörlere büyük iş düşüyor.. Gelin bu yazımızda bu aktörlere ve sistemin nasıl çalıştığına daha yakından bakalım.  

Bir önceki yazımızda The Graph Protokol'ün ne olduğunu ve nasıl işlediğinden bahsetmiştik. Okumadıysanız öncelikle o yazıyı okumanız sonrasında buraya dönmeniz tavsiye edilir. 

<a href="/genel/2021/03/19/defi-dunyasinin-merkeziyetsiz-analiz-saglayicisi-the-graph.html">
         <img alt="Tweet" src="/assets/graph_yazi_link_640.jpg"></a>

### Sistem nasıl çalışıyor? 

Graph tam bir oracle sayılmaz. Zira oracle hizmetine servis sağlayan dış aracılar (oracle düğümleri) dış dünyadan aldıkları bilgiyi akıllı kontrata aktarıyorlar. 

The Graph'ta ise köprü biraz daha farklı işliyor. Blokzincir içinden alınan bilgi, anlamlı bir hale getirildikten sonra hem zincir içi hem de zincir dışı ihtiyaç sahiplerine dağıtılıyor. 


| ![arrows](/assets/delegate-1969952_640.png)|
|:--:| 
| *Image by [Gerd Altmann](https://pixabay.com/users/geralt-9301/) from [Pixabay](https://pixabay.com/)*|

The Graph, şu aralar en mode olan Proof-of-Stake sistemini kullanıyor. Hemen bir parantez açalım: Yabancı olanlara hatırlatma: Bitcoin, Proof-of-Work denen güvenlik sistemini kullanıyor - hani şu en büyük eleştiri kaynağı olan "ama çok enerji harcıyor" sözünün müsebbibi olan madencilerin olduğu sistem. Ethereum da şu an aynı sistemi kullanmakla birlikte, önümüzdeki yıl içinde Proof-of-Stake mekanizmasına geçecekler. Bu sistemde sistemin güvenliğini sağlayanlar bunu kendi mal varlıklarını teminat göstererek garanti edecekler. Böylece eskiden kol gücü yani emek ile korunan sistem, artık zenginlik yani kapital ile korunmaya başlayacak. Ve parantezi kapatıp konumuza geri dönelim. 

### Aktörler kimler?

#### Endeksçiler:

The Graph sisteminde endeksçiler (indexers) ağın düğümlerini oluşturuyorlar.  Bu arkadaşlar blokzincirler hakkındaki bilgileri düzenli bir şekilde tutup, bu bilgiler ile ilgili arama yapıldığında hem endeksleme karşılığı ödül hem de arama yapma karşılığı da bir ücret almaya hak kazanıyorlar. 

#### Yetkilendiriciler:

Tabii önüne gelen endeksçi olamıyor. Bunun için bir miktar parayı (sistemin parası GRT) teminat göstermek gerekiyor. Ya paranız yoksa? Demokrasilerde ve blokzincirlerde çare tükenmez!. O zaman, yetkilendiriciler (delegators) imdadınıza yetişiyor. Bu kişiler, parası olan ancak endeksleme/arama gibi ağır işçilik yapmak istemeyen sermayedarlar. Paralarını işini iyi yapan endeksçilere veriyor, karşılığında yapılan iş karşılığı kazanılan ödül ya da ücretlerden bir kısmını alıyorlar. Sistemde [Mart 2021 itibariyle 157 endeksçi](https://network.thegraph.com/participants?selected=Indexers) ve [5,696 adet yetkilendirici](https://network.thegraph.com/participants?selected=Delegators) bulunmakta. 

#### Küratörler:

Bunun dışında, bir de Küratörler (Curators) var. Bunlar, akıllı sınıfı (!) temsil ediyorlar. Küratörlerin yaptığı, hangi bilgi kaynaklarında hangi analizlerin para yapacağını önceden kestirmek. Böyle bir 'cevher' bulduklarında, hemen analize para (yine sistemin parası olan GRT) kilitliyorlar. Eğer analiz tutarsa, getirinin bir kısmına hak kazanıyorlar. Burada, hızlı ve kaliteli analiz bulmak çok önemli, erken bulan kazanıyor. Zira öyle "analizi ben buldum kimseye kaptırmam" gibi bir münhasırlık yol. Bir analizin kaliteli ve potansiyel olduğunu gören herkes para yatırır, endeksçiler de daha ilgi gören analizler için iş yaparlar. İlk bulan ve para yatıran iyi getiriler elde ederken, daha sonradan katılanlar daha az gelir elde eder. 

#### Kullanıcılar: 
Tabii bir de kullanıcılar var ki - bunlar genelde DeFi ürünleri oluyor. Örneğin DeFi dünyasının ağır topları Uniswap, Synthetix The Graph'in modellerini kullanıyorlar.  Nasıl belli bilgilerini depolamak için bulut üzerinde yer kiralıyorlar, benzer şekilde modellemeleri için The Graph'i tercih ediyorlar. Bu işi yapmak için ekip tutmak, server kiralamak yerine kullandıkça ödedikleri için onların da işine geliyor bu model açıkçası. Zira o ağır top [Uniswap'ın 2021 yılının Ocak ayında sadece 11 çalışanı olduğunu](https://twitter.com/haydenzadams/status/1346575665940860929) söylersek, neden böyle bir servise ihtiyaç duyacakları daha iyi anlaşılır. 

### Neden para konuyor sisteme?

Neden para konuyor peki? Sistem merkezi değil demiştik. Bu nedenle isteyen sisteme girip endeksçi, yetkilendirici ya da küratör olabiliyor. Peki ya bu kişiler kötü niyetli ise?  Özellikle endeks tutanlar, yanlış bilgi sağlamak ya da endekslemek söz konusu olursa koydukları paranın tümünü kaybedebiliyorlar. Hemen belirtelim teminatlarını uzun bir süreliğine koydukları için bilginin yanlış olduğu sonradan anlaşılsa bile cezayı yiyorlar. Küratör ve yetkilendiriciler bilgi sağlamadıkları için böyle bir ağır cezaya tabi değiller ama onlar da eğer yanlış ata oynar yani yanlış analiz ya da endeksçi seçerlerse, paralarını geri çekerken bir ücret ödüyorlar. 

Para konmasının ikinci bir nedeni de, önüne gelenin sisteme girip sistemi çöplük haline getirmesini önlemek için. Zira, böyle bir durumda kaliteli endeksleme yapanları bulmak zorlaşıyor ve genel sistem reputasyonu bozuluyor. 

---

*Not: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*
