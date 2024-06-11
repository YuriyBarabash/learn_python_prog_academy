from bs4 import BeautifulSoup
import requests

url = 'https://themeforest.net'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup.text)
else:
    print('Failed to fetch data from the provided URL')