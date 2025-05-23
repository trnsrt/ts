---
layout: post
title:  "Web3 ve Yapay Zeka - I"
date:   2024-11-01 17:17:56 +0300
categories: Genel
tags: Yazılar, Web3
---

Bu yazımızda yapay zeka ile Web3’ün arasındaki ilişkiyi ve birbirlerini nasıl etkileyeceğini anlamaya çalışacağız[^1]. 

Yapay zeka (YZ) uzun süredir üzerinde çalışılan, yatırım yapılan ve geliştirilen bir alan. Kimi kaynaklar başlangıcını 1950’lere kadar [götürüyor](https://coderspace.io/blog/yapay-zekanin-tarihi-dunden-bugune-yapay-zeka/). Son zamanlarda çok konuşulan ‘genel yapay zeka’ üzerine çalışmalar[^2] ise yirmi yıldan fazla bir süredir devam ediyor. Başlangıçta yavaş seyreden bu gelişmeler, özellikle son yıllarda donanım alanındaki yaşanan gelişmeler sayesinde inanılmaz bir seviyeye geldi.

| ![web3-ai](/assets/web3_ai_800.jpg)|
|:--:| 
| *AI-Web3 relationship illustration generated by ChatGPT (OpenAI), 2024.*|

En basit haliyle yapay zekanın nasıl çalıştığına bir bakalım: 

### Yapay zeka nedir, nasıl çalışır?

Yapay zeka en basit haliyle “bizim ürettiğimiz çeşitli bilgi kaynaklarını bir araya getirip bize satan bir papağan” olarak tanımlanabilir. Bu papağanın en önemli özelliği bizim düşünce yapımızı taklit edebilmesi[^3]. Bu sayede sorduğumuz sorulara bir insan gibi cevap verebiliyor.

Yapay zekanın en büyük kaynağı internet. İnternet üzerindeki tüm bilgiler[^4] yapay zekaya yükleniyor[^5]. Toplanan tüm bilgiler önce temizleniyor ve makinelerin okuyabileceği bir hale getiriliyor. Makineler bu bilgileri alarak analiz ediyorlar[^6]. Son olarak, kullanıcının ona sorduğu soruların yanıtlarını  ‘tahmin ederek[^7]’ onunla konuşur gibi kullanıcıya sunuyorlar[^8].  

Burada ilginç birkaç nokta var. Öncelikle makineler nasıl analiz yapılacağını ‘öğrendikten’ sonra artık kendi kendilerine çalışabiliyorlar. Kullanıcıdan gelen geri bildirimler ile kendi kendilerini eğitiyorlar[^9]. Hatta verdikleri cevaplara nasıl ulaştıkları kimi zaman yapay zeka uzmanlarını bile hayrete düşürüyor.

İyi de nasıl bir ‘şey’ bu yapay zeka? Elle tutulur mu, gözle görülür mü? Gelin şimdi de yapay zeka dünyasının üzerindeki perdeyi hafifçe aralayıp içeriye göz atalım.

### Yapay zekanın katmanları 

Yapay zeka dediğimiz aslına bakarsanız altyapılardan uygulamalara kadar üst üste konarak bize hizmet veren bir ürün destesi. Bu haliyle daha önceki yazılarımızda bahsettiğimiz DeFi’nin destelerine benziyor. 

| ![ai-stack](/assets/ai-stack-a16z_800.jpg)|
|:--:| 
| *Yapay zeka teknoloji destesi. Kaynak: [az16 ai](https://a16z.com/who-owns-the-generative-ai-platform/)*|

Destenin en altında koyu lacivert renkli ‘altyapı katmanı’ var. Yapay zekanın yukarıda saydığımız tüm işlemleri yaparak bize istediğimiz sonucu anında verebilmesi için çok ciddi bir donanım ihtiyacı bulunuyor. Gerek işlemciler (çipler) gerekse bulut platformları bu ihtiyacı karşılıyor. İşte bu nedenle Nvidia gibi çip devlerinin hisse değerleri uçuyor. Amazon ve Microsoft’un sahip olduğu AWS ve Azure, kendi şirketlerinin en büyük kâr kaynakları haline geliyor. 

Bizim çok konuştuğumuz ChatGPT gibi yapay zeka modelleri ise bu altyapının üzerine konuşlandırılıyorlar. Yukarıdaki grafikte koyu mavi olarak gördüğünüz bu ‘orta katman’ işte bu yapay zeka modellerinin bulunduğu yer. Burada pek çok farklı model mevcut. ChatGPT gibi kapalı olanların yanında Microsoft’un Llama’sı gibi yarı-açık[^10] ya da Stable Diffusion gibi tam açık kaynak modeller de bulunmakta[^11].

En üst tarafta açık mavi ile gösterilen yerde ise son kullanıcı için yaratılmış ‘uygulama katmanı’ bulunuyor. Bu uygulamalar ChatGPT gibi modellerin üzerine inşa ediliyor[^12]. 

### Yapay zekanın göz kamaştıran gelişimi

Yapay zeka gözlerimizin önünde inanılmaz bir şekilde büyüyor. Biz kullanıcılar olarak özellikle ChatGPT’nin de etkisiyle yapay zekayı sadece kişisel asistan olarak kullanıyor olsak da, bu teknolojinin daha geniş anlamda iş dünyasına etkileri saymakla bitmez. 

Karşınızda yemeyen içmeyen, sadece ‘enerji harcayan’, gece gündüz çalışan ve şu an için bir üniversite öğrencisi, yakın zamanda ise bir doktoralı niteliğine sahip olacak bir ‘iş gücü’ var[^13].

| ![ai_capabilities](/assets/our-world-ai-capability_800.jpg)|
|:--:| 
| *Her bir alan içinde yapay zekanın ilk performansı \-100’e konulmuş. İnsan performansı ise baz alınarak sıfıra ayarlanmış. Yapay zeka 0 çizgisine geldiğinde insan performansına ulaşmış oluyor. Gördüğünüz gibi yapay zeka okuduğunu anlama, görüntü tanıma, dil anlama konularında insanları geçti. El yazısı ya da ses tanıma ile tahmini akıl yürütme konularında ise bizleri yakalamış durumda. Kaynak: [Our World in Data](https://ourworldindata.org/artificial-intelligence)*|

World Economic Forum, önümüzdeki on yılda YZ’nin Gayrisafi Milli Hasılaya etkisinin yıllık ortalama %0.5 ile %1.5 arasında olacağını [tahmin ediyor](https://www.weforum.org/agenda/2024/05/these-5-countries-are-leading-the-global-ai-race-heres-how-theyre-doing-it/)[^14]. Bu toplamda 1.2 trilyon ile 3.8 trilyon ABD doları bir büyüklük demek\!

Bunu bir de hızla gelişmekte olan robotlar ile birleştirin. Sunduğunuz hizmetin maliyetinden, kazandığınız gelire kadar her yönden sizi ciddi şekilde etkileyeceğini tahmin edebilirsiniz[^15].

### Teknoloji devlerinin yapay zeka yarışı

Teknoloji dünyasının devleri uzun zamandır yapay zekanın kendilerini nasıl etkileyeceğine kafa yoruyor ve ellerinde ne var ne yoksa bu alana yatırıyorlar. Aşağıda teknoloji dünyasında ‘mahşerin dört atlısı’ olan Microsoft, Amazon, Google ve Meta’nın son üç yılda yapay zeka alanında yaptığı yatırımlar var[^16].  Peki bu tabloda yer almayan Apple ile birlikte bu beş devin kenarda ‘nakit’ olarak bekleyen bir 400 milyar ABD Doları parası daha olduğunu söylesek? Sanırım bu alandaki devasa yatırım iştahının bir süre daha devam edeceğini az çok kestirebilirsiniz. 

| ![top_4_ai_spend](/assets/top4_ai_spend_800.jpg)|
|:--:| 
| *Her bir alan içinde yapay zekanın ilk performansı \-100’e konulmuş. İnsan performansı ise baz alınarak sıfıra ayarlanmış. Yapay zeka 0 çizgisine geldiğinde insan performansına ulaşmış oluyor. Gördüğünüz gibi yapay zeka okuduğunu anlama, görüntü tanıma, dil anlama konularında insanları geçti. El yazısı ya da ses tanıma ile tahmini akıl yürütme konularında ise bizleri yakalamış durumda. Kaynak: [Our World in Data](https://ourworldindata.org/artificial-intelligence)*|

Bu alana en büyük yatırımı yapanlar teknoloji devleri olunca akıllara şu soru geliyor: Acaba kullanıcıların Web2 dünyasında teknoloji devlerinin tekelleşmesinden dolayı yaşadığı sıkıntılar yapay zekada da tekrarlanacak mı? Acaba Web3’de olduğu gibi merkeziyetsiz çözümler bu tekelleşmeye karşı alternatif bir yol sunabilir mi?

### Arkası yarın

Bu yazımızda, yapay zeka dünyasına ufak bir pencere açtık. Gerekli yatırım ihtiyacının ancak teknoloji devleri tarafından karşılanabileceğini, bunun da Web2.0’da olduğu gibi bir tekelleşme yaratabileceğine değindik.

Web3 dünyasının merkeziyetsiz uygulamaları Web 2.0’daki tekelleşmeye karşı bir alternatif olarak ortaya çıkmıştı. Acaba merkeziyetsiz çözümler yapay zeka alanında da kullanıcılara benzer bir çıkış yolu sunabilirler mi? 

Önümüzdeki yazıda bu soruya cevap arayacağız.  

[^1]:  Küçük bir not: Yazımızın kapsamı yapay zekanın blokzincir ve merkeziyetsiz girişimler ile ilişkisi. Bu nedenle konuyu basitleştirmek adına yapay zekaya özel teknik kimi açıklamalar metnin içinde değil, dipnotlarda verildi.

[^2]:  Yapay zeka ilk olarak belli konularda uzmanlaşmış olarak çıktı. IBM’in satranç alanında uzmanlaşmış Deep Blue uygulaması gibi. Genel her konuda taleplere cevap veren yapay zeka uygulamaları (Artificial General Intelligence) ise uzman akranlarına göre daha yavaş ilerledi ama son yıllarda hız kazandı.  

[^3]:  Yapay zeka biz insanların kişi ve olayları ilişkilendirme (yani anlamlandırma) yeteneğini taklit ediyor.

[^4]:  Bu bilgiler yazı, resim, video her tür veriyi içeriyor. 

[^5]:  Kamuya açık bu bilgiler daha sonra özel veritabanlarında bulunan daha ‘gizli’ bilgiler ile destekleniyor.

[^6]:  Makinelerin yaptığı, kelimeler arasındaki ilişkileri ve beraber ne şekilde hangi sırayla kullanıldıklarını çıkarmak. ‘Tokenleştirme’ denen bu süreçte her bir kelime (ve alt kırılımları) bir birim olarak alınıyor. Buradaki kritik nokta, bu birimlerin kullanım sıklığı ve başka birimlerle ilişkilerine göre ağırlıklandırılması. Bu ağırlıklandırma sonucu trilyonlarca parametre ortaya çıkıyor. Örneğin ChatGPT’nin 1.8 Trilyon parametresi olduğu tahmin ediliyor

[^7]:  Yapay zeka, hazırlamış olduğu kelime ilişkilerinden çıkardığı haritaları kullanarak kullanıcının isteklerini cevaplıyor.

[^8]:  Yapay zekanın çıktıları olarak metin oluşturmak, görsel tanımak, bilgi bir araya getirmek gibi geniş bir yelpaze sayabilmek mümkün. Burada basitleştirmek adına ChatGPT’nin soru-cevap yöntemini anlattık. 

[^9]:  Hatırlarsınız, ChatGPT ilk çıktığında kullananlar “çok saçma cevaplar veriyor, ben itiraz edince de hemen kendini düzeltiyor” şeklinde yorumlarda bulunurlardı. Bu, yapay zekanın ‘bizi kullanarak’ kendini geliştirmesinin bir örneği aslında.

[^10]:  Facebook’un Llama’sının veri seti kapalı ama bu veri seti içindeki ağırlıklandırmalar açık. Bu ne demek? İsteyen istediği gibi ağırlıkları değiştirerek modeli revize edebilir demek. Örneğin ChatGPT’deki kimi sansür mekanizmalarını kaldırmak gibi. 

[^11]:  ‘Kapalı/özel’ modeller klasik anlamda lisanslı yazılım ürünleri gibiler. Bu modeller gerek veri seti gerekse bu setlerin ağırlıklandırılmasını bizlerden saklıyorlar. Llama gibi yarı-açık modeller ise veri setlerini saklıyor ama bu setlerin ağırlıklandırılmasını bize gösteriyor ve değiştirmeye izin veriyorlar. Tamamen ‘açık kaynak’ ise hem veri setlerini hem de ağırlıklandırmayı herkesin görebileceği ve değiştirebileceği şekilde sunan modellere deniyor.

[^12]:  Bunun yanında üzerine uygulama konulmasına izin vermeden direkt olarak son kullanıcıya ulaşan Midjourney gibi yapay zeka modelleri de mevcut.

[^13]:  Yazıda genel olarak yapay zekanın magazinsel örneklerine yer vermemeye çalıştım ama yeri geldiği için dipnot olarak bile olsa şu anektodu sizinle paylaşmadan geçemeyeceğim: George Mason Üniversitesi’nde ekonomi profesörü olan [Bryan Caplan](https://x.com/bryan_caplan) 2023 yılının Ocak ayında ChatGPT’nin öğrencilerine verdiği sınavdan D notu alması üzerine [Matthew Barnett](https://x.com/MatthewJBar) ile “ChatGPT’nin 2029 yılına kadar hiçbir sınavından A alamayacağı” üzerine bir iddiaya girer. Bundan sadece üç ay sonra ortaya çıkan GPT-4’ün sınavdan A almasıyla birlikte iddiayı [kaybeder](https://x.com/finmoorhouse/status/1638221410328797186). 

[^14]:  Tarih boyunca yıllık %2 civarında bir büyüme gösteren kişi başı GSMH’nin YZ’nın getireceği ‘patlayıcı büyüme’ ile %30’lara çıkacağını iddia eden [araştırmalar bile var](https://www.openphilanthropy.org/research/could-advanced-ai-drive-explosive-economic-growth/). 

[^15]:  Hadi dayanamayıp gelecekten bir örnek daha verelim. YZ’nın gelecekteki en büyük darboğazlarından olması beklenen ‘hesaplama kapasitesini’ aşmak için kendi çiplerini nasıl dizayn edeceğini anlatan, bir OpenAI mühendisi tarafından yazılmış [şu öyküyü](https://press.asimov.com/articles/tinker) hararetle tavsiye ederim.

[^16]:  Sizi hesaplama yapma zahmetinden kurtarıp üç yıllık toplam harcamanın 465 milyar ABD Doları olduğunu belirtelim.

---

*Not 1: Bu yazı ilk olarak 1 Kasım 2024'de [BTC Haber'de yayınlandı](https://www.btchaber.com/web3-ve-yapay-zeka-i/)*

*Not 2: Tüm yazılara [Yazılar](/articles/) sekmesinden ulaşabilirsiniz*

*Genel not: Piyasada oluşacak ihtimalleri değerlendiren bu yazıyı, yatırım tavsiyesi olarak almamanızı rica ederiz. Bu ve diğer yazılarımızın hiçbiri yatırım tavsiyesi değildir. Özellikle DeFi yani merkeziyetsiz finans sektörünün denetime tabi olmamasından dolayı klasik piyasalara göre çok daha riskli olabileceğini göz önünde bulundurun.*
