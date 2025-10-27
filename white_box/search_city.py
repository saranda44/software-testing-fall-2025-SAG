# -*- coding: utf-8 -*-
"""function search_city"""

# collection of strings that will act as a database for the city names
CITIES = [
    "Paris",
    "Budapest",
    "Skopje",
    "Rotterdam",
    "Valencia",
    "Vancouver",
    "Amsterdam",
    "Vienna",
    "Sydney",
    "New York City",
    "London",
    "Bangkok",
    "Hong Kong",
    "Dubai",
    "Rome",
    "Istanbul",
]


def search_city(text):
    """function search city version 1"""
    if text == "*":
        return CITIES

    if len(text) < 2:
        return []

    text_lower = text.lower()

    result = [city for city in CITIES if text_lower in city.lower()]

    return result
