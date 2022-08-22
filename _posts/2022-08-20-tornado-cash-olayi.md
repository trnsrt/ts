---
layout: post
title:  "Tornado Cash olayı ve düşündürdükleri"
date:   2022-08-20 12:17:56 +0300
categories: Genel
tags: Yazılar, DeFi, CoindeskTR
---

Bu haftaki yazımızda geçtiğimiz günlerde ABD tarafından yasaklı listesine alınan Tornado Cash uygulamasını ve bu olayın kripto dünyasına etkilerini ele alacağız. 

### Neydi Tornado Cash?
Tornado Cash, Ethereum blokzinciri üzerindeki para akışlarının kaynağını gizlemek için kullanılan bir uygulama. Temel olarak, kendisine gönderilen ETH'leri topluca bir havuza alıp karıştırıp, daha sonra istenilen adrese çekim yapılabilen bir akıllı kontrat, kimilerinin deyişiyle bir karıştırıcı. Bu sayede, herhangi bir adrese gelen paranın hangi adres tarafından gönderildiği belli olmuyor. Hizmete girdiği 2019 yılından bu yana yaklaşık [7,6 milyar ABD Doları](https://blog.chainalysis.com/reports/tornado-cash-ofac-designation-sanctions/) bu uygulama üzerinden geçirilmiş. 

