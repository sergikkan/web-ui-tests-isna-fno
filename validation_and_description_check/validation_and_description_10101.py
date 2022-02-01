from locators.fno_10101_locators import FNO1010locators
from browser_interaction import BasePage
from time import sleep
import allure
from locators.fno_10101_locators import FNO1010locatorsName as N


class FNO10101WithDescription(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO1010locators

    # РАЗДЕЛ ОБЩАЯ ИНФОРМАЦИЯ
    def section_general_information(self):
        sleep(1)
        assert 'Вид Расчета' in self.browser.page_source
        assert 'Налоговый период' in self.browser.page_source
        assert 'Код валюты' in self.browser.page_source
        self.find_element(*self.locator.DECLARATION_TYPE_SELECT).click()
        self.find_element(*self.locator.INITIAL_SELECT).click()
        self.scroll_200_px()
        sleep(1)

    def section_information_about_taxpayer(self):
        assert 'Отдельные категории налогоплательщика' in self.browser.page_source
        assert 'Вид Расчета' in self.browser.page_source
        self.find_element(*self.locator.SEPERATE_CATEGORY).click()
        self.find_element(*self.locator.CONFIDENTIONAL_SELECT).click()
        self.find_element(*self.locator.TAXPAYER_CHP).click()
        self.scroll_500_px()
        assert 'Расчет суммы авансовых платежей по КНП в соответствии с подпунктом 1) пункта 5 статьи 305 Налогового' \
               ' кодекса' in self.browser.page_source
        assert 'Расчет суммы авансовых платежей по КНП в соответствии с подпунктом 2) пункта 5 статьи 305 Налогового' \
               ' кодекса' in self.browser.page_source

    def second_page_with_first_option(self):
        self.side_stepper_false()
        assert '101.01.001' in self.browser.page_source
        assert 'Общая сумма авансовых платежей за предыдущий налоговый период' in self.browser.page_source
        self.max_symbol_15_input(*self.locator.TOTAL_ADVANCE_AMOUNT, name=N.TOTAL_ADVANCE_AMOUNT)
        self.check_zero_value_input(*self.locator.TOTAL_ADVANCE_AMOUNT,  name=N.TOTAL_ADVANCE_AMOUNT)
        self.check_letter_input(*self.locator.TOTAL_ADVANCE_AMOUNT,  name=N.TOTAL_ADVANCE_AMOUNT)
        self.check_special_symbol_input(*self.locator.TOTAL_ADVANCE_AMOUNT,  name=N.TOTAL_ADVANCE_AMOUNT)

        assert '101.01.002' in self.browser.page_source
        assert 'Cумма авансовых платежей, подлежащая уплате за период до сдачи декларации' in self.browser.page_source
        self.max_symbol_15_input(*self.locator.TOTAL_ADVANCE_AMOUNT_BEFORE_DECLARATION,  name=N.TOTAL_ADVANCE_AMOUNT_BEFORE_DECLARATION)
        self.check_zero_value_input(*self.locator.TOTAL_ADVANCE_AMOUNT_BEFORE_DECLARATION,  name=N.TOTAL_ADVANCE_AMOUNT_BEFORE_DECLARATION)
        self.check_letter_input(*self.locator.TOTAL_ADVANCE_AMOUNT_BEFORE_DECLARATION,  name=N.TOTAL_ADVANCE_AMOUNT_BEFORE_DECLARATION)
        self.check_special_symbol_input(*self.locator.TOTAL_ADVANCE_AMOUNT_BEFORE_DECLARATION,  name=N.TOTAL_ADVANCE_AMOUNT_BEFORE_DECLARATION)

        assert '101.01.003' in self.browser.page_source
        assert 'Сумма ежемесячного авансового платежа' in self.browser.page_source

        self.scroll_200_px()
        self.after_button_click()

    def second_page_with_second_option(self):
        self.side_stepper_false()
        assert '101.01.004' in self.browser.page_source
        assert 'Предполагаемая сумма КПН, исчисленная в соответствии с пунктом 1 статьи 302 Налогового кодекса' \
               in self.browser.page_source
        self.max_symbol_15_input(*self.locator.EXPECTED_SUM, name=N.EXPECTED_SUM)
        self.check_zero_value_input(*self.locator.EXPECTED_SUM, name=N.EXPECTED_SUM)
        self.check_letter_input(*self.locator.EXPECTED_SUM, name=N.EXPECTED_SUM)
        self.check_special_symbol_input(*self.locator.EXPECTED_SUM, name=N.EXPECTED_SUM)

        assert '101.01.005' in self.browser.page_source
        assert 'Предполагаемая сумма КПН, исчисленная в соответствии со статьей 652 Налогового кодекса' \
               in self.browser.page_source
        self.max_symbol_15_input(*self.locator.EXPECTED_SUM2, name=N.EXPECTED_SUM2)
        self.check_zero_value_input(*self.locator.EXPECTED_SUM2, name=N.EXPECTED_SUM2)
        self.check_letter_input(*self.locator.EXPECTED_SUM2, name=N.EXPECTED_SUM2)
        self.check_special_symbol_input(*self.locator.EXPECTED_SUM2, name=N.EXPECTED_SUM2)

        assert '101.01.006' in self.browser.page_source
        assert 'Сумма авансовых платежей, подлежащая уплате за период до сдачи декларации (101.01.004 + 101.01.005/4)' \
               in self.browser.page_source
        assert '101.01.007' in self.browser.page_source
        assert 'Уменьшение суммы авансовых платежей в соответствии со статьей 700 Налогового кодекса' in \
               self.browser.page_source
        self.max_symbol_15_input(*self.locator.DECLINE_SUM1, name=N.DECLINE_SUM1)
        self.check_zero_value_input(*self.locator.DECLINE_SUM1, name=N.DECLINE_SUM1)
        self.check_letter_input(*self.locator.DECLINE_SUM1, name=N.DECLINE_SUM1)
        self.check_special_symbol_input(*self.locator.DECLINE_SUM1, name=N.DECLINE_SUM1)
        self.scroll_900_px()
        assert '101.01.008' in self.browser.page_source
        assert 'Итого сумма авансовых платежей, подлежащая уплате за период до сдачи декларации ' \
               '(101.01.006 - 101.01.007)'
        assert '101.01.009' in self.browser.page_source
        assert 'Сумма ежемесячного авансового платежа' in self.browser.page_source
        self.after_button_click()

    def sending_page(self):
        assert 'Код ОГД' in self.browser.page_source
        assert 'Я несу ответственность в соответствии с Законом Республики Казахстан за достоверность и ' \
               'полноту сведений, приведенных в данной декларации' in self.browser.page_source
        self.scroll_900_px()
        self.check_without_filling_ogd_code()

        allure.attach(self.browser.get_screenshot_as_png(), name='максимальное кол-во символов проверка',
                      attachment_type=allure.attachment_type.PNG)
