Geçtiğimiz yazıda Bitcoin'in geniş kitlelere yayılması için üzerinde çalışılan yeniliklerden Lightning Network'den bahsetmiştik. Bu hafta ise bir başka potansiyel yenilik olan Liquid Network'e bakalım birlikte.. 

### Liquid Network? Nedir o?

Liquid Network aynı Lightning Network gibi Bitcoin'i üzerine inşa edilmiş bir yenilik. Ama benzerlikleri orada bitiyor.  

Kısaca hatırlayacak olursak, Lightning Network Bitcoin üzerine kurulmuş ikinci bir tabaka idi. Bitcoin üzerinde depozito koyup kanal açan aracılar, bu depozitoyu kullanarak birbirileri üzerinden işlem yapabiliyorlar idi. Böylece hem Bitcoin'in sağladığı güvenlik, gizlilik gibi özellikleri kullanabiliyor hem de Bitcoin ağı üzerinde yük yaratmadan binlerce işlem yapabiliyorlar idi. 

Liquid hisse alım-satımı yapan kurumlar ve borsalar arasında hızlı işlem yapmaya yarayan bir özel bir Blockchain. Lightning Network gibi Bitcoin üzerine kurulmuş bir tabaka değil de, Bitcoin'e bağlı bir yan-zincir (side-chain). Ne demek yan zincir? Açıklayalım:

Liquid'in yaratmış olduğu özel bir Blockchain ve buna bağlı olan bir para var L-BTC adında. Hatırlarsanız daha önce Sabitparalar'dan bahsetmiştik. Kendilerini ABD Doları gibi Fiat paraya bağlayan sanal paralardan. L-BTC de kendini Bitcoin'e bağlamış. Yani hem BTC ile aynı değerde hem de bir L-BTC yaratılması için aynı oranda  bir BTC karşılığının olması gerekiyor. Kullanıcılar BTC (Bitcoin'in parası) sahibi olmaya devam ederken L-BTC'nin sağladığı ek avantajlardan yararlanabiliyorlar.  


![liquid_header-min.png](/assets/liquid_header-min.png)

Liquid Network, Bitcoin'den farklı olarak özel bir Blockhain (permissionless). Ne farkı var yani Bitcoin'den? Şöyle: Bitcoin açık bir network olduğu için hem kullanıcılar hem madenciler istedikleri gibi girip çıkabiliyorlar. Liquid Network'de ise Bitcoin'deki gibi madenciler yok. Sadece şu an sayısı 15 olan borsalar ve kurumsal aracılar var. Yapılan işlemleri madenciler onaylamıyor, o işi bu borsa ve kurumsal aracılar yapıyor. Bitcoin'de madencilerin çoğunluğunun işlemi onaylaması gerekirken burada üçte iki çoğunluk gerekiyor, yani 11 borsanın işlemi onaylaması gerekli. 

Kullanıcılar ise L-BTC ile istedikleri gibi işlem yapabiliyor ama L-BTC'lerini satmak için yine bu borsaları kullanmak zorundalar. Kullanıcı olarak bir borsaya girip L-BTC aldığınızda, bu spesifik bir BTC'ye bağlanıyor ve satmaya kalktığınızda o spesifik BTC üzerinden işlem yapılıyor. Böylece olası sahtekarlıklar önlenmiş oluyor. 

#### Nedir sağladığı avantajlar Liquid'in?
Kullanıcılar için Liquid'in sağladığı en büyük avantaj SabitParalar ile benzer aslında. 

Kriptoparanızı (buradaki örnekte BTC'nizi) bir borsada tutmak riskli. Neden? Her ne kadar KriptoBorsa'lar her tür güvenlik önlemini alsalar da merkezi yapılar - dış tehdit ve saldırılara açıklar*. O nedenle özellikle büyük miktarda parayı kurumsal yatırımcılar borsalarda tutmak istemiyorlar.  

Paranızı borsada tutmadığınız durumda ise işlem yapmak istediğinizde çok vaktinizi alıyor. Cüzdanınızdan parayı borsaya göndermek Bitcoin üzerinde en kısasından 10 dakika ama borsanın bunu tam olarak alıp (teyid edip) size işlem yaptırmasına baktığınızda çok daha uzun zaman alıyor. Özellikle çok işlem yapan biri iseniz bu kimi fırsatları kaçırmanıza yol açabilir. 

İşte Liquid bu iki soruna çözüm getiriyor. Paranızı L-BTC'de tuttuğunuzda, borsaya 1 dakika içinde gönderebilir ve hemen alım satım yapabilirsiniz. Daha sonrasında L-BTC'inizi isterseniz kendi cüzdanınıza çekersiniz, ya da BTC'ye çevirirsiniz (1'e 1 aynı oranda). 

