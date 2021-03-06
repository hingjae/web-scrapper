import requests
from bs4 import BeautifulSoup

LIMIT = 50

def get_last_page(URL):
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
    location = html.find("div", {"class":"companyLocation"}).text
    job_id = html.find("h2",{"class":"jobTitle"}).find("a")["data-jk"]
    return {'title': title, 'company': company, 'location': location, 'link':f"https://www.indeed.com/viewjob?jk={job_id}"}

def extract_jobs(last_page, URL):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class" :"cardOutline"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs(word):
    URL = f"https://www.indeed.com/jobs?as_and={word}&limit={LIMIT}"
    last_page = get_last_page(URL)
    jobs = extract_jobs(last_page,URL)
    return jobs