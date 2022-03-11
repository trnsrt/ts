---
layout: post
title:  "DeFi'de Köprü Kazası"
date:   2022-03-11 17:47:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Bu yazımızda, merkeziyetsiz blokzincirler arası köprüler üzerinde Şubat ayı başında yaşanan Wormhole kazasına detaylıca bakacağız. 

### Peki geçenlerde yaşanan köprü kazalarında ne olmuştu?

Wormhole, ağlar arası varlık transferi hizmeti sunan bir köprü. Sitesinde pek çok farklı ağdan bahsetse de temel olarak Ethereum ile Solana arasında ki transferler için kullanılıyor. 2 Şubat günü, bir hacker, bu ağ üzerinden 120,000 ETH (o zamanki değeri ile 322 milyon ABD Doları) kadar bir rakamı 'çaldı'. 

| ![bridge_accident](/assets/bridge-312873_800.jpg)|
|:--:| 
| *Image by [Ulrike Leone](https://pixabay.com/users/ulleo-1834854/) from [Pixabay](https://pixabay.com/)*|

Olayın nasıl gerçekleştiğini anlamak için öncelikle Wormhole nasıl çalışıyor ona bakalım: 

### Nasıl çalışıyor Wormhole?

Wormhole temel olarak Ethereum üzerindeki ETH'lerin Solana'ya geçirilmesini sağlayan bir köprü. Kullanıcılar, ellerindeki ETH'leri Wormhole köprüsünün bulunduğu Ethereum adresine göndererek 'kilitliyorlar'. Wormhole da kullanıcılara bunun karşılığında Solana blokzincirinde wETH olarak adlandırılan bir token 'yaratıyor'. wETH, ETH değerine çıpalanmış bir token. Temel olarak Ethereum blokzincirinde Wormhole'a kilitlenmiş ne kadar ETH varsa, Solana blokzincirinde de o kadar Wormhole tarafından yaratılmış wETH bulunuyor (blokzincirler şeffaf olduğu için bu bilgiler anlık takip edilebiliyor). 

### Sıkıntı nereden çıktı?

Problem ne? Ethereum ile Solana ayrı zincirler. Birbirleri ile konuşmuyorlar. Bir kullanıcı Ethereum blokzincirinde Wormhole'a ETH kilitlediğinde, birileri bu işlemin gerçekten olduğunu teyit edip Wormhole'a bildirmesi gerekiyor ki o da Solana'da o kadar wETH yaratsın. İşte bu birilerine 'koruyucu (guardian)' deniyor. Bu koruyucular işlemleri imzalayıp Wormhole'a bildiriyorlar. Wormhole akıllı kontratı önce bu koruyucuların imzaları gerçek mi diye kontrol ediyor. 

İşte sıkıntı burada başlıyor. Solana sistemi üzerindeki bu imza süreci düzgün çalışmıyor. Solana bunu birkaç gün önce düzeltip güncelleme yayınlıyor. Wormhole da Solana üzerine kurulu bir akıllı kontrat olarak bu güncellemeyi yapıp yayınlıyor ancak bu güncelleme henüz uygulamaya konulmadan hacker işe koyuluyor. Ne yapıyor hacker?

Koruyucu imzasını 'taklit ederek' Ethereum üzerinde 120,000 ETH kilitlemiş gibi yapıyor. Wormhole sistemi 'taklit imzayı' gerçek zannediyor, ve hackera Solana üzerinde ayni miktarda wETH veriyor. Hacker hemen bu paranın 93,750 tanesini Wormhole üzerinden Ethereum zincirine geçirip Wormhole havuzundan çekiyor. Para gitti mi? Gitti!... 

Peki bu para yoktan mı yaratıldı? Hayır. Wormhole üzerinde Ethereum üzerine kilitli yüksek miktarda ETH vardı. Bu ETH'lerin 120,000'i havuzdan çekildi halbuki bu giden ETH'nin karşılığı olarak diğer Solana tarafında insanların kullandığı wETH'ler var. Dolayısıyla bu wETH'lerin arkası boş kaldı, bunları destekleyecek ETH kalmadı diğer tarafta. Bir anda tüm wETH'lerin değeri düşebilir, bu wETH'leri kullananlar için telafisi imkansız yaralar açılabilirdi. Nasıl?  Örneğin, bu wETH'i teminat olarak kullanıp kredi almış biri, wETH değeri düşeceği için teminat oranının altında kalabilir ve tüm wETH'lerini kaybedebilirdi.   

### Zarar büyük, peki çıkış yolu var mı?

Sonra ne oldu? Wormhole bir akıllı kontrat ve bir ekip tarafından geliştirilmiş. Bu ekibi de finansal olarak destekleyen yatırımcılar var. Bu yatırımcılar, hemen bir gün içinde kaybolan 320 milyon ABD Dolarını ETH olarak Ethereum tarafına geri koydular. İyi de neden böyle bir hareket de bulundular, ceplerinden bu kadar para yatırdılar? Birkaç nedeni var. Birincisi Wormhole'un geleceğine inanıyorlar ve bu alanda girişime ciddi bir para koymuşlardı. Bu parayı koymasalar şimdiye kadar koydukları bütün yatırımı kaybedeceklerdi. Öte yandan böyle bir durum Solana sistemi için de büyük bir prestij kaybı olabilirdi. Zaten yakın zamanda birden fazla sistem durması yaşayan ağın bir de böyle bir açığı kaldırması zor olabilirdi - zira bu olayın hemen ardından SOL %10 değer [kaybetti](https://www.coindesk.com/markets/2022/02/03/solanas-sol-tumbles-10-after-326m-wormhole-exploit/). Dolayısı ile Solana ekibi ile ayrı bir anlaşma yapıp zararın bir kısmını o taraftan almış olabilirler. Bunları net olarak bilemiyoruz. 

### Sonuç

Wormhole benzeri köprülerdeki sıkıntılar önümüzdeki dönemde de oldukça konuşulacak gibi. Bu tip olaylar dışarıdan bakanları korkutabilir, ekosistemin gelişmesini yavaşlatabilir ve geniş kitlelerin adaptasyonunu geciktirebilir. Aslına bakarsanız, merkeziyetsiz sistemlerdeki girişimlerin başlangıç aşamalarında bu tip sorunlar yaşanması normal. Zira bu kadar hızlı büyüyen alanlarda hatalar mutlaka olacak. Blokzincirin şeffaf yapısı bir yandan bu olayların hızlıca medyanın ve toplumun gözü önüne serilmesini sağlarken diğer yandan da benzer girişimlerin bu olaylardan anında ders çıkararak olası açıklarını hızlıca kapatmalarına yarıyor. Bu sayede sektörün olgunlaşan kısımları 'kurşun geçirmez' hale geliyor.


---

*Not 1: Bu yazı ilk olarak 11 Mart 2022'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/defide-kopru-kazasi/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*
