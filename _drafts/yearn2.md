
[Geçtiğimiz haftaki yazımızda](/genel/2020/11/10/Defida-merkeziyetsiz-yonetim-platform-yearn-finance.html), merkeziyetsiz portföy yönetim platformu Yearn'e bakmış, platformun ana ürünleri olan [Earn](https://yearn.finance/earn), [yVaults](https://yearn.finance/vaults) ve [Cover](https://yinsure.finance/)'a göz atmıştık.  Bu yazımızda ise gelin Yearn protokolü tokeni YFI ile birlikte platformun risklerine göz atıp değerlendirelim. 

### Ve YFI
Daha önce de birkaç kez yazdığımız gibi, merkeziyetsizlik uzun ince bir yol. Pek çok girişim gibi Yearn protokolü yazılımcı [Andre Cronje](https://twitter.com/AndreCronjeTech)'den oluşan "tek kişilik bir ordu" tarafından kuruldu. Tamamen Andre insiyatifinde gelişen Yearn daha sonra geniş bir topluluk haline geldi. 

Merkeziyetsizleştirme vizyonundaki adımlara baktığımızda, başlangıç genelde gücün kullanıcılara verilmesi ve kodların açık olması oluyor. Bunun hemen arkasında yazılım/geliştirme faaliyetlerini topluluğa bırakmak geliyor. En son adım ise, tüm platformun yönetimini de merkeziyetsizleştirme oluyor. Bu süreci planlamak kolay ancak gerçekleştirmek zor ve meşakkatli. 2020 yazında bu vizyona destek olacak hamle yönetimi tokenlaştırma ile gerçekleşti. 

Yearn ekibi de, kendi merkeziyetsizleştirme yolunda benzer bir sistemi kullandı. Ekip, tabiri caiz ise 'çılgınlar gibi' yeni ürünler ardı ardına piyasaya sürerken, Temmuz ayı ortasında bir gün ansızın YFI token adında bir yönetim tokeni çıkardılar. Bu tokenin özelliği kurucu ortaklara herhangi bir pay verilmeden, tamamının kullanıcılara dağıtılmış olması.  Ha bir de yalnızca 30.000 adet var bunlardan ve yenisi gelmeyecek (en azından tüm kullanıcılar aksi bir karar vermez ise). 

Her ne kadar çıktığı sırada, Andre bangır bangır ["YFI'nin değeri yok, değeri 0" diye bağırsa da](https://medium.com/iearn/yfi-df84573db81), YFI token iki ay içinde 43.000 ABD Doları seviyesine kadar yükseldi. Sonrasında DeFi'daki ayı piyasası nedeniyle düşmüş olsa da Kasım 2020 içinde yaklaşık 10.000-17.000 ABD Doları'ndan işlem görüyor. Bu da tüm Yearn sistemine 300-500 milyon ABD Doları arası bir değer biçilmesi anlamına geliyor. 

Temel olarak Yearn protokolünün yönetimini merkeziyetsiz hale getirmek için tasarlanmış olan YFI tokenları, aslında para da kazandırıyor sahiplerine. [Bir önceki yazımızda]() bahsettiğimiz yVault ürünlerinin alınan kârdan %5 para çekmeden %0.5 oranındaki komisyonların onda biri ürünü yaratan ve yöneten ekibe giderken, kalanı Yearn hazinesine gidiyor. 

Gerek kurucu ortaklara herhangi bir pay verilmemesi, gerekse yVault ürünlerinden alınan komisyonların her bir ürünü geliştirilen ekip ve yöneten kullanıcılara dağıtılması merkeziyetsizlik açısından önemli noktalar.  Neden? Öncelikle diğer DeFi projelerinde gördüğümüz gibi kurucu ekibe %20-30 oranında pay verilmesi, diğer token sahiplerinde tüm işleri kurucu ekip yapacakmış gibi bir intiba bırakıyor. Burada ise kurucu ekip herhangi bir pay almadığı için sistemi yürütmek ve büyütmekte YIF sahiplerine sorumluluk düşüyor. Bu nedenle geliştiricilerin aldığı onda bir komisyon yeni ürün çıkması, kalan Yearn hazinesinin ise oylamalara katılma karşılığı YIF sahiplerine gitmesi ise sistemin gelecekte de düzgün bir şekilde işlemesi için kritik. 

YFI tokenların oyları sonucu alınan kararları 9 kişinin sahip olduğu bir çoklu-imza cüzdanı hayata geçiriyor. Kripto dünyasında bilinen 9 oyuncunun her birinin bir imza yetkisine sahip olduğu cüzdanda işlem yapmak için 6 üyenin oyu gerekiyor. 

Özet olarak, **YIF tokeni, hem token sahiplerine oylamalara katılma karşılığı gelir sağlaması, hem de yazılımcılara geliştirdikleri ürünlerden alınan komisyonlarından pay vermesi sayesinde, bireylerden bağımsız uzun vadeli sürdürülebilir bir platform yaratılmasında kritik bir önem taşıyor.**

### Riskler

Öncelikle, Yearn ürünlerinin her birinin birer akıllı kontrat olduğunu belirtelim. Ve her bir ürünün başka başka DeFi platformları üzerinden getiri sağlamaya çalıştığını ekleyelim. Dolayısıyla, kullanıcı bu ürünlerin üzerinde çalıştığı DeFi platformlarının riskini almak zorunda. 

Üstelik bir değil birden fazla platform riski var. Örneğin, [Delegated yVault](https://yearn.finance/vaults) ürününde, i) kullanıcı elinde tuttuğu kripto para (örneğin [Link](https://www.coingecko.com/en/coins/chainlink)), ii) o paranın emanet verildiği platform (örneğin [Aave](https://app.aave.com/home)), iii) karşılığında borç alınan para (mesela [USDC](https://www.coingecko.com/en/coins/usd-coin)), iv) bu paranın değerlendirildiği platform (örneğin [Curve](https://www.curve.fi/)) ve son olarak da tüm bu sistemi yöneten Yearn akıllı kontratının riskini almak zorunda. Üzerine bir de tüm sistemi yöneten Controller denen strateji yürütücünün manuel riskini. 

Açıkcası, maalesef bu alanda kullanıcıyı ferahlatacak mekanizmalar çok az ve yavaş gelişiyor. Bunlardan bir tanesi, kod anlamında yapılan denetimler. Pek çok proje çok hızlı ilerlediği için bu denetimleri yaptırmaz iken, kendisi eski bir denetim görevlisi olduğu için Andre'nin bu konuda hassasiyet gösterdiğini görüyoruz. [Yeterli mi](https://github.com/iearn-finance/yearn-audits)? Hayır. 

Andre, kendisi hemen hemen her ortamda, ürünlerinin yüksek risk içerdiğini söylüyor. Twitter profilinde "I test in prod" yazıyor, Türkçe meali, "Ben ürünü çıkartırken test ederim, hatalar çıkabilir, dikkat edin". Dolayısıyla konu hakkında tecrübesi az olanların, en azından başlangıç aşamasında uzak durmasında fayda olabilir. 

Andre çok sıkı bir programcı. Üniversite eğitimi hukuk, ancak Yearn öncesinde CryptoBriefing sitesi için değişik blokzincirlerin nasıl çalıştığını incelemeleri yapmakla meşgul olmuş (belki çok ilgisiz ama kripto alanının en ileri gelen gurularında Nick Szabo'nun da hukuk eğitimi almış olması ilginç bir detay). Oldukça zeki ve kuvvetli bir programcı olmasının yanında gelgit'leri olan biri. Kurduğu programı bir süreliğine bıraktı, hem de [bir](https://cointelegraph.com/news/one-man-defi-developer-quits-citing-hostile-community) değil [iki](https://www.coindesk.com/yearn-finances-creator-says-hes-quit-defi-but-project-has-bench-strength) kez. Verdiği kimi sözleri tutmadığı iddia edildi hatta bununla ilgili Güney Afrika'da açılmış davalar olduğu söyleniyor. Başta hemen bu kadar negatif konuşunca insana bir tedirginlik geliyor değil mi? Ama isterseniz biraz daha derinden bakalım: 

Normalde klasik bir dünyadaki bir şirket olsa, yatırımcı ya da kullanıcı şunu düşünür: Şirketin kurucusundan bağımsız olarak iç ve dış denetim kurulları var. Bunun ötesinde kanuni otoriteler var denetim yapan ve usulsüzlük olduğunda ceza yazan. DeFi'da ne yapacağız? Hangi kurum bunları denetleyecek?

İşte DeFi projelerinin özgürlük yanında kullanıcıya getirdiği sorumluklara bir başka örnek. Kullanıcı ne yapacak, nasıl kendini koruyacak? Kripto dünyasının en başından beri yazılıp çizilen "DYOR - Do your own research - kendi araştırmanı kendin yap" sloganı, evet bu dünyanın risklerini anlatmak için geçerli ama bir yandan da geniş kitlelerin bu alana girmesinin önündeki en büyük engel. Ne yapmalı kullanıcı?

Andre hakkında çıkan söylentileri "meyveli ağacı taşlarlar" olarak mı "ateş olmayan yerden duman çıkmaz" olarak mı değerlendirmeli o kullanıcıya kalmış. 

Zira, asıl önemli olan projenin nasıl bir topluluğa sahip olduğu? Kişisel olarak çok sevdiğim Naval Ravikant'ın geçtiğimiz günlerde yazdığı şu tweet'i hatırlayalım "[Bir ürünün sürdürülebilmesi için bir şirket gerektiği gibi, bir protokolün devam etmesi için bir topluluk gerekir](https://twitter.com/naval/status/1325531942431813632?s=20) . Sonuçta Yearn tarafından ortaya çıkarılan bütün ürünler açık kod. İsteyen istediği gibi içine girip bakabilir. Klasik dünyada ise o koca koca şirketlerin içinde de kim bilir neler dönüyor? "Kol kırılır yen içinde kalır" hesabı bu olaylar dış dünyaya yansıtılmıyor. Hangisi daha şeffaf ve güvenilir? 

Topluluk ne kadar geniş, ne kadar aktif, kurucunun topluluk içindeki payı ne? Her ne kadar Andre, Yearn protokolü içinde lider ve kritik bir role sahip olsa da, ekip onunla sınırlı değil. Örneğin DeFi dünyasının en eski ve büyük oyuncularından MakerDAO'nun ileri gelen yazılımcılarından [Mariano Conti](https://twitter.com/nanexcool) geçtiğimiz aylarda Yearn ekibine katıldı. Bunun yanında topluluğun Discord kanalının 8,200, Telegram kanalının ise 13,200 üyesi var. 

Keza bir önceki bölümde bahsettiğimiz YIF tokeninin ana amacı, prokolü kişilerden bağımsız topluluk tarafından sürdürülebilir hale getirmek.  

Dolayısıyla kurucusu Andre'nin gel-git'lerinden bağımsız olara Yearn protokolü takipçisi, kullanıcısı geniş topluluğu ile gelecekte de DeFi'nin önemli platformlarından biri olmaya aday. 

### Neden popüler oldu Yearn ürünleri?
Öncelikle bir önceki yazımızda da belirttiğimiz gibi bu tip ürünlere piyasada gerçekten ihtiyaç var. Yearn sloganını "DeFi, simplified" (Basitleştirilmiş Merkeziyetsiz Finans) olarak belirlemiş. 

Öncelikle piyasaya her gün yeni bir ürün çıkıyor. Yearn ürünleri, kullanıcıları en uygun/en kârlı sonucu alabilmek için farklı farklı protokollerin nasıl çalıştığını anlama zahmetinden kurtarıyor. 

Peki Yearn protokol en kârlı stratejileri mi uyguluyor? Hayır. [Önceki yazımızda](https://turansert.com/genel/2020/11/10/Defida-merkeziyetsiz-yonetim-platform-yearn-finance.html) da belirttiğimiz gibi, Yearn'ın amacı riski minimize etmek. Tek tek yeni girişimleri inceleme ve daha fazla risk almayı göze alan kullanıcılar kendi başlarına daha kârlı stratejiler çizebilirler. 

Bunun yanında, özellikle yVault gibi, elindeki parayı teminat göstererek kredi alıp, sonra bu krediyi farklı stabil paralarda değerlendirme sonrası, kullanıcının sürekli olarak koyduğu teminatın yeterli olup olmadığını sürekli kontrol etmesi gerekiyor. Zira teminat belli bir oranın altına düşerse yanabiliyor. yVault bu anlamda kullanıcıyı böyle bir dertten kurtarıyor. 

Yukarıda bahsettiğimiz özellikler kullanıcıların ilgisini çekti. Ancak bu, tek başına Yearn üzerinde bir milyar ABD Doları para toplanmasına yeterli değil. Baksanıza bu yaz yaşadıklarına. 

| ![Pulse_grafik](/assets/DeFi_pulse_yearn_800.jpg)|
|:--:| 
| *Kaynak: [DeFi Pulse](https://defipulse.com/yearn.finance)*|

Yearn asıl büyümesini DeFi alanında yeni ortaya çıkan yönetim tokenlarının ilk başta çok hızlı değer kazanmaları sayesinde yaşadı. Bu gelişme, Yearn ürünlerinin de benzer şekilde çok iyi getiriler sağlıyor gibi görünmesine neden oldu. ABD Doları bazında üç haneli rakamlara varan getiriler insanların gözlerini kamaştırdı. Büyük miktarlarda "balina" olarak adlandırılan yatırımcı paralar bu alana ve Yearn'a yığıldı. 

### Sonra?
Sonra "deniz tükendi".  Yönetim tokenlarındaki artışların getirdiği üç haneli rakamlar tek haneli rakamlara doğru inmeye başladı. Aslında üç haneli rakamlar yanıltıcı idi. Neden? Çünkü gösterilen getiri, aylık getirinin bileşik hesaba göre yıllığa çevrilmesi idi - açıkcası bu da tek gösterim yolu, zira geçmişe ait veri yok elde. Ama bu yine de yanıltıcı olduğu gerçeğini değiştirmiyor. Örneğin, aylık %5.94 getirili bir ürün her ay aynı şekilde kazandırmaya devam ederse yılda %100 getirir. Soru tabii ki her ay aynı getiriyi getirebilir mi?

Şunu söyleyelim, Yearn ürünleri hâlâ ortada ve getirileri eskisi kadar yüksek olmasa da hâlâ makul rakamlarda. Risk yönetimi açısında yukarıdaki gibi onlarca risk saysak da bu riskler genelde teknik (kod hatası benzeri). Finansal olarak ise gerek Earn gerekse yVault prensip olarak kullanıcıya ellerinde tuttuları kripto paranın üzerine "risksiz getiri" sağlama mantığına göre çalışıyorlar. Neden? Çünkü, kullanıcının kripto parasını teminat verdiklerinde borç olarak stabil para alıp bu stabil parayı yatırım araçlarında değerlendirdikleri için. 

Öte yandan, sistemin kurucusu Andre Cronje ile ilgili çıkan haberler de kimi kullanıcıları sistemden soğutmuş olabilir. Örneğin, Andre'nin attığı birkaç esrarengiz tweet sonrası, kullanıcılar daha tanıtımı bile yapılmamış bir ürün için, "erken kazanç" hevesiyle bir ETH hesabına tam 15 milyon ABD Dolar'a yakın para yatırdılar. Sonrasında bir hacker çıkıp bu hesaptaki paralara el koydu. [Ortalık ayağa kalktı](https://www.coindesk.com/eminence-exploit-defi-compensated). Hacker insaflı çıkıp paranın 8 milyonluk kısmını geri gönderdi de  insanlar yatırdıklarının yarısını geri aldılar. Şahsen, burada Andre'yi haklı bulduğumu söylemeliyim.  Ne işe yaradığını ve hazır olup olmadığını bilmediğiniz bir ürüne üstelik denetimden bile geçmemişken yatırım yapıyorsanız, paranızı kaybetme riskiniz olduğunu bilmeniz gerekir. Paranız yanınca Andre'den medet umuyorsanız, o zaman DeFi ile ilgili bildiklerinizi tekrar gözden geçirmenizi tavsiye ederim. 

### Gelecekte kullanıcıları neler bekliyor?

Yearn ilk ürünlerinde zarar etme riskini minimize eden stratejiler üzerine yoğunlaşmış idi. Bunun yapmanın yolu olarak da stabil paraları seçmişti. Görünen bundan sonra daha volatil kripto paraları kullanarak daha kârlı stratejiler yürütmeye çalışacak. Örneğin, vadeli piyasaları kullanarak, ETH üzerindeki düşüş riskini yok edecek opsiyonlar satın alacak. Bu opsiyonları satın almanın bir maliyeti var doğal olarak. Bu nedenle bu stratejiyi uygularken hedefi, mevcut stabil paralar için kullandığı stratejiyi ETH'ye uygulayıp kazandığı getirinin opsiyon maliyetinden yüksek olmasını sağlamak olacak. 

### Sonuç
Geçtiğimiz yazıda başlayıp bu yazıya uzanan iki bölümlük serimizde, DeFi'nin en ilginç projelerinden biri olan merkeziyetsiz portföy yönetimi platformu Yearn'ı incelemeye çalıştık. Gördüğünüz gibi hareketli, dalgalı, inişli-çıkışlı bir süreci geri bıraktı Yearn. Ama bu süreçte tek bir kişinin tekelinden geniş bir topluluğun aidiyet hissettiği ve büyütmeye çalıştığı bir proje haline geldi. DeFi piyasasındaki yeni gelişimler Yearn'ın da kullanıcıları için yeni ürünler çıkarması için uygun ortamı yaratacak. Geliştiriciler bu fırsatları değerlendirerek yeni ürünler çıkaracaklar mı, kullanıcılar bu ürünleri kullanacaklar mı, hep birlikte yaşayarak göreceğiz. 
