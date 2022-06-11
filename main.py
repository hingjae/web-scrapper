import requests
from bs4 import BeautifulSoup

notice = requests.get("https://it.jbnu.ac.kr/it/9842/subview.do")

soup = BeautifulSoup(notice.text, "html.parser")
# print(soup)

pagination = soup.find("div", {"class":"_paging"})
# print(pagination)

links = pagination.find_all('li')
# print(links)

pages = []

#page number 추출
for link in links:
    pages.append(int(link.string)) # 안에 있는 string만 가져옴 
#span의 경우 pages.append(link.("span").string)
print(pages[1:])

max_page = pages[-1]