#!/usr/bin/env python3
"""Scrape products from an infinite-scroll page using Selenium."""

import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll through a page and return unique product information.

    Args:
        url (str): URL of the infinite-scroll product page.
        scroll_pause (float): Time to wait between scrolls.

    Returns:
        list: A list of unique product dictionaries.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    products = []
    seen = set()

    try:
        driver.get(url)
        time.sleep(scroll_pause)

        while True:
            cards = driver.find_elements(
                "css selector",
                "div.thumbnail"
            )

            for card in cards:
                title_element = card.find_element(
                    "css selector",
                    "a.title"
                )
                price_element = card.find_element(
                    "css selector",
                    "h4.price"
                )
                description_element = card.find_element(
                    "css selector",
                    "p.description"
                )

                title = title_element.get_attribute("title")
                price = price_element.text.strip()

                product_key = (title, price)

                if product_key not in seen:
                    seen.add(product_key)

                    stars = card.find_elements(
                        "css selector",
                        ".ratings p.ws-icon.ws-icon-star"
                    )

                    products.append({
                        "title": title,
                        "price": price,
                        "description": (
                            description_element.text.strip()
                        ),
                        "rating": len(stars)
                    })

            old_height = driver.execute_script(
                "return document.body.scrollHeight"
            )

            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            time.sleep(scroll_pause)

            new_height = driver.execute_script(
                "return document.body.scrollHeight"
            )

            if new_height == old_height:
                break

    finally:
        driver.quit()

    return products
