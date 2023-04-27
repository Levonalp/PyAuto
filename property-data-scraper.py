import requests
from bs4 import BeautifulSoup
import pandas as pd


def fetch_property_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    property_data = {
        'address': soup.find('div', {'class': 'address'}).text.strip(),
        'square_footage': int(soup.find('div', {'class': 'square-footage'}).text.strip()),
        'age': int(soup.find('div', {'class': 'age'}).text.strip()),
        'num_rooms': int(soup.find('div', {'class': 'num-rooms'}).text.strip()),
        'recent_sales': [int(sale.text.strip()) for sale in soup.find_all('div', {'class': 'recent-sale'})]
    }

    return property_data

def collect_property_data(urls):
    property_data_list = []
    
    for url in urls:
        property_data = fetch_property_data(url)
        property_data_list.append(property_data)
    
    property_data_df = pd.DataFrame(property_data_list)
    
    return property_data_df

if __name__ == "__main__":
    property_urls = [
        'https://www.example.com/property/123',
        'https://www.example.com/property/456',
        'https://www.example.com/property/789'
    ]

    property_data_df = collect_property_data(property_urls)
    print(property_data_df)
