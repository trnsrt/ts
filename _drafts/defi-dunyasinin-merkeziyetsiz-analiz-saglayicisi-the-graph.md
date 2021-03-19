---
layout: post
title:  "DeFi dünyasının merkeziyetsiz analiz sağlayıcısı 'The Graph'"
date:   2021-03-20 17:47:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Bu yazımızda DeFi dünyası oyuncularının data ve analiz ihtiyacını karşılamaya yönelik yeni ancak önemli bir işlevi yerine getiren The Graph Protocol'den bahsedeceğiz.

[The Graph Protocol](https://thegraph.com/), DeFi ürünler ile dış dünya arasında köprü görevi gören bir aracı. İşlevi farklı olsa da genel olarak DeFi dünyasının eskilerinden Chainlink’e oldukça benziyor. 

Hatırlayanlar olacaktır, DeFi’nin önemli altyapı sağlayıcılarından olan [Chainlink](https://chain.link/) üzerine [detaylı bir analiz](/genel/2020/12/22/definin-bilgi-kaynagi-oracle.html) yapmıştık.. Gelin önce Chainlink ne işe yarar kısaca hatırlayalım:

### Benzer bir altyapı projesi olan Chainlink'i hatırlayalım önce... 

DeFi platformları özünde kendi başlarına birer dünya. Herhangi bir DeFi ürünü üzerine kurulu olduğu DeFi platformunun içinde güzel güzel yaşıyor. (Şu an ağırlıklı olarak Ethereum bu platform ancak rakipleri de geliyor). Ancak kimi zaman bu ürünlerin kendi blokzincir dışı ile de irtibatı olması gerekiyor.

DeFi ürünlerinin temelini ise akıllı kontratlar oluşturuyor. Akıllı kontrat aslında bir yazılım. Kendisine söyleneni otomatik olarak genellikle 'el değmeden' yerine getiriyor. Harekete geçmesi için uygun koşulların oluştuğunu anlaması gerek. Eğer bu 'işlem yapmayı tetikleyici' bilgi blokzincir içinde ise işi nispeten kolay. Ancak bilgi dışarıda ise o zaman işi zor.

Bu bilginin ona sağlanması gerekiyor. İşte oracle dediğimiz bilgi kaynakları, bu bilgiyi blokzincir dışı dünyadan alıp kontratın işleyeceği bir hale getiriyorlar. Örneğin altın fiyatları üzerine işlem yapan bir akıllı kontrat dış dünyadaki altın fiyatlarını bilmek zorunda. Oracle'lar dış dünya ile blokzincir arasında bu anlamda  bir köprü vazifesi görüyor adeta. Chainlink de bunların en ünlü ve büyük olanı.

### Nedir Graph? Ne işe yarar? Kimler kullanır?
The Graph blokzincirlerin ya da onların üzerinde yaşayan DeFi ürünlerinin performansları hakkında bilgi ve analiz sunan bir hizmet. Tam olarak yaptığı blokzincirlerin yarattığı bilgileri (data ya da veri denebilir bunlara) toplamak, arama yapılacak hale sokmak (endekslemek) ve ihtiyaç duyanların hizmetine sunmak.

| ![e-wallet](/assets/arrows-2899888_800.jpg)|
|:--:| 
| *Image by [Gerd Altmann](https://pixabay.com/users/geralt-9301/) from [Pixabay](https://pixabay.com/)*|

İhtiyaç duyanlar kimler? Başka başka DeFi servisleri, yatırımcılar ya da yatırımcılara danışmanlık verenler...

DeFi dünyası 7/24 çalışan bir dünya. Bilgiye nerede ise gerçek zamanlı ihtiyaç duyuyorsunuz. Size bu tip analizler için hazır araçlar sunan siteler de mevcut. Ama tam istediğiniz gibi bir analiz seti bulabiliyor musunuz? Ya da o site, analizde kullandığı bilgileri sizin istediğiniz yerden mi alıyor?

Normalde DeFi alanında bir girişim olarak böyle bir bilgiye ihtiyaç duyuyorsanız, yapmanız gereken, kendi iç ekiplerinizi kullanıp ihtiyaç duyduğunuz bu araçları sıfırdan yaratmak yani yazmak. İyi de, bir DeFi ürünü olarak zamana karşı yarışıyorsunuz. Rakipler her gün yeni bir özellik sunuyorlar. İnsan kaynağı deseniz zaten kısıtlı. Kısıtlı insan kaynağınızı kendi ana ürününüzü geliştirmek için mi kullanmak istersiniz, yoksa bu tip bir ikincil ihtiyaç için mi?

İşte Graph size herhangi bir blokzincire ait bilgileri istediğiniz formatta alıp istediğiniz şekilde analiz etmenizi sağlayacak bir platform sunuyor. Üstelik istediğiniz zaman ya da sıklıkta yaptırıyor, kullandığınız kadar para ödüyorsunuz.  Tabii ki en büyük avantajı, bunu merkeziyetsiz yani aracılar olmadan daha güvenilir bir şekilde gerçekleştiriyorsunuz. 

### Bir örnek mi versek?
Burada basit bir örnek vermek konuyu somutlaştırmak açısından iyi olabilir. En bilinen örnek olan Uniswap'tan başlayalım: (Yine bir hatırlatma: [Uniswap](https://uniswap.org/), merkeziyetsiz finans dünyasının en büyük takas borsası.  Ne olduğu ve nasıl çalıştığı ile ilgili [şu yazımıza](/genel/2020/09/15/nedir-bu-uniswap.html) bakabilirsiniz)

Uniswap, üzerinde 2020 yılının Şubat ayı içinde toplam [4.2 milyon adet alım-satım işlemi](https://duneanalytics.com/danrobinson/uniswap-combined-metrics) gerçekleşmiş. Bu Ethereum zinciri üzerine yazılmış bu kadar sayıda işlem demek. Bütün bunlar Uniswap içindeki [167 adet farklı havuz](https://info.uniswap.org/pairs)'da gerçekleşmiş. Her bir havuzdaki işlemleri,  hacimleri ve havuzların dinamiklerini düşünürseniz, işleyip analiz edebileceğiniz milyonlarca bilgi var. İşte bu işlemlerin ve havuzların durumunu anlık ya da belli tarih aralıkları içinde dönemsel olarak almak isterseniz The Graph sistemini kullanabilirsiniz.

| ![uniswap_on_the_graph](/assets/uniswap-overview_800.jpg)|
|:--:| 
| *En basitinden The Graph kullanılan bir Uniswap grafik örneği. Kaynak: [The Graph](https://thegraph.com/blog/uniswap-built-on-the-graph)*|

Hemen belirtelim bu ürünü biz son kullanıcıların kullanması oldukça zor. Zira basit de olsa veri tabanlarında bilgi sorgulama ile ilgili teknik yeterliliğe sahip olmak gerekiyor. 

### The Graph'in diğer hizmet sağlayıcılardan farkı ne?
The Graph'ı kuran ekip, sistemi olabildiğince merkeziyetsiz yapmak için oldukça çaba sarfetmiş. Örneğin Chainlink sisteminden söz ederken, her ne kadar müşterileri merkeziyetsiz DeFi platformları olsa da, sistemin oldukça merkezi olduğunu belirtmiştik.

The Graph'de ise daha merkeziyetsiz bir sistem görüyoruz. Sisteme giriş ve çıkış izne tâbi değil herşeyden önce. İşleyiş de olabildiğince kendi kendine oluyor. 

The Graph sisteminin işleyişini yürütenler ağırlıklı olarak ağ üzerindeki bağımsız aktörler (ya da İngilizce node da denilen düğümler). Dataları toplayan, endeksleyen, istenen analizleri çıkaran, datanın doğruluğunu sağlayanlar bunlar. (Detaylı bilgi için en dipteki nota bakabilirsiniz).

The Graph ekibi ise birkaç yerde işin içinde:

Ortaya çıkarılan endeks ya da analizlerin, ihtiyaç sahiplerine düzgün bir şekilde tanıtılması için [Graph Explorer](https://thegraph.com/explorer/) isimli bir dApp kurmuş ekip - bir nevi pazaryeri burası. Bu oldukça kritik. Zira küratörler tarafından en kaliteli endeksler ortaya çıkarılmalı ki, bunlar talep sahipleri tarafından görülebilsin, kullanılsın ve küratör ve endeksçilere para kazandırsın. Ham data IPFS denilen merkeziyetsiz protokolde tutulsa da, Graph Explorer'daki endeks ve analiz bilgileri şimdilik merkezi bir yerde tutuluyor. Gelecekte bu hizmetin merkeziyetsiz bir şekilde sunulması için çalışmalar sürüyor. 

Bunun yanında başlangıçta endeksçilerin hatalı bilgi vermesi gibi konularda karar verici olan ekip olsa da, bu daha sonra protokolün yönetimine bırakılacak.

### Rakipleri var mı? Gelecek nasıl görünüyor?

The Graph şu ana kadar endeksleme ve arama/sorgulama alanındaki merkeziyetsiz en bilinen model. Rakipleri merkezi yapılar: DeFi alanında bilinen en ünlü merkezi servisler [Dune Analytics](https://duneanalytics.com/home), [Glassnode](https://glassnode.com/) ve [Nansen](https://nansen.ai/).  Bunun yanında [Google BigQuery](https://cloud.google.com/bigquery) gibi genel arama hizmetleri de mevcut. 

Ancak bütün merkezi servislerde yukarıda bahsettiğimiz güvenirlilik sıkıntısının yanında istediğin hizmeti tam olarak alamama sorunu var. Blokzincirler inanılmaz bilgi/veri üretiyorlar ve doğru anlamlı veriye ulaşmak çok kritik. Merkezi servisler çok daha oturmuş veriler ile çalışırken, bir yatırımcı yeni ortaya çıkan bir blokzincir ile ilgili bir analiz yapmak istediğinde merkezi servislerde aradığını bulamıyor. Bu anlamda The Graph tam onların istediği gibi bir bilgi akışı ve analiz sağlayabiliyor. 

Bakalım bu alanda da, her alanda olduğu gibi, merkezi platformların hızlı ve kullanıcı dostu arayüzleri ile merkeziyetsiz platformların daha az kullanışlı ama eğilip bükülebilir ve tarafsız yapısı arasındaki tatlı rekabette kim ön plana çıkacak. Şu an görünen her iki hizmetin de farklı alıcıları olacağı ve pazarda kendilerine yer bulacakları şeklinde.. 

Ancak şunu unutmamakta fayda var. Oldukça kuvvetli bir yatırımcı ordusunu arkasına alan, token değeri olarak da çok iyi bir yükseliş yakalayan The Graph, şu an için merkezi rakiplerinin önünde değil. Üstelik bu rakiplerden ayrışacağını belirttiği merkeziyetsizlik konusunda ise daha önünde alacağı çok yol var. Muhtemelen yatırımcıları değer olarak The Graph'ın arkasında olmaya devam edecekler ancak ürün başarıyı bu söz verdiği merkeziyetsizliği başarabildiği ölçüde kazanacak.. 

### Sonuç
The Graph protokolü, merkeziyetsiz blokzincir dünyasının yarattığı bol veriyi, tarafsız bir şekilde tarayıp, endeksleyip, kullanıcıların sorgulamasına sunan ve bu dünyanın ruhuna uygun olarak merkeziyetsizleşmeyi kendine hedef seçmiş bir DeFi ürünü.. Şu an için Ethereum bazlı olarak çalışan protokol bakalım merkeziyetsizlik yolundaki yürüyüşüne devam edecek ve sonrasında vazgeçilmez bir DeFi hizmet sağlayıcı olabilecek mi? 

Yazıyı daha fazla uzatmamak için The Graph sisteminin nasıl çalıştığı konusundaki detayı bir sonraki yazımızda bulabilirsiniz. 

---

*Not 1: Bu yazı ilk olarak 20 Mart 2021'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/yeni-bir-ethereum-rakibi-binance-smart-chain/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*


