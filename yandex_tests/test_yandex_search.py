import allure
from testing_framework import *

from yandex_pages.yandex_main import YandexMain
from yandex_pages.yandex_results import YandexResults
from yandex_pages.yandex_images import YandexImagesResults, YandexImagesTopics, YandexImage


@allure.parent_suite("Yandex UI")
class TestYandexSearch:

    @allure.suite("Search")
    @allure.sub_suite('Search and open site by link')
    def test_01_check_search_and_open_site(self, test_case):
        """Test to check Yandex search of desired site and open"""

        search_text = 'perfect art'
        site_title = 'Perfect Art'
        expected_url = 'https://perfectart.ru/'

        log('Start search by text')
        YandexMain(test_case).search_site_and_select_from_suggest(search_text)

        log('Check search results and open first site')
        yandex_results = YandexResults(test_case)
        yandex_results.check_first_result_link(expected_url, is_open_site=True)
        yandex_results.open_first_site_by_click()

        log('Check that expected site was opened')
        assertTrue(test_case.driver.title == site_title, 'Expected site was not opened')







