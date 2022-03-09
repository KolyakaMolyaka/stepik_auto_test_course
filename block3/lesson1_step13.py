from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


class TestRegistration(unittest.TestCase):

    def setUp(self) -> None:
        self._browser = webdriver.Chrome()
        self._links = []
        for i in range(1, 3):
            self._links.append(f'http://suninjuly.github.io/registration{i}.html')

    def test_registration_pages(self):
        for link in self._links:
            self._browser.get(link)

            req_inputs = self._browser.find_elements(By.CSS_SELECTOR, 'input[required]')
            self.assertEqual(len(req_inputs), 3, f'Количество обязательных на странице {link} полей должно быть равно трём')


            for input in req_inputs:
                input.send_keys('required')

            button = self._browser.find_element_by_css_selector("button.btn")
            button.click()

            self.assertEqual(self._browser.find_element(By.TAG_NAME, 'h1').text, 'Congratulations! You have '
                                                                                 'successfully registered!')

    def tearDown(self) -> None:
        self._browser.quit()


if __name__ == '__main__':
    unittest.main()
