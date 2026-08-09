#!/usr/bin/env python3
"""Retrieve quote information from the quotes API."""

import json

fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """Fetch and return quotes from all available API pages.

    Args:
        base_url (str): Root URL of the quotes website.

    Returns:
        list: Quote dictionaries containing text, author, and tags.
    """
    quotes_list = []
    page = 1

    while True:
        api_url = (
            f"{base_url.rstrip('/')}/api/quotes?page={page}"
        )
        html = fetch_html(api_url)
        data = json.loads(html)

        for quote in data["quotes"]:
            quotes_list.append({
                "text": quote["text"],
                "author": quote["author"]["name"],
                "tags": quote["tags"]
            })

        if not data.get("has_next", False):
            break

        page += 1

    return quotes_list