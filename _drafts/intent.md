Bu yazımızda Web3 dünyasının son gözdelerinden olan Intent konusuna değineceğiz. 

Merkeziyetsiz dünyanın temel değer önerisi, kullanıcılara dijital dünyada büyük bir özgürlük vermesi. Nasıl bir özgürlük bu? Kullanıcının dijital dünyada sahip olduğu varlıklar üzerinde söz hakkının sadece kendisinde olması aslında. Bir başka deyişle, bu hakkı kullanabilmek için bir aracı kullanmak zorunda kalmaması. 

Özellikle dijital dünyada kullanıcı olarak yaşadığımız hak ihlalleri göz önüne alındığında bu özgürlüğün değerini gün geçtikçe daha çok anlıyoruz. Kişisel verilerimizin bizden izinsiz kullanılması, çalınması gibi konular yavaş yavaş hayatımıza girmeye başlıyor. 

Yine de, merkeziyetsiz dünyanın sunduğu bu değer önerisi tek başına kullanıcıları kendisine çekebilmek için yeterli değil. Zira bu teknolojiler insanların hayatına etki etmek istiyorlar ise, onlara çok daha fazla fayda önerebilmeli. Bunlar içinde en önemlisi, kullanıcıya sunulan hizmetlerin rahat, pratik ve esnek olması. Üstelik tüm bunların elbette kullanıcı dijital varlığına tam sahip olmaya devam ederken verilmesi. Yani, bir nevi Web2 dünyasının o sevmediğimiz aracılar tarafından verilen nimetlerinin Web3 dünyasında da sunulması. 

Aslına bakarsanız, tamamen yazılımdan oluşan Web3 dünyası için bu altından kalkılamayacak bir yük değil. Peki neden bu alanda geride kaldı Web3 oyuncuları şimdiye kadar? Temel nedeni, geliştiricilerin bugüne kadar daha çok teknolojinin altyapısını kurmaya odaklanmış olmaları idi. Bunu bir şehrin altına kablo döşenmesi gibi düşünün. Önce şehrin altına temel yapılar döşenmeli ki sonra sıra evlere kablo çekmeye gelsin. 

İşte bu yazımızın konusu olan intent'ler, sundukları yeni özelliklerle Web3 dünyasını, kullanıcıya hizmet tarafında bir adım daha ileri götürmeye adaylar. Gelin nedir intent'ler kısaca bir göz atalım: 

### Nedir Intent? Ne demek tam olarak?
Intent Türkçe anlamıyla maksat, niyet, amaç anlamına geliyor. Blokzincir dünyasında da benzer şekilde kullanıcıya isteğini (niyetini) daha rahatça anlatabileceği ve gerçekleştirebileceği araçlara 'intent' deniyor. Nedir bu amaçlar? Blokzincir bu amaçları tam olarak karşılayamıyor mu? 

Bu soruların cevaplarını verebilmek için blokzincirlerin çalışma prensibini biraz daha yakından anlamak gerekiyor. Blokzincir dediğimiz yapıların ne olduğunu daha önce bu satırlarda yineledik: Esas olarak blokzincirin yaptığı, üzerinden geçen işlemleri değiştirilemez bir şekilde binlerce makine üzerine kaydetmek. Makinelerin işlemleri nasıl ve ne şekilde kaydedeceğini blokzincir yazılımı üzerinde çalışan akıllı kontrat dediğimiz kod parçacıkları belirliyorlar. [^1]

Akıllı kontratlar kullanıcı tarafından çalıştırıldığında kendilerine verilen emirleri satır satır harfiyen yerine getirirler. Bir yandan kesinlik getirdiği için oldukça önemli olan bu özellik bir yandan da kullanıcının ne istediğini çok iyi bilmesini ve bunu doğru bir sıra ile akıllı kontratlara yaptırmasını gerektirir. Ne var ki, kullanıcıların ne böyle bir teknik yetkinliği ne de öğrenme isteği var. (Olmasına da gerek yok zaten.) Üstelik her bir kullanıcının isteği farklı olabiliyor. Bu farklı isteklerin kesin çözümler sunan akıllı kontratlar ile karşılanması neredeyse imkansız. Zaten, her isteği karşılayacak akıllı kontratlar çok karmaşık ve uzun olacağı için kısıtlı blokzincir alanında çalışamazlar da.[^2]

