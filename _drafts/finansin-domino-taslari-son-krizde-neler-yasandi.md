# Finansın Domino Taşları - Son Krizde Neler Yaşandı? - 1

Bu yazımızda, son zamanlarda DeFi'de yaşanan olayları mercek altına alıyoruz. Nasıl başladı, son gelişmeler neler, sorunun kaynağı ne?

Yaklaşık iki ayı aşkın bir süredir kriptopara piyasalarında derin bir karamsarlık söz konusu. Özellikle sektörün iki büyük parası BTC ve ETH'nin düşüşüne paralel yaşanan iflas olayları ve zor duruma düşen kurumsal yatırımcı haberleri bu karamsarlığın temel nedenleri arasında.

### Nasıl başladı?

8 Mayıs tarihinde UST'de yaşanan sıkıntı ile başlayan ve sonrasında domino taşları gibi teker teker birbirini etkileyen olaylar zincirinin başrol oyuncularını inceleyelim öncelikle:

| ![domino_falls](/assets/domino-163523_800.jpg)|
|:--:| 
| *Image by [PublicDomainPictures](https://pixabay.com/users/publicdomainpictures-14/) from [Pixabay](https://pixabay.com/)*|

#### UST

Yaşanan sarsıntının temelinde Terra sisteminin stabil parası olan UST'nin bir ABD dolarına sabitlenmiş çıpasını kaybetmesi var. 

Daha önceki iki yazıda ayrıntılarını incelediğimiz gibi, dolara sabit olmakla birlikte Anchor Protokol tarafından yıllık %20 gibi ağız sulandırıcı bir faiz oranı ile yatırımcılara sunulan UST, bir yıldan kısa bir zaman içinde yaklaşık 18 milyar ABD Doları gibi bir büyüklüğe ulaştı. (Yazıların [ilkini](https://medium.com/turansert/ba%C5%9F%C4%B1ma-gelenler-ustnin-hikayesi-21324bb4969f) ve [ikincisini](https://medium.com/turansert/ust-olay%C4%B1nda-son-perde-cd48c9c6e15b) bağlantılardan okuyabilirsiniz)

| ![domino_falls](/assets/ust_piyasa_değeri_800.jpg)|
|:--:| 
| *UST Piyasa Değeri. Kaynak: [CoinGecko](https://www.coingecko.com/en/coins/terraclassicusd)*|

Büyük ölçüde hormonlu olarak gerçekleşen bu büyümenin sürdürülebilir olmadığı aslında apaçık ortaydı ancak müzik çalarken bütün oyuncular dans etmeye devam ettiler. 

Sonrasında müzik susunca, dans pistinde en hareketli oyuncu olan Three Arrows Capital (3AC)'nin oturacak sandalye bulamadığını gördük. Önce bu arkadaşları bir tanıyalım: 

#### Three Arrows Capital - 3AC

2012 yılında [Zhu Su](https://twitter.com/zhusu) ve [Kyle Davies](https://twitter.com/kyleldavies) adında iki trader [tarafından Singapur'da](https://en.wikipedia.org/wiki/Three_Arrows_Capital)  kurulan [Three Arrows Capita](https://www.threearrowscap.com/about-us/) (kısa adıyla 3AC) esas olarak bir arbitraj fonu. Ne demek arbitraj fonu? Benzer ürünlerin farklı piyasalar arasındaki fiyat farklılıklarından doğan fırsatları değerlendiren bir fon. İşlem yaptıkları  benzer karaktere sahip enstrümanları bir piyasada alıp (ya da borç alıp) diğer tarafta satan (ya da borç veren) böylece riski minimuma indirerek kazanç sağlayan yapılar. 

3AC'nin bu tip piyasa farklılıklarından yararlanarak işlem yaptığı üç temel ürün var (başka pek çok yatırımı dışında). Bunlar BTC/GBTC, ETH/stETH ve USD/UST idi.  (En sondaki dipnot'ta bu üç ürünün neler olduğu konusunda detaylı bilgiyi bulabilirsiniz). 

İşte 3AC piyasadan olabildiğince borçlanıp yukarıdaki üç 'arbitraj' fırsatını kullanarak ciddi bir şekilde büyüdü. Hesaba katmadıkları ne oldu? Yukarıdaki sistemlerin piyasalar yükselişte iken yani müzik devam ederken kazanç sağladığı, piyasaların düşüşe geçtiği noktada ise göz ardı edilen bütün risklerinin bir anda başa geldiği. Neydi bu riskler? 

Birincisi USDT(C) gibi paraları borç alıp UST'ye yatırma stratejisinin, her iki paranın da ABD dolarına çıpalanması nedeniyle 'sıfır risk' gibi görülürken, aslında UST'nin gerçek risklerini gizlemesi. Nedir bunlar? UST'nin aslında temel fonksiyonu olan geniş kitlelerce kullanılma yerine, büyümek için sürdürülemez bir şekilde faiz vermesinin yarattığı ince buzda yürümesi. Bu buz kırıldığında en çabuk batan en çok yük taşıyanlar oldu ki bunların başında 3AC geliyordu. 

İkincisi ise likidite sıkıntısı. 3AC, USD/UST stratejisini olabildiğince sömürmek adına fazla fazla USDC (ve USDT) borçlanabilmek için teminatlar verdi. Nedir verilen bu teminatlar? Yukarıda bahsettiğimiz arbitrajlar sırasında aldığı GBTC ve stETH'ler ya da başta BTC ve ETH olmak üzere likit kriptoparalar. UST'nin çıpasını kaybettiği noktada 3AC'ye borç verenler kredileri geri çağırmaya, kredi geri ödenmediği  nokta da ellerinde tuttukları bu teminatları bozdurmaya başladılar. İşte bu bozdumalar sonrası GBTC'nin piyasa değeri BTC'ye göre %34'e yakın [geriliyor](https://ycharts.com/companies/GBTC/discount_or_premium_to_nav), aynı şekilde stETH'nin değeri .93 ETH'ye [düşüyor](https://coinmarketcap.com/currencies/steth/steth/eth/). BTC, Haziran ayında şimdiye kadar en kötü performans gösterdiği ayı yaşayıp %39.7 oranında değer kaybediyor. 

Yukarıda yaşananların dışında 3AC'nin elindeki GBTC'leri farklı kurumlara teminat göstererek kredi aldığı şeklinde iddialar var ki, doğru ise dolandırıcılık olarak adlandırılabilecek bu durumu 3AC'nin kurulu olduğu Singapur otoritelerinin incelemeye aldığını da belirtelim. 

Gelinen son noktada, 3AC, British Virgin Islands'da mahkemelere başvurup [iflasını isteyerek](https://www.coindeskturkiye.com/sirketler/three-arrows-capital-new-yorkta-iflas-basvurusunda-bulundu-939) beyaz bayrağı çekmiş durumda. İflas sürecinde ortaya dökülecek yeni olayları hep birlikte izleyeceğiz. 


### Arkası yarın 
Domino taşları UST ile başlayıp 3AC ile devam ediyor ancak orada bitmiyor. Diğer taşlara ise önümüzdeki yazımızda bakmaya devam edeceğiz. 

Not: 

**1. BTC/GBTC:** Piyasadan BTC borçlanıp, bu BTC ile GBTC almak. GBTC, elinde BTC tutan özel bir fon (İngilizcede trust fund). ETF dediğimiz sahip olduğu ürünlerin fiyatın takip eden fonlar ABD'de çok yaygın ancak ABD'nin SPK'sı olan SEC  kripto için bu fonlara izin vermiyor. Kriptoparalara yatırım yapmak isteyen büyük emeklilik fonları, ETF'lere izin verilmediği için başlangıçta gidip GBTC alıyorlar idi. Bu aşırı talep nedeniyle GBTC, elinde tuttuğu BTC'den daha yüksek bir değere sahip idi. GBTC'nin birkaç özelliği var; herkes alamıyor (sadece belirli bir nitelikli grup), aldıktan sonra altı ay boyunca satamıyorsunuz, ayrıca öyle geri verip karşılığında BTC almak da yok, satışı sadece piyasaya yapabiliyorsunuz. GBTC primli olduğunda aslında bu bir sorun değil. Eğer %10 primli ise, BTC'ni yatır, altı ay bekle altı ay sonunda %10 primli olarak piyasada sat. İşte 3AC'nin yaptığı işlemlerden biri bu idi. Teorik olarak yok diyenler çıkabilir, zira en kötü GBTC'nin içinde o kadar BTC var, ama pratikte? Ya GBTC'ye olan talep azalır ve GBTC iskontoya düşerse? O zaman zarar etmemek için GBTC'yi satmaz elinizde tutmaya devam edersiniz? Ne zamana kadar? GBTC'ye talebin ve buna bağlı fiyatın artmasını bekleyeceksiniz. Bu nasıl olur? Kolay değil ancak bir çıkış yolu olarak GBTC'yi çıkaran Grayscale bu fonu ETF'e çevirmek için SEC'ye başvurdu. GBTC ETF'e çevrilirse o zaman, tipik bir ETF gibi piyasa yapıcılar girip fiyatı BTC ile denk hale getirebilirler, siz de elinizdeki GBTC'leri elden çıkabilirsiniz. Peki ya SEC izin vermezse (ki vermedi) o zaman? Ya beklemeye devam ya da beklemeye tahammülünüz kalmazsa (ya da zorunlu kalırsanız) piyasada zararına satacaksınız. (Grayscale fonları ile ilgili geçtiğimiz yıl yayınlanan detaylı yazıya [şuradan](https://medium.com/turansert/grayscale-fonlar%C4%B1-6e3de0040881) ulaşabilirsiniz)

**2. ETH/stETH:** Ethereum yeni versiyonunda PoW denen iş kanıtı yönteminden, daha az enerji harcayan PoS sahiplik kanıtı yöntemine geçecek. Sistemin güvenliğini ve işleyişini artık madenciler değil sisteme ETH rehin etmiş onaylayıcılar sağlayacaklar. Bu nedenle onaylayıcı olmak isteyenler 2020 yılının Aralık ayından bu yana ellerindeki ETH'yi (en az 32 ETH olacak şekilde) sisteme kilitliyorlar ve bunun karşılığı bir faiz alıyorlar. Sisteme kilitlenen bu ETH'leri geri çekmek şu an için mümkün değil. Bunun için önce PoS sistemine geçilmesi sonra da yaklaşık altı ay kadar  beklenmesi gerekiyor (kesin süre belli değil). İşte kilitlenen bu ETH'leri likit hale getirmek için çeşitli tokenler türetilmiş durumda. Bunlardan en büyüğü ise [Lido Finance](https://lido.fi/) tarafından çıkarılan staked ETH tokenler ([stETH](https://www.coingecko.com/en/coins/lido-staked-ether)). ETH'nizi Lido Finance'e kilitlediğinizde karşılığında stETH alıyorsunuz. stETH ile hem varlığınızı PoS sistemine kilitlemiş gibi faiz alıyor hem de bu tokeni DeFi sisteminde kullanarak (örneğin varlığınızı başka sistemlere likidite sağlayarak) ekstra gelir elde ediyorsunuz.  Eğer günün birinde ETH ihtiyacınız olursa stETH'yi satabiliyorsunuz ama bunu piyasada yapmak zorundasınız. (Lido Finance ETH'nizi stake ettiği için size geri vermiyor. Siz gidip piyasada satıyorsunuz, dolayısıyla stETH'nin değerini piyasa belirliyor.)  Teorik olarak stETH ile ETH'nin değerinin eşit olması gerek. Zira konan her bir ETH için bir stETH yaratılıyor. Zaten bir gün ETH'ler PoS sisteminden çekilebilir olduğunda stETH'ler de benzer şekilde ETH'ye çevrilebilir. O güne kadar ya bekleyeceksiniz ya da piyasa size ne dikte ediyorsa (ki bu genelde iskontolu bir fiyat oluyor) oradan satacaksınız. 

**3. USD/UST:** UST'nin büyümesinin temel nedenlerinden biri yatırımcıların (ya da al-sat yapan piyasa oyuncularının), bulabildikleri her yerden USD'ye çıpalı paraları (USDT, USDC) borçlanıp bu paraları UST'ye yatırmaları oldu. Öyle ya, bankaların USD mevduata %1'in altında bir faiz verdiği ortamda, USDC için %4 vaat etmek yatırımcılar için müthiş cazip. USDC'yi bu orandan borç alıp %20 ile UST'ye yatırdığınızda da bu da sizin için müthiş. Alan memnun satan memnun. Nereye kadar? Müzik sona erinceye. 


# Finansın Domino Taşları - Son krizde neler yaşandı? 2
Bu yazımızda kripto dünyasında yaşanan son krizin, devam eden halkalarına bakıyoruz. 

Geçtiğimiz yazımızda, kriptopara alanında yaşanan son krizin çıkış noktası olan UST'nin ABD Dolarına çıpasını kaybetmesi sonrasında ise  UST'ye en büyük para yatırmış kurumlardan biri olan 3AC fonununun zora girmesine değinmiştik. Bu yazımızda UST ve 3AC'den etkilenen diğer aktörlere değineceğiz. 

| ![halkalar](/assets/wellness-4225867_800.jpg)|
|:--:| 
| *Image by [Gerd Altmann](https://pixabay.com/users/geralt-9301/) from [Pixabay](https://pixabay.com/)*|

### Kimler 3AC'ye kredi verdi ya da UST'ye mevduat yatırdı?
Önceki yazımızı hatırlatırsak; 3AC farklı piyasalar arasında kendince 'risksiz' olarak adlandırdığı 'arbitraj' fırsatlarını olabildiğince değerlendirebilmek için yüksek miktarda borç almıştı. Nasıl borç alıyordu? Zamanında kazandığı kriptoparaları teminat göstererek. Kimden borç alıyordu? İşte burayı biraz daha açalım. 

3AC temel finansman kaynağı olarak piyasada bulunan merkezi kuruluşları kullanıyordu. Bunlardan en bilinen ikisi BlockFi ve Voyager idi. 

[BlockFi](https://blockfi.com), kullanıcılarının kriptoparalarına yüksek getiri vaad eden bir kredi/mevduat kurumu -  bir nevi bir banka. Kullanıcılar dilerlerse paralarını yüksek faiz ile BlockFi'ya yatırabiliyor ya da bu paraları teminat göstererek stabil para borçlanabiliyorlar. Websitesinde 10 milyar ABD Doları'ndan fazla aktifi olduğunu iddia iddia eden şirket Forbes dergisinin 2021 yılı en iyi 50 Fintech şirketi arasına seçilmiş.

BlockFi, 3AC'ye verdiği kredilere karşılık aldığı teminatların değerlerinin düşmesinden dolayı yaklaşık 80 milyon ABD Doları zarar ettiğini [açıkladı](https://blockfi.com/a-message-from-our-founders-july-2022). Bunun yanına kriptopara piyasalarındaki iniş-çıkış nedeniyle ettiği başka zararları da ekleyen BlockFi, FTX'in kendisine uzattığı yardım eline sarılmak durumunda kaldı. Sonuç 2021 yılı Mar ayında 3 milyar dolar değerleme ile 350 milyon ABD doları [yatırım alan](https://blockfi.com/blockfi-completes-usd350-million-series-d), üç ay sonra  Haziran ayında  5 milyar ABD Doları'ndan yeni [yatırım turuna çıkan](https://www.theinformation.com/articles/crypto-lender-blockfi-in-talks-to-raise-funding-at-5-billion-valuation) şirket, şu an için aldığı 400 milyon ABD Doları borcu ödemediğinde 240 milyon ABD Doları'na FTX'e [satılacak](https://twitter.com/BlockFiZac/status/1542934048296914944?s=20&t=Oy4yBMVoNtKjKUSKdV_CkA). 

Voyager ise Kanada'da halka açılmış bir kriptopara borsası. 27 Haziran'da 3AC'ye kendisine olan 637 milyon ABD Doları borcu ödemesi için [ihtar çektikten](https://decrypt.co/103892/voyager-digital-issues-three-arrows-capital-default-notice) bir kaç gün sonra kriptopara çekimlerini askıya aldığını [duyurdu](https://decrypt.co/104294/voyager-digital-halts-withdrawals-three-arrows-capital-default), sonrasında ise 6 Temmuz'da [iflasını istedi](https://www.reuters.com/technology/crypto-lender-voyager-files-bankruptcy-2022-07-06/). 

Bir başka kripto borç verme kurumu olan Celsius ise 3AC gibi stETH/ETH yatırımlarından dolayı sıkıntıya girerek 13 Haziran'da para çekimlerini durdurduğunu [ilan etti](https://blog.celsius.network/a-memo-to-the-celsius-community-59532a06ecc6). Şu an harıl harıl finansman arayan şirketin satın almak için FTX'in ilgilendiği ancak sonrasında bilançoda 2 milyar ABD Doları açık olduğunu görünce vazgeçtiği söylentileri ortalıkta dolaşıyor. 130 çalışanının işine son veren şirketin, ayakta kalmak için çaba gösterdiği görülüyor. Kendisine iflas etmesini öneren danışmanlarını kovup [yenileri ile anlaşan](https://www.theblock.co/post/156805/celsius-hires-new-restructuring-lawyers-to-help-navigate-its-options-wsj) şirketin, ilginç bir şekilde Aave ve MakerDAO gibi DeFİ platformlarından aldığı borçların tamamını geri ödeyerek teminatlarını kurtaran şirket daha sonra geçtiğimiz hafta içinde iflasını istedi (Beyaz bayrak çeken 3AC'den farklı olarak Celsius borçlarını yeniden yapılandırma arzusunda).

Bunlar dışında ortaya çıkan diğer olayların satır başları ise şöyle: 

- Hong Kong bazlı kripto kredi verme şirketi [Babel Finance](https://babel.finance/), Mayıs ayında 2 milyar ABD Doları değerleme üzerinden 80 milyon ABD Doları yatırım aldıktan sonra, 17 Haziran tarihinde para çekimlerini [durdurdu](https://www.coindesk.com/business/2022/06/17/babel-finance-suspends-withdrawals-citing-unusual-liquidity-pressures/). Şu an borçlarını yeniden yapılandırmak için danışmanlar ile çalışan şirketin sonraki adımları merak konusu. 

- Singapur'da faaliyet gösteren kriptopara borsası CoinFLEX ise muhtemelen Bitcoin Cash'i kuran Roger Ver'e verdiği kredilerin teminatlarını bozdururken 84 milyon ABD Doları [zarar ettiğini](https://www.theblock.co/post/156759/coinflex-outlines-plan-to-recover-84-million-raise-capital-from-new-investors) ve zararı tazmin etmek için Hong Kong'da mahkemeye başvuracağını açıkladı. 

- Yine Singapur'da kurulu bir başka kriptopara borsası Vauld, ise piyasa hareketliliği nedeniyle müşterilerin yoğun para çekişini karşılayamadığını iddia ederek çekimleri [durdurdu](https://decrypt.co/104380/crypto-lending-platform-vauld-halts-operations-citing-financial-difficulties). Şirket bunun yanında iş gücünü %30 oranında azalttığını [açıkladı](https://www.vauld.com/blog/a-message-from-darshan-bathija/). Bir başka büyük kredi verme kuruluşu olan Nexo'nun Vauld'u almak için görüşmelere başladığı [belirtiliyor](https://www.theblock.co/post/155790/nexo-vauld-offer-potential-acquisition).

- Bir başka kripto devi olan Genesis Trading ise 3AC ve Babel Finance'e verdiği kredilerden dolayı yüzmilyonlarca dolar zarar etmiş [durumda](https://www.coindesk.com/business/2022/06/29/genesis-faces-hundreds-of-millions-in-losses-as-3ac-exposure-swamps-crypto-lenders-sources/). Digital Currency Group'un sahibi olduğu şirket oldukça büyük olduğu için bu zararları sineye çekebilecek durumda.  

İrli ufaklı etkilenen şirketlerin hangileri olduğunu merak edenler var ise, [şu resmi olmayan listeye](https://twitter.com/0x_illuminati/status/1544070879709081600?s=20&t=Ymaaobtrc2h5nt12umOqRw) göz atabilirler. 


### Sorun temel olarak nerede? 

Burada bir ayrımı net olarak yapmak gerekiyor. Yaşanan tüm bu olaylar sırasında merkeziyetsiz finans dünyasının oyuncularında ya da verdiği hizmetlerin herhangi birinde sıkıntı yaşanmadı. Bu sistemler şeffaf bir şekilde, kuruldukları gibi çalışmaya devam ettiler. 

Krizin temel nedeni, müşteri parası emanet alan ve sonrasında bu parayı riskli yerlerde değerlendiren merkezi kurumlar oldu.  Örnekler ile anlatalım: 

3AC'nin kimden ne kadar borç aldığı ve bu paraları nereye yatırarak nasıl bir risk altına girdiği bilinmiyor. Aynı şekilde  ellerindeki bir teminatı farklı yerlere vererek fazla fazla kredi kullandıkları şeklinde söylentiler ortaya atıldı. Hâlâ yaptığı işlemlerden ne kadar zarar ettiklerini bilemiyoruz. Her şey bir söylenti. Neden? Hepsi kapalı yapılar çünkü. 

BlockFi, Celsius ya da Voyager gibi kurumların ise, kurumsal görüntüleri ve göz alıcı websiteleri ile müşterilerine sundukları 'güvenilir' imajın aksine aslında en temel riskleri bile göz ardı ettikleri görüldü. Kimilerinin aldıkları teminatın yeterli olmadığı kimilerinin ise teminatsız borç verdikleri anlaşıldı. 

Üstelik bu tip yapıların şeffaf olmamaları nedeniyle yaptıkları hareketleri izlemek ve krizin boyutunu tam olarak kestirebilmek bile maalesef mümkün değil. Ama bildiğimiz bir gerçek var, o da UST'nin 8 Mayıs 2022 tarihinde 18.8 milyar ABD Doları olan piyasa değerinin şu an için buharlaştığı ve birilerinin ciddi para kaybettiği. 

Dolayısıyla, kodların hakim olduğu merkeziyetsiz finans dünyası takır takır işlerken, insanın yürüttüğü merkezi dünyanın kendi kendine işleyemeyeceği bir kez daha görüldü. 

### Sorunları regülasyonlarla çözebilir miyiz? Evet ise nereye kadar?

İşte burada regülasyonun nerede nasıl kullanılması gerektiği de net bir şekilde ortaya çıkıyor aslında. İnsanın işin içinde olduğu, başkasının parasını emanet alan (çoğu merkezi) yapılar, mutlaka bir regülasyona tabi olmalı. Kodun hakim olduğu, yapılan işlemlerin anlık olarak takip edilebildiği DeFi dünyasının ise, doğası gereği toplum tarafından anlık olarak denetlenebildiği, dolayısıyla daha fazla denetimin gereksiz bürokrasi getirmesi dışında, uygulanabilir de olmadığının kabul edilmesi gerekli. 

### Sonuç 

2020 yılının ortasında bir milyar ABD Doları bir kilitli paraya sahip DeFi platformlarının 2022 yılı başlarında 185 milyar ABD Dolarına ulaşan baş döndürücü hızının arkasında yatan temel sebebin kurumsal yatırımcılar olduğu bilinen bir gerçek.  

2022 yılının Mayıs-Haziran aylarında yaşanan kriz ise bu yükselişin ardındaki yüksek kaldıraçlı spekülatif işlem yapan oyuncuların elenmesine yol açtı. Kriz bitti mi? Bu yatırımcıların her biri birer kapalı kutu olduğu için bunu söylemek şu an için zor. Bir daha tekrar eder mi? Bireysel yatırımcıların hafızası kısa ömürlüdür, unuturlar. Kurumsal yatırımcılar ise biraz daha uzun vadeli bakar ve talepkar olurlar. Bu nedenle, bundan sonra bu alanda sektörün kendi regülasyonlarını ortaya çıkarması muhtemel. Zaten bunun olmadığı noktada kanun koyucular kendi kurallarını getirecekler ve bu kuralların nerede başlayıp nerede biteceğini şu anda kestirmek çok zor. 

Gelecek heyecanlı olduğu kadar, bilinmezliklerle de dolu. Birlikte yaşayıp göreceğiz.  
