#!/usr/bin/env python3
"""Scrape quotes from a static HTML page."""

from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """Scrape quotes, authors, and tags from the given URL.

    Args:
        url (str): URL of the quotes page to scrape.

    Returns:
        list: A list of dictionaries containing quote text,
        author, and tags.
    """
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    results = []

    for quote_block in soup.find_all("div", class_="quote"):
        text = quote_block.find("span", class_="text").get_text(strip=True)
        author = quote_block.find(
            "small",
            class_="author"
        ).get_text(strip=True)

        tags = [
            tag.get_text(strip=True)
            for tag in quote_block.find_all("a", class_="tag")
        ]

        results.append({
            "text": text,
            "author": author,
            "tags": tags
        })

    return results