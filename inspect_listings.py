from bs4 import BeautifulSoup

with open("sample_merchandise.html", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

for price in soup.select(".price"):
    print(price.text)

selectors = [
    ".item",
    ".badge",
    ".free-shipping",
    ".sponsored",
    "#results > li",
    ".item + .item",
    "li.item > a"
]

for selector in selectors:
    print(selector, len(soup.select(selector)))


from lab_selectors import extract_listings

listings = extract_listings(html)

for listing in listings:
    print(listing)