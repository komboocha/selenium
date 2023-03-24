from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Project:
    def __init__(self, browser):
        self.browser = browser

    def add_new_project(self):
        new_project_link = self.browser.find_element(By.CSS_SELECTOR,
                                                     "a[href='http://demo.testarena.pl/administration/add_project']")
        new_project_link.click()

    def verify_project_added(self):
        confirmation_button = self.browser.find_element(By.CSS_SELECTOR, 'p')
        assert confirmation_button.is_displayed()

    def click_on_project_label(self):
        project_label = self.browser.find_element(By.CLASS_NAME, 'item2')
        project_label.click()

    def find_project(self, name):
        project = self.browser.find_element(By.ID, 'search')
        project.send_keys(name + Keys.ENTER)

    def verify_project_on_the_list(self, name):
        results = self.browser.find_elements(By.CSS_SELECTOR,
                                             "a[href='http://demo.testarena.pl/administration/project_view/3558']")
        list_of_results = []
        for i in results:
            list_of_results.append(i.text)
        assert name in list_of_results

