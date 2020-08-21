"""
This module contains share fixtures.
"""

import pytest
import selenium.webdriver
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def browser():

    # Initialize the ChromeDriver instance
    options = EdgeOptions()
    options.use_chromium = True
    b = Edge(options=options)

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()
