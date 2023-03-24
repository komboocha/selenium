import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
from pages.project import Project


@pytest.fixture()
def browser():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('http://demo.testarena.pl/zaloguj')
    main_page = MainPage(browser)
    main_page.test_arena_login()
    yield browser
    browser.quit()


def test_user_logged_in(browser):
    main_page = MainPage(browser)
    main_page.wait_for_load('user-info')


def test_add_new_project(browser):
    # open admin panel
    main_page = MainPage(browser)
    main_page.open_admin_panel()

    # add new project
    project_page = Project(browser)
    project_page.add_new_project()

    # verify project has been added
    project_page.verify_project_added()

    # go to projects tab
    project_page = Project(browser)
    project_page.click_on_project_label()

    # search project
    project_page = Project(browser)
    project_page.find_project('Olala')

    # verify project on the list of results
    project_page.verify_project_on_the_list('Olala')

