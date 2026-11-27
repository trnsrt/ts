---
layout: book-section
kind: section
title: "Modüler ve monoblok çözümler – Sorularla Web3"
heading: "Modüler ve monoblok çözümler"
chapter: 2
chapter_title: "Web3 Ekonomisinin Yapı Taşları"
order: 203
permalink: /Sorularla_Web3/bolum-2/moduler-ve-monoblok-cozumler/
description: "Blokzincir altyapıları konusunda en çok konuşulan ve üzerine kafa yorulan konulardan biri monoblok ve modüler blokzincir yapıları."
---

Blokzincir altyapıları konusunda en çok konuşulan ve üzerine kafa yorulan konulardan biri monoblok ve modüler blokzincir yapıları. Ne demek, ne işe yarar, gelin hep birlikte bakalım.

## Blokzincir üzerindeki uygulamaların uyumu {#blokzincir-uzerindeki-uygulamalarin-uyumu}

Web3 dünyasının klasik dünyaya göre en önemli farklarından biri, oluşan standartlar sayesinde kullanıcıya hizmet veren farklı oyuncuların birbirleri ile uyumlu (ahenk içinde) çalışabilmeleri. Gelin biraz daha açalım bu cümleyi:

Klasik dünyada, her bir girişim son kullanıcıya vereceği hizmeti (ya da ürünü) önce kurgular, sonra bazı kısımlarını geliştirir, bazılarını dışarıdan alır, en sonunda da bütün parçaları tek tek bir araya getirir ve kullanıcıya sunar. Bu durumun artısı kullanıcıya rahatlık ve kolaylık sağlaması. Temel eksisi ise, kullanıcının sadece hizmet verenin sunduğu paket ile yetinmek zorunda kalması.

Web3 dünyasında ise durum farklı. Bu dünyada kullanıcı hizmeti (ya da ürünü) oluşturan her bir parçayı kendi seçebiliyor. Web3 dünyasındaki farklı girişimlerin ürettiği her bir parça, blokzincir üzerindeki standartlara uyarak birbirleri ile uyum içinde çalışabiliyor. Bunun temel avantajı, bir yanda parçaları geliştirenler arasında yaşanan rekabet diğer yanda tek bir parça üzerinde uzmanlaşmanın getirdiği inovasyon hızı. Bu dünyada girişimler sadece tek bir sorun ile uğraşıyorlar, diğer sorunları farklı girişimler çözdüğü için hazır çözümleri kullanmak kendilerine zaman ve hız kazandırıyor.

Uygulamalar parça parça birbirleri ile uyumlu çalışıyorlar, çok güzel. Peki ya bu uygulamalara ev sahipliği yapan blokzincir altyapılarını da aynı şekilde parçalara bölerek daha rekabetçi ve hızlı hale getirebilir miyiz?

Konuya aşina olmayanlar için bu soru başta garip gelebilir. Neden blokzincir altyapısını parçalara bölmek zorunda olalım ki? Bu soruyu hakkıyla cevaplamak için blokzincirin kısıtlarını anlamamız gerek. Zira ilk bakışta biz son kullanıcıları direkt olarak ilgilendirmiyor gibi görünen bu sorun, aslında işlem ücreti olarak ödenen paranın artması nedeniyle direkt cebimizi de etkiliyor.

### Blokzincirlerin kısıtları {#blokzincirlerin-kisitlari}

Blokzincirlerin temel işlevini kişiler arasında yapılan işlemlerin geri döndürülemez (değiştirilemez) bir biçimde kaydedilmesi olarak tanımlayabiliriz. Bunu gerçekleştirmenin yolu bu kayıt defterini tutan makinelerin sayısını olabildiğince çok, bulundukları yerleri de olabildiğince dağıtık yapmak, ki bu sayede sistemi ele geçirmek imkansız (ya da çok pahalı) hale gelsin.

Aslında işe teknoloji perspektifinden bakarsanız, merkezi sistemler tek bir yerden yönetildikleri için blokzincire göre çok daha hızlı ve üstündürler. Merkezi sistemlerin zayıf karnı, bu tek yerin, dışarıdan gelecek saldırı ya da baskılara karşı koymakta zorlanması. Özellikle teknik saldırılara karşı sistemi ‘kurşun geçirmez’ yapabilirsiniz ama sistemi politik ya da toplumsal baskılara karşı koruyabilmek teknik konulara göre çok daha karmaşık ve çözümü zor.

