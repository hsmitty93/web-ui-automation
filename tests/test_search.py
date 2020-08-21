"""
These tests cover DuckDuckGo searches.
"""

import pytest

from pages_duckduckgo.result import DuckDuckGoResultPage
from pages_duckduckgo.search import DuckDuckGoSearchPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def search_links(phrase, result_page):
    """
    Search through a results page links to see if 
    titles matches the searched phrase.

    :param phrase: the phrase being searched
    :type phrase: string
    :param result_page: the browser instance for result_page
    :type result_page: class instance
    :return: an array of matches
    :rtype: array[strings]
    """
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    return matches



@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckgo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(phrase)

    # Then the search result title contains "panda"
    assert phrase in result_page.title()

    # And the search result query is "panda"
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to "panda"
    matches = search_links(phrase, result_page)
    assert len(matches) > 0



@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_search_from_results_page(browser, phrase):
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo results page is displayed
    result_page.load(phrase)

    # When the user searches for a new phrase
    result_page.search(phrase)

    # Then the search result query is a new phrase
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to the new phrase
    matches = search_links(phrase, result_page)
    assert len(matches) > 0

    # And the search result title will contain the new phrase
    assert phrase in result_page.title()

@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_autocomplete_pertain_to_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)

    # Given the DuckDuckGo search page is displayed
    search_page.load()
    wait = WebDriverWait(browser, 10)
    # When the user searches for a new phrase
    search_page.search(phrase, enter=False)

    # race condition fix
    wait.until(EC.text_to_be_present_in_element(search_page.AUTOCOMPLETE_TERM, phrase))

    # Then the autocomplete will display
    autocomplete = search_page.search_autocomplete()
    assert autocomplete.is_displayed()

    # And the autocomplete terms will contain the new phrase
    terms = search_page.autocomplete_terms().text.split("\n")
    for term in terms:
        assert phrase.lower() in term.lower()
