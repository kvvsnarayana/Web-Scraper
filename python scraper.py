import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_quotes():
    url = "https://quotes.toscrape.com/"
    headers = {"User-Agent": "Mozilla/5.0"} # Prevents some websites from blocking you
    
    try:
        # 1. Handling Network Fluctuations (Exception Handling)
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Raises an error for bad status codes (like 404 or 500)
        
        # 2. Parsing the Data
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        
        scraped_data = []
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            scraped_data.append([text, author])

        # 3. Organizing into a CSV File
        with open('scraped_quotes.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Quote", "Author"]) # Header
            writer.writerows(scraped_data)
            
        print(f"Successfully scraped {len(scraped_data)} items!")

    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    scrape_quotes()