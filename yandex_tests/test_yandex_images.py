import allure
from testing_framework import *

from yandex_pages.yandex_main import YandexMain
from yandex_pages.yandex_results import YandexResults
from yandex_pages.yandex_images import YandexImagesResults, YandexImagesTopics, YandexImage


@allure.parent_suite("Yandex UI")
class TestYandexImages:
    """Checking Yandex images service"""

    @allure.suite("Images")
    @allure.sub_suite('Check switching images')
    def test_01_check_switching_images(self, test_case):
        """Test to check Yandex Images service"""

        log('Open Images service')
        YandexMain(test_case).open_images_service()

        log('Select first topic')
        YandexImagesTopics(test_case).select_first_topic()

        log('Select second image')
        YandexImagesResults(test_case).select_image(image_position=2)

        log('Switch to next image from slider')
        yandex_image = YandexImage(test_case)
        initial_image_src = yandex_image.select_next_image()

        log('Return to initial image')
        yandex_image.return_to_previous_image(initial_image_src)







