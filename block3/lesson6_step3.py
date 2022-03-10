from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
from time import time as current_time
from math import log


class TestStepik:

    # Добавление фикстуры подготовки сьюта, финализатора
    @pytest.fixture()
    def driver(self):
        browser = webdriver.Chrome()
        yield browser
        browser.quit()

    # Добавление фикстуры параметризатора для разных страниц
    @pytest.mark.parametrize('page', ['895', '896', '897', '898', '899', '903', '904', '905'])
    def test_pages(self, driver, page):
        link = f'https://stepik.org/lesson/236{page}/step/1'

        driver.get(link)

        # получение поля для ввода ответа
        textarea = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ember-text-area'))
        )
        textarea.send_keys(str(log(int(current_time()))))  # отправка ответа

        # отправка ответа
        button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission'))
        )
        button.click()

        # получение результата решения
        result_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))
        )

        got = result_element.text
        expected = "Correct!"

        assert expected == got, f'Получено "{got}", но ожидалось "{expected}"'