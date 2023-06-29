import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
response = requests.get('https://example.com')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract specific data from the webpage
# ...

