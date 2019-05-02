
# Q1: Vérifie si "est" est positioné après un texte dans la phrase, puis si "qui" est situé après est et avant un autre texte.


import requests
import re
url='http://www.gutenberg.org/cache/epub/16/pg16.txt'
url2='http://www.gutenberg.org/cache/epub/41444/pg41444.txt'
# si on passe par le proxy univ orleans :
proxy={"http":"http://wwwcache.univ-orleans.fr:3128/"}
r=requests.get(url2,proxies=proxy)
# si pas de proxy :
# r=requests.get(url)
PeterPan = r.text
len(r.text)
r.encoding
it=re.finditer('(The [^.]* day)\.',PeterPan)
for i in it:
    print(i.groups())