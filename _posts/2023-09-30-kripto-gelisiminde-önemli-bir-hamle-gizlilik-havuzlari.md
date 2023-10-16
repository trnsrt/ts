---
layout: post
title:  "Kriptonun gelişiminde önemli bir hamle: Gizlilik havuzları"
date:   2023-09-30 18:17:56 +0300
categories: Genel
tags: Yazılar, DeFi
---


Bu yazımızda, Vitalik Buterin ve arkadaşları tarafından Eylül ayı başında yayınlanan yeni bir [makaleye](https://ssrn.com/abstract=4563364) göz atacağız. 

### Kriptoparaların düzenlemeler ile uyum sorunu
Kriptoparaların geniş kesimlerce kullanımının önündeki en büyük engellerden bir tanesi düzenleyici kurumların bu paralara mesafeli yaklaşması. Bu tutumun arkasında yatan temel neden bu paraların yasa dışı aktiviteler ile ilişkilendiriliyor olması. Kripto dünyasının buna karşı seslendirdiği "İyi ama en büyük kara para aklama olayları ABD Doları ile üstelik sıkı kuralların uygulandığı bankacılık sektöründe oluyor?" argümanı oldukça makul olsa da maalesef kabul görmüyor. 

#### Blokzincirin temel özelliği şeffaflık
Blokzincirin temel özelliklerinden biri üzerinden geçen işlemlerin herkes tarafından denetlenebiliyor olması. Bu merkeziyetsiz finansın klasik finansa göre temel farklarından biri ve aslında düzenleyici kurumlara işlemleri takip edebilmeleri açısından büyük bir fırsat veriyor. 

#### Bu kadar şeffaf ortamda mahremiyet nasıl sağlanıyor?
Tabii işlemlerin bu kadar şeffaf olmasının kullanıcı açısından sorunlu bir tarafı var, o da temel hak ve özgürlüklerden biri olan mahremiyetin nasıl sağlanacağı. Blokzincir bu sorunu, 'işlemler şeffaf ama hesap sahipleri (yarı) gizli' prensibi ile çözmeye çalışıyor. İşte bu da düzenleyici kurumlar tarafında bir sorun yaratıyor: Kimin kullandığını bilemeden kripto dünyasında kara para finansmanı ile ilişkilendirilen aktiviteleri nasıl önleriz? 

Ethereum benzeri blokzincirlerde, bu tip bir aktiviteye karışmış bir hesap anında mimlenebiliyor ve 'kara listeye' alınıyor. Örneğin bir DeFi platformuna saldırı olduğunda, saldırıyı yapan hesap derhal kara listeye alınıyor ve başta kriptopara borsaları olmak üzere diğer platformlar tarafından bu hesaptan gelen paralar kabul edilmiyor.

#### Mahremiyet özelliği kötüye kullanılıyor olabilir mi?
Özellikle kanun dışı aktivitelerde bulunan saldırganların, kara listelerden kurtulması bu zamana kadar 'karıştırıcı' adı verilen akıllı kontratlar aracılığıyla oluyordu. Bu sistemler temel olarak şu şekilde çalışıyor. Akıllı kontratlar aracılığıyla bir havuz yaratılıyor. Saldırgan herhangi bir hesaptan havuza para gönderiyor, sonra bu parayı belli bir süre sonra kendine ait bir başka hesaba 'çekiyor'. Böylece iki hesap arasındaki bağlantı koparılmış oluyor. 

Hemen aklınıza şu soru gelebilir: "İyi de, kanunlara saygılı insanlar neden bu havuzları kullansın?". Burada temel neden, insanların mahremiyet istekleri. Bir hesaba para gönderdiğinizde tüm blokzincir bu paranın sizin hesabınızdan gittiğini görüyor. Eğer bir şekilde bu hesabın size ait olduğu anlaşılır ise, hem bakiyesi hem de geçmiş ve gelecek tüm bakiyeleri herkes tarafından görülüp takip edilebilir. Bir yerde kahve içmek için kripto para kullandığınızda bunu herkesin görmesini ister misiniz? Ya da bir başka örnek: Herhangi iki ülke arasında yaşanan bir savaşta, taraflardan birine yardım etmek isterseniz, kriptopara kullanmanız durumunda, hesabınızın diğer ülkenin hackerları tarafından hedef haline gelmesi riskine maruz kalabilirsiniz. İşte bunun gibi pek çok makul sebeple de para gönderdiğiniz yer ile hesabınızın bağını koparmak isteyebilirsiniz. 

Bu tip 'karıştırıcı akıllı kontratların' en büyüğü olarak bilinen Tornado Cash, işte tam da bu 'hesaplar arası bağlantıyı koparması' ve özellikle Kuzey Koreli saldırganlar tarafından 'para aklamada' kullanılması nedeniyle ABD'li otoritelerin hiddetini üzerine çekmişti. Öyle ki, alt tarafı bir akıllı kontrat olan bu yazılımın iki geliştiricisinden biri Hollanda'da diğeri ise ABD'de tutuklandı. (Bu konuyu anlatan iki ayrı yazıya [şuradan](/genel/2022/08/20/tornado-cash-olayi.html) ve [şuradan](/genel/2022/08/27/tornado-cash-olayi-defiyi-nasil-etkiler.html) ulaşabilirsiniz.)

### Bu soruna potansiyel bir çözüm: Gizlilik havuzları

Kullanıcıların mahremiyet isteği temel bir hak ve özgürlük. Öte yandan, bunu sağlayan Tornado Cash benzeri yazılımların masum insanların yanında saldırganlar tarafından da kullanılmasının getirdiği sıkıntılar var. Peki burada her iki tarafı da memnun edecek bir orta yol bulunamaz mı?

İşte Ethereum'un kurucusu Vitalik Buterin'in önderliğinde dört kişi tarafından kaleme alınan son [makale](https://ssrn.com/abstract=4563364), bu konuda bir çözüm önerisi ortaya atıyor. Nedir önerilen?  Temel olarak kullanıcıların Tornado Cash benzeri bir yapıyı kullanırken mal varlıklarının 'kirli para' ile olan ilişkisini kopartmak.

Nasıl olacak bu? Kişi hiç kimseye 'çaktırmadan' hesabın sahipliğini kanıtlayacak. Yani 'karda yürüyecek ama izini belli etmeyecek'. İyi de blokzincir gibi şeffaf bir yapıda bu olası mı? Orada da gizlilik üzerine kullanımı gün geçtikçe gelişen teknolojiler imdada yetişiyorlar. Bu teknolojiler sayesinde kullanıcı mal varlığını, 'gizlilik havuzlarında' bulunan 'temiz paralar' ile ilişkilendirebilecek (ya da alternatif olarak 'kirli paralar' ile ilişkisini kesecek). Bunu yapabildiği noktada, artık düzenleyici kurumlardan gelen "Hesaba gelen paranın kaynağı neresi?" sorusuna makul bir cevap verebilecek. 

#### Teknik olarak nasıl çalışıyor?
İyi güzel de nasıl çalışıyor sistem tam olarak? Şimdi gelin işin teknik kısmına da göz atalım. 

Sistemin çalışma prensibi, kullanıcıların paralarını kendi hesapları yerine, 'ilişkili bir para kümesi' (ingilizcesi association-set) içine çekmeleri şeklinde açıklanabilir. Bu bağlantılı para kümesinin nasıl oluşturulacağı tamamen kullanıcıya bırakılmış[^1].

Burada pratik pek çok soru akla geliyor. Birincisi, kullanıcı 'temiz' ve 'kirli' ayrımını nasıl yapacak? Bu oldukça zor ve zahmetli bir iş. Burada kullanıcıya bu iş için uzmanlaşmış aracıların yardım edeceği varsayılıyor. İlişkili küme sağlayıcısı (ingilizcesi 'association set provider') denen bu aracılar, aslında kredi derecelendirme kuruluşları gibi çalışıyorlar. Zincir üzerinde ya da dışında faaliyet gösterebilecek bu aracılar oluşturdukları ilişkili küme listelerini (tercihen zincir üzerinde açıklayarak) kişi ve kurumların hizmetine sunacaklar. Kişi, parasının içinde bulunduğu herhangi bir havuzdan para çektiğinde, parasının 'kirli' işlere bulaşmadığını kanıtlamış olacak. 

Peki kişi paranın kendine ait olduğunu kanıtlarken paraya sahipliğini nasıl gizli tutacak? Nerede kaldı mahremiyet? İşte burada da mahremiyet konusunda son dönemde giderek daha çok kullanılmaya başlanan zk-proof (İngilizce zero-knowledge-proof Türkçesi sıfır-bilgi kanıtları) işin içine giriyor. Zk-proof sayesinde bir kullanıcı içeriğini açıklamadan bir bilgiye sahip olduğunu kanıtlayabiliyor. Bir başka deyişle, bir hesaba sahip olduğunu o hesap ile ilgili hiçbir bilgiyi sızdırmadan tüm dünyaya gösterebiliyor. Bunu nasıl yapıyor peki? Şifreleme ve matematiğin gücünü kullanarak[^2]. 

### Nasıl tepkiler geldi?
Vitalik ve arkadaşlarının makalesi oldukça yeni ve henüz tartışılmaya açıldı. İlk tepkiler genelde negatif oldu. 

Bu tepkilerden en önemlisi, sektörün ağır toplarından ve gizlilik alanında en bilinen kriptoparalardan biri olan Z-cash'in kurucusu Zooko Wilcox-O'Hearn (aka [Zooko](https://twitter.com/zooko)'dan geldi. Zooko yayınladığı bir tweet (post?) [serisinde](https://twitter.com/zooko/status/1701023320400154664) privacy pools gibi yenilikleri, hükümetlerin her geçen gün daha da yoğun bir şekilde insanlara dayatmaya çalıştığı 'masumluğu kanıtlanana kadar herkes suçludur' prensibine uyum sağlamaya çalışan bir hamle olmakla suçluyor. Bu tür hamlelerin kriptonun temel çıkış amacına aykırı olduğunu ve hiçbir zaman efektif olamayacağını belirtiyor. Genel olarak karıştırıcıların paraları karıştırsa bile, bunları kullanan insanların hareketlerinin (havuza para yollar ya da havuzdan para çıkarırken) takip edilebileceğini çünkü insanların örüntü (ingilizcesi 'pattern') içinde hareket eden yaratıklar olduğunu belirtiyor.

Çözüm olarak da (sürpriz!) Zcash benzeri çözümlerin bu tip tavizler vermeden de kullanıldığını üstelik kanunlar ile uyumlu çalışan Coinbase gibi borsalar tarafından da kabul gördüğünü belirtiyor. Kısacası Zooko, otoritelerin biraz daha çaba gösterse Zcash benzeri gizlilik odaklı kriptoparaların yukarıda bahsedilen kara para argümanlarına karşı bir çözüm getirdiğini görebileceği düşünüyor. Bunun yerine tembellik yapıp aynı eski argümanları tekrar ederek yasaklayıcı bir tavır sergilediklerini söylüyor. Mahremiyet havuzu gibi çözümlerin de onların bu konformist yaklaşımına çanak tuttuğunu savunuyor.

Şunu belirtmekte fayda var: Zcash de mahremiyet havuzları da sıfır bilgi kanıtı teknolojisini kullanıyorlar. Zcash bu teknolojiyi kendine temel almış bir çözüm. Vitalik ise, daha yaygın kullanılan ama temelinde sıfır bilgi kanıtı bulunmayan ETH'yi, bu teknolojiyi kullanarak kişisel gizliliği daha korur bir hale getirmeyi amaçlıyor. 

### Sonuç
Mahremiyet havuzu fikri, sektörün gelişmesinin önündeki en büyük engellerden birine çözüm bulmaya çalışması nedeniyle alkışa değer bir çözüm arayışı. Henüz 'kavram' aşamasında olan bu öneri, sektör içindekiler tarafından tartışılıp özümsendikçe, farklı şekilde uygulamalarının ortaya çıkması da olası. Sonuçta bir gün,, kriptoparalara ilgi duyan ancak otoritelerin negatif tutumu nedeniyle bu alana girmekten imtina eden kesimler bu çözümler aracılığıyla kripto alanına adım atarlarsa, mahremiyet havuzları misyonunu başarıyla gerçekleştirmiş olacak. Hemen bugün yarın değil ama birkaç yıl içinde bu alandaki olumlu gelişmeleri görebilmek dileğiyle. 

---
*Not 1: Bu yazı ilk olarak 30 Eylül 2023'de [BTCHaber'de yayınlandı](https://www.btchaber.com/kriptonun-gelisiminde-onemli-bir-hamle-gizlilik-havuzlari/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*

---

[^1]: Teorik olarak böyle bir havuz en çok, o parayı oluşturan tüm paralar yani blokzincirin toplam emisyonu kadar olabilir. En küçük ise kullanıcının hesabı kadar (ki böyle bir durumda kullanıcı hesabının belli etmiş olacağı için 'gizlilik kalmaz'). Kullanıcı işte bu ikisi arasında herhangi bir kümeyi seçebilir. Burada uygulanabilecek yöntemler kullanıcının i) kendi hesabına temiz bulduğu hesapları ekleyerek daha büyük bir küme yapması ya da ii) piyasada bulunan tüm paraların içinden kirli paraları çıkararak bir küme oluşturması olabilir. Bu yöntemlerden birincisine 'üyelik kanıtı' (ingilizcesi membership proof) ikincisine ise 'dışarıda bırakma kanıtı' (ingilizcesi 'exclusion proof') deniyor. Bir örnek ile açıklayacak olursak: 20 tanıdığınız ve güvendiğiniz kişi ile bir araya gelip bir havuz oluşturursanız küçük bir üyelik havuzu oluşturmuş olursunuz. Ya da blokzincir üzerindeki tüm hesapları alıp bundan şüpheli bilinenleri çıkararak (örneğin Kuzey Koreli Lazarus grubuna ait olanlar ya da ABD’nin kara para ile ilgili olarak yayınladığı OFAC listesini) daha büyük bir ‘kötü aktörlerin dışarıda bırakıldığı’ bir havuz oluşturabilirsiniz.

[^2]: Teknik ayrıntılar için [şu yazımıza](https://twitter.com/zooko/status/1701023320400154664) göz atabilirsiniz