### Neden otoritelerin ilgisini çekmişti?
Geçtiğimiz birkaç yıl içinde DeFi dünyasında yaşanan pek çok hack olayında çalınan paraların Tornado Cash aracılığıyla izlerinin kaybettirildiği görüldü. Yapılan incelemeler sonucunda bu hacklerin önemli bir kısmının Kuzey Kore'de devlet tarafından 'yetiştirilen' ve ABD tarafından [2019 yılında yaptırım konan](https://home.treasury.gov/news/press-releases/sm774) Lazarus isimli bir korsan grubu tarafından gerçekleştirildiği anlaşıldı. Bu konudaki son büyük örnek, Axie Infinity tarafından kurulan Ronin blokzincirini Ethereum'a bağlayan köprüde 2022 yılı Mart ayındaki saldırıda çalınan [455 milyon dolar](https://twitter.com/chainalysis/status/1514645221027594245) oldu. 

Kuzey Kore, ABD'nin [1950'lerden beri yaptırım uyguladığı](https://en.wikipedia.org/wiki/Sanctions_against_North_Korea) bir ülke. Bu nedenle yukarıda bahsettiğimiz tek bir olayda devlet bağlantılı hackerların 'yürüttüğü' para elbette Amerikan otoritelerin tüm keyfini kaçırmıştı. Tornado Cash üzerinden geçen paranın yaklaşık [%28'inin direkt hackerlar ve yaptırım altındaki yapılardan geldiği düşünülürse](https://blog.chainalysis.com/reports/tornado-cash-ofac-designation-sanctions/), otoriteler tarafından aksiyon alınması kaçınılmazdı. 

|![Tornado_dagilim](/assets/TC_kaynaklar_800.png)|
|:--:| 
| *Tornado Cash'e gelen varlıkların kaynağı. Kaynak: [Chainalysis](https://blog.chainalysis.com/reports/tornado-cash-ofac-designation-sanctions/)*|

### Otoriteler ve merkezi kurumlar nasıl tepki verdiler?
ABD Hazine Bakanlığının kara para faaliyetlerini önleme alanında çalışan iki kurumu var. Bunlardan biri [FINCEN](https://www.fincen.gov/) (Financial Crimes Enforcement Network - Mali Suçları Araştırma Ağı)  diğeri ise [OFAC](https://home.treasury.gov/policy-issues/office-of-foreign-assets-control-sanctions-programs-and-information) (Office of Foreign Assets Control - Yabancı Varlıklar Kontrol Dairesi). FinCEN özellikle finansal kurumların şüpheli işlemleri belirleme konusunda izleyecekleri yol konusunda politikalar üretirken, OFAC direkt şüpheli kişi ya da kurumların [belirlenmesi](https://home.treasury.gov/policy-issues/financial-sanctions/specially-designated-nationals-and-blocked-persons-list-sdn-human-readable-lists) ve yaptırım uygulanması ile [uğraşıyor](https://cryptobriefing.com/makerdao-should-seriously-consider-preparing-for-dai-depeg-founder/). 

İşte bu iki kurumdan biri olan OFAC, 8 Ağustos 2022'de yayınladığı [bir bildiri](https://home.treasury.gov/news/press-releases/jy0916) ile Tornado Cash uygulamasını ve bu uygulama ile ilişkilendirdiği 38 adresi [yasaklı listesine](https://home.treasury.gov/policy-issues/financial-sanctions/recent-actions/20220808) (SDN - Specially Designated Nationals and Persons List) aldığını açıkladı. 

| ![tornado](/assets/cloud-4249184_800.jpg)|
|:--:| 
| *Image by [Agricom](https://pixabay.com/users/agricom-5627674/) from [Pixabay](https://pixabay.com/)*|

Bu açıklamanın hemen ardından Tornado Cash ile ilgili ardı ardına aksiyonlar gelmeye başladığını gördük. 

* Kripto dünyasının ikinci büyük stabil parası olan USDC'yi çıkaran Circle, Tornado Cash ile ilgili yaptırım listesine alınan hesaplardaki 75.000 USDC'yi [dondurdu](https://www.theblock.co/post/162172/circle-freezes-usdc-funds-in-tornado-cashs-us-treasury-sanctioned-wallets) (burada aklınıza 'İyi ama hani kriptoparalar sadece bana ait varlıklardı, başka kimse onlara dokunamazdı?' sorusu gelebilir. O dediğiniz daha çok BTC, ETH gibi merkeziyetsiz olarak kullanıma çıkmış paralarda geçerli bir durum. USDT, USDC gibi paralar merkezi yapılar tarafından çıkarılan akıllı kontratlar oldukları için bir hamle ile kullanıcının cüzdanında bloke edilebilirler).

* Sadece kripto değil tüm açık kaynak dünyasındaki uygulamaların bir arada bulunduğu ve geçtiğimiz yıllarda Microsoft tarafından satın alınan [Github](https://github.com/), Tornado Cash'in gelişmesine katkı veren hesaplara ait sayfaları [askıya aldı](https://twitter.com/semenov_roman_/status/1556717890308653059?s=20&t=f3MfLgufRQQ3WhQy5oGmkw).

* [Infura](https://infura.io/) ve [Alchemy](https://www.alchemy.com/) gibi merkezi altyapı sağlayıcılar, Tornado Cash ön yüzüne [ulaşımı kestiler](https://www.theblock.co/post/162402/infura-and-alchemy-blocking-access-to-tornado-cash).

* [dydx](https://www.coindeskturkiye.com/sirketler/dydx-bazi-hesaplari-engelledi-1473), Aave, Uniswap, [Balancer](https://twitter.com/BalancerLabs/status/1558212602257231873) benzeri merkeziyetsiz olma hedefinde olan ancak hâlâ merkezi unsurları bulunan protokoller web sitelerinden Tornado Cash ile etkileşime girmiş hesapları [bloke etmeye](https://cryptoslate.com/defi-protocols-aave-uniswap-balancer-ban-users-following-ofac-sanctions-on-tornado-cash/) ya da yetkililere bildirmeye başladılar.

* Tornado Cash'i yürüten DAO kendisini [feshetti](https://cryptoslate.com/tornado-cash-contributor-reveals-dao-shut-down-as-it-cant-fight-the-us-need-to-keep-contributors-safe/). Grup, Discord kanalını ve yönetim forumunu [kapattı](https://www.theblock.co/post/163228/tornado-cashs-discord-server-and-governance-forum-shuttered-amid-arrest) 

* Belki de en ilginç olanı, Hollanda resmi otoriteleri Tornado Cash geliştiricilerinden birini tutukladığını [açıkladı](https://www.coindeskturkiye.com/politika/supheli-tornado-cash-gelistiricisi-hollandada-tutuklandi-1493).

### Kripto dünyası bu konuda ne düşünüyor?
Tornado Cash'e karşı alınan bu aksiyonlar kripto dünyasında tam anlamıyla bir soğuk duş etkisi yarattı.  Konu ile ilgili pek çok kişi ve kurum tepki verdi. Bu tepkileri birkaç temel nokta çevresinde toplamak mümkün. 

ABD'nin bu hareketi öncelikle Tornado Cash'in verdiği hizmet üzerinden eleştiriliyor. Zira, bu uygulama temel olarak kişilere 'mahremiyet' konusunda fayda sağlıyor. 'Mahremiyet' ise temel vazgeçilmez özgürlüklerden bir tanesi ve özellikle blokzincir dünyasındaki kullanıcılar için hayati bir öneme sahip. Blokzincir hepimizin bildiği gibi oldukça şeffaf bir sistem. Kişi ismi görülmese bile hesapların ne yaptıkları herkes tarafından görülebiliyor. Bu da hesapları ve içindeki varlıkları dış tehlikelere açık hale getiriyor. Örneğin, Ukrayna'daki kuruluşlara yardım etmek isteyen bir kullanıcı, hesabından bir transfer yaptığı anda Rus tarafının radarına girip 'mimlenebiliyor'. Ya da hesabında yüklü miktarda para tutan biri, yapacağı herhangi bir işlemin karşı tarafça açığa çıkarılması riskini taşıyabiliyor. 

Elbette, blokzinciri üzerindeki varlıkların terörist aktivitelerde araç olarak kullanılmasını hiç kimse istemiyor, ancak bunun için temel özgürlüklerin kısıtlanması konusunda Amerikan kamuoyu oldukça hassas. ABD'li otoritelerin bu hareketini mideden ufak bir parça almak için girip karaciğer, dalak ve safra kesesini alan acemi cerrahın yaptığı ameliyata benzetenler var. 

İkinci eleştiri ise daha pragmatik. Kripto alanındaki saygın düşünce kuruluşlarından Coincenter, ABD'li otoritelerin 'sap ile samanı karıştırdığını' [iddia ediyor](https://www.coincenter.org/analysis-what-is-and-what-is-not-a-sanctionable-entity-in-the-tornado-cash-case/). Zira, bu tip listelere genel olarak kişi ya da kurumlar alınıyor. Burada ise kara listeye alınan bir uygulama! Kişiler ya da kurumlar kendi iradeleriyle hareket eder, yaptıklarından sorumlu olur ve gerekirse bu hareketlerinden geri dönebilirler. OFAC böyle bir merkezi yapı olan Blender uygulamasını Mayıs 2022'de kara listeye aldığını [açıkladığında](https://home.treasury.gov/news/press-releases/jy0768) kimsenin bir itirazı olmamıştı. Tornado Cash ise bir yazılım. Blokzincirin değiştirilemez özelliği gereği bir kez hizmete sunulduktan sonra isteyenin dilediği gibi kullanabileceği ve bunu kimsenin engelleyemeyeceği bir yazılım. ABD'nin bu hareketi, aslına bakarsanız, ekmek bıçağı ile cinayet işlendiği için bıçak üreticilerini tutuklamaya benziyor.  Coincenter'a göre, Tornado Cash'i çıkaran bir kurum ya da grup varsa bunlar yaptırım altına alınabilir ama uygulamaya ya da onu kullananlara getirilecek yaptırım maksadını aşıyor ve muhtemelen dava edilerek ABD Anayasa Mahkemesinden geri dönecek bir hareket. 

### Arkası yarın
Buraya kadar, Tornado Cash olayını ve arkasından yaşananları toparladık. Bir sonraki yazımızda kripto dünyasının bu karara karşı kısa ve uzun vadeli verdiği tepkiler ve protokoller, geliştiriciler, altyapı platformlarını nelerin beklediğine değineceğiz. 


---

*Not 1: Bu yazı ilk olarak 20 Ağustos 2022'de [Coindesk Türkiye](https://www.coindeskturkiye.com/))'de [yayınlandı](https://www.coindeskturkiye.com/yazarlar/turan-sert/tornado-cash-olayi-ve-dusundurdukleri-1602)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*
