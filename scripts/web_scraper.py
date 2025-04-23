import requests
from bs4 import BeautifulSoup

def fetch_website_info(url):
    try:
        # Send GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get the title of the webpage
        title = soup.title.string
        print(f"Title of the website: {title}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")

if __name__ == "__main__":
    website_url = "https://example.com"  # Replace with your target URL
    fetch_website_info(website_url)
