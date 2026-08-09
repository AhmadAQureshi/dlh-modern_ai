#!/usr/bin/env python3
"""Scrape quotes from all paginated pages."""

import time
from urllib import parse

from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """Scrape quotes by following pagination links.

    Args:
        base_url (str): URL of the first quotes page.

    Returns:
        list: All quote dictionaries collected from every page.
    """
    all_quotes = []
    current_url = base_url
    visited_urls = set()

    while current_url and current_url not in visited_urls:
        visited_urls.add(current_url)

        page_quotes = scrape_basic(current_url)
        all_quotes.extend(page_quotes)

        html = fetch_html(current_url)
        soup = BeautifulSoup(html, "html.parser")

        next_item = soup.find("li", class_="next")

        if next_item is None:
            break

        next_link = next_item.find("a", href=True)

        if next_link is None:
            break

        current_url = parse.urljoin(
            current_url,
            next_link["href"]
        )

        time.sleep(0.5)

    return all_quotes