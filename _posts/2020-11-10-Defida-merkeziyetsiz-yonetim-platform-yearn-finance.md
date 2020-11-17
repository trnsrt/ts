---
layout: post
title:  "DeFi'da merkeziyetsiz portföy yönetimi: Yearn Finance"
date:   2020-11-10 18:47:56 +0300
categories: Genel
tags: Yazılar DeFi
---

Kripto paralar pek çok insan için oldukça teknik ve karışık. Sıradan bir kripto para borsasına girmeye çalışsanız bile bir sürü prosedürden geçmek zorundasınız.  Merkeziyetsiz finans alanında durum daha da içler acısı. Neden? Sıralayalım... 

- Bir kere klasik sistemlere göre temel farklar var. Anlamak için çaba sarfetmek, çok okumak ve kendini eğitmek gerekiyor.
- Denetim yok. Yatırım yaptığınız bir üründe sıkıntı yaşarsanız kendiniz ile başbaşasınız.
- Mevcut ürünleri açıklayıcı çok kaynak yok. Özellikle Türkçe olanlar çok az.
- Her geçen gün yeni bir ürün ekleniyor. Daha birini anlamadan bir yenisi çıkıyor ortaya.
- Üstelik de işlem maliyetleri çok yüksek. İşlem yapmaya kalktığınıza onlarca dolar komisyon ödemek zorunda kalıyorsunuz.

Şöyle bir hizmet olsa yatırımcının parasını alıp değerlendiren? O yere parasını koyup sonrasında gönül rahatlığı içinde işine dönse? Var mı böyle bir yer?

