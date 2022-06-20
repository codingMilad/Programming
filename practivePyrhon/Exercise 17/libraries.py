# Importing modules
from bs4 import BeautifulSoup
import requests

# Access the text using requests module
new_york_times = requests.get("https://www.nytimes.com")
new_york_times_html = new_york_times.text

# Parsing text using beautifulsoup module
soup = BeautifulSoup(new_york_times_html, 'html.parser')
for content in soup.find_all("h3"):
    print(content.get_text())