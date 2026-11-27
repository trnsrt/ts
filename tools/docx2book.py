#!/usr/bin/env python3
"""docx2book.py - convert the "Sorularla Web3" manuscript (.docx) into Jekyll collection pages.

Usage:  python3 -I tools/docx2book.py [--book tr|en] <docx> <out_dir> <img_dir>
        --book selects the per-book profile (default tr = Sorularla Web3; en = Web3 Unlocked, see PROFILES).
        e.g. tools/docx2book.py "Sorularla Web3 - DRAFT 03 - pre-translation.docx" \
                 _sorularla_web3 assets/books/sorularla-web3

Only the Python standard library is used (zipfile + xml.etree); images are resized with macOS `sips`.
The script is deterministic and re-runnable: it rewrites the files it generated earlier and removes
stale ones listed in the manifest `<dir>/.generated` of the previous run. Other files are never touched.

Profile "df" (Sorularla DeFi): parts are heading 1 (-> chapter pages), sections heading 2, body text is style
"Normal (Web)", figure captions are the italic (character style "Emphasis") paragraph - or one-cell table - right
after the image, and plain body paragraphs take their wording from the printed PDF when it can be aligned
confidently (see PrintedText). Needs pdftotext (poppler) for that.

Profiles: "tr" detects chapters by style (heading 1: "Giriş", "Bölüm N: ..."), heading 3 -> "##", figure
captions are heading 6 *before* the image. "en" (Web3 Unlocked) has no heading 1: "Introduction" and
"Chapter N: Title" are Normal paragraphs matched by text; in the Introduction heading 2/3/4 become
"##"/"###"/"####" on the single Introduction page; heading 5 is the figure *title* before the image and
heading 6 the figure caption after it. A heading 2 directly followed by another heading 2 (no text between)
is not a page of its own: its text becomes a bold first line of the next section page.

Mapping for the "tr" profile (docx style name -> output)
  everything before the first non-empty "heading 1"  -> skipped (front matter, TOC)
  heading 1  "Giriş"                 -> page 000-giris.md             (kind: section, chapter 0)
  heading 1  "Bölüm N: Title"        -> page N00-bolum-N.md           (kind: chapter; body = intro text)
  heading 2  (non-empty)             -> page NKK-<slug>.md            (kind: section, one per heading 2)
  heading 3  -> "## text {#id}"
  heading 4  -> short label ending in ":" becomes a bold run-in "**Label:** paragraph"; others "### text {#id}"
  heading 5  -> "#### text {#id}"
  heading 6  -> figure caption for the next image paragraph (or table-figure)
  Normal     -> paragraph; runs: bold "**", italic "*" (merged, edge whitespace moved outside the markers)
  w:numPr    -> Markdown list (bullet or decimal according to numbering.xml, nesting by ilvl)
  hyperlink  -> [text](url) from the rels file (external targets); adjacent links to the same URL are merged
  footnotes  -> kramdown footnotes, renumbered from 1 per page, definitions at the end of the page
  drawing    -> <figure><img ... width height loading="lazy"><figcaption>..</figcaption></figure>
                (text that follows the image inside the same paragraph, usually a "Kaynak:" note, goes into
                the figcaption inside <span class="fig-note">)
  the table  -> a 1-column table that holds an image plus a caption row is emitted as a figure
  empty paragraphs, page breaks, the TOC field and empty headings are dropped.
Text containing "{{" or "{%" is wrapped in {% raw %}...{% endraw %} so Liquid cannot touch it.
"""
import collections
import difflib
import html
import os
import re
import struct
import subprocess
import sys
import zipfile
import xml.etree.ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
PKG = '{http://schemas.openxmlformats.org/package/2006/relationships}'

SITE_TITLE = 'Sorularla Web3'
URL_BASE = '/Sorularla_Web3'
IMG_URL = '/assets/books/sorularla-web3'
P = None            # active profile, set by use_profile()
MAX_IMG_W = 1200

# ----------------------------------------------------------------------------------------------
# manual slug / SEO-title overrides: heading 2 text -> (slug, title without the " – Sorularla Web3" suffix)
OVERRIDES = {
    'Örnek: Modüler blokzincir - Celestia': ('celestia', 'Celestia: Modüler blokzincir'),
    'Örnek: Bitcoin üzerine ikinci seviye çözümler': ('bitcoin-ikinci-seviye', 'Bitcoin üzerine ikinci seviye çözümler'),
    'Örnek: PayPal’ın stabil parası PYUSD': ('pyusd', 'PYUSD: PayPal’ın stabil parası'),
    'Örnek: Stabil paralar sokağına yeni taşınan çocuk: Ethena': ('ethena', 'Ethena: Stabil paralar sokağına yeni taşınan çocuk'),
    'Örnek: 2022 krizi – I. perde: UST Terra’nın hikayesi': ('terra-ust', 'UST Terra’nın hikayesi: 2022 krizi, I. perde'),
    'Örnek: 2022 ABD krizi – II. perde : 3AC’nin iflası': ('3ac-iflasi', '3AC’nin iflası: 2022 ABD krizi, II. perde'),
    'Örnek: 2022 ABD krizi – III. perde : FTX’in batışı': ('ftx-batisi', 'FTX’in batışı: 2022 ABD krizi, III. perde'),
    'Örnek: 2023 ABD bankacılık krizi': ('2023-abd-bankacilik-krizi', '2023 ABD bankacılık krizi'),
    'Örnek: İyilik için Web3 - Crypto Climate Coalition': ('crypto-climate-coalition', 'Crypto Climate Coalition: İyilik için Web3'),
    'Örnek: DeSci - Vibe DAO': ('vibe-dao', 'Vibe DAO: DeSci'),
    'Örnek: BlackRock’un token hamlesi': ('blackrock-token-hamlesi', 'BlackRock’un token hamlesi'),
    'Örnek: ABD’de bir ev tokenleştirmesi': ('abd-ev-tokenlestirmesi', 'ABD’de bir ev tokenleştirmesi'),
    'Kısa vade beklentiler (2025-2026)': ('kisa-vade-beklentiler', None),
}

# Web-edition text corrections (owner-approved). (old, new): each must match exactly once in the whole
# book, counted per source paragraph/caption (a figure caption used for both alt and figcaption counts once).
# A match must lie inside one text run; URLs are never touched. The script fails loudly otherwise.
CORRECTIONS = [
    ('Gelir sırayla bakalım', 'Gelin sırayla bakalım'),
    ('shortların zarar yazdığın en uzun dönemin', 'shortların zarar yazdığı en uzun dönemin'),
    ('bu oran %98’e%2.', 'bu oran %98’e %2.'),
    ('artı yada eksi', 'artı ya da eksi'),
    ('sUSD’nin 2024 yılı', 'sUSDe’nin 2024 yılı'),
    ('WTH.e', 'WETH.e'),
    # GEO batch B3 (owner-approved)
    ('pay düşünüyor', 'pay düşüyor'),
    ('işini içine', 'işin içine'),
    ('gönüllerin', 'gönüllülerin'),
    ('sarfediyorlar', 'sarf ediyorlar'),       # 303 and 201: see CORRECTION_EXPECTED
    ('Geoffery', 'Geoffrey'),                  # body + figure caption: see CORRECTION_EXPECTED
    ('özellike', 'özellikle'),
    ('gösterilebiir', 'gösterilebilir'),
    ('göz atabilirsiniz..', 'göz atabilirsiniz.'),
    ('“yazar neler saçmalamış“', '“yazar neler saçmalamış”'),
    # GEO batch B4 (owner-approved; 'oyun alanın', 'bir çok' and 'Lens protokolün' are narrowed so they cannot hit
    # 'oyun alanında/alanına', 'bir çoklu' or 'protokolünü'; 'Tiktok' also occurs in 103: see CORRECTION_EXPECTED)
    ('CDBC', 'CBDC'),
    ('açıkcası', 'açıkçası'),
    ('barındıyor', 'barındırıyor'),
    ('bir kaç', 'birkaç'),
    ('devretmesine da', 'devretmesine de'),
    ('oyun alanın tamamen', 'oyun alanının tamamen'),
    ('yetişmişti..', 'yetişmişti.'),
    ('Web3 girişimlerin oynadıkça', 'Web3 girişimlerinin oynadıkça'),
    ('Tiktok', 'TikTok'),
    ('zincilerde', 'zincirlerde'),   # 209 'bu zincilerde yok' (owner-approved typo, 2026-11-27)
    ('Mastadon', 'Mastodon'),
    ('bir çok hesabın', 'birçok hesabın'),
    ('bir çoğunda', 'birçoğunda'),
    ('Twitter’in', 'Twitter’ın'),
    ('Lens protokolün Open Actions', 'Lens protokolünün Open Actions'),
    ('insiyatif', 'inisiyatif'),
    ('ilgilli', 'ilgili'),
    ('Howell Lovells', 'Hogan Lovells'),
    # GEO batch B5 (owner-approved). 'Temmuz 2024’de' is on 202 and 410; 'azartesi' is narrowed so it cannot hit
    # 'Pazartesi'/'pazartesi'; the quote-mark fixes that straddle a link are in TR_OUT_CORRECTIONS
    ('tekeli altında girmiş', 'tekeli altına girmiş'),
    ('dipnot’ta', 'dipnotta'),
    ('Orjinalliğin', 'Orijinalliğin'),
    ('anektodu', 'anekdotu'),
    ('pekçok', 'pek çok'),
    ('az16 ai', 'a16z'),
    ('(ingilizce ‘agent)', '(İngilizce ‘agent’)'),      # must come before the general 'ingilizce' entry below
    ('LLama3', 'Llama3'),
    ('Yapay Zeka önümüzdeki', 'Yapay zeka önümüzdeki'),
    ('Temmuz 2024’de', 'Temmuz 2024’te'),
    ('Microsoft’un Llama’sı', 'Meta’nın Llama’sı'),
    ('Apple Store', 'App Store'),
    ('aracılığıya', 'aracılığıyla'),
    ('koşulununun', 'koşulunun'),
    ('veriyor..', 'veriyor.'),
    ('sadece Ethereum bir yıl sonra', 'sadece Ethereum, bir yıl sonra'),
    ('112 ABD Dolarına', '119 ABD Dolarına'),
    ('ETH’ye çevirebildiniz', 'ETH’ye çevirebilecektiniz'),
    ('8 Mayıs tarihinde', '7 Mayıs tarihinde'),
    ('2023 yılının Mart ayına kadar', '2023 yılının Nisan ayına kadar'),
    ('Alameda, azartesi günü', 'Alameda, pazartesi günü'),
    ('“sırada kim var?“', '“sırada kim var?”'),
    ('“paranızı SVB’den çekin“', '“paranızı SVB’den çekin”'),
    ('Autonomus', 'Autonomous'),
    ('kazananan', 'kazanan'),
    ('aktarılacak..', 'aktarılacak.'),
    ('bir yıldan kısa bir zaman içinde', '18 ay kadar bir sürede'),   # 3AC page (owner-approved)
    ('ingilizce', 'İngilizce', 'all'),                   # every lowercase 'ingilizce…' in the book (never in a URL, id or heading)
    # GEO batch B6 (owner-approved). 'Orjinal'/'orjinal' (TDK: "orijinal"), 'Ingilizce' with a plain capital I (201 and 502),
    # '2023’de' (503 and 304; the second 304 hit is '2023’den' -> '2023’ten'); each is never in a URL, id or heading
    ('Orjinal', 'Orijinal', 'all'),
    ('orjinal', 'orijinal', 'all'),
    ('Ingilizce', 'İngilizce', 'all'),
    ('Optimum', 'Optimism'),                             # 201 footnote and 502: the Optimism network
    ('Ensititüsü', 'Enstitüsü'),
    ('Ancorage', 'Anchorage'),
    ('2023’de', '2023’te', 'all'),
    ('Inital', 'Initial', 'all'),                        # 502: both in one paragraph
    ('Daha faz kan', 'Daha fazla kan'),
    ('kriterlerini yavaş yavaş', 'kriterleri yavaş yavaş'),
    ('çıktığı gördük', 'çıktığını gördük'),
    ('sağlıyorsa ise', 'sağlıyorsa'),
    ('var.. Bu pay', 'var. Bu pay'),
    ('başladı..', 'başladı.'),
    ('gerekiyor.. Yok eğer', 'gerekiyor. Yok eğer'),
]
# expected number of matching paragraphs for TR corrections that legitimately occur more than once (default 1)
CORRECTION_EXPECTED = {'Geoffery': 2, 'sarfediyorlar': 2, 'Tiktok': 2, 'Temmuz 2024’de': 2, 'ingilizce': 50,
                       'orjinal': 2, 'Ingilizce': 2, 'Optimum': 2, '2023’de': 3, 'Inital': 2}
# the same for the English profile (default 1)
EN_CORRECTION_EXPECTED = {}
CORRECTION_COUNTS = {c[0]: 0 for c in CORRECTIONS}
_COUNTED = set()
_LINK_SEEN = set()

