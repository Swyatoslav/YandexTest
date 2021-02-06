from testing_framework import *
import allure


class YandexResults:
    """Elements of Yandex Results page"""

    def __init__(self, test_case):
        self.test_case = test_case
        self.results_list_elm       =       Element(By.CSS_SELECTOR, '.content__left .serp-list', 'Results list', self.test_case)

    @allure.step('Check url of first result link')
    def check_first_result_link(self, expected_url, is_open_site=False):
        """Function check url of first result link
        :param expected_url: expected url of first result link
        :param is_open_site: open first link by click o not
        """

        tmp_url_locator = ' div.organic__path a'

        first_link = self.results_list_elm.subelement(tmp_url_locator)
        first_link.should_be_attribute('href', expected_url)

    @allure.step('Open first site by click')
    def open_first_site_by_click(self):
        """Click by first url from results"""

        tmp_link_locator = ' div.organic__path'

        self.results_list_elm.subelement(tmp_link_locator).click()
        delay(0.2, 'Wait for new window')
        second_window = self.test_case.driver.window_handles[1]
        self.test_case.driver.switch_to.window(second_window)




