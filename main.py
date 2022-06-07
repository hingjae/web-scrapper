import requests
# import beautifulsoup4 리눅스에 pip 설치 필요함.!
notice = requests.get("https://it.jbnu.ac.kr/it/9842/subview.do")

print(notice.text)