EN_OVERRIDES = {
    'Web 1.0: The Age of Protocols': ('web-1-0', None),
    'Web 2.0: The Age of Platforms': ('web-2-0', None),
    'Web3: The Quest for Digital Ownership': ('web3', None),
    'What makes Ethereum’s economy tick?': ('ethereum-economy', None),
    'Bitcoin, Solana, and Ethereum: The Big Three': ('bitcoin-solana-ethereum', None),
    'Modular vs. Monolithic Blockchains': ('modular-vs-monolithic', None),
    'Layer 2 Solutions: Ethereum’s Scaling Heroes': ('layer-2-solutions', None),
    "Don't Mind the Gap: Bridges and the Internet of Value": ('bridges', None),
    'Wallets': ('wallets', None),
    'Intents': ('intents', None),
    'The Rise of the Community': ('community', None),
    'Web3 Founders: A New Breed of Entrepreneurs': ('founders', None),
    'Web3 Investors: New Rules, New Roles': ('investors', None),
    'Developers: Powering the Web3 Revolution': ('developers', None),
    'Miners and Validators: Blockchain’s Backbone': ('miners-validators', None),
    'Users: The Heart of Web3': ('users', None),
    'Stablecoins: Web3’s Killer App': ('stablecoins', None),
    'Decentralized Finance: Web3’s Financial Revolution': ('decentralized-finance', None),
    'Exploring the NFT Universe': ('nft-universe', None),
    'Gaming and the Metaverse': ('gaming-metaverse', None),
    'Decentralized Social Media: Taking Back Control': ('decentralized-social-media', None),
    'Digital Identity: Taking Back Your Data': ('digital-identity', None),
    'Decentralized Physical Infrastructure: The Next Frontier': ('physical-infrastructure', None),
    'Decentralized Science: A New Frontier (DeSci)': ('desci', None),
    'Regenerative Finance: A New Web3 Vision': ('regenerative-finance', None),
    'AI Meets Web3': ('ai-meets-web3', None),
    'Case Study: 2022 Crisis Act I – Terra Implosion': ('terra-implosion', '2022 Crisis Act I – Terra Implosion'),
    'Case Study: PayPal’s PYUSD Stablecoin': ('pyusd', 'PayPal’s PYUSD Stablecoin'),
    "Case Study: Ethena's USDe Stablecoin": ('ethena', "Ethena's USDe Stablecoin"),
    'Case Study: 2022 Crisis Act II – 3AC Bankruptcy': ('3ac-bankruptcy', '2022 Crisis Act II – 3AC Bankruptcy'),
    'Case Study: 2022 Crisis Act III – FTX Collapses': ('ftx-collapse', '2022 Crisis Act III – FTX Collapses'),
    'Case Study: 2023 US Banking Crisis': ('2023-us-banking-crisis', '2023 US Banking Crisis'),
    'Tokens Explained': ('tokens', None),
    'Understanding Tokenomics': ('tokenomics', None),
    'Case Study: When BlackRock Went On-Chain': ('blackrock-on-chain', 'When BlackRock Went On-Chain'),
    'Case Study: Tokenizing a US Home': ('tokenizing-a-us-home', 'Tokenizing a US Home'),
    'Short-Term Expectations (2025-2026)': ('short-term-expectations', None),
    'What’s Ahead for Web3 in the Long Term?': ('long-term-outlook', None),
}
# Web-edition fixes of source typos (owner-approved; the printed book has the same typos except where noted).
# (old, new) matches anywhere in a paragraph; (old, new, 'start') only at the start of a paragraph.
EN_CORRECTIONS = [
    ('n the world of stablecoins', 'In the world of stablecoins', 'start'),
    ('in funding rserve', 'in funding reserve'),
    ('individual freedom.It’s worth', 'individual freedom. It’s worth'),
    ('onto the blockchain.The venture', 'onto the blockchain. The venture'),
    ('insight or feature.[^4] This', 'insight or feature. This'),
    ('same group chats.[^4] When', 'same group chats. When'),
    # GEO batch B3 (owner-approved)
    ('until through mid-2025', 'through mid-2025'),
    ('security..', 'security.'),
    # GEO batch B4 (owner-approved)
    ('In 2023, In the first quarter of 2025 alone', 'In the first quarter of 2025 alone'),
    ('%4.5 for USDS', '4.5% for USDS'),
    ('Even though gained some traction', 'Even though it gained some traction'),
    ('Word Economic Forum', 'World Economic Forum'),
    # GEO batch B5 (owner-approved)
    ('In factt', 'In fact'),
    (',] Masa', ', Masa'),                                  # stray ']' after the Ocean Protocol footnote mark
    ('some versions of Mistral', 'some versions of Mistral,'),   # the comma goes before the footnote mark
    ('in matter of hours', 'in a matter of hours'),
    ('caused bank deposits surged', 'caused bank deposits to surge'),
    ('(Case Studies: Valve, NVG8)', '(Case Studies: Vana, NVG8)'),
    ('Apple Store', 'App Store'),
    ('in just under a year', 'in around 18 months'),
    # GEO batch B6 (owner-approved)
    ('a opaque', 'an opaque'),
    ('Bitcoin (BTC) fits this description', 'Bitcoin (BTC) fit this description'),
    ("Gandhi: 'First they ignore you", "Gandhi: ‘First they ignore you"),
    # 502: the airdrop paragraph repeated the 7-20% sentence above it; keep that one and drop the 5-10% sentence
    ('Finally, a slice of the pie is given away for free to early users and supporters through airdrops. While the allocation is often between 5-10%, the strategy behind airdrops has evolved significantly.',
     'The strategy behind airdrops has evolved significantly.'),
    ('up to ~$40,000 within six months', 'up to ~$16,000 within six months'),   # 400 UNI at the $40 maximum
]
# Fixes of the finished page Markdown (each must match exactly once). The footnote mark is a token of its own, so a
# fix that spans it (the source has a stray full stop after the mark) can only be made here, where it reads [^10].
EN_OUT_CORRECTIONS = [
    ('Congress.[^10].', 'Congress.[^10]'),
    # GEO batch B5 (owner-approved). A stray letter in front of a link, a full stop after a footnote mark, and a link
    # that straddles an apostrophe are not inside one text run.
    ('accumulated r[roughly', 'accumulated [roughly'),
    ('2023, r[regulators had seized', '2023, [regulators had seized'),
    ('a repeat of 2008[^9] .', 'a repeat of 2008[^9].'),
    ("[arrested in Singapore'](https://www.finews.com/news/english-news/59522-three-arrows-co-founder-arrested-singapore)s airport",
     '[arrested in Singapore](https://www.finews.com/news/english-news/59522-three-arrows-co-founder-arrested-singapore)’s airport'),
    # dead links (404) removed, text kept
    ('[recap](https://blockapps.net/blog/the-timeline-of-usts-collapse-understanding-the-failures-and-implications-of-algorithmic-stablecoins/)', 'recap'),
    ('[swept away](https://pontem.network/posts/the-collapse-of-3ac-three-arrows-capital-all-you-need-to-know)', 'swept away'),
    # PYUSD: the sentence without a verb (the FedNow link stays)
    ('[FedNow](https://www.frbservices.org/news/press-releases/072023-fednow-live-announcement) which some analysts suggest could intensify competition in instant payments, potentially pressuring margins.',
     '[FedNow](https://www.frbservices.org/news/press-releases/072023-fednow-live-announcement), which some analysts suggest could intensify competition in instant payments, may pressure margins.'),
    # AI page: Synesis One / First Batch as on the Turkish page; Further Reading IV had the same address as III (III keeps it)
    ('Synesis [One](https://www.firstbatch.xyz/), First Batch)', '[Synesis One](https://www.synesis.one/), [First Batch](https://www.firstbatch.xyz/))'),
    ('[IV - The Agentic Economy](https://members.delphidigital.io/reports/deai-iii-composable-compute)',
     '[IV - The Agentic Economy](https://members.delphidigital.io/reports/deai-iv-the-agentic-economy#vox-populi--war-of-the-rails-4435)'),
    # GEO batch B6 (owner-approved): the GENIUS Act is S. 1582 of the 119th Congress (the old target was H.R. 3736, 116th)
    ('[GENIUS Act](https://www.congress.gov/bill/116th-congress/house-bill/3736?q=%257B%2522search%2522:%2522genius+act%2522%257D&s=1&r=1)',
     '[GENIUS Act](https://www.congress.gov/bill/119th-congress/senate-bill/1582)'),
    # 501: the text says "nearly $19 trillion by 2033", so the link goes to the matching article (matched on text + old target)
    ('[value of tokenized assets](https://www.ledgerinsights.com/bcg-addx-estimate-asset-tokenization-to-reach-16-trillion-by-2030/)',
     '[value of tokenized assets](https://www.ledgerinsights.com/bcg-ripple-predict-tokenization-to-reach-18-9-trillion-by-2033/)'),
    ('alt="Forecast token market (2030)"', 'alt="Forecast token market (2033)"'),
    ('<figcaption>Forecast token market (2030)', '<figcaption>Forecast token market (2033)'),   # caption title matches the alt text and the 2033 source
    ('the easier it’s to bring', 'the easier it is to bring'),   # the docx has a straight apostrophe, so this is an output fix
    # dead links removed, text kept
    ('[different kinds of tokens](https://axiomq.com/blog/token-definition-how-they-work-and-why-they-matter/)', 'different kinds of tokens'),
    ('[paid out directly](https://cointelegraph.com/explained/blackrocks-buidl-fund-explained-why-it-matters-for-crypto-and-tradfi)', 'paid out directly'),
]
# Fixes of the finished page Markdown/HTML of the Turkish book (each must match exactly once, or (old, new, count)):
# quote marks straddling a link, one missing full stop after a link, one link removed from a chart caption (text kept).
TR_OUT_CORRECTIONS = [
    ('Galaxy Digital](https://www.galaxydigital.io/)‘in', 'Galaxy Digital](https://www.galaxydigital.io/)’in'),
    ('BUSD](https://paxos.com/busd/)‘yi', 'BUSD](https://paxos.com/busd/)’yi'),
    ('Vibe Bio](https://www.vibebio.com/)‘nun', 'Vibe Bio](https://www.vibebio.com/)’nun'),
    ('[düştü](https://coinmarketcap.com/currencies/steth/steth/eth/) BTC, 2022', '[düştü](https://coinmarketcap.com/currencies/steth/steth/eth/). BTC, 2022'),
    ('<a href="https://turansert.com/genel/2023/03/14/abdde-banka-krizi-ve-gelecek.html">FDIC</a>', 'FDIC'),
    # GEO batch B6 (owner-approved): dead link (404) removed from a chart caption, text kept
    ('<a href="https://www.finoa.io/blog/cost-savings-tokenization/">Finoa</a>', 'Finoa'),
    # the map pin on the house's street address is removed for the owners' privacy, text kept
    ('[bir banliyö evinin](https://www.google.com/maps/place/149+Cottage+Lake+Way,+Columbia,+SC+29209/@33.9594797,-80.9455555,272m/data=!3m1!1e3!4m5!3m4!1s0x88f8b053743f5079:0x8883bce9faf9ed0f!8m2!3d33.9596548!4d-80.9454178)',
     'bir banliyö evinin'),
]
# GEO batch B6 (owner-approved), footnote definitions (they are not in the page blocks that the lists above see):
# {book profile: [(old, new) or (old, new, expected count)]}, each must match exactly once in the whole book
FN_OUT_CORRECTIONS = {
    'tr': [
        ('[ishares Ethereum ETF’](https://www.blackrock.com/us/individual/products/337614/ishares-ethereum-trust-etf)i',
         '[iShares Ethereum ETF](https://www.blackrock.com/us/individual/products/337614/ishares-ethereum-trust-etf)’i'),
    ],
}
# GEO batch B6 (owner-approved), both BlackRock pages (503): CNBC, Coindesk, Nasdaq and Investopedia treat addresses as
# case-sensitive, so 'BlackRock' becomes 'blackrock' inside these six addresses only (link text and businesswire stay);
# applied through LINK_TARGET_FIXES below because one of the links is in a footnote
BLACKROCK_URL_FIXES = {u: u.replace('BlackRock', 'blackrock') for u in (
    'https://www.cnbc.com/2017/10/13/BlackRock-ceo-larry-fink-calls-bitcoin-an-index-of-money-laundering.html',
    'https://www.coindesk.com/business/2022/08/04/BlackRock-to-offer-crypto-for-institutional-investors-through-coinbase-prime/',
    'https://www.coindesk.com/business/2023/10/17/BlackRock-ceo-larry-fink-seeing-client-demand-for-crypto-around-the-world/',
    'https://www.coindesk.com/policy/2023/11/16/BlackRock-files-application-for-spot-ether-etf/',
    'https://www.nasdaq.com/articles/BlackRock-ceo-larry-fink-says-bitcoin-is-an-asset-class-that-protects-you',
    'https://www.investopedia.com/BlackRock-files-for-a-spot-bitcoin-etf-7547609',
)}
# Stray paragraphs (exact text, ordinary paragraphs only) to drop from the web edition; each must match exactly once.
EN_DROP_PARAGRAPHS = {'The Block Pro'}
# Normal-style paragraphs (exact text) that the published contents list as sections of their own.
EN_PROMOTE_TO_SECTION = {'Regenerative Finance: A New Web3 Vision'}
# heading text as it appears in the docx -> heading as printed in the book
EN_HEADING_OVERRIDES = {'Case Study: Terra’s 2022 Crisis (Act One)': 'Case Study: 2022 Crisis Act I – Terra Implosion'}

DF_PARTS = ['Nedir DeFi?', 'DeFi Dünyasının Aktörleri', 'DeFi’nin Altyapı Taşları',
            'DeFi Dünyasına Adım Atacaklar İçin Pratik Bilgiler']
# the 34 heading-2 sections in book order, worded as in the printed contents (İçindekiler)
DF_SECTIONS = [
    'Blokzincirin Çıkış Felsefesi Ne?', 'Blokzincir Finans Dünyasını Nasıl Etkileyecek?',
    'DeFi (Merkeziyetsiz Finans) Ne Demek?', 'DeFi’nin Çıkışı Nasıl Oldu?', 'DeFi’nin Temel Özellikleri Neler?',
    'DeFi’de Yatırım ve Girişimcilik', 'DeFi’de Başarının Sırrı Topluluk', 'DeFi’de Nasıl Merkeziyetsiz Olunuyor?',
    'Peki ya DeFi’nin Riskleri?', 'DeFi’de Regülasyon Olur Mu?', 'Dijitalleşme Sürecinde Gelecekte Bizi Neler Bekliyor?',
    'DeFi Dünyasında Neler Var?', 'MakerDAO: Kişiye Özel Merkez Bankası', 'Compound: Klasik Bankacılığın Rakibi',
    'Uniswap ve DeFi’nin Merkeziyetsiz Borsaları', 'Yearn Finance: DeFi’de Merkeziyetsiz Portföy Yönetimi',
    'Synthetix ve DeFi Türev Piyasaları', 'Hegic: DeFi’de Opsiyon Piyasaları', 'Nexus Mutual: DeFi’nin Sigortası',
    'Ethereum: DeFi’nin Altyapısı', 'Ethereum ve Rakipleri', 'Chainlink: DeFi’nin Bilgi Kaynağı', 'Nedir Oracle?',
    'The Graph: DeFi’nin Merkeziyetsiz Analiz Sağlayıcısı', 'Filecoin: DeFi’nin Merkeziyetsiz Saklama Deposu',
    'Aragon ile DeFi’de Yönetim', 'Stabil Paralar: DeFi’nin Can Suyu',
    'DeFi Dünyasına Girmek İçin İlk Atılacak Adımlar Neler?', 'Elektronik Cüzdan İle DeFi’ye Adım Atmak',
    'DeFi Tokenları Nasıl Satın Alınıyor?', 'DeFi’de İşlem Yaparken Nelere Dikkat Etmeli?',
    'Farklı Merkeziyetsiz Borsaları Aynı Anda Kullanmak', 'DeFi’de Portföy Nasıl Takip Edilir?',
    'DeFi ile Bizi Neler Bekliyor?',
]
DF_OVERRIDES = {
    'Blokzincirin Çıkış Felsefesi Ne?': ('blokzincirin-cikis-felsefesi', None),
    'DeFi (Merkeziyetsiz Finans) Ne Demek?': ('defi-ne-demek', None),
    'MakerDAO: Kişiye Özel Merkez Bankası': ('makerdao', None),
    'Compound: Klasik Bankacılığın Rakibi': ('compound', None),
    'Uniswap ve DeFi’nin Merkeziyetsiz Borsaları': ('uniswap', None),
    'Yearn Finance: DeFi’de Merkeziyetsiz Portföy Yönetimi': ('yearn-finance', None),
    'Synthetix ve DeFi Türev Piyasaları': ('synthetix', None),
    'Hegic: DeFi’de Opsiyon Piyasaları': ('hegic', None),
    'Nexus Mutual: DeFi’nin Sigortası': ('nexus-mutual', None),
    'Ethereum: DeFi’nin Altyapısı': ('ethereum', None),
    'Chainlink: DeFi’nin Bilgi Kaynağı': ('chainlink', None),
    'The Graph: DeFi’nin Merkeziyetsiz Analiz Sağlayıcısı': ('the-graph', None),
    'Filecoin: DeFi’nin Merkeziyetsiz Saklama Deposu': ('filecoin', None),
    'Aragon ile DeFi’de Yönetim': ('aragon', None),
    'Stabil Paralar: DeFi’nin Can Suyu': ('stabil-paralar', None),
    'DeFi Dünyasına Girmek İçin İlk Atılacak Adımlar Neler?': ('ilk-adimlar', None),
    'Elektronik Cüzdan İle DeFi’ye Adım Atmak': ('elektronik-cuzdan', None),
    'DeFi Tokenları Nasıl Satın Alınıyor?': ('token-satin-alma', None),
    'DeFi’de İşlem Yaparken Nelere Dikkat Etmeli?': ('islem-yaparken-dikkat', None),
    'Farklı Merkeziyetsiz Borsaları Aynı Anda Kullanmak': ('borsalari-birlikte-kullanmak', None),
    'DeFi’de Portföy Nasıl Takip Edilir?': ('portfoy-takibi', None),
    'DeFi ile Bizi Neler Bekliyor?': ('defi-ile-neler-bekliyor', None),
    'DeFi’de Başarının Sırrı Topluluk': ('basarinin-sirri-topluluk', None),
    'DeFi’de Nasıl Merkeziyetsiz Olunuyor?': ('nasil-merkeziyetsiz', None),
    'Dijitalleşme Sürecinde Gelecekte Bizi Neler Bekliyor?': ('dijitallesme-gelecek', None),
    'Blokzincir Finans Dünyasını Nasıl Etkileyecek?': ('finansi-nasil-etkileyecek', None),
}

PROFILES = {
    'tr': dict(name='tr', site_title='Sorularla Web3', url_base='/Sorularla_Web3',
               img_url='/assets/books/sorularla-web3', overrides=OVERRIDES, corrections=CORRECTIONS, out_corrections=TR_OUT_CORRECTIONS,
               intro_heading='Giriş', intro_slug='giris', chapter_slug='bolum-%d',
               chapter_label='Bölüm %d: %s', max_words=4,
               chapter_desc='Sorularla Web3 kitabının %d. bölümü: %s.', promote=set(), heading_overrides={}, style_alias={}),
    'en': dict(name='en', site_title='Web3 Unlocked', url_base='/Web3_Unlocked',
               img_url='/assets/books/web3-unlocked', overrides=EN_OVERRIDES, corrections=EN_CORRECTIONS, out_corrections=EN_OUT_CORRECTIONS,
               intro_heading='Introduction', intro_slug='introduction', chapter_slug='chapter-%d',
               chapter_label='Chapter %d: %s', max_words=5,
               chapter_desc='Chapter %d of the book Web3 Unlocked: %s.',
               promote=EN_PROMOTE_TO_SECTION, heading_overrides=EN_HEADING_OVERRIDES, style_alias={}),
}


# Web-edition fixes applied to the finished Markdown of the df pages (after the printed wording was taken over), so a
# rule is only needed where neither the docx nor the print is right. Each must match exactly once in the whole book.
# (Already fixed by the printed text, so not needed: "topladıları", "kullanıcılaradağıtıldı", "YIF", "insiyatifi".)
DF_CORRECTIONS = [
    ('\\*\\*\\*\\*Fark etmişsinizdir', 'Fark etmişsinizdir'),       # four stray asterisks typed in the source
    ('## Defi bir anda nasıl büyüdü?', '## DeFi bir anda nasıl büyüdü?'),
    ('insiyatiflere', 'inisiyatiflere'),
    ('bir başka insiyatif ise', 'bir başka inisiyatif ise'),
    # 304: the manuscript reuses note number 1 for this sentence, but its only note 1 (Messari, p. 67) is the source of
    # the quote further down; this marker has no note of its own
    ('pazarlar idi.[^1]', 'pazarlar idi.'),
    ('gerekiyor.8[^2]', 'gerekiyor.[^2]'),               # 208: the print's footnote digit "8" glued after the stop
]

# Overview of a part for its (otherwise empty) chapter page: a plain descriptive sentence built only from the book's own
# "Kitap hakkında" bullet for that part and the part's section headings; also used as the page description.
DF_CHAPTER_OVERVIEWS = {
    1: ('Bu bölüm, blokzincirin çıkış felsefesini, blokzincirin finans dünyasına etkisini, DeFi’nin çıkışını ve temel '
        'özelliklerini ele alıyor. DeFi’de yatırım ve girişimciliğe, başarının sırrı olarak topluluğa, merkeziyetsizliğe, '
        'risklere ve regülasyona da ayrı başlıklarda yer veriyor.'),
    2: ('Bu bölüm, DeFi dünyasında neler olduğuna bakıyor ve MakerDAO, Compound, Uniswap, Yearn Finance, Synthetix, Hegic '
        've Nexus Mutual projelerini tek tek anlatıyor. Her proje ayrı bir başlık altında işleniyor.'),
    3: ('Bu bölüm, DeFi’nin altyapı taşlarını ele alıyor: Ethereum ve rakipleri, Chainlink ve Oracle kavramı, The Graph, '
        'Filecoin, Aragon ile yönetim ve stabil paralar. Her konu ayrı bir başlık altında anlatılıyor.'),
    4: ('Bu bölüm, DeFi dünyasına adım atacaklar için pratik bilgiler veriyor: ilk adımlar, elektronik cüzdan ve DeFi '
        'tokenlarının satın alınması. İşlem yaparken dikkat edilecekler, merkeziyetsiz borsaları birlikte kullanmak ve '
        'portföy takibi de ayrı başlıklarda anlatılıyor.'),
}
BC_CHAPTER_OVERVIEWS = {
    1: ('Bu bölüm, blokzincir (Blockchain) teknolojisinin ne olduğunu soruyor. Önce üzerimize gelen dalganın farkında olup '
        'olmadığımıza, ardından Blockchain’in ne olduğuna bakıyor.'),
    2: ('Bu bölüm, Blockchain’in finans, tedarik zinciri, sağlık, çevre, seyahat, tahmin piyasaları, sosyal fayda ve sanat '
        'alanlarını nasıl etkileyeceğine bakıyor. Blockchain’in her derde deva olup olmadığına, değişen '
        'girişimcilik ve yatırımcılığa ve ICO ile token dünyasına da değiniyor.'),
    3: ('Bu bölüm, Blockchain’i teknik açıdan ele alıyor: şifrelemeyi, Blockchain’in kendi başına nasıl hareket ettiğini '
        've uzlaşma mekanizmalarını. Üç ayrı başlık altında işleniyor.'),
    5: ('Bu bölüm, Bitcoin’in ne olduğunu, para sayılıp sayılmayacağını ve işlemlerin nasıl gerçekleştiğini anlatıyor. '
        'Geniş kitlelere nasıl yayılabileceği, Lightning Network, Liquid, Bakkt ve Madencilik 2.0 da ayrı başlıklarda '
        'işleniyor.'),
    6: ('Bu bölüm, dünyanın en büyük bilgisayarı olan Ethereum’un hikayesini ve diğer kripto paraları ele alıyor. Sabit '
        'paralar da bu bölümde anlatılıyor.'),
}

