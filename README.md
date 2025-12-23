# Web-Scraper
Engineered a web scraping tool using Python, BeautifulSoup, and Requests to extract and aggregate data from public web pages into structured CSV formats.
A Python-based web scraper designed to collect and organize data from public websites while handling network instability.

# 🚀 Features
* Data Extraction: Extracts quotes and authors from `quotes.toscrape.com` using BeautifulSoup.
* Data Organization: Automatically exports scraped data into a structured `CSV` file.
* Resilient Logic: Uses custom exception handling to manage timeouts and connection errors.

# 🛠️ Tech Stack
* Python Libraries: `requests`, `beautifulsoup4`, `csv`.
* Exception Handling: Implemented `try-except` blocks for `HTTPError`, `ConnectionError`, and `Timeout`.
* User-Agent Spoofing: Included headers to mimic a real browser and prevent simple bot blocking.

# 📦 Installation & Usage
1. Install dependencies: pip install requests beautifulsoup4
2. Run the scraper: python scraper.py
3. View the results in: scraped_quotes.csv
