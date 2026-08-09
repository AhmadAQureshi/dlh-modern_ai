#!/usr/bin/env python3
"""Scrape unique products from an infinite-scroll page."""

import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll through a page and return all unique products.

    Args:
        url (str): URL of the infinite-scroll product page.
        scroll_pause (float): Maximum wait for new content.

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

        check_interval = min(0.5, scroll_pause)

        if check_interval <= 0:
            check_interval = 0.1

        stable_limit = max(
            2,
            int(scroll_pause / check_interval)
        )

        stable_count = 0
        previous_height = 0
        previous_products = 0

        while stable_count < stable_limit:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            time.sleep(check_interval)

            current_height = driver.execute_script(
                "return document.body.scrollHeight"
            )

            current_products = len(
                driver.find_elements(
                    "css selector",
                    "div.thumbnail"
                )
            )

            if (
                current_height == previous_height
                and current_products == previous_products
            ):
                stable_count += 1
            else:
                stable_count = 0

            previous_height = current_height
            previous_products = current_products

        title_elements = driver.find_elements(
            "css selector",
            "div.thumbnail a.title"
        )

        price_elements = driver.find_elements(
            "css selector",
            "div.thumbnail h4.price"
        )

        description_elements = driver.find_elements(
            "css selector",
            "div.thumbnail p.description"
        )

        rating_elements = driver.find_elements(
            "css selector",
            "div.thumbnail .ratings"
        )

        products = []
        seen = set()

        for title_element, price_element, desc_element, rating_element in zip(
            title_elements,
            price_elements,
            description_elements,
            rating_elements
        ):
            title = title_element.get_attribute("title")
            price = price_element.text.strip()

            product_key = (title, price)

            if product_key in seen:
                continue

            seen.add(product_key)

            stars = rating_element.find_elements(
                "css selector",
                "p.ws-icon.ws-icon-star"
            )

            products.append({
                "title": title,
                "price": price,
                "description": desc_element.text.strip(),
                "rating": len(stars)
            })

        return products

    finally:
        driver.quit()
