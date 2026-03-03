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
