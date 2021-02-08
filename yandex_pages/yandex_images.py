from testing_framework import *
import allure


class YandexImagesTopics:
    """Elements of Yandex images topics"""

    def __init__(self, test_case):
        self.test_case = test_case
        self.topics_list_elm        =    Element(By.XPATH,        "//div[@class='PopularRequestList']", 'Popular topics list', self.test_case)
        self.indicator_elm          =    Element(By.CSS_SELECTOR, '.fade_progress_yes .spin2',          'Loader',              self.test_case)

    @allure.step('Waiting for load')
    def wait_for_load(self):
        """Waiting for request loading"""

        delay(0.5, 'Wait for indicator')
        self.indicator_elm.should_be_hidden()

    @allure.step('Select first topic')
    def select_first_topic(self):
        """Selecting first topic"""

        tmp_first_topic = "/div[contains(@class, 'ImagesList')][1]/div[contains(@class, 'PopularRequestList-Item')][1]"

        self.topics_list_elm.should_be_displayed()
        self.topics_list_elm.subelement(tmp_first_topic).click()
        self.wait_for_load()


class YandexImagesResults:
    """Elements of results of selected images topic"""

    def __init__(self, test_case):
        self.test_case = test_case
        self.results_list = Element(By.XPATH, "//*[contains(@class, 'page-layout_page_search')]//*[contains(@class, 'serp-list')]", 'Topic results', self.test_case)

    @allure.step('Select image from results')
    def select_image(self, image_position=1):
        """Selecting image from results
        :param image_position: position of image in results
        """

        tmp_image = f"/div[contains(@class, 'serp-item')][{image_position}]"

        self.results_list.should_be_displayed()
        self.results_list.subelement(tmp_image).click()


class YandexImage:
    """Elements of selected yandex image"""

    def __init__(self, test_case):
        self.test_case = test_case

        self.next_image_btn     =       Button(By.CSS_SELECTOR,  '.MediaViewer-ButtonNext', 'Next image',     self.test_case)
        self.previous_image_btn =       Button(By.CSS_SELECTOR,  '.MediaViewer-ButtonPrev', 'Previous image', self.test_case)
        self.current_img_elm    =       Element(By.CSS_SELECTOR, '.MMImageWrapper img',     'Current image',  self.test_case)

    @allure.step('Select next image')
    def select_next_image(self):
        """Select next image"""

        self.current_img_elm.should_be_displayed()
        initial_image_src = self.current_img_elm.get_attribute('src')
        self.next_image_btn.click()
        self.current_img_elm.should_not_be_attribute_value('src', initial_image_src)

        return initial_image_src

    @allure.step('Return to previous image')
    def return_to_previous_image(self, initial_image_src):
        """Return to previous image
        :param initial_image_src: value of src attribute initial image
        """

        self.previous_image_btn.click()
        delay(1, 'Waiting for action')
        self.current_img_elm.should_be_attribute('src', initial_image_src)






