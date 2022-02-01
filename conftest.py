import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import allure


@pytest.fixture(scope='session')
def browser_setup_and_teardown():
    use_selenoid = False  # set to True to run tests with Selenoid

    if use_selenoid:
        browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities={
                "browserName": "chrome",
                "browserSize": "1920x1080"
            }
        )
    else:
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=ChromeDriverManager(
            chrome_type=ChromeType.GOOGLE).install())
    browser.set_window_size(1920, 1080)
    browser.implicitly_wait(10)

    yield browser

    try:
        browser.get_screenshot_as_png()
    finally:
        allure.attach(browser.get_screenshot_as_png(), name='Результат теста',
                      attachment_type=allure.attachment_type.PNG)
    browser.close()
    browser.quit()
