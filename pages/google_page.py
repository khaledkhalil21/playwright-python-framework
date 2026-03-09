from config.settings import BASE_URL


class GooglePage:

    def __init__(self, page):
        self.page = page
        self.search_box = page.locator("textarea[name='q']")

    def open(self):
        self.page.goto(BASE_URL)

    def search(self, text):
        self.search_box.fill(text)
        self.search_box.press("Enter")