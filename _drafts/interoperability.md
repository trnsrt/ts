Geçtiğimiz yazıda Interoperability (karşılıklı çalışabilirlik) konusuna bakmış, bu alandaki en önemli iki oyuncu olan Polkadot ve Cosmos Network'ü bu yazıya bırakmıştık. 

### Rekabet iyidir

Bu alanda çalışan pekçok network içinde en önde olan iki tanesi ile başlayalım. Aslında yaptıkları ana hatları ile aynı. Sadece detaylarda farklılık gösteriyorlar. Çok teknik detaya girmeden yaptıkları ve farklarını anlatalım ki, aslında interoperability denen kavram aklımızda daha netleşsin. 

### Polkadot

[Polkadot](https://polkadot.network/), Ethereum'un kurucularından ve ana gelişticilerinden [Gavin Wood](http://gavwood.com/)'un çocuğu. Her ne kadar 2014 yılına kadar uzanan bir geçmişi olsa da, asıl geliştirilme süreci 2017 yılının sonlarında [başlıyor](https://medium.com/polkadot-network/polkadot-2018-recap-677dab3e995b). Tabii tek kişi değil çalışan. Tüm altyapının arkasında [Parity](https://www.parity.io/) ve [Web3](https://web3.foundation/) var. İyi güzel de kim bunlar derseniz:

Web3 foundation Gavin Wood tarafından kurulmuş, adem-i merkezi bir dünya vizyonu ile hareket eden bir vakıf. Bu amacı gerçekleştirecek projelere destek veriyorlar. Başlangıçta yoğunlukla Ethereum gelişimi üzerine odaklansalar da, sonraları başka alanlara da girmiş durumdalar. 

Parity ise, 80'i aşkın geliştiriciye sahip Blockchain altyapı teknolojisi geliştiren bir yazılımcı grubu (teknik detay: Rust dili kullanıyorlar). Açık kaynak ürünler geliştiriyorlar - temel hedefleri Web 3 Foundationa'ın vizyonunu hayata geçirereek, kişiden kişiye (P2P) işlemler aracılığı ile yürüyen, merkezi ticari güçlere bağımlı olmayan bir toplum oluşturmak. 

Adem-i merkezi yeni girişimlere altyapı sağlıyorlar kısacası. Eğer Ethereum üzerine bir proje geliştirmek istiyorsanız Parity Ethereum, yok kendi bağımsız Blockchain'inizi geliştirmek istiyorsanız [Substrate](https://www.parity.io/substrate) ürününü size sunuyorlar. 

Web3 Foundation da Polkadot'un geliştirme işini Parity'e vermiş. (Her ikisinde de Gavin Wood'un olmasının bunda payı vardır elbet :)).  İşte Polkadot da bu aşamada bütün bağımsız projelerin birbirleri ile iletişimini sağlayan bir protokol olarak hizmet veriyor.

### Cosmos Network

Cosmos Network de yapı olarak Polkadot'a benziyor. Arkasında Polkadot gibi iki yapı var. [Tendermint](https://tendermint.com/about) ve [The Interchain Foundation](https://interchain.io/) 

Tendermint, yukarıda bahsettiğimiz Parity gibi bir teknoloji geliştirme şirketi. The Interchain Foundation da, yine yukarıdaki Web3 Foundation gibi Cosmos Network'unu geliştirmek üzere İsviçre'de kurulmuş bir vakıf. Onlar da Polkadot'da Web3 Foundation'ın yaptığı gibi, Cosmos Network geliştirme işini Tendermint'e vermişler. 

### Ortak noktaları neler?

Ortak noktaları çok. Her iki ağ da, bağımsız blockchainlerin birarada yaşayacağı bir ekosistem yaratmaya çalışıyorlar. Bu ekosistemi yaratırken, dünya sadece bu ekosistemlerden oluşacak diye düşünmüyorlar doğal olarak. Diğer büyük şu an mevcut ekosistemler ile de bir köprü kuruyorlar kendilerine. Özellikle Bitcoin'in kullanıcı tarafında ağırlığı olması Bitcoin Blockchain'ine bir bağlantıları var. Yazılımcıların ağırlığının Ethereum'da olması nedeniyle oraya da bağlantıları var. 


### Farkları neler peki?
Farkları aslında ayrıntılarda. Neler mi? Çok fazla teknik detaya girmeden bahsedelim. 

Polkadot, tüm ekosistemin kendi oluşturduğu bir network içinde olmasını ve dışarıya bu network üzerinden kurduğu köprüler ile ulaşmayı planlıyor. Bir nevi deniz üzerine kurulu bir ada parçası olarak düşünün. 

Cosmos Network ise her bir Blockchain'i kendisine bağlamanın çok da gerçekci olmayacağı düşüncesi ile iki katmanlı bir sistem öngörüyor. Bir tarafta altyapı olarak Cosmos var. Bir tarafta da daha üst seviyede Blockchain'lerin ihtiyaçlarını karşılayacak ikinci bir seviye - ki buna Cosmos Hub diyorlar. Cosmos Hub, bir nevi onların neler yapacaklarını göstermek amacıyla kurdukları ağ. Ama ne kadar çok fonksiyonu barındırırsanız, üzerinizdeki (ya da içinizdeki) Blockchain'leri o kadar kısıtlamak zorunda olacağınızı düşünerek, bunu opsiyonel yapıyorlar. 

Örneğin, duymuşsunuzdur Binance geliştiricilere kendi ekosisteminde kendi kullanıcılarına yönelik bir sistem kuruyor Binancechain adında. İşte bu sistem için altyapı olarak Cosmos'u kullanacaklar, yani en yalın halinde iletişimi sağlayacak en alttaki ağı. 



Bir önceki yazıda da belirttiğimiz gibi aslında Ethereum, her tür konuda fikri olan girişimlere bir altyapı sunarak aslında bir nevi network sağlıyor. Ancak 
