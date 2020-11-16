
[Geçtiğimiz haftaki yazımızda](/genel/2020/11/10/Defida-merkeziyetsiz-yonetim-platform-yearn-finance.html), merkeziyetsiz portföy yönetim platformu Yearn'e bakmış, platformun ana ürünleri olan [Earn](https://yearn.finance/earn), [yVaults](https://yearn.finance/vaults) ve [Cover](https://yinsure.finance/)'a göz atmıştık.  Bu yazımızda ise gelin Yearn protokolü tokeni YFI ile birlikte platformun risklerine göz atıp değerlendirelim. 

### Ve YFI
Daha önce de birkaç kez yazdığımız gibi, merkeziyetsizlik uzun ince bir yol. Pek çok girişim gibi Yearn protokolü yazılımcı [Andre Cronje](https://twitter.com/AndreCronjeTech)'den oluşan "tek kişilik bir ordu" tarafından kuruldu. Tamamen Andre insiyatifinde gelişen Yearn daha sonra geniş bir topluluk haline geldi. 

Merkeziyetsizleştirme vizyonundaki adımlara baktığımızda, başlangıç genelde gücün kullanıcılara verilmesi ve kodların açık olması oluyor. Bunun hemen arkasında yazılım/geliştirme faaliyetlerini topluluğa bırakmak geliyor. En son adım ise, tüm platformun yönetimini de merkeziyetsizleştirme oluyor. Bu süreci planlamak kolay ancak gerçekleştirmek zor ve meşakkatli. 2020 yazında bu vizyona destek olacak hamle yönetimi tokenlaştırma ile gerçekleşti. 

Yearn ekibi de, kendi merkeziyetsizleştirme yolunda benzer bir sistemi kullandı. Ekip, tabiri caiz ise 'çılgınlar gibi' yeni ürünler ardı ardına piyasaya sürerken, Temmuz ayı ortasında bir gün ansızın YFI token adında bir yönetim tokeni çıkardılar. Bu tokenin özelliği kurucu ortaklara herhangi bir pay verilmeden, tamamının kullanıcılara dağıtılmış olması.  Bu arada sadece 30.000 adet var bunlardan ve yenisi gelmeyecek (en azından tüm kullanıcılar aksi bir karar vermez ise). 

Her ne kadar çıktığı sırada, Andre bangır bangır ["YFI'nin değeri yok, değeri 0" diye bağırsa da](https://medium.com/iearn/yfi-df84573db81), YFI token iki ay içinde 43.000 ABD Doları seviyesine kadar yükseldi. Sonrasında DeFi'nin ayı piyasasına girmesiyle fiyatı 8,600 ABD Doları seviyelerine kadar inse de, Kasım 2020 içinde 10.000-18.000 ABD Doları gibi geniş bir bant aralığında işlem görüyor. Bu da tüm Yearn sistemine 300-550 milyon ABD Doları arası bir değer biçilmesi anlamına geliyor. 

Temel olarak Yearn protokolünün yönetimini merkeziyetsiz hale getirmek için tasarlanmış olan YFI tokenları sahiplerine para da kazandırıyor. [Bir önceki yazımızda](/genel/2020/11/10/Defida-merkeziyetsiz-yonetim-platform-yearn-finance.html) bahsettiğimiz yVault ürünlerinden alınan toplam komisyonların (kârdan %5 ve kullanıcının parasını geri çekmek istemesi durumda uygulanan %0.5'in toplamı bunlar) onda biri ürünü yaratan ve yöneten ekibe giderken, kalanı Yearn hazinesinde kalıyor. Hazinede kalan bu para YFI token sahiplerine dağıtılıyor.

Gerek kurucu ortaklara herhangi bir pay verilmemesi, gerekse yVault ürünlerinden alınan komisyonların geliştirici ekip ve kullanıcılara dağıtılması merkeziyetsizlik açısından önemli noktalar.  Neden? Öncelikle diğer DeFi projelerinde gördüğümüz gibi kurucu ekibe %20-30 oranında pay verilmesi, diğer token sahiplerinde tüm işleri kurucu ekip yapacakmış gibi bir izlenim yaratıyor. Burada ise kurucu ekip, baştan herhangi bir pay almadığı için sistemi yürütmek ve büyütmekte YIF sahiplerine de sorumluluk düşüyor. Bu nedenle geliştiricilerin aldığı onda bir komisyon yeni ürün çıkması, kalan Yearn hazinesinin ise oylamalara katılma karşılığı YIF sahiplerine gitmesi sistemin gelecekte de düzgün bir şekilde işlemesi için kritik. 

YFI tokenların oyları sonucu alınan kararları 9 kişinin sahip olduğu bir çoklu-imza cüzdanı hayata geçiriyor. Kripto dünyasında bilinen 9 oyuncunun her birinin bir imza yetkisine sahip olduğu cüzdanda işlem yapmak için 6 üyenin oyu gerekiyor. 

Özet olarak, **YIF tokeni, hem token sahiplerine oylamalara katılma karşılığı gelir sağlıyor, hem de yazılımcılara geliştirdikleri ürünlerden alınan komisyonlardan pay veriyor. Bu da bireylerden bağımsız uzun vadeli sürdürülebilir bir platform yaratılmasında kritik bir önem taşıyor.**

### Riskler neler?

#### Platform, platform üzerine olunca Akıllı Kontrat riski artıyor.. 
Öncelikle, Yearn ürünlerinin her birinin birer akıllı kontrat olduğunu belirtelim. Ve her bir ürünün başka başka DeFi platformları üzerinden getiri sağlamaya çalıştığını ekleyelim. Dolayısıyla, kullanıcı bu ürünlerin üzerinde çalıştığı DeFi platformlarının riskini almak zorunda. 

Üstelik bir değil birden fazla platform riski var. Örneğin, [Delegated yVault](https://yearn.finance/vaults) ürününde, i) kullanıcı elinde tuttuğu kripto para (örneğin [Link](https://www.coingecko.com/en/coins/chainlink)), ii) o paranın emanet verildiği platform (örneğin [Aave](https://app.aave.com/home)), iii) karşılığında borç alınan para (mesela [USDC](https://www.coingecko.com/en/coins/usd-coin)), iv) bu paranın değerlendirildiği platform (örneğin [Curve](https://www.curve.fi/)) ve son olarak da tüm bu sistemi yöneten Yearn akıllı kontratının riskini almak zorunda. Üzerine bir de tüm sistemi yöneten Controller denen strateji yürütücünün manuel riskini. 

Açıkcası, maalesef bu alanda kullanıcıyı ferahlatacak mekanizmalar çok az ve yavaş gelişiyor. Bunlardan bir tanesi, kod anlamında yapılan denetimler. Pek çok proje çok hızlı ilerlediği için bu denetimleri yaptırmaz iken, kendisi eski bir denetim görevlisi olduğu için Andre'nin bu konuda hassasiyet gösterdiğini görüyoruz. [Yeterli mi](https://github.com/iearn-finance/yearn-audits)? Hayır. 

Andre, hemen hemen her ortamda ürünlerinin yüksek risk içerdiğini söylüyor. Twitter profilinde "I test in prod" yazıyor, Türkçe meali "Ben ürünü çıkartırken test ederim, hatalar çıkabilir, dikkat edin". Dolayısıyla konu hakkında tecrübesi az olanların, en azından başlangıç aşamasında Yearn ürünlerinden uzak durmasında fayda olabilir. 

#### Platform ne kadar Andre'ye bağlı?

Andre çok sıkı bir programcı. Üniversite eğitimi hukuk, ancak Yearn öncesinde CryptoBriefing sitesi için değişik blokzincirlerin nasıl analiz ediyor imiş (bu arada kripto alanının en önde gelen şahsiyetlerinden Akıllı Kontratların mucidi [Nick Szabo](https://twitter.com/NickSzabo4)'nun da hukuk eğitimi almış olması ilginç bir detay). Oldukça zeki ve kuvvetli bir programcı olmasının yanında gelgitleri olan biri. Kurduğu programı bir süreliğine bıraktı, hem de [bir](https://cointelegraph.com/news/one-man-defi-developer-quits-citing-hostile-community) değil [iki](https://www.coindesk.com/yearn-finances-creator-says-hes-quit-defi-but-project-has-bench-strength) kez. Verdiği kimi sözleri tutmadığı iddia edildi. Hatta bununla ilgili [Güney Afrika'da açılmış davalar olduğu söyleniyor](https://unchainedpodcast.com/why-bitcoin-now-meltem-demirors-and-lyn-alden-on-the-perfect-conditions-for-bitcoin/). Başta hemen bu kadar negatif konuşunca insana bir tedirginlik geliyor değil mi? Ama isterseniz biraz daha derinden bakalım: 

Andre hakkında çıkan söylentileri "meyveli ağacı taşlarlar" olarak mı "ateş olmayan yerden duman çıkmaz" olarak mı değerlendirmeli o kullanıcıya kalmış. 

Zira, asıl önemli olan projenin nasıl bir topluluğa sahip olduğu. Kişisel olarak çok sevdiğim Naval Ravikant'ın geçtiğimiz günlerde yazdığı şu tweeti hatırlatayım size: "[Bir ürünün sürdürülebilmesi için bir şirket gerektiği gibi, bir protokolün devam etmesi için de bir topluluk gerekir](https://twitter.com/naval/status/1325531942431813632?s=20) . Sonuçta Yearn tarafından ortaya çıkarılan bütün ürünler açık kod. İsteyen istediği gibi içine girip bakabilir. Klasik dünyada ise o koca koca şirketlerin içinde de kim bilir neler dönüyor? "Kol kırılır yen içinde kalır" hesabı bu olaylar dış dünyaya yansıtılmıyor. Hangisi daha şeffaf ve güvenilir? 

Bir sistemin sürdürülebilirliğine bakarken belli sorular var cevaplanması gereken: Topluluk ne kadar geniş, ne kadar aktif, kurucunun topluluk içindeki payı ne? Her ne kadar Andre, Yearn protokolü içinde lider ve kritik bir role sahip olsa da, ekip onunla sınırlı değil. Örneğin DeFi dünyasının en eski ve büyük oyuncularından MakerDAO'nun ileri gelen yazılımcılarından [Mariano Conti](https://twitter.com/nanexcool) geçtiğimiz aylarda Yearn ekibine katıldı. Bunun yanında topluluğun Discord kanalının 8,200, Telegram kanalının ise 13,200 üyesi var. 

Keza bir önceki bölümde bahsettiğimiz YIF tokeninin ana amacı, prokolü kişilerden bağımsız topluluk tarafından sürdürülebilir hale getirmek.  

Dolayısıyla kurucusu Andre'nin gelgitlerinden bağımsız olarak Yearn protokolü, takipçi sayısı ve kullanıcısı geniş bir topluluk olarak gelecekte de DeFi'nin önemli platformlarından biri olmaya aday. 

### Neden popüler oldu Yearn ürünleri?
Öncelikle bir önceki yazımızda da belirttiğimiz gibi bu tip ürünlere piyasada gerçekten ihtiyaç var. Yearn sloganını "DeFi, simplified" (Basitleştirilmiş Merkeziyetsiz Finans) olarak belirlemiş. 

Öncelikle piyasaya her gün yeni bir ürün çıkıyor. Yearn ürünleri, kullanıcıları en uygun/en kârlı sonucu alabilmek için farklı farklı protokollerin nasıl çalıştığını anlama zahmetinden kurtarıyor. 

Peki Yearn protokol en kârlı stratejileri mi uyguluyor? Hayır. [Önceki yazımızda](https://turansert.com/genel/2020/11/10/Defida-merkeziyetsiz-yonetim-platform-yearn-finance.html) da belirttiğimiz gibi, Yearn'ın amacı riski minimize etmek. Tek tek yeni girişimleri inceleme ve daha fazla risk almayı göze alan kullanıcılar kendi başlarına daha kârlı stratejiler çizebilirler. 

Bunun yanında, özellikle yVault gibi, kripto para teminat göstererek kredi alıp, sonra bu krediyi farklı stabil paralarda değerlendirme stratejisi sürekli takip istiyor. Zira teminat değeri belli ürünün altına düşerse teminat yanabiliyor.  yVault bu anlamda kullanıcıyı böyle bir dertten kurtarıyor. 

Yukarıda bahsettiğimiz özellikler kullanıcıların ilgisini çekti. Ancak bu, tek başına Yearn üzerinde bir milyar ABD Doları para toplanmasına yeterli değil. Baksanıza bu yaz yaşadıklarına. 

| ![Pulse_grafik](/assets/DeFi_pulse_yearn_800_v2.jpg)|
|:--:| 
| *Kaynak: [DeFi Pulse](https://defipulse.com/yearn.finance)*|

Yearn asıl büyümesini DeFi alanında yeni ortaya çıkan yönetim tokenlarının ilk başta çok hızlı değer kazanmaları sayesinde yaşadı. Bu gelişme, Yearn ürünlerinin de benzer şekilde çok iyi getiriler sağlıyor gibi görünmesine neden oldu. ABD Doları bazında üç haneli rakamlara varan getiriler insanların gözlerini kamaştırdı. Büyük miktarlarda "balina" olarak adlandırılan yatırımcı paralar bu alana ve Yearn'a yığıldı. 

### Sonra?
Sonra "deniz tükendi".  Yönetim tokenlarındaki artışların getirdiği üç haneli rakamlar tek haneli rakamlara doğru inmeye başladı. Aslında üç haneli rakamlar yanıltıcı idi. Neden? Çünkü gösterilen getiri, aylık getirinin bileşik hesaba göre yıllığa çevrilmesi idi - açıkcası bu da tek gösterim yolu, zira geçmişe ait veri yok elde. Ama bu yine de yanıltıcı olduğu gerçeğini değiştirmiyor. Örneğin, aylık %5.94 getirili bir ürün her ay aynı şekilde kazandırmaya devam ederse yılda %100 getirir. Soru tabii ki her ay aynı getiriyi getirebilir mi?

Şunu söyleyelim, Yearn ürünleri hâlâ ortada ve getirileri eskisi kadar yüksek olmasa da hâlâ makul rakamlarda. Risk yönetimi açısından yukarıdaki gibi onlarca risk saysak da bu riskler genelde teknik alanda (kod hatası benzeri). Finansal olarak ise gerek Earn gerekse yVault prensip olarak kullanıcıya ellerinde tuttukları kripto paranın üzerine "risksiz getiri" sağlama mantığına göre çalışıyorlar. Neden? Çünkü, kullanıcının kripto parasını teminat verdiklerinde borç olarak stabil para alıp bu stabil parayı yatırım araçlarında değerlendirdikleri için. 

Öte yandan, sistemin kurucusu Andre Cronje ile ilgili çıkan haberler de kimi kullanıcıları sistemden soğutmuş olabilir. Örneğin, Andre'nin attığı birkaç esrarengiz tweet sonrası, kullanıcılar daha tanıtımı bile yapılmamış bir ürün için, "yüksek kazanç" hevesiyle bir ETH hesabına tam 15 milyon ABD Dolar'a yakın para yatırdılar. Sonrasında bir hacker çıkıp bu hesaptaki paralara el koydu. [Ortalık ayağa kalktı](https://www.coindesk.com/eminence-exploit-defi-compensated). Hacker insaflı çıkıp paranın 8 milyonluk kısmını geri gönderdi de  insanlar yatırdıklarının yarısını geri aldılar. Şahsen, burada Andre'yi haklı bulduğumu söylemeliyim.  Ne işe yaradığını ve hazır olup olmadığını bilmediğiniz bir ürüne üstelik denetimden bile geçmemişken yatırım yapıyorsanız, paranızı kaybetme riskiniz olduğunu bilmeniz gerekir. Paranız yanınca Andre'den medet umuyorsanız, o zaman DeFi ile ilgili bildiklerinizi tekrar gözden geçirmenizi tavsiye ederim. 

### Gelecekte kullanıcıları neler bekliyor?

Yearn ilk ürünlerinde zarar etme riskini minimize eden stratejiler üzerine yoğunlaşmış idi. Bunun yapmanın yolu olarak da stabil paraları seçmişti. Görünen bundan sonra daha volatil kripto paraları kullanarak daha kârlı stratejiler yürütmeye çalışacak. Örneğin, vadeli piyasaları kullanarak, ETH üzerindeki düşüş riskini yok edecek opsiyonlar satın alacak. Bu opsiyonları satın almanın bir maliyeti var doğal olarak. Bu nedenle bu stratejiyi uygularken hedefi, mevcut stabil paralar için kullandığı stratejiyi ETH'ye uygulayıp kazandığı getirinin opsiyon maliyetinden yüksek olmasını sağlamak olacak. 

### Sonuç
Geçtiğimiz yazıda başlayıp bu yazıya uzanan iki bölümlük serimizde, DeFi'nin en ilginç projelerinden biri olan merkeziyetsiz portföy yönetimi platformu Yearn'ı incelemeye çalıştık. Gördüğünüz gibi hareketli, dalgalı, inişli-çıkışlı bir süreci geri bıraktı Yearn. Ama bu süreçte tek bir kişinin tekelinden geniş bir topluluğun aidiyet hissettiği ve büyütmeye çalıştığı bir proje haline geldi. DeFi piyasasındaki gelişmeler Yearn platformuna da yeni ürünler çıkarması için uygun ortamı yaratacak. Geliştiriciler bu fırsatları değerlendirerek yeni ürünler çıkaracaklar mı? Kullanıcılar bu ürünleri kullanacaklar mı? Hep birlikte yaşayarak göreceğiz. 
