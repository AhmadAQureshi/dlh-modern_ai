#!/usr/bin/env python3
"""Scrape products from a static e-commerce page using Selenium."""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_products_list(url):
    """Scrape product information from a static product page.

    Args:
        url (str): URL of the product category page.

    Returns:
        list: Product dictionaries containing title, price,
        description, and rating.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    products = []

    try:
        driver.get(url)
        time.sleep(2)

        product_cards = driver.find_elements(
            By.CSS_SELECTOR,
            ".thumbnail"
        )

        for card in product_cards:
            title_element = card.find_element(
                By.CSS_SELECTOR,
                "a.title"
            )
            price_element = card.find_element(
                By.CSS_SELECTOR,
                "h4.price"
            )
            description_element = card.find_element(
                By.CSS_SELECTOR,
                "p.description"
            )
            rating_element = card.find_element(
                By.CSS_SELECTOR,
                ".ratings p[data-rating]"
            )

            rating_value = rating_element.get_attribute(
                "data-rating"
            )

            products.append({
                "title": title_element.get_attribute("title"),
                "price": price_element.text.strip(),
                "description": description_element.text.strip(),
                "rating": int(rating_value)
            })

    finally:
        driver.quit()

    return products