Temel sorunlardan biri burada ortaya çıkıyor. Blokzincire gönderilen işlemler basit ama kullanıcıların istekleri karmaşık ve birbirinden farklı. Ne yapılacak o zaman? Özellikle başta Ethereum olmak üzere son zamanlarda blokzincir dünyasında popüler olan birkaç trend var. 

Bunlardan biri, blokzincirleri daha modüler hale getirerek, hem rekabeti artırmak hem de kullanıcılara daha geniş bir kapasite sunmak.  Modüler yapı olarak da adlandırılan bu gelişme ile blokzincirin kısıtlı alanını sadece değeri kaydetmek ile sınırlı tutup, alan üzerinde çok yer tutan akıllı kontrat işlemlerini ikinci seviye çözümlere çekmek amaçlanıyor. Bu sayede, işlemleri gerçekleştirmenin yükünü ikinci seviyeye atıp, sadece bu işlemlerin doğru yapıldığına dair kanıtları ve işlem sonuçlarını ana zincirde tutmak. 

Modüler yapının en bilinen örneklerini,  Ethereum üzerindeki işlemleri kendi blokzincirler üzerine taşıyıp, yaptıkları işlemlerin kayıtlarını Ethereum'a atan ikinci seviye çözümlerde gördük. 

Son zamanlarda da, bu ana blokzincir üzerindeki işlem yükünü zincir üzerinden (ingilizcesi on-chain) alıp, zincir dışına (ingilizcesi off-chain) çıkaran bir başka yeni trend olarak intent'ler karşımıza çıktı. 

Intent'ler, temel olarak kullanıcıların yapmak istedikleri kompleks işlemleri anlayıp onları zincir dışında gerçekleştiren, sonra bu işlemlerin sonuçlarını zincire kaydeden araçlara verilen genel ad. Yani kullanıcı yaptırmak istediği işlemler için tek tek blokzincir ile muhatap olmuyor. Hatta ne yapması gerektiğini bilmesine bile gerek yok. Ne istediğini belirtiyor ve aracılar onun yerine gerekli işlemleri gerçekleştiriyorlar. 

### Ne tip işlemlerden bahsediyoruz?

Intent ile neler yapılabileceği ile ilgili uçsuz bucaksız hayaller kurabilirsiniz. Dilerseniz, pratik bir örnek ile başlayalım neler yapabileceğimize; merkeziyetsiz bir borsa üzerinde al-sat işlemi yapmak. 

Kullanıcı bir token almak istiyor olsun. Şu anda pratik olarak baktığımızda, bu işlem için merkezi borsaları kullanması çok daha pratik.  Merkezi borsalar, emir defteri dediğimiz sistem ile kullanıcıya çok farklı fiyat seviyelerinden alım için emir yazdırabilme imkanı veriyorlar. 

Merkeziyetsiz dünyanın en büyük borsası olan Uniswap'ta ise bu mümkün değil. Kullanıcı sadece borsanın verdiği fiyattan işlem yapabiliyor. Bunun temel sebebi, emir defterinin çalışabilmesi için farklı fiyat seviyelerinde emirlerin bulunduğu bir tahta ve bu tahtada sürekli değişen emirlerin girilmesi gerekiyor. Böyle bir sistemi blokzincir üzerinde yapabilmek blok alanlarının kısıtlı olması nedeniyle mümkün değil. 

İşte Uniswap bu soruna çare bulabilmek amacıyla kullanıcılarına Uniswap X adında yeni bir ürün sundu. Bu üründe, kullanıcı hangi tokeni hangi fiyattan almayı istediğini belirttiği noktada, bu emri alan aracılar piyasayı tarayarak en uygun fiyattan emiri karşılıyorlar. Aracılar, piyasayı tararken farklı merkeziyetsiz borsalara hatta farklı zincirlerdeki borsalara bakarken, emri kendi portföylerinden bulunan tokenlerden de karşılayabiliyorlar. Bir nevi, piyasa yapıcı aracılar ortaya çıkıyor. 

