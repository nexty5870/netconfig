from bs4 import BeautifulSoup
import requests

macdetail = 'b0:26:28:22:3a:40'
source = requests.get('https://hwaddress.com/?q='+ macdetail).text
soup = BeautifulSoup(source, 'lxml')

vendor = soup.find('div', class_='table-responsive')
company = vendor.a.text
print(company)



