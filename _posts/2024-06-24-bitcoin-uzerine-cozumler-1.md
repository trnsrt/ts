---
layout: post
title:  "Bitcoin üzerine ikinci seviye çözümler - I"
date:   2024-06-25 11:17:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Gelin önümüzdeki iki yazıda, özellikle son bir yıldır adını daha sık duymaya başladığımız Bitcoin üzerine geliştirilen ikinci seviye çözümlere bakalım. Bu yazımızda, Bitcoin’in daha geniş kesimlerce kullanımının önemini ve bunu kimlerin istediğine göz atacağız. Bir sonraki yazımızda ise Bitcoin üzerindeki çözümlerin tarihçesini, son zamanlarda hızlanmalarına neden olan gelişmeleri ve bu gelişmelerin geleceğini inceleyeceğiz.

### Blokzincirlerin ölçeklenme sorunu
Blokzincir için temel olarak kendisi üzerine yazılan bilgileri sonsuza kadar tutan bir kayıt defteri teknolojisi denebilir. Bu defter üzerine yazılan bilgilerin doğru bir şekilde tutulması ve sonradan bozulmaması için defteri tutanların çok sayıda ve birbirinden bağımsız olması lazım. Neden? Az sayıda olurlarsa, tek bir elden kontrol edilebilirler. Böyle bir durumda, ileride bir gün bu 'tek el' dışarıdan gelen baskılara karşı koyamayabilir ve kayıtları değiştirebilir ya da kimi insanların kayıtlarını sistem üzerinde işlemeyebilir. 

Defter tutanların sayısını çok fazla yapmak istediğinizde, defteri basit tutmanız gerekiyor. Eğer bunun tam aksi sisteme karmaşık işlemler koymaya başlarsanız, bu defteri tutan ya da doğruluğunu kontrol eden makineler yavaş yavaş devreden çıkıyorlar, çünkü güçleri yetmiyor!. O zaman da yine az sayıda makine ve merkezileşme sorunu ortaya çıkıyor. 

### Zincirler bu duruma nasıl çare üretiyorlar?

Büyük blokzincirlerden biri olan Solana bu soruna, "teknoloji zaten gelişiyor, makineler de gelişiyor, ben güçlü makineler ile yola devam edeceğim" şeklinde bir felsefe ile yaklaşıyor. 

Diğer büyük zincir olan Ethereum ise "ben merkeziyetsizlikten ödün vermem, kullanıcının taleplerini karşılamak için bu yükü üzerime kurulu olan ikinci seviye çözümlere (İngilizce roll-up, Türkçesi 'dürüm' gibi düşünebilirsiniz) atıyorum" diyor. 

### Peki ya Bitcoin?

Peki ya en büyük blokzincir olan Bitcoin ne yapıyor? Öncelikle şunu belirtelim, Ethereum ya da Solana gibi zincirler tüm dünyanın üzerinde farklı farklı işlemler yapacakları bir altyapı kurmaya çalışıyorlar. Bu nedenle bu zincirlere aynı zamanda 'akıllı kontrat platformu' deniyor. Bitcoin'in ise böyle bir derdi yok! Bu sistemi kurup geliştirenlerin temel derdi, sadece ve sadece değer transferinde kullanılacak, sansür edilemeyen bir paraya sahip bir sistem kurmak. Akıllı kontratlar ile yapılacak farklı işlemlerin sistemi yoracağından endişe eden Bitcoin, basitleşmek adına akıllı kontratlara karşı hasmane bir tutum sergiliyor. 

Yukarıdaki paragrafta, 'Bitcoin sistemini geliştirenler' diye bir tanım kullandık. Temel sistemi kuran geliştiriciler dediğimiz bu grup, Bitcoin'in lokomotifi olsa da aslında tüm ekosistemin sadece bir parçasını oluşturuyor. Ekosistem içinde başka oyuncular da var ve bu oyuncuların talep ve beklentileri geliştiricilerden farklı olabiliyor. 

### Bitcoin ekosisteminde geliştiriciler dışında başka kimler var?

#### Madenciler
Bitcoin ekosisteminin geliştiriciler dışında bir başka önemli aktörü sistemin operasyonel olarak güvenli bir şekilde işlemesini sağlayan madenciler. Madenciler, bir yandan sistemin cefakar 'hamalları' olarak bütün yükü çekerken, bir yandan da dış dünyadan gelen "ama Bitcoin de çok fazla enerji harcıyor" gibi söylemleri göğüslemek zorunda kalıyorlar. 

