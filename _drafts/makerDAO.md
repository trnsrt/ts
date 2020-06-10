DeFi hareketinin en büyük oyuncusu MakerDAO. Gelin sisteme birlikte tekrar bakalım. 

### Nedir MakerDAO?
MakerDAO, DeFi hareketinin şu ana kadar ki en büyük oyuncusu (sabit-stabil paraları saymazsak) - bu piyasanın yaklaşık [yarısına sahip](https://defipulse.com/)

### Neden önemli?
MakerDAO, özünde merkez bankası olmaya çalışan merkeziyetsiz bir platform. Bu bile başlı başına onu ilginç yapıyor. 


### Nasıl çalışıyor?

#### DAI sabit (stabil) para

Bir merkez bankası olarak MakerDAO para basıyor - bu paranın adı DAI. DAI bir sabit (stabil) para. 1 DAI bir ABD Dolarına eşit. 

Peki diğer sabit paralardan ne farkı var bunun? Öncelikle DAI başlı başına bir yenilik. Diğer bütün sabit paraların (örneğin Tether - USDT) karşılığı bir fiat/itibari para. Yani piyasada gördüğünüz USDT'lerin karşılığı olarak bankada ABD Doları var (yani - var gibi demek daha doğru. Teoride böyle olması lazım ama Tether aslında olması gereken paranın bir kısmı ile kripto para almış - ne yapacaksınız, sonuçta bir merkezi yapı ve kapalı kutu Tether - bu da onun riski olsun, alıp almamak size kalmış). 

DAI'de ise karşılık olarak bir itibari para değil kripto para var. Ama şimdilik bunu bir kenara bırakalım. 

#### Kredi nasıl yaratılıyor?

MakerDAO'da kredi yaratmak için öncelikle teminat yatırmanız gerekiyor. Bunu da CDP denen Akıllı Kontratlar ile yapıyorsunuz. 100 birimlik kredi yaratmak için (en az) 150 birim kripto para göndermek gerekli. 

Krediyi DAI parası olarak yaratıyorsunuz. Sonra yarattığınız bu parayı borsalarda başka kripto paralara çevirebiliyorsunuz. 

Peki teminat olarak ne tür kripto para gönderebiliyorsunuz? Şu anda [ağırlıklı olarak](https://daistats.com/#/) ETH (%90 kadarı). Kalanı da WBTC - Bitcoin bazlı yaratılmış bir para. 

Sonrasında krediyi kapatmak istediğinizde borcunuz kadar DAI'yi  yakıyorsunuz (başta yarattığınız miktarı). Bunun üzerine CDP Akıllı Kontratı da teminat verdiğiniz parayı hesabınıza geri yolluyor. 

#### Ya teminatımın değeri azalırsa?

Sistemde borcunuz DAI yani sabit para - bir ABD Dolarına eşit. Ama teminatınız kripto para. Ya değer kaybederse? Çok da olmayacak bir ihtimal değil bu. 

İki strateji var izleyebileceğiniz. Birincisi teminatı baştan yüksek tutma (yani kredinizin %150'sinden daha fazla) ya da değeri azalırsa ekstra teminat yollamak. Ya da diğer bir alternatif kredinizi kapatarak teminat/kredi oranını yükseltmek. 

Eğer her ikisini de yapmazsanız, o zaman sistem sizin tuttuğunuz ETH'lerden teminatınızı müzayedeye koyuyor. Satılan ETH'ler ile DAI'ler yakılıyor ve teminat/borç oranınız %150 seviyesine çekiliyor. 

#### Peki mevduat nasıl yaratılıyor?

Bu da kredi çekmenin tam tersi aslında. Kredi çekerken kişiler ellerindeki ETH'i teminat olarak verip DAI yaratıyorlar - yani DAI olarak borçlanıyor, karşılığında da bir faiz veriyorlar. Bunun tam tersi olarak DAI sahibi olarak paranızı sisteme yatırıp bir faiz alabilirsiniz (Dai Savings Rate - DSR deniyor buna da). Gerçi Mart ayında sistemdeki bir sıkıntıdan dolayı sistemin yöneticisi (MKR tutanlar), bu faiz oranını %0 yaptılar. 

#### Kim niye kredi alır bu sistemden?

Elinizde ETH var ve yükseleceğini düşünüyorsunuz. Paraya ihtiyacınız varsa ya da bu yükselişten daha da yararlanmak istiyorsanız, ETH'nizi teminat verip DAI yaratabilirsiniz. Sonra bu DAI'yi satıp ihtiyacınızı görebilir ya da karşılığında biraz daha ETH alabilirsiniz. Böylece, efektif olarak margin trading denen kaldıraçlı işlemleri yapma imkanınına kavuşmuş olursunuz. 

#### Kim niye kredi verir peki?
Sabit/stabil para tutmak istiyorsunuz ancak Tether benzeri kripto paraların tamamen karşılıklı olmamaları sizde şüphe uyandırıyor. O zaman arkasında %150 oranında ETH olan ama ABD Dolarına bağlı tamamen merkeziyetsiz DAI alabilirsiniz. 

Yukarıda yazdığımız gibi "ya aniden ETH çok düşerse" diye kaygınız olursa o zaman da sistemin MKR satarak ödeme yapması gibi bir yol var. 

"Ya satılacak MKR'yi kimse almazsa?" diye iyice şüpheli yaklaşırsanız (ki şüphe bu dünyada her zaman iyidir), o ihtimal de düşünülmüş. Olası her tür varoluşsal kriz için sistem bütün teminatları sahiplerine geri döndürüyor. Yani diyelim elinizde DAI var - sistem bir DAI bir ABD Dolarına eşit olacak şekilde paranız kadar ETH veriyor. Ya da kredi kullanmıştınız ETH teminatlı olarak - sistem kredinizi ödeyip teminatınız olan ETH'yi size geri veriyor. 

#### Sistem nasıl yönetiliyor?

DeFi protokollerin en kritik yanlardan biri nasıl yönetildikleri oluyor. İşin ruhuna uygun olarak yönetimlerinin de merkeziyetsiz olmasını bekliyor insan. MakerDAO da kendi yönetimini demokratik bir şekilde gerçekleştirmeye çalışıyor. 

İç yönetim mekanizması için bir kripto para yaratılmış. Bu paranın adı MKR. MKR sahipleri paraları oranında sistem üzerinde söz sahibiler. Hangi konularda? Yukarıda bahsettiğimiz teminat/kredi oranında örneğin. Ya da kredilere uygulanacak faiz oranında. 

Peki MKR sahiplerinin sistemi koruyacağına nasıl emin oluyoruz? Babasının hayrına değil tabii, çıkarları var onların da bu işten. Ne tip bir çıkar? MKR sahipleri sistemi yönetmenin yanında, alınan faizler üzerinden bir komisyon alıyorlar. 

Ama bunun yanında MKR sahiplerinin sistem iyi işlemediği zaman zarar etme ihtimalleri de var. Örneğin, eğer teminat olarak kullanılan ETH ani olarak çok hızlı bir şekilde düşer ve kredileri (yani yaratılmış DAI'leri) karşılayamaz ise, o zaman sistem MKR yaratıp açık piyasada satarak kredilerin tekrar teminatlandırılmasını sağlıyor. Piyasaya durup dururken ekstradan arz yapıldığında MKR fiyatı normal olarak düşecek - o nedenle MKR sahipleri olabildiğince bu durumdan kaçacaklar. 

Yani yukarıdaki iki paragrafın özü: MKR sahipleri sistemin sigortası görevini yapıyor. Aldıkları komisyonu sigorta masrafı olarak düşünün, eğer risk gerçekleşirse ödeyecekleri maliyeti de sigortanın karşılığı olarak. Ya da daha farklı bir deyişle: Bankaların sendikasyon kredilerinde aldıkları yüklenici ücreti (underwriting fee) gibi; MKR sahipleri açılan kredileri "yükleniyorlar". 



Not: MakerDAO ile ilgili eski yazılarıma şuradan ulaşabilirsiniz: Şubat 2019 tarihli [MakerDAO kredi kullanımında çığır açar mı?](https://medium.com/@turansert/makerdao-kredi-kullan%C4%B1m%C4%B1nda-%C3%A7%C4%B1%C4%9F%C4%B1r-a%C3%A7ar-m%C4%B1-5b0d27a60bb1), Mayıs 2020 tarihli [Merkeziyetsiz Finans ve Maker DAO - bir yılda neler değişti?](https://medium.com/@turansert/merkeziyetsiz-finans-ve-maker-dao-bir-y%C4%B1lda-neler-de%C4%9Fi%C5%9Fti-f133e9cd4007)

----

- Aradan geçen zamanda neler oldu? Oran olarak büyüklükleri gösteren chart
- En iyi test zaman - olgunlaşması, nasıl
- Başından geçen kriz
- Governance nasıl değişmiş
- Rakipler gelmiş mi?
- Single DAI'den multi DAI'ye geçiş
- 

Bir sonraki yazıda: 
MakerDAO nasıl bir merkez bankası gibi çalışıyor? DAI Stability Fee bankanın DAI'nin arzı tarafındaki para politikasını belirlemesini sağlarken, DAI savings rate ise DAI'ye talep kısmında politika belirlemesini sağlıyor? [Peki bunu kim yapıyor](https://ethereumprice.org/guides/article/dai-savings-rate-explained/)? Yönetim kimin elinde?.. 

https://ethereumprice.org/guides/article/dai-savings-rate-explained/
