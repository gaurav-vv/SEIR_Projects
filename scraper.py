# Write a python program that takes a URL on the command line, fetches the page, and outputs (one per line).
# 1. Page Title(without any html tags)
# 2. Page Body (just the text, without any html tags)
# 3. All the URLs that the page points/link to

import sys, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urljoin


if len(sys.argv) < 2:
    print("Usage: python scraper.py <URL>")
    sys.exit(1)

url = sys.argv[1]


if not url.startswith("http"):
    url = "https://" + url


chrome_op = Options()
chrome_op.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_op)

try:
    driver.get(url)
    time.sleep(4)  
    html = driver.page_source
except Exception as e:
    print("Error:", e)
    driver.quit()
    sys.exit(1)
    

soup = BeautifulSoup(html, "html.parser")
print("Page title:", driver.title)


print("\nBody Text:")
body = soup.body
if body:
    print(body.get_text(separator=" ", strip=True))
else:
    print("Body is not found")



print("\nlinks:")
link_set = set()

for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        actual_url = urljoin(url, href)
        if actual_url not in link_set:
            print(actual_url)
            link_set.add(actual_url)

driver.quit()

#for static 

# import requests
# import sys
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin

# if len(sys.argv) < 2:
#     print("Usage: python script.py <URL>")
#     sys.exit(1)

# url = sys.argv[1]

# if not url.startswith("http"):
#     url = "https://" + url
    
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
# }

# try:
#     web_p = requests.get(url, headers=headers, timeout=10)
#     web_p.raise_for_status()  
#     soup = BeautifulSoup(web_p.content, "html.parser")
# except requests.exceptions.RequestException as e:
#     print("Error in fetching:", e)
#     sys.exit(1)

# print("Page title :")
# if soup.title and soup.title.string:
#     print(soup.title.string.strip())
# else:
#     print("Unable to find the title")



# print("\nPage Body Text:")
# body_ = soup.body
# if body_:
#     text_ = body_.get_text(separator=" ", strip=True)
#     print(text_)
# else:
#     print("Body not found")


# print("\nThe links are:")
# link_set = set() 
# for link in soup.find_all("a"):
#     href = link.get("href")
#     if href:
#         Actuall_url = urljoin(url, href) 
#         if Actuall_url not in link_set:
#             print(Actuall_url)
#             link_set.add(Actuall_url)
