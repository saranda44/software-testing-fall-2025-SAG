# -*- coding: utf-8 -*-
"""Module test function search test"""
# pylint: disable=import-error
import pytest

from white_box.search_city import CITIES, search_city


@pytest.mark.parametrize("search_text, expected", [("", []), ("P", [])])
def test_should_return_no_results_when_search_text_is_fewer_than_two_characters(
    search_text, expected
):
    """Requirement 1: Returns no results when text length < 2"""
    result = search_city(search_text)
    assert result == expected


@pytest.mark.parametrize(
    "search_text,expected_result",
    [
        ("Va", ["Valencia", "Vancouver"]),
        ("Lo", ["London"]),
        ("Ro", ["Rotterdam", "Rome"]),
    ],
)
def test_should_return_matching_cities_when_text_matches_prefix(
    search_text, expected_result
):
    """Requirement 2: Returns cities starting with the search text"""
    result = search_city(search_text)
    for city in expected_result:
        assert city in result


@pytest.mark.parametrize(
    "search_text,expected_result",
    [
        ("va", ["Valencia", "Vancouver"]),
        ("vA", ["Valencia", "Vancouver"]),
        ("lOn", ["London"]),
    ],
)
def test_should_return_results_case_insensitive_when_search_text_has_mixed_case(
    search_text, expected_result
):
    """Requirement 3: Search should be case-insensitive"""
    result = search_city(search_text)
    for city in expected_result:
        assert city in result


@pytest.mark.parametrize(
    "search_text,expected_result",
    [("ape", ["Budapest"]), ("don", ["London"]), ("ong", ["Hong Kong"])],
)
def test_should_return_cities_when_search_text_is_part_of_city_name(
    search_text, expected_result
):
    """Requirement 4: Should match substring within city names"""
    result = search_city(search_text)
    for city in expected_result:
        assert city in result


@pytest.mark.parametrize("search_text", ["*"])
def test_should_return_all_cities_when_search_text_is_asterisk(search_text):
    """Requirement 5: '*' should return all cities"""
    result = search_city(search_text)
    for city in CITIES:
        assert city in result
    assert len(result) == len(CITIES)
