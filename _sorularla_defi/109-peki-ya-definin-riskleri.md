---
layout: book-section
kind: section
title: "Peki ya DeFi’nin Riskleri? – Sorularla DeFi"
heading: "Peki ya DeFi’nin Riskleri?"
chapter: 1
chapter_title: "Nedir DeFi?"
order: 109
permalink: /Sorularla_DeFi/bolum-1/peki-ya-definin-riskleri/
description: "DeFi’nin başlıca riskleri akıllı kontrat hataları, birlikte çalışan ürünlerin zincirleme etkilenmesi, küçük ekiplerin yönetici anahtarları, merkezi borsaların yönetimde orantısız güç kazanması, kriptoparaların inişli çıkışlı olması, manipüle edilebilen dış veriler (oracle) ve altyapının ölçeklenmesi. Korunmak için kendi araştırmayı yapmak, dış denetimden geçmiş projelere bakmak ve sigortadan yararlanmak öneriliyor."
---

Peki ya DeFi’nin riskleri yok mu? Olmaz mı? Hem de istemediğiniz kadar. Neler diye merak ediyorsanız sizi şuraya alalım:

## Nedir DeFi’nin riskleri ve varsa önlemleri? {#nedir-definin-riskleri-ve-varsa-onlemleri}

Risk hayatın bir parçası. Maalesef genel olarak riski, ‘var ya da yok’ denkleminde değerlendirmeyi seviyoruz. Halbuki, riskin de onlarca tonu var. Örneğin, sabah evden çıkıp sokakta yürümeye başladığınızda bile aslında risk alıyorsunuz. Allah korusun, araba çarpabilir, balkondan saksı düşebilir gibi... Peki bu nedenle sokağa çıkmamalı mı? Tabii ki hayır. İki gökdelen arasına ip bağlayıp üzerinde yürümekle sokakta yoldan karşı karşıya geçmek tabii ki farklı riskler.

Önemli olan riskin ve derecesinin farkında olmak. Gelin DeFi’de kullanıcıların karşılaşabileceği risklere kısaca göz atalım şimdi:

### En önemli risk akıllı kontrat kodlamasında {#en-onemli-risk-akilli-kontrat-kodlamasinda}

