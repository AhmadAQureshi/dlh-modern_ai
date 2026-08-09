#!/usr/bin/env python3
"""Provide a function for retrieving the HTML content of a web page."""

import requests


def fetch_html(url, headers=None, timeout=10):
    """Fetch a web page and return its HTML content as text.

    Args:
        url (str): URL of the web page to retrieve.
        headers (dict, optional): HTTP headers included in the request.
        timeout (int, optional): Maximum waiting time in seconds.

    Returns:
        str: Full HTML content returned by the server.

    Raises:
        requests.exceptions.RequestException: If the request fails or
            the server returns an HTTP status code of 400 or higher.
    """
    response = requests.get(
        url,
        headers=headers,
        timeout=timeout
    )
    response.raise_for_status()

    return response.text