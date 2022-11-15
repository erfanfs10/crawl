from bs4 import BeautifulSoup
import requests


def get_links():
    url = 'https://www.trthaber.com/haber/spor/'
    links = list()
    response = requests.get(url)
    if response.status_code == 200:
        bs = BeautifulSoup(response.text, "html.parser")
        div = bs.find('div', attrs={'class': 'katListe2'})
        link = div.find_all('a')
        for i in link:
            links.append('https://www.trthaber.com/'+i.get('href'))
       
    return links


def crawl_pages(url):
    response = requests.get(url)
    if response.status_code==200:
        bs = BeautifulSoup(response.text, "html.parser")
        div_header = bs.find('div', attrs={'class': 'news-detail-header'})
        title = div_header.find('h1')
        body = bs.find('h2', attrs={'class': "detOzet"})
        
    return {'title': title.text, 'body': body.text}
    