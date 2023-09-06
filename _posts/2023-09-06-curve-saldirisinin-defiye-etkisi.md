---
layout: post
title:  "Curve saldırısının DeFi'ye etkileri - 1"
date:   2023-09-26 18:17:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Bu yazımızda Ağustos ayı başlarında DeFi dünyasını çalkalayan ve başta Curve olmak üzere birçok platformu etkileyen hack olayını ve DeFi dünyasına etkilerini anlamaya çalışacağız. 

Merkeziyetsiz finans (DeFi) dünyasının bayrak isimlerinden Curve tarafında yaşanan bir hack (saldırı) olayı DeFi'nin şu anki yapısı ve geleceği ile ilgili pek çok tartışmayı beraberinde getirdi. Gelin önce şu hack olayını bir kez daha hatırlayalım, sonrasında da DeFi dünyasına etkilerini konuşalım. 

### Neler olmuştu? 
Öncelikle DeFi'ye aşina olmayanlar için hikayemizin baş kahramanı olan Curve'ü tanıtalım. Curve, merkeziyetsiz kriptopara alım-satım platformları içinde Uniswap'ın arkasından ikinci büyük oyuncu.  Nedir ikisinin farkı?

Uniswap, hemen hemen her tür kriptoparanın alınıp satıldığı, tüm DeFi dünyasına hitap eden bir platform iken, Curve daha çok değeri birbirine denk kriptoparaların alınıp satıldığı daha niş bir oyuncu. (Curve'ün nasıl çalıştığını merak edenler dipnottaki uzun açıklamaya dalabilirler. :)) 

Bu iki sistemin bir başka farkı ise, Uniswap'ın başta a16z gibi kripto dünyasının ağır toplarından aldığı ciddi finansmanın da etkisi ile daha çok bir Web2 şirketi gibi davranırken (örneğin çıkarttığı yeni modellerin kopyalanmasını iki-dört yıl arası sürelerde yasaklarken) Curve'ün özellikle bir DAO olarak Web3 ilkelerine daha bağlı bir şekilde hareket etmesi.  

#### Yaşanan saldırı
Konumuza geri dönersek: 30 Temmuz Pazar sabahı, Curve'ün sahip olduğu havuzlardan bir kısmında paraların hızlı bir şekilde havuzlardan boşaltıldığını ve tam olarak dört farklı havuzdan yaklaşık 73 milyon ABD Doları para kaçırıldığını [öğrendik](https://www.btchaber.com/curve-financeta-47-milyon-dolarlik-siber-saldiri/)[^1]. 

#### Saldırı sonrası yaşananlar
Saldırgan havuzlardan para kaçırırken birkaç ilginç gelişme de yaşandı. Örneğin, saldırganın hareketlerini takip eden kimi botlar, havuzdaki paraları saldırgandan önce 'çaldılar'. Beyaz şapkalı saldırgan (ingilizcesi 'white hat hacker') olarak adlandırılan bu hackerler sayesinde çalınan paraların yaklaşık %30'luk bir kısmı geri alındı (bu savaşın detaylarına bir sonraki yazımızda değineceğiz).

| ![dogs](/assets/dogs-2921382_800.jpg)|
|:--:| 
| *Image by [Anja](https://pixabay.com/users/cocoparisienne-127419/) from [Pixabay](https://pixabay.com/)*|

Bu arada Curve protokolü saldırıyı düzenleyenlere çalınan parayı geri vermeleri karşılığında (artık bu tip işlemlerde standart halini almaya başlayan) bu paranın %10'unu ödül olarak [vaat etti](https://etherscan.io/tx/0xc45e47f6e7d3e74763032e2fb991fa9a003d8ed55c13c93c6a5368ff322d7742). Hackerlara 6 Ağustos tarihine kadar süre veren protokol, eğer bu tarihe kadar para geri dönmezse ödülü saldırganları açığa çıkaranlara vereceğini ve bu kişiler ile mahkemede hesaplaşacaklarını da mesajına ekledi. 

Sonrasında saldırgan, iki Curve havuzunda duran yaklaşık 33 milyon ABD Dolarını iade etti. İşin ilginç yanı, iade ederken gönderdiği [mesajda](https://etherscan.io/tx/0x23c4799784c91023204bd68a94ec7a963486f2485dc43c13d8b804d5301b8041) "Bu hafta saçma sapan yorumlar gördüm. Şunu açıklığa kavuşturmak isterim ki, paraları geri iade etme nedenim beni bulma ihtimaliniz değil, projelerinizi mahvetmek istememem. Bu para pek çok insan için büyük bir para ama benim için değil. Hepinizden daha akıllıyım." yazmasıydı. Görüyorsunuz değil mi, pek çoğumuza inanılmaz gelen rakamlar, birkaç 'degen' diye adlandırılabilecek kişi için 'önemsiz' bir hale gelmiş.

Sonuç olarak toplamda çalınan paranın yaklaşık 53 milyon ABD Dolarlık kısmı o ya da bu şekilde [geri alındı](https://twitter.com/PeckShieldAlert/status/1688404426825117697) ancak tamamı geri gelmediği için Curve, saldırganı açığa çıkarana 1.85 milyon ABD Doları ödül vereceğini açıkladı. 

#### Saldırının CRV fiyatına etkisi
Olay sadece dört havuzun boşaltılması ile sınırlı kalmadı. Havuzların boşaltıldığını gören diğer havuzlardaki likidite sağlayıcılar paralarını platformdan hızla çekmeye başladılar. Curve havuzlarına kilitli para miktarı 3.1 milyar ABD Dolarından 1.7 milyar ABD Dolarına kadar düştü. 

| ![curve-kilitli-miktar](/assets/curve_tvl_defillama_2308_800.png)|
|:--:| 
| *Saldırının Curve havuzlarına etkisi. Kaynak: [DeFiLlama](https://defillama.com/protocol/curve-finance)*|

Özellikle FTX krizi sonrası likidite sıkıntısı çeken DeFi dünyası, bir de Curve olayından dolayı darbe almış oldu.  Bu sırada 73 cent civarında olan CRV tokenin fiyatı birkaç saat içinde 63 cente kadar düştü (bu yazı yazıldığı sırada CRV yaklaşık 44 cent üzerinden işlem görüyordu). İşte bu durum da başka bir problemi beraberinde getirdi. Gelin şimdi de ona değinelim. 

#### Curve'ün kurucusu Egorov'un işleri
Curve platformunun kurucusu olan Michael Egorov, elinde tuttuğu yüksek miktarda CRV tokeni Aave platformuna teminat olarak vermiş ve karşılığında tam 63 milyon ABD Doları kredi almıştı[^2]. Eğer CRV fiyatı 32 cente düşerse kredi likide olacaktı. Kredinin likide olması demek Aave'nin kredinin teminatı olan CRV'yi piyasada bozdurması demekti. Bu da çok normal olarak CRV fiyatının daha da düşmesi anlamına gelecekti. Sonuç olarak olay, CRV'yi teminat olarak kabul eden başka kredilendirme platformlarını da domino taşı gibi etkileyerek tüm DeFi'yi sarsacak bir kasırgaya dönüşebilirdi[^3]. ('Kan kokusunu' alan pek çok traderin o anda çok sayıda CRV'yi shortladığını tahmin edebilirsiniz sanırım.) 

Egorov, bu durumun önüne geçmek için elinde bulunan CRV tokenleri piyasa değerinin oldukça altında bir fiyata (40 cent) [bir grup yatırımcıya satarak](https://twitter.com/sandraaleow/status/1687191897171972096) likidite sorununu çözdü. Tezgah üstü denen piyasa dışı işlemler ile satılan 84.5 milyon CRV token ile birlikte yaklaşık 33.8 milyon ABD Doları finansman sağlayan Egorov, bu para ile borcunun bir kısmını kapatarak CRV'deki kanamayı durdurdu. 

Durdurdu durdurmasına ama bu hareket kripto dünyasında kaşların kalkmasına da neden oldu. Zira, Egorov bu satışların ilkini kripto dünyasının şaibeli isimlerine (Justin Sun, Jeffrey Huang, DWF Labs) yapmıştı. Üstelik anlaşmanın detayları da tam olarak bilinmiyor. Kimileri, tokenleri satın alan partilerin altı ay satmama sözü verdiğini söylüyor ama bu ne kadar ciddi bir taahhüt bilinmiyor. Keza aynı partilerin CRV token fiyatı 80 centin üzerine çıkarsa satma hakkı olduğu da [yazılıyor](https://www.theblock.co/post/242516/curve-founder-michael-egorov-sells-more-crv-to-dcfgod-and-others).[^4] 

### Arkası yarın
Bu yazımızda, oldukça karmaşık ama bir o kadar da renkli bir hack hikayesini şu ana kadar gerçekleşmiş kısmıyla aktarmaya çalıştık. Önümüzdeki yazımızda ise bu saldırının DeFi dünyasında yarattığı tartışmalara göz atacağız. Kim bilir, belki de o zamana kadar kalan 18 milyon ABD Doları da ele geçirilmiş olur.. 

---

[^1]: Detayını merak edenler için Alchemix’e ait alETH-ETH havuzu, Curve'ün kendisine ait CRV/ETH havuzu, Pendle'a ait pETH-ETH havuzu ve Metronome ait msETH-ETH havuzları 'kurultuldu'. Neden 'ait' diyoruz? Platformlar kendilerine ait tokenlere (örneğin Alchemix ETH'ye bağlı bir para olan alETH) likidite sağlamak için Curve üzerinde bu tip havuzlar açtırabiliyorlar. 

[^2]: Egorov'un kriz öncesi farklı farklı platformlarda 115 milyon ABD Doları borcu ve bu borca karşı teminat olarak verdiği yaklaşık 400 milyon dolar değerinde CRV token vardı. 'Niye bu kadar borç almış?' diye bir soru akıllara gelebilir. Bunun birkaç nedeni var. Birincisi, paraya ihtiyacı olduğunda CRV tokenları piyasada da satabilirdi. Böyle bir durumda CRV'nin fiyatı düşer, kendi mal varlığı da azalırdı. O nedenle satmak yerine teminat vermeyi seçmiş olabilir. Bir başka neden, vergi avantajı olabilir. Eğer CRV'yi satsa kazancı üzerinden vergi ödemek durumunda kalacaktı. Bunun yerine elinde uzun süre tuttuğunda, belli bir süre sonra vergi muafiyeti kazanıyor olabilir. Peki neden bu kadar paraya ihtiyacı var? Orada da işin magazinsel kısmı devreye giriyor: Arkadaş, her ne kadar DeFi dünyasında aktif olsa da 'gerçek hayatta' da varlık sahibi olmayı seviyor. Nitekim bu yıl içinde eşi ve kendisine Avustralya'da 40 milyon ABD Doları değerinde [iki malikane satın aldı](https://www.theblock.co/post/232464/curve-finance-ceo-michael-egorov-wife-mansions-australia).

[^3]: Burada her ne kadar fazla teminat (ingilizcesi over-collateralized) taşıyor olsalar da kredi verme platformları da risk altındalar. Örneğin Aave, Egorov'un açık pozisyonunu kapatmak için CRV tokenleri piyasada satmak ister ancak fiyat çok düşük kalırsa zarar edebilirdi. Bundan dolayı borcun tamamını kapatamazsa, o zaman kendi [sigorta fonu olan](https://docs.aave.com/aavenomics/safety-module) AAVE/ETH havuzundaki AAVE'leri satmak zorunda kalacak, bu da AAVE'nin fiyatını olumsuz etkileyecekti. 

[^4]: Sonrasında Aave, Yearn, Wintermule gibi göreceli daha yatırımcıların girmesi, Egorov'un ilk turda 'denize düşen yılana sarılır' şekilde hareket ettiğini gösteriyor aslında.

[^5]: Burada ‘Ee, 500 ABD Doları değerinde ETH’si vardı, 2500 ABD Doları olmuş işte’ diye düşünebilirsiniz ama ETH 2500 ABD dolarına gelirken havuzdaki ETH sayısı azalacak. Havuza para koyduğunuzda havuzdan bir pay alıyorsunuz. Dolayısıyla o payı satarken size ilk koyduğunuz kadar ETH verilmeyecek. Bir başka deyişle, havuza başta 500 USDC ve 1 ETH olarak toplam 1000 ABD Doları koymak yerine, onu kenarda tutsanız, ileride ETH 2,500 ABD Dolarına yükseldiğinde toplam varlığınız 3,000 ABD Doları olacaktı (2500 ABD Doları değerinde bir ETH artı 500 USDC). Havuzda tuttuğunuzda bu ETH 1000, 1500 ABD seviyelerinde satılarak azalacağı için, size ufak bir miktar ETH ve bolca USDC verilecekti ama toplam 3000 ABD Dolarından az olacaktı. 


*Curve sistemini merak edenler için özel not*

Curve'ün Uniswap'tan farklı bir çalışma prensibi olmasının temel bir nedeni var. Bu tip platformlarda işlem yapmak isteyenler, genelde iki tokenden oluşan havuzlarda alım-satım yapıyorlar. Bu tokenlerden birini havuza koyup diğerini havuzdan satın alıyorlar (yani iki tokeni takas ediyorlar). Tokenin hangi fiyattan alınıp satılacağına ise havuzdaki token miktarına göre matematiksel bir formül karar veriyor. Piyasa fiyatları ani değişim gösterdiğinde, havuzun fiyatı piyasanın gerisinde kalabiliyor. İşte bu sırada arbitraj yapan oyuncular devreye girip, ucuz kalan tokenleri toplayarak token fiyatını piyasaya uyumlu hale getiriyorlar. Tabii bu işten ciddi bir kazanç elde ediyorlar. İyi de birileri bu işten kazanç elde ederken bir başkası da kaybediyor olmalı? Gayet tabii. O da havuza en başta o parayı koyan kişiler, bir başka deyişle likidite sağlayıcıları. Havuza para koyanların uğradığı bu zarara 'geçici kayıp' (ingilizcesi 'impermanent loss') deniyor. Geçici denmesinin nedeni, tokenlerdan birinin piyasa değeri yükseldiğinde yaşanan kaybın, tokenin değeri eski haline gelirse ortadan kalkıyor olması. Peki ya eski fiyatına dönmezse? Örneğin, ETH/USDC havuzuna ETH 500 ABD Doları para koymuş bir likidite sağlayıcı ETH fiyatı 2500 ABD Dolarına çıkarsa ne yapacak?Yapacağı bir aksiyon yok (riski hedge etmek yoluna gidebilir ama o da bir maliyet) [^5]. 'Geçici zarar' kalıcıya dönüşecek. Likidite sağlayıcıları, havuzda yapılan işlemlerden komisyon kazanıyor ve bu komisyonların yaptıkları zarardan fazla olması (yani kâra geçebilmeleri) için 'dua' ediyorlar. 

İşte Curve bu durumun önüne geçebilmek için genelde değeri birbiri ile denk hareket eden kriptoparalara odaklanıyor. Bunların içinde en bilinenleri stabil paralar. Örneğin USDC/USDT çifti bir havuzdaki tokenlerin değeri genel olarak 1 ABD Doları çevresinde gezindiği için likidite sağlayıcılarının 'geçici zararı' hiçbir zaman kalıcıya dönmüyor. Tabii böyle olunca, Curve likidite sağlayıcılara “arkadaşlar bakın 'geçici zarar etmediniz' o nedenle gelin bu havuzlara para koyma işinden beklediğiniz komisyonları azaltın” diyebiliyor. İşte Curve, kullanıcılara önerdiği düşük komisyonlar ile çok ciddi bir likidite sağlayıcısı haline geldi. Bir yandan da, havuzlarına para konmasını teşvik edebilmek için, yeni yarattığı kendine ait CRV tokenleri havuz sahiplerine dağıtmaya başladı. Hangi havuza ne kadar teşvik verileceğine mevcut CRV token sahipleri karar verdiği için piyasada CRV tokene karşı büyük bir talep oluştu. Hatta Convex gibi, token sahiplerinden CRV token toplayıp bununla istediği havuzlara daha fazla teşvik verilmesini sağlayan, karşılığında aldığı tokenleri ise bu token sahiplerine geri veren sistemler bile türedi.

---

*Not 1: Bu yazı ilk olarak 6 Eylül 2023'de [BTCHaber'de yayınlandı](https://www.btchaber.com/curve-saldirisinin-defiye-etkileri-i/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

