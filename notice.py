from unittest import result
import requests
from bs4 import BeautifulSoup

LIMIT = 10
URL = "https://it.jbnu.ac.kr/it/9842/subview.do"

def extract_notice_page():
    notice = requests.get(URL)
    soup = BeautifulSoup(notice.text, "html.parser")
    # print(soup) 
    pagination = soup.find("div", {"class":"_paging"})
    # print(pagination)
    links = pagination.find_all('li')
    # print(links)
    pages = []
    #page number 추출
    for link in links:
        pages.append(int(link.string)) # tag를 제외하고 안에 있는 string만 가져옴 
    #span의 경우 pages.append(link.("span").string)
    # print(pages[1:])
    max_page = pages[-1]
    # print(range(max_page))
    return max_page

def extract_notice_contents(last_page):
    for page in range(last_page):
        requests.get(f"{URL}&start={page*LIMIT}")
        print(result.status_code)