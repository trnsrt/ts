---
layout: post
title:  "Peki Bitcoin şifrelemesi nasıl çalışıyor?"
date:   2018-04-26 16:25:45 +0300
categories: Genel
---

Önceki iki yazımızda, önce merkezi olmayan sistemlerin çalışmasında temel unsur olan [**"şifreleme"**'nin neden önemli olduğunu](http://ademimerkezi.com/genel/2018/04/25/sifreleme-ne-demek-neden-onemli.html), sonra da Şifreleme'nin temel taşları olan [Öğütme (hashing), Özel Anahtar, Genel Anahtar, Şifreleme (Encryption)](http://ademimerkezi.com/genel/2018/04/26/sifreleme-mi-cok-karisik-degil-mi.html)'ye daha detaylı bakmıştık. 

Şimdi de dilerseniz, bütün bu kavramlar Bitcoin içerisinde nasıl hayata geçirilmiş ona bakalım. Bir nevi Bitcoin'in sırrını çözelim :) 


### Peki Bitcoin şifrelemesi nasıl çalışıyor?

Bitcoin (ve diğer benzer Blockchain sistemleri) önceki yazıda yazdığımız her iki kavramı ([öğütme ve şifreleme](http://ademimerkezi.com/genel/2018/04/26/sifreleme-mi-cok-karisik-degil-mi.html)) kullanarak kendi sistemlerini otomatik güvenli hale getiriyorlar (ya da tek bir kişiye duyulan güven ihtiyacını sıfıra indiriyorlar). 

#### Şifrele ki senden geldiğini anlasınlar

Önce şifreleme kısmına bakalım. Efendim, biliyorsunuz Blockchain sistemi bir dijital varlığın bir kimseden diğerine geçmesini sağlıyor. 

Varsayalım benim bir dijital varlığım, örneğin 1 Bitcoin'im var. Öncelikle, demiştik ki, bütün Blockchain işlemleri aynı şekilde tüm makineler tarafından tutuluyor. Dolayısıyla sistemdeki bütün makineler bu 1 Bitcoin'in bende olduğunu biliyor (o paraya nasıl sahip olduğum ise aşağıda anlatacağımız işlem sonucu daha netlik kazanacak). 

Şimdi ben bu parayı Ayşe'ye göndereceğim. Sistem üzerindeki makinelere diyorum ki "Ey ahali, ben 1 Bitcoin'imi Ayşe'ye gönderiyorum". Sistemde "ben" diye bahsettiğim bana ait bir adres. Ayşe de aynı şekilde bir adres. Dolayısı ile diyorum ki, "Ben, bu adresin sahibi kişi şu adrese bu kadar parayı gönderiyorum". Sistem üzerinden görülenler: bana ait hesap numarası, karşı tarafa ait hesap numarası ve ne kadar para gönderildiği. 

Merak ediyorsanız nasıl bir şeydir bu diye, işte bir örnek aşağıda: Bunu da kaydedip internet üzerinde [yayınlıyorlar](https://blockchain.info/block/0000000000000000001c2fa26ad4d4850fe94e688cfccf812c4fbe6d245761eb)


&nbsp;

| ![Transaction_Bitcoin_Block _519273.png](/assets/Transaction_Bitcoin_Block_519273.png) | 
|:--:| 
| *Bitcoin İşlem Örneği* |

&nbsp;

Yukarıdaki işlemi yazarken aslında iki küçük ekleme yapıyorum işleme. Birincisi, işlemi sisteme kendi Özel Anahtarım ile kaydediyorum. Böylece herkes bana ait olduğunu anlıyor bu paranın. İkincisi de, Ayşe'nin Genel Anahtarını da kaydediyorum. Böylece paranın Ayşe'ye gittiğini de anlıyor herkes. Ve bu parayı sadece Ayşe kullanabilir, çünkü bu Genel Anahtara karşılık gelen Özel Anahtar sadece Ayşe'de var. 

Eğer Ayşe bu parayı bir gün Mehmet'e göndermek isterse, benzer şekilde kendi Özel Anahtarı'nı kullandığında sistem bakacak "Hah tamam bu para zamanından Ayşe'nin Genel Anahtarı kullanılarak gönderilmişti, yani Ayşe'nin malı, şimdi Ayşe Özel Anahtarını kullanarak bu malın kendi sahipliğini ve Mehmet'in Genel Anahtarını kullanarak bu sahipliği Mehmet'e geçirdiğini söylüyor, o zaman yapalım bu transferi" diyecek. 

Şimdiye kadar (2009 yılındaki başlangıcından beri) Bitcoin üzerinde yapılmış bütün transferler kayıtlı ve yukarıdaki gibi görülebiliyor. Yani aslında işlemlerin hepsi şeffaf - hem de en başından beri. Yani Ayşe'ye gönderdiğim parayı da ben birinden aldım. Bu kişi de bir başkasından. Böyle böyle 2009 yılına kadar gidebilirsiniz. Peki ya en başında ne olmuştu? Bu kadar Bitcoin nasıl çıktı ortaya? Şimdi ona da bakalım: 

#### Öğüt ki, sonsuza kadar kaydedilsin

Hatırlar mısınız, önceki bir yazımızda şunu demiştik: "Blockchain sisteminde yükü çeken makinelerin bu yaptıkları işlemleri kayıt etme, daha sonra da teyit etme işlemi sonucu aldıkları ödüle (ya da lotaryaya) Bitcoin deniyor. Neden lotarya deniyor? Zira, bu on dakikada bir yapılan teyit işlemi aslında çok zor bir bulmaca. Bir nevi Sudoku oyunu gibi düşünün"

Şimdi dilerseniz bu bulmaca konusunu biraz daha açalım. Ortada tabii ki bir bulmaca yok ama bir öğütme işlemi var. Aynı yukarıda olduğu gibi "girdi" ve "çıktı" kısmı olan bir SHA şifrelemesi. 

Girdinin (input) iki parçası var 
- Belli bir süre içinde gerçekleşen tüm işlemlerin bir dökümü 
- Bir de bir sayı

Çıktı (Output) ise yukarıdaki gibi 64 karakterli bir şifre. 

Sistem söyle çalışıyor. 
1. Her 10 dakikada bir Bitcoin ile yapılan bütün işlemler bir araya toplanıyor ve makinelere gönderiliyor

![transactions-v3.png](/assets/transactions-v3.png)


2. Sonra sistem bütün makinelere şunu söylüyor: *"Ey makineler, işlemlerin toplam [dökümü](https://blockchain.info/block/0000000000000000001c2fa26ad4d4850fe94e688cfccf812c4fbe6d245761eb) elinize geçti, şimdi bu işlem dökümünü alın yanına öyle bir sayı ekleyin ki, öğütmeye koyduğunuzda çıkan çıktı (output) beş tane sıfır ile başlasın"*

3. Makineler bu çıktıyı alıyor ve sırayla rakamları denemeye başlıyorlar. Önce 1 ekliyor, çıkan sonuca bakıyor, 


![transaction1-v1.png](/assets/transaction1-v1.png)

yok olmadı, "370ff8b0..." ile başlayan bir output verdi. 

Sonra 2 ekliyor, yine bakıyor:


![transaction2-v1.png](/assets/transaction2-v1.png)


bu sefer "58ed8d94..." diye başlayan bir sayı verdi... Yine olmadı... 

Böyle böyle sırayla tüm sayılar deneniyor. Ta ki bir sayı (diyelim "25264") bize "00000..." ile başlayan bir sonuç verene kadar!

![transaction3-v1.png](/assets/transaction3-v1.png)


4. "00000..." ile başlayan sonucu ilk bulan makine "Buldum!" diyerek bu sonuca ulaştıran sayıyı ("25264") diğer makinelere haber veriyor. 

5. Sonucu gören makineler, işlem dökümünü 25264 sayısı ile birlikte şifreye sokuyorlar, bakıyorlar hakikaten çıkan sonuç "00000..." ile başlıyor, "Tamam" diyorlar, "Sonuç doğru" ve bir sonraki 10 dakika için yapılan işlemlere geçiyorlar. 
6. 25264 rakamını bulan makine işte bu ödülü (şu anda 12.5 Bitcoin yani 100,000 ABD Doları civari bir rakam) kazanıyor!

İşte bu kadar. Yukarıda anlatılanları görsel olarak izlemek isterseniz, aşağıdaki İngilizce videoyu hararetle tavsiye ederim. Aklınıza yatmayan her konu basit bir şekilde özetlenmiş. 


&nbsp;

<iframe width="560" height="315" src="https://www.youtube.com/embed/_160oMzblY8" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

&nbsp;

Yukarıdaki süreç her 10 dakikada bir tekrar ediyor ve her 10 dakikada bir 12.5 Bitcoin yaratılarak, sonucu bulan makineye veriliyor yani sisteme sokuluyor (buna İngilizce "mining" deniyor). İşte yukarıda bahsettiğimiz birbirimize transfer edilen Bitcoin'ler bu şekide yaratılıyor. Şu ana kadar (Nisan 2017 itibariyle) 17 Milyon Bitcoin yaratıldı. Önümüzdeki 100 yıl boyunca yaklaşık 4 milyon Bitcoin daha girecek sisteme ve orada 21 Milyon'da duracak piyasadaki miktar. 

Nasıl oldu da 9 yılda 17 Milyon yaratılırken bundan sonraki 100 yılda 4 Milyon'a düşecek derseniz, Bitcoin yaratıcıları para enflasyona yenik düşmesin diye her dört yılda bir verilen ödülü yarıya düşürüyorlar. İlk dört yıl 10 dakikada bir 50 Bitcoin verilirken, sonra bu 25'e düştü, şu an 12.5'da, 2021'de 6.25'e inecek. 

Peki bu madenciler bu ödül ile yaşıyorlar, ödül miktarı düşerse madencilik yapmayı bırakmazlar mı diye akla bir soru gelebilir. Olabilir tabii ama bu yeni para yaratımı ile ilgili bir konu. Madenciler bir de aynı zamanda, yapılan transferler üzerinden bir komisyon almaya devam ediyorlar. Eğer Bitcoin kişiler arası para transferinde sık kullanılmaya devam ederse ya da değeri şimdiki gibi yüksek olursa bir sorun olmaz. Çok düşerse o zaman bir kısım madenci sahneden çekilir, kalanlara pastadan daha büyük bir dilim düşer ve onlar çalışmaya devam ederler. 

### Bu kadar mı?

Evet, aslında işin özü bu kadar basit. Genel Anahtar aracılığı ile zamanında bana gönderilmiş olan bir varlığı, Özel Anahtarımı kullanarak şifreleyip bir başkasına gönderiyorum. Sistem de bu işlemleri 10 dakikada bir toplayıp öğütüp bir paket haline getiriyor. Şifrelemeyi kullanarak bana ait olduğunu kanıtladığım bir dijital varlığı öğütücü sayesinde bir başkasına kati olarak transfer ediyorum - bunun için de hiç kimsenin onay vermesine ihtiyaç duymuyorum. 

Para örneğinden yola çıktık ama tekrar edelim. Dijital olarak bana ait olan her tür varlık ve bilgiyi bu şekilde bir başkasına transfer edebilirim bu teknoloji ile. Seçenekler ve ihtimaller sınırsız - gerisi hayal gücünüze kalmış...  

