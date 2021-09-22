---
layout: post
title:  "DeFi neden farklı? - Uyumlu çalışma"
date:   2021-09-11 08:47:56 +0300
categories: Genel
tags: Yazılar, DeFi, DeFi'ye Giriş
---
Bu yazımızda DeFi'yi klasik finanstan farklı kılan özelliklerden uyumlu çalışmaya bakıyoruz. 

DeFi'nin klasik finansa göre temelden farklı belli birkaç özelliği var. Bunlardan ilki olan 'açık kaynak' felsefesine yazı dizimizin ilkinde değinmiştik. Bu yazıda ise, ikinci temel farklı özellik olan uyumlu çalışma (composability) özelliğine değineceğiz. 

## Klasik finansın sıkıntıları
Aslına bakarsanız birkaç yüzyıl önceye dayanan klasik finans, 20. Yüzyılın içerisinde ağır ağır belli temellere oturdu. Başlangıçta sadece mevduat toplama ve kredi verme ekseninde gelişen sektör, yüzyılının ikinci yarısından itibaren yeni yeni ürünler ile hızlanmaya başladı. Hız derken yanlış anlaşılma olmasın, genel olarak yeni ürün çıkarma süreçleri genelde yıllarca hatta on yıllarca sürmeye devam etti. 

Teknolojinin hayatımızın içine daha da girmesi ile birlikte bu gelişme hızları artmaya başladı. Kimilerince dijitalleşme olarak da adlandırılan bu sürecin sayesinde artık yeni ürünler daha hızlı bir şekilde müşteri beğenisine sunuluyor. 

Bu süreçte bâki kalan belki de en önemli özellik rekabet. Rekabet, bir yandan kurumlar için hızlı hareket edebilmenin itici gücü ama bir yandan da kurumların arkasına saklandıkları bir mazeret. Ne demek istediğimizi biraz daha açalım. 

Eskinin rekabeti korumacı bir rekabet idi. Yani, bilginin, hizmetin nasıl yapıldığının rakiplerden saklanması temeline dayanıyordu. Zira, saklanmadığı durumda rakiplerin ürün ya da hizmeti 'kopyalama' riski ortaya çıkıyordu. 

Benzer şekilde bu rekabetin getirdiği 'gizliliğin' bir başka sonucu da, kurumların kendi yaptıklarını 'kalın duvarlar' altında saklaması. Bir örnek verelim: Toprak Mahsülleri Ofisi'nin Haydarpaşa'daki siloları dikkatinizi çekmiştir: 

| ![silol](/assets/silos-tim-hallam_800.jpg)|
|:--:| 
| *Kaynak: [Tim Hallam](https://www.instagram.com/p/CTXnmzKobMA/) özel izniyle*|

İşte finans devleri de böyle silolar şeklinde çalışır. Yani ürünlerin tüm geliştirmesini kendi içlerinde yapar, lisans ve telif zırhları altında saklar ve en önemlisi başka kurumlar (hele de rakipler) ile ortak çalışma yapmazlar. 

Kişisel bir örnek ile devam edeyim. ABD'de danışmanlık yaptığım günlerde içinde olduğum bir projede, [Paine Webber](https://en.wikipedia.org/wiki/Paine_Webber) adındaki bir yatırım bankasının (sonradan UBS satın aldı) üst yönetimine, müşterilerin farklı farklı bankalardaki hesaplarını bir ekranda görebilmek için ne yapılması gerektiğini araştırıyorduk. Banka, farklı alternatifler içinden [Yodlee](https://www.yodlee.com/) firmasını seçti, hatta yanlış hatırlamıyorsam yatırım da yaptı Geçenlerde, ABD'deki bir başka bankada bulunan hesabıma girdiğimde, bu 'tüm hesapları aynı ekranda görebilme' özelliğinin artık hayata geçtiğini gördüm. Harika değil mi? Öyle gibi görünüyor, ancak bu proje içinde tam yirmi yıl önce yer almıştım. Sanki bir parça yavaş, ne dersiniz?

Klasik finans oyuncuları, artık yavaş yavaş bu korumacı felsefeden uzaklaşmaya başlıyorlar. Sektör içinde 'açık bankacılık' denen, bilginin belli standartlar üzerinden diğer kurumlar ile paylaşılması konusunda belli bir yol katedildi. Yeterli mi? Kişisel kanaatim bu konuda olumlu bir ilerleme yaşansa da bunun hâlâ yavaş bir geliştiği yönünde.   

### DeFi'nin avantajı ne?

Geçtiğimiz yazımızda, detaylı olarak bahsettiğimiz 'açık kaynak' hareketi ise yukarıda ilk bahsettiğimiz 'korumacı felsefenin' tam tersi olarak kopyalamayı serbest bırakıyor, hatta teşvik ediyor. Onların dünyasında rekabet, ürettiğini saklamaktan değil, hep ileriye giderek yenisini yaratmaktan geçiyor. 

DeFi'deki bir başka özellik ise, yine 'açık kaynak' felsefesinin bir uzantısı olarak, farklı ürünler bir arada kulanılabiliyor. Hatta buna 'money lego' adı veriliyor. Yani ürünler lego parçaları gibi birbirlerine takılıp çıkarılabiliyor, birbirleri ile 'ahenkli bir şekilde çalışabiliyorlar'. Aynı legoda olduğu gibi bu parçalar bir araya getirilip onlarca, yüzlerce farklı ürün yaratılabiliyor.  

Örnek vermek gerekirse, yukarıda bahsettiğimiz müşterinin kullandığı tüm kurumlara ait hesaplarını bir arada görebilmesi özelliği DeFi'de ilk günden mevcut. [Zapper](https://zapper.fi/), [Zerion](https://zerion.io/) gibi kimi portföy takip ürünleri kullanıcının kulandığı tüm ürünlerin bakiyelerini göstermekle kalmıyor, bunu geçmişten bugüne takip edilebilir şekilde sunuyorlar. Başlangıçta, sadece portföy takip hizmeti olarak başlayan bu servisler daha sonrasında elektronik cüzdan ve 'farklı borsalardan fiyat alarak en uygun seçeneği müşteriye sunma' olarak adlandırabileceğimiz toplayıcı hizmetini de vermeye başladılar. 

Nasıl beceriyorlar kısa süre içinde bunları yapmayı? Temel nedeni, bu bilgilerin tamamı blokzincir üzerinde tutuluyor. Yani şeffaf bir şekilde herkesin kullanımına açık. Bu bilgilere ulaşmak ve bu bilgileri kullanmak için herhangi birinin izninine ihtiyaç yok. Dolayısıyla, bu bilgileri alıp toplamak ve kullanıcıya sunmak artık çocuk oyuncağı. 

Bir sonraki yazımızda DeFi'yi klasik finanstan ayıran önemli özelliklerden 'emanet tutma' konusuna değineceğiz. 

---

*Not 1: Bu yazı ilk olarak 25 Eylül 2021'de [BlockchainIST Center](https://medium.com/blockchainist-center)'da [yayınlandı]()*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.* 