Kullanıcı intent kullanarak tercih ettiği sonucu deklare ediyor: “Şu fiyattan şu kadar token almak istiyorum”. Sonrasına ise karışmıyor. Şu anda bu işi yapan toplayıcı dediğimiz (ingilizcesi ‘aggregator’) yerler var. Ancak toplayıcılar genel olarak bir yada birkaç merkeziyetsiz borsadan fiyat alıp kullanıcıya sunuyorlar (odos gibi emri birkaç parçaya bölüp farklı yerlerde işleme sokarak daha optimal fiyat veren toplayıcılar da mevcut). Intent ise bu işlemi çok daha özgür bir şekilde yapıyor. Aracılar isterlerse farklı borsalardan isterlerse farklı zincirlerden ya da kimi zaman kendi portföylerinden verilen işlemi gerçekleştiriyorlar. Bunların hiçbir kullanıcının umurunda değil. O istediği emrin yerine getirilmesi ile ilgileniyor. Emir yerine getirildiğinde de işlem blokzincir üzerinde sonuçlandırılıyor. 

Peki bu merkeziyetsizliğe ya da aracısızlığa aykırı mı? Pek sayılmaz. Sonuçta kullanıcı istediği emri istediği fiyattan gerçekleştiriyor. İşlemin sonucu da ancak blokzincire yazılınca geçerli oluyor. Arada kullandığı aracılar arasında bir rekabet var, herhangi bir aracıya işlem öncesi parasını emanet etmesi gerekmiyor - dolayısıyla aracıların kullanıcı üzerindeki gücü neredeyse sıfıra yakın. 

Uniswap, bu alanda en öne çıkan kullanım alanı olsa da örnekleri çoğaltmak mümkün. Örneğin, blokzincirler arası bir köprü across, intent sistemini kullanarak pazarda oldukça ciddi bir pay almış durumda. Blokzincirler arası geçişte likidite sağlayıcıların oluşturduğu havuzları kullanan köprülerin aksine across, her ağda farklı intent sağlayıcılar ile çalışıyor. Kullanıcı parasını bir ağdan diğerine geçirmek istediğinde across intent hizmeti veren aracılar içinde bunu en ucuza ve en hızlı şekilde verebilecek olanı aracıyı seçiyor. Bu durum kullanıcıya ucuz ve hızlı para geçişini sağlarken, across'a da geçmişte sıkça yaşanan havuzların boşaltılması riskinden korunma imkanı veriyor. 

### Sonuç

Intent'ler önümüzdeki dönemde, özellikle modüler yapılar içinde daha sık örneklerini göreceğimiz bir dünyanın kapılarını bizlere açıyor. Modüler yapılar rekabeti artırıp, gelişmenin önünü açtıkları ve ölçeklenme sağladıkları için oldukça avantajlılar. Bu tip artıların yanında onlarca farklı hizmet sağlayıcının olması, her birinin farklı standartlar kullanmasının getirdiği eksiler de söz konusu. Bir yanda kullanıcının kafası karışıyor, öte yanda, örneğin likiditenin farklı zincirlere yayılmasının getirdiği optimum fiyatı bulamama gibi sorunlar söz konusu. Modüler yapılar intent'ler sayesinde kullanıcıları kendilerinde tutmayı başarabilecekler. 





—-

[^1]: Uygulama ya da protokol adı verilen akıllı kontratlar oldukça basit ve herkese açık bir şekilde yazılmış olmak zorundalar. Neden? Çünkü ne yapıp ne yapamayacağının çok iyi bir şekilde bilinmesi gerek. Bunun için de dışarıdan isteyen herkesin denetleyeceği bir şekilde bizlere sunulmaları zorunlu. 

[^2]: Akıllı kontratlar, kullanıcı tarafından çalıştırıldığında kendisinden istenen işlemi yapar ve hem işlemi hem de sonucunu blokzincir üzerine yazarlar. Blokzincir, üzerinde binlerce kullanıcının olduğu büyük bir yer ama kullanım alanı kısıtlı. Üstelik binlerce makinede bu işlemlerin yapılması gerekiyor. Büyük büyük işlemler getirip yüksek kapasiteli makineler kullanalım derseniz bu sefer sistemi götürebilecek makine sayısında azalma oluyor. Bu da sistem üzerinde merkezileşmeye yol açıyor ki - Web3 sevdalıları için en tehlikeli konulardan biri sistemlerin merkezileşmesi. Merkezileşme, sistemde dış tehlikelere karşı zaafiyet yaratıyor (siber ataklardan tutun, belli bir kesimin sistemi kontrol edebilmesine kadar). İşte bu nedenle, işlemlerin basit olması elzem.