BC_PARTS = ['Nedir Bu Blockchain Allah Aşkına?', 'Blockchain Beni Nasıl Etkileyecek?', 'Teknik Olarak Blockchain',
            'Blockchain’in Geleceği', 'Bitcoin', 'Ethereum ve Diğer Kripto Paralar']
# the 28 heading-2 sections in book order, worded as in the printed contents (index); a docx heading may continue
# beyond the printed wording ("ICO ve Token Dünyası: Yeni dünyada ...")
BC_SECTIONS = [
    'Üzerimize gelen dalganın farkında mıyız?', 'Sahi nedir bu Blockchain Allah aşkına?',
    'Blockchain finans dünyasını nasıl etkileyecek?', 'Finans dünyasından örnekler neler?',
    'Blockchain tedarik zincirini sağlamlaştırabilir mi?', 'Sağlık için Blockchain çözümleri neler?',
    'Blockchain çevremizi korumamıza yardımcı olabilir mi?', 'Blockchain seyahat sektörünü uçurur mu?',
    'Blockchain geleceği tahmin için kullanılabilir mi?', 'Blockchain’i sosyal fayda için kullanabilir miyiz?',
    'Blockchain sanat dünyasına ne katabilir?', 'Blockchain her derde deva mı?',
    'Blockchain bulunduğum sektöre yarar mı?', 'Değişen girişimcilik ve yatırımcılık', 'ICO ve Token Dünyası',
    'Blockchain şifrelemesi ne demek?', 'Blockchain nasıl kendi başına hareket ediyor? İpucu: Uzlaşma',
    'Uzlaşma mekanizmaları neler?', 'Bitcoin ne tam olarak?', 'Bitcoin para mı gerçekten? Nasıl?',
    'Bitcoin işlemi nasıl gerçekleşiyor?', 'Bitcoin geniş kitlelere nasıl yayılır?',
    'Bitcoin üzerinde ışık hızıyla işlem nasıl gerçekleşir? Lightning Network',
    'Bitcoin üzerinden büyük işlemleri hızlı yapmak mümkün mü? Bir çözüm: Liquid',
    'Bakkt kurumsal yatırımcıyı kripto paraya çeker mi?', 'Madencilik 2.0: Beyaz yakalıdan madenci olur mu?',
    'Dünyanın en büyük bilgisayarı olan Ethereum’un hikayesi ne?', 'Diğer kripto paralar neler?',
]
# Web-edition fixes of the finished page Markdown (each must match exactly once); only where the print has it right.
BC_CORRECTIONS = [
    ('Doğrulanabilirlik/Sahicililk', 'Doğrulanabilirlik/Sahicilik'),
    ('Blockhain', 'Blockchain', 6),                     # (old, new, expected count); the print has the typo too
    ('olmasında dolayı', 'olmasından dolayı'),
    ('başlangıça', 'başlangıca'),
    ('BTC’nin orjinal yaratıcılarının', 'BTC’nin orijinal yaratıcılarının'),   # GEO batch B6 (owner-approved), 506
    # 201: the manuscript sentence is unfinished ("... KYC) ve"); this is the printed wording
    ('(know-your-customer ya da kısaca KYC) ve', '(know-your-customer ya da kısaca KYC) konularında alacakları bir hayli yol var.'),
]
BC_OVERRIDES = {
    'Blockchain’i sosyal fayda için kullanabilir miyiz?': ('sosyal-fayda', None),
    'Blockchain nasıl kendi başına hareket ediyor? İpucu: Uzlaşma': ('kendi-basina-hareket', None),
    'Bitcoin üzerinde ışık hızıyla işlem nasıl gerçekleşir? Lightning Network': ('lightning-network', None),
    'Bitcoin üzerinden büyük işlemleri hızlı yapmak mümkün mü? Bir çözüm: Liquid': ('liquid-network', None),
    'Madencilik 2.0: Beyaz yakalıdan madenci olur mu?': ('madencilik-2-0', None),
    'Dünyanın en büyük bilgisayarı olan Ethereum’un hikayesi ne?': ('ethereum-hikayesi', None),
    'Blockchain tedarik zincirini sağlamlaştırabilir mi?': ('tedarik-zinciri', None),
    'Blockchain çevremizi korumamıza yardımcı olabilir mi?': ('cevre', None),
    'Blockchain geleceği tahmin için kullanılabilir mi?': ('tahmin-piyasalari', None),
    'Üzerimize gelen dalganın farkında mıyız?': ('dalganin-farkinda-miyiz', None),
    'Sahi nedir bu Blockchain Allah aşkına?': ('nedir-bu-blockchain', None),
    'Blockchain finans dünyasını nasıl etkileyecek?': ('finans-dunyasi', None),
    'Sağlık için Blockchain çözümleri neler?': ('saglik', None),
    'Blockchain seyahat sektörünü uçurur mu?': ('seyahat', None),
    'Blockchain sanat dünyasına ne katabilir?': ('sanat', None),
    'Blockchain her derde deva mı?': ('her-derde-deva', None),
    'Blockchain bulunduğum sektöre yarar mı?': ('sektore-yarar-mi', None),
    'Blockchain şifrelemesi ne demek?': ('sifreleme', None),
    'Bakkt kurumsal yatırımcıyı kripto paraya çeker mi?': ('bakkt', None),
}

PROFILES_EXTRA = {
    'bc': dict(name='bc', site_title='Sorularla Blockchain', url_base='/Sorularla_Blockchain',
               img_url='/assets/books/sorularla-blockchain', overrides=BC_OVERRIDES, corrections=[],
               intro_heading=None, intro_slug=None, chapter_slug='bolum-%d', chapter_label='%s', max_words=4,
               chapter_desc='Sorularla Blockchain kitabının %d. bölümü: %s.', promote=set(), heading_overrides={},
               style_alias={}, lead_styles={'Subtitle'}, parts=BC_PARTS, sections=BC_SECTIONS, heading_prefix=True,
               plain_captions=True, printed_pdf='assets/books/Sorularla_Blockchain.pdf', out_corrections=BC_CORRECTIONS,
               chapter_overviews=BC_CHAPTER_OVERVIEWS,
               printed_cfg=dict(layout=False, start='Üzerimize gelen dalganın farkında', headers=(), lookback=300,
                                multi_end=True, keep_punct=True, strict=True)),
    'df': dict(name='df', site_title='Sorularla DeFi', url_base='/Sorularla_DeFi',
               img_url='/assets/books/sorularla-defi', overrides=DF_OVERRIDES, corrections=[],
               intro_heading=None, intro_slug=None, chapter_slug='bolum-%d', chapter_label='%s', max_words=4,
               chapter_desc='Sorularla DeFi kitabının %d. bölümü: %s.', promote=set(), heading_overrides={},
               style_alias={'Normal (Web)': 'Normal'}, parts=DF_PARTS, sections=DF_SECTIONS,
               printed_pdf='assets/books/Sorularla_DeFi.pdf', out_corrections=DF_CORRECTIONS,
               chapter_overviews=DF_CHAPTER_OVERVIEWS,
               printed_cfg=dict(layout=True, start='NEDİR DEFI?', headers=('SORULARLA DEFI', 'MERKEZİYETSİZ FİNANS'),
                                keep_punct=True)),
}
PROFILES.update(PROFILES_EXTRA)

# Body-heading text overrides (GEO batch B): change the TEXT of a ## / ### / #### heading but keep its CURRENT {#id}.
# Keyed per book profile, then by (output file name, current id); ids are only unique within a page.
# Each entry must be applied exactly once or main() exits non-zero. The new text is escaped with esc_md like any heading.
BODY_HEADING_OVERRIDES = {
    'df': {
        ('103-defi-ne-demek.md', 'peki-ya-musteriler'): 'Peki, ya finans sisteminin müşterileri?',
    },
    'tr': {
        ('201-ethereumun-ekonomisi-nasil-calisiyor.md', 'islem-gelirleri'): 'Ethereum’un işlem gelirleri',
        ('201-ethereumun-ekonomisi-nasil-calisiyor.md', 'mev-gelirleri'): 'Ethereum’un MEV gelirleri',
        ('201-ethereumun-ekonomisi-nasil-calisiyor.md', 'ekstra-guvenlik-gelirleri-restaking'): 'Ethereum’un ekstra güvenlik gelirleri (restaking)',
        ('201-ethereumun-ekonomisi-nasil-calisiyor.md', 'peki-giderleri-neler'): 'Peki Ethereum’un giderleri neler?',
        ('201-ethereumun-ekonomisi-nasil-calisiyor.md', 'ultra-sound-money-soylemi-nereden-geliyor'): 'ETH için “ultra-sound money” söylemi nereden geliyor?',
        ('201-ethereumun-ekonomisi-nasil-calisiyor.md', 'onumuzdeki-donem-neler-getirecek'): 'Ethereum’da önümüzdeki dönem neler getirecek?',
        ('201-ethereumun-ekonomisi-nasil-calisiyor.md', 'teknik-olarak'): 'Ölçeklenme: teknik olarak',
        ('201-ethereumun-ekonomisi-nasil-calisiyor.md', 'eth-para-politikasina-etkisi'): 'Ölçeklenmenin ETH para politikasına etkisi',
        ('201-ethereumun-ekonomisi-nasil-calisiyor.md', 'teknik-acidan'): 'MEV sorunu: teknik açıdan',
        ('201-ethereumun-ekonomisi-nasil-calisiyor.md', 'eth-para-politikasina-etkisi-2'): 'MEV sorununun ETH para politikasına etkisi',
        ('412-ethena.md', 'ya-arkadaki-teminatin-degeri-duserse'): 'Ya USDe’nin arkasındaki teminatın değeri düşerse?',
        ('412-ethena.md', 'bu-kadar-mi-hayir-stabil-para-disinda-bir-urun-daha-var-susde'): 'Bu kadar mı? Hayır. Ethena’da stabil para dışında bir ürün daha var: sUSDe',
        ('412-ethena.md', 'sistemin-riskleri-neler'): 'Ethena sisteminin riskleri neler?',
        ('412-ethena.md', 'shortlamak-her-zaman-gelir-getirmiyor-ya-uzun-sure-negatif-gidip-zarar-yazarsa'): 'Ethena için short’lamak her zaman gelir getirmiyor; ya uzun süre negatif gidip zarar yazarsa?',
        ('412-ethena.md', 'kaldi-mi-baska-risk'): 'Ethena’da başka risk kaldı mı?',
        ('412-ethena.md', 'riskler-cok-mu-fazla'): 'Ethena’nın riskleri çok mu fazla?',
        ('000-giris.md', 'topluluk'): 'Web3’te topluluk',
        ('000-giris.md', 'kurucu-ekipler'): 'Web3’te kurucu ekipler',
        ('000-giris.md', 'yatirimcilar'): 'Web3’te yatırımcılar',
        ('000-giris.md', 'gelistiriciler'): 'Web3’te geliştiriciler',
        ('000-giris.md', 'madenciler-ve-onaylayicilar'): 'Web3’te madenciler ve onaylayıcılar',
        ('000-giris.md', 'kullanicilar'): 'Web3’te kullanıcılar',
        ('202-bitcoin-solana-ve-ethereum.md', 'son-donemde-neler-yasadik'): 'Kripto piyasasında son dönemde neler yaşadık?',
        ('204-ikinci-seviye-cozumler.md', 'ethereum-guvencesi'): 'İkinci seviye çözümlerde Ethereum güvencesi',
        ('204-ikinci-seviye-cozumler.md', 'her-ek-yazilim-risk-demek'): 'İkinci seviye çözümlerde her ek yazılım risk demek',
        ('204-ikinci-seviye-cozumler.md', 'gelirler'): 'İkinci seviye çözümlerin gelirleri',
        ('204-ikinci-seviye-cozumler.md', 'giderler'): 'İkinci seviye çözümlerin giderleri',
        ('205-kopruler.md', 'sikintilari-neler'): 'Köprülerin sıkıntıları neler?',
        ('207-intentler.md', 'ne-tip-islemlerden-bahsediyoruz'): 'Intent ile ne tip işlemlerden bahsediyoruz?',
        ('208-celestia.md', 'baska-neler-var'): 'Modüler blokzincir dünyasında başka neler var?',
        ('209-bitcoin-ikinci-seviye.md', 'madenciler'): 'Bitcoin ekosisteminde madenciler',
        ('209-bitcoin-ikinci-seviye.md', 'kullanicilar'): 'Bitcoin ekosisteminde kullanıcılar',
        ('209-bitcoin-ikinci-seviye.md', 'gelistiriciler'): 'Bitcoin ekosisteminde geliştiriciler',
        ('209-bitcoin-ikinci-seviye.md', 'cok-guzelmis-neden-daha-once-dusunulmedi-bu-cozumler'): '“Çok güzelmiş, neden Bitcoin üzerinde daha önce düşünülmedi bu çözümler?”',
        ('209-bitcoin-ikinci-seviye.md', 'peki-nasil-yapilacak-bu-cozumler'): 'Peki Bitcoin üzerinde nasıl yapılacak bu çözümler?',
        ('209-bitcoin-ikinci-seviye.md', 'yan-zincirler'): 'Bitcoin için yan-zincirler',
        ('301-topluluk.md', 'girisime-ne-zaman-katki-vermeye-basliyorlar'): 'Topluluklar girişime ne zaman katkı vermeye başlıyorlar?',
        ('303-yatirimcilar.md', 'ama-zamanla-gucleniyorlar'): '… ama yatırımcılar zamanla güçleniyorlar…',
        ('303-yatirimcilar.md', 've-uzmanlasiyorlar'): '…ve yatırımcılar uzmanlaşıyorlar',
        ('304-gelistiriciler.md', 'rapordan-onemli-basliklar'): 'Developer Report’tan önemli başlıklar',
        ('304-gelistiriciler.md', 'ilgi-cekici-noktalar'): 'Developer Report’taki ilgi çekici noktalar',
        ('304-gelistiriciler.md', 'diger-aglarda-durum-nasil'): 'Diğer ağlarda geliştiricilerin durumu nasıl?',
        ('306-kullanicilar.md', 'daha-iyi-bir-kullanici-deneyimi'): 'Web3 için daha iyi bir kullanıcı deneyimi',
        ('306-kullanicilar.md', 'urun-pazar-uyumu'): 'Web3’te ürün-pazar uyumu',
        ('601-kisa-vade-beklentiler.md', 'teknolojik-altyapi-artik-buyuk-olcude-tamamlaniyor'): 'Web3’te teknolojik altyapı artık büyük ölçüde tamamlanıyor',
        ('601-kisa-vade-beklentiler.md', 'kullanici-dostu-uygulamalar-artacak'): 'Web3’te kullanıcı dostu uygulamalar artacak',
        ('601-kisa-vade-beklentiler.md', 'regulasyonlar'): 'Web3 için regülasyonlar?',
        ('601-kisa-vade-beklentiler.md', 'urun-pazar-uyumu'): 'Web3’te ürün-pazar uyumu',
        # GEO batch B4: question/claim headings that lacked their subject
        ('401-stabil-paralar.md', 'piyasanin-hakimi-kim'): 'Stabil para piyasasının hakimi kim?',
        ('401-stabil-paralar.md', 'ya-merkeziyetsiz-alternatifler'): 'Ya merkeziyetsiz stabil para alternatifleri?',
        ('402-merkeziyetsiz-finans-defi.md', 'neden-finans-alani-one-cikti'): 'Web3’te neden finans alanı öne çıktı?',
        ('402-merkeziyetsiz-finans-defi.md', 'daha-da-buyumesi-icin-onunde-hangi-engeller-var'): 'DeFi’nin daha da büyümesi için önünde hangi engeller var?',
        ('402-merkeziyetsiz-finans-defi.md', 'care-ne'): 'DeFi için çare ne?',
        ('406-dijital-kimlik.md', 'blokzincir-deva-olur-mu-bu-derde'): 'Blokzincir deva olur mu bu dijital kimlik derdine?',
        ('406-dijital-kimlik.md', 'pratikte-nasil-calisabilir'): 'Dijital kimlik pratikte nasıl çalışabilir?',
        ('407-merkeziyetsiz-fiziksel-altyapilar-depin.md', 'blokzincir-ve-kripto-nerede-devreye-giriyor'): 'DePIN’de blokzincir ve kripto nerede devreye giriyor?',
        ('407-merkeziyetsiz-fiziksel-altyapilar-depin.md', 'gelecekte-bu-alanda-bizi-neler-bekliyor'): 'Gelecekte DePIN alanında bizi neler bekliyor?',
        ('408-onarici-finans-refi.md', 'blokzincir-nasil-yardimci-olabilir'): 'Blokzincir onarıcı finansa nasıl yardımcı olabilir?',
        ('408-onarici-finans-refi.md', 'her-sey-gulluk-gulistanlik-mi'): 'ReFi’de her ‘şey’ güllük gülistanlık mı?',
        # GEO batch B5
        ('413-terra-ust.md', 'en-son-neler-yasandi'): 'UST’de en son neler yaşandı?',
        ('413-terra-ust.md', 'isin-ozu-guven'): 'Stabil paralarda işin özü güven',
        ('413-terra-ust.md', 'olanlardan-nasil-sonuclar-cikarabiliriz'): 'UST krizinden nasıl sonuçlar çıkarabiliriz?',
        ('413-terra-ust.md', 'bu-bir-yol-kazasi'): 'UST krizi bir yol kazası',
        ('414-3ac-iflasi.md', 'nasil-basladi'): '3AC’nin iflası nasıl başladı?',
        ('415-ftx-batisi.md', 'neler-olmustu'): 'FTX’te neler olmuştu?',
        ('416-2023-abd-bankacilik-krizi.md', 'neler-oldu-neden-oldu'): '2023 ABD bankacılık krizinde neler oldu, neden oldu?',
        ('416-2023-abd-bankacilik-krizi.md', 'cikarilacak-dersler-ve-gelecek-bize-neler-getirecek'): 'ABD bankacılık krizinden çıkarılacak dersler ve gelecek bize neler getirecek?',
        ('417-crypto-climate-coalition.md', 'neden-boyle-bir-organizasyona-ihtiyac-duyulmus'): 'Neden LCCC gibi bir organizasyona ihtiyaç duyulmuş?',
        ('417-crypto-climate-coalition.md', 'ortaklar-nasil-katkida-bulunuyor'): 'LCCC’nin ortakları nasıl katkıda bulunuyor?',
        ('418-vibe-dao.md', 'hangi-alanlara-girmisler'): 'Vibe Bio hangi alanlara girmiş?',
        # GEO batch B6 (chapter 5): headings that did not say what the page is about
        ('501-tokenler.md', 'nasil-cozuldu-bu-sorun'): 'Nasıl çözüldü bu kopyalanma sorunu?',
        ('501-tokenler.md', 'peki-ya-merkezsiz-olarak-cozum-var-mi'): 'Peki ya kopyalanma sorununa merkezsiz olarak çözüm var mı?',
        ('501-tokenler.md', 'nasil-bir-pazardan-bahsediyoruz'): 'Nasıl bir token pazarından bahsediyoruz?',
        ('501-tokenler.md', 'en-buyuk-gelisme-stabil-paralarda'): 'Tokenleştirmede en büyük gelişme stabil paralarda',
        ('502-tokenomics.md', 'nasil-bir-planlama-yapmali-nelere-dikkat-etmeli'): 'Token ekonomisi için nasıl bir planlama yapmalı? Nelere dikkat etmeli?',
        ('502-tokenomics.md', 'surec-dejenere-olmaya-dogru-ilerler'): 'Airdrop süreci dejenere olmaya doğru ilerler…',
        ('502-tokenomics.md', 'peki-kanuni-olarak-nasil-degerlendiriliyorlar'): 'Peki tokenler kanuni olarak nasıl değerlendiriliyorlar?',
        ('502-tokenomics.md', 'turkiyede-durum-ne'): 'Türkiye’de tokenlerin durumu ne?',
        ('503-blackrock-token-hamlesi.md', 'gelelim-son-olaya-ne-oldu'): 'Gelelim BlackRock’ın son hamlesine. Ne oldu?',
        ('503-blackrock-token-hamlesi.md', 'etflere-benziyor-mu-bu-urun-neden-onemli'): 'ETF’lere benziyor mu BUIDL? Neden önemli?',
        ('504-abd-ev-tokenlestirmesi.md', 'neydi-islem'): 'Neydi bu ev tokenleştirme işlemi?',
    },
    'en': {
        ('103-web3.md', 'the-movement-begins'): 'The Web3 Movement Begins',
        ('103-web3.md', 'a-new-foundation'): 'A New Foundation for Web3',
        ('103-web3.md', 'the-search-for-product-market-fit'): 'Web3’s Search for Product-Market Fit',
        ('103-web3.md', 'breaking-down-the-silos'): 'Breaking Down Blockchain Silos',
        ('201-ethereum-economy.md', 'who-lives-here'): 'Who Lives in Ethereum’s Digital Nation?',
        ('201-ethereum-economy.md', 'an-auction-for-every-transaction'): 'An Auction for Every Ethereum Transaction',
        ('201-ethereum-economy.md', 'mev-revenue'): 'Ethereum’s MEV Revenue',
        ('201-ethereum-economy.md', 'what-the-future-holds'): 'What the Future Holds for Ethereum',
        ('203-modular-vs-monolithic.md', 'ethereums-persistent-challenge'): 'Ethereum’s Persistent Scaling Challenge',
        ('412-ethena.md', 'what-if-collateral-prices-drop'): 'What if USDe’s Collateral Prices Drop?',
        ('412-ethena.md', 'what-if-the-yield-engine-goes-into-reverse'): 'What if Ethena’s Yield Engine Goes into Reverse?',
        ('412-ethena.md', 'the-centralization-dilemma'): 'Ethena’s Centralization Dilemma',
        ('412-ethena.md', 'code-oracles-and-regulators'): 'Other Ethena Risks: Code, Oracles, and Regulators',
        ('412-ethena.md', 'is-it-worth-the-risk'): 'Is Ethena Worth the Risk?',
        ('000-introduction.md', 'the-new-financial-system'): 'Web3’s New Financial System',
        ('000-introduction.md', 'the-ownership-economy'): 'The Ownership Economy in Everyday Life',
        ('000-introduction.md', 'the-next-horizons'): 'Web3’s Next Horizons',
        ('101-web-1-0.md', 'open-and-free-by-design'): 'Web 1.0: Open and Free by Design',
        ('101-web-1-0.md', 'clumsy-by-modern-standards'): 'Web 1.0: Clumsy by Modern Standards',
        ('102-web-2-0.md', 'the-gold-rush'): 'The Web 2.0 Gold Rush',
        ('102-web-2-0.md', 'the-price-of-free'): 'The Price of "Free" in Web 2.0',
        ('102-web-2-0.md', 'radical-centralization'): 'Web 2.0: Radical Centralization',
        ('102-web-2-0.md', 'proprietary-walled-gardens'): 'Web 2.0: Proprietary, Walled Gardens',
        ('102-web-2-0.md', 'fast-user-focused-applications'): 'Web 2.0: Fast, User-Focused Applications',
        ('202-bitcoin-solana-ethereum.md', 'whats-been-happening-lately'): 'What’s Been Happening Lately in Crypto Markets?',
        ('204-layer-2-solutions.md', 'security-by-inheritance'): 'Layer 2 Security by Inheritance',
        ('204-layer-2-solutions.md', 'hubs-of-innovation'): 'Layer 2s as Hubs of Innovation',
        ('204-layer-2-solutions.md', 'an-economic-flywheel'): 'The Layer 2 Economic Flywheel',
        ('204-layer-2-solutions.md', 'the-road-ahead'): 'The Road Ahead for Layer 2s',
        ('205-bridges.md', 'the-great-migration'): 'The Great Migration Across Chains',
        ('205-bridges.md', 'how-they-work-lock-and-mint'): 'How Bridges Work: Lock and Mint',
        ('205-bridges.md', 'a-battlefield-of-ideas'): 'A Battlefield of Bridge Designs',
        ('205-bridges.md', 'the-billion-dollar-risk'): 'The Billion-Dollar Risk of Bridges',
        ('205-bridges.md', 'the-future-is-invisible'): 'The Future of Bridges is Invisible',
        ('206-wallets.md', 'the-new-center-of-gravity'): 'The New Center of Gravity for Smart Wallets',
        ('207-intents.md', 'old-way-vs-new-way'): 'Old Way vs. New Way of Making Transactions',
        ('207-intents.md', 'the-solver-marketplace'): 'The Intent Solver Marketplace',
        ('207-intents.md', 'from-theory-to-standard'): 'Intents: From Theory to Standard',
        ('207-intents.md', 'the-road-ahead'): 'The Road Ahead for Intents',
        ('301-community.md', 'the-journey-to-decentralization'): 'A Project’s Journey to Decentralization',
        ('301-community.md', 'the-inevitable-path-to-decentralization'): 'The Inevitable Path to Decentralization for Web3 Projects',
        ('301-community.md', 'nice-in-theory-not-so-in-reality'): 'DAOs: Nice in theory not so in reality…',
        ('303-investors.md', 'a-weaker-hand-at-the-table'): 'A Weaker Hand at the Table for Investors',
        ('303-investors.md', 'but-the-pendulum-swings-back'): '...But the Pendulum Swings Back for Investors',
        ('304-developers.md', 'key-takeaways-what-to-watch'): 'Developer Report Key Takeaways: What to Watch',
        ('305-miners-validators.md', 'why-do-they-exist'): 'Why Do Miners and Validators Exist?',
        ('306-users.md', 'a-new-model-for-identity'): 'A New Model for Identity in Web3',
        ('306-users.md', 'a-radically-better-user-experience'): 'A Radically Better User Experience for Web3',
        ('306-users.md', 'finding-product-market-fit-through-pain'): 'Finding Web3’s Product-Market Fit Through Pain',
        ('601-short-term-expectations.md', 'infrastructure-has-nearly-arrived'): 'Web3 Infrastructure Has Nearly Arrived',
        ('601-short-term-expectations.md', 'tackling-the-scaling-problem'): 'Tackling the Blockchain Scaling Problem',
        ('601-short-term-expectations.md', 'apps-designed-for-everyday-users'): 'Web3 Apps Designed for Everyday Users',
        ('601-short-term-expectations.md', 'finding-product-market-fit'): 'Finding Product-Market Fit for Web3 Apps',
        # GEO batch B4
        ('401-stablecoins.md', 'who-owns-the-market'): 'Who Owns the Stablecoin Market?',
        ('401-stablecoins.md', 'what-about-decentralized-alternatives'): 'What About Decentralized Stablecoin Alternatives?',
        ('402-decentralized-finance.md', 'why-finance-first'): 'Why Finance First in Web3?',
        ('402-decentralized-finance.md', 'what-stands-in-the-way-of-growth'): 'What stands in the way of DeFi’s growth?',
        ('402-decentralized-finance.md', 'the-path-to-adoption'): 'The Path to DeFi Adoption',
        ('406-digital-identity.md', 'will-blockchain-be-the-cure'): 'Will blockchain be the cure for digital identity?',
        ('406-digital-identity.md', 'how-it-works-in-practice'): 'How Digital Identity Works in Practice',
        ('407-physical-infrastructure.md', 'where-does-crypto-come-in'): 'Where Does Crypto Come In for DePIN?',
        ('408-regenerative-finance.md', 'how-blockchain-helps'): 'How Blockchain Helps ReFi',
        # GEO batch B5
        ('410-ai-meets-web3.md', 'where-opposites-attract'): 'Where Opposites Attract: Blockchain and AI',
        ('413-terra-implosion.md', 'what-happened-next'): 'What Happened Next to UST?',
        ('413-terra-implosion.md', 'trust-is-everything'): 'Trust Is Everything for Stablecoins',
        ('414-3ac-bankruptcy.md', 'how-it-started'): 'How the 3AC Bankruptcy Started',
        ('415-ftx-collapse.md', 'what-happened'): 'What Happened to FTX?',
        # GEO batch B6
        ('501-tokens.md', 'cbdcs-programmable-money'): 'CBDCs: Programmable Money',
        ('503-blackrock-on-chain.md', 'the-real-strategy-tokenizing-everything'): 'BlackRock’s Real Strategy: Tokenizing Everything',
    },
}


