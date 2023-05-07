Bu yazımızda Ethereum ekosisteminde gittikçe önem kazanan Liquid Staking Derivatives alanının oyuncularına göz atacağız. 

Geçtiğimiz yazımızda Ethereum'un Shapella güncellemesi sonrası çekimlere izin vermesinin ekosisteme etkilerini incelerken, bu alanda en büyük değişimin kısaca LSD olarak adlandırılan Liquid Staking Derivatives cephesinden geleceğini belirtmiştik. 

#### Nedir bu LSD tokenler?
LSD (Liquid Staking Derivatives), sisteme kilitli ETH'leri likit hale getiren türev tokenlere verilen genel isim. Kısaca hatırlayacak olursak Ethereum Aralık 2020'de Ethereum'un yüksek enerji sarfeden hisse kanıtı (ingilizcesi Proof-of-Work kısaca PoW) sisteminden kapital yoğun hisse (rehin) kanıtı (ingilizcesi Proof-of-Stake kısaca PoS) sistemine geçmişti. Bu sistemin işlemesi için gerekli olan işleri ise onaylayıcı dediğimiz oyuncular yapıyor. Onaylayıcılar bu işi layıkıyla yaptıklarını kanıtlamak için sisteme en az 32 ETH kilitliyorlar (ya da rehin ediyorlar, ingilizcede 'Stake' olarak geçiyor) ve yaptıkları bu iş karşılığı ödül kazanıyorlar. 

İşte bu geçiş sorası ortaya çıkan LSD'ler sayesinde kullanıcılar, hem sisteme minimum 32 ETH yerine daha az miktarda kilitleme yaparak sistemin verdiği ödülden yararlanabiliyor hem de LSD tokenleri bir varlık olarak kullanarak DeFi'de ekstra gelir kazanma fırsatı elde ediyorlar. O günden bu yana çeşitli badireler atlatsalar da, hızlı bir şekilde büyüyen LSD'lerin, özellikle Nisan ayında gerçekleşen Shapella güncellemesi ile birlikte seviye atlamaları bekleniyor. Bunun en temel nedeni de artan likidite. 

Shapella güncellemesi öncesi Ethereum sistemine rehin edilen ETH'lerin çekimine izin verilmediği için LSD tokenleri sadece ikinci pazarda alınıp satılabiliyorlardı; bu da arz talebe göre tokenin ETH ile olan 1'e 1 dengesini bozabiliyordu. Artık bundan sonra LSD tokenler geri verilip yerine ETH alınabiliyor olacak. Bu da LSD tokenlerin üzerindeki en büyük belirsizliği ortadan kaldırıyor. Bunun yanında, LSD tokenlerin kullanımını artıracak yeni DeFi ürünleri sayesinde bu tokenlerin pazar payının artması neredeyse kesin gibi.

ETH staking pazarının yaklaşık %xxx elinde totan LSD tokenlerin birkaç büyük oyuncusu var. Bu oyuncular gerek felsefe gerekse işleyiş olarak birbirlerinden bir hayli ayrılıyorlar. Gelin şimdi de bu oyuncuları tek tek inceleyerek aralarındaki farklara değinelim. 

### Lido
LSD piyasasının açık ara en büyüğü Lido. Bir DAO olarak işleyen Lido, Aralık 2020'de daha piyasa yeni açıldığında aktif oldu. Bu da onlara ilk olma avantajı (ingilizcede 'first-mover-advantage') getirdi. O sırada aktif olan pek çok oyuncu arasından hızla sıyrıldı Lido. Bunun iki temel nedeni var.

#### Curve'de havuzlar
Birincisi, likidite. Bu geniş kitlerlerce benimsenmek için olmaz olmaz bir koşul. Lido bunun önemini erken anlamış durumda. DeFi üzerinde likidite sağlayan en önemli platformlardan olan Curve üzerinde açtıkları stETH/ETH havuzu sayesinde stETH son derece popüler oldu. Neden? Havuzu kullananlara verdikleri i LDO (kendi yönetim tokeni) teşvikleri sayesinde. 

