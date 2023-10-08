import requests
import re
from bs4 import BeautifulSoup

url = "https://zinduaschool.com/blog/"


response = requests.get(url)
html_content = response.content

# Parse the HTML content using Beautiful Soup

soup = BeautifulSoup(html_content, 'html.parser')

articles = soup.find_all('h1')
for article in articles:
    print (article.text)

datepattern = r'^\d{1,2})\s(January|February|March|April|May|June|July|August|September|October|November|December)\s(\d{4}'
if re.match(datepattern, date):
    print (date)


