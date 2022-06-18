from re import L
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://www.indeed.com/jobs?as_and=python&limit={LIMIT}"
def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class":"pagination"})

    links = pagination.find_all("a")
    pages = []

    for link in links[:-1]:
        pages.append(int(link.string)) #span안의 string만 가져옴.

    max_page = pages[-1]
    return max_page

def extract_job(html):
    title = html.find("h2", {"class":"jobTitle"}).find("a").find("span")["title"]
    company = html.find("span", {"class":"companyName"}).string
    return {'title': title, 'company': company}

def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class" :"cardOutline"})
    for result in results:
        job = extract_job(result)
        print(job)
    return jobs