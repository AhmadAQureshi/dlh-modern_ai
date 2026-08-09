#!/usr/bin/env python3
"""Log in to a website and scrape protected quotes."""

import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """Log in and scrape quotes available after authentication.

    Args:
        login_url (str): URL of the login page.
        user (str): Username.
        pwd (str): Password.

    Returns:
        list: A list of quote dictionaries.
    """
    session = requests.Session()

    login_response = session.get(login_url)
    login_response.raise_for_status()

    soup = BeautifulSoup(
        login_response.text,
        "html.parser"
    )

    csrf_token = soup.find(
        "input",
        {"name": "csrf_token"}
    )["value"]

    credentials = {
        "username": user,
        "password": pwd,
        "csrf_token": csrf_token
    }

    response = session.post(
        login_url,
        data=credentials
    )
    response.raise_for_status()

    protected_url = "https://quotes.toscrape.com/"
    response = session.get(protected_url)
    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    quotes = []

    for quote in soup.find_all("div", class_="quote"):
        text = quote.find(
            "span",
            class_="text"
        ).get_text(strip=True)

        author = quote.find(
            "small",
            class_="author"
        ).get_text(strip=True)

        tags = [
            tag.get_text(strip=True)
            for tag in quote.find_all("a", class_="tag")
        ]

        quotes.append({
            "text": text,
            "author": author,
            "tags": tags
        })

    return quotes
