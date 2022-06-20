import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs/companies?q=python"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
    pages = pages[0:-1]
    last_page = pages[-1].get_text(strip=True)
    return int(last_page)

def extract_job(html):
    company = html.find("a",{"class":"s-link"}).string
    return {'company': company}

def extract_jobs(last_page):
    companies = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("h2", {"class":"mb4"})#.find("a",{"class":"s-link"}).string
        for result in  results:
            company = extract_job(result)
            companies.append(company)
    return companies

def get_jobs():
    last_page = get_last_page()
    companies = extract_jobs(last_page)
    return companies