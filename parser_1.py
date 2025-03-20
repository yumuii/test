from itertools import count
import requests
from bs4 import BeautifulSoup
import json

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
data = []
id_generator = count(start=1)

for page in range(1, 51):
    url = base_url.format(page)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('article', class_='product_pod')

        for product in products:
            name = product.find('h3').text
            price = product.find(class_='price_color').text
            img_element = product.find('div', class_='image_container').find('img')
            img_url = "http://books.toscrape.com/" + img_element['src'].replace('../', '') if img_element and 'src' in img_element.attrs else "Нет изображения"
            unique_id = next(id_generator)

            data.append({
                'ID': unique_id,
                'Name': name,
                'Price': price[1:],
                'Image_Url': img_url
            })

        print(f"Страница {page} обработана.")
    else:
        print(f"Ошибка при запросе страницы {page}:", response.status_code)

with open('products.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Все данные сохранены в файл products.json.")