# Link-target fixes (GEO batch B2): the manuscript wraps some targets in a Google search URL. Exact old target -> new target,
# per book profile, applied where hyperlinks are read (para_tokens). Each entry must apply exactly once or main() exits
# non-zero (counted once per source paragraph, like the CORRECTIONS lists).
LINK_TARGET_FIXES = {
    'en': {
        'https://www.google.com/search?q=https://uniswap.org/blog/uniswapx-protocol': 'https://uniswap.org/blog/uniswapx-protocol',
        'https://www.google.com/search?q=https://www.warren.senate.gov/oversight/letters/senators-warren-marshall-kennedy-release-new-information-renew-push-for-answers-from-silvergate-bank-over-role-in-ftx-collapse%23:~:text=On%252520December%2525206%25252C%2525202022%25252C%252520Senators,of%252520dollars%252520in%252520customer%252520funds.': 'https://www.warren.senate.gov/newsroom/press-releases/senators-warren-marshall-kennedy-release-new-information-renew-push-for-answers-from-silvergate-bank-over-role-in-ftx-collapse/',
        # GEO batch B3: cross-references to the author's Google Docs drafts -> the book's own pages
        'https://docs.google.com/document/d/1-Rf-rlm3lRqtTnjk41B7xTP6oG-_n9Li2MxWoxrVKRw/edit?pli=1&tab=t.0#heading=h.4afnykvvbdxe': '/Web3_Unlocked/chapter-4/terra-implosion/',
        # GEO batch B4: double-encoded Wikipedia link, on three pages (102, 406 and 407)
        'https://en.wikipedia.org/wiki/Facebook%25E2%2580%2593Cambridge_Analytica_data_scandal': 'https://en.wikipedia.org/wiki/Facebook%E2%80%93Cambridge_Analytica_data_scandal',
        # GEO batch B5: PYUSD 'launched' -> PayPal's own announcement
        'https://www.btchaber.com/paypaldan-stablecoin-adimi/': 'https://newsroom.paypal-corp.com/2023-08-07-PayPal-Launches-U-S-Dollar-Stablecoin',
    },
    'tr': {
        # GEO batch B3: cross-references to the author's Google Docs drafts -> the book's own pages
        'https://docs.google.com/document/d/1-Rf-rlm3lRqtTnjk41B7xTP6oG-_n9Li2MxWoxrVKRw/edit?pli=1&tab=t.0#heading=h.4afnykvvbdxe': '/Sorularla_Web3/bolum-4/terra-ust/',
        'https://docs.google.com/document/d/1-Rf-rlm3lRqtTnjk41B7xTP6oG-_n9Li2MxWoxrVKRw/edit?pli=1&tab=t.0#heading=h.11x2tby82xx6': '/Sorularla_Web3/bolum-4/3ac-iflasi/',
        'https://docs.google.com/document/d/1-Rf-rlm3lRqtTnjk41B7xTP6oG-_n9Li2MxWoxrVKRw/edit?pli=1&tab=t.0#heading=h.ady8ubskdz0u': '/Sorularla_Web3/bolum-4/ftx-batisi/',
        'https://docs.google.com/document/d/1nXVnAHjWh1ZJgeiEXESsYBE0b4tzmDcoRVwBuP7a88U/edit?tab=t.0#heading=h.hc6v4ww0l9l4': '/Sorularla_Web3/bolum-2/bitcoin-ikinci-seviye/',
        'https://docs.google.com/document/d/15gK0HBOOWCXaFLsgMWq8iU5eNcWX0DX4-biunxRLWKY/edit?tab=t.0#heading=h.ih27gnaxht20': '/Sorularla_Web3/bolum-2/ikinci-seviye-cozumler/',
        'https://docs.google.com/document/d/1nXVnAHjWh1ZJgeiEXESsYBE0b4tzmDcoRVwBuP7a88U/edit?tab=t.0#heading=h.k8wpuu9c1bq0': '/Sorularla_Web3/bolum-2/kopruler/',
        'https://docs.google.com/document/d/1nXVnAHjWh1ZJgeiEXESsYBE0b4tzmDcoRVwBuP7a88U/edit?tab=t.0#heading=h.vl2qdgkyp4lf': '/Sorularla_Web3/bolum-2/intentler/',
        'https://docs.google.com/document/d/1nXVnAHjWh1ZJgeiEXESsYBE0b4tzmDcoRVwBuP7a88U/edit?tab=t.0#heading=h.2qn41fbxvsqn': '/Sorularla_Web3/bolum-2/cuzdanlar/',
        # GEO batch B5: the manuscript has a bare domain that Word resolved against the old blog post's address
        'https://turansert.com/genel/2022/05/20/delphidigital.io': 'https://delphidigital.io',
        'https://turansert.com/genel/2023/03/31/chain.link': 'https://chain.link',
    },
}
LINK_TARGET_FIXES['tr'].update(BLACKROCK_URL_FIXES)    # GEO batch B6
LINK_TARGET_FIXES['en'].update(BLACKROCK_URL_FIXES)
# expected number of source paragraphs per link fix, default 1 (the Wikipedia link: 102, 406, 407)
LINK_FIX_EXPECTED = {'https://en.wikipedia.org/wiki/Facebook%25E2%2580%2593Cambridge_Analytica_data_scandal': 3}


def use_profile(name):
    global P, SITE_TITLE, URL_BASE, IMG_URL, CORRECTION_COUNTS
    P = PROFILES[name]
    SITE_TITLE, URL_BASE, IMG_URL = P['site_title'], P['url_base'], P['img_url']
    CORRECTION_COUNTS = {c[0]: 0 for c in P['corrections']}
    PROFILE_USES.clear()


PROFILE_USES = {}


TR = str.maketrans({'ç': 'c', 'Ç': 'c', 'ğ': 'g', 'Ğ': 'g', 'ı': 'i', 'İ': 'i', 'ö': 'o', 'Ö': 'o',
                    'ş': 's', 'Ş': 's', 'ü': 'u', 'Ü': 'u', 'â': 'a', 'Â': 'a', 'î': 'i', 'Î': 'i',
                    'û': 'u', 'Û': 'u'})


def slugify(text, max_words=None, max_len=None):
    t = text.translate(TR).lower()
    t = re.sub(r"[’'‘`´]", '', t)          # apostrophes are dropped, not turned into hyphens
    t = re.sub(r'[^a-z0-9]+', '-', t).strip('-')
    if max_words:
        t = '-'.join(t.split('-')[:max_words])
    if max_len and len(t) > max_len:
        t = t[:max_len].rsplit('-', 1)[0] if '-' in t[:max_len] else t[:max_len]
    return t


WARNINGS = []


def warn(msg):
    WARNINGS.append(msg)
    print('WARN:', msg, file=sys.stderr)


# ----------------------------------------------------------------------------------------------
# inline model: a Tok is a tuple-like object; rendering yields pieces with a markdown and an html form
class Tok:
    __slots__ = ('kind', 'text', 'b', 'i', 'url', 'inner', 'fid', 'rid')

    def __init__(self, kind, text='', b=False, i=False, url=None, inner=None, fid=None, rid=None):
        self.kind, self.text, self.b, self.i = kind, text, b, i
        self.url, self.inner, self.fid, self.rid = url, inner or [], fid, rid


class Piece:
    __slots__ = ('md', 'html', 'emph')

    def __init__(self, md, htm, emph=False):
        self.md, self.html, self.emph = md, htm, emph


def esc_md(text):
    out = []
    for k, c in enumerate(text):
        if c in '\\*_`[]<{}|':
            out.append('\\' + c)
        elif c == '&':
            out.append('\\&' if re.match(r'&(#\w+|\w+);', text[k:]) else '&')
        elif c == '$' and text[k:k + 2] == '$$':
            out.append('\\$')
        else:
            out.append(c)
    return ''.join(out)


def esc_html(text):
    return html.escape(text, quote=False)


def md_url(u):
    for a, b in ((' ', '%20'), ('(', '%28'), (')', '%29'), ('<', '%3C'), ('>', '%3E'), ('"', '%22'), ('\\', '%5C')):
        u = u.replace(a, b)
    return u


def line_start_escape(s):
    if not s:
        return s
    if s[0] in '#>-+|:~=':
        return '\\' + s
    m = re.match(r'^(\d+)([.)])(\s|$)', s)
    if m:
        return m.group(1) + '\\' + s[len(m.group(1)):]
    return s


def has_ws_only(t):
    return t.kind == 't' and t.text.strip() == ''


