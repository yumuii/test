import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'user-agent': user}


link = "https://browser-info.ru/"
response = requests.get(link, headers = header).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', id = "tool_padding")

#Check JS
check_js = block.find('div', id = "javascript_check")
status_js = check_js.find_all('span')[1].text
result_js = f'Javascript: {status_js}'

#Check flash
check_flash = block.find('div', id = "flash_version")
status_flash = check_flash.find_all('span')[1].text
result_flash = f'Flash: {status_flash}'

#Check user_agent
check_agent = block.find('div', id = "user_agent").text


print(result_js, result_flash, check_agent, sep = '\n')