#### Aave stETH mevduatları
İkinci neden ise, DeFi dünyasının en büyük kredi kurumlarından biri olan Aave ile yaptıkları anlaşma. Bu anlaşma ile Lido'nun LSD tokeni olan stETH Aave'de mevduat ve teminat olarak [kullanılmaya başlandı](https://dune.com/LidoAnalytical/Integration-Lido-Aave). Bu LSD tokenler arasında bir ilk olarak Lido'yu bir anda öne fırlattı.

Bundan sonrası bir sarmal gibi geldi. stETH'nin bir yandan Aave'de mevduat geliri sağlarken bir yanda da ETH staking geliri veriyor olması yatırımcıları buraya çekti. Yatırımcıların ETH'lerini Lido'ya yatırmaları Lido'yu en büyük ve aynı zamanda en likit LSD tokeni yaptı. Likiditenin olduğu yerde de, bu alana yatırım yapmak isteyen ama hacmin sığlığından dolayı çekinen daha büyük fonlar piyasaya girmeye başladı. Sonrası ise Lido'nun LSD pazarında %90'a yakın sahip olmasına kadar giden bir yol[^1]. 

Tabii Aave havuzlarını kullanmanın bir başka nedeni de yukarıda bahsettiğimiz işlemi kaldıraçlı bir şekilde yaparak geliri daha da artırabilme imkanı. Yatırımcılar ellerinde tuttukları stETH'yi getirip Aave'ye teminat olarak yatırıp ETH alıyorlar. Aldıkları bu ETH ile gidip daha fazla stETH satın alıp, yine protokole teminat olarak koyuyorlar. Sonra bir daha.. Bu borç/teminat sarmalı ile pozisyonlarını iyice büyütüyorlar. Böylece, kaldıraçlı ETH staking işlemi yaparak, riskli ama bir taşla birkaç kuş vurmayı sağlayan bir strateji ortaya çıkıyor. 

[Lido piyasa pazar payı]

#### 3AC'nin yol açtığı yol kazası
Tabii bu 'saadet zinciri' bir yere kadar gidebilir. Nereye kadar? Aslına bakarsanız, buradaki en büyük risk olan, stETH'nin ETH ile olan 1:1 denkliğini kaybetmesi durumuna kadar. Oldu mu? Evet. 

Temmuz 2022'de bu alandaki en büyük spekülatörlerden olan 3AC diğer stratejilerinden dolayı likidite sıkıntısına girince sahip olduğu tüm stETH'leri satmaya başladı. Piyasaya ani giren yüklü miktarda satış stETH'nin fiyatını düşürdü. stETH'nin fiyatı düşmesi Aave havuzundaki stETH teminatların değerini de düşürmeye başladı. Terste kalan spekülatörler, ya yeni stETH teminat eklemek ya da borçlandıkları ETH'leri geri getirmek zorunda kaldılar.

Aslına bakarsanız, 3AC krizinin Lido ile bir ilişkisi yok. O nedenle, bir süre sonra stETH/ETH oranı tekrar makul düzeylere (her ne kadar bir miktar düşük olsa da) geldi. Şu anda da rehin edilen tüm ETH'ler içinde [%32 pazar payı ile](https://dune.com/hildobby/eth2-staking) piyasanın lideri.

#### Nasıl çalışıyor Lido?
Lido'nun çalışma prensibi olarak bir 'aracı' olduğunu hemen belirtelim. Kullanıcılar, Lido'nun akıllı kontratları aracılığıyla ETH'lerini bu alanda hizmet veren 30 adet operatör üzerinden ETH sistemine yatırıyorlar. (Belirli kıstaslar uygulanarak Lido tarafından seçilen bu operatörlerin her birine stake etmeleri için verilen ETH miktarı [neredeyse eşit miktarda](https://www.rated.network/o/Lido?network=mainnet&timeWindow=1d&viewBy=operator&page=1)). 

Rehin ettikleri ETH, staking geliri kazandıkça kullanıcıların da ellerindeki stETH miktarı artıyor. Bu durum, yani elde tutulan stETH miktarının sürekli değişiyor olması (ingilizcede rebasing olarak geçiyor), kimi DeFi protokolleri için sorun teşkil etmezken (Curve, Yearn gibi) kimileri için (Uniswap, 1Inch gibi) problemli bir durum. Bu nedenle, wstETH denen, adedi sabit ama değeri kazandığı staking geliri ile birlikte artan 'dürüm' token da kullanıcıların hizmetine [sunulmuş durumda](https://help.lido.fi/en/articles/5231836-what-is-wrapped-steth-wsteth).  

Bundan sonrasında Mayıs ayı içinde Lido, kullanıcıların stETH'lerini direkt olarak ETH'ye çevirmelerine olanak sağlayacak mekanizmayı kullanıcılara sunacak. Bu durum ETH çekişlerini hızlandırır mı? Muhtemelen hayır. Zaten şu anda oran 1:1'e gelmiş durumda, yani isteyen serbest piyasada stETH'sini ETH'ye fazla bir kayıp yaşamadan çevirebiliyor.

Lido ile ilgili en büyük çekince pazarda çok büyük bir paya sahip olması. Ethereum sistemi bunu çok sevmiyor. Lido da kendini daha merkeziyetsiz yapmak için çabalıyor. Örneğin, Şubat ayında [açıkladıkları](https://blog.lido.fi/introducing-lido-v2/) Lido v2 ile birlikte, isteyen herkesin belli şartları karşılaması durumunda operatör olabileceği yeni versiyona geçeceğini belirtelim. Böylece 'neden sadece 30 operatör var?' sorusuna cevap verebilecekler. 

### Ve rakipler: CEX staking hizmetleri
Lido pazarın büyük hakimi olsa da, rakiplerin de eli armut toplamıyor. Her bir rakip kendini Lido'ya göre farklılaştırarak pazardan pay kapmaya çalışıyor. Yukarıda genel olarak Lido'nun nasıl çalıştığını anlattık. Rakiplerin de Lido'dan nasıl farklılaştıklarını kısa kısa özetlemeye çalışalım. 

Merkezi borsalar (ingilizcesi Centralized Exchange ya da kısaca 'CEX') biraz geç de olsa staking hizmetine girdiler ve hızla büyümeye çalışıyorlar. Bunlar içinde en büyüğü Coinbase ve tokeni cbETH. 

#### Coinbase ve cbETH
Coinbase staking hizmetini Haziran 2022'de sunmaya başladı. Oldukça geç. Üstelik verdiği staking hizmetinin karşılığı olarak aldıkları komisyon oranının yüksekliğine rağmen (%25) kısa zamanda %13 pazar payı ile piyasanın ikinci büyük oyuncusu haline geldi. Peki, niye yatırımcılar ETH'lerini rehin etmek için Coinbase'e getiriyorlar?

Temel nedeni, Coinbase'in hâlâ bir numaralı emanet tutan kurum olmasının getirdiği güven. Kişiler ya da kurumlar, teknik olarak hakim olmadıkları bir konuda, paralarını Lido ya da benzeri merkeziyetsiz platformalara yatırmaktan imtina ediyorlar. Sonuçta, staking hizmetinde bir sorun çıksa karşılarında Coinbase gibi muhatap görmek istiyorlar. Bu, aslına bakarsanız DeFi üzerinde merkeziyetsiz platformlar varken, merkezi alım-satım platformlarının hâlâ piyasada hakim olması ile benzer bir durum. Bir diğer neden ise, cbETH'nin aynı stETH'de olduğu gibi Curve, Aave, Compound gibi DeFi'nin ağır topları ile gerçekleştirdiği entegrasyon. 

Bu arada Coinbase'in verdiği staking hizmeti nedeniyle başının ABD'nin SPK'sı olan SEC ile dertte olduğunu da belirtelim. Daha önce, bu alanda hizmet veren Kraken'i ile uzlaşma yapan ve Kraken'in verdiği staking hizmetini zorla kapattıran SEC, benzer bir kapatma uyarısını Coinbase'e de yapmış durumda. Her ne kadar kaygı verici bir durum gibi görünse de Kraken ile Coinbase'in verdikleri hizmetin aynı olmadığını belirtelim. Kraken, çok daha muğlak ve müşterilere 'garantili getiri' vaad eden bir staking hizmeti sunuyordu. Üstelik Kraken'in bu hizmeti operasyonlarının ufak bir parçası olduğu için, başlarını daha fazla derde sokmadan, 30 milyon ABD Doları ödeyip hizmeti kapatma sözü verdiler[^2].

Coinbase için ise durum daha farklı. Birincisi, Coinbase burada tamamen teknoloji servis sağlayıcısı hizmeti verdiğini iddia ediyor. Yatırımcının parasını direkt olarak staking'e yatırdığını ve gelen geliri de komisyonlarını kestikten sonra kullanıcıya aktardıklarını belirtiyor. Kraken gibi herhangi bir gelir de vaad etmiyor. Üstelik staking gelirleri Kraken'in aksine Coinbase için oldukça önemli bir rakam. Bu nedenle, Coinbase bu konuda mahkeme dahil her tür savaşı vereceğini ifade etti. Hatta, SEC onlara dava açmadan önce, karşı bir dava açarak, SEC'i köşeye sıkıştırma yönünde bir strateji de gütmeye başladılar.

#### Binance ve WBETH
Merkezi borsaların en büyüğü olan Binance de staking çekimlerinin başlaması ile piyasaya yeni bir ürün sunarak pazar payını (şu an için %4.55 seviyesinde) artırma uğraşı içinde. Binance'in bundan önce Lido'nun stETH'si benzeri, BNB ağı üzerinde çıkardığı 1 ETH değerinde olan BETH tokeni vardı. Kullanıcılar staking geliri kazandıkça cüzdanlarına ekstra BETH geliyordu. Şimdi, çıkardığı yeni WBETH (Wrapped BETH) token ile, artık BETH tokenleri ile staking gelirleri aynı wstETH gibi otomatik olarak WBETH içinde toplanacak. Bu token hem BNB hem de Ethereum ağında DeFi protokollerinde kullanılabilecek.

### Diğer merkeziyetsiz protokoller
Lido benzeri pek çok farklı merkeziyetsiz protokol de var ve önümüzdeki dönemde hem sayı hem pazar payı olarak artış göstermeleri beklenebilir. Yerimiz dar olduğu için bu yazıda bunların en büyük ve en bilineni olan Rocketpool'a değineceğiz. 

#### Rocketpool
Rocketpool, Ethereum'un temel ilkelerinden merkeziyetsizlik konusunda bayrağı Lido'dan daha ileriye taşımaya çalışıyor. Nasıl? Lido, kullanıcıların parasını shake eden 30 operatörü kendi elleriyle seçerken, Rocketpool'da 16 ETH getiren herkes mini-havuzlar kurarak operatör olabiliyor. Kalan 16 ETH ise, kullanıcılardan geliyor. Kullanıcılar koydukları ETH karşılığı rETH alıyorlar. rETH, stETH gibi değeri ETH'ye bire-bir bağlı bir token değil, wstETH ya da cbETH gibi gelir kazandıkça değeri artan bir token. 

Tamamen merkeziyetsiz bir DAO tarafından yürütülen Rocketpool, belki de bu nedenle kuruluşu çok eskilere dayansa da, hizmet vermeye Lido'dan çok sonra Kasım 2021'de başladı ve gerek hizmet gerekse pazar payı olarak (%2.73) yavaş ilerliyor. Yine de, Ethereum dünyasının önde gelenleri, Lido'nun sistem üzerindeki dominansından duydukları endişe nedeniyle Rocketpool sistemine daha sıcak bakıyorlar.

### Ve mahallenin yeni çocukları: Eigenlayer ve DVT
Piyasaya doluşan LSD'ler yetmezmiş gibi, bir de şimdi geçtiğimiz ay içinde 50 milyon ABD Doları yatırım alan yeni bir girişim var: Eigenlayer. Yapmaya çalıştıkları oldukça ilginç. Kısaca değinelim:

Ethereum üzerinde stake edilen ETH'lerin temel işlevi Ethereum zincirinin güvenliğini sağlamak. Yukarıda stake edilmiş bu ETH'lerin bir değeri olduğundan bahsetmiştik. İşte Eigenlayer, aynı LSD'lerin DeFi'de değerlendirilmesinde olduğu gibi, bu rehin edilmiş ETH'lerin, Ethereum dışında başka zincirlerin (ya da uygulamaların) güvenliği için kullanılmasını sağlayacak. Bunu da kuracağı bir pazaryeri aracılığıyla yapacak. Restaking de denen bu sistem sayesinde, kullanıcı hem Ethereum'un hem de kendi seçtiği diğer zincirlerin staking gelirini kazanacak.

Burada unutulmaması gereken, ekstra gelir kazandırsa da, kullanıcının parasını farklı yerlerde kullandırmasının getireceği ekstra risklerin olabileceğinin unutulmaması. Eigenlayer henüz kurulma aşamasında (birinci seviye mainnet'i yakın zamanda açacaklar) ve muhtemelen 2023 yılının sonbaharı gibi kullanıma açılacak. 

Bu alandaki bir başka yenilik olan DVT sistemi (Distributed Validator Technology - Türkçesi dağıtık onaylayıcı teknolojisi) ise, birden fazla kullanıcının bir araya gelip onaylayıcıyı olabilmelerini sağlayan yeni bir teknoloji. Ethereum'un merkeziyetsizlik felsefesi ile uyumlu bu teknolojiden önümüzdeki dönemde sıkça söz edildiğini duyacağız gibi görünüyor. 

### Sonuç
LSD'ler staking geliri sağlamak amacıyla Ethereum üzerine rehin edilen kapitalin daha verimli kullanılması amacıyla geliştirilen, kendini geçtiğimiz iki yılda kanıtlamış, adını önümüzdeki dönemde daha da sık duymaya başlayacağımız bir türev token türü. LSD'leri kapital olarak kullanan yeni DeFi ürünleri ya da restaking benzeri yenilikler bu verimliliği daha da ileri götürüp ETH'den elde edilecek geliri daha da artırabilir. Yenilikleri hep birlikte izlemeye devam edeceğiz. 

[^1]: Staking pazarında LSD'ler dışında staking havuzları ve bireysel staking yapanlar da var. Burada verdiğimiz %90 rakamı sadece LSD tokenler için geçerli. 

[^2]: Nitekim, çekim işlemleri başladıktan sonra en fazla çekim yapan kurum Kraken oldu
