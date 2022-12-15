---
layout: post
title:  "FTX Olayı ve DeFi'ye Etkisi"
date:   2022-11-14 12:17:56 +0300
categories: Genel
tags: Yazılar, DeFi, CoindeskTR
---

Bu yazımızda sonu FTX'in iflası ile biten geçen hafta yaşanan olaylardan ve bu olayların merkeziyetsiz finansa etkilerinden bahsedeceğiz. 

### Sağır sultanın bile duyduklarını hatırlayalım önce
Öncelikle neler olduğunu basında yer aldığı şekliyle hatırlayalım:

Olaylar zinciri, Coindesk'in 2 Kasım tarihinde FTX (borsa) ve Alameda Research (kardeş kuruluş olan alım-satım firması) arasındaki girift ilişkileri [haber yapmasıyla](https://www.coindeskturkiye.com/sirketler/sam-bankman-friedin-iki-sirketi-ayni-bilancoda-bulusuyor-2581) başladı.

Haber bir-iki kişiyi huylandırsa da başlangıçta finans çevrelerinde çok büyük bir yankı getirmedi. Ne de olsa, FTX'in sahibi olan Sam Bankman Fried ([SBF](https://twitter.com/SBF_FTX)), başkanlık yarışındaki adaylara hatırı sayılır bağışlar yapmış, uzun süredir DC'de lobi faaliyetlerinde bulunan kıvırcık saçlı dahi bir çocuk idi. Regülatörler ile bu kadar sıkı-fıkı olan ve tüm sektöre düzenlemelerin nasıl olması gerektiği konusunda akıl satan biri elbette kendi evini de düzenli tutardı; haber muhtemelen çok da kritik görülmemişti. 

