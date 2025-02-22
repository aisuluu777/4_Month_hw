import requests
from bs4 import BeautifulSoup


URL = 'https://www.litres.ru/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}

def get_html(url, params = ''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

def get_data(html):
    bs = BeautifulSoup(html, features='html.parser')
    items = bs.find_all('div', class_='Art_content__ituUa Art_content_full___CBpM')
    books_list = []
    for item in items:
        title = item.find('a', class_='ArtInfo_title__h_5Ay').get_text(strip=True)
        author = item.find('a', class_='ArtPersons_row__yX2gU').get_text(strip=True)
        books_list.append({'title': title,
                           'author': author})
    return books_list


def parsing_litres():
    response = get_html(URL)
    if response.status_code == 200:
        books_list2 = []
        for page in range(1, 3):
            response = get_html("https://www.litres.ru/new/", params={'page': page})
            books_list2.extend(get_data(response.text))
            return books_list2
        else:
            raise Exception('Error in parsing booksite' )

# print(parsing_litres())

