from locators.main_page_locators import MainPageLocators
from time import sleep
from browser_interaction import BasePage
import allure
import pyautogui


class MainPageAttribute(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = MainPageLocators

    def select_profile_individual(self):
        sleep(1)
        self.hover(*self.locator.CHANGE_PROFILE)
        self.find_element(*self.locator.SELECT_FIZ_PROFILE).click()


class Select910FNO(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = MainPageLocators

    def send_doc(self):
        self.find_element(*self.locator.SEND_DOC_BUTTON).click()

    def input_search_910(self):
        self.find_element(*self.locator.INPUT_SEARCH).send_keys('910')

    def assert_910_fno(self):
        self.browser.find_element_by_xpath("//*[contains(.,'910.00 Упрощенная декларация"
                                           " для субъектов малого бизнеса')]").is_displayed()

    def select_910_fno_after_search(self):
        self.find_element(*self.locator.FIRST_RESULT_AFTER_SEARCH).click()

    def open_910_fno(self):
        self.send_doc()
        self.input_search_910()
        self.assert_910_fno()
        self.select_910_fno_after_search()


class Select860FNO(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = MainPageLocators

    def send_doc(self):
        self.find_element(*self.locator.SEND_DOC_BUTTON).click()

    def input_search_910(self):
        self.find_element(*self.locator.INPUT_SEARCH).send_keys('860')

    def assert_860_fno(self):
        sleep(1)
        assert '860.00 Декларация по плате за пользование водными ресурсами поверхностных источников'

    def select_860_fno_after_search(self):
        self.find_element(*self.locator.SELECT_860).click()

    def open_860_fno(self):
        self.send_doc()
        self.input_search_910()
        self.assert_860_fno()
        self.select_860_fno_after_search()


class Select870FNO(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = MainPageLocators

    def send_doc(self):
        self.find_element(*self.locator.SEND_DOC_BUTTON).click()

    def input_search_870(self):
        self.find_element(*self.locator.INPUT_SEARCH).send_keys('870')

    def assert_870_fno(self):
        sleep(1)
        assert '870.00 Декларация по плате за эмиссии в окружающую среду'

    def select_870_fno_after_search(self):
        sleep(1)
        pyautogui.moveTo(530, 646, 0.1)
        pyautogui.click()

    def open_870_fno(self):
        self.send_doc()
        self.input_search_870()
        self.assert_870_fno()
        self.select_870_fno_after_search()


class Select10101FNO(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = MainPageLocators

    def send_doc(self):
        self.find_element(*self.locator.SEND_DOC_BUTTON).click()

    def input_search_10101(self):
        self.find_element(*self.locator.INPUT_SEARCH).send_keys('101.01')

    def assert_10101_fno(self):
        self.browser.find_element_by_xpath("//*[contains(.,'101.01 Расчет суммы авансовых платежей по корпоративному "
                                           "подоходному налогу, подлежащей уплате за период до "
                                           "сдачи декларации')]").is_displayed()

    def select_10101_fno_after_search(self):
        sleep(1)
        self.find_element(*self.locator.FIRST_RESULT_AFTER_SEARCH).click()

    def open_10101_fno(self):
        self.send_doc()
        self.input_search_10101()
        self.assert_10101_fno()
        self.select_10101_fno_after_search()


class Select10102FNO(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = MainPageLocators

    def send_doc(self):
        self.find_element(*self.locator.SEND_DOC_BUTTON).click()

    def input_search_10102(self):
        self.find_element(*self.locator.INPUT_SEARCH).send_keys('101.02')

    def assert_10102_fno(self):
        self.browser.find_element_by_xpath("//*[contains(.,'101.02 Расчет суммы авансовых платежей по "
                                           "корпоративному подоходному налогу, подлежащей уплате за "
                                           "период после сдачи декларации')]").is_displayed()

    def select_10102_fno_after_search(self):
        sleep(2)
        pyautogui.moveTo(530, 656, 0.1)
        pyautogui.click()

    def open_10102_fno(self):
        self.send_doc()
        self.input_search_10102()
        self.assert_10102_fno()
        self.select_10102_fno_after_search()


class Select10103FNO(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = MainPageLocators

    def send_doc(self):
        self.find_element(*self.locator.SEND_DOC_BUTTON).click()

    def input_search_10103(self):
        self.find_element(*self.locator.INPUT_SEARCH).send_keys('101.03')

    def assert_10103_fno(self):
        self.browser.find_element_by_xpath("//*[contains(.,'101.03 Расчет по корпоративному подоходному налогу, "
                                           "удерживаемому у источника выплаты с дохода резидента')]").is_displayed()

    def select_10103_fno_after_search(self):
        sleep(1)
        self.find_element(*self.locator.FIRST_RESULT_AFTER_SEARCH).click()

    def open_10103_fno(self):
        self.send_doc()
        self.input_search_10103()
        self.assert_10103_fno()
        self.select_10103_fno_after_search()


class Select400FNO(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = MainPageLocators

    def send_doc(self):
        self.find_element(*self.locator.SEND_DOC_BUTTON).click()

    def input_search_400(self):
        self.find_element(*self.locator.INPUT_SEARCH).send_keys('400')

    def assert_400_fno(self):
        self.browser.find_element_by_xpath("//*[contains(.,'400.00 Декларация по акцизу')]").is_displayed()

    def select_400_fno_after_search(self):
        pyautogui.moveTo(530, 666, 0.1)
        pyautogui.click()

    def open_400_fno(self):
        self.send_doc()
        self.input_search_400()
        self.assert_400_fno()
        self.select_400_fno_after_search()


class Select421FNO(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = MainPageLocators

    def send_doc(self):
        self.find_element(*self.locator.SEND_DOC_BUTTON).click()

    def input_search_421(self):
        self.find_element(*self.locator.INPUT_SEARCH).send_keys('421')

    def assert_421_fno(self):
        self.browser.find_element_by_xpath("//*[contains(.,'421.00 Расчет акциза за структурное подразделение или "
                                           "объекты, связанные с налогообложением')]").is_displayed()
        sleep(2)

    def select_421_fno_after_search(self):
        pyautogui.moveTo(530, 646, 0.1)
        pyautogui.click()

    def open_421_fno(self):
        self.send_doc()
        self.input_search_421()
        self.assert_421_fno()
        self.select_421_fno_after_search()


class TaxPeriodSelect(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = MainPageLocators

    def select_date_tax_pay(self):
        sleep(1)
        self.find_element(*self.locator.HALF_YEAR_SELECT).click()
        self.find_element(*self.locator.FIRST_HALF_YEAR).click()
        self.find_element(*self.locator.INPUT_YEAR).click()
        try:
            self.find_element(*self.locator.SELECT_YEAR_2020).click()
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Выборка налогового периода 2020 г.',
                          attachment_type=allure.attachment_type.PNG)
        self.find_element(*self.locator.SEND_TAX_PERIOD).click()


class Select100FNO(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = MainPageLocators

    def send_doc(self):
        sleep(1)
        self.find_element(*self.locator.SEND_DOC_BUTTON).click()

    def input_search_100(self):
        self.find_element(*self.locator.INPUT_SEARCH).send_keys('100')
        sleep(2)

    def assert_100_fno(self):
        self.browser.find_element_by_xpath(
            "//*[contains(.,'100.00 Декларация по корпоративному подоходному налогу')]").is_displayed()

    def select_100_fno_after_search(self):
        self.find_element(*self.locator.FIRST_RESULT_AFTER_SEARCH).click()

    def select_tax_period(self):
        self.find_element(*self.locator.INPUT_YEAR).click()
        sleep(1)
        self.find_element(*self.locator.SELECT_YEAR_2020).click()
        sleep(2)
        self.find_element(*self.locator.SEND_TAX_PERIOD).click()

    def open_100_fno(self):
        self.send_doc()
        self.input_search_100()
        self.assert_100_fno()
        self.select_100_fno_after_search()
        self.select_tax_period()


class Select701FNO(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = MainPageLocators

    def send_doc(self):
        sleep(1)
        self.find_element(*self.locator.SEND_DOC_BUTTON).click()

    def input_search_701(self):
        self.find_element(*self.locator.INPUT_SEARCH).send_keys('701.00')
        sleep(2)

    def assert_701_fno(self):
        assert '701.00 Расчет текущих платежей по налогу на транспортные средства' in self.browser.page_source

    def select_701_fno_after_search(self):
        pyautogui.moveTo(530, 646, 0.1)
        pyautogui.click()

    def select_tax_period(self):
        self.find_element(*self.locator.INPUT_YEAR).click()
        sleep(1)
        self.find_element(*self.locator.SELECT_YEAR_2020).click()
        sleep(1)
        self.find_element(*self.locator.SEND_TAX_PERIOD).click()

    def open_701_fno(self):
        self.send_doc()
        self.input_search_701()
        self.assert_701_fno()
        self.select_701_fno_after_search()
        self.select_tax_period()


class Select250FNO(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = MainPageLocators

    def send_doc(self):
        sleep(1)
        self.find_element(*self.locator.SEND_DOC_BUTTON).click()

    def input_search_250(self):
        self.find_element(*self.locator.INPUT_SEARCH).send_keys('250.00')
        sleep(2)

    def assert_250_fno(self):
        assert '250.00 Декларация об активах и обязательствах физического лица' in self.browser.page_source

    def select_250_fno_after_search(self):
        pyautogui.moveTo(530, 646, 0.1)
        pyautogui.click()

    def select_tax_period(self):
        self.find_element(*self.locator.DATE_SELECT).click()
        sleep(1)
        self.find_element(*self.locator.DATE_SELECT_TODAY).click()
        sleep(1)
        self.find_element(*self.locator.SEND_TAX_PERIOD).click()

    def open_250_fno(self):
        self.send_doc()
        self.input_search_250()
        self.assert_250_fno()
        self.select_250_fno_after_search()
        self.select_tax_period()


class Select700FNO(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = MainPageLocators

    def send_doc(self):
        sleep(1)
        self.find_element(*self.locator.SEND_DOC_BUTTON).click()

    def input_search_700(self):
        self.find_element(*self.locator.INPUT_SEARCH).send_keys('700.00')
        sleep(2)

    def assert_700_fno(self):
        assert '700.00 Декларация по налогу на транспортные средства, по земельному налогу и налогу на имущество' in self.browser.page_source

    def select_700_fno_after_search(self):
        pyautogui.moveTo(530, 646, 0.1)
        pyautogui.click()

    def select_tax_period(self):
        self.find_element(*self.locator.INPUT_YEAR).click()
        sleep(1)
        self.find_element(*self.locator.SELECT_YEAR_2020).click()
        sleep(1)
        self.find_element(*self.locator.SEND_TAX_PERIOD).click()

    def open_700_fno(self):
        self.send_doc()
        self.input_search_700()
        self.assert_700_fno()
        self.select_700_fno_after_search()
        self.select_tax_period()
