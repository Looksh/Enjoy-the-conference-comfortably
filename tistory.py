import requests
from bs4 import BeautifulSoup

TISTORY_URL = 'https://yunwoong.tistory.com/157?category=916095'

def extract_conference():
    result = requests.get(TISTORY_URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    print(soup.title)