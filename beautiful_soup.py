import requests
from bs4 import BeautifulSoup

url = "https://tgif-website.netlify.app/house_data.html"


page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

print(soup.title)


mydivs = soup.find_all(class_ = 'col')
print(mydivs)

# table_content = soup.find(id="table-rows")

# print(table_content)
