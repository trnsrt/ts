---
layout: book-section
kind: section
title: "Celestia: Modüler blokzincir – Sorularla Web3"
heading: "Örnek: Modüler blokzincir - Celestia"
chapter: 2
chapter_title: "Web3 Ekonomisinin Yapı Taşları"
order: 208
permalink: /Sorularla_Web3/bolum-2/celestia/
description: "Celestia, diğer blokzincirlere hizmet veren modüler bir altyapı zinciri: bir blokzincirin dört temel işlevinden yalnızca ikisini, işlemleri sıralamayı (uzlaşma/consensus) ve işlem yayınlamayı (data publishing) yapmaya aday. İşlem yayınlamayı Ethereum’a göre çok daha ucuza sunuyor ve birçok ikinci seviye ağ bunu kullanmaya başladı. En önemli rakipleri EigenDA ve Avail."
---

Celestia’yı, bundan önceki satırlarda bir blokzincirin temelde gerçekleştirmesi gereken dört fonksiyon içinden sadece iki tanesini yapmaya aday basitleştirilmiş bir altyapı blokzinciri olarak tanımladık. Bu iki fonksiyon, aslında son kullanıcıya çok da dokunmayan, yapılan işlemi sıralama (uzlaşma/consensus) ve işlem yayınlama (data publishing) fonksiyonları.

Kripto alanının iki saygın ismi olan Nick White ve Mustafa Al-Bassam tarafından kurulan Celestia, kendisini diğer blokzincirlere hizmet veren bir altyapı (bir nevi B2B) olarak tanımlıyor. Hizmet verdikleri bu iki alandan özellikle 'işlem yayınlama', onlara göre blokzincirlere fazla değer katmayan, adeta yük olan bir fonksiyon. Neden?

İşlem sonuçlarını yayınlama (data publishing) çok fazla blok alanı isteyen bir fonksiyon. Bu, kendi blokzinciriniz varsa çok büyük bir sorun olmayabilir ama eğer Ethereum üzerine kurulu ikinci seviye çözüm iseniz, işlemleri Ethereum üzerinde yayınlamanız gerekiyor. Buradaki sorun Ethereum'un yoğunluğu nedeniyle oldukça pahalı olması. Şu an ikinci seviye çözümlerin maliyetleri içinde en büyük kalem burası. Celestia ile bu maliyetleri 100'de birine indirmek mümkün. İşte Celestia'nın sunduğu temel çözüm bu[^1].

Celestia, ikinci seviye blokzincirlerin temel fonksiyonunun işlem gerçekleştirme (execution) olduğuna, bu nedenle blokzincirlerin bu alana odaklanması gerektiğine inanıyor. Özellikle ikinci seviye çözümler için temel değer önerileri şu şekilde: Kullanıcının parası, Ethereum zinciri üzerinde güvende[^2]. Sen son kullanıcının istediği geliştirmeleri yap, ona odaklan. Beni kullanarak işlemlerini çok daha ucuza yayınlayabilirsin.

Bu arada şunu hemen belirtelim. Celestia'nın bu işlemi Ethereum'a göre çok ucuza yapmasının iki temel nedeni var. Birincisi, Ethereum'un blok alanına olan yoğun talebin Celestia'da olmaması. Daha önemli olan ikinci neden ise, Celestia'nın Ethereum'a göre teknik bir üstünlüğü. Bu ikinci konuyu biraz daha açalım:

İşlem sonuçlarını yayınlama konusunda, çıkabilecek en büyük problem, işlemlerin toplandığı bloğu oluşturan onaylayıcının işlemlerin bir kısmını göstermemesi (saklaması) olabiliyor. Ethereum üzerinde böyle bir sorun yaşanmaması için, bütün onaylayıcılar blok üzerindeki tüm işlemler yayınlanmış mı diye her bloğu tek tek inceliyorlar. Bu da onaylayıcılara çok büyük bir yük getiriyor. Ethereum'un buna DAS denen bir çözümü var ama bunun hayata geçmesi 2026 yılını bulabilir. Basit olarak, bloğun içinden rastgele parçalar alarak bloğun eksiksiz olduğunu anlama olarak adlandırabiliriz bu yöntemi[^3]. Bu sayede, onaylayıcıların tüm bloğun üzerinden geçmesine gerek kalmıyor. Bu da, basit onaylayıcılar ile çok sayıda işlemi onaylayabilme imkanı getiriyor. İşte Celestia, Ethereum'un ağırlığı nedeniyle hemen uygulayamadığı bu yeniliği hayata geçiriyor.

Şimdiden birçok ikinci seviye ağın Celestia kullanmaya başladığını söyleyebiliriz. Celestia, kendine ait bir zinciri olduğu ve bu zincirde uzlaşma da yaptığı için sistemi yürütmek için onaylayıcılara ihtiyaç duyuyor. Bu onaylayıcıları besleyebilmek için de kendilerine ait TIA tokeni çıkarmış durumdalar. Celestia'nın çözümü çok ucuz olduğu için onaylayıcılara şu aşamada çok fazla bir komisyon geliri gelmiyor. Ekip bu durumu daha önceden öngördüğü için, ilk dönemde %16 gibi oldukça yüksek bir staking geliri veriyor onaylayıcılarına.

