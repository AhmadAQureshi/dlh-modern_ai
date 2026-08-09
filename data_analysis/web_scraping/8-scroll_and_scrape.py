#!/usr/bin/env python3
"""Scroll through an infinite page and scrape all product information."""

import time

from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll through an infinite-scroll page and extract products.

    Args:
        url (str): URL of the infinite-scroll product page.
        scroll_pause (float): Seconds to wait after each scroll.

    Returns:
        list: Unique product dictionaries containing title, price,
        description, and rating.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    products = []
    seen_products = set()

    try:
        driver.get(url)
        time.sleep(scroll_pause)

        previous_height = driver.execute_script(
            "return document.body.scrollHeight"
        )

        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            time.sleep(scroll_pause)

            current_height = driver.execute_script(
                "return document.body.scrollHeight"
            )

            if current_height == previous_height:
                break

            previous_height = current_height

        product_cards = driver.find_elements(
            "css selector",
            "div.thumbnail"
        )

        for card in product_cards:
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
            star_elements = card.find_elements(
                "css selector",
                ".ratings p.ws-icon.ws-icon-star"
            )

            title = title_element.get_attribute("title")
            price = price_element.text.strip()
            product_key = (title, price)

            if product_key in seen_products:
                continue

            seen_products.add(product_key)

            products.append({
                "title": title,
                "price": price,
                "description": description_element.text.strip(),
                "rating": len(star_elements)
            })

    finally:
        driver.quit()

    return products
