---
layout: post
title:  "Modüler ve monoblok zinciler - 1"
date:   2024-03-07 18:17:56 +0300
categories: Genel
tags: Yazılar, DeFi
---

Blokzincir altyapıları konusunda en çok konuşulan ve üzerine kafa yorulan konulardan biri monoblok ve modüler blokzincir yapıları. Ne demek, ne işe yarar, gelin hep birlikte bakalım. 

### Blokzincir üzerindeki uygulamaların uyumu
Web3 dünyasının klasik dünyaya göre en önemli farklarından biri, oluşan standartlar sayesinde kullanıcıya hizmet veren farklı oyuncuların birbirleri ile uyumlu (ahenk içinde) çalışabilmeleri. Gelin biraz daha açalım bu cümleyi:

Klasik dünyada, her bir girişim son kullanıcıya vereceği hizmeti (ya da ürünü) önce kurgular, sonra bazı kısımlarını geliştirir, bazılarını dışarıdan alır, en sonunda da bütün parçaları tek tek bir araya getirir ve kullanıcıya sunar. Bu durumun artısı kullanıcıya rahatlık ve kolaylık sağlaması. Temel eksisi ise, kullanıcının sadece hizmet verenin sunduğu paket ile yetinmek zorunda kalması.

Web3 dünyasında ise durum farklı. Bu dünyada kullanıcı hizmeti (ya da ürünü) oluşturan her bir parçayı kendi seçebiliyor. Web3 dünyasındaki farklı girişimlerin ürettiği her bir parça, blokzincir üzerindeki standartlara uyarak birbirleri ile uyum içinde çalışabiliyor. Bunun temel avantajı, bir yanda parçaları geliştirenler arasında yaşanan rekabet diğer yanda tek bir parça üzerinde uzmanlaşmanın getirdiği inovasyon hızı. Bu dünyada girişimler sadece tek bir sorun ile uğraşıyorlar, diğer sorunları farklı girişimler çözdüğü için hazır çözümleri kullanmak kendilerine zaman ve hız kazandırıyor.

Uygulamalar parça parça birbirleri ile uyumlu çalışıyorlar, çok güzel. Peki ya bu uygulamalara ev sahipliği yapan blokzincir altyapılarını da aynı şekilde parçalara bölerek daha rekabetçi ve hızlı hale getirebilir miyiz? 

Konuya aşina olmayanlar için bu soru başta garip gelebilir. Neden blokzincir altyapısını parçalara bölmek zorunda olalım ki? Bu soruyu hakkıyla cevaplamak için blokzincirin kısıtlarını anlamamız gerek. Zira ilk bakışta biz son kullanıcıları direkt olarak ilgilendirmiyor gibi görünen bu sorun, aslında cebimizden işlem ücreti olarak çıkan paranın artması nedeniyle direkt cebimizi de etkiliyor. 

#### Blokzincirlerin kısıtları

Blokzincirlerin temel işlevini kişiler arasında yapılan işlemlerin geri döndürülemez (değiştirilemez) bir biçimde kaydedilmesi olarak tanımlayabiliriz. İşlemleri geri döndürülemez şekilde gerçekleştirebilmenin temel yollarından biri, bu kayıt defterini tutan makinelerin sayısını olabildiğince çok, bulundukları yerleri de olabildiğince dağıtık yapmak, ki bu sayede sistemi ele geçirmek imkansız (ya da çok pahalı) hale gelsin.

Aslına bakarsanız, merkezi sistemler tek bir yerden yönetildikleri için blokzincire göre çok daha hızlı ve üstündürler. Bu merkezi sistemlerin zayıf karnı ise, bu tek yerin, dışarıdan gelecek saldırı ya da baskılara karşı koyamaması.  Özellikle saldırılara karşı sistemi 'kurşun geçirmez' yapabilirsiniz ama sistemi politik ya da toplumsal baskılara karşı koruyabilmek teknik konulara göre çok daha karmaşık ve çözümü zor. Neticede sistemleri yönetenler de birer insan.

Olabildiğince çok makine kullanmak için, blokzincirin kayıt defterini küçük tutmak zorundasınız. Bunu yapmazsanız, sistemi ancak kapasitesi yüksek makineler yürütebilir, bu da makine sayısının azalması (yani sistemin merkezileşmesine) sonucunu doğurur ve güvenlik riski doğar. 

