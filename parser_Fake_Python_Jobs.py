import requests
from bs4 import BeautifulSoup


link = "https://realpython.github.io/fake-jobs/"
response = requests.get(link)

if response.status_code == 200:
    soup=BeautifulSoup(response.text, 'lxml')
    blocks = soup.find_all('div', class_= "card")
    for block in blocks:
        job = block.find('h2', class_="title is-5").text
        company = block.find('h3', class_="subtitle is-6 company").text
        print(f'Вакансия: {job}', f'Компания: {company}', sep = '\n', end = '\n\n')

else:
    print(f'Ошибка: {response.status_code}')