Sonrasında asıl fırtına, 6 Kasım Pazar akşamı Binance'in sahibi olan [Changpeng Zhao](https://twitter.com/cz_binance) (CZ)'nin ellerinde bulunan FTX borsasının tokeni olan FTT'leri piyasada satacağını [açıkladığı tweet](https://twitter.com/cz_binance/status/1589283421704290306) ile koptu. FTX ve Alameda'nın likidite yetersizliği ile ilgili söylentiler arşa çıktı ve Pazartesi akşamı SBF, FTX'in satışı için CZ ile anlaştığını [duyurdu](https://twitter.com/sbf_ftx/status/1590012124864348160). Satışin ilk aşaması olan ön incelemenin (ingilizcede 'Due-Diligence' kısaca DD) daha henüz ikinci günündeydik ki, Binance FTX'i almaktan [vazgeçtini açıkladı](https://twitter.com/binance/status/1590449161069268992). 10 Kasım Perşembe günü hata yaptığını kabul eden ve şirketi kurtarmak için yatırımcı aradığını açıklayan SBF [tweetinin](https://twitter.com/sbf_ftx/status/1590709166515310593) ertesi günü, 11 Kasım'da FTX çatısı altındaki [134 kuruluş](https://twitter.com/sbf_ftx/status/1590709166515310593) iflas koruma istemiyle mahkemeye başvurdu. 

Böylece kripto dünyasının kimine göre ikinci, kimine göre üçüncü büyük kriptopara borsasının tam altı günde (Pazar'dan Cuma'ya) gözlerimizin önünde çöküşünü izledik. En son [Ocak ayında 32 milyar ABD Doları üzerinden](https://cryptobriefing.com/ftx-raises-400m-at-32b-valuation/) yatırım alan FTX'in değeri sıfıra indi. Daha hafta başında 16 milyar ABD Doları olduğu tahmin edilen SBF'in kişisel serveti de [benzer şekilde buhar oldu](https://twitter.com/WatcherGuru/status/1591062761316155393). İnanılmaz değil mi?  Gelin şimdi işin içine biraz daha girelim ve Amerikalıların 'peel the onion' dedikleri (Türkçesi 'soğanı yavaş yavaş soyup cücüğüne ulaşmak' oluyor ama ben şu yaşıma kadar böyle bir deyiş duymadım) işin temeline inmeye çalışalım.

### FTX özelinde sorun nereden çıktı?

Sorunun ne olduğu ile ilgili pek çok söylenti var. Söylenti olmasının temel nedeni, kimsenin şirketin finansal durumuna hakim olmaması. Bilinen temel gerçek FTX'in müşteri fonlarını Alameda'ya kullandırmış olduğu. Peki FTX, herkesin gözü önünde bunu nasıl becerdi?

Hikayeyi en başa saralım: 2017 yılında ilk olarak Alameda Research'i kuran SBF, değişik ülkelerde (özellikle Japonya'da) Bitcoin fiyatlarının farklı olmasında kaynaklanan arbitraj fırsatlarını değerlendirerek para kazanıyor. Bu fırsatlar bitince borsalara likidite sağlamak olarak adlandırabileceğimiz piyasa yapıcılık işine soyunuyor. Ardından da 2019 yılında FTX borsasını kuruyor; böylece likidite sağlayıp başkasına kazandırdığı paradan kendisi de pay almak istiyor.

Buradan sonrası eğer iddalar doğru ise tam bir yozlaşma hikayesi: FTX, kendisine gelen büyük alım emirlerini işlemi gerçekleştirmeden önce Alameda'ya haber veriyor. Alameda da bu sayede emir öncesi işleme konu tokeni ucuzdan alıp emir sonrası satarak risksiz kâr elde ediyor (Ingilizcede 'front-running' denen olay).

Bu hikayenin bir parçası. Öte yandan, Alameda'nın yaptığı işlemler (al-sat ya da uzun vadeli portföy yatırımları) için nakde ihtiyaç var. Nereden bulacak parayı? FTX'de kuzu kuzu yatan müşteri paraları var ya?. İyi ama FTX çok transparan olmakla övünüyor, denetimden geçiyor; öyle parayı açık açık Alameda'ya veremez. Nasıl yapacaklar bunu? İşte burada kadraja FTX'in kendi çıkardığı borsa tokeni olan FTT giriyor. 

FTT temelde borsada işlem yaparken komisyon indirimi sağlayan bir token. Aynı zamanda FTX borsasında işlem görüyor, yani görünürde likit bir piyasaya sahip. Ama aslına bakarsanız FTT'nin çok küçük bir kısmı piyasada bulunmakta ve fiyatı FTX tarafından kolayca manipüle edilebiliyor. Sistem şöyle işlemiş:

En başta, Alameda Research FTX'in çıkardığı FTT'leri çok ucuzdan satın alıyor. Sonrasında FTT'nin fiyatını FTX üzerinde uçuruluyor. Alameda ucuzdan aldığı ve artık fiyatı katlanmış olan FTT'leri FTX'e teminat olarak gösteriyor ve karşılığında kredi alıyor. Alan memnun, satan memnun, FTX'in yatırımcıları da memnun (FTX kâr ediyor çünkü). Sorun nerede? Bu sistem nereye kadar devam eder?

Coindesk haberi sonrası dikkatlerin üzerine çevrildiği bu saadet zincirini patlatabilecek tek bir kişi var. O da CZ. Zira CZ, zamanında FTX kurulurken ona yatırım yapmış sonra 2021 yılında bu yatırımdan oldukça kâr ederek çıkmış. Çıkarken kendisine BUSD ve FTT verilmiş. [Elinde geçen hafta itibariyle en 580 milyon doları değerinde FTT](https://twitter.com/cz_binance/status/1589329217874931712?s=20&t=E39sb1uZkzbNhCt2DJLn5g) var. Geçen Pazar akşamı [attığı tweet](https://twitter.com/cz_binance/status/1589283421704290306) ile bu FTT'leri satacağını açıklaması, zaten çok az likiditesi olan token fiyatının satış baskısı nedeniyle inişe geçmesi demek. FTT'de yaşanan çöküş ise, Alameda'nın borçlarına karşı verdiği FTT teminatın erimesi ve firmanın açığa düşmesi anlamına geliyor. 

Alameda Pazartesi günü panik halindeki yatırımcıların yaptığı satışları karşılamak ve FTT fiyatını 22 dolarda tutmak için büyük savaş verse de sonunda yenik düşüyor. Sonuç olarak bir tweet koca bir yapının temelindeki taşın çekilmesi ve kumdan kulenin yıkılmasına neden oluyor. 

| ![sand_tower](/assets/sand-2549096_800.jpg)|
|:--:| 
| *Image by [flockine](https://pixabay.com/users/flockine-5479910/) from [Pixabay](https://pixabay.com/)*|

### Genel olarak sorunun temeli nerede?
Bugün yaşanan olayların izini bu yıl meydana gelen UST/LFG (Luna/Terra) ve sonrasındaki 3AC [krizlerine kadar dayandırmak](/genel/2022/07/22/finansin-domino-taslari-son-krizde-neler-yasandi.html) mümkün.

Genel olarak yaşananı, DeFi'nin 2020 yılı ortasından itibaren yarattığı rüzgarı kullanan merkezi yapıların, oluşan özgür ortamı dejenere etmesi olarak özetleyebiliriz. DeFi'de neredeyse bir yılda bir milyar ABD Dolarından yüz yirmi milyar ABD Dolarına [yükselen](https://defillama.com/) baş döndürücü büyüme yaşandı. **Herkes bu büyümenin artan yatırımcı ilgisi sonucu oluştuğunu düşünse de, arkada yatan esas nedenin merkezi yapıların hesapsız kitapsız kullandığı krediler ile gerçekleştirdiği kaldıraçlı işlemler olduğu sonradan anlaşıldı**. 

İşler iyi giderken herkesi mutlu eden bu durum, rüzgar tersine döndüğünde önce UST'yi, sonrasında başta 3AC olmak üzere Voyager, Celsius gibi pek çok yapıyı [çöküşe sürükledi](/genel/2022/07/22/finansin-domino-taslari-son-krizde-neler-yasandi.html). Krizin baş mimarları ile çalışan daha pek çok kurum vardı ama başlarını suyun üstünde tuttuğu sürece kimse ne kadar hasar aldığını açıklamadı. Görünen o ki, o arada zarar gören firmalardan biri de FTX ve Alameda oldu. Üstüne üstlük, SBF o dönemde BlockFi ve Voyager gibi zordaki kurumlara yatırım yapmasıyla ön plana çıkmıştı. O zamanlar piyasada 'beyaz şövalye' olarak adlandırılan SBF'in bunu gerçekten bu amaçla mı, yoksa kendi zararlarını gizlemek amacıyla mı yaptığını kimse bilmiyor [^1]. Neden?

Buradaki temel sorun, bu merkezi yapıların tamamen birer kara kutu gibi çalışıyor olmaları. DeFi'nin inanılmaz yükselişi sırasında elde edilen kârların ve büyüme hırsının bu alanda at koşturan merkezi yapıları gözünü kararttığından yukarıda bahsettik; ancak konu sadece bu oyuncular ile sınırlı değil. Bu oyuncular kadar bunlara sermaye koyan girişim sermayesi fonlarının ya da borç veren diğer merkezi yapıların da gözlerine perde inmiş olduğunu anlıyoruz. FTX'in zaman zaman çıktığı yatırım turlarında, yatırımcılara sunduğu raporlarda (denetimsiz birkaç sayfalık notlar) sunulan kâr rakamlarının kimse tarafından sorgulanmadığını duyuyoruz. Aynı şekilde bu fonların ya da borç verenlerin, FTX ile Alameda arasındaki çarpık ilişkiyi yeterince sorgulamadığını okuyoruz. 

"Burası yepyeni bir dünya, burada kurallar farklı" söylemi ile sap ile samanın kasıtlı olarak birbirine karıştırıldığını söylemek mümkün. Burada karıştırılan sap ve saman,  insanlar tarafından yönetilen merkezi yapılara merkeziyetsiz yapılarmış gibi davranılması. 

Merkeziyetsiz yapıların birer yazılım (akıllı kontrat) olduklarını, sadece blokzincir üzerinde çalışabileceklerini ve bu sayede yaptıkları işlemlerin ve sonuçların şeffaf bir şekilde herkesin denetimine açık olduğunu anlamamız gerekiyor. 

Merkezi ya da yarı-merkezi yapılarda ise bunu söylemek mümkün değil. Zira insan, girdiği her alanı 'kirletme' kapasitesine sahip. Peki o zaman ne yapacağız? Merkezi yapılar her zaman olacak, olmalı da. En azından yapılması gereken, bu yapılarda şeffaflığı sağlamak. Nasıl olacak bu? Gelin ona bakalım şimdi de.

### Bu sorunlardan kurtulmanın yolu ne?
Yaşananlar acı, parası kalanlar için üzücü. Maalesef burada elimiz kolumuz bağlı. Tek konuşabileceğimiz gelecekte bu tip olayların önlenmesi için neler yapılabileceği. 

#### Merkezi yapılar
Merkezi yapıların ise, artık yaşanan vahşi batı ortamında kendilerine çeki düzen vermeleri şart oldu. Bunun da birbirine geçmiş iki yöntemi var. 

Birincisi öz denetim, yani müşteriler adına emanet tutulan paralar. FTX'de yaşananlardan sonra spotların kendisine çevrileceğini bilen CZ'nin müşteri hesapları için rezerv-kanıtı (ingilizcesi proof-of-reserves) yöntemini [vurgulaması](https://twitter.com/cz_binance/status/1590694652088582144) akıllıca bir hamle. Zaten sonrasında pek çok borsa benzer açıklamalarda [bulundular](https://cointelegraph.com/news/binance-proof-of-reserve-pledge-gains-support-following-ftx-crisis). Bu hamle ile borsalar müşteri paralarını başka yerlere harcamadıklarını blokzincir üzerinde kanıtlayabiliyorlar. 

İkincisi ise merkezi yapıların blokzincir dışı yükümlülükleri ve bunları karşılayacak varlıklarının (banka kredisi, diğer kurumlar ile olan blokzincir dışı borç-alacak ilişkileri gibi) tam olarak anlaşılması için dış denetime tabi olmaları ve denetlenmiş rakamlarını kamuoyuna açıklamaları gerekli.

#### Kanuni ve düzenleyici otoriteler
Tabii gözler bir yandan da kamu otoritelerine çevriliyor. Bu tip borsalarda geniş kitlelerin paraları emanet alındığı için denetleyici kurumlar da devreye girebiliyor. Buradaki temel sıkıntı yeni bir teknoloji olan kripto alanında otoritelerin çok haklı olarak bekle gör politikası izlemeleri ve kanuni altyapıyı henüz oluşturmamış olmaları. (FTX olayında, SBF'in yaptığı lobi ödemelerinin, DC'deki denetleyici kurumlar ile sıkı fıkı olmasının ya da ABD'li bir kongre üyesinin [iddia ettiği gibi](https://twitter.com/RepTomEmmer/status/1590717374801809409) SEC başkanı Gensler ile yakın ilişkilerinin kendisine ne kadar fayda sağladığı - otoriteler tarafından üzerine gidilmemesi gibi - belki önümüzdeki dönemde daha da açığa çıkar). 

Burada otoritelerin önündeki en büyük engel, bu dünyayı anlamak ve sektörün büyümesini sekteye uğratmayacak şekilde gerekli düzenlemeleri yapabilmek. Bunun da aslında çok temel bir prensibi var: **Eğer bir kurum hangi nedenle olursa olsun müşterinin varlığını elinde tutuyor ise, geleneksel bir finans kurumu gibi mali ve organizasyonel olarak yeterli olduğunu kanıtlamalı ve bu durum otoriteler tarafından denetlenmeli. Bu durumun merkeziyetsiz yapılar için geçerli olmadığını, zira orada kullanıcıların varlıklarını kendi egemenliklerinde tuttuklarını belirtmek gerek.** 

#### Merkeziyetsiz yapılar
Bütün bu hazin olaydan belki olumlu çıkarabilecek tek sonuç, merkezi ve merkeziyetsiz yapı farkının bir kez daha gözler önüne serilmesi oldu. Merkeziyetsiz yapılar tüm bu süreçten hasarsız bir şekilde çıktılar. 

Gelecek dönemde bu yapılar için sorun olabilecek en önemli konu, merkezi yapıların yaşadıkları güçlüklerden dolayı ellerinde tuttukları tokenleri satma ihtimalleri nedeniyle piyasada yaşanabilecek artçı sarsıntılar olacak. Zira Alameda ve FTX Ventures'un yatırım yaptığı [toplam 255 girişim var](https://twitter.com/Edvis100/status/1591106598436761603). 

Elbette, sorun yaşayan kurumlardan dolayı tüm kripto dünyası imaj ve güven kaybına uğradı. Örneğin kısa vadede, geçtiğimiz hafta açıklanan ABD enflasyon verileri sonrası tüm piyasalarda bir coşku yaşanırken, kriptoparalar diğerlerinden negatif olarak ayrıştı. Bu alanda çalışan onlarca girişim ve binlerce insan var. Birkaç kendini bilmez kişinin yüzünden kısa vadede bu insanların zorluk yaşayacak olması çok acı. Yine de, yakın vade atlatıldıktan sonraki dönemde merkeziyetsiz yapıların önünün daha da açılacağını söyleyebiliriz. 

#### Kullanıcılar
Kullanıcılar açısından ise, hep söylediğimizi tekrar edelim. Kripto dünyasının size verdiği en büyük güç, paranıza tamamen egemen olmanız. Bunu lütfen kullanın. Bu dünyada paranızın güvenliği için kriptopara borsalarına ihtiyacınız yok, onu kendiniz sağlayabilirsiniz. Zahmetli mi, evet (orada da yeni gelişmeler daha güvenli ve zahmetsiz hale getirecek bu süreci), ama bunu yapmak zorundasınız. Kendi kişisel kripto cüzdanınıza sahip olmak çok önemli. Bunu yapmayacak kadar kendinizi ehil hissetmiyorsanız, belki de finansal riskleri zaten çok yüksek olan bu dünyadan uzak durmanız sizin için en hayırlısı olabilir. 

### Sonuç
FTX/Alameda olayından çıkarılacak pek çok ders var. Çok popüler karşılanmayacak olsa da, bu talihsiz olayın uzun vadede merkeziyetsiz sistemlerin gelişmesi için sağlıklı  olacağını düşünüyorum[^2]. FTX gibi kapalı kutu yapıların aksine DeFi, tüm topluma şeffaf ve denetlenebilir bir altyapı sunuyor. 

Sektör öz denetimin ne kadar önemli olduğunun bir kez daha farkına vardı. Bundan sonra kurumlar, imaj (dahi çocuk, değişen dönem, hızlı davranma vs vs) yerine eski dünyanın temel kriterlerine (değer önerisi, kârlılık, alınan risk, girilen ilişkiler, denetim gibi) çok daha fazla önem vereceklerdir diye umuyorum. 

Bundan sonra bu olayları yaşamayacak mıyız? Gayet tabii benzerleri ileride de olacak. İşte burada da merkeziyetsiz kurumlar daha ön plana çıkacak. Merkeziyetsiz girişimler içinde de,  zamanla kullanımları arttıkça teknik risklere karşı kurşun geçirmez hale gelen, kullanıcı dostu ve net değer önerisi yaratanlar ön plana çıkacak. Bu tahminler doğru çıkacak mı, hep birlikte yaşayarak göreceğiz.

Notlar:

[^1]: FTX’in BlockFi’yi satın alması sonrası şirketi kendi emanet çözümleri kullanmaya zorladığı ve böylece BlockFi müşterilerinin paralarını kendisine çekmeyi amaçladığı [şeklinde bir söylenti](https://twitter.com/AutismCapital/status/1591103568123408384) de var.  Bir başka spekülasyon ise, Alameda'nın piyasa yapıcılığı işinden sürekli bir zarar yaptığı, normalde böyle bir piyasa yapıcının dükkanı kapatıp gitmesinin mantıklı olduğu ancak bunun FTX'in can damarı olan likiditenin kesilmesine neden olacağı için SBF'nin böyle bir hamle yapamadığını [söylüyor](https://twitter.com/0xdoug/status/1591161987547168768).

[^2]: Bu arada ilk seçenek olan Binance'in FTX'i alma senaryosunun çok daha vahim sonuçları olabilirdi. Zira bu bir kara kutunun diğerini satın alması ile daha büyük bir kara kutunun ortaya çıkması demek olacaktı. Bu da uzun vadede daha büyük riskler doğurabilirdi.

Yazı dışında görsel olarak ilgi duyarsanız, konuya ilişkin hazırladığımız DeFine programına da göz atabilirsiniz. 

<table>
<td style="width:33%"><iframe width="224" height="126" src="https://www.youtube.com/embed/Ra4x4IF5UAA" frameborder="0" allowfullscreen></iframe>
</td>
</table>

---

*Not 1: Bu yazı ilk olarak 17 Ekim 2022'de [Coindesk Türkiye](https://www.coindeskturkiye.com/)'de [yayınlandı](https://www.coindeskturkiye.com/yazarlar/turan-sert/ftx-olayi-ve-defiye-etkisi-2696)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*