Blokzincirlerin temel olarak sattıkları 'şey' bu blok alanıdır. Kayıt defterini küçük tuttuğunuzda ise, yüksek talebi karşılamakta zorluk çeker hale gelirsiniz. Blokzincirler (ideal olarak) yüksek talep geldiğinde durmazlar[^6], onun yerine işlem ücretlerini artırırlar ki, işi acil olmayanlar beklesin. Bu durum, bir noktaya kadar makul görünse de, yüksek işlem ücretleri kullanıcıları bir noktadan sonra alternatif arayışlara doğru itebilir.  

#### En büyük blokzincirlerden Ethereum'un sıkıntıları

İşte Ethereum uzun süredir böyle bir sorun ile karşı karşıya. 2020-21 yılları arasında DeFi ve NFT alanındaki yoğun talep nedeniyle Ethereum işlem ücretleri inanılmaz derecede arttı. Ethereum geliştiricileri bu soruna hızlı bir çözüm bulmakta yetersiz kaldılar. 

Ethereum'u geliştiren topluluk başlangıçta blokzinciri dikey olarak parçalara bölerek talebi karşılamak gibi bir hayale sahipti. (Bunu Ethereum bir ada ise, aynı işi yapan küçük küçük adacıklar olarak düşünebilirsiniz; bir adada DeFi bir başka adada NFT işlemlerinin yapılması gibi). Sonrasında bunun havadaki bir uçağın motorunu seyir halindeyken parçalara bölmekten daha zor bir iş olduğunu anlayan geliştiriciler, strateji değişikliğine gitmek zorunda kaldılar. Bu değişiklik sonrası, sistemleri üzerinde yük oluşturan parçaları dışarı vermeye (bir nevi 'outsource' etmeye) başladılar. 

### Blokzincirin parçaları neler?
Yukarıda yazdığımız gibi blokzincirin temel özelliği bir kayıt defteri olması. Blokzincirin kayıt tutarken gerçekleştirdiği dört temel fonksiyon var. Bu dört temel parçayı şu şekilde özetleyebiliriz: 

- **İşlemi gerçekleştirmek (execution)**: Aklınıza gelebilecek her tür işlemin yapılması. Bu; bir kişiye varlık transferinden merkeziyetsiz bir borsada token alım-satımına, ya da NFT satın almaya kadar her tür işlemin bizzat yerine getirilmesi. Bu genelde şu şekilde oluyor: Herhangi bir uygulama yukarıdan bahsedilen işlemleri gerçekleştirdiğinde, sistemi işleten Biz son kullanıcılar için en tanıdık blokzincir fonksiyonu. 
- **Yapılan işlemi sıralamak (consensus)**: İşlem yapmak için emir verdiniz, çok güzel. Yapmak istediğiniz işlem hemen blokzincire yazılmıyor. Bir havuzda toplanıp sonra işleniyor. Toplama sırasında işlemlerin bir sıraya konması gerekiyor. Neden? Aynı anda iki kişi aynı işlemi yapmak isteyebilir. Bu durumda bunlardan daha yüksek işlem ücreti veren öne geçiyor. Ya da bir kişi aynı hesaptan iki işlem birden göndermek isteyebilir[^1]. İşte bu sorunları önlemek için makinelerin emirlerin hangi sırayla blokzincire işlenmesi gerektiği konusunda 'uzlaşması' gerekiyor. 
- **İşlem sonuçlarının bloğa yazılıp kesinleşmesi (settlement)**: Gerçekleşen işlemler havuzdan alınıp sıraya kondu. Şimdi sıra bunun sonucu olarak oluşan durumun blokzincire yazılmasına geliyor. Yani siz birine para gönderdiğinizde sizin hesabınızın o para kadar azalması karşı tarafın hesabının ise aynı miktarda artması gerekiyor. Bir önceki adımda, makineler (madenciler ya da onaylayıcılar) hangi işlemin hangi sıra ile gerçekleşeceği konusunda uzlaşıp blokları oluşturduktan sonra hesapların son hali blokzincir üzerinde kesinleştiriliyor.
- **İşlem sonuçlarının tüm sisteme anons edilmesi (data publishing)**: İşlemler yapıldı, sıraya kondu, bloğa kondu ve blokzincire işlendi (yani para el değiştirdi); şimdi sıra bunun tüm sisteme bildirilmesine geldi. Bu önemli bir konu, zira uygulamaların bundan sonra yapılacak işlemler için hesapların son/güncel durumunu bilmesi gerekiyor. [^2]

