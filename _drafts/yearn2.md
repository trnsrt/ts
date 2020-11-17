[Geçtiğimiz haftaki yazımızda](/genel/2020/11/10/Defida-merkeziyetsiz-yonetim-platform-yearn-finance.html) merkeziyetsiz portföy yönetim platformu Yearn'e göz atmış, platformun ana ürünleri olan [Earn](https://yearn.finance/earn), [yVaults](https://yearn.finance/vaults) ve [Cover](https://yinsure.finance/)'a bakmıştık.  

<a href="/genel/2020/11/10/Defida-merkeziyetsiz-yonetim-platform-yearn-finance.html">
         <img alt="Tweet" src="/assets/ts_yearn-yazi.jpg"></a>

Bu yazımızda ise gelin Yearn protokolünün tokeni YFI ile birlikte platformun risklerini değerlendirelim. 

### Ve YFI
Daha önce de birkaç kez yazdığımız gibi, merkeziyetsizlik uzun ince bir yol. Bu alanda kurulmuş pek çok girişim gibi Yearn protokolü de merkezilikten merkeziyetsizliğe benzer bir yol izledi. Başlangıçta yazılımcı [Andre Cronje](https://twitter.com/AndreCronjeTech)'den oluşan "tek kişilik bir ordu" tarafından kurulan Yearn zamanla daha geniş bir topluluk haline geldi. 

Merkeziyetsizleştirme vizyonundaki adımlara baktığımızda, yol genelde gücün kullanıcılara verilmesi ve kodların açık hale getirilmesi şeklinde başlıyor. Bunun hemen arkasından sıra yazılım/geliştirme faaliyetlerini topluluğa bırakmaya geliyor.  Son olarak platformun yönetiminin de merkeziyetsizleştirilmesi ile vizyon tamamlanıyor. 

Bu süreci planlamak kolay ancak gerçekleştirmek zor ve meşakkatli.  Özellikle son adım. DeFi alanında bu son adımı gerçekleştirmeye yönelik keskin hamle 2020 yazında yönetimi tokenlaştırma oldu (Compound ile başlayan süreç ile ilgili [şu yazımıza göz atabilirsiniz](/genel/2020/06/25/Compoundun-yonetim-tokeni-COMP-nasil-calisiyor.html))

Yearn ekibi de, kendi merkeziyetsizleştirme sürecinde benzer bir sistemi kullandı. Ekip, tabiri caiz ise 'çılgınlar gibi' yeni ürünler ardı ardına piyasaya sürerken, Temmuz ayı ortasında bir gün ansızın YFI token adında bir yönetim tokeni çıkarttı. Bu tokenin özelliği kurucu ortaklara herhangi bir pay verilmeden, tamamının kullanıcılara dağıtılmış olması.  Bu arada sadece 30.000 adet var bu tokenlardan ve yenisi gelmeyecek (en azından tüm kullanıcılar aksi bir karar vermez ise). 

Her ne kadar çıktığı sırada, Andre bangır bangır ["YFI'nin değeri yok, değeri 0" diye bağırsa da](https://medium.com/iearn/yfi-df84573db81), YFI token iki ay içinde 43.000 ABD Doları seviyesine kadar yükseldi. Sonrasında DeFi'nin ayı piyasasına girmesiyle fiyatı 8,600 ABD Doları seviyelerine kadar inse de, YFI token Kasım 2020 içinde 10.000-20.000 ABD Doları gibi geniş bir bant aralığında işlem görüyor. Bu da tüm Yearn sistemine 300-600 milyon ABD Doları arası bir değer biçilmesi anlamına geliyor. 

| ![Pulse_grafik](/assets/yearn_price_chart_800.jpg)|
|:--:| 
| *Kaynak: [CoinGecko](https://www.coingecko.com/en/coins/yearn-finance)*|

Temel olarak Yearn protokolünün yönetimini merkeziyetsiz hale getirmek için tasarlanmış olan YFI tokenları sahiplerine para da kazandırıyor. [Bir önceki yazımızda](/genel/2020/11/10/Defida-merkeziyetsiz-yonetim-platform-yearn-finance.html) bahsettiğimiz yVault ürünlerinden alınan toplam komisyonların (kârdan %5 ve kullanıcının parasını geri çekmek istemesi durumda uygulanan %0.5 cezanın toplamı bunlar) onda biri ürünü yaratan ve yöneten ekibe giderken, kalanı Yearn hazinesine kalıyor. Hazinede kalan bu para daha sonra oy kullanma yoluyla yönetime katılan YFI token sahiplerine dağıtılıyor.

Gerek kurucu ortaklara herhangi bir pay verilmemesi, gerekse yVault ürünlerinden alınan komisyonların geliştirici ekip ve kullanıcılara dağıtılması merkeziyetsizlik açısından önemli noktalar.  Neden? 

Öncelikle diğer DeFi projelerinde gördüğümüz kurucu ekibe %20-30 oranında pay verilmesi, kalan tokenları satın alan kişilerde tüm işi bu kurucu ekip yapacakmış gibi bir izlenim yaratıyor. Yearn platformunda ise, kurucu ekip baştan herhangi bir pay almadığı için sistemi yürütmek ve büyütmekte YIF token sahiplerine de sorumluluk düşüyor. Onların da böyle bir sorumluluk almak için teşvik edilmeleri gerek. İşte bu nedenlerle, yeni çıkan ürünlerde geliştiricilerin yaratılan komisyonların onda birini alması, kalan komisyonun ise oylamalara katılma karşılığı YIF sahiplerine verilmesi sistemin gelecekte de düzgün bir şekilde işlemesi için kritik. 

YFI token sahiplerinin oylamaları sonucu çıkan kararları 9 kişinin sahip olduğu bir çoklu-imza cüzdanı hayata geçiriyor. Kripto dünyasında bilinen 9 oyuncunun her birinin bir imza yetkisine sahip olduğu bu cüzdanda işlem yapmak için 6 üyenin oyu gerekiyor.  Merkeziyetsiz mi? Tam olarak değil, ama hiç yoktan iyidir. 

Özet olarak, **YIF tokeni, hem token sahiplerine oylamalara katılma karşılığı gelir sağlıyor, hem de yazılımcılara geliştirdikleri ürünlerin yarattığı komisyonlardan pay veriyor. Bu da bireylerden bağımsız uzun vadeli sürdürülebilir bir platform yaratılmasında kritik bir önem taşıyor.**

### Riskler neler?

#### Platform, platform üzerine olunca Akıllı Kontrat riski artıyor.. 
Öncelikle, Yearn ürünlerinin her birinin birer akıllı kontrat olduğunu belirtelim. Ve her bir ürünün başka başka DeFi platformları üzerinden getiri sağlamaya çalıştığını da ekleyelim. Dolayısıyla, kullanıcı yalnızca bu ürünlerin değil aynı zamanda bu ürünlerin üzerinde çalıştığı DeFi platformlarının riskini almak zorunda. 

Üstelik bir değil birden fazla platform riski var. Örneğin, [Delegated yVault](https://yearn.finance/vaults) ürününde, i) kullanıcı elinde tuttuğu kripto para (örneğin [Link](https://www.coingecko.com/en/coins/chainlink)), ii) o paranın emanet verildiği platform (örneğin [Aave](https://app.aave.com/home)), iii) karşılığında borç alınan para (mesela [USDC](https://www.coingecko.com/en/coins/usd-coin)), iv) bu paranın değerlendirildiği platform (örneğin [Curve](https://www.curve.fi/)) ve son olarak da tüm bu sistemi yöneten Yearn akıllı kontratının riskini almak zorunda. Üzerine bir de tüm sistemi yöneten Controller denen strateji yürütücünün manuel işlem yapma riskini. 

| ![yearn_complex](/assets/mark-516277_800.jpg)|
|:--:| 
| *Image by [Gerd Altmann](https://pixabay.com/users/geralt-9301/) from [Pixabay](https://pixabay.com/)*|

Açıkcası bu alanda kullanıcıyı ferahlatacak mekanizmalar çok az ve yavaş gelişiyorlar. Bunlardan bir tanesi, kod anlamında yapılan denetimler. Pek çok proje çok hızlı ilerlediği için bu denetimleri yaptırmaz iken, kendisi eski bir denetim görevlisi olduğu için Andre'nin bu konuda hassasiyet gösterdiğini görüyoruz. [Yeterli mi](https://github.com/iearn-finance/yearn-audits)? Hayır. 

Andre, hemen hemen her ortamda ürünlerinin yüksek risk içerdiğini söylüyor. Twitter profilinde "I test in prod" yazıyor, Türkçe meali "Ben ürünü çıkartırken test ederim, hatalar çıkabilir, dikkat edin". Dolayısıyla konu hakkında tecrübesi az olanların, en azından başlangıç aşamasında Yearn ürünlerinden uzak durmasında fayda olabilir. 

#### Platform ne kadar Andre'ye bağlı?

Andre çok sıkı bir programcı. Üniversite eğitimi hukuk, ancak Yearn öncesinde CryptoBriefing sitesi için değişik blokzincirleri analiz ediyor (bu arada kripto alanının en önde gelen şahsiyetlerinden Akıllı Kontratların mucidi [Nick Szabo](https://twitter.com/NickSzabo4)'nun da [hukuk eğitimi almış olması](https://en.wikipedia.org/wiki/Nick_Szabo) ilginç bir detay). Oldukça zeki ve kuvvetli bir programcı olmasının yanında gelgitleri olan biri: Kurduğu programı bir süreliğine bıraktı, hem de [bir](https://cointelegraph.com/news/one-man-defi-developer-quits-citing-hostile-community) değil [iki](https://www.coindesk.com/yearn-finances-creator-says-hes-quit-defi-but-project-has-bench-strength) kez. Verdiği kimi sözleri tutmadığı iddia edildi. Hatta bununla ilgili [Güney Afrika'da açılmış davalar olduğu söyleniyor](https://unchainedpodcast.com/why-bitcoin-now-meltem-demirors-and-lyn-alden-on-the-perfect-conditions-for-bitcoin/). 

Andre hakkında çıkan söylentileri "meyveli ağacı taşlarlar" olarak mı "ateş olmayan yerden duman çıkmaz" olarak mı değerlendirmeli o kullanıcıya kalmış. 

Zira, asıl önemli olan projenin nasıl bir topluluğa sahip olduğu. Kişisel olarak çok sevdiğim Naval Ravikant'ın geçtiğimiz günlerde yazdığı şu tweeti hatırlatayım size: "[Bir ürünün sürdürülebilmesi için bir şirket gerektiği gibi, bir protokolün devam etmesi için de bir topluluk gerekir](https://twitter.com/naval/status/1325531942431813632?s=20) . 

<a href="https://twitter.com/naval/status/1325531942431813632?s=20">
         <img alt="Tweet" src="/assets/naval_tweet_on_platforms_640.jpg"></a>

Sonuçta Yearn tarafından ortaya çıkarılan bütün ürünler açık kod. İsteyen istediği gibi içine girip bakabilir. Klasik dünyada ise o koca koca şirketlerin içinde de kim bilir neler dönüyor? "Kol kırılır yen içinde kalır" hesabı bu olaylar dış dünyaya yansıtılmıyor. Hangisi daha şeffaf ve güvenilir? 

Bir sistemin sürdürülebilirliğine bakarken belli sorular var cevaplanması gereken: Topluluk ne kadar geniş, ne kadar aktif, kurucunun topluluk içindeki payı ne? Her ne kadar Andre, Yearn protokolü içinde lider ve kritik bir role sahip olsa da, ekip onunla sınırlı değil. Örneğin DeFi dünyasının en eski ve büyük oyuncularından [MakerDAO](https://makerdao.com/en/)'nun ileri gelen yazılımcılarından [Mariano Conti](https://twitter.com/nanexcool) geçtiğimiz aylarda Yearn ekibine katıldı. Bunun yanında topluluğun Discord kanalının 8,200, Telegram kanalının ise 13,200 üyesi var. 

Keza bir önceki bölümde bahsettiğimiz YIF tokeninin ana amacı, prokolü kişilerden bağımsız topluluk tarafından sürdürülebilir hale getirmek.  

Dolayısıyla kurucusu Andre'nin gelgitlerinden bağımsız olarak Yearn protokolü, takipçi sayısı ve kullanıcısı geniş bir topluluk olarak gelecekte de DeFi'nin önemli platformlarından biri olmaya aday. 

### Neden popüler oldu Yearn ürünleri?
Öncelikle [bir önceki yazımızda](/genel/2020/11/10/Defida-merkeziyetsiz-yonetim-platform-yearn-finance.html) da belirttiğimiz gibi bu tip ürünlere piyasada gerçekten ihtiyaç var. Yearn sloganını "DeFi, simplified" (Basitleştirilmiş Merkeziyetsiz Finans) olarak belirlemiş. 

DeFi platformlarını kullanmak, ileri seviyede teknik ve finans bilmek gerektirebiliyor. Geniş kitlelerden böyle bir bilgi birikimi beklemek haksızlık. Yapılması gereken ürünleri anlaşılır hale getirmek. Yearn platformu, daha kırk fırın ekmek yemesi gerekse de, bu yolda atılmış olumlu bir adım. 

Bunun ötesinde piyasaya her gün yeni bir ürün çıkıyor. Yearn platformu, kullanıcıları farklı ürünlerin nasıl çalıştığını anlama zahmetinden kurtarıyor. 

Peki Yearn protokol en kârlı stratejileri mi uyguluyor? Hayır. [Önceki yazımızda](/genel/2020/11/10/Defida-merkeziyetsiz-yonetim-platform-yearn-finance.html) da belirttiğimiz gibi, **Yearn'ın amacı riski minimize etmek**. Tek tek yeni girişimleri incelemeyi ve daha fazla risk almayı göze alan kullanıcılar kendi başlarına daha kârlı stratejiler çizebilirler. 

Bunun yanında, özellikle yVault gibi ürünlerde, kripto para teminat göstererek kredi alıp, sonra bu krediyi farklı stabil paralarda değerlendirme stratejisi sürekli takip istiyor. Zira teminat değeri belli ürünün altına düşerse teminat yanabiliyor. yVault bu anlamda kullanıcıyı böyle bir dertten kurtarıyor. 

Yukarıda bahsettiğimiz özellikler kullanıcıların ilgisini çekti. Ancak bu, tek başına Yearn üzerinde bir milyar ABD Doları para toplanmasına yeterli değil. Baksanıza bu yaz yaşadıklarına: 

| ![Pulse_grafik](/assets/DeFi_pulse_yearn_800_v2.jpg)|
|:--:| 
| *Kaynak: [DeFi Pulse](https://defipulse.com/yearn.finance)*|

Yearn asıl büyümesini, DeFi alanında yeni ortaya çıkan yönetim tokenlarının ilk başta çok hızlı değer kazanmaları sayesinde yaşadı. Bu gelişme, Yearn ürünlerinin de benzer şekilde çok iyi getiriler sağlıyor gibi görünmesine neden oldu. ABD Doları bazında üç haneli rakamlara varan getiriler, insanların gözlerini kamaştırdı. Büyük miktarlarda "balina" olarak adlandırılan yatırımcı paraları bu alana ve Yearn platformuna yığıldı. 

### Sonra?
Sonra "deniz tükendi".  Yönetim tokenlarındaki artışların getirdiği üç haneli rakamlar tek haneli rakamlara doğru inmeye başladı. Aslında üç haneli rakamlar yanıltıcı idi. Neden? 

Çünkü gösterilen getiri, aylık getirinin bileşik hesaba göre yıllığa çevrilmesi idi. Açıkcası bu da tek gösterim yolu, zira geçmişe ait veri yok elde. Ama bu yine de yanıltıcı olduğu gerçeğini değiştirmiyor. Örneğin, aylık %5.94 getirili bir ürün her ay aynı şekilde kazandırmaya devam ederse yılda %100 getirir. Soru tabii ki her ay aynı getiriyi getirebilir mi?

Şunu söyleyelim: Yearn ürünleri hâlâ ortada ve getirileri eskisi kadar yüksek olmasa da hâlâ makul rakamlarda. Risk yönetimi açısından yukarıdaki gibi onlarca risk saysak da bu riskler genelde teknik alanda (kod hatası benzeri). Finansal olarak ise gerek Earn gerekse yVault prensip olarak kullanıcıya ellerinde tuttukları kripto paranın üzerine "risksiz getiri" sağlama mantığına göre çalışıyor. Nasıl yapıyorlar bunu? Kullanıcının kripto parasını teminat verdiklerinde, borç olarak stabil para alıp bu stabil parayı yatırım araçlarında değerlendirdikleri için. Yani, **teminat volatil (iniş-çıkışlı), ama hem yatırım yapılan hem de bu yatırım için kullanılan kredi tam tersi olarak sıfıra yakın volatileye sahip.** 

Öte yandan, sistemin kurucusu Andre Cronje ile ilgili çıkan haberler de kimi kullanıcıları sistemden soğutmuş olabilir. Örneğin, Andre'nin attığı birkaç esrarengiz tweet sonrası, kullanıcılar daha tanıtımı bile yapılmamış bir ürün için, "yüksek kazanç" hevesiyle bir ETH hesabına tam 15 milyon ABD Dolar'a yakın para yatırdılar. Sonrasında bir hacker çıkıp bu hesaptaki paralara el koydu. [Ortalık ayağa kalktı](https://www.coindesk.com/eminence-exploit-defi-compensated). Hacker insaflı çıkıp paranın 8 milyonluk kısmını geri gönderdi de  insanlar yatırdıklarının yarısını geri aldılar. Şahsen, burada Andre'yi haklı bulduğumu söylemeliyim.  Ne işe yaradığını ve hazır olup olmadığını bilmediğiniz bir ürüne, üstelik denetimden bile geçmemişken yatırım yapıyorsanız, paranızı kaybetme riskiniz olduğunu bilmeniz gerekir. Paranız yanınca Andre'den medet umuyorsanız, o zaman DeFi ile ilgili bildiklerinizi tekrar gözden geçirmenizi tavsiye ederim. 

### Gelecekte kullanıcıları neler bekliyor?

Yearn, ilk ürünlerinde zarar etme riskini minimize eden stratejiler üzerine yoğunlaşmış idi. Bunun yapmanın yolu olarak da stabil paraları seçmişti. Görünen bundan sonra daha volatil kripto paraları kullanarak daha kârlı stratejiler yürütmeye çalışacak. Örneğin, vadeli piyasaları kullanarak, ETH üzerindeki düşüş riskini yok edecek opsiyonlar satın alacak. Ancak bu opsiyonları satın almanın doğa olarak bir maliyeti var. Bu nedenle, bu stratejiyi uygularken hedefi, ETH'yi yatırarak kazanacağı getirinin opsiyon maliyetinden yüksek olmasını sağlamak olacak. 

### Sonuç
Geçtiğimiz yazıda başlayıp bu yazıya uzanan iki bölümlük serimizde, DeFi'nin en ilginç projelerinden biri olan merkeziyetsiz portföy yönetimi platformu Yearn'ı incelemeye çalıştık. Gördüğünüz gibi hareketli, dalgalı, inişli-çıkışlı bir süreci geri bıraktı Yearn. Ama bu süreçte tek bir kişinin tekelinden geniş bir topluluğun aidiyet hissettiği ve büyütmeye çalıştığı bir proje haline geldi. DeFi piyasasındaki gelişmeler Yearn platformuna da yeni ürünler çıkarması için uygun ortamı yaratacak. Geliştiriciler bu fırsatları değerlendirerek yeni ürünler çıkaracaklar mı? Kullanıcılar bu ürünleri kullanacaklar mı? Hep birlikte yaşayarak göreceğiz. 
