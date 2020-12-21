Oracles

Bugün son kullanıcı olarak direkt olarak kullanmadığımız, ancak Merkeziyetsiz Finans'ın en kritik konularından biri olan Oracle konusuna bakıp, nedir ve neye yarar anlamaya çalışalım: 

### Nedir Oracle?
Oracle'in tam Türkçesi karışık. Kahin ya da uzman olarak çevrilebilir. Peki ne işe yarar?

Efendim, Bitcoin ile başlayan merkeziyetsiz dünyanın, Ethereum ile devam eden bir sonraki adımında, karmaşık işlemleri gerçekleştirebilmek için Akıllı Kontrat denen bir yenilik kullanılıyor. Akıllı Kontrat dediğimiz, aslında bir kod. Güzelliği ne? Tamamen tarafsız bir şekilde kendisinden ne istenirse onu istendiği zaman yapıyor. Böylece, kontrata taraf olanlar, eğer belirlenen koşullar gerçekleşirse, kontratın yerine geleceğinden emin oluyorlar. 

Çok güzel ancak ufak bir sorun var. Kontratın, kendisini harekete geçirecek bu önceden belirlenmiş koşulların oluştuğunu bilmesi gerek. Bu koşulların oluşup oluşmadığını belirleyen bilgilerin büyük çoğunluğu ise, blokzincirin içinde değil, dışından geliyor. Ya biri bu bilgiyi kontrata verecek ya da kontrat bu bilgiyi bir kaynaktan alacak. 

