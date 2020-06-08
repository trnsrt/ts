DeFi hareketindeki en kritik konulardan biri Oracle.. Nedir bu Oracle? Gelin hep birlikte inceleyelim. 

### Nedir bu Oracle ve neden önemli?
Bu satırlarda DeFi sisteminin merkeziyetsiz olduğunu sürekli olarak yazıyoruz. 

Merkeziyetsiz bir yapıda sistemin işleyini Akıllı Kontratlar sağlıyor. Daha önceki bir [yazımızda] Akıllı Kontratların aslında akıllı değil daha çok basit sözleşmeler olduğunu belirtmiştik. Özünde Akıllı Kontrat kendisine verilen direktifi koşulsuz bir şekilde gerçekleştiren bir kod. Gücünü de "kod" olmasında alıyor. Biliyoruz ki, beklenen koşul gerçekleştiğinde bu kod otomatik olarak çalışacak - öyle bir kişinin ya da otoritenin keyfini beklemeyecek. 

Peki ya, "beklenen koşulun" gerçekleştiğini nereden biliyoruz? Daha doğrusu bu koşulun gerçekleştiğini Akıllı Kontrat'a kim söylüyor? Bildiniz: Oracle. 

#### Neden önemli?

Kontrat üzerindeki yaptırım gücünün tek sahibi olduğu için Oracle çok önemli. Özellikle merkezi olmayan yapılarda. Çünkü, doğası gereği bu yapılarda sistemi geri döndürüp yapılan işlemi geri alamazsınız. Gerçekleşmiş bir koşula olmamış gibi davranamazsınız. 

#### Nerede bu Oracle?

Oracle genelde sistem dışında oluyor. Tarafların hakem olarak belirledikleri herhangi bir üçüncü parti olabilir. Örneğin, yarın havanın Ankara'da 25 C'nin üzerinde ya da altında olacağı konusunda iddiaya tutuşan iki kişi, kendi aralarında Devlet Meteoroloji İşlerinin her sabah açıkladığı verileri baz alırlarsa Oracle Meteoloji İşleri olur. 

#### Şu anda nasıl hallediyor DeFi Oracle olayını?

İşte bu tip Akıllı Kontratların bulunduğu blok zincirler (ki çoğunluğu altyapı olarak ağırlıklı Ethereum kullanıyorlar) bu bilgileri genelde blokzincir dışından alıyorlar. [[[Bu bilgileri alabilmek için genelde api'ler kullanarak üzerinde anlaşılan üçüncü parti yapılardan bilgileri çekiyorlar]]]


### Gelecekte neler olması planlanıyor?

DeFi hareketinin en önemli özelliği merkeziyetsiz olmak diyoruz. Bu alandaki pek çok projenin hâlâ pek çok bakımdan merkezi olduğunu ve yavaş yavaş merkeziyetsiz hale geldiğinden bahsediyoruz. 

İşte Oracle yani tarafsız bilgi kaynakları için de benzer süreç söz konusu. Şu anda tamamen merkezi dış dünyadan alınan bilgilerin zamanla merkeziyetsiz şekilde alınması düşünülüyor. 

Nasıl olacak bu? Bir örnek verelim. Diyelim blokzincir üzerindeki herhangi bir işlemin gerçekleşmesi için Ethereum fiyatının (örneğin ETH/DAI yani Ethereumun DAI fiyatı) referans alınıyor olması lazım. Böyle bir durumda Akıllı Kontrat'ın sistem dışına çıkıp bilgi çekmek yerine Ethereum sistemi içindeki bir merkeziyetsiz kripto para borsasına gidip oradan bu bilgiyi alması mümkün olabilir. Bu alanda [Uniswap](https://uniswap.exchange/swap) bu tip ihtiyaçlar için bir referans noktası olmak için gerekli altyapıyı sunmakta. 


### Sonuç 

