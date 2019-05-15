Geçtiğimiz yazıda Interoperability (karşılıklı çalışabilirlik) konusuna bakmış, bu alandaki en önemli iki oyuncu olan Polkadot ve Cosmos Network'ü bu yazıya bırakmıştık. 

### Rekabet iyidir

Bu alanda çalışan pekçok network içinde en önde olan iki tanesi ile başlayalım. Aslında yaptıkları ana hatları ile aynı - Ethereum ile başlayan Blockchain'lerin birbirleri ile etkileşimde olma olayını bir adım öteye götürmek. Sadece detaylarda farklılık gösteriyorlar. 

Çok teknik detaya girmeden kim olduklarını, ortak yönlerini ve farklarını anlatalım ki, aslında interoperability denen kavram aklımızda daha netleşsin. 

### Polkadot

[Polkadot](https://polkadot.network/), Ethereum'un kurucularından ve ana gelişticilerinden [Gavin Wood](http://gavwood.com/)'un çocuğu. Gavin sonradan Ethereum'u bırakarak Polkadot üzerine yoğunlaşmaya karar veriyor. 

Her ne kadar 2014 yılına kadar uzanan bir geçmişi olsa da, Polkadot'un asıl yazılım süreci 2017 yılının sonlarında [başlıyor](https://medium.com/polkadot-network/polkadot-2018-recap-677dab3e995b). Tabii tek kişi değil çalışan. Tüm altyapının arkasında [Parity](https://www.parity.io/) ve [Web3](https://web3.foundation/) denen iki yapı var. İyi güzel de kim bunlar derseniz:

Web3 foundation Gavin Wood tarafından kurulmuş, adem-i merkezi (merkezi olmayan) bir dünya vizyonu ile hareket eden bir vakıf. Bu amacı gerçekleştirecek projelere destek veriyorlar. Başlangıçta yoğunlukla Ethereum gelişimi üzerine odaklansalar da, sonraları başka alanlara da girmiş durumdalar. 

Parity ise, 80'i aşkın geliştiriciye sahip Blockchain altyapı teknolojisi geliştiren bir yazılımcı şirketi (teknik detay: Rust dili kullanıyorlar). Açık kaynak ürünler geliştiriyorlar. Temel hedefleri Web 3 Foundation'ın vizyonunu hayata geçirereek, kişiden kişiye (P2P) işlemler aracılığı ile yürüyen, merkezi ticari güçlere bağımlı olmayan bir toplum oluşturmak. 

Adem-i merkezi yeni girişimlere altyapı sağlıyorlar kısacası. Eğer Ethereum üzerine bir proje geliştirmek istiyorsanız Parity Ethereum, yok kendi bağımsız Blockchain'inizi geliştirmek istiyorsanız [Substrate](https://www.parity.io/substrate) yazılımını size sunuyorlar. 

Polkadot'un sahibi olan Web3 Foundation bu projeyi geliştirme işini Parity'e vermiş. (Her ikisinde de Gavin Wood'un olmasının bunda payı vardır elbet :)).  İşte Polkadot da kendi ekosistemleri içindeki projelerin birbirleri ile iletişimini sağlayan bir protokol olarak hizmet veriyor.

### Cosmos Network

Cosmos Network de yapı olarak Polkadot'a benziyor. Arkasında Polkadot gibi iki yapı var. [Tendermint](https://tendermint.com/about) ve [The Interchain Foundation](https://interchain.io/) 

Tendermint, yukarıda bahsettiğimiz Parity gibi bir teknoloji geliştirme şirketi. The Interchain Foundation da, yine yukarıdaki Web3 Foundation gibi Cosmos Network'unu geliştirmek üzere İsviçre'de kurulmuş bir vakıf. Onlar da Polkadot'da Web3 Foundation'ın yaptığı gibi, Cosmos Network geliştirme işini Tendermint'e vermişler. 

### Ortak noktaları neler?

Ortak noktaları çok. Her iki ağ da, bağımsız blockchainlerin birarada yaşayacağı bir ekosistem yaratmaya çalışıyorlar. Bu ekosistemi yaratırken, dünya sadece bu ekosistemlerden oluşacak diye düşünmüyorlar doğal olarak. Diğer büyük şu an mevcut ekosistemler ile de bir köprü kuruyorlar kendilerine. Özellikle Bitcoin'in kullanıcı tarafında ağırlığı olması Bitcoin Blockchain'ine bir bağlantıları var. Yazılımcıların ağırlığının Ethereum'da olması nedeniyle oraya da bağlantıları var. 

İyi de bir ekosistem içinde olursa ne olur, ne faydası var diye aklınızdan geçiyor ise: Geçen yazıda bir örnek vermiştik. Bir tane daha verelim. Örneğin Ethereum gibi bir network üzerinde çalışan uygulamaları kullanarak, örneğin [AirSwap](https://www.airswap.io/) kişiden kişiye dijital varlık değişimi yapabilirsiniz, yani bir Blockchain'e ait token'ı bir başka Blockchain'e ait token ile değiştirebilirsiniz. Ya da kimseye başvurmadan herhangi bir kredi skorlamasına tabi olmadan kendi kendinize elinizde olan Ethereum parası ETH'i teminat verip,  DAI sabitparası borçlanabilirsiniz. 

Bütün bunlar Ethereum üzerinde kurulu yapılar arasında yapılabilir. Ancak Ethereum halka açık bir altyapı olduğu için ağır ilerliyor, ayrıca pek çok kısıtı var geliştiriciler için. İşte Polkadot ve Cosmos Network, özel yapılar olarak hem daha hızlı hareket ediyorlar, hem de Blockchain yaratıcıları daha bağımsız yapma vaadleri var. 

Bu arada hem Polkadot hem de Cosmos Network'un sistemi korumak amacıyla Proof-of-Stake algoritmalarını kullandıklarını belirtelim (o nedir diye soracak olursanız teknik olarak şu yazımızda anlatmaya çalışmıştık)


### Farkları neler peki?
Farkları aslında ayrıntılarda. Neler mi? Çok fazla teknik detaya girmeden bahsedelim. 

Madenciler kısıtlı sayıda olduğu bir Blockchain geliştiricisi olarak yeterli sayıda madenci bulmak zor olabiliyor. Polkadot ve Cosmos Network'un Blockchain'lere verdiği en önemli faydalardan biri Blockchain güvenliğini sağlayan madenci havuzu kullanımı. Bunu yaparken bir miktar farklılık gösteriyorlar. 

Polkadot, elindeki madencileri sistem içindeki Blockchain'lere eşit olarak dağıtıyor. Cosmos'da ise her bir Blockchain gelip ne kadar madenci ihtiyacı olduğunu ve bunlar için ne kadar ödül vereceğini açıklıyor - madenciler istedikleri Blockchain'in güvenliğini sağlıyorlar, daha özgür ama daha az disiplini olan bir yapı. 

İşte bu güvenlik başta olmak üzere değişik hizmetlerin nasıl verildiği konusunda Polkadot ile Cosmos arasında felsefe farkı var. 

Polkadot, tüm Blockchain'lere sabit bir hizmet veriyor. Bir parça yemekhanede tabildot veren yemekhaneler gibi. Cosmos ise daha çok alakart yemek sunuyor gibi görünüyor. 

Cosmos Network ise her bir Blockchain'i kendisine bağlamanın çok da gerçekci olmayacağı düşüncesi ile iki katmanlı bir sistem öngörüyor. Bir tarafta altyapı olarak Cosmos var. Bir tarafta da daha üst seviyede Blockchain'lerin başta güvenlik olmak üzere çeşitli ihtiyaçlarını karşılayacak ikinci bir seviye - ki buna Cosmos Hub diyorlar. Cosmos Hub, bir nevi onların neler yapacaklarını göstermek amacıyla kurdukları ağ. Ama ne kadar çok fonksiyonu barındırırsanız, üzerinizdeki (ya da içinizdeki) Blockchain'leri o kadar kısıtlamak zorunda olacağınızı düşünerek, bunu opsiyonel yapıyorlar. 

Örneğin, duymuşsunuzdur Binance geliştiricilere kendi ekosisteminde kendi kullanıcılarına yönelik bir sistem kuruyor Binancechain adında. İşte bu sistem için altyapı olarak Cosmos'u kullanacaklar, yani en yalın halinde iletişimi sağlayacak en alttaki ağı. 

### Gelecek nasıl olacak?

Gerek Polkadot gerekse Cosmos, Ethereum tarafından başlatılan interoperability kavramının bir sonraki evreye taşımaya adanmış girişimler. Her ne kadar her iki girişimin arkasında özel/kapalı yazılım grupları olsa da, bütün kodları Açık Kaynak. Yeni Blockchain girişimleri için bunları kullanmakta bir sakınca yok. Belirsiz olan, bunlardan hangisinin ivme kazanacağı ve kazanan olacağı. Belki de girişimler işlerini şansa bırakmayacak ve şu an piyasa lideri olan ancak yavaş gelişen Ethereum içinde kalmaya devam edecekler. Bunun için beş on yıl arası beklemek gerekiyor sanırım. 
