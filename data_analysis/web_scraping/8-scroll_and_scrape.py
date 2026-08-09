#!/usr/bin/env python3
"""Scrape unique products from an infinite-scroll page."""

import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll through a page and return all unique products.

    Args:
        url (str): URL of the infinite-scroll products page.
        scroll_pause (float): Seconds to wait after each scroll.

    Returns:
        list: A list of unique product dictionaries.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.page_load_strategy = "eager"

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        last_height = driver.execute_script(
            "return document.body.scrollHeight"
        )

        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            time.sleep(scroll_pause)

            new_height = driver.execute_script(
                "return document.body.scrollHeight"
            )

            if new_height == last_height:
                break

            last_height = new_height

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
                ".ratings p.ws-icon.ws-icon-star"
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
