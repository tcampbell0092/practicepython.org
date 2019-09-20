import bs4
import requests
res = requests.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')
soup = bs4.BeautifulSoup(res.text, "html.parser")
for lines in soup.find_all('p'):
    with open('vanity_fair.txt', 'w') as open_file:
        open_file.write('Vanity Fair Text')
