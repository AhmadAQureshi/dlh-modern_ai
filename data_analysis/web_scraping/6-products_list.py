#!/usr/bin/env python3
"""Scrape products from a static e-commerce page using Selenium."""

import time
from selenium import webdriver


def scrape_products_list(url):
    """Scrape unique products from a static product category page.

    Args:
        url (str): URL of the product category page.

    Returns:
        list: A list of dictionaries containing product information.
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
        time.sleep(2)

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

            rating_element = card.find_element(
                "css selector",
                ".ratings p[data-rating]"
            )

            title = title_element.get_attribute("title")
            price = price_element.text.strip()

            product_key = (title, price)

            if product_key in seen:
                continue

            seen.add(product_key)

            products.append({
                "title": title,
                "price": price,
                "description": description_element.text.strip(),
                "rating": int(
                    rating_element.get_attribute("data-rating")
                )
            })

        return products

    finally:
        driver.quit()