Bununla da bitmiyor madencilerin çilesi. Ödül kazanmak için amansız bir mücadele içindeler. Rekabetin gün be gün arttığını çok net bir şekilde izleyebiliyoruz. Madencilerin ödül kazanmak için sarf ettikleri efor, ödüle hak kazanmak için kendilerine verilen bir bulmacayı çözerken yaptıkları deneme sayısı (İngilizce 'hash rate') ile ölçülüyor ve bu rakam gün geçtikçe artıyor. 

| ![hash-rate](/assets/hash-rate.png)|
|:--:| 
| *Madencilerin saniyede yaptıkları deneme sayısı. Kaynak:  [Bitcoin.com](https://www.blockchain.com/explorer/charts/hash-rate)*|

Öte yandan diğer bir temel sorun ise, verilen ödüllerin her dört yılda bir azalıyor olması. Peki ne yapacak bu durumda madenciler? Taş mı yesinler? Uzun vadede madenciler için kurtuluşun temel yolu diğer gelir kalemleri olan Bitcoin üzerinde yapılan işlemlerden alacakları komisyonların artmasından geçiyor. 

Uzunca bir süredir Bitcoin üzerinde ödenen işlem ücretleri ödüllerin yanında yok denecek kadar az idi, ta ki geçtiğimiz yıla kadar. 2023 yılı başında ortaya çıkan Ordinals protokolü sayesinde, işlem ücretlerinin madencilerin gelir kalemleri içinde %5 civarına çıktığını gördük. 

| ![hash-rate](/assets/bitcoin-madenci-odulleri.png)|
|:--:| 
| *Madencilerin günlük kazançları (milyon ABD Doları - 7 günlük ortalamalar). Kaynak:  [TheBlock](https://www.theblock.co/data/on-chain-metrics/bitcoin)*|

Bitcoin üzerinde işlem sayısının artması madencilerin uzun vadede yaşayabilmeleri için oldukça kritik ve bunun için para transferlerinin ötesinde yeni işlemlere ihtiyaçları var. 

#### Kullanıcılar
Bitcoin ağı içindeki en önemli aktör elbette kullanıcılar. Sistemin gerçek bir değer ifade etmesi için geniş kitleler tarafından sürekli bir şekilde kullanılması gerekiyor. 

Bitcoin sistemini kurgulayan Satoshi Nakamoto, yarattığı tanıtım dokümanının (ingilizcesi 'White Paper) başlığını 'Bitcoin: Eşler Arası Elektronik Ödeme Sistemi [pdf](https://bitcoin.org/files/bitcoin-paper/bitcoin_tr.pdf) (ingilizcesi 'Bitcoin: A Peer-to-Peer Electronic Cash System') koymuştu. Ne var ki, Bitcoin'in bu vizyona ulaşabildiğini söylemek şu an için zor. Hatta bana sorarsanız, bu vizyonda bir gerileme bile var. Zira, 2010'lu yıllarda Bitcoin en azından kriptopara borsalarında alım satım yaparken işlem çifti olarak kullanılıyordu, bu konudaki liderliğini bile zaman içinde USDT, USDC gibi stabil paralara kaybetti. Şu an elinde kala kala, 'sansür edilemeyen dijital altın' söylemi kaldı sadece. Bu nedenle Bitcoin'in kullanıcılara farklı değer önerileri ile gelmesi geniş kesimlerce kullanılabilmesinin tek yolu gibi görünüyor.  

Öte yandan, Bitcoin'in 1 ile 2 trilyon ABD Doları arası değişen bir piyasa değeri var.  Kullanıcılar için büyük bir değer ama finansal olarak verimli kullanıldığını söylemek zor. Finansal piyasalarda ya da Ethereum gibi akıllı kontrat platformlarında, elinizde bir değer varsa bunu başkalarına kullandırarak (ya da teminat olarak koyup borç alarak) ekstra bir kazanç elde etmeniz, bir başka deyişle kapitalinizin verimini artırmanız mümkün. Bitcoin sistemi için aynısını söylemek mümkün değil. Dolayısıyla, büyük bir değer sistem içinde atıl olarak duruyor. 

### Arkası yarın

İşte yukarıda saydığımız madenciler ve kullanıcıların taleplerini bir iş fırsatı olarak gören bir grup geliştirici Bitcoin sistemi üzerine aynı Ethereum sisteminde olduğu gibi ikinci seviye çözümler üretmek için kolları sıvadılar. 

---

*Not 1: Bu yazı ilk olarak 25 Haziran 2024'de [BTC Haber'de yayınlandı](https://www.btchaber.com/bitcoin-ozerine-cozumler-i/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Piyasada oluşacak ihtimalleri değerlendiren bu yazıyı, yatırım tavsiyesi olarak almamanızı rica ederiz. Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*



https://www.btchaber.com/bitcoin-ozerine-cozumler-i/
