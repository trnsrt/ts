---
layout: post
title:  "Dinamik NFT'ler"
date:   2022-10-24 17:17:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Bu yazımızda adını gelecekte daha çok duyacağımız farklı bir NFT çeşidi olan dinamik NFT'lerden (dNFT) bahsedeceğiz. 

Dijital dünyanın fiziksel dünyaya göre temel farklarından biri, bir ve sıfırlardan oluşuyor olması. Bu da bize burada oluşturulan her tür objenin daha sonra değiştirilebilir ya da çoklanabilir olması özelliğini sağlıyor. Bu özellik bir yandan avantaj bir yandan ise dezavantaj getirmekte. Avantajı, dijital varlıklara inanılmaz bir esneklik sağlaması. Dezavantaj ise dijital varlığın fiziki bir objenin aksine sınırsız sayıda üretilebilmesinin (çoklanmasının) o varlığa değer ifade etme ya da saklama konusunda sıkıntı yaşatması. 

Blokzincirin dijital dünyaya getirdiği temel özelliklerden biri işte bu dijital varlıkları sınırlı hale getirebilmesi. Nasıl sağlıyor bunu? Herkese açık bir defteri olarak, üretilen varlığın adedini ve özelliklerini bir daha değiştirilemeyecek şekilde kayıt ediyor ve o şekilde saklıyor. İşte bu özellik, dijital varlıkların fiziksel olanlar ile aynı klasmana tabi tutulmasını sağlayan müthiş bir yenilik olarak hayatımıza giriyor.

Buraya kadar her şey gayet güzel ilerliyor. Artık NFT'ler ile sınırlı sayıda dijital varlık oluşturmak ve bunları blokzincire koyarak sonsuza kadar aynı formda tutmak mümkün.

Peki ya bu NFT'yi bir süre sonra değiştirmek istersek? Ya da farklı ihtiyaçlar nedeniyle NFT'yi değiştirme zorunluluğu doğarsa ne olacak? Mümkün mü bu? Dijital dünyanın en önemli yanı esneklik demiştik. Dolayısıyla bu bahsettiğimiz özellik tabii ki bu dünyada mümkün. Nasıl olabilir? Gelin sizi dinamik NFT'ler ile tanıştıralım.

