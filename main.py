'''If you want to scrape a website :
1. Use the API
2. HTML Web Scraping using some tool like bs4
'''

import requests
from bs4 import BeautifulSoup
url = "https://kukufm.com"

r = requests.get(url)
htmlcontent = r.content
print(htmlcontent)
print("\n\n")
soup = BeautifulSoup(htmlcontent, 'html.parser')
print(soup.prettify)
print("\n\n")
title = soup.title
print(title)
print(type(title))
