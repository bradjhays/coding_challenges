"""."""
import os
import csv
import time
import logging

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


logger = logging.getLogger(__name__)


def main():
    # Set up the Chrome driver
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Navigate to the Google search page
    driver.get(
        "https://www.google.com/search?q=site%3Acrunchbase.com+%2B+%22their+latest+funding+was%22+%2B+2023"
    )

    # Wait for the "More results" button to appear and click it
    driver.implicitly_wait(5)
    more_button = driver.find_element(By.CLASS_NAME, "VknLRd")
    more_button.click()

    # Wait for the search results to load
    time.sleep(5)

    # Extract the search results and write them to a CSV file
    with open("search_results.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Description", "URL"])
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        results = soup.select("div.tF2Cxc")
        for result in results:

            title = None
            logger.info("starting %s", result)
            try:
                title = result.select_one("h3").text
            except Exception as err:
                logger.warning("- failed to get title: %s", err)

            description = None
            try:
                description = result.select_one("span.aCOpRe").text
            except Exception as err:
                logger.warning("- failed to get description: %s", err)

            url = None
            try:
                url = result.select_one("a")["href"]
            except Exception as err:
                logger.warning("- failed to get url: %s", err)

            writer.writerow([title, description, url])

    # Close the Chrome driver
    driver.quit()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        force=True,
        format="[%(asctime)s] p%(process)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
    )
    main()
