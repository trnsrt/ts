Bugünkü yazımızda, DeFi'nin en büyük hırsızlıklardan biri sonucu çalınan paranın geçtiğimiz haftalarda geri (ç)alınma hikayesine' ve ardında bıraktığı sorulara göz atacağız.

### Öncelikle nedir olay?
DeFi üzerindeki en büyük hırsızlıklardan biri geçtiğimiz yılın Şubat ayında [yaşanmıştı](/genel/2022/03/11/defide-kopru-kazasi.html). Ethereum ile Solana arasında kriptopara transferine aracılık eden [Wormhole köprüsüne](https://www.portalbridge.com/#/transfer) ait tam 320 milyon ABD Doları tutarındaki ETH çalınmıştı.  Kripto dünyasının dev kuruluşlarından olan [Jump Crypto](https://jumpcrypto.com/) olayın hemen ardından çalınan parayı yerine koyarak hem Wormhole yatırımını kurtarmış hem de küçük yatırımcıların zarar görmesini engellemişti ama sonuçta bu kadar büyük bir zararı da sineye çekmek zorunda kalmıştı. (Bu olayın detaylarını geçtiğimiz yıl yazdığımız bir yazıda [incelemiştik](/genel/2022/03/11/defide-kopru-kazasi.html)).

O günden bu yana değişik DeFi protokolleri arasında gezinen çalıntı para, en son [Oasis Procotol](https://oasis.app/)'e ait bir emanet hesabına transfer edilmişti. İşte bu sırada, Jump Crypto'ya ait bir ekip, İngiltere'de yüksek mahkemeden bir karar çıkartarak, Oasis'in de yardımıyla 225 milyon ABD Dolarına denk ETH'yi[^1] hesaptan geri 'çaldılar'.

Çalınmış bir paranın geri alınabiliyor olması her ne kadar olumlu bir olay olarak görülse de yapılan işlem pek çok soruyu da beraberinde getirdi. "Hani blokzincir üzerindeki hesapların erişimi sadece hesap sahibinde idi? Nasıl oluyor da bu para çalınabiliyor?",  "Hani 'kod kanun' idi, mahkeme kararı DeFi'ye nasıl nüfuz edebiliyor?", "Merkeziyetsiz olduğunu iddia eden Oasis protokolü nasıl oluyor da kullanıcının kendisine emanet ettiği paranın çalınmasına 'yataklık' edebiliyor?" ortaya atılan sorulardan birkaçı. Dilerseniz, öncelikle olayın teknik olarak nasıl geliştiğine hızlıca bir bakalım, sonra da bu peş peşe sıraladığımız sorulara yanıt arayalım (teknik tarafa merak duymayan okuyucularımız, bir sonraki 'sorular' kısmına direkt geçiş yapabilirler).

### Nasıl gerçekleşti peki?[^2]
Çalınan para Şubat 2022'den bu yana çeşitli DeFi protokolleri arasında gezdi durdu[^3]. Saldırganlar en son olarak 23 Ocak tarihinde bu parayı Oasis protokolüne ait bir emanet hesabına [geçirdiler](https://etherscan.io/tx/0x5b7a789deafa61792c62e17f2b18e8a76ca995b77853ba54d20d755a98120a5b). İşte olaylar buradan sonra hız kazandı. 

[Oasis](https://oasis.app/), merkeziyetsiz dünyanın en eski ve prestijli ekiplerinden olan MakerDAO içinden çıkma bir ekip. MakerDAO, ETH gibi varlıkları teminat olarak gösterip DAI borç alabileceğiniz bir protokol. Oasis ise kullanıcıların MakerDAO'yu kullanabilmesi için çıkarılmış arayüzlerden bir tanesi. Kullanıcı, parasını Oasis'e ait kontratlar aracılığıyla kilitliyor ve karşılığında Oasis kontratı aracılığıyla DAI basıyor (yani borç alıyor).

İşte Wormhole istismarcısı (ingilizcede 'exploiter' olarak geçen kelimenin direkt çevirisi, siz saldırgan da diyebilirsiniz), Oasis kontratına koyduğu 225 milyon ABD Doları tutarındaki ETH benzeri token (wstETH ve rETH) karşılığında 78 milyon ABD Doları tutarından DAI borç alıyor. 

Normalde Oasis kontratları 'değiştirilemez' kontratlar. Ne demek bu? Kullandığınız kontratların değiştirilemez olması, kullanıcı olarak parayı emanet ettiğiniz yerin, yarın öbür gün kafasına göre kontratın kodunu değiştirerek paranızı alıp götürememesi demek. Peki o zaman bu para nasıl bu kontrattan alındı? İşte burada 'şeytan ayrıntıda gizlidir' konusu giriyor kadraja. 

Efendim, Oasis'in verdiği ekstra bir hizmet daha var. O da otomatik zarar durdurma (ingilizcesi stop-loss olan belli bir zarar oluşması durumunda pozisyonu kapatma)  tektikleme mekanizması. Temel olarak, kullanıcıyı ani fiyat değişimlerinden korumak için kurulmuş bir mekanizma bu ama aynı zamanda burada kullanıcıya ekstra başka faydalar da sağlayabiliyor. Eğer, ETH değer kaybeder ve teminat/borç oranınız belli bir rakamın altına düşerse, bu kontrat otomatik olarak teminatınızın bir kısımını satıp borcunuzu kapatarak sizin açığa düşmenizi engelliyor. Ya da tam tersi, ETH'nin değeri yükselir ve teminat/borç oranınız belli bir rakamın üzerine çıkarsa, sizin için DAI basarak daha fazla borç almanıza imkan sağlıyor. Bu özellik sadece kullanıcı seçerse işliyor (bir başka deyişle opsiyonel). 

İşte, Wormhole istismarcısının hatası bu opsiyonu seçmek oluyor. Neden? Çünkü bunu seçtiği noktada o tetikleme mekanizmasını çalıştıran başka bir akıllı kontrata kendi hesabının kontrolünü de vermiş oluyor. Her ne kadar Oasis kontratı değiştirilemez olsa da bu diğer akıllı kontrat değiştirilebilir/güncellenebilir bir kontrat! Yani? Yanisi, geliştiriciler isterse bu kontratın çalışma mantığını istedikleri gibi değiştirebilirler[^4]!

Jump Crypto ekibi bu güncellenebilir kontratta bir hata olduğunu farkediyor ve Oasis ekibine kontratı güncelleyerek parayı hesaptan kendilerine aktarmalarını istiyor [^5]. Oasis ekibi, 'hiçbir zaman kullanıcı fonlarına dokunmayacakları' gerekçesiyle bunu reddediyor ama bir yandan da Jump'a şöyle diyorlar: "mahkemeden karar getirirseniz ona uymak zorunda kalırız". Bunun üzerine Jump Crypto, İngiliz mahkemelerine başvuruyor ve yargıç 'tabii ki alabilirsiniz' deyince, dönüp Oasis'in kapısını [tekrar çalıyorlar](https://cointelegraph.com/news/jump-crypto-oasis-app-counter-exploits-wormhole-hacker-for-225m). 

Mahkeme kararını gören Oasis ekibi değiştirilebilir kontratı değiştirme hakkına sahip imza yetkililerinin arasına Jump ekibini de koyuyor. Sonrasında Jump ekibi bu imza yetkisi sayesinde istismarcıya ait emanet hesabını ele geçiriyor, krediyi geri ödüyor, teminatı çözüp tam 225 milyon ABD Dolarını [kendi hesaplarına](https://etherscan.io/address/0x5fec2f34d80ed82370f733043b6a536d7e9d7f8d#tokentxns) transfer ediyorlar.  Tam bir saat 53 dakika süren bütün süreç bittikten sonra Jump Crypto'nun Oasis kontratındaki imza yetkisi kaldırılıyor.

### Sorular, sorular... 

Çalınan bir paranın geri alınıyor olması dış dünyada takdir görüyor tabii. Zira, DeFi ile ilgili dışarıdan gelen en büyük eleştirilerden biri, saldırı ve istismar aracılığıyla ciddi paraların kaybedilmiş olması. DeFi'nin o ana kadar yaşanmış en büyük ikinci hırsızlık olayında mutlu sona ulaşılmış olması geniş kitlelerin algısını olumlu yönde değiştirebilir.

DeFi ve kripto dünyasının içindekilerin olaya bakış açısı ise oldukça farklı. Zira, kripto ve DeFi için en kritik konulardan biri yapılan işlemlerin 'kesin' olması. Siz, herhangi bir işlem yaptığınızda blokzincir üzerine yazıldıktan sonra bu işlemin sonlandırıldığını varsayarsınız. Bu durum DeFi'nin hem gücü hem de zayıf karnı olarak değerlendirilebilir. Bir yanda işlem gerçekleştiğinde anında mahsuplaşma olması süreçleri hızlandırır, kapitali çok daha verimli kullanmayı ve varlıklar üzerinde tam egemenlik sağlamayı getirir. Öte yandan herhangi bir hack olduğunda da paranız geri döndürülemez şekilde elinizden kaçar. Benzer şekilde akıllı kontratların kod ne söylerse onu yapacağını ve yapılanların değiştirilemeyeceğini düşünürsünüz. Nereden bakarsanız bakın ortada karmaşık bir durum var. İşte bu nedenle, dilerseniz yukarıda sorduğumuz sorular üzerinden konuyu açıklamaya çalışalım. 

#### *"Hani blokzincir üzerindeki hesapların erişimi sadece hesap sahibinde idi? Nasıl oluyor da bu para çalınabiliyor?"*
Evet, blokzincir üzerindeki hesapların erişimi sadece o hesaba erişen anahtarların elinde; bu hep böyleydi, bundan sonra da böyle olacak. Burada, Wormhole istismarcısı, parasını teminat olarak bir başka akıllı kontrata yatırıyor. Normalde bu akıllı kontratın kullanıcının parasını almak gibi bir özelliği yok. Sorun, istismarcının seçtiği opsiyon nedeniyle, 'değiştirilebilir bir kontrat'a kendi hesabına kontrolünü vermiş olması. Normalde bunda da bir sorun olmayabilir di, sonuçta bu değiştirilebilir kontrat bir bot, otomatik işlem yapıyor. Sorun bu değiştirilebilir kontratta bir 'açık' olması ve bu açık nedeniyle üçüncü bir partinin opsiyonun olduğu kontratı değiştirerek emanetteki paraya erişebilir hale gelmesi. (İstismarcı olarak birilerine güvenmek zorunda olmak tam bir oximoron -tezat- aslında).

#### *"Hani 'kod kanun' idi, mahkeme kararı DeFi'ye nasıl nüfuz ediyor?"*
Bu çok haklı bir soru. Sıkça kullandığımız bir söz var: Merkeziyetsizlik uzun ince bir yol. Protokoller merkezi başlayıp zamanla merkeziyetsiz oluyorlar. Oasis, MakerDAO'nun merkeziyetsizlik vizyonu gereği ana ekibin ortadan kaldırıldığı 2021 Haziran ayında kurulmuş bir yan ekip. Henüz tam anlamıyla merkeziyetsiz değiller. Bu nedenle, kurucu ekip mahkemeden gelen bir emri uygulamak zorunda kalmış. Neden? Haklı olarak mahkeme kararına uymadıkları durumda ortaya çıkabilecek ceza riskini almak istemedikleri için. 

"İyi işte, mahkeme kararı çıkmış ve suçlular cezalandırılmış" diyebilirsiniz tabii. Peki ya yarın öbür gün birinin hakkınızda yapacağı bir şikayet nedeniyle mahkemeden sizin varlıklarınıza el koyma kararı çıkarsa? Hani nerede kaldı 'dijital dünyada varlıklara tam sahip olma' özelliği?

#### *"Merkeziyetsiz olduğunu iddia eden Oasis protokolü nasıl kullanıcının kendisine emanet ettiği paranın çalınmasına 'yataklık' ediyor?"*
Oasis CEO'su, 'akıllı kontrat kodu içinde bulunan ve üçüncü partilere erişim imkanı veren' açığı daha önce farketmediklerini [söylüyor](https://thedefiant.io/oasis-rugs-the-rugger-but-how/) (bir protokol dostu ekip (Jump?) bunu farkedip Oasis'e bildiriyor. Sonra da bu açık sayesinden fonlar kurtarılıyor. Sonrasında da 'açık' kapatılıyor (kontratın güncellenebilirlik özelliği kaldırılıyor). Ne kadar inandırıcı? Size kalmış. 

Kontratların değiştirilebilir olması DeFi'nin ruhuna aykırı bir durum. Öte yandan bu durum yeni protokollerde kaçınılmaz olabiliyor. Zira, bu protokoller için 'kullanıcıların fonlarını korumak çok önemli. Kodda bir hata olması durumunda hemen müdahale edilmesi gerekebiliyor. İşte bunu yapabilmek için de genelde 'değiştirilebilir' kontrat kullanılıyor.

[Ethereum'un kendi sitesinde](https://ethereum.org/en/developers/docs/smart-contracts/upgrading/#proxy-patterns) değiştirilebilir kontratların artı ve eksilerinden detaylıca bahsediliyor. Yukarıdaki artıların güzel ancak çeşitli risklerin olduğunun da altı çiziliyor. Neler mesela? Bu kontratlar merkeziyetsizlik ve güvenlik açısından sorunlar yaratabilir, kullanıcının geliştirici ekibe güven duymasını gerektirir (hani blokzincir güvene olan ihtiyacı kaldıracaktı?), geliştirici ekiplerin hızlı geliştirme sürecinde "nasıl olsa sorun çıkarsa düzeltiriz" şeklinde düşünüp yeterince titiz davranmamalarına neden olabilir.

Burada Oasis'e yöneltilen önemli sorulardan biri de şu: Normalde değiştirilebilir kontrat güncellenmeden önce kullanıcılara belli bir süre verilir. Bu sayede, kontratın yeni halinden memnun olmayan kullanıcılar, güncelleme öncesinde paralarını çekebilirler. Oasis'in böyle bir iç kuralının olmaması ve kontratı anında değiştirip uygulamaya koyması merkeziyetsizliğe aykırı bir tutum olması nedeniyle ciddi şekilde eleştiriliyor.

### Sonuç 
Geçtiğimiz hafta yaşanan olay, en hafifinden "Wormhole istismarcısı ava giderken avlandı" ya da "intikam soğuk yenen bir yemektir, Jump Crypto ise sabırlı bir müşteri" şeklinde yorumlanabilir. Öte yandan konuya "iki yanlış bir doğru etmez" şeklinde bakmak da aynı şekilde mümkün. DeFi'nin önünde alması gereken bir hayli yol var [^6]. Protokoller bu yolda ne şekilde ilerleyecekler, hep birlikte yaşayarak göreceğiz. 

---


[^1]: Tam olarak geri alınan para 219 milyon ABD Doları değerinde wstETH (ETH'ye denk Lido tarafından çıkarılan likit staking tokeni) ve 6 milyon ABD Doları değerinde rETH (ETH'ye denk rocketpool tarafından çıkarılan likit staking tokeni). 

[^2]: Teknik detaylara meraklı olanlar için [şu yazı](https://www.blockworksresearch.com/research/we-do-a-little-counter-exploit) ilginizi çekebilir.  

[^3]: Para protokoller arasında transfer edildi ama Tornado Cash benzeri bir karıştırıcı/temizleyiciye sokulmadığı için nereye gittiği hep takip edilebilir oldu.

[^4]: Normalde bir kullanıcı için çok şüpheli bir durum değil bu. Sonuçta bu diğer akıllı kontrat otomatik çalışan bir bot. Ama burada kullanıcı normal bir kullanıcı değil 320 milyon dolar para kaldırmış bir dolandırıcı.

[^5]: Kontrattaki açığın ne olduğu tam olarak belli değil. Kontratı değiştirme hakkının Oasis tarafından üçüncü bir partiye verilebilmesi olduğu düşünülüyor. 

[^6]: DeFi girişimlerinin önünde aşmaları gereken, i) kullanıcı fonlarını 'doğru ve kurallı' bir şekilde korumaktan, ii) istismarcıları engeleyecek düzgün kodlar ve iç düzenlemelerin oluşturulmasına ve iii) dış dünyanın müdahalesini minimuma indirecek kadar merkeziyetsizliğe yelken açılmasına uzanan geniş bir yelpaze var. 
