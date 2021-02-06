from testing_framework import *
import allure


class YandexMain:
    """Elements of Yandex main page"""

    def __init__(self, test_case):
        self.test_case = test_case
        self.search_inp         =   TextField(By.CSS_SELECTOR, '[id="text"]',                  'Search',             self.test_case)
        self.images_btn         =   Button(   By.CSS_SELECTOR, '[data-id="images"]',           'Images',             self.test_case)
        self.suggestions_popup  =   PopupList(By.CSS_SELECTOR, '.mini-suggest__popup-content', 'Search suggestions', self.test_case)

    @allure.step('Open Yandex page')
    def open_site(self):
        """Open Yandex page"""

        self.test_case.driver.get(self.test_case.site)
        self.search_inp.should_be_displayed()

    @allure.step('Open images service')
    def open_images_service(self):
        """Open images service by button"""

        self.images_btn.click()
        delay(0.2, 'Wait for new window')
        second_window = self.test_case.driver.window_handles[1]
        self.test_case.driver.switch_to.window(second_window)

    @allure.step('Search site by text and select from results')
    def search_site_and_select_from_suggest(self, search_text):
        """Function to enter into search field some text and select something from suggestions
        :param search_text: text to be entered into search field
        """

        self.search_inp.enter_text(search_text)
        self.suggestions_popup.should_be_displayed()
        self.suggestions_popup.select(search_text)