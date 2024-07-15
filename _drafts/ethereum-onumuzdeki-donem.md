### Önümüzdeki dönem neler getirecek?
Önümüzdeki dönemde Ethereum ekosistemi, ölçeklenme, maliyetleri azaltma ve sansüre karşı daha merkeziyetsiz bir hale gelme konusunda çalışmalar yürütüyor.  (Yapılan tüm çalışmaların yol haritasının Ethereum kurucusu Vitalik Buterin'in geçtiğimiz yıl yayınladığı [şu diyagramda](https://twitter.com/VitalikButerin/status/1588669782471368704/photo/1) görebilirsiniz]

Gelin şimdi tek tek bu iyileştirmelerin önce teknik olarak ne işe yarayacağına, sonra da varsa ETH'nin para politikasına nasıl bir etki yapacağına bakalım. İlk konumuz ölçeklenme. 

#### Ölçeklenme ve maliyetlerin azaltılması

##### Teknik olarak
Ölçeklenme, Ethereum'un geniş kesimlere ulaşan bir altyapı olmasının önündeki en büyük engel. Ethereum ileride oluşabilecek yoğun talebi karşılamanın yolunu üzerine gelecek yükü ikinci seviye çözümlere atmakta bulmuş durumda. Bu nedenle, Ethereum geliştiricilerinin şu an için odaklandığı temel geliştirmeler, ikinci seviye çözümlerin işlem maliyetlerini azaltmaya yönelik.

İkinci seviye çözümlerin temel masraf kalemi, üzerilerinde kullanıcılar tarafından yapılan binlerce işlemi Ethereum blokzinciri üzerine aktarma sırasında kullandıkları alan için ödedikleri ücret. Ethereum geliştiricilerin üzerinde çalıştıkları temel bir geliştirme ile (EIP-4844) ikinci seviye çözümlerin Ethereum'a aktarmaları gereken veri miktarını minimuma indirmeyi planlıyor. Hedef, bu sayede ikinci seviye çözümlerin saniyede 100,000 işlem yapmasına olanak verecek bir altyapı olmak. 

Blokzincirlerin sağladığı en önemli faydalardan bir tanesi, geçmişe yönelik olarak işlemlerin kaydının değiştirilemez bir şekilde saklanıyor olması. Ethereum blokzinciri de kendi üzerinde geçmişte yapılmış tüm işlemlerin kaydının tutulmasını istiyor. Sistem bunu sadece kendi üzerinde yapılan işlemlerden değil, ikinci seviye çözümlerden de aynı şekilde istiyor. Yani onlara 'kendi üzerinizde yapılan tüm işlemlerin kayıtlarını bana aktarmalısın' diyor. Ve bu bilgi, Ethereum üzerindeki binlerce makinede tutuluyor. Halbuki, ikinci seviye çözümler için bu bilgilerin geçmişe yönelik o kadar detaylı tutulmasına gerek yok, bu işlemlerin doğru olduğunu gösteren basit kanıtların tutulması yeterli [^2].  İşte yapılan bir diğer geliştirme (EIP-4444) ile, üç aydan fazla bir süre Ethereum üzerinde kalan ikinci seviye çözümlerin detay bilgilerinin silinmesi, dolayısıyla Ethereum sistemi üzerinde yer işgal etmemesi planlanıyor. 

Yukarıdaki geliştirmeler tamamlandıktan sonra daha uzun vadede ölçeklenme konusunda planlanan iki önemli geliştirme var. Bunlardan birincisi ikinci seviye çözümler yanında, Ethereum'un kendisi üzerindeki işlemleri de çok basit hale getirmek. Burada temel olarak amaçlanan, yeni gelişen teknolojiler (örneğin SNARK) sayesinde, onaylayıcıların üzerindeki işlem yükünü alarak, Ethereum ana sisteminin çok daha fazla kapasiteye sahip olması. Öyle ki, bir noktada sistem üzerindeki her bir validatörün, ikinci seviye bir çözüm gibi yüzlerce işlemi bir anda yapabilmesi mümkün olabilecek. Bir diğer bakış açısıyla, şu an dışarıda olan ikinci seviye çözümlere benzer Ethereum'a doğal olarak bağlı ikinci seviye çözümler gelecek (Ingilizcede enshired roll-up denen, sisteme işlenmiş çözümler)[^3]. 

İkinci bir geliştirme ise, onaylayıcılar üzerindeki yükü daha da azaltmayı planlıyor. Şu anki durumda, onaylayıcılar onaylamak oldukları bloğun tamamını kontrol etmek zorundalar. İleride DAS (data-availability-sampling) denilen bir sistem ile artık bloğun ufak bir kısmını onaylayarak doğruluğunu kontrol edebilecekler. 

Bu iki geliştirme ile onaylayıcıların üzerindeki yük azalıyor. Ne demek tam olarak bu, neye yarar? Onaylayıcıların üzerindeki yükün azalması demek, onaylayıcı olmak için gerekli makine gücünün azalması demek (örneğin, yüksek işlem kapasitesi gerektiren pahalı bir makine yerine akıllı saat ile bile onaylayıcı olabilmek). Bunun da getireceği en büyük artı, sistemi yürütebilen daha fazla makine olması, bunun da sistemi daha merkeziyetsiz hale getirmesi. Bu uzun vadede, gerek büyüme gerekse sansüre dayanıklılık için olmazsa olmaz bir koşul. 

##### Ether para politikasına etkisi
Yukarıda yapılan iyileştirmelerin ikinci seviye çözümlerin ETH'ye ödeyeceği ücretleri düşüreceğini söyleyebiliriz. İyi de o zaman neden Ethereum geliştiricileri sistemin gelirlerini azaltacak bu iyileştirmek için bu kadar çaba sarfediyorlar? Bunun birkaç nedeni var. 

Birincisi, Ethereum'un geçmişte yaşadığı sıkışıklıkların işlem ücretlerini ne kadar artırdığının görülmesi. 
[Ethereum işlem ücretleri]

Ethereum geliştiricileri, bu tip bir sıkışıklığın önümüzdeki dönemde bir kaç kez daha yaşanması durumunda kullanıcıların farklı ağlara kaçmasını istemiyorlar. Zira, onların beklentisi kullanıcı sayılarının yüz hatta binlerce kez artması. Bunu Ethereum üzerinde gerçekleştirmeleri mümkün olmadığı için işlem yükünü ikinci seviye çözümlere atmaya çalışıyorlar. İkinci seviye çözümler ise ancak işlem maliyetleri azalırsa bu yükü almaya razı olacaklar. Neden? Çünkü kullanıcıları kendilerine ancak düşük işlem ücreti uygularlarsa çekebilirler, bunun için de kendilerinin Ethereum’a ödeyecekleri ücretin (yani masraflarının) aynı oranda düşük olması gerekiyor. Burada karşılıklı bir çıkar ilişkisi söz konusu. 

İkincisi, Ethereum geliştiricileri artık ağırlıklı olarak altyapı çözüm tarafına odaklanmış durumdalar. Kullanıcı perspektifinden uygulamaların geliştirilmesi kısmını ikinci seviye çözümlere bırakmış durumdalar. Burada da olabildiğince çok ikinci seviye çözümün uygulamaya konmasının rekabeti artıracağını görüyorlar.  Yeni ikinci seviye çözümler de ancak maliyetler azalırsa ortaya çıkarlar; geliştiriciler bunun da farkındalar. 

Bir yandan da Ethereum, ikinci seviye çözümleri kendisi için ücretsiz bir deney laboratuarı olarak görüyor. Girişim sermayesi parası ile desteklenen ikinci seviye çözümler, aralarındaki rekabet nedeniyle gerekli iyileştirmeleri hızlı bir şekilde yapıp yürürlüğü koyuyorlar. Bu geliştirmeler ikinci seviyede kullanılıp sorunları giderildikten sonra birinci seviye için uyarlanabilir bir hale gelecekler. 

Ethereum geliştiricilerinin ölçeklenme ile birlikte üzerinde çalıştıkları bir diğer konu ile MEV konusunu nihai bir çözüme oluşturmak. 

#### MEV sorunu/konusu
##### Teknik açıdan
Yukarıda ilk kısımda bahsettiğimiz MEV konusu Ethereum üzerinden bir kambur oluşturuyor. Zira, MEV sisteme iki yönden zarar veriyor. Birincisi, kullanıcıların yapmaya çalıştıkları işlemlerden elde edecekleri kârı azaltıyor. İkincisi ise MEV'ye neden olan blok yapıcıların aynı zamanda gelen işlemleri sansür edebilme gücüne sahip olmasına yol açıyor.  

Bunu çözebilmek için geliştiriciler işlemlerin onaylanması sırasında çalışan aktörleri olabildiğince rekabet içine sokmaya çalışıyorlar. Kullanıcılar tarafından havuz düşen işlemlerin yürürlüğe koyanlar ile işlemleri gerçekleştirenler şu aşamada ortak çalışıyorlar. Blok oluşturanların temel amacı, blok üzerinden elde edecekleri kârı maksimize ederek cebe atmak. Şu an için üzerinde çalışılan geliştirme ile (blok oluşturmayı öneren ile blok yapanların ayrılması, ingilizcesi proposer-builder separation kısaca PBS) bu iki kesim arasındaki rekabetin artırılması planlanıyor. 

Rekabeti artırmanın yanında, işlem havuzuna (bir deyişle bekleme odasına) düşen işlemlerin şifrelenmesi, blok yapıcıların sansürüne uygulama gücünü ortadan kaldıracak.

Uzun vadede yapılacak diğer iyileştirmeler ile MEV botlarının kullanıcı işlemlerinin önüne geçerek kullanıcıları zarara uğratmasının da önüne geçilecek.

#####  Ether para politikasına etkisi
Yukarıdaki geliştirmelerin toplu adı olan PBS uygulamasının ether para politikasına çok net bir etkisi olacak Zira PBS ile planlanan MEV ile ortaya çıkan gelirin paylaşımının değiştirilmesi. Birincisi bu gelirin önemli bir kısmının, rekabet nedeniyle blokları oluşturanların değil işlemleri onaylayanların yani ETH'yi stake edenlerin cebine gitmesi. İkincisi ise bu gelirlerin kalan kısmının yakılması. Dolayısıyla, şu an için tüm geliri cebine atan blok oluşturucuların gelirlerin sadece ufak bir kısmını alacak olması. 

Bu sayede hem ether stake edenlerin geliri artacak, hem de MEV burn ile piyasadaki ETH'nin sayısında azalma olacak. 

#### Kullanım kalitesinin artırılması
Yukarıda bahsettiğimiz gibi, esasında Ethereum bir altyapı olarak kullanıcı ile ilgili konularda geliştirmeleri ikinci seviye çözümlere bırakma niyetinde. Yine de, belli standartların oturtulması amacıyla kimi geliştirmelerin Ethereum seviyesinde yapılması, ağın geniş kesimlerce kullanılması için oldukça önemli. 

Bu geliştirmelerin en önemlisi Account Abstraction olarak adlandırılan hesap soyutlama. Oldukça teknik olarak görülebilecek bu geliştirme en basit anlatımı ile, kullanıcıların hesaplarını on-iki kelime ile koruyan sistemin getirdiği zorlukları ortadan kaldırma amacını taşıyor. On iki kelimeyi kaybetmenin sonucu hesaplara erişimin de kaybedilmesi korkusu bana sorarsanız, önemli bir kesimin kişisel cüzdan kullanmamasının en önemli nedenlerinden AA ile hesapların birer akıllı kontrat haline gelmesi ve kullanıcının farklı mekanizmalar ile hesaplarını erişim imkanının verilmesi Ethereum'un geniş kesimlerce kullanılmasının önündeki en büyük engellerden birini ortadan kaldıracak. 

[Önümüzdeki dönemde ETH para arzının potansiyel gelişimi tablosu - Jon Charboonau]

