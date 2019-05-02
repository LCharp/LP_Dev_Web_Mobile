
    ''' Imports'''


import requests
import re
import csv
from bs4 import BeautifulSoup


    '''Notes'''


#recherche par nom de balise
#soup.find('p')
#soup.find_all('p')

#retourne les balises de 2 caracteres
#soup.find(re.compile(r'..'))

# par les fonction
#def f(tag):
#    return len(tag.name) == 2 

#soup.find_all(f)

#recherche par propriete CSS
#soup.select('.biglink')

#recherche par nom + valeur d'attributs
#soup.find('a', href = re.compile('Python'))


    '''Exercice 3'''


UNI= requests.get("https://stackoverflow.com/questions/tagged/beautifulsoup")
soup= BeautifulSoup(UNI.text, 'lxml')

Liste1 = soup.find_all('a', class_='question-hyperlink', limit = 10)
Liste2 = soup.find_all('span', class_='vote-count-post', limit=10)
Liste3 = soup.find_all('div', class_='status', limit=10)


data1 = []
data2 = []
data3 = []

i=0
while i<10:
    x = Liste1[i].get_text()
    y = (Liste2[i].find('strong', string=re.compile("-?[0-9]*"))).find(string=re.compile("^-?[0-9]*$"))
    z = (Liste3[i].find('strong', string=re.compile("-?[0-9]*"))).find(string=re.compile("^-?[0-9]*$"))
    data1.append(x)
    data2.append(y)
    data3.append(z)
    i += 1

j=0
file = open('data.csv', 'w')
while j<10:
    writer = csv.writer(file, delimiter='|')
    writer.writerow((data1[j],data2[j], data3[j]))
    j += 1

file.close()


    '''Exercice 4'''


UNI = requests.get("http://formation.univ-orleans.fr/fr/formation/rechercher-une-formation.html#nav")
soup = BeautifulSoup(UNI.text, 'lxml')

