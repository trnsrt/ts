




- mible-wimble https://www.theblockcrypto.com/2019/01/08/mimblewimble-history-technology-and-the-mining-industry/
- Grin, Beam
- Farkları, özellikleri
- Critisim: Monetary policy
- Amaçları ne böyle bir para çıkarmanın?
-- Bitcoin'in bir gün vulnerable olacağını düşünmeleri mi? Güvenlik açısından?
-- Şu an yeterince private olmadığı için insanları bir gün çekmeyeceğini düşündükleri için?
-- Şimdiden erken bir projede yer alıp "voliyi vurmak"?
- Fair launch https://twitter.com/lopp/status/1085885684404019200
https://twitter.com/nic__carter/status/1085886693872492545
- in terms of scaling?.
- bitcoin maximalists, interested
-- completely decentralized project (as opposed to ICO)
-- technology interesting
-- 

how the whitepaper came about?
- mysterious creater (like satoshi)
- came out of nowhere (harry potter character - posted a paper something on an IRC)
- mible-wimble a new blockchain
- another developer (harry potter character) said he is working on grin

Grin yaklaşık bir buçuk iki yıldır geliştirme halinde

Bitcoin'de adresler belli olduğu için para nereden geldi, nereye gitti bilindiği için kullanıcıları bir şekilde takip etmek ya da paranın izini sürmek mümkün oluyor idi. Çünkü Bitcoin'de bir işlem yaptığınızda bunu Bitcoin ağındaki bir makineye (düğüm-node) gönderiyorsunuz o da tüm sisteme yayıyor. Buradan da paranın izini sürülebilir oluyor. Burada öyle değil. 
Privacy olarak çözümü dandelion adı verilen bir protokol kullanıyor. Dandelion kara hindiba çiçeği demek. MW'de siz sisteme bir işlem gönderdiğinizde bunu alan makine rastgele bir başka makineye gönderiyor, o bir başkasına ve böyle böyle ilk gönderen makinanın izinin sürülemeyeceği bir "bozma (fluff)" sürecinden geçiliyor. 


solves two problems
- one is the kind of scaling side of the blocks, and the
- second appears to be privacy coming as default.
- to verify an output, you have to follow it all the way back to the beginning of a chain, basically, in order to verify it. This uses some mathematical tricks so that instead of having to verify the entire history of the chain, you can just verify instead that everything amounts to zero, so all the transactions and all the outputs and everything that goes into it just have to equal zero and then you know, you can validate it from there. you know that’s fine, and there was no new money created there. The inputs equal the outputs
- Well, there are no addresses. So everything happens kind of on the wallet side. So, on a Mimblewimble blockchain, since there’s no concept of address, all you have is a UTXO set that just has outputs in it. It’s basically outputs and outputs and outputs all the way down. The way a transaction works is you don’t kind of put an address in and send it off to the chain. You actually have to communicate with another wallet. So the two wallets will work together, use their private keys to build a valid transaction, and then afterwards that transaction can get sent to the chain. So there’s certain, there are no addresses in a cryptographic sense.
- the solution for this wallet exchange, it’s not a one size fits all solution. Some people will be very, very concerned about, you know, everything is extremely private, and want to kind of set up their own communication network to make sure that everything they do is extremely private. Other people might be happy enough using an intermediary service that actually does the matchups and the transaction building. So what we’re trying to do on Grin is just make sure that we can enable all of those possibilities.

*A lot of flexibility for performing a transaction, you have to find a transacting party then match and then result to be written in blockchain- so it is always an output and it is always a zero-sum game, so you do not need to validate the whole history*
a lot more flexibility then? This could be done over email, private chat groups. It can be done almost with anything? 
- Yes. We have somebody now working on sending exchanges over Keybase, which I think is a nice little solution there because you already have the communication going there. You have filed in place, you have the people building mobile wallets, it should be possible to go and bump your phones together to do the transaction. So there’s, there’s a lot of possibilities there, definitely.

*bitcoin maximalists love it. especially grin. just like bitcoin, no founder, all key developers are hidden. is it something developed by crypto anarchists, as a backup to bitcoin, in case bitcoin to become influenced by a government or a centralized power in that sense?*

*or they (maximalists) like it because the development is faster, or changing founding blocks of bitcoin is difficult? or they see a fundamental problem (flaw, architectural isseu) in bitcoin so they look for an innovative system*

*It is private becauase all the information including private keys and data amounts are hidden with something called perfect information hiding*
if putting transaction data amounts and hiding your private key into a form which nobody can … It’s called perfect hiding, perfect information hiding

*block size will be limited to improve efficiency. If you create anything that fills up the block you will be penalized (pay higher fees)
block size limits. There’s a waiting because on a Mimblewimble Blockchain outputs can be destroyed, which actually reduces the … When you send and output and spend it off, it reduces the size of the chain, basically. The amount of data that has to be sent around. So transactions are weighted in a certain way that if you’re creating a lot of outputs, you’re penalized. If you destroy a lot of outputs, you’re not penalized as much. Your fees are lower, we have a soft limit and a hard limit. We’re actually still in the middle of adjusting a little bit, but yes, we do have limits.

-- mible-wimble
--- all the developers are harry potter subjects (fans)
---
