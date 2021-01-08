---
layout: post
title:  "DeFi'da opsiyon piyasaları"
date:   2021-01-05 16:47:56 +0300
categories: Genel
tags: Yazılar DeFi
---

DeFi yani merkeziyetsiz finans dünyası, klasik finans dünyasında kullanılan her tür aracın bir kopyasını çıkarmaya devam ediyor. Gelin bu yazımızda bu araçlardan opsiyon piyasalarına bir göz atalım. 

Hatırlarsanız daha önceki yazılarımızda, DeFi'nin girmeye başladığı klasik finans alanlarından mevduat ve krediyi [MakerDAO](https://medium.com/turansert/merkeziyetsiz-finans-ve-maker-dao-bir-y%C4%B1lda-neler-de%C4%9Fi%C5%9Fti-f133e9cd4007) ve [Compound](https://www.btchaber.com/klasik-bankaciligin-rakibi-compound/), sigortacılığı [Nexus Mutual](https://www.btchaber.com/defi-sigortasi-nexus-mutual/), borsacılık işlemlerini [Uniswap](https://www.btchaber.com/nedir-bu-uniswap/) ve [rakipleri](https://www.btchaber.com/uniswap-rakipleri-curve-balancer-ve-sushiswap/), sentetik türev ürünlerini [Synthetix](https://www.btchaber.com/defi-turev-piyasasi-synthetix-nasil-calisiyor/) ve portföy yönetimini ise [Yearn](https://www.btchaber.com/merkeziyetsiz-portfoy-yonetimi-platformu-yearn-finance/) örneklerinden yola çıkarak anlatmıştık. Bu yazımızda ise, klasik finansın temel direklerinden biri olan opsiyon piyasaları merkeziyetsiz nasıl çalıştığına hızlıca bir göz atacağız. Ama önce tam olarak bilmeyenler için opsiyonun ne olduğuna ve nasıl çalıştığına bir bakalım: 

### Opsiyon nedir, ne işe yarar?
En basit anlatımı ile opsiyon, herhangi bir varlığı gelecekte istediğiniz bir tarihte, belli bir fiyattan alma ya da satma hakkına sahip olmak demek. 

#### Alım opsiyonu
Varsayalım bir varlığa sahip olmak istiyorsunuz, ancak bugün için alma imkanınız yok. Birkaç hafta sonra olacak, ama o zaman çok geç olabilir, varlık sizin alabileceğinizin çok üstünde bir değere çıkabilir. 

Ne yapacaksınız bu durumda, fırsat kaçacak mı? Hayır. Şimdi almak yerine, ileride belirli bir fiyattan o varlığı satın alma hakkına sahip olabilirsiniz. Yani bu varlık için bir **'alım opsiyonu' (ingilizcesi 'call option')** kullanabilirsiniz. 

Bu size ne verir? İleride olası bir hızlı yükselişte kârı kaçırmama fırsatı. Bilirsiniz ki, varlığın değeri yükselse bile siz onu belli bir fiyattan alabileceksiniz. Yok, o gün geldi ve varlığın değeri uçup gitmedi, tam tersine düştü, o zaman ödediniz prim dışında bir kaybınız yok. Alım opsiyonunu kullanmazsınız, olur biter.

#### Satım opsiyonu 
Bunun tam tersi de mümkün. Varsayalım, elinizde tuttuğunuz herhangi bir varlığın değerinin gelecekte nasıl bir seyir izleyeceğini kestiremiyorsunuz. 

Bu durumda o varlığı gelecekte belli bir fiyattan satma hakkını almak isterseniz, o varlık için  **'satım opsiyonu' (ingilizcesi 'put option')** kullanabilirsiniz. 

Bu size ne verir? En azından kafa rahatlığı. Bilirsiniz ki, gelecekte o varlığın fiyatı korkunç bir şekilde düşerse bile, siz baştan belirlenmiş bir fiyattan varlığı satıp zarar etmekten kurtulabilirsiniz. Eğer korktuğunuz gerçekleşmez ve varlığın değeri tam tersine yükselirse, o zaman da opsiyon maliyeti dışında hiç bir zararınız olmaz. Satma hakkını kullanmaz ve varlığı değerlenmiş haliyle elinizde tutmaya devam edersiniz (ya da satıp kârı realize edersiniz).

 | ![skyscraper_cleaners](/assets/glass-facade-817732_640.jpg)|
