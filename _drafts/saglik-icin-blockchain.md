---
layout: post
title:  "Sağlık için Blockchain"
date:   2018-04-17 20:16:43 +0300
categories: Genel
---
Son iki yazımızda Blockchain'i sadece finans dünyası değil başka pek çok alanda da kullanılabileceğini söylemiş ve bunlardan [sanat](http://ademimerkezi.com/genel/2018/04/06/sanat-icin-blockchain.html) ve [filantropi ve hayır dünyası](http://ademimerkezi.com/genel/2018/03/29/Iyilik-icin-blockchain.html) yararına yapılabileceklere bakmıştık. 

Bu yazımızda ise sağlık alanında Blockchain bize ne gibi faydalar sağlayabilir ona bir göz atalım dilerseniz. 

--

### Sorunlar, sıkıntılar

2015 yılı Haziran ayında "thedarkoverlord" isimli bir hacker yaklaşık [10 milyon Amerikalı'ya ait medikal datayı](https://www.zdnet.com/article/hacker-advertising-huge-health-insurance-database/) 1 milyon ABD Dolarına yakın bir rakamdan satışa çıkardı. Hacker bu gizli medikal bilgileri dört ayrı şirketin ana bilgisayarlarından almıştı. İşte size merkezi sistemlerin en büyük dezavantajlarından biri: Dataların bir arada tutulduğu merkezi yapılar her zaman güvenlik açığı potansiyeli taşır.

Öte yandan sağlık kurumlarının kendi özel veritabanlarını tutmaları ve hastaya ait bilgilerin kurumlar arasında paylaşımı ciddi bir sıkıntı. Sistemlerin birbiri ile konuşmaması bir yana bir şekilde iletişim sağlansa bile yaşanan gecikmeler dakikaların bile çok önemli olduğu kimi durumlarda daha ciddi sorunlara hatta ölümlere kadar giden kayıplara yol açabiliyor. Bilgi eğer hastanın kontrolünde olsa acil müdahale gerektiren kritik durumlarda hasta (ya da yakınları) o an ulaşabildikleri ilk sağlık kurumunda yetkili kişilere bu bilgilere erişime izin verebilir ve hastaya gerekli müdahaleler zamanında yapılabilir. 

Hemen akla şu soru gelebilir: "Sağlık kurumları kendi aralarında anlaşsa ve bu sistemleri kursa ya? Ya da hükümetler onları zorlasa. Blockchain'e gerçekten gerek var mı?" Buna üç farklı açıdan bakarak cevap vermek mümkün: 

1. Öncelikle bu tip farklı sağlık kurumlarının birbirleri ile konuşmalarını sağlamak için gerekli sistem entegrasyonu ya da iletişimi oldukça zor, karmaşık ve zaman alıcı. Üstelik çok maliyetli. Halbuki bütün hastanelerin bağlanacakları ortak bir platform olsa ve hasta kayıtlarına bu platform aracılığı ile ulaşılsa sağlık kurumları ciddi bir yatırıma girmeden sistemin nimetlerinden faydalanabilirler. 
2. Tabii gecikmiş müdahalerin hastada yol açacağı fiziki tahribat ve sonrasında bu tahribatların tedavisi için yapılacak masrafların büyüklüğü göz önüne alındığında, ortak bir platformun sigorta şirketleri için de ciddi bir tasarruf sağlayacağını öngörmek zor değil.    
3. Bir de yukarıda en başta bahsettiğimiz bilginin değişik kurumlara açık olması durumunda yanlış ellere geçmesi ve güvenliğinin sağlanamaması konusu var. 

### Çözümler?

Özellikle sağlık alanına hitap eden kişisel bilgilerin korunması, saklanması ve güvenli şekilde paylaşılması konusunda pekçok yeni girişim var. Sadece bununla da sınırlı değil elbette girişimler, özellikle ilaç kullanımı ile ilgili tüm zinciri ilgilendiren konularda çalışanlar da var. İsterseniz sözü daha fazla uzatmadan bu girişimlerden birer cümle ile bahsedelim. 

[Healthureum](https://www.healthureum.io/) Ethereum Blockchain'i kullanarak sizin medikal kayıtlarınız üzerinde tam bir sahipliğiniz olmasını sağlıyor. Yani kayıtlarınız Blockchain üzerinde şifreli olarak saklanıyor. Sizin izin verdiğiniz kuruluşlar sizin izin verdiğiniz ölçüde Healthureum platformu üzerinden bu kayıtlara ulaşabiliyorlar. 

&nbsp;

| ![healthureum.png](/assets/healthureum2.png) | 
|:--:| 
| *Healthureum sistemi [nasıl çalışıyor](https://healthureum.wordpress.com/2018/01/24/advantages-of-a-blockchain-enabled-ehr-as-implemented-by-project-healthureum-over-the-conventional-record-keeping-software-that-is-presently-in-use-2/)?* | 

&nbsp;


[Tierion](https://tierion.com/) da benzer şekilde hasta datalarının sağlıklı bir şekilde kayıt edilmesi ve kayıtlarını tutarlılığı (değiştirilemezliği) konusunda çalışıyor ve [Philips Blockchain Labs](http://www.2.forms.healthcare.philips.com/blockchainlabs) ile işbirliği içinde. Keza MIT altındaki Media Lab merkezinden çıkma girişimlerden [MedRec](http://medrec.io) de hastaların datalarının kendi kontrolleri altında izin verdikleri kurumlarla kolayca paylaşılabilmesine yoğunlaşmış. Bir başka girişim [Factom](https://www.factom.com) ise Blockchain altyapısını kullanarak global ama özellikle sağlık hizmetlerine erişimin zor olduğu bölgelerde yaşayanların sağlık datalarının dağıtık bir yapıda (Blockchain üzerinde) tutulması ve biometrik verifikasyon ile erişimi konusunda uzmanlaşmış ve 2016 yılında Bill & Melinda Gates Foundation'dan [yatırım almış](https://www.gatesfoundation.org/How-We-Work/Quick-Links/Grants-Database/Grants/2016/11/OPP1159449).

[ScalaMed](https://www.scalamed.com) ilaçlar ve reçeteler üzerinde yapılan sahteciliği önlemek amacıyla ilaç üreticileri, dağıtıcılar, hastaneler ve eczane zincilerini bir araya getiren ve ilaçların kayıt, teyid ve transferini güvenli, kaçağa yol açmayacak şekilde yapılmasını sağlayacak bir Blockchain altyapılı bir sistem üzerinde çalışyor. Bu alanda çalışan diğer bir girişim olan [MediLedger](https://www.mediledger.com/) ise Genentech ve Pfizer'i içine alan bir pilot çalışma ile benzer şekilde ilaçların üreticiden hastaya ulaşımındaki kaçakları önlemek için Blockchain bazlı çözümlere kafa yoruyor. 

### Sonuç

Önceki yazılarımızda da belirttiğimiz gibi, Blockchain tabanlı sistemler henüz emekleme aşamasında. Sağlık alanındaki girişimlerde odak daha çok kişisel bilgilerin korunmasına yoğunlaşmış durumda ve geçmişte yaşanan olaylardan dolayı bu gayet anlaşılır. Ancak hasta hayatını kurtarabilecek bilginin hızlı paylaşımı ve maliyetleri artıran bürokrasinin azaltılması gibi konularda da Blockchain bazlı girişimler sektöre yeni açılımlar getirebilir. 

Özellikle sağlık alanında data paylaşımında herhangi bir standart henüz oturmuş değil ve yukarıdaki örneklerden de gördüğünüz gibi bu alanda dominant oyuncu olmaya aday pekçok girişim var. Sağlık, ilaç ve sigorta sektörleri teknolojik yenilikleri yakından takip etseler de organizasyonel değişiklik getirebilecek değişim ve yeniliklerde genelde tutucu davranırlar. Dolayısıyla, özellikle tüm kurumların kullanabileceği ortak bir platforma geçiş konusuna da son derece ihtiyatlı yaklaşacaklarını hatta zorlansalar bile ayak direyeceklerini görmek sürpriz olmaz. Bakalım, Blockchain sağlık alanındaki yaşanan kimi dertlere bir şekilde deva olabilecek mi?

--

Eğer Blockchain teknolojisinin nasıl çıktığını merak ediyorsanız, "[Geceleri uykunuzu ne kaçırıyor](http://ademimerkezi.com/genel/2018/03/01/Geceleri-uykunuzu-ne-kaciriyor.html)" ve "[Sahi nedir bu Blockchain Allah aşkına?](http://ademimerkezi.com/genel/2018/03/02/Sahi-nedir-bu-blockchain-allah-askina.html) yazılarımıza, bu teknolojinin şu anda en olgun şekilde kullanılan uygulamalarından Bitcoin'e ilginiz varsa "[Bitcoin ne tam olarak?](http://ademimerkezi.com/genel/2018/03/13/Bitcoin-ne-tam-olarak.html), "[Bitcoin para mı gerçekten?](http://ademimerkezi.com/genel/2018/03/22/Bitcoin-para-mi-gercekten.html)" ve "[Bütün bunlar bir balon mu?](http://ademimerkezi.com/genel/2018/03/05/Butun-bunlar-bir-balon-mu.html)" yazılarımıza göze atabilirsiniz. 
