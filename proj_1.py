import sys
import requests
from bs4 import BeautifulSoup


# if len(sys.argv) < 2:
#     print("Usage: python script.py <URL>")
#     sys.exit(1)
try:
    url = sys.argv[1]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
except Exception as e:
    print(e)

print("PAGE TITLE:")
if soup.title:
    print(soup.title.string.strip())
else:
    print("title not found")


print("Page Body Text: ")
body = soup.body
if body:
    text = body.get_text()
    print(text.strip())
else:
    print("body not found")


print("The links are")
for link in soup.find_all("a"):
    href= link.get("href")
    if href:
        print(href)