DeFi yani merkeziyetsiz finans dünyası, klasik finans dünyasında kullanılan her tür aracı bir kopyasını çıkarmaya devam ediyor. Gelin bu yazımızda bunlardan opsiyon piyasalarına bir göz atalım. 

Hatırlarsanız daha önceki yazılarımızda, klasik finansın kapsadığı alanlardan, mevduat ve kredi vermeyi [MakerDAO](https://medium.com/turansert/merkeziyetsiz-finans-ve-maker-dao-bir-y%C4%B1lda-neler-de%C4%9Fi%C5%9Fti-f133e9cd4007) ve [Compound](https://www.btchaber.com/klasik-bankaciligin-rakibi-compound/), sigortacılığı [Nexus Mutual](https://www.btchaber.com/defi-sigortasi-nexus-mutual/), para borsasını [Uniswap](https://www.btchaber.com/nedir-bu-uniswap/) ve [rakipleri](https://www.btchaber.com/uniswap-rakipleri-curve-balancer-ve-sushiswap/), sentetik türev ürünlerini [Synthetix](https://www.btchaber.com/defi-turev-piyasasi-synthetix-nasil-calisiyor/), portföy yönetimini ise [Yearn](https://www.btchaber.com/merkeziyetsiz-portfoy-yonetimi-platformu-yearn-finance/) örneklerinden yola çıkarak anlatmıştık. Bu yazımızda ise, klasik finansın en temel direklerinden biri olan opsiyon piyasaları merkeziyetsiz nasıl oluyor bir göz atalım. 

### Opsiyon nedir, ne işe yarar?
En basit anlatımı ile opsiyon, herhangi bir varlığı gelecekte istediğiniz bir tarihte, belli bir fiyattan alma ya da satma hakkına sahip olmak demek. 

#### Alım opsiyonu
Varsayalım bir varlığa sahip olmak istiyorsunuz, ancak bugün için o an alma imkanınız yok. Birkaç hafta sonra ise olacak, ama o zaman çok geç olabilir, varlık sizin alabileceğinizin çok üstünde bir değere çıkabilir. Ne yapabilirsiniz? İleride belli bir fiyattan o varlığı satın alma hakkına sahip olabilirsiniz. Yani bu varlık için bir 'alım opsiyonu' (Ingilizcesi call option) alabilirsiniz. Bu size ne verir? İleride olası bir hızlı yükselişte kârı kaçırmama fırsatı. Bilirsiniz ki, varlığın değeri yükselse bile siz onu belli bir fiyattan alabileceksiniz. Yok, varlığın değeri uçup gitmedi, tam tersine düştü, o zaman bir kaybınız yok. Alım opsiyonunu kullanmazsınız, olur biter.

#### Satım opsiyonu 
Bunun tam tersi de mümkün. Elinizde tuttuğunuz herhangi bir varlığın değerinin gelecekte nasıl bir seyir izleyeceğini kestiremiyorsunuz. Bu durumda o varlığı gelecekte belli bir fiyattan satma hakkını almak isterseniz, o varlık için  'satım opsiyonu' (ingilizcesi 'put option') alabilirsiniz. Bu size ne verir? En azından kafa rahatlığı. Bilirsiniz ki, gelecekte o varlığın fiyatı korkunç bir şekilde düşse bile, siz o baştan belirli fiyattan satıp zarar etmekten kurtulabilirsiniz. Eğer korktuğunuz gerçekleşmez ve varlığın değeri tam tersine yükselirse, o zaman hiç bir zararınız olmaz. Satma hakkını kullanmaz ve varlığı değerlenmiş haliyle elinizde tutmaya devam edersiniz (ya da satıp kârlı realize edersiniz).

#### Rakamsal bir örnek mi versek?
Call ve put opsiyonlarını bir örnek ile açıklayalım. Bir varlığın şu anki değeri 1.000 TL olsun. Bunu bir ay sonra da 1.000 TL'ye alma hakkı yani call opsiyonun değeri de 50 TL diyelim. Bu size bir ay sonra aynı varlığı 50 TL bedel karşılığı garantili 1.000 TL'ye alma hakkı veriyor. Diyelim bir ay sonra varlığın değeri 1.200 TL'ye yükseldi. Bu durumda, kazancınız varlığın değer artışı olan 200 TL eksi opsiyon maliyeti 50 TL'den net olarak 150 TL olur. Diyelim varlık 900 TL'ye düştü. O zaman sadece opsiyonun maliyeti olan 50 TL'ye işin içinden sıyrılma hakkına sahipsiniz. 

Put opsiyonu da benzer şekilde çalışıyor. 1.000 TL değerli bir varlığı bir ay sonra 1.000'ye satma hakkını yani put opsiyonu 50 TL'ye aldığınızı varsayalım. Bir ay sonrasında değer 800 TL'ye düşerse opsiyonu kullanarak varlığı 1,000 TL'ye satabilir ve 50 TL opsiyon bedelini ödedikten sonra net 150 TL kâra sahip olabilirsiniz. Varlığın değeri tam tersi 1,300 TL'ye çıkarsa, o zaman opsiyonu kullanmaz, bunun yerine varlığı piyasada 1,300 TL'ye satar ve opsiyonun maliyeti olan 50 TL düştükten sonra 250 TL'yi cebe atarsınız. 

#### Tamam niye aldığımızı anladık da, kim satıyor bu opsiyonları?
Peki, bir kullanıcı olarak bunu alıyoruz, ama kim satıyor? Sizin düşündüğünüzün tam tersini bekleyen ya da düşünenler var. Onlardan alma imkanınız var. Bunun daha da ötesinde ise, bu işin risk yönetimini yapan profesyoneller var. Bunlar karmaşık ihtimal hesapları ile bu 'alım ya da satım opsiyonunu' ücreti karşılığı size satıyor ve bundan para kazanıyorlar.

### Kripto dünyasında nasıl oluyor opsiyonlar?
Kripto para dünyasının opsiyonlara ihtiyacı olduğunu söylemek o kadar da zor değil! Bu kadar belirsizliğin, inişin çıkışın olduğu bir dünyada kim akıl rahatlığı istemez ki?

Kripto dünyasına hizmet veren merkezi borsalar ve finans kurumlarında opsiyonlar oldukça yaygın olarak kullanılıyor ([Deribit](https://www.deribit.com), [FTX](https://ftx.com) bunlardan birkaçı). Profesyonel olarak çok fazla opsiyon kullanmak zorunda olanlar için maliyeti daha düşük bu kurumlardan işlem yapmak gayet cezbedici olabilir.

Ancak, hep söylediğimiz gibi, bu bahsettiğimiz yapıların en büyük handikapı merkezi olmaları. Buralarda işlem yapanlar, aynı zamanda bu merkezi yapıların her tür riskini de almak zorunda. Üstelik, diğer kripto borsa işlemlerinde de bahsettiğimiz gibi, kullanıcılar bu tip mekanizmaları kullanabilmek için nispeten zahmetli bir üyelik/yeterlilik sürecinden geçmek zorunda. 

Oysa merkeziyetsiz dünyanın, elektronik cüzdanını bağlayan herkese saniyeler içinde bu hizmeti verebilmesi gayet tabii rahatlık ve kolaylık anlamında oldukça avantajlı.  Merkeziyetsiz yapıların şu an için dezavantajı, likiditenin azlığından dolayı opsiyon fiyatlarının oldukça yüksek olması. Ancak bu alanda likiditeyi artırmak için çalışmalar sürüyor. 

### Başka kim ne için kullanılır bu piyasaları?
Yukarıdaki basit örnekte alım ve satım opsiyonlarının nasıl kullanılacağından bahsettik. Ancak bununla bitmiyor kullanım alanları. Birkaç örnek daha verelim konuyu daha iyi anlamak için:

Varsayalım kripto para madenciliği işi yapıyorsunuz. Masraflarınız fiat para ile (yol, su, elektrik) ama geliriniz kripto para cinsinden. Ani bir düşüş olursa ne yapacaksınız? Eğer masrafları karşılayacak kadar satım opsiyonu koyarsanız, nakit akışınızı daha düzenli hale getirebilirsiniz. 

Bir diğer örnek: Kripto paranız var ve likidite sağlayarak para kazanmak istiyorsunuz. Merkeziyetsiz opsiyon platformları, alım ve satım opsiyonlarını kullanıcılara sunmak dışında, aynı Uniswap ve Synthetix'de olduğu gibi, kurdukları havuzlar aracılığıyla, bu alana yatırım yapıp para kazanmak isteyenlere de ilginç fırsatlar sunuyorlar. Bu havuzların kullanım şeklinde önümüzdeki yazımızda değineceğiz. 

### Kimler var merkeziyetsiz opsiyon piyasasında?
Merkeziyetsiz opsiyon piyasasının en büyük oyuncusu [Hegic](https://www.hegic.co/). Onu [Opyn](https://opyn.co/#/) takip ediyor. Bunların yanında yeni çıkan ya da çıkma aşamasında olan [Opium](https://opium.network), [Auctus](https://auctus.org),  [Finnexus](https://finnexus.io/#/), [Primitive](https://primitive.finance), [Pods](https://www.pods.finance) ve [Hedget](https://hedget.com) var. 

### Arkası yarın
Bir sonraki yazımızda Hegic örneğinden yola çıkarak opsiyon havuzları nasıl işliyor, tokenlar ne işe yarıyor onlara bakacağız. 
