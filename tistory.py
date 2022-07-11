import requests
from bs4 import BeautifulSoup

TISTORY_URL = 'https://yunwoong.tistory.com/157?category=916095'
result = requests.get(TISTORY_URL)
soup = BeautifulSoup(result.text, 'html.parser')

def extract_conference_title():
    titles = []
    conference_card = soup.find_all('figure')

    for card in conference_card:
        #title
        conference_title = card.find('p', {'class':'og-title'}).string
        titles.append(conference_title)
    return titles

def extract_conference_content():
    date = []
    location = []
    conference_card = soup.find_all('ul', style='list-style-type: disc;')

    for card in conference_card:
        #date
        conference_date = card.find('li').string
        date.append(conference_date)

        #location
        conference_location = card.select_one('li:nth-child(2)').string
        location.append(conference_location)

        print(conference_location)
    return date, location