class Renderer:
    """Turns token lists into markdown/html. ctx supplies footnote numbering."""

    def __init__(self, ctx):
        self.ctx = ctx

    # -- helpers ------------------------------------------------------------------------------
    @staticmethod
    def normalize(toks, strip_bold=False):
        out = []
        for t in toks:
            if t.kind == 't':
                t = Tok('t', t.text, False if strip_bold else t.b, t.i)
                if t.text.strip() == '':
                    t.b = t.i = False
                elif P is not None and P['name'] == 'en' and t.b and not re.search(r'\w', t.text):
                    t.b = False         # a bold comma or dash is a stray formatting artefact
            if out and t.kind == 't' and out[-1].kind == 't' and (out[-1].b, out[-1].i) == (t.b, t.i):
                out[-1] = Tok('t', out[-1].text + t.text, t.b, t.i)
            elif t.kind == 'link' and strip_bold:
                t = Tok('link', url=t.url, inner=[Tok(x.kind, x.text, False, x.i, fid=x.fid) if x.kind == 't' else x for x in t.inner])
                out.append(t)
            elif out and t.kind == 'link' and out[-1].kind == 'link' and out[-1].url == t.url:
                out[-1] = Tok('link', url=t.url, inner=out[-1].inner + t.inner)
            else:
                out.append(t)
        return out

    @staticmethod
    def eff(t, flag):
        if t.kind == 't':
            return getattr(t, flag)
        if t.kind == 'link':
            inner = [x for x in t.inner if x.kind == 't' and x.text.strip()]
            return bool(inner) and all(getattr(x, flag) for x in inner) and \
                all(x.kind in ('t', 'fn') for x in t.inner)
        return False

    @staticmethod
    def unflag(t, flag):
        if t.kind != 'link':
            return t
        inner = [Tok('t', x.text, False if flag == 'b' else x.b, False if flag == 'i' else x.i) if x.kind == 't' else x
                 for x in t.inner]
        return Tok('link', url=t.url, inner=inner)

    # -- main ---------------------------------------------------------------------------------
    def render(self, toks, strip_bold=False):
        toks = self.normalize(toks, strip_bold)
        return self._groups(toks, 'b')

    def _groups(self, toks, flag):
        pieces = []
        k = 0
        while k < len(toks):
            on = self.eff(toks[k], flag)
            j = k
            while j < len(toks) and self.eff(toks[j], flag) == on:
                j += 1
            seg = toks[k:j]
            if on:
                pieces.extend(self._emph(seg, flag))
            elif flag == 'b':
                pieces.extend(self._groups(seg, 'i'))
            else:
                pieces.extend(self._plain(seg))
            k = j
        return pieces

    def _emph(self, seg, flag):
        # move edge whitespace out of the markers
        lead = trail = ''
        seg = list(seg)
        while seg and has_ws_only(seg[0]):
            lead += seg.pop(0).text
        while seg and has_ws_only(seg[-1]):
            trail = seg.pop().text + trail
        if seg and seg[0].kind == 't':
            s = seg[0].text.lstrip()
            lead += seg[0].text[:len(seg[0].text) - len(s)]
            seg[0] = Tok('t', s, seg[0].b, seg[0].i)
        if seg and seg[-1].kind == 't':
            s = seg[-1].text.rstrip()
            trail = seg[-1].text[len(s):] + trail
            seg[-1] = Tok('t', s, seg[-1].b, seg[-1].i)
        seg = [self.unflag(t, flag) for t in seg]
        pieces = []
        if lead:
            pieces.append(Piece(esc_md(lead), esc_html(lead)))
        if seg:
            if flag == 'b':
                inner = self._groups(seg, 'i')
                tag, mk = 'strong', '**'
            else:
                inner = self._plain(seg)
                tag, mk = 'em', '*'
            imd = join_pieces(inner, 'md')
            ihtml = join_pieces(inner, 'html')
            lead2 = imd[:len(imd) - len(imd.lstrip())]       # whitespace that came from inside a link
            trail2 = imd[len(imd.rstrip()):]
            if lead2 or trail2:
                imd, ihtml = imd.strip(), ihtml.strip()
                if lead2:
                    pieces.append(Piece(lead2, lead2))
            if imd.startswith('*') or imd.endswith('*'):
                md = '<%s>%s</%s>' % (tag, ihtml, tag)
            else:
                md = mk + imd + mk
            pieces.append(Piece(md, '<%s>%s</%s>' % (tag, ihtml, tag), True))
            if trail2:
                pieces.append(Piece(trail2, trail2))
        if trail:
            pieces.append(Piece(esc_md(trail), esc_html(trail)))
        return pieces

    def _plain(self, seg):
        out = []
        for t in seg:
            if t.kind == 't':
                out.append(Piece(esc_md(t.text), esc_html(t.text)))
            elif t.kind == 'br':
                out.append(Piece('<br>', '<br>'))
            elif t.kind == 'fn':
                n = self.ctx.footnote_number(t.fid)
                out.append(Piece('[^%d]' % n, ''))
            elif t.kind == 'link':
                inner = self._groups(self.normalize(t.inner), 'b')
                imd = join_pieces(inner, 'md')
                ihtml = join_pieces(inner, 'html')
                lead = imd[:len(imd) - len(imd.lstrip())]
                trail = imd[len(imd.rstrip()):]
                imd, ihtml = imd.strip(), ihtml.strip()
                if not imd:
                    warn('link with empty text: %s' % t.url)
                    imd, ihtml = esc_md(t.url), esc_html(t.url)
                out.append(Piece(lead + '[%s](%s)' % (imd, md_url(t.url)) + trail,
                                 lead + '<a href="%s">%s</a>' % (html.escape(t.url, quote=True), ihtml) + trail))
        return out


def join_pieces(pieces, form):
    acc = ''
    for p in pieces:
        s = p.md if form == 'md' else p.html
        if form == 'md' and p.emph and acc.endswith('*') and s.startswith('*'):
            s = p.html
        acc += s
    return acc


def plain_text(toks):
    out = []
    for t in toks:
        if t.kind == 't':
            out.append(t.text)
        elif t.kind == 'link':
            out.append(plain_text(t.inner))
        elif t.kind == 'br':
            out.append(' ')
    return re.sub(r'\s+', ' ', ''.join(out)).strip()


# ----------------------------------------------------------------------------------------------
def flat_text(toks):
    """text tokens of a paragraph, including those inside links (link URLs are never included)"""
    out = []
    for t in toks:
        if t.kind == 't':
            out.append(t)
        elif t.kind == 'link':
            out.extend(x for x in t.inner if x.kind == 't')
    return out


class Docx:
    def __init__(self, path):
        self.z = zipfile.ZipFile(path)
        st = ET.fromstring(self.z.read('word/styles.xml'))
        self.styles = {s.get(W + 'styleId'): s.find(W + 'name').get(W + 'val')
                       for s in st.iter(W + 'style') if s.find(W + 'name') is not None}
        self.doc = ET.fromstring(self.z.read('word/document.xml'))
        self.body = self.doc.find(W + 'body')
        self.cstyle = {}          # character style id -> (bold, italic) as defined in styles.xml
        for st_el in st.iter(W + 'style'):
            if st_el.get(W + 'type') == 'character':
                rp = st_el.find(W + 'rPr')
                if rp is not None:
                    self.cstyle[st_el.get(W + 'styleId')] = (self.flag(rp, 'b'), self.flag(rp, 'i'))
        self.rels = self._rels('word/_rels/document.xml.rels')
        self.fn_rels = self._rels('word/_rels/footnotes.xml.rels')
        self.footnotes = {}
        fx = ET.fromstring(self.z.read('word/footnotes.xml')) if 'word/footnotes.xml' in self.z.namelist() \
            else ET.Element('footnotes')
        for f in fx.findall(W + 'footnote'):
            if f.get(W + 'type') in ('separator', 'continuationSeparator', 'continuationNotice'):
                continue
            self.footnotes[int(f.get(W + 'id'))] = f
        self.numfmt = self._numbering()

    def _rels(self, name):
        d = {}
        if name in self.z.namelist():
            for r in ET.fromstring(self.z.read(name)).findall(PKG + 'Relationship'):
                d[r.get('Id')] = (r.get('Target'), r.get('TargetMode'), r.get('Type').rsplit('/', 1)[-1])
        return d

    def _numbering(self):
        nx = ET.fromstring(self.z.read('word/numbering.xml'))
        ns = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
        absfmt = {}
        for an in nx.iter(ns + 'abstractNum'):
            lv = {}
            for l in an.findall(ns + 'lvl'):
                nf = l.find(ns + 'numFmt')
                lv[int(l.get(ns + 'ilvl'))] = nf.get(ns + 'val') if nf is not None else 'bullet'
            absfmt[an.get(ns + 'abstractNumId')] = lv
        res = {}
        for n in nx.iter(ns + 'num'):
            res[n.get(ns + 'numId')] = absfmt[n.find(ns + 'abstractNumId').get(ns + 'val')]
        return res

    def style(self, p):
        ps = p.find(W + 'pPr/' + W + 'pStyle')
        return self.styles.get(ps.get(W + 'val'), 'Normal') if ps is not None else 'Normal'

    # -- inline extraction --------------------------------------------------------------------
    @staticmethod
    def flag(rpr, name):
        if rpr is None:
            return False
        e = rpr.find(W + name)
        return e is not None and e.get(W + 'val') not in ('0', 'false')

    def run_tokens(self, r, rels):
        rpr = r.find(W + 'rPr')
        b, i = self.flag(rpr, 'b'), self.flag(rpr, 'i')
        rs = rpr.find(W + 'rStyle') if rpr is not None else None
        if rs is not None and rs.get(W + 'val') in self.cstyle:       # e.g. "Emphasis" / "Strong"
            cb, ci = self.cstyle[rs.get(W + 'val')]
            b, i = b or cb, i or ci
        toks = []
        buf = ''
        for ch in r:
            tag = ch.tag
            if tag == W + 't':
                buf += ch.text or ''
            elif tag == W + 'tab':
                buf += ' '
            elif tag == W + 'br':
                if ch.get(W + 'type') in (None, 'textWrapping'):
                    if buf:
                        toks.append(Tok('t', buf, b, i)); buf = ''
                    toks.append(Tok('br'))
            elif tag == W + 'footnoteReference':
                if buf:
                    toks.append(Tok('t', buf, b, i)); buf = ''
                toks.append(Tok('fn', fid=int(ch.get(W + 'id'))))
            elif tag == W + 'drawing':
                if buf:
                    toks.append(Tok('t', buf, b, i)); buf = ''
                blip = ch.find('.//' + A + 'blip')
                toks.append(Tok('img', rid=blip.get(R + 'embed')))
            elif tag == W + 'pict' and ch.find('.//{urn:schemas-microsoft-com:vml}rect') is not None:
                if buf:
                    toks.append(Tok('t', buf, b, i)); buf = ''
                toks.append(Tok('hr'))
            elif tag == '{http://schemas.openxmlformats.org/markup-compatibility/2006}AlternateContent':
                # a horizontal-rule shape (grey "Rectangle" with an image fallback): keep as a divider
                if buf:
                    toks.append(Tok('t', buf, b, i)); buf = ''
                toks.append(Tok('hr'))
            elif tag in (W + 'rPr', W + 'footnoteRef', W + 'lastRenderedPageBreak'):
                pass
            else:
                warn('unhandled run child %s' % tag)
        if buf:
            toks.append(Tok('t', buf, b, i))
        return toks

    def para_tokens(self, p, rels):
        toks = self._para_tokens_raw(p, rels)
        first = id(p) not in _COUNTED
        _COUNTED.add(id(p))
        fixes = LINK_TARGET_FIXES.get(P['name'], {})
        if fixes:
            link_first = p not in _LINK_SEEN      # the set keeps the element alive, so a re-read of the same paragraph is recognised
            _LINK_SEEN.add(p)
            hit_urls = set()                       # a link split in two runs/hyperlinks (same target) counts once per paragraph
            def fix_links(ts):
                for t in ts:
                    if t.kind == 'link':
                        if t.url in fixes:
                            if link_first and t.url not in hit_urls:
                                hit_urls.add(t.url)
                                PROFILE_USES[('link fix', t.url)] = PROFILE_USES.get(('link fix', t.url), 0) + 1
                            t.url = fixes[t.url]
                        fix_links(t.inner)
            fix_links(toks)
        joined = ''.join(t.text for t in flat_text(toks))
        for corr in P['corrections']:
            old, new = corr[0], corr[1]
            anchored = len(corr) > 2 and corr[2] == 'start'
            every = len(corr) > 2 and corr[2] == 'all'      # replace every occurrence in the paragraph (each inside one run)
            n = (1 if joined.startswith(old) else 0) if anchored else joined.count(old)
            if not n:
                continue
            if first:
                CORRECTION_COUNTS[old] += n
            hit = [t for t in flat_text(toks) if old in t.text]
            if every:
                if sum(t.text.count(old) for t in hit) != n:
                    raise SystemExit('correction %r has an occurrence that does not lie inside a single text run' % old)
                for t in hit:
                    t.text = t.text.replace(old, new)
                joined = ''.join(t.text for t in flat_text(toks))
                continue
            if anchored and hit and not hit[0].text.startswith(old):
                raise SystemExit('anchored correction %r does not start the paragraph' % old)
            if len(hit) != 1 or hit[0].text.count(old) != 1:
                raise SystemExit('correction %r does not lie inside a single text run' % old)
            hit[0].text = hit[0].text.replace(old, new)
            joined = ''.join(t.text for t in flat_text(toks))
        return toks

    def _flat(self, parent):
        """children of a paragraph with tracked changes accepted: insertions are kept, deletions dropped"""
        for ch in parent:
            if ch.tag in (W + 'ins', W + 'smartTag'):
                yield from self._flat(ch)
            elif ch.tag in (W + 'del', W + 'moveFrom', W + 'commentRangeStart', W + 'commentRangeEnd'):
                continue
            elif ch.tag == W + 'moveTo':
                yield from self._flat(ch)
            else:
                yield ch

    def _para_tokens_raw(self, p, rels):
        toks = []
        stack = []               # complex fields (fldChar begin/separate/end), e.g. HYPERLINK "url"

        def close_field():
            f = stack.pop()
            res = f['toks']
            m = re.search(r'HYPERLINK\s+"([^"]*)"(?:\s+\\l\s+"([^"]*)")?', f['instr'])
            if m:
                url = m.group(1) + ('#' + m.group(2) if m.group(2) else '')
                imgs = [t for t in res if t.kind == 'img']
                rest = [t for t in res if t.kind != 'img']
                has_text = any(t.kind in ('t', 'fn') and (t.kind == 'fn' or t.text.strip()) for t in rest)
                if imgs:
                    warn('image inside a field hyperlink to %s: the image is kept, the link is not' % url)
                if has_text:
                    res = imgs + [Tok('link', url=url, inner=rest)]
                else:
                    res = imgs + rest
                    if not imgs:
                        warn('empty field link %r' % f['instr'].strip())
            (stack[-1]['toks'] if stack and stack[-1]['phase'] == 'result' else toks).extend(res)

        for ch in self._flat(p):
            if ch.tag == W + 'r' and (ch.find(W + 'fldChar') is not None or ch.find(W + 'instrText') is not None):
                for sub in ch:              # one run may hold begin + instrText + separate
                    if sub.tag == W + 'fldChar':
                        kind = sub.get(W + 'fldCharType')
                        if kind == 'begin':
                            stack.append({'instr': '', 'phase': 'instr', 'toks': []})
                        elif kind == 'separate' and stack:
                            stack[-1]['phase'] = 'result'
                        elif kind == 'end' and stack:
                            close_field()
                    elif sub.tag == W + 'instrText' and stack:
                        stack[-1]['instr'] += sub.text or ''
                continue
            if ch.tag == W + 'r' and stack:
                if stack[-1]['phase'] == 'result':
                    stack[-1]['toks'].extend(self.run_tokens(ch, rels))
                continue
            if ch.tag == W + 'r':
                toks.extend(self.run_tokens(ch, rels))
            elif ch.tag == W + 'hyperlink':
                rid = ch.get(R + 'id')
                if rid is None:
                    # internal cross-reference: resolved to the site permalink of the target page after conversion
                    inner = []
                    for r in ch.findall(W + 'r'):
                        inner.extend(self.run_tokens(r, rels))
                    toks.append(Tok('link', url='#bm:' + (ch.get(W + 'anchor') or ''), inner=inner))
                    continue
                target, mode, _ = rels[rid]
                inner = []
                for r in ch.findall(W + 'r'):
                    inner.extend(self.run_tokens(r, rels))
                imgs = [t for t in inner if t.kind == 'img']       # a linked image: keep the image, not the link
                if imgs:
                    warn('image inside a hyperlink to %s: the image is kept, the link is not' % target)
                    toks.extend(imgs)
                    inner = [t for t in inner if t.kind != 'img']
                    if not any(t.kind == 't' and t.text.strip() for t in inner):
                        continue
                toks.append(Tok('link', url=target, inner=inner))
            elif ch.tag in (W + 'pPr', W + 'bookmarkStart', W + 'bookmarkEnd', W + 'proofErr'):
                pass
            else:
                warn('unhandled paragraph child %s' % ch.tag)
        while stack:            # a field that continues into the next paragraph: close it here
            close_field()
        return toks


def strip_italic(toks):
    out = []
    for t in toks:
        if t.kind == 'link':
            out.append(Tok('link', url=t.url, inner=[Tok(x.kind, x.text, x.b, False, x.url, x.inner, x.fid, x.rid) for x in t.inner]))
        else:
            out.append(Tok(t.kind, t.text, t.b, False, t.url, t.inner, t.fid, t.rid))
    return out


def force_italic(toks):
    out = []
    for t in toks:
        if t.kind == 'link':
            out.append(Tok('link', url=t.url, inner=[Tok(x.kind, x.text, x.b, True, x.url, x.inner, x.fid, x.rid)
                                                      if x.kind == 't' else x for x in t.inner]))
        elif t.kind == 't':
            out.append(Tok('t', t.text, t.b, True))
        else:
            out.append(t)
    return out


def is_caption(toks):
    """a figure caption right after an image: mostly italic, or (profile bc) a short 'Image by / Kaynak' line"""
    if italic_fraction(toks) >= 0.5:
        return True
    if P.get('plain_captions'):
        tx = plain_text(toks)
        return bool(re.match(r'^(Image by|Photo by|Kaynak)', tx)) and len(tx) < 150
    return False


