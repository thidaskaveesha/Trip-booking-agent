from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import urllib.parse

def search_hotels(destination, nights, budget_lkr):
    hotels = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        query = urllib.parse.quote(f"{destination} hotels booking")
        page.goto(f"https://www.google.com/search?q={query}")
        page.wait_for_timeout(3000)

        html = page.content()
        soup = BeautifulSoup(html, "html.parser")

        results = soup.select("div.g")[:5]
        for result in results:
            title = result.select_one("h3")
            link = result.select_one("a")
            if title and link:
                hotels.append({
                    "name": title.text,
                    "url": link['href']
                })

        browser.close()
    return hotels