DeFi projelerinin özünde müşterilere sunulan birer akıllı kontrat olduğunu belirtelim. Bu akıllı kontratların ise özünde birer yazılım olduklarını ekleyelim. Bu kontratları yazanlar birkaç geliştirici. Örneğin, bir sonraki bölümde bahsedeceğimiz DeFi alanındaki en büyük protokol olan Uniswap’ın kurucusunun, 6 Ocak 2021’de attığı bir [tweetten](https://twitter.com/haydenzadams/status/1346575665940860929?lang=en), 3 milyar ABD Doları piyasa değeri olan protokolün sahip olduğu ekip elemanı sayısının 11 olduğunu öğreniyoruz. Kodun içinde yazım hataları olması, kimi senaryo ve parametrelerin unutulmuş olması gayet olası. Bu tip hataların şakaya gelir yanı yok, bu kontratlara ciddi miktarda para yatırıyor insanlar.

### Birlikte çalışabilme güzel fakat... {#birlikte-calisabilme-guzel-fakat}

DeFi’nin temel özelliklerinden bahsederken, klasik finansa göre en önemli farkın, DeFi ürünlerinin birbirleri ile çalışabilmesi olduğunu belirtmiştik. Örneğin, farklı DeFi ürünlerine yatırım yapmayı kolaylaştıran DeFi portföy yönetimi yearn.finance kullanırken, hatırı sayılır sayıda akıllı kontrat bir arada çalışıyor. Bunu Jenga oyununda üst üste koyduğunuz taşlara benzetebiliriz. Alttaki taşlardan birinin oynaması tüm kuleyi yıkabilir. Bir önceki maddede bahsettiğimiz bir protokolün kullandığı akıllı kontratların herhangi birinde çıkacak bir sorun, bu protokol ile entegre çalışan diğer ürünlerin de canını ciddi şekilde yakabilir.

### Ufak ekiplerin yönettiği projelerde operasyonel riskler olabilir {#ufak-ekiplerin-yonettigi-projelerde-operasyonel-riskler-olabilir}

DeFi protokollerinin getirdiği merkeziyetsizliğin aslında bir vizyon olduğunu da unutmayın. Hemen hemen her proje merkezi başlar ve yavaş yavaş merkeziyetsiz hâle gelir. Başlangıçta merkezi başlayan protokollerde, ürün geliştirmenin ufak bir ekip tarafından yapıldığını belirtelim. Hızlı davranabilmek ve ürünlerin geliştirme aşamasında sıkça rastlanacak hataları gidermek için başlangıçta ekiplerin projenin yönetici anahtarlarına sahip olduğunu da ekleyelim. Ekip üyelerinin elinde olan bu anahtarların kişilerin kötü kullanımına yol açabileceğini unutmayın. Özellikle, kimi blokzincirlerde yeni başlayan projelerde; ‘rug-pull’ (halıyı altından çekmek) olarak bahsedilen hareketle ekip üyelerinin proje havuzlarına yatırılan paraları alıp kaçtığını da hep birlikte gördük.

### Merkeziyetsiz yönetimler henüz oturmuş değil {#merkeziyetsiz-yonetimler-henuz-oturmus-degil}

Projeler gelişmeye başladıkça yavaş yavaş yönetimi bırakmaya başlıyorlar. Merkeziyetsiz yönetim, stratejik kararları verme hakkının projenin yönetim tokeni sahiplerine devredilmesi anlamına geliyor. Devir sonrası token sahiplerinin nasıl hareket edecekleri önem kazanıyor.

Kimi durumlarda, aldıkları tokenleri kendi cüzdanlarına çekmeyip borsada tutan yatırımcılar nedeniyle bazı merkezi borsalar, projenin yönetiminde ‘orantısız’ bir güce sahip olabiliyorlar. Bu ağırlık projenin selameti açısından risk yaratabilir. Örneğin, merkezi borsanın projenin büyümesinden çok kısa vadeli kâr getirecek stratejik hamlelere odaklanması gayet olası. Öte yandan, kimi merkezi borsaların kendi blokzincirleri üzerinde DeFi ürünlerine ev sahipliği yaptığını düşünürsek, yönetim tokenine sahip oldukları başka blokzincirlerde kurulu projeler içinde söz sahibi olmaları risk yaratabilir.

### Kriptoparaların inişli-çıkışlı olması da bir risk {#kriptoparalarin-inisli-cikisli-olmasi-da-bir-risk}

Kriptoparaların ne kadar inişli-çıkışlı (ya da İngilizceden dilimize geçmiş bozuk kelimelerden biri ile ‘volatil’) olduğunu söylemeye gerek yok sanırım. İşte bu iniş-çıkışlar kimi durumda yatırımcı ya da işlem yapanlara sıkıntılı zamanlar geçirtebiliyor. Özellikle borçlanma platformunu kullanırken, alınan kredi karşılığı teminat olarak kriptopara veriliyor. Genel olarak yüksek oranda (İngilizcede ‘over-collateralized’) olarak verilen bu teminatlar belli bir seviyenin altına düşerse, teminat likide ediliyor. Kripto piyasasının 7/24 çalışması nedeniyle, olası ani inişlerde, teminat oranının üstünde kalmak zor olabiliyor. Burada yatırımcı hızlı hareket ederek; ya teminat verdiği kriptopara miktarını artırmalı ya da aldığı kredinin bir kısmını geri ödeyerek teminatının likide edilmesini önlemeli.

### Dışarıdan alınan bilgiler manipüle edilebilir {#disaridan-alinan-bilgiler-manipule-edilebilir}

DeFi projelerinin üzerine kurulu oldukları blokzincir altyapıları (örneğin Ethereum), doğaları gereği akıllı kontratların zincirin dışıyla iletişim kurmasına olanak vermezler. Akıllı kontratların ise belli koşullar oluştuğunda harekete geçmeleri gerekir; ancak koşulların oluştuğu bilgisine ihtiyaçları var. Bu dışarıdan gelecek bilgiyi onlara oracle denen bilgi kaynakları sağlar (Daha detaylı bilgiyi ‘Chainlink: DeFi’nin bilgi kaynağı’ bölümümüzde bulabilirsiniz). Bu bilgi başka DeFi projelerinden, başka blokzincirlerden ya da tamamen fiziksel hayattan bile gelebilir. DeFi projeleri kimi zaman oracle kaynakları maliyetli olduğu için, bilgiyi kendileri bir-iki blokzincir içindeki kaynaktan almayı seçebiliyorlar. Bu kaynakların manipüle edilmesi nedeniyle projeye yanıltıcı bilgi gelmesi durumunda ise proje yatırımcıları zarara uğrayabiliyor.

### DeFi altyapı projelerinin ölçeklenmesi de bir problem {#defi-altyapi-projelerinin-olceklenmesi-de-bir-problem}

Piyasada endişenin hakim olduğu ya da ufak çaplı krizlerin yaşandığı ortamda, DeFi projelerinin üzerinde yer aldığı altyapı projelerine adeta bir hücum başlıyor. Bu da projelerin kimi durumlarda yüksek talebi karşılayamaz hâle gelmesine yol açabiliyor. 2021 yılının Mayıs ayında yaşanan krizde, Ethereum projesi alnının akıyla krizden çıkarken, rakip birkaç projede ciddi sıkışmalar yaşandığını gördük. Öte yandan, Ethereum herhangi bir durma yaşamadan krizden çıkarken, işlem ücretlerinin arşa çıktığını da belirtelim. Böyle bir durumda maliyetlerin yüksekliğinin farkına varmayan yatırımcılar, düşük ücretler ile işlem yapmaya kalktıklarında saatlerce beklemek zorunda kaldılar.

## Peki nasıl korunabiliriz bu risklerden? {#peki-nasil-korunabiliriz-bu-risklerden}

DeFi’nin de riskleri ile ilgili aslında en büyük sorun, bu riskleri değerlendirme sıkıntısından kaynaklanıyor. Risklerin neler olduğunu görebiliyorsunuz; ancak olma ihtimalini ve olduğundaki zararı kestirmek zor olabiliyor. Bunun da temel nedeni DeFi sistemlerinin henüz yeni olması.

### Mutlaka kendi araştırmanızı yapmak gerek {#mutlaka-kendi-arastirmanizi-yapmak-gerek}

Öncelikle, daha önceki bölümlerde bahsettiğimiz; yatırım yaparken yaptığınız incelemelerin tamamını, kullanacağınız platformlar için de yapmanız gerekiyor. Kripto dünyasının en temel düsturdur bu: “Kendi araştırmanı kendin yap.” (İngilizcede ‘Do your own research’ - DYOR) Çok meşakkatli bir iş olduğunun, çoğumuzun özellikle teknik olarak bu protokollerin ne iş yaptığını bile bilmezken onların doğru çalışıp çalışmadığını anlamanın zorluğunun farkındayım. İşte tam da bu nedenle, bu alana yatırım yapmayı düşünenlerin yüksek risk altına girdiklerini iyi anlaması gerekiyor. Göreceli olarak riski azaltacak konuların başında ise olabildiğince çok okuyarak bilgi sahibi olmak geliyor.

### DeFi diye, denetim yaptırmayacak değil elbet {#defi-diye-denetim-yaptirmayacak-degil-elbet}

Akıllı kontrat yazılım hatalarını önlemenin bir yolu yok mu? Tabii ki bolca test yapmak, farklı senaryoları düşünmek ve buna göre akıllı kontratı kurgulamak önemli ancak yeterli değil. Bu alanda, dış denetim yapan firmalar mevcut. Projelerin dış denetimden geçmiş olmaları, risk olmadığı anlamına gelmese de en azından bilinen belli risklere karşı yatırımcılara bir güven veriyor. Bu firmalar ile ilgili en büyük sıkıntı ise, hem oldukça pahalı hem de DeFi alanındaki rekabet nedeniyle oldukça yoğun olmaları. Yine de son kullanıcıların, projelerin web sitelerinden yapılmış olan dış denetimlere dikkat etmeleri gerekiyor. Bu alanda belli başlı büyük protokolleri inceleyerek onlara puan veren [DefiSafety](https://defisafety.com/) benzeri siteler de projeler konusunda fikir verebilir.

### Yeni proje yüksek risk demek {#yeni-proje-yuksek-risk-demek}

DeFi projeleri zamana karşı yarıştıkları için çoğu zaman bu tip denetimleri yaptırmadan piyasaya çıkıyorlar. Açıkçası son kullanıcının, yeni çıkmış projelere baştan tüm paralarını kaybetmeyi göze alarak yatırım yapmalarını söylemek en sağlıklısı. Projenin eski olması ile içerdiği risk arasında ters bir orantı olduğu da söylenebilir: Bir ürün ne kadar uzun süredir hizmet veriyorsa, kodlama anlamındaki risk de göreceli olarak o kadar azalıyor denebilir.

### Sigorta imkânı da var {#sigorta-imkani-da-var}

Öte yandan dileyen yatırımcılar kullandıkları protokollerin belli risklerine karşı sigorta yaptırabilirler. (Bir sonraki kısımda bulunan ‘Nexus Mutual: DeFi’nin sigortası’ bölümünde bu konuya detaylı olarak bakacağız.) Hemen belirtelim, bu sigortaların da kapsama alanları şimdilik oldukça dar. Zamanla DeFi projeleri olgunlaşırken, farklı risklerin de sigortalanmaya başladığını göreceğiz.

### Zaman pek çok sorunun ilacı {#zaman-pek-cok-sorunun-ilaci}

DeFi projelerinin yaşadıkları sıkıntılardan ders çıkarmaları önemli. Örneğin, bir sonraki bölümde detaylıca bahsedeceğimiz MakerDAO; 2020 yılının Mart ayında yaşanan Kara Perşembe olayında yatırımcılarına para kaybettirmiş iken (sonra bu kayıpları kendi hazinesinden karşıladı), 2021 yılının Mayıs ayında yaşanan benzer krizden herhangi bir sorun yaşamadan çıktı. Keza, Ethereum blokzinciri üzerinde yaşanan yoğunluk, kuvvetle muhtemelen 2022 yılı içinde gelecek ETH 2.0 yeni versiyon ile bir nebze azalacak (ki öncesinde ikinci seviye çözümler ile de yoğunlukta azalma emareleri görülmeye başladı bile).

## Sonuç {#sonuc}

DeFi ürünleri, yap-boz şeklinde gelişiyorlar. Doğal olarak bunların bir kısmı benimsenecek, muhtemelen pek çoğu da batacak. Bu durumu azımsamak, küçümsemek yerine böyle olduğunu kabullenip ona göre değerlendirmek önemli; zira bu alanda ayakta kalacak projelerin uzun vadede kullanıcılara, dijital dünyada finansal özgürlük anlamında ciddi kazanımlar sağlayacağını unutmamak gerekiyor.
