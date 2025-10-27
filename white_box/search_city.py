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
    result = []
    if len(text) < 2:
        return result
    return result
