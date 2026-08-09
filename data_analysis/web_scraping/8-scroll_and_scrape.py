#!/usr/bin/env python3
"""Scroll through a page and scrape unique products using Selenium."""

import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll through an infinite page and return unique products.

    Args:
        url (str): URL of the infinite-scroll product page.
        scroll_pause (float): Maximum waiting period for page loading.

    Returns:
        list: A list of unique product dictionaries.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        pause = min(scroll_pause, 0.3)
        previous_count = -1
        stable_count = 0
        scroll_count = 0

        while stable_count < 5 and scroll_count < 60:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            time.sleep(pause)

            cards = driver.find_elements(
                "css selector",
                "div.thumbnail"
            )

            current_count = len(cards)

            if current_count == previous_count:
                stable_count += 1
            else:
                stable_count = 0

            previous_count = current_count
            scroll_count += 1

        cards = driver.find_elements(
            "css selector",
            "div.thumbnail"
        )

        products = []
        seen = set()

        for card in cards:
            title = card.find_element(
                "css selector",
                "a.title"
            ).get_attribute("title")

            price = card.find_element(
                "css selector",
                "h4.price"
            ).text.strip()

            key = (title, price)

            if key in seen:
                continue

            seen.add(key)

            description = card.find_element(
                "css selector",
                "p.description"
            ).text.strip()

            stars = card.find_elements(
                "css selector",
                ".ratings .ws-icon-star"
            )

            products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": len(stars)
            })

        return products

    finally:
        driver.quit()
