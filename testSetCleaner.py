import re

RE_replacements = [
    #(r'[-—\[\]\(\)=,;’‘\'\"]', ' '), #replace those symbols with space
    (r'[^aābcčdeēfgģhiījkķlļmnņoprsštuūvzž\.0123456789]', ' '),
    #(r'\d+', '0'), #replace a string of 1 or more digits with 0
    (r'\d+\.?', '0'), #replace a string of 1 or more digits with or without a . to 0
    #(r'\s\w[\.]+', ' '), #aizvietot abriviatūras ar space. Broken
    (r'\s\s+', ' '), #replace a string of 1 or more spaces with space
    (r'\w*\d\w*', '0'), #replace weird m0 l0 m0 m0 m0 l0aa teksts
    (r'(0[\s]?)+', '0 '), #replace 0 0 0 0 0 0 and 0000 with just 1 0
    (r'apg\.', 'apgāds'),
    (r'apm\.', 'apmēram'),
    (r'att\.', 'attēls'),
    (r'bulv\.', 'bulvāris'),
    (r'°C', 'Celsija grāds'),
    (r'c\.', 'ciems'),
    (r'cet\.', 'ceturksnis'),
    (r'dep\.', 'departaments'),
    (r'diagr\.', 'diagramma'),
    (r'dok\.', 'dokuments'),
    (r'dsk\.', 'daudzskaitlis'),
    (r'°F', 'Fārenheita grāds'),
    (r'f\.', 'fonds'),
    (r'g\.', 'gads'),
    (r'gab\.', 'gabals'),
    (r'gr\.', 'grupa'),
    (r'gs\.', 'gadsimts'),
    (r'g\.\s?t\.', 'gadu tūkstotis'),
    (r'ģimn\.', 'ģimnāzija'),
    (r'iec\.', 'iecirknis'),
    (r'il\.', 'ilustrācija'),
    (r'inst\.', 'institūts'),
    (r'inv\.', 'inventārs'),
    (r'īst\.\s?v\.', 'īstajā vārdā'),
    (r'izdevn\.', 'izdevniecība'),
    (r'krāj\.', 'krājums'),
    (r'kr\.', 'kreisais'),
    (r'kp\.', 'kredītpunkts'),
    (r'l\.', 'lieta'),
    (r'laid\.', 'laidiens'),
    (r'lb\.', 'labais'),
    (r'lauk\.', 'laukums'),
    (r'līn\.', 'līnija'),
    (r'lp\.', 'lapa'),
    (r'lpp\.', 'lappuse'),
    (r'p\.\s?m\.\s?ē\.', 'pirms mūsu ēras'), #samainīts ar vietām ar m.ē.
    (r'mēn\.', 'mēnesis'),
    (r'milj\.', 'miljons'),
    (r'mljrd\.', 'miljards'),
    (r'ned\.', 'nedēļa'),
    (r'nod\.', 'nodaļa'),
    (r'not\.', 'noteikumi'),
    (r'nov\.', 'novads'),
    (r'[nN]r\.', 'numurs'),
    (r'oriģ\.', 'oriģināls'),
    (r'p/a\.', 'pašvaldības aģentūra'),
    (r'(pers\. k\.|p\. k\.)', ''),
    (r'piel\.', 'pielikums'),
    (r'piem\.', 'piemēram'),
    (r'piez\.', 'piezīme'),
    (r'pils\.', 'pilsēta'),
    (r'plkst\.', 'pulksten'),
    (r'm\.\s?ē\.', 'mūsu ēras'), #samainīts ar vietām ar p.m.ē.
    (r'p\.\s?m\.\s?ē\.', 'pirms mūsu ēras'),
    (r'p\.\s?n\.', 'pasta nodaļa'),
    (r'priekšp\.', 'priekšpilsēta'),
    (r'progr\.', 'programma'),
    (r'proj\.', 'projekts'),
    (r'prot\.', 'protokols'),
    (r'psk\.', 'pamatskola'),
    (r'raj\.', 'rajons'),
    (r'resp\.', 'respektīvi'),
    (r'sal\.', 'salīdzināt'),
    (r'sēj\.', 'sējums'),
    (r'(skat\.|sk\.)', 'skatīt'),
    (r'spec\.', 'speciāls'),
    (r'spied\.', 'spiedogs'),
    (r'š\.\s?g\.', 'šī gada'),
    (r'šķ\.', 'šķira'),
    (r'tab\.', 'tabula'),
    (r't\.\s?i\.', 'tas ir'),
    (r'tūkst\.', 'tūkstotis'),
    (r'u\.\s?c\.', 'un citi'),
    (r'univ\.', 'universitāte'),
    (r'u\.\s?t\.\s?jpr\.', 'un tā joprojām'),
    (r'u\.\s?tml\.', 'un tamlīdzīgi'),
    (r'utt\.', 'un tā tālāk'),
    (r'uzņ\.', 'uzņēmums'),
    (r'val\.', 'valoda'),
    (r'var\.', 'variants'),
    (r'vsk\.', 'vienskaitlis'),
    (r'v\.\s?tml\.', 'vai tamlīdzīgi'),
    (r'\s\w\.\s', ' ') #remove uzv saīsin
]

done_txt = open(r"F:\RTU stuff\Thesis\test_corpus_DONE.txt", "w", encoding="utf-8")
done_txt.write("")
done_txt.close()
print("Cleared file")

done_txt = open(r"F:\RTU stuff\Thesis\test_corpus_DONE.txt", "a", encoding="utf-8")

with open(r"F:\RTU stuff\Thesis\test_corpus.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.lower()
        for old, new in RE_replacements:
            line = re.sub(old, new, line)
        #line = re.sub(r'[-\[\]\(\)=]', ' ', line).sub(r'\d*', '0', line).sub(r'\s*', ' ', line)
        #print(line)
        done_txt.write(line)

done_txt.close()
print('done')