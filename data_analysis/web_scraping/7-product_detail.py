#!/usr/bin/env python3
"""Scrape details of a single product using Selenium."""

import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """Scrape details from a single product page.

    Args:
        url (str): URL of the product detail page.
        delay (float): Seconds to wait after loading the page.

    Returns:
        dict: Product title, price, description, and rating.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(delay)

        caption = driver.find_element(
            "css selector",
            ".caption"
        )

        headings = caption.find_elements(
            "css selector",
            "h4"
        )

        title = headings[1].text.strip()

        price = caption.find_element(
            "css selector",
            "h4.price"
        ).text.strip()

        description = caption.find_element(
            "css selector",
            "p.description"
        ).text.strip()

        stars = driver.find_elements(
            "css selector",
            ".ratings .ws-icon-star"
        )

        return {
            "title": title,
            "price": price,
            "description": description,
            "rating": len(stars)
        }

    finally:
        driver.quit()
