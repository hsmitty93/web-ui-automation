"""
This Module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""
from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoResultPage:

    # Locators
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    # Shortcut
    RESULT_URL = 'https://duckduckgo.com/?q=panda&t=hk&ia=web'

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def result_link_titles(self) -> List:
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self) -> str:
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def load(self, search_phrase):
        self.browser.get(self.RESULT_URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)

        # Clean the input of previous search
        search_input.clear()
        search_input.send_keys(phrase + Keys.RETURN)

    def title(self):
        return self.browser.title
