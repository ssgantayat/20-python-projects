import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithtomi.com/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all('h2', {'class': 'post-title'})
title1 = title[0].getText()
for t in title:
    print(t.getText())