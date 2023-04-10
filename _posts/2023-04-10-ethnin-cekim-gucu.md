---
layout: post
title:  "ETH'nin çekim gücü"
date:   2023-04-10 11:17:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Bu yazımızda bu hafta başlayacak olan Ethereum'dan çekim olayının ne olduğuna ve kısa/uzun vadeli etkilerine değineceğiz.

Web3 temelli teknolojilerin en büyük altyapılarından olan Ethereum, birkaç yıl önce açıkladığı yol haritasının önemli kilometre taşlarından birine önümüzdeki hafta içinde ulaşacak. Yaklaşık iki yıldan uzun bir süredir sistem üzerine rehin edilmiş kilitli ETH'ler 12 Nisan'dan sonra çekilebilir hâle gelecek.  Gelin şimdi önce kısaca bugünlere nasıl geldik ona bakalım, sonrasında da bu olayın ekosisteme etkilerine değinelim. 

### Bugünlere nasıl geldik?
Efendim, bildiğiniz gibi Ethereum hem büyüklük hem de faaliyet süresi olarak Bitcoin'den sonra gelen ikinci büyük ağ. Dolayısıyla sistemi geliştirenler ilk kuruluş aşamasında pek çok konuda büyük ağabeyi Bitcoin'i taklit etmişler. 

Bu konulardan belki de en önemlisi sistemin işleyişini sağlayan madenciler. Madenciler kullanıcıların yaptıkları işlemleri gerçekleştirerek sistemin düzgün çalışmasını sağlayan ağır işçiler esasında. Bunu yaparken iş kanıtı denen faydalı ancak fazla enerji harcayan bir yol kullanıyorlar (ingilizcesi proof-of-work; kısaca PoW). Bitcoin topluluğuna göre burada bir sorun yok, hatta bu gerekli bir koşul bu. Doğrudur değildir, yazımızın konusu olmadığı için girmeyeceğiz. Ethereum topluluğu ise bir süre sonra yeni kurulan diğer zincirlerin çıkardığı enerji harcamayan hisse kanıtı (ingilizcesi proof-of-stake; kısaca PoS) sistemini beğeniyor. Beğenmekle de kalmıyor, kendi sistemlerini de PoS'a çevirmek için çok uzun bir süredir hummalı bir şekilde çalışıyorlar. 

Oldukça uzun süren, çetrefilli bir hazırlık dönemi geçiriyor Ethereum topluluğu. Önce çok detaylı, kapsamlı bir değişim planı sunuyor, ancak daha sonra bu planın altından kalkamayacaklarını anlıyor ve planı basitleştiriyorlar. Nihayet 2020 yılının Aralık ayında da basitleştirilmiş planı uygulamaya koyuyorlar.

Planın birinci aşamasında, sistem PoW olarak çalışmaya devam ederken, buna paralel yedek bir PoS zinciri başlatıyorlar. PoS zincirinin en önemli özelliği madencilerin yerini onaylayıcıların (ya da doğrulayıcılar; ingilizcesi 'validator') alıyor olması. Bu onaylayıcılar, sistemi yürütmek için ellerindeki ETH'yi rehin etmek zorundalar. Neden? Eğer yamuk bir hareket yaparlarsa ceza olarak rehin tuttukları bu ETH'ler yakılsın diye. 

İlk başta PoS sisteminin düzgün ve stabil çalışması için rehin edilen bu ETH'lerin geri alınmasına izin verilmiyor idi. (Bu oldukça riskli bir durum aslına bakarsanız. Paranızı sisteme belirsiz bir süreliğine kilitliyorsunuz. Tabii bunu hayrına yapmadıklarını söylemeye gerek yok; koyduğunuz paraya karşılık aldığınız bir ödül var.)

