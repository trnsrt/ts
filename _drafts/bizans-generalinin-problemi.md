


Blockchain bazlı şifreli sistemlerin birbirine bağlı ancak birbirinden bağımsız binlerce makineden oluştuğunu daha önceki yazılarımızda bahsetmiştik. Peki bu makineler nasıl hep birlikte aynı anda aynı kararı veriyorlar? Aralarında hiç sorun çıkmıyor mu? Eğer çıkıyorsa bu sorunları nasıl çözüp tekrar aynı yolda ilerliyorlar? Birileri sistemi manipule etmek isterse ne olacak? Olamaz mı? Olur tabii ki.. Sistemin mimarlari buna karşı nasıl önlemler almış ona bir göz atalım şimdi. 



Konuya başlamadan önce Blockchain sistemini kısaca hatırlatmakta yarar var. Demiştik ki, Blockchain yapılan bir işlemin binlerce makinede kaydının tutulması ve belli aralıklar ile (örneğin Bitcoin'de 10 dakikada bir) bütün makinelerin ellerindeki kayıtların toplanıp tabiri caiz ise bir balya haline getirilmesi şeklinde çalışan bir sistem idi. Bir araya getirilen bu bilgilerin her makinada aynı şekilde bulunması gerekiyor ki, üzerine yeni bir balya işlem gelebilsin. Dolayısı ile altta kalan balyadaki bilgiler hem tutarlı olsun, hem sonradan değiştirilemesin (balya bağlandıktan sonra binlerce makineye dönüp işlem değişikliği yapamazsınız, imkansıza yakın bu), ki buna "Mutabakat Mekanizması" (consensus mechanism) deniyor. 

Peki ama yukarıda bahsettiğimiz bu 10 dakikada bir her makinede işlemler nasıl aynı şekilde bulunuyor? Ya birileri ortama nifak tohumu ekmeye kalkar ve sahte işlem girmeye kalkarsa. Nasıl sağlanacak bu mutabakat?.




Efendim, ilginçtir, bu mimari anlaşmazlıklar için kullanılan terim "Bizans Generalleri Problemi" olarak biliniyor. Nedir bu, kısaca anlatalım. 

