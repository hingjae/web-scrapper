import requests
from bs4 import BeautifulSoup

notice = requests.get("https://it.jbnu.ac.kr/it/9842/subview.do")

soup = BeautifulSoup(notice.text, "html.parser")
# print(soup)

pagination = soup.find("div", {"class":"_paging"})
print(pagination)

pages = pagination.find_all('a')
# print(pages)

# for page in pagination:
#     print(page.find("li"))