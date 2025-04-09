import requests
from bs4 import BeautifulSoup



base_link = "https://quotes.toscrape.com/page/{}/"
for page in range(1,11):
    link = base_link.format(page)
    response = requests.get(link)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('div', class_ = "quote")
        print('----------------------------------------------------------------------------------')
        print(f'Страница: {page}')
        print('----------------------------------------------------------------------------------')
        for quote in quotes:
            text = quote.find('span', class_="text").text
            author = quote.find('small', class_="author").text
            print(f'Цитата: {text}', f'Aвтор: {author}', sep = '\n', end = '\n\n')

    else:
        print(f"Ошибка при запросе страницы {page}:", response.status_code)