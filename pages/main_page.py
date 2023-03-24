from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MainPage:
    def __init__(self, browser):
        self.browser = browser

    def test_arena_login(self):
        email = self.browser.find_element(By.ID, 'email')
        password = self.browser.find_element(By.ID, 'password')
        log_in_button = self.browser.find_element(By.ID, 'login')
        email.send_keys('administrator@testarena.pl')
        password.send_keys('sumXQQ72$L')
        log_in_button.click()

    def wait_for_load(self, element):
        wait = WebDriverWait(self.browser, 10)
        element = (By.CLASS_NAME, element)
        wait.until(expected_conditions.presence_of_element_located(element))

    def open_admin_panel(self):
        admin_panel = self.browser.find_element(By.CLASS_NAME, 'header_admin')
        admin_panel.click()

