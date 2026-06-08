from bs4 import BeautifulSoup
import lxml
import requests

## Scrape du site quoes.toscrape, Le script récupère les citations et les auteurs et les stocke dans une liste. Il me dit exactement le nombre de citations dans chaque page. Pleins d'autres possibilités
all_quotes=[]
page = 1

while True:#boucle infinie
    html_text = requests.get(f'https://quotes.toscrape.com/page/{page}/').text #on recup l'url de la page
    soup= BeautifulSoup(html_text, 'lxml')
    quote_cards= soup.find_all('div', class_= 'quote')#container des citations
    next_btn=soup.find('li', class_='next')#btn next qui agit sur la pagination

    for each in quote_cards:
        quote=each.find('span', class_='text').text
        author = each.find('small', class_='author').text        
        all_quotes.append({'quote': quote, 'author':author})

    print(f"Page {page} — {len(quote_cards)} quotes")
    if next_btn is None :#dès que le bouton next disparait on casse la boucle
        break

    page+=1

print(f"We have {len(all_quotes)}quotes for {page} pages")      