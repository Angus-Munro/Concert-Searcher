from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

class Concert:
    def __init__(self, date, artists):
        self.date = date
        self.artists = artists

    def get_details(self):
        return f"[{self.date}] {self.artists}"

concerts_info = []

for page in range(1,11):
    url = f"https://www.songkick.com/metro-areas/26794-australia-sydney?page={page}#metro-area-calendar"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    event_listings = soup.find_all(class_="event-listings-element")

    for event_listing in event_listings:
        # Get concert date and artists
        title = event_listing.get('title', 'No title attribute')
        artist_names = event_listing.strong.get_text()

        # Create a dictionary with concert details
        concert_details = {
        'date': title,
        'artists': artist_names
        }

        # Append the dictionary to concerts_info list
        concerts_info.append(concert_details)

    time.sleep(1)

with open('D:\\My Drive\\Standard Concert Search.txt', 'w') as file:
    dates = {}
    for concert in concerts_info:
        date = concert['date']
        if date in dates:
            dates[date].append(concert)
        else:
            dates[date] = [concert]

    for date, concerts in dates.items():
        file.write(f"{date}:\n")
        for concert in concerts:
            file.write(f"{concert['artists']}\n")
        file.write("\n")