| ![labrador](/assets/labrador-5741850_640.jpg)|
|:--:| 
| *Bilgiyi kapıp gelsin bunlar gibi :) Kaynak: Image by [Jana Schmidt](https://pixabay.com/users/jawika-19109282/) from [Pixabay](https://pixabay.com/)*|


Örneğin, 2020 yılı ABD seçimleri sonucunda kimin seçileceği ile ilgili yapılan tahminlerde, kaynak olarak [Amerikan hükümetinin resmi web sitesinde yeni başkan olarak kimin yazıldığı](https://www.usa.gov/presidents#item-37462) kullanılıyor. İşte Akıllı Kontratın sonucu bu siteden alarak çalışması ve doğru tahmin edenleri belirlemesi gerekiyor. Peki Akıllı Kontrat bunu nasıl alacak?

Bu, en basit ve bariz örnek. İki yıl önce yayınlanan [tahmin piyasaları için blockchain yazımızda](/genel/2018/07/13/gelecegi-tahmin-için-blockchain.html), bu kaynakların blokzincir dünyası dışında, tarafsız olduğu kabul edilen bilgi sağlayıcılardan (örneğin WSJ gazetesi) alınıp blokzincire otomatik ya da uzmanlar tarafından manuel olarak girilmesinden bahsetmiştik. 

ABD seçimi tek bir olaya bağlı tahminlerde işe yarayabilecek olan manuel bilgi aktarımı, merkeziyetsiz dünyada çok da işe yaramayacak gibi görünüyor. Gelin bakalım ne gerekiyor DeFi dünyasına: 

### Merkeziyetsiz dünya için neden önemli?

Merkeziyetsiz finans dünyasının lego gibi birbirine iç içe geçmiş bir şekilde çalıştığından söz etmiştik daha önce. İşte bu lego parçalarının çalışması için yukarıdaki basit örnekte olduğu gibi tek bir kaynağın ötesinde, onlarca hatta yüzlerce bilginin Akıllı Kontratlara akması gerekiyor. 

Böyle bir durumda bilgi kaynaklarının olabildiğince tarafsız bir şekilde bu bilgiyi toplayıp yayınlaması gerekiyor. Bu tip kaynakların, yapılan işin doğasına uygun olarak merkeziyetsiz olmaları, işin güvenilir ve tarafsız gerçekleşmesi için çok önemli. Sadece tarafsız olmaları değil, aynı zamanda çok hızlı bir şekilde toplamaları gerekiyor kaynakların bu bilgileri. Çünkü, dijital teknolojide saniyelerin bile büyük önemi var. 

Bir örnek verelim. Merkeziyetsiz dünyada [türev piyasalarının nasıl olabileceğini anlattığımız bir yazımızda](/genel/2020/08/20/defi-turev-piyasalari-nasil-oluyor.html), bu piyasaların en büyüğü olan [Synthetix'in nasıl çalıştığına da bir diğer yazımızda](/genel/2020/08/28/Defi-turev-piyasasi-synthetix-nasil-calisiyor.html) anlatmıştık.  

Bu tip türev piyasalarında her tür ürünün sentetik bir türevi olabileceğinden bahsetmiştik. Ne demek bu? Basit olarak, herhangi bir ürünün, örneğin altın ya da petrol fiyatını birebir taklit eden ürünlerin, Sythetix üzerinde işlem yapması demek. Ürünün kendisi değil taklidi işlem gördüğünden dolayı, bu piyasalarda işlem yapılabilmesi için dış dünyadaki orijinal fiyatların buraya aktarılması gerek, üstelik çok sık bir şekilde. 

İşte oracle dediğimiz uzmanlar, Akıllı Kontratların ihtiyacı olan bu bilgiyi onlara sağlayan yapılar.  Ve her ne kadar kullanıcı olarak direkt temasa geçmesek bile bizim için de çok kritik bir altyapı hizmetini yerine getiriyorlar. 

### Merkezi kaynak mı istersiniz yoksa merkeziyetsiz mi?

Yukarıda verdiğimiz örnekte merkeziyetsiz bir oracle örneği verdik ancak hemen belirtmek lazım. Bu alanda en büyüklerden bir tanesi ABD'nin en büyük borsası olan Coinbase tarafından yaratılan oracle. Coinbase Price Oracle sayesinde, piyasada işlem gören tokenların fiyat bilgilerini sürekli bir biçimde elde etmek mümkün. 

Merkezi yapılar, DeFi dünyasında genelde hoş karşılanmazlar. Bunun temel nedeni, hep bahsettiğimiz dijital dünyada merkezi yapıların güvenlik açığı olarak adlandırılması. Zira, tek kaynak olmaları nedeniyle bu yapılara yapılacak saldırılar sonrası fiyatların manipüle edilmesine yol açabilir. Bu da, o fiyatlara kullanarak hizmet veren platformları zor durumda bırakabilir. 

### Merkeziyetsiz platformlar nasıl yapıyorlar bu işi?

Tabii bilgiyi zincir dışından içine taşımak o kadar basit bir olay değil. Fazla tekniğe girmeden şu şekilde anlatmaya çalışalım, ancak son kullanıcı olarak ilginizi çekmiyor ise bir sonraki bölüme atlayabilirsiniz: 

Biliyorsunuz, Bitcoin blokzincirinin güvenliğini madenciler sağlıyor. Bu madenciler, aslına bakarsanız Bitcoin sisteminin fiziki dünyaya bağlı olduğu (dayandığı) tek kısım. Zira, sistemin korunabilmesi için fiziki olarak elektrik harcanması gerekiyor. Bunu yapan madencilerin her biri aslında bir makine ve bu dünyanın deyişi ile blokzincir ağının bir düğümü... 

İşte, oracle sistemlerinde de benzer şekilde dış dünya ile ilişkiyi bu ağ üyesi makineler kuruyorlar. Bilgi ihtiyacı olan DeFi yapıları, bir Akıllı Kontrat aracılığıyla ne tip bir bilgi istediklerini teknik olarak belirtip oracle hizmeti veren ağın içine koyuyorlar. Teknik derken kasıt, hangi bilgi kaynağının kullanılacağından, ne sıklıkla ve hangi hizmet süreleri (örneğin %99.99)  çalışma gerekliliği gibi istekler. 

Ağ içindeki düğümler bu talepleri içeren Akıllı Kontratları gördüklerinde bu hizmeti ne kadar bir ücret karşılığı yerine getirebileceklerini Akıllı Kontrata bildiriyorlar. Bu ücret genel olarak o ağın kullandığı kripto para üzerinden oluyor. Anlaşma sağlanıp da sistem çalışmaya başladığında, düğümler dış dünyadaki kaynaklardan aldıkları bilgileri Akıllı Kontrat'a aktarıyor, diğer düğümler ağ üzerinden bu bilginin doğruluğunu teyid ediyor. Sonrasında Akıllı Kontrat farklı düğümlerden gelen teyid edilmiş bilgilerin ağırlıklı ortalamasını alıp bir değer buluyor ve talep sahibine bildiriyor. Böylece, bir kişiye bağlı kalmadan, istendiği kadar farklı kaynak kullanılarak olabildiğince tarafsız bilgi sağlanmış oluyor. 

### Son zamanlarda önemi arttı mı?

DeFi dünyasının patlamasıyla birlikte doğru ve hızlı veriye olan ihtiyaç da arttı ve bu alandaki servis sağlayıcılar ciddi rağbet görmeye başladılar... Öyle ki, bu alandaki en büyük iki oyuncu olan Chainlink ve Nest, Eylül 2020'de Ethereum ağın en çok meşgul eden uygulamalar arasına girip bir ayda toplam 2.5 milyon ABD Doları işlem ücreti ödediler. 

Bu alandaki belli başlı oyuncular Chainlink, Band Protocol, Test Protocol, DIA, DOS Network, Zap ve Tellor olarak sıralanıyor. Ancak hemen belirtelim Chainlink bu piyasanın ağır hakimi.. Bu saydığımız oyuncuların piyasa değerlerine bırakalım hemen aşağıya: 

| ![Oracle_servis_saglayicilar](/assets/Oracle_Servis_Saglayicilar.png)|
|:--:| 
| *Oracle servis sağlayıcılar 21 Aralık 2020 piyasa değerleri Kaynak: [CoinGecko](https://www.coingecko.com/en)*|

Chainlink'in bu ağırlığı neye dayanıyor, ne kadarı anlaşılabilir, onu bir sonraki yazımıza bırakalım artık.. 

### Sıkıntıları neler?
Merkeziyetsiz Finans dünyasında oracle sistemlerinin en büyük sıkıntısı gecikmeler. Yukarıdaki bilgi aktarımda bahsetmiştik. Bilgi toplanıyor, blokzincir ağına aktarılıyor, orada teyit ediliyor ve talep edene gönderiliyor. Dijital dünyada aslında saniyeler içinde yapılabilecek bir işlem. Bilginin teyidi sonrası blokzincire yazılıyor olması nedeniyle, blok oluşturma hızları darboğaz yaratıyor. Örneğin Ethereum sisteminde her bir blok 10-20 saniye arasında oluşuyor. Bu da bilginin ulaşımında gecikmeler olması demek. 

Bunun yanında, bilgiyi tek bir kaynaktan alan platformlar da sıkıntı yaşayabiliyor. Örneğin, kendine herhangi bir token fiyat bilgisi olarak merkezi olmayan bir borsayı seçen platformlar

### Sonuç
Hep bahsettiğimiz emekleme aşamasındaki Merkeziyetsiz Finans dünyasının ayağa kalkıp yürümesi için gerekli yapı taşlarında biri oracle servis sağlayıcılar. Şu an için tek bir oyuncunun ağırlığında olması ve merkezi servis sağlayıcıların potansiyel risk barındırması nedeniyle, bu alan aynı hizmet verdiği DeFi platformları gibi teknik olarak farklı ürünlerin çıkmasına ve hacim olarak büyümeye gebe... 

Bir sonraki yazımızda Chainlink örneğini daha yakından inceleyerek, bu farklı ürünler neler olabilir ve bu alan daha nerelere ulaşabilir ona bakacağız.. 
