import requests
import re
import time
from datetime import datetime, timedelta

# Base URL for scraping
base_url = "https://igenaptar.katolikus.hu/2025/?homost="

# Start and end months
start_month = "2024-12"
end_month = "2025-11"

# Function for retry logic
def fetch_with_retries(url, retries=5, delay=5):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                print(f"Retry {attempt + 1}/{retries}: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print(f"Failed to fetch {url} after {retries} attempts.")
                return None

# Function to extract gospel references from raw HTML
def extract_gospels(html):
    # Regex pattern for the gospel references
    gospel_pattern = r"<a href='nap/index.php\?holnap=(\d{4}-\d{2}-\d{2})#evangelium'>([^<]+)</a>"

    # Find all matches for dates and gospels
    matches = re.findall(gospel_pattern, html)
    return matches

# Function to scrape gospel references
def scrape_gospels():
    # Parse the start and end dates
    start_date = datetime.strptime(start_month, "%Y-%m")
    end_date = datetime.strptime(end_month, "%Y-%m")
    current_date = start_date

    while current_date <= end_date:
        # Format the sublink for the current month
        year_month = current_date.strftime("%Y-%m")
        url = f"{base_url}{year_month}"
        print(f"Processing: {year_month}...")

        # Fetch the page
        html = fetch_with_retries(url)
        if not html:
            current_date = (current_date + timedelta(days=31)).replace(day=1)
            continue

        # Extract and print gospel references
        gospels = extract_gospels(html)
        for date, gospel in gospels:
            print(f"{date} : {gospel.strip()}")

        # Move to the next month
        current_date = (current_date + timedelta(days=31)).replace(day=1)

# Run the scraper
if __name__ == "__main__":
    scrape_gospels()
