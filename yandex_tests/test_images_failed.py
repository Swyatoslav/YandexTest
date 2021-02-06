import allure
from testing_framework import *

from yandex_pages.yandex_images import YandexImagesResults, YandexImagesTopics, YandexImage
from yandex_pages.yandex_main import YandexMain


@allure.parent_suite("Yandex UI")
class TestImagesFailed:
    """Test shows example of error """

    @allure.suite("Images")
    @allure.sub_suite('Failed images')
    def test_01_check_switching_images_failed(self, test_case):
        """Test shows example of error"""

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

        raise AssertionError('Test error')
