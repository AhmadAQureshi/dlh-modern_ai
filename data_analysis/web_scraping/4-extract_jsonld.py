#!/usr/bin/env python3
"""Extract quote information from JSON-LD embedded in an HTML page."""

import json

from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """Extract quotes from JSON-LD blocks found at the given URL.

    Args:
        url (str): URL of the page containing JSON-LD data.

    Returns:
        list: Quote dictionaries containing text, author, and tags.
    """
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    quotes = []

    scripts = soup.find_all(
        "script",
        type="application/ld+json"
    )

    for script in scripts:
        json_content = script.string

        if not json_content:
            continue

        try:
            data = json.loads(json_content)
        except json.JSONDecodeError:
            continue

        if isinstance(data, list):
            objects = data
        else:
            objects = [data]

        for item in objects:
            if not isinstance(item, dict):
                continue

            if item.get("@type") != "Quote":
                continue

            author_data = item.get("author", {})
            if isinstance(author_data, dict):
                author = author_data.get("name")
            else:
                author = author_data

            keywords = item.get("keywords", [])

            if isinstance(keywords, str):
                tags = [
                    tag.strip()
                    for tag in keywords.split(",")
                    if tag.strip()
                ]
            elif isinstance(keywords, list):
                tags = keywords
            else:
                tags = []

            quotes.append({
                "text": item.get("text"),
                "author": author,
                "tags": tags
            })

    return quotes
