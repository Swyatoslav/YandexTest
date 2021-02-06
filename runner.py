import os
import shutil
import time
from datetime import datetime

from testing_framework.pytest_runner import run_tests
from testing_framework.config import Config
import logging
from time import time, sleep

if __name__ == '__main__':

    print('Define pathes')
    root = os.getcwd()
    tests_folder = os.path.join(root, 'yandex_tests')
    result_path = os.path.join(root, 'allure-results')
    report_name = f'report_{round(time())}'
    report_path = os.path.join(root, report_name)

    print('Start tests')
    command = f'python -m pytest -n 4 {tests_folder} --alluredir {result_path}'
    print(command)
    os.system(command)

    print('Generation of new report')
    os.system(r'cd {}'.format(root))
    os.system(f'allure generate -c {result_path} -o {report_path}')

    print('Start allure server')
    sleep(1)
    os.system(r'allure open -p {} {}'.format('22222', report_path))
