---
layout: post
title:  "Ethereum'un Gelecek Vizyonu ve Yol Haritası"
date:   2022-09-30 17:17:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Bu yazımızda Ethereum'un uzun vadeli vizyonu ve bu vizyona ulaşabilmek için kendine çizdiği yol haritasına bakıyoruz.

Ethereum yeni versiyona geçme süreci olan 'merge' konusunu gerek bu satırlarda gerekse blokzincir dünyasında detaylıca incelendi. Peki Ethereum geliştiricilerinin nihai planı ne ve buna ulaşabilmek için 'teknik olarak' neler planlıyorlar? Gelin sırayla göz atalım.

| ![fork](/assets/road-1579405_800.jpg)|
|:--:| 
| *Image by [NicStae](https://pixabay.com/users/nicstae-3062126/) from [Pixabay](https://pixabay.com/)*|

### Ethereum nasıl bir gelecek planlıyor?

Öncelikle Ethereum'un bir topluluk olduğunu ve gelecek ile ilgili kararların bu topluluk tarafından verileceğini belirtelim. Yine de bu konuda en çok kafa yoranlardan Ethereum'un kurucusu olan Vitalik Buterin'in geçtiğimiz yıl sonunda yazdığı [bir blog yazısı](https://vitalik.ca/general/2021/12/06/endgame.html) bize Ethereum'un vizyonu konusunda ipucu verebilir. Şöyle diyor Vitalik: 

***'İleride blok üretiminin merkezi olduğu bir zincir bizi bekliyor olacak. Ancak bu zincirde blokların onayı hayli merkeziyetsiz ve güvene ihtiyaç duymadan yapılacak ve özel (ihtisaslaşmış) sansür-karşıtı bir mekanizma (sihir) blok üretici sansürüne engel olacak'***

Hazmı zor bir cümle (Vitalik’in her blog yazısında olduğu gibi). Ethereum'un geleceğini anlamak için biraz açmakta fayda var bu cümleyi. 

Blokzincirlerin en büyük ölçeklenme sıkıntısı üretilen blok büyüklüğünün (yani kapasitesinin) sınırlı olması. Kapasite sınırlı tutuluyor zira  artırdığınız durumda blokzinciri çalıştıran makinelerin (düğümlerin) tüm işlemleri yapabilmesi için çok güçlü makineler gerekiyor. Ne kadar güç ihtiyacı o kadar basit makinenin devre dışı kalması demek. Bu da sistemin merkezileşmesi bir başka deyişle Ethereum geliştiricilerinin en büyük kabusu anlamına geliyor. 

İşte Ethereum sistemi olabildiğince makinenin sistem içinde olması yani sistemin olabildiğince merkeziyetsiz olabilmesi için, kendi sistemini bölmeye başlıyor. Öncelikle geçen yazımızda da bahsettiğimiz gibi, Ethereum ikinci seviye çözümler ile birlikte artık kendi onaylayıcıların üzerindeki yükü [^1] atmaya çalışıyor. Nasıl yapıyor bunu?

Öncelikle, işlem yapma (ingilizcesi 'execution') rolünü, ağırlıklı olarak ikinci seviye çözümlere paslıyor. Böylece, ağır işlemler ikinci seviye çözümler aracılığıyla gerçekleştiriliyor. İkinci seviye çözümler yaptıkları işlemlerin sonuçlarını ana Ethereum ağına yazıyorlar. Böylece ana Ethereum ağı ikinci seviye üzerindeki her işlemi tekrar yapmak zorunda kalmıyor.

İkinci olarak, ileride talebin çok fazla olması durumunda blok oluşturmanın yarattığı ağır yükü kaldırabilmek için blok üretimini güçlü ama sayıca az (dolayısıyla daha merkezi) bir grup üreticiye bırakıyorlar.  İşte merkezileşme tehlikesi burada beliriyor. Bu tehlikeyi ortadan kaldırabilmek için, işlemlerin doğru olduğunu kontrol işlemini olabildiğince merkeziyetsizleştirme yoluna gidiyorlar.

Bu vizyonu gerçekleştirebilmek için paralel olarak devam eden beş teknik geliştirme var. Bunları İngilizce tabirleriyle The Merge ('birleşme'), The Surge ('sıçrama'), The Verge ('sınırlama'), The Purge ('arındırma') ve The Splurge ('hava atma') deniyor. Gelin şimdi de bu kafiyeli adlara sahip geliştirmelere bakalım kısaca (bu terimlerin hepsini tek bir diagramda görmek isterseniz Vitalik'in Aralık 2021'de attığı [şu tweete](https://twitter.com/vitalikbuterin/status/1466411377107558402) bakıp gözlerinizi kanatabilirsiniz :) ).  

#### The Merge (Birleşme): 

Bu hafta içinde olan meşhur birleşme. Birleşme denmesinin nedeni şu: Az önce bahsettiğimiz, işlemleri ikinci seviyeye yüklemenin bir parçası olarak, Ethereum kendisini iki katmana ayırıyor. İşlemleri gerçekleştiren 'execution' katmanı ve işlemleri onaylayan ve zincirin uzlaşı içinde ilerlemesini sağlayan 'consensus' katmanı. Execution katmanı bildiğimiz şu zamana kadar kullandığımız Ethereum aslında. Consensus katmanı ise PoS ile birlikte 2020 yılında hayata geçen 'yeni' Ethereum diğer adıyla eth2. Merge ile birlikte Execution katmanında bulunan PoW yok ediliyor ve bu katman eth2 altında 'birleştiriliyor'. 

#### The Surge (Sıçrama):

The Surge, tamamen ikinci seviye çözümlerin ölçeklenebilmesi üzerine kurulu. 

Ethereum'un önümüzdeki dönemde artacak işlem talebini ikinci seviye çözümler karşılayacak.  Bu çözümler Ethereum ile sıkı-fıkı çalıştıkları için Ethereum'a ile aralarında çift yönlü bir bilgi akışı söz konusu.[^2] Onlarca çözümün bilgi akışının olacağını düşünürsek, ileride Ethereum üzerindeki düğümler üzerindeki yük yine artmaya başlayacak. İşte böyle bir durumda yapılmakta olan birkaç geliştirme onaylayıcıları rahatlatacak. 

Öncelikle orijinal Ethereum planında olan 'sharding' (türkçeye parçalara bölme olarak çevirebiliriz) sayesinde onaylayıcılar tüm datayı değil belli bir parçasını onaylayacaklar.  İlk aşamada blok içindeki bir parçanın tamamını indirip kontrol edecekler (buna PDS proto-dank-sharding deniyor). Aslında bu bir ara çözüm ve arada bir duyabileceğiniz EIP-4844 geliştirmesi ile gelecek. 

Başlangıçta düğümler bunu yapabilirler ancak ileride talebin çok artması durumunda tüm veriyi indirmek düğümlere yine yük getirecek. Bu nedenle daha sonraki bir dönemde sunulacak iki yeni geliştirme sayesinde (DAS ve KZG[^3]) basit onaylayıcılar bile önlerine gelen blok parçalarının doğru ve eksiksiz bir biçimde oluşturulduğunu kontrol edebilecekler. Bunu yaparken tüm parçayı yüklemek zorunda kalmayıp, daha basit şekilde matematiksel olarak örnekleme yapacaklar. Bu sayede, onaylayıcıların işlem onaylama kapasitesi çok ciddi bir şekilde artacak.

Bir diğer önemli değişiklik, ikinci seviye çözümlerin Ethereum üzerinde çok fazla kapasite (gas) kullanması. İşte EIP-4844 ile gelen bir başka yenilik, bu fonksiyonların artık çok daha fazla verinin taşınabildiği ama kapasiteden o kadar yemeyen 'data blob' ('su baloncuğu' diye çevirsek yanlış olmaz sanırım) formatının gelmesi. Bu formatın özelliği hem ucuz olması hem de bir ay sonra sistemden silinmesi sayesinde geçmiş veriyi şişirmemesi. "Geçmiş veriyi kaybetmiyor muyuz bu durumda?" Çok değil, zira burada saklanan en kapsamlı veri, ikinci seviyede işlem bilgisinin doğruluk kanıtları. İşlem gerçekleşip aradan bir ay geçtikten sonra geriye dönüp bakmanın bir anlamı yok.[^4]

Bunların dışında kısa vadede yapılacak bir başka geliştirme ise, ikinci seviye çözümlerin Ethereum üzerindeki kapasite kkullanımını azaltacak.[^5] EIP-4488 olarak adlandırılan bu geliştirme çok basit ve hızlıca kurulacak ve kısa vadedeki ihtiyaçları giderecek. 

#### The Verge (Sınırlandırma)
The Verge, temel olarak işlemleri onaylamak için gerekli bilgileri sınırlandırarak onaylayıcıların üstlerindeki yükü yükü azaltmaya çalışıyor.  

Ethereum sistemi üzerinde bir işlem gerçekleştiği noktada, onaylayıcılar işlem öncesi durumu alıp, yapılan işlemi hesaplayıp, işlem sonrası durumu buluyor ve doğruluğunu onaylıyorlar. Bunun için ilk olarak işlem öncesi durumun (state) bilinmesi (ve elde olması) gerekiyor. Sorun şu ki, hesaplar ve işlemler arttıkça bu mevcut durumların olduğu liste büyümeye ve Ethereum üzerinde darboğaz yaratmaya başlıyor. 

Bu sıkıntının önüne geçilebilmesi için, onaylayıcılar blok başlamadan önce tüm Ethereum sisteminin mevcut durum tablosunu önlerine almak yerine, sadece o blokta gerçekleşen işlemlere ait mevcut durumlarını dikkate alacak. Bu sayede onaylayıcıların önündeki en büyük darboğazlardan biri yok edilecek [^6] Tüm sistemin mevcut durumu inşaatçılar tarafından tutulacak ama onlar zaten işin hamaliyesini yaptıkları için farketmeyecek. Burada önemli olan onaylayıcıların üzerindeki yükü azaltarak merkeziyetsizlikten feragat etmemek.

#### The Purge (Arındırma)
The Purge temel olarak sistem üzerindeki geçmiş datanın temizlenmesi ve onaylayıcıların ihtiyacı olan hard-disk kapasitesini azaltmayı hedefliyor. 

Onaylayıcılar, Ethereum blokzinciri üzerindeki işlemleri onaylayabilmek için işlem arayüzü programları (client) kullanıyorlar. Bu arayüzlerin bloklara ait her tür datanın tarihçesini tutması gerekiyor. İşlemlerin ve sistemin doğruluğunu kontrol etmek isteyen bir kullanıcı, bütün bu datayı indirmek zorunda (ki bu yüzlerce GB büyüklüğünde). Yeni gelen bir geliştirme (EIP-4444) ile birlikte bir yıldan daha eski datanın tutulmasına gerek kalmayacak. "Nasıl yani? Tüm geçmiş silinecek mi?" diye soracak olursanız, cevap tabii ki hayır. Bu data, büyük data merkezleri tarafından (örneğin Etherscan) tutulmaya devam edecek. 

Bunun yanında bir önceki The Verge kısmında gördüğümüz, inşaatçılar tarafından tutulan 'tüm sisteme ait mevcut durumlar' içinde bir ya da iki yıldan fazla süredir aktif olmayanlar silinecek, ki inşaatçılar rahat etsin (Yine bu verinin Etherscan benzeri yerlerde tutulmasına devam tabii)

#### The Splurge (Hava atma)
Son olarak ise merkeziyetsizlik için oldukça önemli yenilikler getiren The Splurge var. Bu sürecin sonu artık pastayı yaptıktan sonra üzerine konan çilek adeta. 

Ethereum eski sisteminde madenciler blokları oluşturur ve diğer madencilere onaya sunarlardı, yani her iki işi de madenciler yapardı. Eth2 ile birlikte madencilerin yerini onaylayıcılar alacak ve iki işi yapmaya devam edecekler. Ancak dediğimiz gibi ileride kapasitenin çok artması gerektiği durumlarda blok oluşturmak için güçlü makineler gerekecek. İşte bu nedenle, Ethereum bir güçler ayrılığına gidecek. Özel amaçlı inşaatçı makineler blokları oluşturacak, onaylayıcı olan bir başka grup ise bunları onaylayacak. [^7] (Bu ayrıma PBS proposer-builder separation deniyor). 

Burada önemli bir ayrıntı da şu. Blok oluşturanlar bazı işlemleri bloklarına almayarak sansüre kalkışabilirler.  Bunu önlemek için onaylayıcılar sansüre-dayanıklı listeler (censorship resistance list kısaca 'crList') oluşturarak, bloklara girmeye uygun tüm işlemlerin bir listesinin yapacaklar. İnşaatçılar blokları oluştururken bu listeleri kullanmak zorunda kalacaklar. Yani, inşaatçılar emek ve güç yoğun ama işlemler üzerinde fazla bir söz hakkı olmayan oyuncular olacaklar. 


### Sonuç
Ethereum, geçen hafta yaşadığımız merge sonrası geçmişte yaşadığı darboğazları yaşamamak ve ileride her tür uygulamanın ihtiyacı olan altyapı hizmetine yetebilecek kapasitesi getirebilmek için nasıl bir yol haritası izlemesi gerektiğini belirlemiş durumda. Bunlar, üzerinde kurulu ikinci seviye çözümlerin ölçeklenmesini sağlayacak The Surge; sistemi yürüten onaylayıcıların yükünü hafifleten The Verge; sistem üzerinde ayakbağı oluşturan geçmişi temizleyecek olan The Purge ve son olarak merkeziyetsizlik konusunda iyileştirmeler getiren The Splurge olarak karşımıza çıkıyor. 

Oldukça karmaşık sayılabilecek beş ayrı koldan (Merge neredeyse bitmiş olarak düşünülebilir) yürüyen bu süreçte öncelik 'The Surge' kısmı ile Ethereum'un ölçeklendirmek. Burada 'sharding' bir numaralı öncelik. Sonrasında 'The Splurge' içindeki PBS yani blok üretici ile onaylayıcılarının (ve teklif edenlerin) ayrılması geliyor.   Bu ikisi çok önemli, zira en acil problemler olan ölçeklenme ve sansüre karşı dayanıklılık için bu iki geliştirme önemli. Ethereum geliştiricileri bu iki konuya öncelik verebilmek için diğer konuları (örneğin The Verge) geri plana atmaya razılar. 

Bütün bu işlemlerin özünde, Ethereum'u ileride sansüre karşı koruyacak olan merkeziyetsizlik prensibinden vazgeçmeden, yüksek hacimli işlem sayılarını başarıyla işlemek var. Plan karmaşık görünse de aslında Ethereum geliştiricilerinin kafasında oldukça net. Gerçekleşmesi ise uzunca bir süre alacak. Önümüzdeki dönemde aşama aşama hayata geçmeye başladığını hep birlikte göreceğimizi umuyoruz. 

---

*Kaynaklar:*

- *[The End Game](https://vitalik.ca/general/2021/12/06/endgame.html) - Vitalik Buterin*
- *[The Hitchhiker's Guide to Ethereum](https://members.delphidigital.io/reports/the-hitchhikers-guide-to-ethereum/) - Delphi Digital*
- *[The Complete Guide to Rollups](https://members.delphidigital.io/reports/the-complete-guide-to-rollups) - Delphi Digital*


[^1]: "Nedir bu yük?" diye soracak olursanız; tam donanımlı düğümlerin yaptığı iki temel iş var. Birincisi, blok içindeki her bir işlemin doğru olup olmadığını anlamak. Bunun için blok öncesi durumu alıyorlar (Ayşe'nin 10 ETH'si, Ali'nin 5 ETH'si var), istenen işlemi yapıyorlar (Ayşe, Ali'ye 1 ETH gönderdi), blok sonundaki durumu kontrol ediyorlar (Ayşe'nin 9 ETH'si, Ali'nin 6 ETH'si var). İkincisi ise, bu bloğa eklenen blokta bu işlemin ve son durumun doğru bir şekilde işlendiğini kontrol edip onaylıyorlar.

[^2]: Nedir bu bilgi akışı? Temel birkaç tane var. Birincisi Roll-up üzerinde yapılan işlemlere ait bilginin ve bu işlem sonucu değişen hesap bakiyelerin sıkıştırılmış bir halinin ana ağa bildirilmesi. İkincisi verilen sıkıştırılmış bilgilerin doğru olduğunun teminatı kanıtların sunulması. Roll-up tarafından gelen bilginin doğru olup olmadığının kontrolü onaylayıcıların işi. Bu da onaylayıcılar üzerinde büyük bir yük demek.

[^3]: Bu iki çözüm, oluşturulan blokların doğru oluşturulduğunu bulmaya yarayan DAS (data-availability-sampling) ve datanın tam olduğunu anlamaya yarayan KZG committments. KZG sistemi geçici bir çözüm, zira kuantum bilgisayarlar tarafından kırılabilirler ve kurucularına güvenmek zorundasınız. Uzun vadede KZG yerine ZK-proof denen sıfır-bilgi-kanıtı gerektiren STARK'ların kullanılması planlanabilir. Bunun için ZK-proof teknolojisinin daha geliştirilerek sisteme getirdiği hesaplama yükünün hafifletilmesi gerekiyor.

[^4]: İkinci seviye çözümler içinde Optimistic Rollup'lar, yapılan işlemlerin doğruluğuna itiraz için bir haftalık bir süre veriyor. O sürede itiraz olmaz ise işlem zaten onaylanıyor, dolayısıyla bir aylık süre fazlasıyla yeterli. Zk-roll up çözümlerde zaten böyle bir süreye gerek yok, işlemler anında gerçekleşiyor.

[^5]: EIP-4488 ile 2. Seviye çözümün en temel ihtiyacı olan calldata fonksiyonunun Ethereum üzerindeki gaz ihtiyacı 16 gas/byte'dan 3 gas/byte'a iniyor.

[^6]: Burada inşaatçı olan ağır işçi oyuncular yine tüm mevcut durumu almak zorundalar ama onlar zaten güçlü makinelere sahip oldukları için bu büyük bir problem yaratmayacak. Burada önemli olan merkeziyetsiz onaylayıcıların üzerindeki yükü olabildiğince azaltmak. Burada bir diğer nokta da, içeriye alınan işlemlere ait mevcut durumların Verkle tree denen daha verimli bir yöntem ile bloğa aktarılması.

[^7]: Burada, blokları oluşturan inşaatçılar, içeri bir an önce girmek isteyen kullanıcılardan 'bahşiş' alabilecekler. Bunun dışında, şu anda da olan ve MEV (miner-extractable-value) denen işlemlerin öncelik sırasında oluşan arbitraj fırsatları da bu inşaatçılar tarafından alınacak. Bunun karşılığında bu inşaatçılar, oluşturdukları bloklar kabul edilsin diye kazandıkları paranın bir kısmını onaylayıcılara verecekler. Düzgün çalışan bir piyasada, kullanıcıların verdiği ücretlerin ve MEV'lerin büyük kısmının inşaatçılar tarafından blokları kabul edilmesini sağlamak için onaylayıcılara verilmesi beklenir. Bu da, onaylayıcıların yani ETH stake edenlerin kazandıkları paranın (faiz gelirinin üzerine) artması anlamına gelir.


*Not 1: Burada özellikle madenciler konusunda yer alan ve işlemleri önerenler ile onaylayanların ayrılmasına yönelik halihazırda tartışılan [bir öneri](https://ethresear.ch/t/proposer-block-builder-separation-friendly-fee-market-designs/9725) de bulunmakta*

*Not 2: Bu yazı ilk olarak 30 Eylül 2022'de [BTCHaber.com](https://www.btchaber.com/)'da [yayınlandı](https://www.btchaber.com/ethereumun-vizyonu-ve-yol-haritasi/)*

*Not 3: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

