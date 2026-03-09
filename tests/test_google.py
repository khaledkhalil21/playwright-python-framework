import pytest
from pages.google_page import GooglePage


@pytest.mark.parametrize("search_term", [
    "Playwright",
    "Python automation",
    "QA Automation",
    "Selenium vs Playwright",
    "pytest tutorial"
])

def test_google_search(page, search_term):

    google = GooglePage(page)

    google.open()
    google.search(search_term)
    # assert False