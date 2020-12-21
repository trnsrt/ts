Bu yazımızda, son kullanıcı olarak direkt olarak kullanmadığımız ancak Merkeziyetsiz Finans için kritik konularından biri olan Oracle konusuna bakıp, nedir ve neye yarar anlamaya çalışalım: 

### Nedir Oracle?
Oracle'in tam Türkçesi karışık. Kahin ya da uzman olarak çevrilebilir. Peki ne işe yarar?

Efendim, Bitcoin ile başlayan merkeziyetsiz dünyanın, Ethereum ile devam eden bir sonraki adımında, karmaşık işlemleri gerçekleştirebilmek için 'akıllı kontrat' denen bir yenilik kullanılıyor. Akıllı kontrat dediğimiz, aslında bir kod. Güzelliği ne? Tamamen tarafsız bir şekilde kendisinden ne istenirse onu istendiği zaman yapıyor. Böylece, kontrata taraf olanlar, eğer belirlenen koşullar gerçekleşirse, kontratın yerine geleceğinden emin oluyorlar. 

Çok güzel ancak ufak bir sorun var. Kontratın, kendisini harekete geçirecek bu önceden belirlenmiş koşulların oluştuğunu bilmesi gerek. Bu koşulların oluşup oluşmadığını belirleyen bilgilerin büyük çoğunluğu ise, blokzincirin içinde değil, dışından geliyor. Ya biri bu bilgiyi kontrata verecek ya da kontrat bu bilgiyi bir kaynaktan alacak. 