| ![walk](/assets/template-3379485_800.jpg)|
|:--:| 
| *Image by [Markus Distelrath](https://pixabay.com/users/distelapparath-2726923/) from [Pixabay](https://pixabay.com/)*|

### Dinamik NFT'ler

Dinamik NFT'ler (kısaca dNFT olarak geçiyor), blokzincire yazıldıktan sonra özelliklerinin değiştirilebildiği NFT'lere deniyor. Bu şimdiye kadar alışık olduğumuz statik NFT kavramından bir parça farklı. Önce statik NFT'lere bir göz atalım: 

NFT dediğimiz aslında ufak bir kod parçası. Bu kod parçası üzerinde metadata denen bilgiler var. Bu kod parçası, NFT'nin kendine ait tekil bir numarasını ve işaret ettiği varlığın (bu, örneğin içinde bir resim barındıran bir dosya olabilir) nerede saklandığını söylüyor.  İşte en basit halinde, statik NFT'de bu kod parçası bir akıllı kontrat olarak blokzincire yazılıyor ve barındırdığı tüm bilgiler değiştirilemez şekilde orada o şekilde kalıyor. 

Dinamik NFT'lerde ise, bu kod parçasına farklı koşullar ve parametreler eklenerek blokzincir üzerinde sonradan değiştirilebilir hale getiriliyor. İyi de tam olarak ne işe yarayacak bu özellik? Birkaç örnek verirsek dinamik NFT'lerin hayatımıza neler katacağı daha iyi anlaşılabilir:

Bir firma olarak verdiğiniz hizmeti satın alan müşterilerinize sadakat puanı olarak NFT verdiğinizi düşünelim. Müşteri başlangıç seviyesi NFT'yi aldı, ama bir süre sonra hizmetinizin sürekli kullanıcısı olarak 'Gold' ya da 'Platinum' seviyesine geçmeye hak kazandı. Ne yapacaksınız? Ona ayrı bir NFT mi göndereceksiniz? Öyle olduğunda eski NFT ne olacak? Yarın öbür gün alt seviyeye düşerse tekrar değiş tokuş mu yapacaksınız? Dinamik NFT'ler ile bu sorunu kökünden halledebilir ve fiziki dünyada kullandıklarınıza benzer özelliklerde NFT'ler üretip müşterilerinizi ödüllendirebilirsiniz. 

Benzer şekilde müşterilerinize verdiğiniz NFT'leri, onların kullanım tarzlarına uygun olarak kişiselleştirebilir, yeni özellikler ekleyebilir, böylece onlar ile aranızda sürekli kendini yenileyen sıkı bir bağ kurabilirsiniz. 

Benzer faydalar sadece dijital alanda yer alan girişimler için de geçerli. Örneğin, oyun içi verilen NFT'lerin zaman içinde oyuncunun seviye atlaması sonucu daha farklı özellikler ve haklar içeren NFT'ye dönüşmesi mümkün olabilir. 

### Nasıl oluyor dinamik NFT'ler

Aslına bakarsanız, dinamik NFT öyle süper yeni bir teknoloji değil, sadece kullanım alanı olarak henüz fazla duymadık onları. Akıllı kontratlar ile oluşturulan ürünlerin değiştirilebilir olması DeFi'nin (merkeziyetsiz finansın) ilk günlerinden beri hayatımızda. Gerek akıllı kontratların 'güncellenebilir' olması gerekse içine yeni bilgilerin yazılması finans dünyası uygulamalarında sık rastlanan bir durum. NFT'ler tarafında ise genel olarak statik NFT'lerin daha yaygın olduğunu görüyoruz ama dediğimiz gibi ileride bunun değişmesi çok olası. 

Burada en kritik nokta, özellikle kontratın çalıştırılması sırasında ihtiyaç duyulacak bilginin buraya nasıl sağlanacağı. Zira akıllı kontratlar kod parçacıkları olarak dış dünya ile ilişki kurabilen yapılar değil. Onlara gerek blokzincir üzerinden gerekse dış dünyadan bilgi gerekli- ki NFT üzerindeki değişimleri yansıtabilsinler. 

Orada da bilgi sağlayıcı (oracle Türkçesiyle kahin) olarak adlandırılan servisler devreye giriyor. Aynı DeFi ürünlerinde olduğu gibi, dış dünyadan ihtiyaç duyulan bilgiler oracle tarafından akıllı kontrata aktarılıyor. Yapılan satın alma ya da kullanımlar sonucu kullanıcının bir üst seviyeye çıkacağı bilgisi dış dünyadan oracle aracılığı ile akıllı kontrata aktarıldığı noktada gerekli değişikler uygulamaya konabiliyor. 

### Peki statik mi dinamik mi?

Burada üreticiler için temel soru NFT üretilirken statik mi yoksa dinamik bir model mi seçileceği. Orada da aslına bakarsanız NFT'den ne beklediğinize vereceğiniz cevap size doğru yolu gösterecek. 

Eğer, bir sanat eseri üretiyorsanız, genelde statik model seçmeniz uygun. Eserinizi satın alanlar doğal olarak yarın öbür gün içeriğinin değişmeyeceğini, dolayısıyla eser üzerinde tam sahiplik hakları olacağını beklerler. Bu güvenceyi de onlara ancak statik NFT'ler verebilir.

Hele bir de işin içine 10,000 adetlik koleksiyonlar girdiğinde statik model daha da cazip hale geliyor. Zira, dinamik NFT esnek olsa da içine koyduğunuz her parametre akıllı kontratın büyümesine ve kontratı çalıştırdığınızda blokzincir üzerinde daha fazla yer kaplamasına (gaz harcayacağı için) neden olur, bu da size daha fazla maliyet olarak geri döner. 

Yok, yukarıda örneğini verdiğimiz gibi sürekli olarak güncellenmesi gereken, farklı özellikler eklenebilecek bir ürün istiyorsanız o zaman dinamik NFT'ler üreticiler için daha cazip bir çözüm olabilir. 

### Sonuç
Dinamik NFT'ler fiziki dünya varlıklarının tokenleştirilmesi konusunda ortaya çıkabilecek sorunların çözümünde bize yardımcı olabilecek, bu sayede dijital varlıkların geniş kesimlerce benimsenmesine katkıda bulunabilecek bir NFT çeşidi olarak karşımıza çıkıyorlar. Önümüzdeki dönemde, istekler geliştikçe, dinamik NFT'lere olan talebin de artacağını söylemek kahinlik olmaz herhalde. Hep birlikte izleyip göreceğiz. 

*Not. Bu konuda daha detaylı bilgi için bu yazıya da esin kaynağı olan şu [blog yazısı](https://thecryptoilluminati.substack.com/p/dynamic-nfts-overview) ilginizi çekebilir.* 

---

*Not 1: Bu yazı ilk olarak 24 Ekim 2022'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı]([https://www.btchaber.com/wikipediaya-web3den-rakip-var-golden-protocol/](https://www.btchaber.com/dinamik-nftler/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*
