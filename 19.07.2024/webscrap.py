import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'
response = requests.get(url)
if response.status_code == 200:
    print("Successfully retrieved the page!")
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all('span', class_='titleline')
    if headlines:
        for index, headline in enumerate(headlines, 1):
            print(f"{index}. {headline.get_text()}")
    else:
        print("No headlines found. The structure of the page may have changed.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
