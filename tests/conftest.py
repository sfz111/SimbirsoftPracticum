from _pytest.fixtures import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.form_page import FormPage


@fixture(scope="function")
def driver():
    options = Options()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    yield driver

    driver.quit()


@fixture(scope="function")
def form_page(driver):
    yield FormPage(driver)