### Monoblok ve modüler zincirler
Blokzincirin yukarıda saydığımız fonksiyonlarının nasıl gerçekleştirileceği konusunda iki farklı ekol var. Bunlardan bir tanesi yukarıda saydığımız bütün fonksiyonların tek bir elden yapılması (aynı Apple ekosistemi gibi), diğeri ise her bir işlemin farklı farklı oyuncular tarafından yürütülmesi (bir nevi android sistemler gibi).

| ![zebras](/assets/zebra_real_lego.jpg)|
|:--:| 
| *Image by [Nel Botha](https://pixabay.com/users/nel_botha-nz-1267169/) (left) and [M W](https://pixabay.com/users/efraimstochter-12351/) (right) from [Pixabay](https://pixabay.com/)*|

Bitcoin ve Solana'nın başını çektiği ağlar, monoblok yapı dediğimiz birinci ekolu benimsediler. Bitcoin için bu yolu seçmek kolaydı, zira Bitcoin özünde tek bir uygulamaya bağlı bir ağ (ingilizcesi application specific). Bahsettiğimiz tek uygulama da Bitcoin parası olan BTC. Bitcoin üzerine uygulama kurmak mümkün değil, çünkü akıllı kontrat desteği yok[^3]. Bu nedenle, Bitcoin kendini basit tutarak ölçeklenme yoluna gitti[^7].

Solana ise, çok daha genele hitap eden, üzerinde akıllı kontrat çalışan bir ağ. Onlar ise, ölçeklenme problemini blokları büyüterek çözdüler. Bu durumun yan etkisi, sistemi yürüten makinelerin yüksek kapasite ihtiyacı, bunu karşılayacak makine sayısı az olduğu için sistemin merkezileşme riski. 

Yelpazenin öbür ucunda ise, yukarıda saydığımız fonksiyonları farklı farklı yapan yerler var. Örneğin, son birkaç yıldır en çok konuşulan konu Ethereum üzerine kurulu ikinci seviye çözümler. Bir sonraki yazımızda ikinci seviye çözümlere modülerlik açısından bakacağız. 

---

[^1]: Duran blokzincirler yok mu? Var tabii. Bu alanda sabıkası olan zincirler var ama onların henüz yeterince olgunlaşmamış olduğunu söyleyerek şimdilik istisna olarak görüp konumuz dışında bırakıyoruz.
[^2]: Meşhur 'çifte harcama' problemi, ingilizcesi double spending. Kişi aynı parayı A ve B kişine aynı anda göndermeye çalışabilir. Bunu yaptığında makinelerden bir kısmı A kişisine giden işlemi alır, kimileri ise B kişisine giden işlemi. Böyle bir durumda iki ayrı blok sisteme girer. Zaman içinde topluluk ya A kişine giden bloğun peşine takılır ya da B kişisine giden bloğun. Böylece konsensus oluşmuş olur.
[^3]: 'Data publishing' olarak adlandırılan bu özellik, kimi zaman 'data availability' olarak yanlış adlandırılabiliyor. 'Data availability' geçmiş tüm işlemlerin saklanması olarak düşünülebilir (bir başka deyişle ingilizcede data storage olarak adlandırılan kavram) - onun blokzincir üzerindeki tüm makinelerde saklanmasına gerek yok. Birkaç makine bütün geçmişi (ya da arşivi) saklayabilir.
[^4]: 4.	Basitleştirmek için bu şekilde anlatıyorum, teknik arkadaşlar hemen çullanmasın. Aslında kastedilen, 'script' dediğimiz kodların çok kısıtlı olması. Taproot geliştirmesi ile birlikte özellikle ordinals üzerinden bu kısıt bir parça kırıldı ama hâlâ yeterli sayılmaz. Bitcoin üzerine ikinci seviye çözümler de geliştirilmeye çalışıyor ama bu çözümlerin tam layıkıyla çalışabilmesi için Bitcoin üzerinde yeni güncellemelerin gelmesi (bir nevi soft fork olması) gerekiyor ki bu tip güncellemeler Bitcoin'e üç-dört yılda bir ancak geliyor. Bu güncelleme gelene kadar Bitcoin üzerinde akıllı kontrat kullanımı için bir ara çözüm olan BitVM geliştiriliyor. İlgilenenler bu alanda çalışan Türk bir ekibin (Chainway) kurduğu Citrea çözümünü inceleyebilirler.