|:--:| 
| *Image by [Gerhard Bögner](https://pixabay.com/users/bogitw-851103/) from [Pixabay](https://pixabay.com/)*|

#### Rakamsal bir örnek mi versek?
Call ve put opsiyonlarını bir örnek ile açıklayalım:

Bir varlığın şu anki değeri 1.000 TL olsun. Bunu bir ay sonra da 1.000 TL'ye alma hakkı yani 'call' opsiyonun değeri de 50 TL diyelim. Bu, size 50 TL bedel karşılığı aynı varlığı bir ay sonra garantili 1.000 TL'ye alma hakkı veriyor. 

Varsayalım bir ay sonra varlığın değeri 1.200 TL'ye yükseldi. Bu durumda, kazancınız varlığın değer artışı olan 200 TL eksi opsiyon maliyeti 50 TL'den net olarak 150 TL olur. Ya da varlık 900 TL'ye düştü. O zaman sadece opsiyonun maliyeti olan 50 TL'ye işin içinden sıyrılma hakkına sahipsiniz. 

'Put' opsiyonu da benzer şekilde çalışıyor. 1.000 TL değerinde bir varlığı bir ay sonra 1.000 TL'ye satma hakkını yani 'put' opsiyonu 50 TL'ye aldığınızı varsayalım. 

Bir ay sonrasında değer 800 TL'ye düşerse opsiyonu kullanarak varlığı 1.000 TL'ye satabilir ve 50 TL opsiyon bedelini ödedikten sonra net 150 TL kâra sahip olabilirsiniz. Varlığın değeri tam tersi 1.300 TL'ye çıkarsa, o zaman opsiyonu kullanmaz, bunun yerine varlığı piyasada 1.300 TL'ye satar ve opsiyonun maliyeti olan 50 TL düştükten sonra 250 TL'yi cebe atarsınız. 

Ufak bir ayrıntı daha: Eğer opsiyonu sadece vade tarihinde kullanabiliyorsanız buna **Avrupa tipi opsiyon** deniyor. Yok eğer, vade tarihine kadar herhangi bir noktada kullanma imkanınız var ise bu **Amerikan tipi opsiyon** oluyor. 

#### Tamam niye aldığımızı anladık da, kim satıyor bu opsiyonları?
Peki, bir kullanıcı olarak bunu alıyoruz, ama kim satıyor? Sizin düşündüğünüzün tam tersini bekleyen ya da düşünenler var. Onlardan alma imkanınız var. Onun ötesinde, bu işin risk yönetimini yapan profesyoneller de var. Bu kişi ve kurumlar, karmaşık ihtimal hesapları ile bu 'alım ya da satım' opsiyonlarını belli bir ücret karşılığı size satıyor ve bundan ciddi para kazanıyorlar.

### Kripto dünyasında nasıl oluyor opsiyonlar?
Kripto para dünyasının opsiyonlara ihtiyacı olduğunu söylemek o kadar da zor değil! Bu kadar belirsizliğin, inişin çıkışın olduğu bir dünyada kim akıl rahatlığı istemez ki?

Kripto dünyasına hizmet veren merkezi borsalar ve finans kurumlarında opsiyonlar oldukça yaygın olarak kullanılıyor ([Deribit](https://www.deribit.com), [FTX](https://ftx.com) bunlardan birkaçı). Profesyonel olarak çok fazla opsiyon kullanmak zorunda olanlar için, maliyeti daha düşük bu kurumlardan işlem yapmak gayet cezbedici olabilir.

Ancak, hep söylediğimiz gibi, bu bahsettiğimiz yapıların en büyük handikapı merkezi olmaları. Buralarda işlem yapanlar, aynı zamanda bu merkezi yapıların her tür riskini de almak zorunda. Üstelik, diğer kripto borsa işlemlerinde de bahsettiğimiz gibi, kullanıcılar bu tip mekanizmaları kullanabilmek için nispeten zahmetli bir üyelik ve yeterlilik (minimum işlem hacim, büyüklük gibi) sürecinden geçmek zorunda. 

Oysa merkeziyetsiz dünyanın, elektronik cüzdanını bağlayan herkese, saniyeler içinde bu hizmeti verebilmesi, rahatlık ve kolaylık anlamında büyük avantaj.  

Merkeziyetsiz yapıların şu an için temel dezavantajı, likiditenin azlığından dolayı opsiyon fiyatlarının oldukça yüksek olması. Ancak bu alanda likiditeyi artırmak için çalışmalar hızla ilerliyor ve belli bir noktaya gelmiş durumda.

### Kripto dünyasında opsiyon kullanımı klasik dünya ile aynı mı?
Yukarıdaki basit örnekte alım ve satım opsiyonlarının nasıl kullanılacağından bahsettik. Bu klasik dünyanın en temel opsiyon kullanım alanı. Kripto, yepyeni bir dünyanın kapılarını açarken, opsiyon piyasalarının kullanım alanını da yukarıdaki örnekten daha öteye taşıyor. Birkaç örnek daha verelim konuyu daha iyi anlamak için:

Varsayalım kripto para madenciliği işi yapıyorsunuz. Masraflarınız (yol, su, elektrik) fiat para ile ama geliriniz kripto para cinsinden. Ani bir düşüş olursa ne yapacaksınız? Eğer masrafları karşılayacak kadar satım opsiyonu kullanırsanız, nakit akışınızı daha düzenli hale getirip ayağınızı yorganınıza göre uzatabilirsiniz. 

Bir diğer örnek: Kripto paranız var ve likidite sağlayarak para kazanmak istiyorsunuz. Merkeziyetsiz opsiyon platformları, aynı Uniswap'ın borsa işlemlerinde ve Synthetix'in türev piyasalarında yaptığı gibi, kurdukları havuzlar aracılığıyla, bu alana yatırım yapıp para kazanmak isteyenlere ilginç fırsatlar sunuyorlar. Herhangi bir opsiyon yazma bilgisine sahip olmadan bu havuzlara katılarak, getiri kazanmak mümkün (riski unutmadan tabii). Bu havuzların kullanım şekline önümüzdeki yazımızda değineceğiz. 

### Kimler var merkeziyetsiz opsiyon piyasasında?
Merkeziyetsiz opsiyon piyasasının en büyük oyuncusu [Hegic](https://www.hegic.co/). Onu [Opyn](https://opyn.co/#/) takip ediyor. Bunların yanında yeni çıkan ya da çıkma aşamasında olan [Opium](https://opium.network), [Auctus](https://auctus.org),  [Finnexus](https://finnexus.io/#/), [Primitive](https://primitive.finance), [Pods](https://www.pods.finance) ve [Hedget](https://hedget.com) var.  

Hegic, yaklaşık 100 milyon ABD Doları'na yaklaşan üzerine kilitli para miktarı ile son zamanlarda diğer oyuncuların ciddi şekilde önüne geçmiş durumda (kilitli para miktarı, yatırımcıların havuzlara koyduğu para demek). Burada Hegic’in havuzunun henüz Ekim 2020’de başladığının da altını çizelim. İkinci ile arasındaki farka bakınca bu çok daha iyi anlaşılıyor (her ne kadar Opyn farklı bir sistem izliyor olsa da).. 

 | ![hegic_vs_opyn](/assets/hegic_vs_opyn_TVL_v2.png)|
|:--:| 
| *Hegic ve Opyn'da kilitlenen toplam miktar Kaynak:[DeFiPulse](https://defipulse.com/)*|

### Arkası yarın
Bir sonraki yazımızda Hegic örneğinden yola çıkarak opsiyon havuzları nasıl işliyor, tokenlar ne işe yarıyor onlara bakacağız. 

---

---

*Not 1: Bu yazı ilk olarak 6 Ocak 2021'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/defide-opsiyon-piyasalari/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

