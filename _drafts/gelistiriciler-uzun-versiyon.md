Bu yazımızda, artık geleneksel hale gelmeye başlayan Electric Capital'in hazırladığı 'Geliştirici Raporu'ndan ilginç çıkarımları paylaşacağız.

Kullanıcılara daha fazla söz hakkı ve oluşan katma değerden daha fazla pay vermeyi hedefleyen Web3'ün itici gücünü topluluklar oluşturuyor. Temeline insanı alan bu oluşumun kullanıcılar dışında kilit taşlarından biri de, bu dünyayı inşa eden yazılımcılar (bir başka deyişle geliştiriciler). 

Hatırlayanlar olacaktır, bundan bir yıl önce yine [bu satırlarda](/genel/2022/01/31/blokzincirin-gelecegi-geli%C5%9Ftiricilerin-elinde.html) Electric Capital tarafından yayınlanan geliştirici raporunu detaylıca ele almıştık. (Konu hakkında hiçbir bilgisi olmayanların öncelikle [o yazıya](/genel/2022/01/31/blokzincirin-gelecegi-geli%C5%9Ftiricilerin-elinde.html) göz atmasını şiddetle tavsiye ederim.)
 
Artık geleneksel hale gelmeye başlayan geliştirici [raporunun sonuncusu geçtiğimiz hafta içinde yayınlandı](https://github.com/electric-capital/developer-reports/blob/master/dev_report_2022.pdf). Gelin bu yazımızda raporun önemli noktalarına göz gezdirelim, ancak daha öncesinde bu rapor neden önemli, ne kadar kapsayıcı ve eksik yönleri neler sorularına yanıt arayalım. 

### Neden önemli bir rapor bu?

Hepimiz hemen her gün Web3 dünyası ile ilgili haberlere boğulmuş durumdayız. "Hangi blokzincir ne kadar büyümüş? Kim ne kadar yatırım almış? Kim geliştiricilere ne kadar teşvik vermiş? Kriz olunca, geliştiriciler Web3'ü terk etmeye mi başlamış?" gibi... Electric Capital'in raporu, işte bu dünyada gerçekten ne olup bittiğini sayılara dayalı somut bir şekilde ortaya koymaya çalışan en kapsamlı çalışmalardan bir tanesi. 

Temel girdi olarak kendilerine 'açık kaynak' projelerin ortak toplanma alanı olan GitHub deposunu alıyorlar. Burada bulunan yaklaşık 250 milyona yakın kod kayıtlarını (ya da yüklemelerini) sıkı bir temizlemeden geçiriyorlar. Örneğin başkasından kopyalanmış orijinal olmayan kodları silerek yaklaşık %65'ini en baştan eliyorlar [^1]. Sonrasında da bu kayıtları geliştiricilerin tipi (tam/yarı zamanlı, tek seferlik) tecrübesi (tecrübeli/yeni girmiş, tek/çoklu ağda çalışan vb), çalıştığı ağ (Ethereum, Bitcoin, alternatif L1'ler, L2'ler vb) ve son raporda olduğu gibi içinde bulundukları kullanım alanı (DeFi, NFT) gibi farklı kriterlerde toplam 180 sayfalık bir rapor haline getiriyorlar. Bu arada raporu oluşturan bütün datayı da 'açık kaynak' olarak ekosisteme sunuyorlar. Üstelik bu son rapor ile birlikte artık canlı verilerin de yer aldığı bir websitesini de ücretsiz kullanıma açmışlar 👉 www.developerreport.com

| ![sandbox](/assets/arrows-3380595_800.jpg)|
|:--:| 
| *Image by [Gerd Altmann](https://pixabay.com/users/geralt-9301/) from [Pixabay](https://pixabay.com/)*|

Rapor şimdiye kadar gördüğümüz en kapsamlı çalışma olsa da, elbette kendi içinde belirli kısıtları var. Bunlardan en önemlisi, kapsamın sadece 'açık kaynak' depoları içeriyor olması; pek çok proje (özellikle NFT'lerde) kapalı olarak çalıştıkları ve sonrasında sonuçları Github'a koydukları için kayıt sayıları düşük olabiliyor. Bu, her ne kadar haklı bir eleştiri olarak görünse de, karşı argüman olarak yazılımları kapalı bir şekilde geliştirmenin tam merkeziyetsizlik ve açık kaynak ruhuna aykırı olduğunu savunanlar da var. Bu arada ileride raporun kapsamına Github depolarının yanında, blokzincire direkt olarak yüklenmiş akıllı kontrat kodlarının da dahil edilmesinin planlandığını belirletelim.

Bir başka göz ardı edilen nokta, özellikle geliştirme sürecinde - başta yapılan testler olmak üzere - pek çok mühendislik işinin direkt Github'a kayıt gerektirmediği için kapsama girmiyor oluşu. Buna ek olarak, Github'a konan her kayıt da aynı eforu gerektirmeyebiliyor; basit ya da rutin bir değişiklik ile üzerine aylarca kafa yorulduktan sonra yapılan bir güncelleme bu rapora göre eşit muamele görüyor. 

Yine de yukarıdaki bütün kısıtlarına rağmen rapor, özellikle yıldan yıla değişen trendleri ve farklı blokzincirlerin gelişimlerini  göstermesi açısından ileriye yönelik önemli göstergeleri içinde barındırabiliyor. Gelin şimdi de raporun içeriğine bakalım: 

### Neler içeriyor rapor?

Rapor, ilk olarak yıllar itibariyle geliştirici sayılarının nasıl geliştiğine bakıyor. Burada önemli bir ayrıntı geliştiricilerin tam, yarı ve tek-seferlik geliştiriciler olarak ayrılmış olması [^2]. Daha sonrasında iki büyük - Bitcoin ile Ethereum - ve ardından gelen en büyük 200 ekosistemin karşılaştırmalı geliştirici sayıları inceleniyor. Bu karşılaştırma, özellikle çok sık duyduğumuz alternatif zincirlerin büyüklükleri ve gelişimlerini anlayabilmek için oldukça faydalı. Raporda son olarak özellikle iki büyük kullanım alanı olan merkeziyetsiz finans (DeFi) ve NFT alanına da spot ışık tutulmakta. 

Raporun başındaki yönetici özeti (sayfa 5), aslında belki de Twitter'dan da okuduğunuz temel bazı verileri (TL; DR:) vermesi açısından önemli. Gelin madde madde bunları sıralayalım: 

- Aralık 2022 itibariyle Web3 üzerinde çalışan toplam 23,343 geliştirici bulunmakta
- Her ay açık kaynak projelere Github üzerinde 471,000'den fazla kayıt yüklenmekte
- Kripto varlık değerlerindeki keskin düşüşe rağmen geliştirici sayısında bir önceki yıla göre %5 artış var. Özellikle, tam zamanlı geliştiriciler  içinde bu oran %8'e yükseliyor. 
- 2022 yılı içinde 61,000'den fazla geliştirici koda katkıda bulunmuş ki, bu tüm zamanların en yükseği[^3]
- Kripto dünyasının şu anki toplam piyasa değeri bir önceki boğa piyasası olan Ocak 2018 ile hemen hemen aynı olmasına rağmen, geliştirici sayısı aynı döneme kıyasla %297 oranında artmış. 
- Ocak 2018'den bu yana geliştirici sayılarında Bitcoin'de 3 kat, Ethereum'da 5 kat artış görülürken, diğer daha küçük ekosistemlerde de benzer şekilde 5 katı geçen artışlar yaşanmış
- Bitcoin ve Ethereum ağır toplar olsa da, geliştiricilerin %72'si diğer ekosistemlerde aktifler
- Geliştiricilerin %15'inden fazlası (3,901 geliştirici) merkeziyetsiz finans alanında çalışırken, %4 kadarı (900+) NFT alanında kod yazıyorlar. 

### Raporda ilgi çeken noktalar neler?

Yukarıda raporun ekosistem ile kuşbakışı özetini gördük. Detaylarda ilgi çekebilecek diğer noktalar da şu şekilde (İlgi çeken bir bilgiyi kaynağından görmek isterseniz rapordaki ilgili sayfa numarasına gidebilirsiniz): 

#### Geliştirici sayılarının yıl yıl değişimi

Geliştirici sayısında en tepe nokta Haziran 2022'de 26 bin ile görülürken sonrasında altı ay içinde yaklaşık %11'lik bir düşüş gerçekleşmiş. (Sayfa 35) Yarı-zamanlı ve tek-seferlik geliştiricilerin katkılarının tam zamanlılara göre çok daha fazla düşüş gösterdiğini de belirtelim (yarı zamanlı %13, tek seferlik %14'e karşılık tam zamanlı %7). (Sayfa 36)

Sektöre tam zamanlı olarak giren geliştiricilerin sektörde kalışları genel olarak da daha yüksek. Örneğin, tam zamanlıların %30'u bir sonraki yıl da kod girmeye devam ederken, bu oran tüm geliştiricilerde %8 civarında. (Sayfa 39) Benzer şekilde sektörden ayrılan (GitHub'a kayıt yapmayan) geliştiricilerin %95'i yarı-zamanlı ve tek-seferlik geliştiriciler. (Sayfa 41)

Sektöre uzun vadeli yukarıdan baktığımızda ilgi çeken bir nokta ise yıllar itibariyle geliştirici sayılarının ağların toplam değerine oranı (Sayfa 18)

| ![ecdr-dev_vs_network](/assets/electric_cap_dev_report_dev_vs_network.jpg)|
|:--:| 
| *Kaynak: [Electric Capital Developer Report](https://github.com/electric-capital/developer-reports/blob/master/dev_report_2022.pdf) - Sayfa 18*|

Kripto ağlarının toplam piyasa değerinin yaşanan ayı piyasası sonrası bir önceki boğa piyasasının zirvesi olan 2018 yılı Ocak ayı ile hemen hemen aynı seviyede olduğunu görüyoruz. Bur rağmen aylık aktif geliştirici sayı aynı dönemde yaklaşık 3 kat artmış durumda. 


##### En büyük beş ağ hangisi?

Sektörün ağır topu Ethereum'un liderliği geçen yıl olduğu gibi aynı şekilde devam etmekte. Ethereum tüm sektördeki tam zamanlı geliştiricilerin yaklaşık %25'ine sahip (Sayfa 58) ve kendisine en yakın topluluğun 2,5 katı büyüklüğünde (Sayfa 70). Sektörün 1000'den fazla toplam geliştiriciye sahip büyük beşlisi ise Ethereum, Solana, Polkadot, Cosmos ve Polygon olarak sıralanıyor[^4] (Sayfa 81) 

| ![ecdr-1st](/assets/electric_cap_dev_report_1st_grp_2022_v2.jpg)|
|:--:| 
| *Kaynak: [Electric Capital Developer Report](https://github.com/electric-capital/developer-reports/blob/master/dev_report_2022.pdf) - Sayfa 81*|

Anlaşılması zor olabileceği için grafiği kısaca açıklayalım: Grafiğin yatay düzlemi ağların 2021 yılındaki tam zamanlı geliştirici sayısını, dikey düzlem ise 2022 yılındaki aynı sayıları gösteriyor. Ortada gördüğünüz grafiği yarıdan bölen çizgi ise iki yıl sayılarının eşit olduğu nokta. Dolayısıyla, grafikten çıkan sonuç mahşerin beş atlısından sadece Polkadot'un 2022 yılında geliştirici sayısı olarak aynı kaldığı, diğer dört topluluğun geliştirici sayılarının arttığı şeklinde (hatta Solana'daki artış %50'den daha fazla olmuş). 

##### Sonraki grup?

En büyük beşli sonrası bir alt seviyede 300'ün üzeri toplam geliştiriciye sahip ekosistemler ise sırasıyla Bitcoin, Near, Polkadot'un kardeş ağı Kusama, Cardano, Internet Computer, Starknet, Tezos, The Graph, Avalanche ve Celo olarak sıralanmakta.[^5] (Sayfa 83)

| ![ecdr-2nd](/assets/electric_cap_dev_report_2nd_grp_2022.jpg)|
|:--:| 
| *Kaynak: [Electric Capital Developer Report](https://github.com/electric-capital/developer-reports/blob/master/dev_report_2022.pdf) - Sayfa 83*|

Burada dikkat çekici iki nokta, geçtiğimiz yıl sadece 40 geliştiricisi olan Starknet'in bu sayıyı üç katına çıkardığı, bunun yanında BNB Chain, Tezos ve Avalanche'in geliştirici sayılarında bir azalış görüldüğü. Starknet, özellikle zk (zero-knowledge) teknolojisi geliştiricisi olarak sektörün potansiyeli yüksek adaylarından biri olarak görülüyor. BNB Chain'de ise geçmişte verilen teşvikler nedeniyle görülen geliştirici akımının ters yönlü olarak diğer ağlara doğru kaydığını söylemek mümkün. Avalanche ise geçtiğimiz yıl piyasaya sunduğu subnet'lerindeki geliştirmelerin daha çok kapalı olması nedeniyle sayının düşük göründüğünü belirtiyor. 

Geçtiğimiz yıl ilk beş içinde yer alan Bitcoin ise bu sene bir alt lige düşmüş gibi görünüyor. Her ne kadar kötü bir performans gibi görülse de şaşırtıcı bir durum değil bu. Zira Bitcoin kendisini bir teknoloji altyapı platformu değil, dijital bir para olarak tanımlıyor. Bu nedenle Bitcoin'e öyle çok büyük geliştirici akını beklemek mantıklı değil. Bitcoin üzerinde aylık yeni katkı yapan geliştirici sayılarına baktığımızda ise karşımıza ilginç bir tablo çıkıyor (Sayfa 53): 

| ![ecdr-btc-new_dev](/assets/electric_cap_dev_report_bitcoin_new_devs_2022.jpg)|
|:--:| 
| *Kaynak: [Electric Capital Developer Report](https://github.com/electric-capital/developer-reports/blob/master/dev_report_2022.pdf) - Sayfa 53*|

2018 yılı başından bu yana kriptopara piyasa değerleri ciddi artışlar ve azalışlar gösterse de, Bitcoin ekosistemi düzenli bir şekilde hemen her ay kendisine ortalama 100 yeni geliştirici kazandırıyor. Bu da bize Bitcoin'in piyasa koşullarından etkilenmeyen 'dirençli' bir yapısı olduğunu gösteriyor. 


##### Biraz daha alt gruba 'zoom' yapalım mı? 

Yukarıdaki listelerde yer alan isimler (belki Starknet dışında) şimdiye kadar duyulmuş ve konuşulan ağlar. Yeni neler geliyor derseniz, yukarıdaki tablonun sol altında yer alan gruba 'zoom' yapmanız gerekiyor. (Sayfa 77) 


| ![ecdr-3rd](/assets/electric_cap_dev_report_3rd_grp_2022.jpg)|
|:--:| 
| *Kaynak: [Electric Capital Developer Report](https://github.com/electric-capital/developer-reports/blob/master/dev_report_2022.pdf) - Sayfa 77*|

Bu grupta en dikkat çeken iki isim, Facebook'un Diem (önceki adıyla Libra) projesinin kapanması sonrası oluşan iki ekip Aptos ve Sui. Bu ekipler Facebook sonrası toplu olarak bu projelere geçiş yaptıkları ve sonrasında ciddi yatırım aldıkları için geliştirici sayısında ciddi bir artış göstermiş durumdalar. Bunun yanında Flow, Algorand, Stacks, XRP, Stellar'ın geliştirici sayılarında bir azalış gözlemleniyor. 

 Rapor çok daha detaya inerek sayıca daha aktif geliştiricilere  de iniyor. İlgilenenlere raporu detaylıca incelemelerini hararetle tavsiye ederim.


##### Geliştiriciler büyük projelere doğru toplanıyorlar
Rapordaki bir diğer ilginç nokta ise, 2018 yılından bu yana geliştiricilerin büyük projelere doğru yönelmeye başladıkları (Sayfa 97)


| ![ecdr-btc-new_dev](/assets/electric_cap_dev_report_top200-eth-btc_2022.jpg)|
|:--:| 
| *Kaynak: [Electric Capital Developer Report](https://github.com/electric-capital/developer-reports/blob/master/dev_report_2022.pdf) - Sayfa 97*|

Bitcoin ve Ethereum dışındaki en büyük 200 proje 2018 yılı başında toplamın %25'i kadar aktif geliştiriciye sahip iken bu rakam 2022 yılı sonunda neredeyse %50'ye gelmiş durumda. Görünen o ki, eskinin 'vizyoner' ama havada kalan binlerce projesine dağılan geliştiriciler, şimdilerde daha ayağı yere basan projelere doğru kayıyorlar. 

Bu arada geliştiriciler için önemli bir nokta, ağlardan ziyade hangi teknolojiye odaklanmaları gerektiği olabilir. Orada da Ethereum Virtual Machine (EVM) kullanan ağların ağırlığı olduğunu görüyoruz. Ethereum'un 5,734 geliştiricisinin yanında, EVM kullanan diğer birinci ve ikinci seviye ağların 2,817 geliştiricisi eklendiğinde, tüm EVM kullanan ekosistemin 8,390 geliştirici ile toplam Web3 geliştiricilerinin %36'sını oluşturduğunu görüyoruz. [Sayfa 138]

Rapordaki bir başka ilginç gözlem ise, farklı projelerin farklı başlangıç tarihlerini eşleştirerek yapılan analiz olmuş. (Sayfa 122)

| ![ecdr-L1-aging](/assets/electric_cap_dev_report_L1_aging_2022.jpg)|
|:--:| 
| *Kaynak: [Electric Capital Developer Report](https://github.com/electric-capital/developer-reports/blob/master/dev_report_2022.pdf) - Sayfa 122*|

Böyle bakıldığında ilginç görünen nokta, büyük projelerin 200 tam zamanlı geliştiriciye ulaşmasının yaklaşık 4 yıl sürüyor olması (2.2 yıl süren Polkadot hariç). 

Raporda geliştiricilerin artık yavaş yavaş birden fazla ağ için geliştirme yapmaya başladıklarını da görmekteyiz. (Sayfa 145)

##### DeFi'de durum nasıl?

Rapor içinde blokzincirin en büyük uygulama alanı olan merkeziyetsiz finansa (DeFi) özel bir alan ayırılmış. Burada ilk olarak gördüğümüz, 2020 yazında başlayan DeFi'nin ilk çıkışından bu yana DeFi alanında çalışan geliştirici sayısının %240 oranında arttığı (Sayfa 161). Buna rağmen bu sayının 2021 yılına göre %9 aşağıda olduğunu belirtelim (Sayfa 162). 2022 yılının DeFi için zor bir yıl olduğunu gösteren bir başka örnek. 

Ağ bazında baktığımızda ise karşımıza şu tablo çıkıyor (Sayfa 166): 

| ![ecdr-defi-grps](/assets/electric_cap_dev_report_defi_grps_2022.jpg)|
|:--:| 
| *Kaynak: [Electric Capital Developer Report](https://github.com/electric-capital/developer-reports/blob/master/dev_report_2022.pdf) - Sayfa 166*|

Görüldüğü gibi Ethereum DeFi'nin tartışmasız bir numarası olarak en yakın rakibine geliştirici sayısında yaklaşık 3 kat fark atıyor. 

Öte yandan bu alandaki geliştiricilerin ağ olarak paylarına baktığımızda ilginç bir nokta daha var: 


| ![ecdr-defi-eth-dominance](/assets/electric_cap_dev_report_defi_eth_dominance_2022.jpg)|
|:--:| 
| *Kaynak: [Electric Capital Developer Report](https://github.com/electric-capital/developer-reports/blob/master/dev_report_2022.pdf) - Sayfa 169*|

DeFi'nin ilk çıktığı 2020 yazında tüm geliştiricilerin %70'i Ethereum üzerinde iken şimdi bu rakam %50'lere düşmüş durumda. Bu da sektöre yeni giren geliştiricilerin ağırlıklı olarak alternatif ağlara yöneldiğini gösteriyor bize. 

##### Peki ya NFT'ler?

NFT'ler ya da oyunlar ile ilgili geliştirici sayılarının güvenirliği oldukça düşük. Rapor bu durumun özellikle altını çizerek, bir geliştiricinin yazdığı ufak bir kodun, özellikle koleksiyon projelerinde çok büyük bir kitleyi kendine çekebildiğini vurguluyor. İlerisi için topluluğun proje ile bağını ve etkileşimini ölçecek yeni metrikler üzerinde çalışıldığı da ek olarak belirtilmiş. 

Raporda, yeni açılan cüzdanların yaptığı ilk hareketleri gösteren şu tablo da ilgi çekici: (Sayfa 175)


| ![ecdr-defi-nft-wallets](/assets/electric_cap_dev_report_defi_ntf_wallets_2022.jpg)|
|:--:| 
| *Kaynak: [Electric Capital Developer Report](https://github.com/electric-capital/developer-reports/blob/master/dev_report_2022.pdf) - Sayfa 175*|

2022 yılı içinde yeni açılan cüzdanların %80'inde ilk yapılan işlem NFT işlemi olmuş! Yani kripto ile ilgisi olmayan kitlenin bu alana giriş noktasının ağırlıklı NFT'lerden geçtiğini gösteren ilginç bir tablo.. 

### Sonuç

Geliştiriciler, teknoloji dünyasının önce temellerini daha sonra üzerine katlarını çıkan ve ekosistemin en kritik parçalarından birini oluşturan bir grup. Bu grubun hareketleri bize gelecek ile ilgili çok ilginç ipuçları verebiliyor. 

Electric Capital'in geliştirici raporu pek çok farklı çıkarımlar yapılabilecek bir hazine adeta. Eminim geliştirici camiası içinden rapora dudak bükecekler olacaktır. Yine de daha iyisi yapılana kadar en azından trendleri görebilmek için elimizdeki en kapsamlı çalışmalardan biri olan bu rapor dikkatlice okunmayı ve üzerine tartışılmayı hak ediyor. 

---

*Not 1: Bu yazı ilk olarak 23 Ocak 2023'de*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

---

Dipnotlar:

[^1]: Fingerprinting denen yöntem ile yazılımların ilk çıkış noktalarını belirleyip daha sonra başka projelerde kopyala/yapıştır yöntemi ile kullanılmasını, çatallamaları, açık kaynak kitaplıklarını birleştirme yoluyla oluşturulan kayıtları eliyorlar. 

[^2]: Raporda ayda 10 günden fazla kod üzerinde çalışanlara 'tam zamanlı', 10 günden az çalışanlar 'yarı-zamanlı', üç ayda en bir kez katkıda bulunanları 'tek-seferlik' geliştiriciler olarak adlandırıyorlar.  

[^3]: Toplam sayı 23,343 ama 61,000 yeni geliştirici nasıl oluyor derseniz, bir önceki nottaki tam zamanlı, yarı-zamanlı ve tek-seferlik geliştirici tanımlarına tekrar bakabilirsiniz. Eğer bir geliştirici üç aydan fazla süre katkıda bulunmuyor ise o zaman 23,343'lük geliştirici kitlesinin içine giremiyor. 

[^4]: Tam zamanlı geliştiricilerde 300'den fazla geliştiriciye sahip ilk grup için sıralama Ethereum, Polkadot, Cosmos, Solana ve Bitcoin şeklinde (sayfa 70)

[^5]: En büyük beşli sonrası bir alt seviyede 200'ün üzeri toplam geliştiriciye sahip ekosistemler ise sırasıyla Polygon, Polkadot'un kardeş ağı Kusama, Near, Cardano, Tezos, BNB Chain, Internet Computer ve Starknet olarak sıralanmakta. (Sayfa 74)
