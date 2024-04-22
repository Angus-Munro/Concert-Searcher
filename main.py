from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.songkick.com/metro-areas/26794-australia-sydney"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

listings = soup.find(class_="metro-area-calendar")
descendents = listings.find_all()

for desc in descendents:
    if 'date-element' in desc.get('class', []):
        print("\n\n", desc.text.strip())
    if 'artists-venue-location-wrapper' in desc.get('class', []):
        desc.get_text(separator='\n', strip=True)
        p_tags = desc.find_all('p')
        for p in p_tags:
            print(p.text.strip())
        print("\n")