Blokzincirin dış baskılardan etkilenmemesi için sistemi yürüten makineleri olabildiğince dağıtık tutmanız gerekir. Bunun için de blokzincirin kayıt defterini küçük tutmak zorundasınız. Bunu yapmazsanız, sistemi ancak kapasitesi yüksek makineler yürütebilir, bu da makine sayısının azalması (yani sistemin merkezileşmesi) sonucunu doğurur ve güvenlik riski ortaya çıkar.

Blokzincirlerin temel olarak sattıkları ‘şey’ bu blok alanıdır. Kayıt defterini küçük tuttuğunuzda ise, yüksek talebi karşılamakta zorluk çeker hale gelirsiniz. Blokzincirler (ideal olarak) yüksek talep geldiğinde durmazlar[^1], onun yerine işlem ücretlerini artırırlar ki, işi acil olmayanlar beklesin. Bu durum, bir noktaya kadar makul görünse de, yüksek işlem ücretleri kullanıcıları bir noktadan sonra alternatif arayışlara doğru itebilir.

### En büyük blokzincirlerden Ethereum’un sıkıntıları {#en-buyuk-blokzincirlerden-ethereumun-sikintilari}

İşte Ethereum uzun süredir böyle bir sorun ile karşı karşıya. 2020-21 yılları arasında DeFi ve NFT alanındaki yoğun talep nedeniyle Ethereum işlem ücretleri inanılmaz derecede arttı. Ethereum geliştiricileri bu soruna hızlı bir çözüm bulmakta yetersiz kaldılar.

Ethereum’u geliştiren topluluk başlangıçta blokzinciri dikey olarak parçalara bölerek talebi karşılamak gibi bir hayale sahipti. (Bunu Ethereum bir ada ise, aynı işi yapan küçük küçük adacıklar olarak düşünebilirsiniz; bir adada DeFi bir başka adada NFT işlemlerinin yapılması gibi). Sonrasında bunun havadaki bir uçağın motorunu seyir halindeyken parçalara bölmekten daha zor bir iş olduğunu anlayan geliştiriciler, strateji değişikliğine gitmek zorunda kaldılar. Bu değişiklik sonrası, sistemleri üzerinde yük oluşturan parçaları dışarı vermeye (bir nevi ‘outsource’ etmeye) başladılar.

## Blokzincirin parçaları neler? {#blokzincirin-parcalari-neler}

Yukarıda yazdığımız gibi blokzincirin temel özelliği bir kayıt defteri olması. Blokzincirin kayıt tutarken gerçekleştirdiği dört temel fonksiyon var. Bu dört temel parçayı şu şekilde özetleyebiliriz:

- **İşlemi gerçekleştirmek (execution)**: Aklınıza gelebilecek her tür işlemin yapılması. Bu; bir kişiye varlık transferinden merkeziyetsiz bir borsada token alım-satımına, ya da NFT satın almaya kadar her tür işlemin bizzat yerine getirilmesi. Bu genelde şu şekilde oluyor: Herhangi bir uygulama yukarıdan bahsedilen işlemleri gerçekleştirdiğinde, sistemi işleten zincire yaptığı işlemler ve sonuçlarını bildiriyor. Biz son kullanıcılar için en tanıdık blokzincir fonksiyonu.
- **Yapılan işlemin onaylanması (consensus)**ı: İşlem yapmak için verilen emir bir makine tarafından tüm sisteme anons ediliyor. Bunun hemen arkasından bu işlemin geçerli bir işlem olup olmadığının diğer tüm makineler tarafından onaylanması gerekiyor. Yani makineler “evet bu işlem geçerli bir işlemdir, gelen işlemler şu sırada gerçekleşmiştir ve bu işlemler sonucu her bir hesapta şu kadar varlık bulunmaktadır” şeklinde aralarında anlaşıyorlar.
- **İşlem sonuçlarının bloğa yazılıp kesinleşmesi (settlement)**: Gerçekleşen işlemler havuzdan alınıp sıraya kondu. Şimdi sıra bunun sonucu olarak oluşan son durumun blokzincire yazılmasına geliyor. Yani siz birine para gönderdiğinizde sizin hesabınızın o para kadar azalması karşı tarafın hesabının ise aynı miktarda artması gerekiyor. Bir önceki adımda, makineler (madenciler ya da onaylayıcılar) hangi işlemin hangi sıra ile gerçekleşeceği konusunda uzlaşıp blokları oluşturduktan sonra hesapların son halini (bakiyeleri) blokzincir üzerinde kesinleştiriyor. Bu noktadan sonra artık geri dönüş yok.
- **İşlem sonuçlarının tüm sisteme anons edilmesi (data publishing)**: İşlemler yapıldı, sıraya sokuldu, bloğun içine yerleştirildi ve blokzincire işlendi (yani para el değiştirdi); şimdi sıra bunun tüm sisteme bildirilmesine geldi. Bu önemli bir konu, zira uygulamaların bundan sonra yapılacak işlemler için hesapların son/güncel durumunu bilmesi gerekiyor[^2].

