---
layout: book-section
kind: section
title: "Bitcoin üzerinden büyük işlemleri hızlı yapmak mümkün mü? Bir çözüm: Liquid – Sorularla Blockchain"
heading: "Bitcoin üzerinden büyük işlemleri hızlı yapmak mümkün mü? Bir çözüm: Liquid"
chapter: 5
chapter_title: "Bitcoin"
order: 506
permalink: /Sorularla_Blockchain/bolum-5/liquid-network/
description: "Bitcoin doğası gereği yavaş gelişiyor ama ona eklenen başka teknolojiler çok daha hızlı ilerleyip Bitcoin’in geniş kitlelerce kullanımını kolaylaştırmaya…"
---

*Bitcoin doğası gereği yavaş gelişiyor ama ona eklenen başka teknolojiler çok daha hızlı ilerleyip Bitcoin’in geniş kitlelerce kullanımını kolaylaştırmaya çalışıyorlar. Bunlardan biri de Liquid. Ne olduğu aşağıda:*

Geçtiğimiz [bölümde](/Sorularla_Blockchain/bolum-5/lightning-network/) Bitcoin’in geniş kitlelere yayılması için üzerinde çalışılan yeniliklerden Lightning Network’den bahsetmiştik. Bu hafta ise bir başka potansiyel yenilik olan [Liquid Network](https://www.blockstream.com/liquid/)[^1][’](https://www.blockstream.com/liquid/)e bakalım birlikte.

## Liquid Network? Nedir o? {#liquid-network-nedir-o}

Liquid Network aynı Lightning Network gibi Bitcoin’i üzerine inşa edilmiş bir yenilik. Ama benzerlikleri orada bitiyor.

Kısaca hatırlayacak olursak, Lightning Network Bitcoin üzerine kurulmuş ikinci bir tabaka idi. Bitcoin üzerinde depozito koyup kanal açan aracılar, bu depozitoyu kullanarak birbirleri üzerinden işlem yapabiliyorlar idi. Böylece hem Bitcoin’in sağladığı güvenlik, gizlilik gibi özellikleri kullanabiliyor hem de Bitcoin ağı üzerinde yük yaratmadan binlerce işlem yapabiliyorlar idi.

Liquid hisse alım-satımı yapan kurumlar ve borsalar arasında hızlı işlem yapmaya yarayan özel bir Blockchain. Farkı Lightning Network gibi Bitcoin üzerine kurulmuş bir tabaka değil de Bitcoin’e bağlı bir yan-zincir (side-chain) olması. Ne demek yan zincir? Açıklayalım:

Liquid’in yaratmış olduğu özel bir Blockchain ve buna bağlı olan bir para var L-BTC adında (Sabitparalar’dan bir başka [bölümde](/Sorularla_Blockchain/bolum-6/diger-kripto-paralar-neler/#sabitparalar-dalgali-denizler-icinde-sakin-sular-sunar-mi-bize) bahsediyoruz). Kendilerini ABD Doları gibi İtibari paraya bağlayan sanal paralardan. L-BTC de kendini Bitcoin’e bağlamış. Yani hem BTC ile aynı değerde hem de bir L-BTC yaratılması için aynı oranda bir BTC karşılığının olması gerekiyor. Kullanıcılar BTC (Bitcoin’in parası) sahibi olmaya devam ederken L-BTC’nin sağladığı ek avantajlardan yararlanabiliyorlar.

<figure markdown="1">
<a href="/assets/books/sorularla-blockchain/506-1.png"><img src="/assets/books/sorularla-blockchain/506-1.png" alt="Kaynak: Blockstream" width="601" height="600" loading="lazy"></a>
<figcaption markdown="span">Kaynak: [Blockstream](https://www.blockstream.com/liquid/)[^2]</figcaption>
</figure>

Liquid Network, Bitcoin’den farklı olarak özel bir Blockchain (permissionless). Ne demek bu? Şöyle: Bitcoin açık bir network olduğu için hem kullanıcılar hem madenciler istedikleri gibi girip çıkabiliyorlar. Liquid Network’de ise Bitcoin’deki gibi madenciler yok. Sadece şu an sayısı 15 olan borsalar ve kurumsal aracılar var. Yapılan işlemleri madenciler onaylamıyor, o işi bu borsa ve kurumsal aracılar yapıyor. Bitcoin’de madencilerin çoğunluğunun işlemi onaylaması gerekirken burada üçte iki çoğunluk gerekiyor, yani 11 borsanın işlemi onaylaması gerekli.

Kullanıcılar ise L-BTC ile istedikleri gibi işlem yapabiliyor ama L-BTC’lerini satmak için yine bu borsaları kullanmak zorundalar. Kullanıcı olarak bir borsaya girip L-BTC aldığınızda, bu spesifik bir BTC’ye bağlanıyor ve satmaya kalktığınızda o spesifik BTC üzerinden işlem yapılıyor. Böylece olası sahtekarlıklar önlenmiş oluyor.

## Nedir sağladığı avantajlar Liquid’in? {#nedir-sagladigi-avantajlar-liquidin}

Kullanıcılar için Liquid’in sağladığı en büyük avantaj SabitParalar ile benzer aslında.

kripto paranızı (buradaki örnekte BTC’nizi) bir borsada tutmak riskli. Neden? Her ne kadar kripto para borsaları her tür güvenlik önlemini alsalar da merkezi yapılar — dış tehdit ve saldırılara açıklar\*. O nedenle özellikle büyük miktarda parayı kurumsal yatırımcılar borsalarda tutmak istemiyorlar.

Paranızı borsada tutmadığınız durumda ise işlem yapmak istediğinizde çok vaktinizi alıyor. Cüzdanınızdan parayı borsaya göndermek Bitcoin üzerinde en kısasından 10 dakika ama borsanın bunu tam olarak alıp (teyid edip) size işlem yaptırmasına baktığınızda çok daha uzun zaman alıyor. Özellikle çok işlem yapan biri iseniz bu kimi fırsatları kaçırmanıza yol açabilir.

İşte Liquid bu iki soruna çözüm getiriyor. Paranızı L-BTC’de tuttuğunuzda, borsaya 1 dakika içinde gönderebilir ve hemen alım satım yapabilirsiniz. Daha sonrasında L-BTC’inizi isterseniz kendi cüzdanınıza çekersiniz, ya da BTC’ye çevirirsiniz (1'e 1 aynı oranda).

## Var mı sakıncaları? {#var-mi-sakincalari}

Teoride yukarıda yazılanlar çok güzel görünse de Liquid’e kuşku ile bakanlar da yok değil. Bu kuşkuların ciddi bir kısmı felsefi aslında.

Bitcoin’in bağımsız yapısını ön plana çıkaranlar Liquid Network gibi yapıların özel network olmasına takılıyorlar. Dediğimiz gibi işlemleri onaylayanlar madenci değil özel olarak seçilmiş 15 kurum. Kaldı ki bu seçilmiş kurumların hepsinin sicili de o kadar iyi sayılmaz ([a](https://www.coindesk.com/crypto-exchange-zaif-hacked-in-60-million-6000-bitcoin-theft/), [b](https://medium.com/@bitfinexed/wash-trading-bitcoin-how-bitfinex-benefits-from-fraudulent-trading-8bd66be73215), [c](https://www.trustnodes.com/2018/09/14/bitmex-seemingly-trading-against-its-own-customers-price-manipulation-in-plain-sight)). Ya bu 15 kurum içinde 11'i birlikte hareket ederse? Liquid yaratıcıları da böyle bir riski kabul ediyorlar ama karşılaştırmanız gerekenin paranızı (BTC’ninizi) bir borsada tutmanın riski ile 15 farklı borsada tutmanın riski olması gerektiğini söylüyorlar. Tek bir borsanın risklerini almaktansa, riski 15 ayrı borsaya dağıttığınızı belirtiyorlar. Ama nereden bakarsanız bakın, BTC’nin orjinal yaratıcılarının düşlediği özgür dünyadan sapma bu yapı sonuç olarak.

İkinci bir eleştiri ise, Blockstream’e yapılıyor. Kâr güden bir kurum olan Blockstream, kendi kaynaklarını kullanarak bugün için Bitcoin’in geliştiren hatırı sayılır sayıda yazılımcıya iş olanağı sağlıyor. Eleştirenler, bu kişilerin ileride Bitcoin’i geliştirirken de Blockstream’ın istediği alanlara yönelip tarafsızlıklarını kaybedebileceklerinden endişe duyuyorlar. Şahsen çok katılmadığım bir kaygı. Zira Bitcoin geliştiricisi olmak için herhangi bir sertifika ya da izin gerekmiyor. İsteyen yazılımcı Bitcoin’i geliştirmek için katkıda bulunabilir. Blockstream’in bu yazılımcılara iş veriyor olması, başka yazılımcıları da Bitcoin üzerinde çalıştırmaya sevk edebilir, ki bu gayet Bitcoin’in yararına bir durum.

Sonuç

Her ne kadar yukarıdaki eleştirileri yazsak da, özünde Liquid kullanıcılara fayda sağlayan bir yapı. Riskler de katlanılabilir görünüyor. Bitcoin’in kullanan kişilerinin her birinin ondan beklentisi farklı. Kimi hızlı işlem yapmak isterken, kimi gizlilik kimi de baskılara karşı koyabilme özelliğini nedeniyle Bitcoin kullanıyor. Liquid hızlı işlem yapmak ve bu işlemler için yüksek komisyon vermek istemeyenlere uygun bir yapı. Bitcoin’in kurumsal yatırımcılar tarafından daha sık kullanılmasını sağlayacağı bunun sonucu da piyasadaki likiditeyi artırıcı bir faydası olacağı düşünülüyor. Yani özünde aynı Lightning Network gibi Bitcoin’in gelecekte geniş kitlelerce adaptasyonuna yardımcı olmaya çalışan bir araç. Başarılı olacaklar mı hep birlikte göreceğiz.

[^1]: [https://www.blockstream.com/liquid/](https://www.blockstream.com/liquid/)

[^2]: [https://www.blockstream.com/liquid/](https://www.blockstream.com/liquid/)