| ![labrador](/assets/labrador-5741850_640.jpg)|
|:--:| 
| *Biri bilgiyi kapıp gelsin bunun gibi :) Kaynak: Image by [Jana Schmidt](https://pixabay.com/users/jawika-19109282/) from [Pixabay](https://pixabay.com/)*|


Örneğin, 2020 yılı ABD seçimleri sonucunda kimin seçileceği ile ilgili yapılan tahminlerde, kaynak olarak [Amerikan hükümetinin resmi web sitesinde yeni başkan olarak kimin yazıldığı](https://www.usa.gov/presidents#item-37462) kullanılıyor. İşte akıllı kontratın sonucu bu siteden alarak çalışması ve doğru tahmin edenleri belirlemesi gerekiyor. Peki akıllı kontrat bunu nasıl alacak?

Bu, en basit ve bariz örnek. İki yıl önce yayınlanan [tahmin piyasaları için blockchain yazımızda](/genel/2018/07/13/gelecegi-tahmin-için-blockchain.html), bu kaynakların blokzincir dünyası dışında, tarafsız olduğu kabul edilen bilgi sağlayıcılardan (örneğin WSJ gazetesi) alınıp blokzincire otomatik ya da uzmanlar tarafından manuel olarak girilmesinden bahsetmiştik. 

ABD seçimi tek bir olaya bağlı tahminlerde işe yarayabilecek olan manuel bilgi aktarımı, merkeziyetsiz dünyada çok da işe yaramayacak gibi görünüyor. Gelin bakalım ne gerekiyor DeFi dünyasına: 

### Merkeziyetsiz dünya için neden önemli?

Merkeziyetsiz finans dünyasının oyuncusu olan değişik platformlar, aynı bir legonun parçaları gibi birbirine iç içe geçmiş bir şekilde çalışıyorlar. Yukarıdaki basit örneğin ötesinde, bu lego parçalarının birbirleriyle uyumlu şekilde hareket edebilmeleri için onlarca hatta yüzlerce bilginin akıllı kontratlara akması gerekiyor. Bunu sağlayabilmek için kaynaklardan alınan bilginin hem doğru ve tarafsız hem de çok hızlı bir şekilde toplanması gerekiyor. 

Bir örnek verelim: Sentetik türev piyasaları, basitçe herhangi bir ürünün (örneğin altın ya da petrol) aslına sahip olmadan, o ürünün kazancına (ya da kaybına) ortak olma ve alım-satımını yapmaya imkan veren pazarlar idi. Merkeziyetsiz sentetik türev borsasında ürünün kendisi değil taklidi alındığı ya da satıldığı için, dış dünyadaki orijinal fiyatların buraya aktarılması gerek, hem de çok sık bir şekilde. 

İşte oracle dediğimiz uzmanlar, Akıllı Kontratların ihtiyacı olan bu bilgiyi onlara sağlayan yapılar.  Ve her ne kadar kullanıcı olarak direkt temasa geçmesek bile bizim için de çok kritik bir altyapı hizmetini yerine getiriyorlar. 

### Merkezi kaynak mı istersiniz yoksa merkeziyetsiz mi?

Yukarıda verdiğimiz örnekte merkeziyetsiz bir oracle örneği verdik ancak hemen belirtmek lazım. Bu alanda en büyüklerden bir tanesi ABD'nin en büyük borsası olan Coinbase tarafından yaratılan oracle. Coinbase Price Oracle sayesinde, piyasada işlem gören tokenların fiyat bilgilerini sürekli bir biçimde elde etmek mümkün. 

Merkezi yapılar, DeFi dünyasında genelde hoş karşılanmazlar. Bunun temel nedeni, hep bahsettiğimiz dijital dünyada merkezi yapıların güvenlik açığı olarak adlandırılması. Zira, tek kaynak olmaları nedeniyle bu yapılara yapılacak saldırılar sonrası fiyatların manipüle edilmesine yol açabilir. Bu da, o fiyatlara kullanarak hizmet veren platformları zor durumda bırakabilir. 

### Merkeziyetsiz platformlar nasıl yapıyorlar bu işi?

Bilgiyi zincir dışından içine taşımak o kadar da basit bir olay değil. Fazla tekniğe girmeden anlatmaya çalışalım (son kullanıcı olarak ilginizi çekmiyor ise bir sonraki bölüme atlayabilirsiniz): 

Biliyorsunuz, Bitcoin blokzincirinin güvenliğini madenciler sağlıyor. Bu madenciler, aslına bakarsanız Bitcoin sisteminin fiziki dünyaya bağlı olduğu (dayandığı) tek kısım. Zira, sistemin korunabilmesi için fiziki olarak elektrik harcanması gerekiyor. Bunu yapan madencilerin her biri aslında bir makine ve bu dünyanın deyişi ile blokzincir ağının bir ilmeği... 

İşte, oracle sistemlerinde de benzer şekilde dış dünya ile ilişkiyi bu ağ üyesi makineler kuruyorlar. Bilgi ihtiyacı olan DeFi yapıları, bir Akıllı Kontrat aracılığıyla hangi tür teknik bilgi istediklerini oracle hizmeti veren ağın içine koyuyorlar. Teknik derken kasıt, hangi bilgi kaynağının kullanılacağından, ne sıklıkla ve hangi hizmet süreleri (örneğin %99.99)  çalışma gerekliliği gibi istekler. 

Ağ içindeki üyeler böyle talepleri içeren bir akıllı kontrat gördüklerinde bu hizmeti ne kadar bir ücret karşılığı yerine getirebileceklerini kontrata bildiriyorlar. Bu ücret genel olarak o ağın kullandığı kripto para cinsinden belirleniyor. Anlaşma sağlanıp sistem çalışmaya başladığında, bilgi sağlayıcı üyeler dış dünyadaki kaynaklardan aldıkları bilgileri akıllı kontrata aktarıyor, diğer üyelerde ağ üzerinden bu bilginin doğruluğunu teyid ediyor. Sonrasında akıllı kontrat, farklı üyelerden gelen teyid edilmiş bilgilerin ağırlıklı ortalamasını alıp bir değer buluyor ve talep sahibine bildiriyor. Böylece, bir kişiye bağlı kalmadan, istendiği kadar farklı kaynak kullanılarak olabildiğince tarafsız bilgi sağlanmış oluyor. 

### Son zamanlarda önemi arttı mı?

DeFi dünyasının patlamasıyla birlikte doğru ve hızlı veriye olan ihtiyaç da arttı ve bu alandaki servis sağlayıcılar ciddi talep görmeye başladı... Öyle ki, bu alandaki en büyük iki oyuncu olan Chainlink ve Nest, Eylül 2020'de Ethereum ağın en çok meşgul eden uygulamalar arasına girip bir ayda toplam 2.5 milyon ABD Doları işlem ücreti ödediler. 

Bu alandaki belli başlı oyuncular Chainlink, Band Protocol, Test Protocol, DIA, DOS Network, Zap ve Tellor olarak sıralanıyor. Ancak hemen belirtelim Chainlink bu piyasanın neredeyse tek hakimi.. Bu saydığımız oyuncuların piyasa değerleri şu şekilde: 

| ![Oracle_servis_saglayicilar](/assets/Oracle_Servis_Saglayicilar_v2.png)|
|:--:| 
| *Kaynak: [CoinGecko](https://www.coingecko.com/en) 21 Aralık 2020*|

Chainlink'in bu ağırlığı neye dayanıyor, ne kadarı anlaşılabilir, onu bir sonraki yazımıza bırakalım artık.. 

### Sıkıntıları neler?
Merkeziyetsiz Finans dünyasında oracle sistemlerinin en büyük sıkıntısı gecikmeler. Yukarıda bilgi aktarımda bahsetmiştik. Bilgi toplanıyor, blokzincir ağına aktarılıyor, orada teyit ediliyor ve talep edene gönderiliyor. Dijital dünyada aslında saniyeler içinde yapılabilecek bir işlem. Bilginin teyidi sonrası blokzincire yazılıyor olması nedeniyle, blok oluşturma hızları darboğaz yaratıyor. Örneğin Ethereum sisteminde her bir blok 10-20 saniye arasında oluşuyor. Bu da bilginin ulaşımında gecikmeler olması demek. 

Bunun yanında, bilgiyi tek bir kaynaktan almak da sıkıntı yaratabiliyor. Örneğin, kimi platformların akıllı kontratları, ihtiyaç duydukları token fiyat bilgisini tek bir borsadan çekebiliyorlar. Bazı akıllılar ise özellikle likiditenin azaldığı durumlarda bu merkeziyetsiz borsada o tokenların fiyatlarını manipüle edip, bu fiyatları kullanan platformlarda anlık işlemler ile ciddi kazançlar elde edebiliyorlar. Bunu önlemenin yolu, akıllı kontratları iyi dizayn etmek ve bilginin birkaç farklı yerden gelmesini sağlayarak manipülasyonu zorlaştırmak. 

### Sonuç
Hep bahsettiğimiz emekleme aşamasındaki Merkeziyetsiz Finans dünyasının ayağa kalkıp yürümesi için gerekli yapı taşlarından biri de oracle servis sağlayıcılar. Şu an için tek bir oyuncunun ağırlığında olması ve merkezi servis sağlayıcıların potansiyel risk barındırması nedeniyle, bu alan aynı hizmet verdiği DeFi platformları gibi teknik olarak farklı ürünlerin çıkmasına ve hacim olarak büyümeye gebe... 

Bir sonraki yazımızda Chainlink örneğini daha yakından inceleyerek, bu farklı ürünler neler olabilir ve bu alan daha nerelere ulaşabilir ona bakacağız.. 


Not 1: Merkeziyetsiz dünyada [türev piyasalarının nasıl olabileceğini anlattığımız bir yazımızda](/genel/2020/08/20/defi-turev-piyasalari-nasil-oluyor.html), bu piyasaların en büyüğü olan [Synthetix'in nasıl çalıştığına da bir diğer yazımızda](/genel/2020/08/28/Defi-turev-piyasasi-synthetix-nasil-calisiyor.html) anlatmıştık.  