| ![yearn_relax](/assets/yearn_relax_800.jpg)|
|:--:| 
| *Image by [Gerd Altmann](https://pixabay.com/users/geralt-9301/) from [Pixabay](https://pixabay.com/)*|

Öncelikle söyleyelim, yukarıda bahsettiğimiz tüm dertlere çare olacak bir çözüm henüz yok. Daha doğrusu böyle çözümler mevcut ancak bunların çoğu merkezi yapılar. Paranızı alıp değerlendiren fonlar ya da aracılar var ama bu merkeziyetsizlik ruhuna çok da uygun değil. Peki ya merkeziyetsiz çözümler?

Gelin bugün 2020 yazında DeFi'nin parlayan yıldızlarından haline gelen, 'merkeziyetsiz portföy yönetimi' girişimi [Yearn](https://yearn.finance/) platformuna bakalım. 

### Ne yapar Yearn protokolü?
Yearn protokolü çok basit olarak, bir kaç belirlenmiş strateji doğrultusunda paranızı otomatik şekilde değerlendirmeye yarıyor. Çıkış amacı, riski az stabil paraları farklı platformlarda değerlendirerek ekstra getiri yaratmak. Bir başka deyişle, **geliri maksimize etmek yerine riski minimize etmek yoluya kullanıcısına makul bir getiri sağlama** hedefindeler. 

Yearn protokolünün sloganı "basitleştirilmiş merkeziyetsiz finans"("DeFi simplified"). Ancak Yearn burada ölçüyü bir parça kaçırmış sanki.  Sistemin kullanıcı arayüzleri gayet basit. Örneğin diğer tüm DeFi protokollerinde olduğu gibi kullanıcı web sitesine girdiğinde saniyeler içinde kripto cüzdanınızı bağlayıp kullanmaya başlayabiliyor. Ancak giriş ekranı o kadar basit ki, kullanıcının ne yapması gerektiğini anlaması gerçekten zaman alabiliyor, çünkü herhangi bir açıklama yok. Bunun temel nedeni, sistemin kurucusu [Andre Cronje](https://twitter.com/AndreCronjeTech)'nin bir programcı olarak ürüne odaklı olması ve birinci önceliği hızlı ürün çıkarmaya vermesi. Adeta "bu işi bilmiyorsan hiç buralarda vakit geçirme" dercesine hafif bir üstten bakış havası seziyor insan. İşte tipik bir DeFi sıkıntısı: Kullanıcı dostu, net, açıklayıcı arayüz eksikliği. 

Neyse ki topluluğun katkıları ile neyin ne olduğu ve nasıl yapılacağını anlatan [sayfalar](https://docs.yearn.finance/) websitesine sonradan eklenmiş. Ancak bu sayfaları bulmak bile kullanıcı için kolay değil. Neyse, konudan fazla sapmadan gelin ne tip ürünler var Yearn içinde, ona bakalım. 

### Ne tip ürünler var?
Yearn sitesine girince onlarca ürün görebilirsiniz, ancak temel olarak iki ana grup olduğunu söyleyebiliriz. Bunlardan birincisi, ilk çıkan ürünleri olan Earn. Bu ürünün başarısı sonrası, daha riskli bir alana girip ikinci ürünleri yVault'u çıkarıyorlar. Bunun yanında tamamen pazarlama ağırlıklı bir sigorta ürünü ve deneme aşamasında olan pek çok farklı projeyi de sitede görmek mümkün.

#### Earn
Kullanıcının parasını alıp, çeşitli borç verme protokolleri arasında gezdirerek en yüksek getiriyi otomatik olarak sağlayan [Earn](https://yearn.finance/earn) Yearn platformundan çıkan ilk ürün. 

[Daha önce bir yazımızda detaylı olarak baktığımız borç verme platformu Compound](/genel/2020/06/18/klasik-bankaciligin-rakibi-compound.html) ve rakipleri Aave ve dYdX, Earn ürününün elindeki parayı dolaştırdığı birbirine rakip üç temel DeFi projesi. **Kullanıcıların ağırlıklı olarak ABD Doları'na bağlı stabil paralarını değerlendirdiği bu ürün, hem getirisi hem de riski düşük bir yatırım alternatifi olarak öne çıkıyor. Özet olarak DeFi dünyasındaki birbirinden inişli çıkışlı kripto paralarının riskini almak istemeyen yatırımcılar için makul getiriler sunan bir araç.** 

Neden kullanıcılar Earn kullansın? Bir kaç temel nedeni var. 

Öncelikle kullanıcının farklı borç verme protokollerini sürekli olarak kontrol etmek için zamanı yok, bunun yerine elinde olan bir stabil parayı Yearn protokolüne koyup kendi işine dönebilir  - üstelik herhangi bir komisyon ödemeden.  

İkincisi, Earn para transferi sırasında çıkabilecek yüksek işlem ücretlerinden kullanıcıyı kurtarıyor - sonuçta işlem yaptığınızda ödenecek ücreti işlemin tutarı değil, yapılacak işlemin ne kadar karmaşık olduğu ve ne kadar hızlı yapmak istediğiniz belirliyor. Kullanıcının 100 ABD Doları'nı platformlar arası değiştirirken ödeyeceği ücret ile Earn'in 10 milyon ABD Doları için aynı işlemi yapmasında ödeyeceği ücret arasında öyle ahım şahım bir fark yok. 

Üçüncü önemli neden ise, Earn içinde yatırımcıların para yatırabildiği dört farklı stabil para var. Bunlar DAI, USDC, USDT, TUSD. Bütün bu paralar bir başka protokol olan Curve içinde özel bir havuzda tutuluyor. Curve, Uniswap benzeri ancak stabil paralar üzerine uzmanlaşmış merkeziyetsiz bir borsa ([şu yazımızda detayı bulabilirsiniz](/genel/2020/09/22/uniswap-rakipleri-curve-balancer-ve-sushiswap.html)). Curve kullanıcıları, bu dört stabil paraları alıp sattıkça bu havuza komisyon veriyorlar. Bu komisyonlar da Earn'e para koymuş yatırımcılara gidiyor. Dolayısıyla, bireysel olarak elde edemeyeceği ekstra bir gelir kapısına sahip oluyor kullanıcılar.

#### yVaults

Yearn ekibinin çıkardığı ikinci ürün ise, DeFi piyasasının 2020 yazında yaşadığı hızlı yükselişin temel nedenlerinden olan getiri çiftçiliği (yield farming) furyasından yararlanmayı hedefleyen [yVaults](https://yearn.finance/vaults) oldu. 

Hatırlatmak gerekirse, getiri çiftçiliği temel olarak, herhangi bir platforma likidite sağlama karşılığında komisyon geliri ile birlikte o platformun yönetim tokenlarını da kazanmak demek.  DeFi platformlarının yönetimini merkeziyetsizleştirmek için kullanıcılara dağıtılan bu tokenlar, [Uniswap](https://app.uniswap.org/) gibi merkezi olmayan borsalarda hızlıca işleme sokularak yatırımcılar ciddi kazanç sağladılar.  **yVault, bir yandan Earn gibi kullanıcının parasını stabil paralara koyuyor bir yandan da getiri çiftçiliğinden para kazanmaya çalışıyor**.

yVault'un Earn'e göre farklarına bakalım isterseniz hızlıca: 

Earn, strateji olarak en iyi borç verme oranına bakıp ona göre kullanıcının parasını uygun platforma yönlendiriyor.  yVault ise bu getirinin yanında ilgili protokolün verdiği yönetim tokenlarının piyasa değerlerini de dikkate alıyor.  Kullanıcının parasını da her iki getirinin toplamının en yüksek olduğu yere yatırıyor. 

Dolayısıyla yVault Earn'e göre daha riskli bir strateji güdüyor. Neden? Zira, burada Earn gibi borç verme protokollerinde otomatik para dolaştırmanın ötesinde, getiri çiftçiliği işini mekanik olarak yapan bir kontrolör var. Bu merkeziyetsizlik ruhuna bir parça aykırı, ancak stratejiyi belirlemek ve uygulamak için böyle bir "aracı" gerekli gibi görünüyor. 

Öte yandan, yVault ürünleri "al ve tut" stratejisi izledikleri için hangi üründen para kazandılar ise, kazandıklarını gidip yine aynı ürüne yatırıyorlar. Dolayısıyla bu getiri çiftçiliğinin prim yaptığı dönemlerde toplam getiri oranını daha da artırabiliyor. 

Bu arada, kontrolör olması manuel işlem anlamına geliyor. Bu nedenle yVault, ürünlerinde getiri çiftçiliğinden kazanılan kârın %5'ini komisyon olarak alıyor. Bir de kullanıcı parasını çekmek istediğinde eğer o ürünün boşta parası varsa kullanıcıya ücretsiz geri ödeme yapıyor, ama tüm para yatırım olarak değerlendirilmişse o zaman yatırımı bozma ücreti olarak %0.5 oranında bir komisyon kesiyor.

Başta da bahsettiğimiz gibi Earn ve yVault, stabil paralar üzerinden yatırımcıya riski az getiri stratejisine odaklanmışlar. Bunlara ek olarak kullanıcının stabil olmayan volatil paraları değerlendirebileceği bir başka ürün daha yaratmış Yearn. Aslında yapılan iş aynı, stabil parayı değerlendirmek. 

Peki ya kullanıcı elinde tuttuğu volatil kripto paradan vazgeçmek istemiyor ise ne yapacak? 

O zaman kullanıcıya stabil para bulalım ve onu değerlendirelim. Nasıl? Hatırlarsanız, bir yazımızda DeFi'nin ilk büyük platformlarından [MakerDAO'dan bahsetmiştik](/genel/2019/02/15/MakerDAO-kredi-kullaniminda-cigir-acar-mi.html). Kullanıcıların Ether teminat gösterip, DAI kredi kullanabildiği bir merkeziyetsiz sistem. İşte Yearn burada benzer bir sistemi kullanıyor. 

Delegated Vaults denen bu üründe kullanıcılar [Aave](https://www.coingecko.com/en/coins/aave) ya da [Link](https://www.coingecko.com/en/coins/chainlink) kripto parası koyup, sonrasında borç verme ve getiri çiftçiliğinden para kazanabiliyor. Nasıl oluyor bu? Sistem, kullanıcının koyduğu parayı teminat göstererek stabil para borç alıyor. Sonra bu stabil parayı yukarıdaki bahsettiğimiz yVault ürünlerine koyarak ekstra stabil para gelir kazanıyor. Kazandığı bu stabil para ile gidip orijinal para ne ise ondan satın alıp tekrar ürünün içine koyuyor. Böylece kullanıcı, sahip olduğu Aave ya da Link'in getirisinden (ve riskinden) feragat etmeden, ekstra getiri kazanma imkanına sahip oluyor.

Yalnız bu ürün diğer yVault ürünlerine göre daha riskli. Neden? Mevcut yVault risklerinin üzerinde bir de Delegated Vault ürününün getirisi eğer alınan borç için ödenen faizden az olursa, kullanıcının koyduğu paranın sistemde kilitli kalma riski var. Bu para ancak sistemdeki getiri ödenen faizden fazla olursa tekrar kullanıma açılıyor.

#### Diğer ürünler
Bunun yannda deneme anlamında pek çok yeni ürün çıkarma çabaları da sürüyor Yearn'da.. Malum, açık kaynaklı "lego" gibi bir sistem DeFi.. Bu dünyadaki ürünler aynı dili konuştukları için yeni ürün çıkarmak yıllar, aylar değil, haftalar alıyor. 

Alın örneğin [yInsure](https://yinsure.finance/) ürününü. Daha önceki [bir yazımızda bahsettiğimiz](/genel/2020/10/20/definin-sigortasi-nexus-mutual.html) DeFi'nin en büyük sigortacısı olan [Nexus Mutual](https://nexusmutual.io/) üzerinden aparılan bir sigortacılık ürünü. Bir diğer adı da [Cover](https://yinsure.finance/). Nexus Mutual, üyelerinden KYC (Know-Your-Customer yani Müşterini Tanı) prosedürü isterken, yinsure, benzer sistemi DeFi'nin KYC'den uzak kendi dünyası içinde kullanıcılarına sunuyor. 

Bunun dışında henüz ArGe aşamasında olan, şu anki mevcut DeFi sistemi içinde yaşanan aksaklıkların önüne geçip kullanıcıya daha sorunsuz bir deney sunmaya çalışan birçok ürüne sahip Yearn. Bunların ne zaman ve ne kadar yaygınlaşacağını hep birlikte göreceğiz. 

Kullanımda olan tüm Yearn ürünleri ile ilgili yatırılmış ya da yatırıma yönlendirilmiş para, günlük/haftalık/aylık kazançları topluca görebileceğiniz [bir bilgi sayfası da mevcut](https://stats.finance/yearn). 

### Arkası yarın

Bir sonraki yazımızda, Yearn'ın çıkardığı token olan YFI'ya,  hem protokol hem de token'in nasıl bir yıldız gibi parlayıp sonra neden durulduğuna ve başta kurucusu Andre  Cronje olmak üzere sistemin risklerine bakacağız.. 

---

*Not 1: Bu yazı ilk olarak 10 Kasım 2020'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/merkeziyetsiz-portfoy-yonetimi-platformu-yearn-finance/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

---