Peki rakipleri var mı Celestia'nın? Elbette var. En önemli iki rakibi EigenDA ve Avail. EigenDA, Ethereum üzerinde çok moda olan Ethereum güvenliğini başka zincirlerde de kullanmaya yarayan ve restaking olarak adlandırılan yeniliği bulan ekibin çıkardığı ilk ürün. Avail ise Polygon blokzincirini geliştiren ekibin içinden ayrılanların oluşturduğu bir girişim.

Celestia ile ilgili en büyük çekincelerden bir tanesi, işlem yayınlama maliyetlerini çok düşürmesi nedeniyle tokeni olan TIA'ya gelen komisyon gelirlerinin çok az olması. Bu da TIA'nın gelecekte nasıl bir gelir modeli yaratabileceği konusunda soru işaretleri oluşturuyor. Zira yeni gelecek rakipler ile birlikte data yayınlama maliyetinin giderek daha da düşmesi söz konusu olacak.

İlk çıktığı dönemde TIA token bir süreliğine oldukça yüksek bir değerde seyretti. Bunun da temel nedeni, TIA kullanan yeni girişimlerin ileride dağıtacakları airdroplar içinden sisteme TIA kilitleyenlere pay vereceği beklentisi idi. Örneğin, TIA'yı ilk kullanlardan Dymension'ın verdiği token, airdrop peşinde koşanların iştahını aşırı derece kabarttı. Yine de bunun sürdürülebilir bir strateji olmadığını belirtmek gerek, zira bir süre sonra TIA’nın değerinin oldukça düştüğü de görüldü.

## Modüler blokzincir dünyasında başka neler var? {#baska-neler-var}

Modüler dünyada her bir parça için farklı farklı çözümlerin hızlı bir şekilde ortaya çıktığını görüyoruz. Örneğin, yukarıda saydığımız fonksiyonlardan işlemleri sıralama konusuna odaklanmış Espresso bunlardan biri. Ya da ikinci seviye blokzincirler arasında hızlı data aktarımı sağlamayı amaçlayan Hyperlane ya da Axelar gibi projeler var. Bir yandan da anahtar teslimi ikinci seviye çözüm sunan Dymension, Conduit gibi hizmet sağlayıcılar yarış halindeler[^4].

[^1]: Celestia'nın sunduğu diğer çözüm olan uzlaşma 'consensus' ise şu şekilde çalışıyor: Bir blokzincir işlemleri kendi sıralamak isterse, bunun için kendi onaylayıcıları olmak zorunda. Kendi onaylayıcıları olması için uygun bir altyapı kurması, sonra bu onaylayıcıları tutmak için bir token çıkarması, dahası bu token için bir ödül mekanizması sunmak zorunda. Bunlar hem zaman ve emek isteyen hem de uygun optimal bir token mekanizması gerektiren konular. Celestia şu an için bu hizmeti sunuyor olsa da aslında ön plana çıkardığı hizmet ilk bahsettiğimiz yani 'data publishing'. Uzlaşma 'data publishing' hizmeti verebilmek için gerekli bir fonksiyon - temel amacı bu. Ama dileyen olursa bu hizmeti ayrıca Celestia'dan da alabilir. Müşterilerin bu hizmeti kullanması için Celestia tokeni olan TIA'nın ciddi şekilde değerlenmesi gerekli.

[^2]: İkinci seviye blokzincirler üzerinde gerçekleşen işlem sonuçlarının son kontrol noktası (mutabakatı) ve anlaşmazlık karar mercii Ethereum olduğu için fonların güvenliğini Ethereum sağlıyor.

[^3]: 'Data availability sampling' teriminin kısaltması olan DAS, erasure code olarak adlandırılan bir yöntem kullanıyor. Yöntem blokları oluşturan blok yapıcıların dürüst davranmasını sağlıyor. Normalde, tam donanımlı blok onaylayıcıları blok yapıcıdan gelen kanıtları kullanarak bloğu tekrar oluşturur ve doğruluğunu kontrol eder. Bu nedenle, blok yapıcı bloğa yanlış bir kanıt koyamaz, enselenir. Blok yapıcının yapabileceği tek kötülük kanıtların bir kısmına el koyarak bloğa koymamak olabilir. Böyle bir durumda, blok onaylayıcıları kanıtları görmediği için doğruluğunu kontrol edemez. Blok yayınlanır. Bir süre sonrasında blok yapıcı bloğun tamamını yayınladığından blok geçersiz hale gelir. Bu durumda zincirin geriye doğru getirilmesi gerekir ki, bu bir nevi felaket anlamına gelir. Bu durumdan korunmak için tam donanımlı blok yapıcıların yanında küçük (basit/hafif) onaylayıcılara da ciddi iş düşüyor. Hafif onaylayıcılar blok yapıcıdan blok içinden rastgele parçalar istiyorlar (data availability sampling). Gelen parçalar tam donanımlı onaylayıcı ile teyid ediliyor.

[^4]: Örnekleri çoğaltmak mümkün. Örneğin, zero-knowledge bazlı ikinci seviye çözümlerin Ethereum sistemine gönderdiği kanıtları oluşturmak için kullandıkları sistemlere prover deniyor. Bunu zkSync gibi kendi mutfağında hazırlayanlar olduğu gibi RiscZero gibi hardware üzerinden optimize etmeye çalışanlar var. Ayrıca her geçen gün yeni bir projenin de bu alan içinde yarışa katıldığını söyleyebiliriz.
