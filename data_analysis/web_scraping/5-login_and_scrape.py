#!/usr/bin/env python3
"""Log in to the quotes website and scrape protected quotes."""

import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """Log in and scrape quotes visible after authentication.

    Args:
        login_url (str): URL of the website's login page.
        user (str): Username used for authentication.
        pwd (str): Password used for authentication.

    Returns:
        list: Quote dictionaries containing text, author, and tags.

    Raises:
        ValueError: If the CSRF token cannot be found.
        requests.RequestException: If an HTTP request fails.
    """
    session = requests.Session()

    login_response = session.get(login_url, timeout=10)
    login_response.raise_for_status()

    soup = BeautifulSoup(login_response.text, "html.parser")
    csrf_input = soup.find("input", attrs={"name": "csrf_token"})

    if csrf_input is None or not csrf_input.get("value"):
        raise ValueError("CSRF token not found")

    credentials = {
        "username": user,
        "password": pwd,
        "csrf_token": csrf_input.get("value")
    }

    login_response = session.post(
        login_url,
        data=credentials,
        timeout=10
    )
    login_response.raise_for_status()

    protected_url = requests.compat.urljoin(login_url, "/")
    quotes_response = session.get(protected_url, timeout=10)
    quotes_response.raise_for_status()

    soup = BeautifulSoup(quotes_response.text, "html.parser")
    quotes = []

    for quote_block in soup.find_all("div", class_="quote"):
        text = quote_block.find(
            "span",
            class_="text"
        ).get_text(strip=True)

        author = quote_block.find(
            "small",
            class_="author"
        ).get_text(strip=True)

        tags = [
            tag.get_text(strip=True)
            for tag in quote_block.find_all("a", class_="tag")
        ]

        quotes.append({
            "text": text,
            "author": author,
            "tags": tags
        })

    return quotes
