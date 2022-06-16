# from notice import extract_notice_page, extract_notice_contents


# extract_notice_page()

# # last_notice_page = extract_notice_page()

# # extract_notice_contents(last_notice_page)

import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&limit=50&vjk=e80e9fb4813ea766")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

pages = pagination.find_all("a")
spans = []

for page in pages:
    spans.append(page.find("span"))

print(spans[:-1])