İkinci aşamada ise, topluluk geçtiğimiz yıl 15 Eylül'de PoW'u bırakıp PoS'a geçişi  sorunsuz bir şekide tamamladı. Tabii yatırımcıların bir sonraki sorusu, 'ee, ne zaman çekebileceğiz bu koyduğumuz ETH'leri?' oldu. Geliştiriciler tarih vermeyi sevmezler. Başta "altı ay ile bir yıl arası" minvalinde bir şeyler gevelediler. Nihayetinde yapılan testlerin ardından, Mart ayı içinde [Shapella](https://twitter.com/TimBeiko/status/1638971921168756736)[^1] adını verdikleri ETH'nin çekilebilmesine olanak sağlayan iyileştirmenin tarihini 12 Nisan (Türkiye saati ile 12 Nisan'ı 13 Nisan'a bağlayan gece yarısı) olarak [açıkladılar](https://twitter.com/TimBeiko/status/1640722906744487936). 

| ![domino](/assets/castle-1086896_800.jpg)|
|:--:| 
| *Image by [Andreas Lischka](https://pixabay.com/users/webandi-1460261/) from [Pixabay](https://pixabay.com/) *|

### Ne olacak şimdi?
Tarihin açıklanması ile birlikte yatırımcılar açısından en büyük soru işareti, 'ETH çekilmesinin fiyata nasıl etki edebileceği' oldu. Bunu bilebilmek oldukça zor. Değerlendirme yapabilmek için öncelikle verileri bir ortaya koyalım. 

Şu an piyasada toplam [120 milyon ETH var](https://ultrasound.money/). Rehin edilen ETH ise bunun yaklaşık %15'i yani [18 milyon civarında](https://beaconcha.in/). Bunun yanında bir de 1.1 milyon ETH kadar rehin edenlere verilecek [bir ödül var](https://etherscan.io/stat/supply). Peki, 13 Nisan'da bütün bu rehin edilmiş ETH piyasaya çıkacak mı? 

Bu sorunun cevabı hayır. Birincisi ve en önemlisi, pek çok kişi ya da kurum rehin tuttuğu parasını çekmek istemeyecek, zira koyduğu paraya güzel bir getiri elde ediyorlar (şu an için [yıllık %4.4 civarında](https://ethereum.org/en/staking/)). Bu durum sadece rehin edilen ETH için geçerli, ödül olarak verilecek ETH'ler faiz kazanmadığı için muhtemelen hemen yatırımcılar tarafından çekilecek. Bu paranın bir kısmı piyasada satılacak bir kısmı da sisteme tekrar geri rehin edilecek (çünkü getiri gayet iyi). 

İkincisi, Ethereum geliştiricileri düzenli bir çıkış planı öngörüyorlar; parasını almak isteyenler öyle bir anda kapıya yığılmayacaklar. Burada ilk öncelik hak edilmiş ödüllerin çekimine verilmiş durumda. Onun da günlük bir sınırı var, ama kısaca şunu söyleyebiliriz. Toplam 1 milyon ETH'lik ödül yaklaşık dört-beş gün içinde eşit oranlarda (günlük 258 bin ETH) çekilecek. Bundan sonra sırada rehin edilenler geliyor ki, burada da günlük 58 bin ETH çekimi gibi bir sınır var. 

Bu rakamların ne ifade ettiğini anlamak için bir karşılaştırma yapacak olursak, yukarıda bahsettiğimiz günlük çekilebilecek 258 bin ETH, şu anki ETH spot piyasa hacminin ortalama %5-10'u gibi bir tutar. 

Yukarıdaki rakamların dışında, detay sayılabilecek ama oldukça önemli başka veriler de var elimizde. Örneğin tüm rehin edilen ETH'lerin %32'si Liquid Staking (Türkçesi likit rehin) denen [Lido](https://lido.fi/ethereum), [RocketPool](https://rocketpool.net/) ve [FRAX](https://app.frax.finance/staking/overview) benzeri havuzların elinde. Bu havuzlardan büyük bir çıkış olması beklenmiyor. Neden? Çünkü buraya zamanında para koyanlar, bunun karşılığında bir token aldılar (Lido da [stETH](https://www.coingecko.com/en/coins/lido-staked-ether), Rocketpool'da [rETH](https://www.coingecko.com/en/coins/rocket-pool-eth) gibi). Bu tokenler likit yani piyasada alınıp satılıyorlar. Fiyatları da ETH'ye çok yakın. Dolayısıyla, Lido'ya para yatırmış birinin parasını bozdurmak için kilitlerin açılmasını beklemesine gerek yok. Liquid staking ile birlikte borsalar ya da staking havuzları tarafından rehin edilmiş yani hızlı çekim beklenmeyen rakam, toplam rehin edilmiş miktarın [dörtte üçüne denk](https://dune.com/xplorer/shanghai-event-dashboard) durumda[^2].

| ![stake_dagilim](/assets/eth-staker-distribution-dune.jpg)|
|:--:| 
| *Kaynak: [Dune Analytics](https://dune.com/xplorer/shanghai-event-dashboard)*|

Sonuç olarak, ortada görünenden daha küçük ama belirsizlik içeren bir denklem var. Burada, benim yazılarımda sıkça referans verdiğim [Delphi Digital](https://www.delphidigital.io/), Mart ayı içinde yayınlanan ve bu yazıda da yararlandığım bir [raporda](https://members.delphidigital.io/reports/brace-yourselves-shanghai-is-coming/), konuyla ilgili bir senaryo analizi yapmış. Bu analizde, rehin edilmiş tokenlerin yaklaşık olarak %10'unun çekileceğini öngörüyorlar[^3]. **Kısacası, 13 Nisan sonrası ilk dört-beş gün çekilen ödüllerden dolayı piyasaya girecek yüksek miktarda ETH nedeniyle hareketli günler geçirebiliriz. Sonrasında daha düzenli bir seyir izlenmesi beklenebilir.**

### Uzun vadede bizi neler bekliyor?

Yukarıda hep çekim sonrası yaşanacak fırtınalı havaya değindik. Kısa vade için ilginç, izlenmeye değer bir durum bu. İlk çalkantılı dönem geçtikten sonra ise, Ethereum için yol daha açık görünüyor. 

Öncelikle, ETH'nin üzerinde 'Demokles'in kılıcı' gibi duran 'çekim' belirsizliği ortadan kalkmış olacak. Malum, piyasalar belirsizlik sevmez ve belirsizliği aşırı biçimde fiyatlar. Zaten, aşağıdaki grafikte gördüğünüz ETH'nin BTC karşısında yaşadığı Ocak ayının ilk haftasından Mart ayı sonuna kadar yaklaşık %18,5'lik düşüşü bu belirsizliğe bağlayan önemli bir yatırımcı kitlesi var.

| ![ETH-BTC](/assets/eth-btc-trading-economics-230408-800.jpg)|
|:--:| 
| *Kaynak: [Trading Economics](https://tradingeconomics.com/ethbtc:cur)*|

İkinci olarak, önümüzdeki dönemde rehin edilen ETH miktarının artmasını da bekleyebiliriz. Zira, artık 'rehin ettiğimde ne zaman geri çekeceğim' sorusu ortadan kalkıyor ama sistem rehin edilen ETH'ye ödül vermeye devam ediyor. Başka zincirlere baktığınızda Ethereum üzerindeki staking oranının oldukça düşük olduğunu görüyorsunuz. 

| ![en-buyuk-on-zincir](/assets/en-buyuk-on-zincir-staking.png)|
|:--:| 
| *Kaynak: [Staking Rewards](https://www.stakingrewards.com/)*|

Önümüzdeki dönem için beklenti ETH üzerindeki rehin miktarının şu anki %15 seviyesinden %25-30 seviyelerine çıkması. Buradaki artışın en önemli nedeni, liquid staking servislerinin yaygınlığının artması olacak. Öyle ya, liquid staking üzerindeki en büyük belirsizlik ('acaba çekim yapılabilecek mi?') ortadan kalktıktan sonra ETH'ye birebir bağlı ama ekstradan gelir kazandıran bir token var elinizde. 

DeFi alanında, liquid staking token bazlı ürünlere ilginin artacağını söylemek kahinlik sayılmaz. stETH'yi mevduat yapabileceğiniz, ya da teminat olarak kullanıp kredi alabileceğiniz ürünler şimdiden mevcut. Hem bu ürünlerin kullanımı artacak hem de bunlara yenileri eklenecek. Bu arada, örneğin bir başka ilginç ürün ise, rehin edilmiş ETH ya da ya da bu tokenleri (stETH', rETH, cbETH ve LsETH gibi) kullanarak diğer zincirlerde rehin edilmesini sağlayan [Eigenlayer](https://www.eigenlayer.xyz/). İzlemeye değer. 

### Sonuç 

Rehin edilen ETH'lerin 13 Nisan'dan itibaren çekilebilmesi, ilk dört-beş gün boyunca piyasalara ciddi bir hareketlilik getirecek. Sonrasında ise ortadan kalkacak belirsizlik, hem yeni ürünlerin piyasaya çıkmasına hem de rehinlerin artmasına yol açacak. Ethereum topluluğu ise yol haritasında sırada bekleyen sistem iyileştirmelerine odaklanacak. 

--

*Not 1: Bu yazı ilk olarak 10 Nisan 2023'de [BTCHaber'de yayınlandı](https://www.btchaber.com/ethnin-cekim-gucu/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

--

[^1]: İlk olarak Shangai adı verilen geliştirme, Capella isimli bir başka geliştirme ile aynı anda yürürlüğe gireceği için tüm sürece ikisinin birleşimi Shapella adı verildi. 

[^2]: Bunun yanında 1468 adet sistemden çıkmış onaylayıcı [var](https://beaconscan.com/validators#exited) (toplam 47 bin ETH). Onlar da ödül kazanmadıkları için sistemden çıkacaklardır.

[^3]: Tam hesaplaması ise şu şekilde. %3.5 Kraken'dan gelecek. Malum, Kraken SEC ile yaptığı anlaşma gereği staking hizmetine son veriyor. O nedenle rehin verdiği ETH'leri geri çekmek durumunda. %1 iflas etmiş olan Celsius'un sahip olduğu ve bozdurulacak olan ETH var. %2.5 kendi evinde staking yapanların artık işin operasyonel yüküne katlanmak istemedikleri için bırakacakları düşünülüyor. %3 de yukarıda bahsettiğimiz sistemin dörtte üçünü oluşturan liquid staking, borsalar ve staking havuzlarından çıkış olacağı öngörülmüş.
