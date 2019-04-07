import selenium

from selenium import webdriver

from django.test import LiveServerTestCase

class TitleTest(LiveServerTestCase):

    def  setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_title_shown_on_home_page(self):
        self.browser.get(self.live_server_url)
        assert 'Travel Wishlist' in self.browser.title