def italic_fraction(toks):
    tot = it = 0
    for t in flat_text(toks):
        n = len(t.text.strip())
        tot += n
        if t.i:
            it += n
    return it / tot if tot else 0.0


def clean_edges(toks):
    """collapse whitespace runs; strip paragraph edges."""
    split = []
    for t in toks:          # a footnote reference inside a link text: split the link around it
        if t.kind == 'link' and any(x.kind == 'fn' for x in t.inner):
            seg = []
            for x in t.inner:
                if x.kind == 'fn':
                    if seg:
                        split.append(Tok('link', url=t.url, inner=seg))
                    split.append(x)
                    seg = []
                else:
                    seg.append(x)
            if seg:
                split.append(Tok('link', url=t.url, inner=seg))
        else:
            split.append(t)
    toks = split
    hoisted = []
    for t in toks:          # line breaks at the edges of a link text belong outside the link
        if t.kind == 'link' and t.inner and (t.inner[0].kind in ('br', 'fn') or t.inner[-1].kind in ('br', 'fn')):
            inner = list(t.inner)
            pre, post = [], []
            while inner and inner[0].kind in ('br', 'fn'):
                pre.append(inner.pop(0))
            while inner and inner[-1].kind in ('br', 'fn'):
                post.insert(0, inner.pop())
            hoisted.extend(pre + [Tok('link', url=t.url, inner=inner)] + post)
        else:
            hoisted.append(t)
    toks = hoisted
    toks = [Tok(t.kind, re.sub(r'[ \t\r\n ]+', ' ', t.text) if t.kind == 't' else t.text,
                t.b, t.i, t.url, t.inner, t.fid, t.rid) for t in toks]
    # collapse across token boundaries
    prev_space = True
    for t in toks:
        if t.kind == 't':
            if prev_space and t.text.startswith(' '):
                t.text = t.text.lstrip(' ')
            prev_space = t.text.endswith(' ') if t.text else prev_space
        elif t.kind == 'br':
            prev_space = True
        else:
            prev_space = False
    while toks and ((toks[0].kind == 't' and not toks[0].text.strip()) or toks[0].kind == 'br'):
        toks.pop(0)
    while toks and ((toks[-1].kind == 't' and not toks[-1].text.strip()) or toks[-1].kind == 'br'):
        toks.pop()
    if toks and toks[0].kind == 't':
        toks[0].text = toks[0].text.lstrip()
    if toks and toks[-1].kind == 't':
        toks[-1].text = toks[-1].text.rstrip()
    return toks


# ----------------------------------------------------------------------------------------------
class Page:
    def __init__(self, kind, order, chapter, chapter_title, heading, slug, title):
        self.kind, self.order, self.chapter = kind, order, chapter
        self.chapter_title, self.heading, self.slug, self.title = chapter_title, heading, slug, title
        self.blocks = []        # markdown blocks
        self.plain = []         # plain text of ordinary paragraphs (for description)
        self.fn_ids = []        # docx footnote ids in order of reference
        self.heading_ids = set()
        self.img_n = 0
        self.stats = {'figures': 0, 'h3': 0, 'links': 0, 'fn_defs': 0}
        self.captionless = []

    def footnote_number(self, fid):
        if fid in self.fn_ids:
            warn('footnote %d referenced twice on page %s' % (fid, self.slug))
            return self.fn_ids.index(fid) + 1
        self.fn_ids.append(fid)
        return len(self.fn_ids)

    def unique_id(self, text):
        base = slugify(text, max_len=80) or 'baslik'
        if not base[0].isalpha():       # kramdown only accepts {#id} starting with a letter
            base = 'b-' + base
        cand, n = base, 2
        while cand in self.heading_ids:
            cand = '%s-%d' % (base, n)
            n += 1
        self.heading_ids.add(cand)
        return cand

    @property
    def filename(self):
        return '%03d-%s.md' % (self.order, self.slug)

    @property
    def permalink(self):
        if self.kind == 'chapter':
            return '%s/%s/' % (URL_BASE, P['chapter_slug'] % self.chapter)
        if self.chapter == 0:
            return '%s/%s/' % (URL_BASE, P['intro_slug'])
        return '%s/%s/%s/' % (URL_BASE, P['chapter_slug'] % self.chapter, self.slug)


