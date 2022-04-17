---
layout: post
title:  "Tokenler ve farkları"
date:   2022-04-17 08:47:56 +0300
categories: Genel
tags: Yazılar, Web3, DeFi, DeFi'ye Giriş
---


Bu yazımızda NFT yani non-fungible-token terimini içindeki token kavramını irdeleyeceğiz. 

NFT dünyasını incelediğimiz bu yazı dizimizin ilkinde NFT  dünyasına ilk adımımızı atmış ve 'dijital dünyada sahiplik nasıl oluyor?' sorusuna yanıt aramıştık. Gelin şimdi de non-fungible-token kavramını farklı standartlar üzerinden değerlendirelim.

### Token standartları
Token, Türkçeye belirteç olarak çevirebileceğimiz herhangi bir dijital varlığa işaret eden onu gösteren jetonlar olarak düşünülebilir. 


|![tokens](/assets/coins-7080656_800.jpg)|
|:--:| 
| *Image by [ Alex Volodsky](https://pixabay.com/users/alex-v-1376556/) from [Pixabay](https://pixabay.com/)*|

Bu tokenlerin, herkes tarafından anlaşılabilmesi ve kullanılabilmesi için belli standartlar geliştirilmiş. Bunlardan en önemli olan üç tanesine değinmekte ve farklarını anlamakta fayda var. 

#### Değiştirilebilir (fungible) tokenler 
İlk olarak hayatımıza giren token Bitcoin ile ortaya çıkan BTC oldu. Bu token, paranın temel özelliklerinden biri olan birbiriyle değiştirilebilir (fungible) olma özelliği taşıyordu. Neden önemli bu?

Değiştirilebilirlik, paranın alışverişlerde değişim aracı olarak kullanılabilmesi için oldukça kritik. Bu ticaretin güvene dayalı esaslarından bir tanesi. Sattığınız bir ürün için aldığınız parayı başka bir ürün için kullanabilmelisiniz ve bu paranın değeri diğer aynı cins paralar ile aynı olmalı. Bir paranın diğeri ile aynı olmaması durumu ticareti sekteye uğratabilir. Eski zamanlarda, krallar dolaşımdaki paraları altın ya da gümüşten yaparken, zamanla masrafların artması nedeniyle piyasaya içine başka madenler karıştırılmış paralar katmaya başladılar, ki bu pek çok krallığı krize ve hatta yıkılmaya doğru götüren nedenler arasında sayılır. 

Günümüzde kullandığımız itibari paralar birbiri ile değiştirilebilir özelliğe sahipler. Kağıt paralar, seri numaralı olması nedeniyle birbirinin aynı olmasalar da, değer olarak (sahte olmadıkları sürece) birini ya da öbürünü almanız sizin için çok da büyük bir fark yaratmaz. 

İşte kripto dünyasındaki ilk çıkan tokenler de birbirileri ile değiştirilebilir şekilde ortaya çıktılar. Bitcoin sonrası çıkan Ethereum'un parası ETH de benzer özellikler ile oluşturuldu. Ethereum dünyası, üzerine kurulan pek çok farklı platforma ev sahipliği yapıyor. İşte bu platformlar kendi sistemlerinin paraları çıkarmak istedikleri durumda, bu paraların tüm Ethereum dünyası içinde dolaşımda olabilmesi için belli standartlara uygun olmak zorundalar. Geliştiriciler çıkaracakları tokenin para özellikleri taşımasını istiyorlarsa, [ERC-20](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/) denilen standardı uygulamak zorundalar. 

2015 yılında sunulan değiştirilemez tokenler, sonrasında yaşanan ICO (initial coin offering - halka arzlar çılgınlığının da öncüsü oldu. Projeler, halktan para toplamak için ERC-20 standardında token çıkardılar ve bunları Ethereum sisteminde ETH karşılığında halka sattılar. Bu tokenleri almak isteyen kitle ilk olarak ETH tokeni almak zorunda idi. Bu da o dönemde ETH'ye olan talebi ciddi şekilde artırdı. ETH fiyatları bir anda 1400 ABD Doları seviyesine geldi. 

 | ![ETH_fiyat_grafigi](/assets/ETH-2017-20_800.jpg)|
|:--:| 
| *Mayıs 2017-Mart 2020 arası ETH'nin fiyat grafiği. Kaynak: [Coingecko](https://www.coingecko.com/en/coins/ethereum)*|

Sonrasında ise rüzgar tersine döndü. 2018 yılının Şubat ayından sonra bu sefer ters döngüye girildi. ICO rüzgarı dindi ve yeni çıkan projelere talep kalmadı. Bu da ETH talebini azalttı. Öte yandan, ICO'larda ETH toplayan projeler masraflarını karşılamak için hazinelerinde duran ETH'leri satmaya başladılar. Bu da iki yıl süren bir süreçte ETH'nin 100 ABD Dolarına kadar gerilemesine neden oldu.

#### Tekil - değiştirilemez (non-fungible) tokenler

Blokzincir dünyasında temellerin atılması sonrası ortaya çıkan uygulamalar zamanla değişmeye ve gelişmeye başladı. Bu değişim zamanla yeni ihtiyaçlar doğurdu. Örneğin, sanat eserleri ya da koleksiyonlar, sahiplik belgeleri, sigorta poliçeleri gibi dijital ortamdaki varlıklar yukarıda bahsettiğimiz 'değiştirilebilir' token elbisesine sığmamaya ve aynı fiziksel dünyada olduğu gibi 'tek ve eşsiz' şekilde yer almayı istemeye başladılar. 

Bunun üzerine Ethereum dünyası 2018 yılında [ERC-721](https://eips.ethereum.org/EIPS/eip-721) standardını uygulamaya koydu. NFT olarak da adlandırılan  bu token standardı da aslında bakarsanız kendi içinde bir akıllı kontrat. Herhangi bir dijital varlığa işaret ederken, o varlığa ait bir 'eşsiz tanımlayıcı' (ingilizcesi unique ID) belirliyor. Örneğin herhangi bir koleksiyona ait 10,000 parça var ise, bu parçaların her biri 1'den 10,000'e kadar rakam ile tanımlanıyor ve her bir parça diğerinden farklı olarak işlem görüyor yani eşsiz oluyor. 

### Hibrit tokenler 
Yazılım dünyasının en güzel yanlarından biri ihtiyaçlara göre yazılımların hızlı bir şekilde geliştirilebilmesi. Yukarıda bahsettiğimiz değiştirilebilir (fungible) tokenler ve eşsiz (non-fungible) tokenler sonrası, kimi projeler çıkardıkları tokenlerin bazı durumlarda değiştirilebilir bazı durumlarda eşsiz olmasını istediler. 'İyi de niye ihtiyaç duyuldu buna?' diye merak edenlere biraz teknik yanıtı da hemen verelim: 

Yukarıda bahsettiğimiz ERC-20 ve ERC-721 esasında birer akıllı kontrat. ERC-20 ile token çıkarmak için bir akıllı kontrat geliştirmeli ve bunu Ethereum zincirine yazmalısınız. ERC-721 ile örneğin 10,000 parçadan oluşan bir koleksiyon yarattığınızda bir temel kontrat ve 10,000 eşsiz tanımlayıcı yaratıp blokzincire yazıyorsunuz. 

Ethereum blokzinciri kısıtlı bir kapasiteye sahip. Her bir kontratı zincire yazmak oldukça maliyetli. Hele bir de zincire talep yüksek olduğu zamanlarda bu maliyet iyice yukarı çıkabiliyor. 

Kimi oyunlarda ise oyunun doğası gereği arada bir çoklu sayıda değiştirilebilir para çıkarmanız gerekiyor Böyle olunca, her seferinde ERC-20 token kontratını yazmak maliyetleri artırabiliyor. Bunun yerine her yeni çıkaracağınız parayı, ERC-721 standardındaki bir non-fungible token tanımlayıcısı ile çıkarmak ve sonra bunları çoklu hale getirmek bir çözüm olabilir - ancak ERC-721 ile bu yapılamaz. İşte bu nedenle çıkarılan ERC-1155 standardı, hem ERC-721 tokeni ile çıkan bir NFT koleksiyonu gibi eşsiz tanımlayıcılı hem de bu eşsiz tanımlanan tokenlerin her birinin sonrasında ERC-20 token gibi kullanılmasını sağlayan hibrit bir yapı olarak kurgulanmış. 


## Sonuç
Ethereum üzerindeki farklı token standartlarına bakmak bize NFT yani 'eşsiz belirteçlerin'  özelliklerini anlamak açısından fayda sağlayabilir. Bir sonraki yazımızda, NFT'ler herhangi bir dijital varlığa nasıl 'değer' katıyorlar onu inceleyeceğiz. 

---

*Not 1: Bu yazı ilk olarak 17 Nisan 2022'de [BlockchainIST Center](https://medium.com/blockchainist-center)'da [yayınlandı]()*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.* 