### Var mı sakıncaları?

Teoride yukarıda yazılanlar çok güzel görünse de kuşku ile bakanlar da yok değil. Bu kuşkuların ciddi bir kısmı felsefi aslında. 

Bitcoin'in bağımsız yapısını ön plana çıkaranlar Liquid Network gibi yapıların özel network olmasına takılıyorlar. Dediğimiz gibi işlemleri onaylayanlar madenci değil özel olarak seçilmiş 15 kurum. Kaldı ki bu seçilmiş kurumların hepsinin sicili de o kadar iyi sayılmaz[a(https://www.coindesk.com/crypto-exchange-zaif-hacked-in-60-million-6000-bitcoin-theft/)][b(https://medium.com/@bitfinexed/wash-trading-bitcoin-how-bitfinex-benefits-from-fraudulent-trading-8bd66be73215)][c(https://www.trustnodes.com/2018/09/14/bitmex-seemingly-trading-against-its-own-customers-price-manipulation-in-plain-sight)]. Ya bu 15 kurum içinde 11'i birlikte hareket ederse? Liquid yaratıcıları da böyle bir riski kabul ediyorlar ama karşılaştırmanız gerekenin paranızı (BTC'ninizi) bir borsada tutmanın riski ile 15 farklı borsada tutmanın riski olması gerektiğini söylüyorlar. Tek bir borsanın risklerini almaktansa, riski 15 ayrı borsaya dağıttınızı belirtiyorlar. Ama nereden bakarsanız bakın, BTC'nin orjinal yaratıcılarının düşlediği özgür dünyadan sapma bu yapı sonuç olarak . 

İkinci bir eleştiri ise, Blockstream'e yapılıyor. Kar güden bir kurum olan Blockstream, kendi kaynaklarını kullanarak bugün için Bitcoin'in geliştiren hatırı sayılır sayıda yazılımcıya iş olanağı sağlıyor. Eleştirenler, bu kişilerin ileride Bitcoin'i geliştirirken de Blockstream'ın istediği alanlara yönelecekleri ve tarafsızlıklarını kaybedebileceklerinden endişe duyuyorlar. Şahsen çok katılmadığım bir kaygı. Zira Bitcoin geliştiricisi olmak için herhangi bir sertifika ya da izin gerekmiyor. İsteyen yazılımcı Bitcoin'i geliştirmek için katkıda bulunabilir. Blockstream'in bu yazılımcılara iş veriyor olması, başka yazılımcıları da Bitcoin üzerinde çalıştırmaya sevk edebilir, ki bu gayet Bitcoin'in yararına bir durum. 

### Sonuç

Her ne kadar yukarıdaki eleştirileri yazsak da, özünde Liquid kullanıcılara fayda sağlayan bir yapı. Riskler de katlanılabilir görünüyor. Bitcoin'in kullanan kişilerinin her birinin ondan beklentisi farklı. Kimi hızlı işlem yapmak isterken, kimi gizlilik kimi de baskılara karşı koyabilme özelliğini nedeniyle Bitcoin kullanıyor. Liquid hızlı işlem yapmak ve bu işlemler için yüksek komisyon vermek istemeyenlere uygun bir yapı. Bitcoin'in kurumsal yatırımcılar tarafından daha sık kullanılmasını sağlayacağı bunun sonucu da piyasadaki likiditeyi artırıcı bir faydası olacağı düşünülüyor. Yani özünde aynı Lightning Network gibi Bitcoin'in gelecekte geniş kitlelerce adaptasyonuna yardımcı olmaya çalışan bir araç. Başarılı olacaklar mı yakından takip edeceğiz... 


---

* Hep dediğimiz gibi Fiat paranızı bankada tuttuğunuzda banka riski alıyorsunuz. Kimseye güvenmeyecek kadar paranoyak iseniz alıp yastığınızın altına koyabilirsiniz ama orada da evinize hırsız girebilir. Bitcoin Kriptocüzdanlar sayesinde kendinizde tutabileceğiniz ve gerçekten sahip olduğunuzu kanıtlayabileceğiniz tek sanal para belki de. Kendi özel anahtarınızı bir kağıda yazdıktan sonra (kağıdı kaybetmemek şartıyla) sizden kimse alamaz ve bu kağıt ile birlikte parayı istediğiniz her yere götürebilirsiniz (isterseniz kağıda bile yazmayın ve hafınıza güveniyorsanız bu karmaşık şifreyi ezberleyin, size kalmış).



- Sidechain to Bitcoin
- Works in-and-out to Bitcoin
- Good thing is if anything happens to L-BTC that does not affect Bitcoin
- Not mined by Bitcoin but rather federated
- 2 out of 3 members should approve transactions
- Members are exchanges and institutions
- Permissioned network - kim oldukları belli
- Yeni girenlere de içindeki üyeler karar veriyorlar
- Sidechain olarak ne işe yarıyor?
- Peg edilmiş - yani sen Liquid BTC aldığında onun karşılığı BTC olarak duruyor ve kullanılamıyor
- Kullanıcıları büyük fonlar ama normal bireyler de kullanabilir (hızlı işlem yapmak isteyenler)
- L-BTC aldığında aynı miktarda paranın BTC'ye bağlı olduğunu görmesi lazım sistemin (keza gönderdiğinde de), orada BTC network'unde olduğunu test etmeli
- Ayrıca bütün işlemlerini BTC gibi listelemiş (aynı Blockchain explorer gibi girip görebiliyorsunuz)
- 


Yararı ne?
- Normalde işlem yaptığınızda paranızı bir exchange'de bırakmak sakıncalı (exchange batabilir)
- Sürekli olarak kendi özel cüzdanınıza çekmelisiniz
- Ama institution olarak bunu yaptığınızda al, geri götür zaman alıcı ve fırsat kaçırabilirsin
- Bir nevi daha önce bahsedilen stablecoin gibi bir para çıkarılmış L-BTC
- Bunu aldığında paranı burada tutabiliyorsun ve BTC'ye anlık olarak geçirebiliyorsun
- Paranı exchange'de tutmayıp L-BTC olarak kendine çekiyorsun ve 1 dakika içinde ona geçiriyorsun
- Bir exchange riski almak yerine riski dağıtıyorsun (onlarca exchange'e) - 11 out of 15 institutions
- Likiditeden dolayı piyasaya girmeyenlere alternatif bir yol sunuyor
- Aynı zamanda kimi denetleyiciler piyasanın likit olmadığını söylüyor ve ETF kurulmasına izin vermiyor, bu o işe yarıyo

- Bir özelliği de Private Network'ler genelde işlemleri gizli tutarken, Liquid üzerindeki işlemler takip edilebiliyor Bitcoin gibi, o şekilde bir şeffaflık var


Not 10 minutes but 1 minute


- So it is not decentralized as Bitcoin
- But it has a purpose - functionality
- Yet you own the asset as in Bitcoin
- You have the risk when you are on the sidechain 

- Differences with Lightning Network
- Lightning 
- is a not-for-profit organization
- is a second layer on top of Bitcoin,
- useful for payments and small transactions (more P2P transactions)
- brings scalability to Bitcoin

- Liquid
- For profit organization
- is another blockchain (side-chain) tied to Blockchain
- Relies on Bitcoin anonymity and censorship resistance
- However fees are going to developers rather than miners (just like Lightning Network)
- Useful for large transactions which require fast execution
- Brings liquidity (really?)

- Peki USDT Tether'e göre farkı ne?
- BTC'ye pegged - çok daha şeffaf (para gerçekten var mı sorusunu çözüyor), daha hızlı
- 


Gelecekte neler olabilir?
- Liquid BTC ile sadece BTC değil başka assetleri de peg edebilirsin - security çıkarabilirsin, onları trade edebilirsin


Çekinceler 
- Profit bir organizasyon bunun arkasında (Bitcoin'in bağımsız yapısına aykırı)
- Çok fazla Bitcoin developer kullanıyor (dolayısı ile Bitcoin'in gelişimine de nüfuz edebilir) - gerçi bu developera iş vermesi Bitcoin için iyi bir şey, sonuçta Bitcoin bir şirket değil, isteyen katılıp gelişimine katkıda bulunabilir

