import shutil

import allure
import pytest
from allure_commons.types import AttachmentType
from testing_framework import *
import os

from yandex_pages.yandex_main import YandexMain


@pytest.fixture(scope='function')
def test_case(request):
    """Function prepare test environment and open Yandex site"""

    log('Fill main test case options')
    tmp_test_case = TestCaseUI()  # Collector to all main test data
    tmp_test_case.screen_list = []
    tmp_test_case.driver = get_driver(tmp_test_case.config)
    tmp_test_case.screen_dir = get_screenshot_dir(request.function.__name__, tmp_test_case.config)
    YandexMain(tmp_test_case).open_site()

    def teardown():
        tmp_test_case.driver.quit()

        if tmp_test_case.screen_dir:
            shutil.rmtree(tmp_test_case.screen_dir)

    request.addfinalizer(teardown)

    return tmp_test_case


def pytest_exception_interact(node, call, report):
    test_case = node.funcargs.get('test_case')
    driver = test_case.driver

    scrn_list, scrn_path = test_case.screen_list, test_case.screen_dir

    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    allure.attach(driver.current_url, name='Fail time url', attachment_type=AttachmentType.TEXT)
    scrn_list.append(add_screenshot_to_dir(driver, scrn_path))

    with open(make_video(scrn_list, scrn_path), 'rb') as video:
        allure.attach(video.read(), name='Test Case video', attachment_type=AttachmentType.WEBM)

    console_pathes = get_console_log(driver, test_case.screen_dir)
    for index, error in enumerate(console_pathes):
        with open(error[0], 'rb') as console_file:
            allure.attach(console_file.read(), f'Console_{error[1]}', attachment_type=AttachmentType.JSON)

    network_pathes = get_network_log(driver, test_case.screen_dir)
    for index, path in enumerate(network_pathes):
        with open(path[0], 'rb') as network_log:
            allure.attach(network_log.read(), name=f"Network_{path[1]}", attachment_type=AttachmentType.JSON)

    driver.close()

