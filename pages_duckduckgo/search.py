"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:

    # URL
    URL = 'https://www.duckduckgo.com'

    # Locators
    SEARCH_HOMEPAGE = (By.ID, 'search_form_homepage')
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
    SEARCH_AUTOCOMPLETE = (By.CSS_SELECTOR, '.search__autocomplete')
    AUTOCOMPLETE_TERMS = (By.CSS_SELECTOR, '.acp-wrap')
    AUTOCOMPLETE_TERM = (By.CSS_SELECTOR, '.acp')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def search(self, phrase, enter=True):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.click()
        if (enter):
            search_input.send_keys(phrase + Keys.RETURN)
        else:
            search_input.send_keys(phrase)

    def search_autocomplete(self):
        return self.browser.find_element(*self.SEARCH_AUTOCOMPLETE)

    def autocomplete_terms(self):
        return self.browser.find_element(*self.AUTOCOMPLETE_TERMS)

