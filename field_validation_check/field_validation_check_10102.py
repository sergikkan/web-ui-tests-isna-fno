from locators.fno_10101_locators import FNO1010locators
from locators.main_page_locators import MainPageLocators
from browser_interaction import BasePage
from selenium.webdriver.common.by import By
from time import sleep
import allure


class FNO10102FieldCheck(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO1010locators
        self.locator_main = MainPageLocators

    # РАЗДЕЛ ОБЩАЯ ИНФОРМАЦИЯ
    def all_field_name_check(self):
        assert 'Вид отчетности (расчета)' in self.browser.page_source
        assert 'Код валюты' in self.browser.page_source
        assert 'Налоговый период' in self.browser.page_source
        assert 'Отдельная категория' in self.browser.page_source
        assert 'Категории налогоплательщика	' in self.browser.page_source
        self.scroll_900_px()
        assert 'Расчет суммы авансовых платежей по КНП в соответствии с подпунктом 1) пункта 5 статьи 305 Налогового ' \
               'кодекса' in self.browser.page_source
        assert 'Расчет суммы авансовых платежей по КНП в соответствии с подпунктом 2) пункта 5 статьи 305 ' \
               'Налогового кодекса' in self.browser.page_source
        self.find_element(*self.locator.FIRST_TAX_CODEX_CHECKBOX).click()
        self.after_button_click()
        assert '101.02.001 Исчисленная сумма КПН на предыдущий налоговый период' in self.browser.page_source
        assert 'в соответствии с пунктом 1 статьи 302 Налогового кодекса' in self.browser.page_source
        assert 'в соответствии со статьей 652 Налогового кодекса' in self.browser.page_source
        assert '101.02.002 Сумма авансовых платежей, подлежащая уплате за период после сдачи декларации' \
               in self.browser.page_source
        assert 'Расчет суммы авансовых платежей по КПН в соответствии с подпунктом 4) пункта 5 статьи 305 ' \
               'Налогового кодекса' in self.browser.page_source
        assert '101.02.002 Сумма авансовых платежей, подлежащая уплате за период после сдачи декларации' \
               in self.browser.page_source
        assert '101.02.003 Уменьшение суммы авансовых платежей в соответствии со статьей ' \
               '700 Налогового кодекса' in self.browser.page_source
        assert '101.02.004 Сумма ежемесячного авансового платежа' in self.browser.page_source
        self.hover(*self.locator_main.ACTIVATE_SLIDER)
        self.find_element(*self.locator_main.FIRST_PAGE).click()
        self.scroll_700_px()
        self.find_element(*self.locator.SECOND_TAX_CODEX_CHECKBOX).click()
        self.after_button_click()
        self.scroll_700_px()
        assert '101.02.005 Предполагаемая сумма КПН, исчисленная в соответствии ' \
               'с пунктом 1 статьи 302 Налогового кодекса' in self.browser.page_source
        assert '101.02.006 Предполагаемая сумма КПН, исчисленная в ' \
               'соответствии со статьей 652 Налогового кодекса' in self.browser.page_source
        assert '101.02.008 Уменьшение суммы авансовых платежей в соответствии ' \
               'со статьей 700 Налогового кодекса' in self.browser.page_source