def yq(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def make_description(page):
    text = ' '.join(page.plain[:6])
    text = re.sub(r'\s+', ' ', text).strip()
    if not text:
        return None
    sents = re.split(r'(?<=[.!?])\s+(?=[A-ZÇĞİÖŞÜ“‘"\'(0-9])', text)
    if len(sents) > 1 and len(sents[0]) < 15:      # drop a bare greeting such as "Merhaba!"
        sents = sents[1:]
    out = ''
    for s in sents:
        cand = (out + ' ' + s).strip()
        if len(cand) <= 160:
            out = cand
            if len(out) >= 110:
                break
        else:
            break
    if not out:
        cut = text[:157]
        cut = cut.rsplit(' ', 1)[0] if ' ' in cut else cut
        out = cut.rstrip(' ,;:–-') + '…'
    return out


def front_matter(page):
    desc = make_description(page)
    if not desc:
        desc = P['chapter_desc'] % (page.chapter, page.chapter_title)
    lines = ['---', 'layout: book-section', 'kind: ' + page.kind,
             'title: ' + yq(page.title), 'heading: ' + yq(page.heading), 'chapter: %d' % page.chapter,
             'chapter_title: ' + yq(page.chapter_title), 'order: %d' % page.order,
             'permalink: ' + page.permalink, 'description: ' + yq(desc), '---', '']
    return '\n'.join(lines)


# ----------------------------------------------------------------------------------------------
def img_dims(path):
    with open(path, 'rb') as f:
        d = f.read()
    if d[:8] == b'\x89PNG\r\n\x1a\n':
        return struct.unpack('>II', d[16:24])
    if d[:2] == b'\xff\xd8':
        k = 2
        while k < len(d):
            if d[k] != 0xFF:
                k += 1
                continue
            m = d[k + 1]
            if m in (0xD8, 0x01) or 0xD0 <= m <= 0xD7:
                k += 2
                continue
            ln = struct.unpack('>H', d[k + 2:k + 4])[0]
            if m in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                h, w = struct.unpack('>HH', d[k + 5:k + 9])
                return w, h
            k += 2 + ln
    raise ValueError('cannot read image size: ' + path)


class PrintedText:
    """The printed book (PDF) as a word stream, used to give plain body paragraphs their final printed wording.

    pdftotext -layout is cleaned (running headers, page numbers, footnote blocks, known headings/captions dropped,
    line-end hyphenation joined when the joined word exists in the book text), then every docx paragraph is aligned in
    reading order with a monotonic pointer. A paragraph is replaced only if it is plain (no links, uniform
    formatting), word similarity (difflib, ignoring case, punctuation and a/â) is >= 0.90 and the word-count ratio is
    0.85..1.15. Everything is deterministic."""

    HEADERS = ('SORULARLA DEFI', 'MERKEZİYETSİZ FİNANS')

    @staticmethod
    def key(t):
        t = t.replace('İ', 'i').replace('I', 'ı').lower()
        t = t.translate(str.maketrans('âîûêô', 'aiueo')).replace('ı', 'i')
        return re.sub(r'[^0-9a-zçğöşü]+', '', t)

    def __init__(self, pdf, heading_texts, caption_texts, vocab_texts, cfg=None):
        cfg = cfg or dict(layout=True, start='NEDİR DEFI?', headers=self.HEADERS)
        self.lookback = cfg.get('lookback', 0)          # how far behind the pointer an anchor may be (two columns)
        self.multi_end = cfg.get('multi_end', False)
        self.keep_punct = cfg.get('keep_punct', False)  # keep stand-alone punctuation tokens ("-", "...") in the text
        self.strict = cfg.get('strict', False)          # extra guards for an unreliable text layer (dashes, glued words)
        out = subprocess.run(['/opt/homebrew/bin/pdftotext'] + (['-layout'] if cfg['layout'] else []) + [pdf, '-'],
                             check=True, capture_output=True).stdout.decode('utf-8')
        heads = set(self.key(h) for h in heading_texts if self.key(h))
        caps = set(self.key(c) for c in caption_texts if self.key(c))
        pages = out.split('\f')
        lines_all = []
        started = False
        for pg in pages:
            lines = [l.rstrip() for l in pg.split('\n')]
            while lines and not lines[0].strip():
                lines.pop(0)
            while lines and not lines[-1].strip():
                lines.pop()
            if not lines:
                continue
            if not started:
                if any(l.strip() == cfg['start'] for l in lines):
                    started = True
                else:
                    continue
            if cfg['layout']:
                if lines and lines[0].strip() in cfg['headers']:
                    lines.pop(0)
                if lines and re.fullmatch(r'\d{1,3}', lines[-1].strip()):
                    lines.pop()
                # footnote block at the page bottom: unindented "N. text" after a blank line, to the end of the page
                for k, l in enumerate(lines):
                    if re.match(r'^\d{1,2}\.\s+\S', l) and k > 0 and not lines[k - 1].strip():
                        lines = lines[:k]
                        break
            else:
                # reading-order text of a two-column layout: page numbers ("009") are dropped; the footnotes at the
                # bottom start with a number glued to the text ("1http://...", "2Why ...") and run to the page end
                lines = [l for l in lines if not re.fullmatch(r'\d{3}', l.strip())]
                for k, l in enumerate(lines):
                    if k >= len(lines) // 3 and re.match(r'^\d{1,3}(?:https?://|www\.|[^\W\d_])', l.strip()):
                        lines = lines[:k]
                        break
            lines_all.extend(l.strip() for l in lines if l.strip())
        # drop known heading / caption lines (1-3 consecutive lines whose joined text equals one)
        keep = []
        i = 0
        while i < len(lines_all):
            hit = 0
            for k in (1, 2, 3):
                if i + k <= len(lines_all):
                    kk = self.key(' '.join(lines_all[i:i + k]))
                    if kk and (kk in heads or kk in caps):
                        hit = k
                        break
            if hit:
                i += hit
            else:
                keep.append(lines_all[i])
                i += 1
        toks = ' '.join(keep).split(' ')
        toks = [t for t in toks if t]
        # soft hyphenation: join when the joined word exists elsewhere in the book text
        vocab = set()
        for t in vocab_texts:
            for w in t.split():
                vocab.add(self.key(w))
        for t in toks:
            if not t.endswith('-'):
                vocab.add(self.key(t))
        words = []
        for t in toks:
            if words and words[-1].endswith('-') and len(words[-1]) > 1 and t[:1].islower():
                a = words[-1][:-1]
                joined = a + t
                if self.key(joined) in vocab or self.key(a + '-' + t) not in vocab:
                    words[-1] = joined
                else:
                    words[-1] = a + '-' + t
            else:
                words.append(t)
        self.words = [w for w in words if self.key(w) or self.keep_punct]
        self.keys = [self.key(w) for w in self.words]
        self.vocab = vocab
        self.pos = 0

    def join(self, toks):
        if not self.keep_punct:
            return ' '.join(toks)
        res = ''
        for t in toks:        # a stray punctuation token belongs to the word before it
            res += (t if (res and re.fullmatch(r'[.,;:!?)’”…]+', t)) else (' ' + t if res else t))
        return res

    @staticmethod
    def _footnote_free(p_tok, d_tok):
        """printed token p_tok aligned with docx token d_tok: keep a trailing digit only if the docx has it"""
        m = re.match(r'^(.*[^\W\d_\s])(\d{1,2})$', p_tok)
        if m and not re.search(r'\d{1,2}$', d_tok or ''):
            return m.group(1)
        return p_tok

    def align(self, text, marks=None):
        """-> (printed_text or None, info dict). marks: docx word positions (0..n) of footnote references; info['marks']
        then holds the matching positions in the printed word list info['out']."""
        dw = text.split()
        dk = [self.key(w) for w in dw]
        if not self.keep_punct:
            dk2 = [k for k in dk if k]
            dw = [w for w, k in zip(dw, dk) if k]
            dk = dk2
        elif self.strict and re.search('[—–]', text):
            return None, {'n': len(dk), 'reason': 'dash'}      # the print renders spaced dashes differently
        n = len(dk)
        info = {'n': n}
        if n < 6:
            info['reason'] = 'short'
            return None, info
        P = self.keys
        k0 = min(8, n)
        best, bs = -1, 0
        lo = max(0, self.pos - self.lookback)
        hi = min(len(P), self.pos + 600)
        for st in range(lo, hi):
            sc = sum(1 for j in range(k0) if st + j < len(P) and P[st + j] == dk[j])
            if sc > best:
                best, bs = sc, st
        if best < max(3, k0 // 2):
            # fall back: exact 5-gram of the first words anywhere ahead
            g = dk[:5]
            bs = -1
            for st in range(lo, min(len(P) - 4, self.pos + 4000)):
                if P[st:st + 5] == g:
                    bs = st
                    break
            if bs < 0:
                info['reason'] = 'no anchor'
                return None, info
        s = bs
        win = P[s:s + int(n * 1.4) + 10]
        sm_ = difflib.SequenceMatcher(None, dk, win, autojunk=False)
        blocks = [b for b in sm_.get_matching_blocks() if b.size]
        if not blocks:
            info['reason'] = 'no anchor'
            return None, info
        last = blocks[-1]
        cands = set()
        cands.add(s + last.b + last.size + max(0, n - (last.a + last.size)))
        cands.add(s + last.b + last.size)
        if self.multi_end:          # also try the ends implied by the last few solid matching blocks
            for blk in [b for b in blocks if b.size >= 2][-4:]:
                cands.add(s + blk.b + blk.size + max(0, n - (blk.a + blk.size)))
                cands.add(s + blk.b + blk.size)
        bestr, be = -1, None
        for e in sorted(cands):
            e = min(e, len(P))
            r = difflib.SequenceMatcher(None, dk, P[s:e], autojunk=False).ratio()
            if r > bestr:
                bestr, be = r, e
        for sh in (1, 2, 3):        # the anchor may sit a few words late: the print may begin with the docx's first word
            s2 = s - sh
            if s2 >= lo and P[s2] == dk[0]:
                r2 = difflib.SequenceMatcher(None, dk, P[s2:be], autojunk=False).ratio()
                if r2 > bestr:
                    bestr, s = r2, s2
        info.update(ratio=bestr, start=s, end=be, plen=be - s)
        lr = (be - s) / n
        info['lenratio'] = lr
        if bestr < 0.90:
            info['reason'] = 'similarity < 0.90'
            return None, info
        if not (0.85 <= lr <= 1.15):
            info['reason'] = 'length ratio'
            return None, info
        # build the printed text, dropping footnote markers that the docx does not have
        ps, pk = self.words[s:be], P[s:be]
        sm2 = difflib.SequenceMatcher(None, dk, pk, autojunk=False)
        for tag, a0, a1, b0, b1 in sm2.get_opcodes():
            if tag != 'equal' and (a1 - a0 >= 6 or b1 - b0 >= 6):
                info['reason'] = 'large local difference'
                return None, info
            if tag != 'equal' and self.strict and re.search('[-–—]', ' '.join(dw[a0:a1])) and \
                    not re.search('[-–—]', ' '.join(ps[b0:b1])):
                info['reason'] = 'dash lost in the print text layer'
                return None, info
            if tag != 'equal' and self.strict and re.search('[a-zçğıöşü][A-ZÇĞİÖŞÜ]', ' '.join(ps[b0:b1])) and \
                    not re.search('[a-zçğıöşü][A-ZÇĞİÖŞÜ]', ' '.join(dw[a0:a1])):
                info['reason'] = 'words glued together in the print text layer'
                return None, info
        out = []
        spans = []
        ops = sm2.get_opcodes()
        for oi, (tag, a0, a1, b0, b1) in enumerate(ops):
            o0 = len(out)
            if tag == 'equal':
                for x, y in zip(range(a0, a1), range(b0, b1)):
                    out.append(self._footnote_free(ps[y], dw[x]))
            elif tag == 'delete' and (oi == 0 or oi == len(ops) - 1) and any(dk[a0:a1]):
                # words at the very edge of the paragraph that the chosen print span lacks: keep the docx words
                # (a delete in the middle is the print's copy-edit and stays dropped)
                out.extend(dw[a0:a1])
            elif tag == 'insert' and (oi == 0 or oi == len(ops) - 1) and any(pk[b0:b1]):
                pass    # print words before the paragraph's first word or after its last one: a neighbour's text
            elif tag in ('replace', 'insert'):
                for y in range(b0, b1):
                    t = ps[y]
                    m = re.match(r'^(.*[^\W\d_\s])(\d{1,2})$', t)
                    if m and self.key(t) not in self.vocab and self.key(m.group(1)) in self.vocab:
                        t = m.group(1)
                    out.append(t)
            spans.append((tag, a0, a1, o0, len(out)))
        if marks:
            qs = []
            for pm in marks:
                q = len(out)
                for tag, a0, a1, o0, o1 in spans:
                    if a0 <= pm <= a1:
                        edge = tag == 'delete' and o1 > o0
                        q = o0 + (pm - a0) if (tag == 'equal' or edge) else (o0 if pm == a0 else o1)
                        break
                qs.append(q)
            info['marks'] = qs
        info['out'] = out
        self.pos = max(self.pos, be)
        return self.join(out), info


class Converter:
    def __init__(self, docx_path, out_dir, img_dir):
        self.dx = Docx(docx_path)
        self.out_dir, self.img_dir = out_dir, img_dir
        self.pages = []
        self.img_in_bytes = 0
        self.img_out_bytes = 0
        self.img_files = []
        self.captionless = []
        self.report_links_raw = 0
        self.slugs_seen = {}

    # -- images -------------------------------------------------------------------------------
    def emit_image(self, page, rid):
        target = self.dx.rels[rid][0]
        src = 'word/' + target
        data = self.dx.z.read(src)
        ext = os.path.splitext(target)[1].lower()
        page.img_n += 1
        name = '%03d-%d%s' % (page.order, page.img_n, ext)
        final = os.path.join(self.img_dir, name)
        dest = os.path.join(self.img_dir, '.work-' + name)       # work on a copy; sips output is not byte-stable
        with open(dest, 'wb') as f:
            f.write(data)
        self.img_in_bytes += len(data)
        w, h = img_dims(dest)
        if w > MAX_IMG_W:
            subprocess.run(['sips', '--resampleWidth', str(MAX_IMG_W), dest], check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if ext in ('.jpg', '.jpeg'):
            tmp = dest + '.tmp'
            subprocess.run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '80', dest, '--out', tmp],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if os.path.getsize(tmp) < os.path.getsize(dest):
                os.replace(tmp, dest)
            else:
                os.remove(tmp)
        # keep an existing file when the new one is the same image re-encoded (same size in pixels, bytes within 0.1%)
        if os.path.exists(final) and img_dims(final) == img_dims(dest) and \
                abs(os.path.getsize(final) - os.path.getsize(dest)) <= max(8, os.path.getsize(final) // 1000):
            os.remove(dest)
        else:
            os.replace(dest, final)
        w, h = img_dims(final)
        self.img_out_bytes += os.path.getsize(final)
        self.img_files.append(name)
        return name, w, h

    def figure(self, page, rid, caption_toks, note_toks, alt=None):
        name, w, h = self.emit_image(page, rid)
        r = Renderer(page)
        cap_plain = plain_text(caption_toks)
        has_fn = any(t.kind == 'fn' for t in caption_toks + note_toks)
        if caption_toks:
            pc = r.render(caption_toks, strip_bold=True)
            cap_html = join_pieces(pc, 'md' if has_fn else 'html')
        else:
            cap_html = ''
        if alt is None:
            if not cap_plain:
                alt = ''
                page.captionless.append((page.filename, name, alt))
            else:
                alt = cap_plain
        note_html = join_pieces(r.render(note_toks), 'md' if has_fn else 'html') if note_toks else ''
        cap = ''
        if cap_html and note_html:
            cap = '<figcaption>%s <span class="fig-note">%s</span></figcaption>' % (cap_html, note_html)
        elif cap_html:
            cap = '<figcaption>%s</figcaption>' % cap_html
        elif note_html:
            cap = '<figcaption><span class="fig-note">%s</span></figcaption>' % note_html
        page.stats['figures'] += 1
        page.stats['links'] += sum(1 for t in caption_toks + note_toks if t.kind == 'link')
        if has_fn:      # footnote refs need markdown: kramdown parses the figcaption as span markdown
            cap = cap.replace('<figcaption>', '<figcaption markdown="span">')
            return ('<figure markdown="1">\n<a href="%s/%s"><img src="%s/%s" alt="%s" width="%d" height="%d" loading="lazy"></a>\n%s\n</figure>'
                    % (IMG_URL, name, IMG_URL, name, html.escape(alt, quote=True), w, h, cap))
        return ('<figure><a href="%s/%s"><img src="%s/%s" alt="%s" width="%d" height="%d" loading="lazy"></a>%s</figure>'
                % (IMG_URL, name, IMG_URL, name, html.escape(alt, quote=True), w, h, cap))

    # -- conversion ---------------------------------------------------------------------------
    def run(self):
        dx = self.dx
        page = None
        chapter, chapter_title = 0, ''
        sec_k = 0
        pending_label = None     # Tok list of a run-in label waiting for the next paragraph
        pending_caption = None   # Tok list
        list_items = []          # current list: (ilvl, ordered, toks)
        started = False
        en = P['name'] == 'en'
        df = P['name'] in ('df', 'bc')
        late = en or df          # figures are built after their caption (placeholder blocks)
        h1_i = h2_i = 0
        self.repl = {}
        self.bookmarks = {}      # bookmark name -> (page, heading id or None) of the place it marks
        anchor = [None, None]    # page and heading id the converter is currently at
        reg_cur, carry = [], []
        if P.get('printed_pdf'):
            self.align_printed()
        pending_title = None     # en: heading 5 (figure title) waiting for its image
        pending_fig = None       # en: figure waiting for an optional heading 6 caption
        demote_h2 = False        # en: the next heading 2 is a sub-heading of the current section page

        def flush_list():
            nonlocal list_items
            if not list_items:
                return
            counters = {}
            lines = []
            r = Renderer(page)
            plain_parts = []
            for ilvl, ordered, toks, _nid in list_items:
                toks = clean_edges(toks)
                for lv in [k for k in counters if k > ilvl]:
                    del counters[lv]
                counters[ilvl] = counters.get(ilvl, 0) + 1
                marker = '%d. ' % counters[ilvl] if ordered else '- '
                text = line_start_escape(join_pieces(r.render(toks), 'md'))
                lines.append(' ' * (4 * ilvl) + marker + text)
                page.stats['links'] += sum(1 for t in toks if t.kind == 'link')
            add_block('\n'.join(lines))
            list_items = []

        def add_block(md, plain=None):
            if '{{' in md or '{%' in md:
                md = '{% raw %}' + md + '{% endraw %}'
            page.blocks.append(md)
            if plain:
                page.plain.append(plain)

        def flush_label():
            nonlocal pending_label
            if pending_label is not None:
                r = Renderer(page)
                add_block('**%s**' % join_pieces(r.render(pending_label, strip_bold=True), 'md').rstrip())
                pending_label = None

        def flush_fig():
            nonlocal pending_fig
            if pending_fig is not None:
                f = pending_fig
                pending_fig = None
                main = f['title'] or f['caption'] or []
                notes = (f['caption'] or []) if f['title'] else []
                if f['note']:
                    if notes:
                        notes = notes + [Tok('t', ' ')]
                    elif f['title'] or f['caption']:
                        pass
                    notes = notes + f['note']
                f['page'].blocks[f['idx']] = self.figure(f['page'], f['rid'], main, notes)

        def flush_title():
            nonlocal pending_title
            if pending_title is not None:
                t = pending_title
                pending_title = None
                r = Renderer(page)
                hid = page.unique_id(plain_text(t))
                add_block('#### %s {#%s}' % (join_pieces(r.render(t, strip_bold=True), 'md'), hid))
                warn('heading 5 %r not followed by an image (kept as ####)' % plain_text(t))

        def new_page(kind, order, ch, cht, heading, slug, title):
            nonlocal page, pending_title
            flush_list()
            flush_label()
            flush_fig()
            if pending_title is not None and page is not None:
                flush_title()
            page = Page(kind, order, ch, cht, heading, slug, title)
            self.pages.append(page)
            anchor[0], anchor[1] = page, None

        children = list(dx.body)

        def register():
            for nm in reg_cur:
                self.bookmarks[nm] = (anchor[0], anchor[1])
            del reg_cur[:]

        for idx, el in enumerate(children):
            register()                      # bookmarks of the previous element: the converter state is now final
            if el.tag == W + 'bookmarkStart':
                carry.append(el.get(W + 'name'))
                continue
            if el.tag == W + 'bookmarkEnd':
                continue
            if started:
                if el.tag == W + 'p':
                    reg_cur.extend(b.get(W + 'name') for b in el.iter(W + 'bookmarkStart'))
                reg_cur.extend(carry)
            carry = []
            if el.tag == W + 'sdt':
                continue
            if el.tag == W + 'sectPr':
                continue
            if el.tag == W + 'tbl' and df:
                # layout tables around figures: an empty table is skipped, a one-text table is the caption
                if not started:
                    continue
                tps = [clean_edges(dx.para_tokens(tp, dx.rels)) for tp in el.iter(W + 'p')]
                tps = [t for t in tps if t]
                if not tps:
                    continue
                if len(tps) == 1 and pending_fig is not None and pending_fig['caption'] is None:
                    pending_fig['caption'] = strip_italic(tps[0])
                    continue
                raise SystemExit('unsupported table on page %s' % page.slug)
            if el.tag == W + 'tbl':
                if not started:
                    continue
                flush_list(); flush_label()
                self.handle_table(page, el, pending_caption)
                pending_caption = None
                continue
            if el.tag != W + 'p':
                warn('unhandled body element %s' % el.tag)
                continue
            raw_style = dx.style(el)
            style = P['style_alias'].get(raw_style, raw_style)
            is_lead = raw_style in P.get('lead_styles', ())
            if is_lead:
                style = 'Normal'
            if not started:
                if en:
                    if ''.join(t.text or '' for t in el.iter(W + 't')).strip() != P['intro_heading']:
                        continue
                elif style != 'heading 1':
                    continue
            toks_raw = dx.para_tokens(el, dx.rels)
            if is_lead:
                toks_raw = force_italic(toks_raw)
            text = plain_text(toks_raw)      # includes text inside links
            has_img = any(t.kind == 'img' for t in toks_raw)

            # ---- structure headings
            if en and style == 'Normal' and (text == P['intro_heading'] or re.match(r'^Chapter\s+\d+\s*:', text)):
                started = True
                text = re.sub(r'\s+', ' ', text)
                if text == P['intro_heading']:
                    chapter, chapter_title, sec_k = 0, text, 0
                    new_page('section', 0, 0, text, text, P['intro_slug'], '%s – %s' % (text, SITE_TITLE))
                else:
                    m = re.match(r'^Chapter\s+(\d+)\s*:\s*(.+)$', text)
                    chapter, chapter_title, sec_k = int(m.group(1)), m.group(2).strip(), 0
                    heading = P['chapter_label'] % (chapter, chapter_title)
                    new_page('chapter', chapter * 100, chapter, chapter_title, heading,
                             P['chapter_slug'] % chapter, '%s – %s' % (heading, SITE_TITLE))
                continue
            if late and has_img and not (style in ('heading 1', 'heading 2') and text):
                style = 'Normal'
            if en and started and chapter > 0 and style == 'Normal' and text in P['promote']:
                PROFILE_USES[('promote', text)] = PROFILE_USES.get(('promote', text), 0) + 1
                style = 'heading 2'
            if style in ('heading 1', 'heading 2') and not (en and style == 'heading 2' and chapter == 0):
                if not text:
                    if any(t.kind in ('img', 'fn', 'link') for t in toks_raw):
                        warn('empty %s paragraph %d has content' % (style, idx))
                    continue
                if any(t.kind in ('fn', 'img') for t in toks_raw):
                    warn('%s %r contains footnote/image' % (style, text))
                text = re.sub(r'\s+', ' ', text)
                if style == 'heading 2' and text in P['heading_overrides']:
                    PROFILE_USES[('heading', text)] = PROFILE_USES.get(('heading', text), 0) + 1
                    text = P['heading_overrides'][text]
                if df and style == 'heading 1':
                    started = True
                    printed = P['parts'][h1_i]
                    if PrintedText.key(text) != PrintedText.key(printed):
                        raise SystemExit('part heading %r does not match %r' % (text, printed))
                    h1_i += 1
                    chapter, chapter_title, sec_k = h1_i, printed, 0
                    new_page('chapter', chapter * 100, chapter, chapter_title, printed,
                             P['chapter_slug'] % chapter, '%s – %s' % (printed, SITE_TITLE))
                elif style == 'heading 1':
                    started = True
                    if text == 'Giriş':
                        chapter, chapter_title, sec_k = 0, 'Giriş', 0
                        new_page('section', 0, 0, 'Giriş', 'Giriş', 'giris', 'Giriş – ' + SITE_TITLE)
                    else:
                        m = re.match(r'^Bölüm\s+(\d+)\s*:\s*(.+)$', text)
                        if not m:
                            raise SystemExit('unexpected heading 1: %r' % text)
                        chapter, chapter_title, sec_k = int(m.group(1)), m.group(2).strip(), 0
                        heading = 'Bölüm %d: %s' % (chapter, chapter_title)
                        new_page('chapter', chapter * 100, chapter, chapter_title, heading,
                                 'bolum-%d' % chapter, '%s – %s' % (heading, SITE_TITLE))
                else:
                    if not started:
                        continue
                    if df:
                        printed = P['sections'][h2_i]
                        kt, kp = PrintedText.key(text), PrintedText.key(printed)
                        if kt != kp and not (P.get('heading_prefix') and kt.startswith(kp)):
                            raise SystemExit('section heading %r does not match printed %r' % (text, printed))
                        h2_i += 1
                        text = printed
                    if late and demote_h2:
                        demote_h2 = False
                        flush_list(); flush_label(); flush_fig(); flush_title()
                        add_block('## %s {#%s}' % (esc_md(text), page.unique_id(text)))
                        continue
                    if late:
                        j = idx + 1
                        while j < len(children) and children[j].tag == W + 'p' and not \
                                ''.join(t.text or '' for t in children[j].iter(W + 't')).strip():
                            j += 1
                        if j < len(children) and children[j].tag == W + 'p' and dx.style(children[j]) == 'heading 2' \
                                and ''.join(t.text or '' for t in children[j].iter(W + 't')).strip():
                            warn('heading 2 %r is followed directly by another heading 2: the next one becomes a ## sub-heading on this page' % text)
                            demote_h2 = True
                    sec_k += 1
                    if text in P['overrides']:
                        slug, title = P['overrides'][text]
                        title = title or text
                    else:
                        if text.startswith('Örnek:') or text.startswith('Case Study:'):
                            warn('prefixed heading without override: %r' % text)
                        slug, title = slugify(text, max_words=P['max_words']), text
                    key = (chapter, slug)
                    if key in self.slugs_seen:
                        warn('duplicate slug %s in chapter %d' % (slug, chapter))
                    self.slugs_seen[key] = True
                    new_page('section', chapter * 100 + sec_k, chapter, chapter_title, text, slug,
                             '%s – %s' % (title, SITE_TITLE))
                continue
            if not started:
                continue
            if not text and not has_img and any(t.kind == 'fn' for t in toks_raw) and \
                    all(t.kind == 'fn' or (t.kind == 't' and not t.text.strip()) for t in toks_raw):
                # a paragraph that holds only footnote references: they belong to the text just before
                flush_list(); flush_label()
                refs = ''.join(join_pieces(Renderer(page).render([t]), 'md') for t in toks_raw if t.kind == 'fn')
                if late and pending_fig is not None:
                    flush_fig()
                if page.blocks and isinstance(page.blocks[-1], str) and not page.blocks[-1].startswith(('<figure', '#')):
                    page.blocks[-1] += refs
                else:
                    page.blocks.append(refs)
                continue
            if not text and not has_img and any(t.kind == 'hr' for t in toks_raw):
                flush_list(); flush_label(); flush_fig(); flush_title()
                add_block('* * *')
                continue
            if not text and not has_img:
                continue

            toks = clean_edges(toks_raw)
            has_numpr = el.find(W + 'pPr/' + W + 'numPr') is not None

            if late:
                if en and style == 'heading 6' and not has_img and pending_fig is not None and pending_fig['caption'] is None:
                    pending_fig['caption'] = toks
                    continue
                if df and not has_img and not has_numpr and style == 'Normal' and pending_fig is not None \
                        and pending_fig['caption'] is None and is_caption(toks_raw):
                    pending_fig['caption'] = strip_italic(toks)
                    continue
                flush_fig()
                if pending_title is not None and not has_img:
                    flush_title()

            if not (has_numpr and style == 'Normal'):
                flush_list()

            if en and style == 'heading 6':
                warn('heading 6 %r without a preceding image (kept as a paragraph)' % plain_text(toks))
                style = 'Normal'

            # ---- headings 3..6
            if style in ('heading 2', 'heading 3', 'heading 4', 'heading 5', 'heading 6'):
                ptext = plain_text(toks)
                r = Renderer(page)
                if en and style == 'heading 5':
                    flush_label()
                    pending_title = toks
                    continue
                if style == 'heading 6':
                    flush_label()
                    if pending_caption is not None:
                        warn('caption without image: %r' % plain_text(pending_caption))
                    pending_caption = toks
                    continue
                if style == 'heading 4' and ptext.endswith(':') and len(ptext) <= 80:
                    flush_label()
                    pending_label = toks
                    continue
                flush_label()
                if en and chapter == 0:
                    level = {'heading 2': '##', 'heading 3': '###', 'heading 4': '####'}[style]
                else:
                    level = {'heading 3': '##', 'heading 4': '###', 'heading 5': '####'}[style]
                hid = page.unique_id(ptext)
                anchor[1] = hid
                md = join_pieces(r.render(toks, strip_bold=True), 'md')
                bh = BODY_HEADING_OVERRIDES.get(P['name'], {}).get((page.filename, hid))
                if bh is not None:
                    PROFILE_USES[('body heading', page.filename, hid)] = PROFILE_USES.get(('body heading', page.filename, hid), 0) + 1
                    md = esc_md(bh)
                add_block('%s %s {#%s}' % (level, md, hid))
                if style == 'heading 3':
                    page.stats['h3'] += 1
                page.stats['links'] += sum(1 for t in toks if t.kind == 'link')
                continue

            if style not in ('Normal',):
                warn('unhandled style %r (paragraph %d): %r' % (style, idx, text[:50]))

            # ---- images
            if has_img and late:
                flush_list(); flush_label()
                imgs = [t for t in toks_raw if t.kind == 'img']
                rest = clean_edges([t for t in toks_raw if t.kind != 'img'])
                if rest and not re.search(r'\w', plain_text(rest)):
                    warn('punctuation-only text %r next to an image on page %s dropped' % (plain_text(rest), page.slug))
                    rest = []
                for n, im in enumerate(imgs):
                    page.blocks.append(None)
                    f = dict(page=page, idx=len(page.blocks) - 1, rid=im.rid, title=pending_title if n == 0 else None,
                             caption=None, note=rest if n == len(imgs) - 1 else [])
                    if df and f['note']:            # text inside the image paragraph is its caption
                        f['caption'], f['note'] = strip_italic(f['note']), []
                    if n == len(imgs) - 1:
                        pending_fig = f
                    else:
                        pending_fig = f
                        flush_fig()
                pending_title = None
                continue
            if has_img:
                flush_list(); flush_label()
                imgs = [t for t in toks_raw if t.kind == 'img']
                rest = clean_edges([t for t in toks_raw if t.kind != 'img'])
                for n, im in enumerate(imgs):
                    page.blocks.append(self.figure(page, im.rid, pending_caption or [] if n == 0 else [],
                                                   rest if n == len(imgs) - 1 else []))
                pending_caption = None
                continue

            if pending_caption is not None:
                warn('caption %r not followed by an image (page %s)' % (plain_text(pending_caption), page.slug))
                pending_caption = None

            # ---- lists
            if has_numpr:
                flush_label()
                npr = el.find(W + 'pPr/' + W + 'numPr')
                numid = npr.find(W + 'numId').get(W + 'val')
                ilvl = int(npr.find(W + 'ilvl').get(W + 'val'))
                fmt = dx.numfmt.get(numid, {}).get(ilvl, 'bullet')
                ordered = fmt != 'bullet'
                if list_items and ilvl == 0 and (list_items[-1][1] != ordered or list_items[-1][3] != numid):
                    flush_list()
                list_items.append((ilvl, ordered, toks_raw, numid))
                continue

            # ---- ordinary paragraph (+ run-in label)
            if P['name'] == 'en' and plain_text(toks).strip() in EN_DROP_PARAGRAPHS:
                key = ('drop paragraph', plain_text(toks).strip())
                PROFILE_USES[key] = PROFILE_USES.get(key, 0) + 1
                continue
            if df and plain_text(toks).strip() == '.':
                self.dropped_dots = getattr(self, 'dropped_dots', 0) + 1
                continue
            if df and id(el) in self.repl:
                toks = list(self.repl[id(el)])
            r = Renderer(page)
            md = join_pieces(r.render(toks), 'md')
            plain = plain_text(toks)
            if pending_label is not None:
                lab = join_pieces(r.render(pending_label, strip_bold=True), 'md').rstrip()
                md = '**%s** %s' % (lab, md)
                pending_label = None
            else:
                md = line_start_escape(md)
            page.stats['links'] += sum(1 for t in toks if t.kind == 'link')
            add_block(md, plain)

        register()
        flush_list(); flush_label(); flush_fig()
        if pending_title is not None:
            flush_title()
        if pending_caption is not None:
            warn('dangling caption %r' % plain_text(pending_caption))
        return self.pages

    def align_printed(self):
        """pre-pass: align docx paragraphs with the printed PDF (profile "df"); fills self.repl and self.align_log"""
        dx = self.dx
        pdf = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', P['printed_pdf'])
        started = False
        items = []                       # (el, kind, text, toks)
        prev_img = False
        heading_texts = list(P['parts']) + list(P['sections'])
        caption_texts, vocab_texts = [], []
        for el in dx.body:
            if el.tag == W + 'tbl':
                if started:
                    for tp in el.iter(W + 'p'):
                        tx = plain_text(dx.para_tokens(tp, dx.rels))
                        if tx:
                            caption_texts.append(tx)
                continue
            if el.tag != W + 'p':
                continue
            raw_style = dx.style(el)
            style = P['style_alias'].get(raw_style, raw_style)
            if raw_style in P.get('lead_styles', ()):
                style = 'Normal'
            if not started:
                if style == 'heading 1':
                    started = True
                else:
                    continue
            toks = dx.para_tokens(el, dx.rels)
            if raw_style in P.get('lead_styles', ()):
                toks = force_italic(toks)
            text = plain_text(toks)
            if any(t.kind == 'img' for t in toks):
                prev_img = True
                continue
            if not text:
                continue
            if style.startswith('heading'):
                heading_texts.append(text)
                prev_img = False
                continue
            kind = 'caption' if prev_img and is_caption(toks) else 'body'
            if kind == 'caption':
                caption_texts.append(text)
            prev_img = False
            vocab_texts.append(text)
            items.append((el, kind, text, toks, el.find(W + 'pPr/' + W + 'numPr') is not None))
        pt = PrintedText(pdf, heading_texts, caption_texts, vocab_texts, P.get('printed_cfg'))
        self.align_log = []
        self.align_stats = collections.Counter()
        for el, kind, text, toks, is_list in items:
            if kind == 'caption':
                continue
            ctoks = clean_edges(toks)
            ctext = plain_text(ctoks)
            reason = None
            flags = {(t.b, t.i) for t in ctoks if t.kind == 't' and t.text.strip()}
            if is_list:
                reason = 'list item'
            elif any(t.kind == 'link' for t in ctoks):
                reason = 'has hyperlink'
            elif any(t.kind not in ('t', 'fn') for t in ctoks):
                reason = 'line break / other inline content'
            elif len(flags) > 1:
                reason = 'mixed bold/italic'
            self.align_stats['body paragraphs'] += 1
            marks, wcount = [], 0
            for t in ctoks:
                if t.kind == 't':
                    wcount += sum(1 for w in t.text.split() if PrintedText.key(w) or pt.keep_punct)
                elif t.kind == 'fn':
                    marks.append(wcount)
            fns = [t for t in ctoks if t.kind == 'fn']
            typed = []               # df: hand-typed "[^N]" markers, taken out for the alignment and put back after
            atext = ctext
            if not fns and re.search(r'\[\^\d+\]', ctext):
                atext = re.sub(r'\[\^\d+\]', '', ctext)
                for m in re.finditer(r'\[\^(\d+)\]', ctext):
                    pre = re.sub(r'\[\^\d+\]', '', ctext[:m.start()])
                    typed.append((sum(1 for w in pre.split() if PrintedText.key(w) or pt.keep_punct), m.group(1)))
                marks = [q for q, _ in typed]
            elif fns and re.search(r'\[\^\d+\]', ctext):
                print('ALIGN: paragraph with real footnotes and typed markers left as is: %s' % ctext[:60])
            printed, info = pt.align(atext, marks or None)
            if reason is None and printed is None:
                reason = info['reason']
            if reason is not None:
                self.align_stats['kept: ' + reason] += 1
                self.align_log.append(dict(status='kept', reason=reason, docx=ctext, info=info))
                continue
            if typed and printed is not None:
                res, prev, out = [], 0, info['out']
                for q, (_, num) in zip(info['marks'], typed):
                    seg = pt.join(out[prev:q])
                    res.append(seg + ' [^%s]' % num if seg else '[^%s]' % num)
                    prev = q
                rest = pt.join(out[prev:])
                printed = ' '.join(x for x in res + [rest] if x)
            if printed == ctext:
                self.align_stats['identical'] += 1
            else:
                self.align_stats['replaced'] += 1
            fb, fi = next(iter(flags)) if flags else (False, False)
            if fns:
                res, prev, need = [], 0, False
                out = info['out']
                for q, ft in zip(info['marks'], fns):
                    seg = pt.join(out[prev:q])
                    if seg:
                        res.append(Tok('t', (' ' if need else '') + seg, fb, fi))
                    res.append(ft)
                    need, prev = True, q
                seg = pt.join(out[prev:])
                if seg:
                    res.append(Tok('t', (' ' if need else '') + seg, fb, fi))
                self.repl[id(el)] = res
            else:
                self.repl[id(el)] = [Tok('t', printed, fb, fi)]
            self.align_log.append(dict(status='replaced' if printed != ctext else 'identical', docx=ctext,
                                       printed=printed, info=info))

    def handle_table(self, page, tbl, pending_caption):
        dx = self.dx
        rows = tbl.findall(W + 'tr')
        cells = [[tc for tc in tr.findall(W + 'tc')] for tr in rows]
        paras = [[p for tc in row for p in tc.findall(W + 'p')] for row in cells]
        flat = [p for row in paras for p in row]
        imgs = [t for p in flat for t in dx.para_tokens(p, dx.rels) if t.kind == 'img']
        texts = [clean_edges([t for t in dx.para_tokens(p, dx.rels) if t.kind != 'img']) for p in flat]
        texts = [t for t in texts if t]
        if len(imgs) == 1 and len(texts) <= 1 and all(len(r) == 1 for r in cells):
            cap = pending_caption or (texts[0] if texts else [])
            note = [] if pending_caption is None else (texts[0] if texts else [])
            alt = None
            if not pending_caption and texts:
                alt = re.sub(r'[\s.]*\(Kaynak:.*\)\s*$', '', plain_text(texts[0])).rstrip(' .')
            page.blocks.append(self.figure(page, imgs[0].rid, cap, note, alt))
            return
        raise SystemExit('unsupported table layout on page %s' % page.slug)

    # -- output -------------------------------------------------------------------------------
    def footnote_defs(self, page):
        dx = self.dx
        r = Renderer(page)
        lines = []
        for n, fid in enumerate(page.fn_ids, 1):
            f = dx.footnotes[fid]
            paras = []
            for p in f.findall(W + 'p'):
                toks = clean_edges(dx.para_tokens(p, dx.fn_rels))
                if not toks:
                    continue
                page.stats['links'] += sum(1 for t in toks if t.kind == 'link')
                paras.append(line_start_escape(join_pieces(r.render(toks), 'md')))
            if not paras:
                warn('empty footnote %d' % fid)
                paras = ['']
            body = ('\n\n    ').join(paras)
            if '{{' in body or '{%' in body:
                body = '{% raw %}' + body + '{% endraw %}'
            lines.append('[^%d]: %s' % (n, body))
            page.stats['fn_defs'] += 1
        return '\n\n'.join(lines)

    def hand_typed_notes(self, page):
        """df: the manuscript has hand-typed notes: "[^N]" markers in the text plus paragraphs / list items that start
        with "[^N]" (or "[N]"). Marker + definition with the same number -> real footnote (renumbered per page from 1 in
        order of first reference); definition without marker -> "**Not:** ..." paragraph at the end of the page; marker
        without definition -> removed. Returns (footnote definition lines, log entries)."""
        defs, blocks, log = {}, [], []
        conts = {}               # definition number -> blocks that continue it (lists / paragraphs right after it)
        cur = None
        dpat = re.compile(r'^\\\[\^?(\d+)\\\]\s*(.*)$', re.S)
        for b in page.blocks:
            if '\n' not in b and dpat.match(b):
                m = dpat.match(b)
                cur = int(m.group(1))
                defs[cur] = m.group(2)
                continue
            if b.startswith('- ') and re.match(r'^- \\\[\^\d+\\\]', b):
                keep = []
                for line in b.split('\n'):
                    lm = re.match(r'^- \\\[\^(\d+)\\\]\s*(.*)$', line)
                    if lm:
                        cur = int(lm.group(1))
                        defs[cur] = lm.group(2)
                    else:
                        keep.append(line)
                if keep:
                    blocks.append('\n'.join(keep))
                continue
            if cur is not None and not b.startswith(('#', '<figure')):
                conts.setdefault(cur, []).append(b)       # continuation of the note above
                log.append('block after note %d moved into it: %s' % (cur, b[:40].replace('\n', ' ')))
                continue
            cur = None
            blocks.append(b)
        order = []
        for b in blocks:
            for x in re.findall(r'\\\[\^(\d+)\\\]', b):
                if int(x) not in order:
                    order.append(int(x))
        if not defs and not order:
            return [], log
        newnum = {n: k for k, n in enumerate([n for n in order if n in defs], 1)}
        def sub(m):
            n = int(m.group(1))
            if n in newnum:
                return '[^%d]' % newnum[n]
            log.append('marker [^%d] removed (no definition)' % n)
            return ''
        page.blocks = [re.sub(r' ?\\\[\^(\d+)\\\]', sub, b) for b in blocks]
        notes = []
        for n in sorted(defs):
            if n not in newnum:
                notes.append('**Not:** %s' % defs[n])
                notes.extend(conts.get(n, []))
        for n in sorted(defs):
            log.append('definition %d -> %s' % (n, 'footnote %d' % newnum[n] if n in newnum else 'Not:'))
        page.blocks.extend(notes)
        out = []
        for n in sorted(newnum, key=lambda n: newnum[n]):
            d = '[^%d]: %s' % (newnum[n], defs[n])
            for cb in conts.get(n, []):
                d += '\n\n' + '\n'.join('    ' + l if l else l for l in cb.split('\n'))
            out.append(d)
        return out, log

    def resolve_links(self, text, page):
        """internal cross-references ("#bm:NAME") -> permalink of the page holding the bookmark (+ heading id)"""
        if '#bm:' not in text:
            return text
        def target(name):
            t = self.bookmarks.get(name)
            if not t or t[0] is None:
                return None
            pg, hid = t
            return pg.permalink + ('#' + hid if hid else '')
        def md(m):
            u = target(m.group(2))
            if u is None:
                warn('unresolved internal link %r on page %s' % (m.group(2), page.slug))
                return m.group(1)
            return '[%s](%s)' % (m.group(1), u)
        text = re.sub(r'\[((?:[^\[\]\\]|\\.)*)\]\(#bm:([^)\s]*)\)', md, text)
        def html_(m):
            u = target(m.group(1))
            return 'href="%s"' % (u or '#')
        return re.sub(r'href="#bm:([^"]*)"', html_, text)

    def apply_out_corrections(self):
        corr = P.get('out_corrections', [])
        counts = {c[0]: 0 for c in corr}
        want = {c[0]: (c[2] if len(c) > 2 else 1) for c in corr}
        for page in self.pages:
            for k, b in enumerate(page.blocks):
                for c in corr:
                    n = b.count(c[0])
                    if n:
                        counts[c[0]] += n
                        b = b.replace(c[0], c[1])
                page.blocks[k] = b
        bad = {k: v for k, v in counts.items() if v != want[k]}
        if bad:
            raise SystemExit('output corrections must match exactly once; got %r' % bad)

    def write(self):
        os.makedirs(self.out_dir, exist_ok=True)
        files = []
        self.note_log, extra_defs = {}, {}
        for page in self.pages:
            if P['name'] == 'df':
                extra, lg = self.hand_typed_notes(page)
                extra_defs[page.filename] = extra
                if lg:
                    self.note_log[page.filename] = lg
        self.apply_out_corrections()
        for page in self.pages:         # a part without text of its own gets its overview as body and description
            ov = P.get('chapter_overviews', {}).get(page.chapter)
            if page.kind == 'chapter' and ov and not page.blocks:
                page.blocks = [ov]
                page.plain = [ov]
        fn_counts = {}
        for page in self.pages:
            fdefs = self.footnote_defs(page)
            page.blocks = [self.resolve_links(b, page) for b in page.blocks]
            fdefs = self.resolve_links(fdefs, page)
            for c in FN_OUT_CORRECTIONS.get(P['name'], []):
                n = fdefs.count(c[0])
                fn_counts[c[0]] = fn_counts.get(c[0], 0) + n
                if n:
                    fdefs = fdefs.replace(c[0], c[1])
            if extra_defs.get(page.filename):
                fdefs = (fdefs + '\n\n' if fdefs else '') + '\n\n'.join(extra_defs[page.filename])
                page.stats['fn_defs'] += len(extra_defs[page.filename])
            body = '\n\n'.join(page.blocks)
            text = front_matter(page) + ('\n' + body + '\n' if body else '')
            if fdefs:
                text += '\n' + fdefs + '\n'
            with open(os.path.join(self.out_dir, page.filename), 'w', encoding='utf-8') as f:
                f.write(text)
            files.append(page.filename)
        bad = {c[0]: fn_counts.get(c[0], 0) for c in FN_OUT_CORRECTIONS.get(P['name'], [])
               if fn_counts.get(c[0], 0) != (c[2] if len(c) > 2 else 1)}
        if bad:
            raise SystemExit('footnote corrections must match exactly once; got %r' % bad)
        used = set(p for pg in self.pages for p in pg.fn_ids)
        if used != set(self.dx.footnotes):
            warn('footnotes not referenced: %s' % sorted(set(self.dx.footnotes) - used))
        return files


def sweep(dirpath, new_files):
    """remove files generated by a previous run (manifest) that are not part of this run"""
    man = os.path.join(dirpath, '.generated')
    if os.path.exists(man):
        with open(man, encoding='utf-8') as f:
            for name in f.read().split('\n'):
                if name and name not in new_files and os.path.basename(name) == name:
                    p = os.path.join(dirpath, name)
                    if os.path.isfile(p):
                        os.remove(p)
    with open(man, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(new_files)) + '\n')


def main(argv):
    argv = list(argv)
    book = 'tr'
    if len(argv) > 2 and argv[1] == '--book':
        book = argv[2]
        del argv[1:3]
    if len(argv) != 4 or book not in PROFILES:
        print(__doc__)
        return 2
    use_profile(book)
    docx, out_dir, img_dir = argv[1:]
    log_path = os.environ.get('DOCX2BOOK_LOG')
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(out_dir, exist_ok=True)
    conv = Converter(docx, out_dir, img_dir)
    conv.run()
    files = conv.write()
    for kind, items in (('promote', P['promote']), ('heading', P['heading_overrides'])):
        for it in items:
            if PROFILE_USES.get((kind, it), 0) != 1:
                raise SystemExit('%s rule %r must match exactly once; got %d' % (kind, it, PROFILE_USES.get((kind, it), 0)))
    for (fname, hid) in BODY_HEADING_OVERRIDES.get(P['name'], {}):
        n = PROFILE_USES.get(('body heading', fname, hid), 0)
        if n != 1:
            raise SystemExit('body heading override (%s, #%s) must apply exactly once; got %d' % (fname, hid, n))
    for old in LINK_TARGET_FIXES.get(P['name'], {}):
        n = PROFILE_USES.get(('link fix', old), 0)
        if n != LINK_FIX_EXPECTED.get(old, 1):
            raise SystemExit('link target fix %r must apply %d time(s); got %d' % (old, LINK_FIX_EXPECTED.get(old, 1), n))
    if P['name'] == 'en':
        for txt in EN_DROP_PARAGRAPHS:
            if PROFILE_USES.get(('drop paragraph', txt), 0) != 1:
                raise SystemExit('drop paragraph %r must match exactly once; got %d' % (txt, PROFILE_USES.get(('drop paragraph', txt), 0)))
    bad = {k: v for k, v in CORRECTION_COUNTS.items() if v != (CORRECTION_EXPECTED if P['name'] == 'tr' else EN_CORRECTION_EXPECTED).get(k, 1)}
    if bad:
        raise SystemExit('corrections must match exactly once; got %r' % bad)
    sweep(out_dir, files)
    sweep(img_dir, conv.img_files)
    tot = {k: sum(p.stats[k] for p in conv.pages) for k in ('figures', 'h3', 'links', 'fn_defs')}
    print('pages: %d (%d sections, %d chapters)' % (len(conv.pages),
          sum(p.kind == 'section' for p in conv.pages), sum(p.kind == 'chapter' for p in conv.pages)))
    print('totals:', tot)
    print('images: %d, %.1f MB -> %.1f MB' % (len(conv.img_files), conv.img_in_bytes / 1e6, conv.img_out_bytes / 1e6))
    for p in conv.pages:
        print('%s\t%s\t%s\t%s\t%s' % (p.order, p.slug, p.permalink, p.title, p.heading))
    for fn, name, alt in [c for p in conv.pages for c in p.captionless]:
        print('CAPTIONLESS %s %s -> alt=%r' % (fn, name, alt))
    if getattr(conv, 'dropped_dots', 0):
        print('dropped "." paragraphs: %d' % conv.dropped_dots)
    for fn, lg in sorted(getattr(conv, 'note_log', {}).items()):
        print('NOTES %s: %s' % (fn, '; '.join(lg)))
    if getattr(conv, 'align_stats', None) is not None:
        print('alignment with the printed text:', dict(conv.align_stats))
        if log_path:
            import json
            with open(log_path, 'w', encoding='utf-8') as f:
                json.dump(conv.align_log, f, ensure_ascii=False, indent=1)
    print('warnings: %d' % len(WARNINGS))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