## Monoblok ve modüler zincirler {#monoblok-ve-moduler-zincirler}

Blokzincirin yukarıda saydığımız fonksiyonlarının nasıl gerçekleştirileceği konusunda iki farklı ekol var. Bunlardan bir tanesi yukarıda saydığımız bütün fonksiyonların tek bir elden yapılması (aynı Apple ekosistemi gibi), diğeri ise her bir işlemin farklı farklı oyuncular tarafından yürütülmesi (bir nevi Android sistemler gibi).

Bitcoin ve Solana’nın başını çektiği ağlar, monoblok yapı dediğimiz birinci ekolü benimsediler. Bitcoin için bu yolu seçmek kolaydı, zira Bitcoin özünde tek bir uygulamaya bağlı bir ağ (İngilizcesi ‘application specific’). Bahsettiğimiz tek uygulama da Bitcoin parası olan BTC. Bitcoin üzerine uygulama kurmak mümkün değil, çünkü akıllı kontrat desteği yok[^3]. Bu nedenle, Bitcoin kendini basit tutarak ölçeklenme yarışına girmemeyi tercih etti[^4].

Solana ise, çok daha genele hitap eden, üzerinde akıllı kontrat çalışan bir ağ. Onlar ise, ölçeklenme problemini blokları büyüterek çözdüler. Bu durumun yan etkisi, sistemi yürüten makinelerin yüksek kapasite ihtiyacı, bunu karşılayacak makine sayısı az olduğu için sistemin merkezileşme riski.

Yelpazenin öbür ucunda ise, yukarıda saydığımız fonksiyonları farklı farklı yapan yerler var. Örneğin, son birkaç yıldır en çok konuşulan konu Ethereum üzerine kurulu ikinci seviye çözümler. Şimdi gelin onlara bakalım.

[^1]: Duran blokzincirler yok mu? Var tabii. Bu alanda sabıkası olan zincirler var ama onların henüz yeterince olgunlaşmamış olduğunu söyleyerek şimdilik istisna olarak görüp konumuz dışında bırakıyoruz.

[^2]: ‘Data publishing’ olarak adlandırılan bu özellik, kimi zaman ‘data availability’ olarak yanlış adlandırılabiliyor. ‘Data availability’ geçmiş tüm işlemlerin saklanması olarak düşünülebilir (bir başka deyişle İngilizcede data storage olarak adlandırılan kavram) - onun blokzincir üzerindeki tüm makinelerde saklanmasına gerek yok. Birkaç makine bütün geçmişi (ya da arşivi) saklayabilir.

[^3]: Basitleştirmek için bu şekilde anlatıyorum, teknik arkadaşlar hemen çullanmasın. Aslında kastedilen, ‘script’ dediğimiz kodların çok kısıtlı olması. Taproot geliştirmesi ile birlikte özellikle Ordinals üzerinden bu kısıt bir parça kırıldı ama hâlâ yeterli sayılmaz. Bitcoin üzerine ikinci seviye çözümler de geliştirilmeye çalışıyor ama bu çözümlerin tam layıkıyla çalışabilmesi için Bitcoin üzerinde yeni güncellemelerin gelmesi (bir nevi soft fork olması) gerekiyor ki bu tip güncellemeler Bitcoin’e üç-dört yılda bir ancak geliyor. Bu güncelleme gelene kadar Bitcoin üzerinde akıllı kontrat kullanımı için bir ara çözüm olan BitVM geliştiriliyor. İlgilenenler bu alanda çalışan Türk bir ekibin ([Chainway](https://chainway.xyz/)) kurduğu [Citrea](https://citrea.xyz/) çözümünü inceleyebilirler.

[^4]: Bunun uzun vadede sürdürülebilir bir strateji olup olmadığı konusunda tartışmalar mevcut. Bu haliyle Bitcoin sistemini sürdüren madencilerin ana gelir kaynağı yeni blok oluşturma sonrası verilen madencilik ödülleri. Bu ödül ise her dört yılda bir yarılanıyor. Madencilerin bir diğer gelir kalemi olan işlem ücretleri, Bitcoin sadece para transferi için kullanılırsa çok az kalıyor. Eğer Bitcoin üzerine yeni sistemler (örneğin DeFi kullanan ikinci seviye çözümler) olursa, o zaman işlem ücretleri ve madencilerin gelirleri de artacak.
