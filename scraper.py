import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

try:
    Response = requests.get(url, headers=headers, timeout=10)
    Response.raise_for_status()  
    soup = BeautifulSoup(Response.content, "html.parser")
except requests.exceptions.RequestException as e:
    print("Error in fetching:", e)
    sys.exit(1)

print("Page title :")
if soup.title and soup.title.string:
    print(soup.title.string.strip())
else:
    print("Unable to find the title")



print("\nPage Body Text:")
body_ = soup.body
if body_:
    text_ = body_.get_text(separator=" ", strip=True)
    print(text_)
else:
    print("Body not found")


print("\nThe links are:")
link_set = set() 
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        Actuall_url = urljoin(url, href) 
        if Actuall_url not in link_set:
            print(Actuall_url)
            link_set.add(Actuall_url)
