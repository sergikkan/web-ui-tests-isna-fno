from locators.fno_500_locators import FNO_500_Locators
from browser_interaction import BasePage
import allure
from time import sleep
from selenium.common.exceptions import WebDriverException
from selenium import webdriver

class FNO500Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO_500_Locators

    def check_tax_period_text(self):
        try:
            assert '421.00 Расчет акциза за структурное подразделение или объекты, связанные с налогообложением' \
                   in self.browser.page_source
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Выборка налогового периода',
                          attachment_type=allure.attachment_type.PNG)

    # ВЫБОР НАЛОГОВОГО ПЕРИОДА ФНО400
    def select_date_tax_pay(self):
        sleep(1)
        self.find_element(*self.locator.MONTH).click()
        element = self.browser.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[9]/div")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        sleep(1)
        self.find_element(*self.locator.MONTH_SELECT).click()
        self.find_element(*self.locator.YEAR).click()
        sleep(0.5)
        self.find_element(*self.locator.YEAR_SELECT).click()
        sleep(2)
        self.find_element(*self.locator.SEND_DOC).click()

    ''' НИЖЕ ПЕРВАЯ СТРАНИЦА '''

    # Информация о декларации
    def first_page_before_2004(self):
        self.find_element(*self.locator.DECLARATION_TYPE).click()
        sleep(0.3)
        self.find_element(*self.locator.DECLARATION_TYPE_SELECT).click()
        self.scroll('600')
        self.find_element(*self.locator.CONTRACT_NAME).send_keys('1')
        self.find_element(*self.locator.CONTRACT_NUMBER).send_keys('2')
        self.find_element(*self.locator.CONTRACT_DATE).click()
        sleep(0.3)
        self.find_element(*self.locator.CONTRACT_DATE_SELECT_BEFORE_2005_1).click()
        sleep(0.3)
        self.find_element(*self.locator.CONTRACT_DATE_SELECT_BEFORE_2005_2).click()
        sleep(0.3)
        self.find_element(*self.locator.CONTRACT_DATE_SELECT_BEFORE_2005_3).click()
        sleep(0.3)
        self.find_element(*self.locator.CODE).click()
        sleep(0.3)
        self.find_element(*self.locator.CODE_SELECT).click()
        self.find_element(*self.locator.UNIT).send_keys('5')
        sleep(0.3)
        self.find_element(*self.locator.APPS).click()
        sleep(0.3)
        self.find_element(*self.locator.APPS_SELECT_ALL).click()
        self.scroll('800')
        sleep(0.3)
        self.find_element(*self.locator.CONTROL_TEXT2).click()
        sleep(0.3)
        self.find_element(*self.locator.AFTER).click()

    def first_page_after_2005(self):
        self.find_element(*self.locator.DECLARATION_TYPE).click()
        sleep(0.3)
        self.find_element(*self.locator.DECLARATION_TYPE_SELECT).click()
        self.scroll('600')
        self.find_element(*self.locator.CONTRACT_NAME).send_keys('1')
        self.find_element(*self.locator.CONTRACT_NUMBER).send_keys('2')
        self.find_element(*self.locator.CONTRACT_DATE).click()
        self.find_element(*self.locator.CONTRACT_DATE_SELECT_AFTER_2005).click()
        self.find_element(*self.locator.CODE).click()
        sleep(0.3)
        self.find_element(*self.locator.CODE_SELECT).click()
        self.find_element(*self.locator.UNIT).send_keys('5')
        self.find_element(*self.locator.APPS).click()
        sleep(0.3)
        self.find_element(*self.locator.APPS_SELECT_ALL).click()
        self.scroll('800')
        sleep(0.3)
        self.find_element(*self.locator.CONTROL_TEXT2).click()
        sleep(0.3)
        self.find_element(*self.locator.AFTER).click()

    def app_1(self):
        sleep(1)
        #self.find_element(*self.locator.CHAPTER_1).click()
        self.scroll('500')
        self.find_element(*self.locator.OIL_1).send_keys('10')
        self.find_element(*self.locator.OIL_2).send_keys('20')
        self.find_element(*self.locator.OIL_3).send_keys('30')
        self.find_element(*self.locator.OIL_4).send_keys('40')
        self.find_element(*self.locator.OIL_5).send_keys('50')
        self.find_element(*self.locator.OIL_6).send_keys('60')
        self.find_element(*self.locator.OIL_8).send_keys('10')
        sleep(0.3)
        assert '110' in self.browser.page_source
        self.scroll('400')
        self.find_element(*self.locator.OIL_9).send_keys('90')
        self.find_element(*self.locator.OIL_10).send_keys('100')
        self.find_element(*self.locator.OIL_11).send_keys('110')

        #self.find_element(*self.locator.CHAPTER_2).click()
        self.scroll('600')
        self.find_element(*self.locator.GAS_1).send_keys('120')
        self.find_element(*self.locator.GAS_2).send_keys('130')
        self.find_element(*self.locator.GAS_3).send_keys('140')
        self.find_element(*self.locator.GAS_4).send_keys('150')
        self.find_element(*self.locator.GAS_5).send_keys('160')
        self.find_element(*self.locator.GAS_6).send_keys('170')
        sleep(0.3)
        assert '330' in self.browser.page_source
        self.scroll('600')
        self.find_element(*self.locator.GAS_8).send_keys('20')
        self.find_element(*self.locator.GAS_9).send_keys('200')
        self.find_element(*self.locator.GAS_10).send_keys('210')
        self.find_element(*self.locator.GAS_11).send_keys('220')

        #self.find_element(*self.locator.CHAPTER_3).click()
        self.scroll('600')
        self.find_element(*self.locator.NATURE_GAS_1).send_keys('230')
        self.find_element(*self.locator.NATURE_GAS_2).send_keys('240')
        self.find_element(*self.locator.NATURE_GAS_3).send_keys('250')
        self.find_element(*self.locator.NATURE_GAS_4).send_keys('260')
        self.find_element(*self.locator.NATURE_GAS_5).send_keys('270')
        self.find_element(*self.locator.NATURE_GAS_6).send_keys('280')
        sleep(0.3)
        assert '550' in self.browser.page_source
        self.scroll('600')
        self.find_element(*self.locator.NATURE_GAS_8).send_keys('30')
        self.find_element(*self.locator.NATURE_GAS_9).send_keys('290')
        self.find_element(*self.locator.NATURE_GAS_10).send_keys('300')
        self.find_element(*self.locator.NATURE_GAS_11).send_keys('310')

        #self.find_element(*self.locator.CHAPTER_4).click()
        self.scroll('400')
        self.find_element(*self.locator.WATER_1).send_keys('320')
        self.find_element(*self.locator.WATER_2).send_keys('330')
        self.find_element(*self.locator.WATER_3).send_keys('40')
        self.find_element(*self.locator.WATER_4).send_keys('340')
        assert '980' in self.browser.page_source
        self.find_element(*self.locator.AFTER).click()

    def app_2(self):
        sleep(1)
        self.find_element(*self.locator.PART_1).click()
        self.scroll('500')
        self.find_element(*self.locator.SECOND_APP_1).send_keys('10')
        self.find_element(*self.locator.SECOND_APP_2).send_keys('20')
        self.find_element(*self.locator.SECOND_APP_3).send_keys('30')
        self.find_element(*self.locator.PART_2).click()
        self.find_element(*self.locator.SECOND_APP_4).send_keys('40')
        self.scroll('500')
        self.find_element(*self.locator.AFTER).click()

    def app_3_before_2004(self):
        sleep(0.5)
        self.find_element(*self.locator.THIRD_APP_FIRST_PART).click()
        self.scroll('500')
        self.find_element(*self.locator.THIRD_APP_1).send_keys('10')
        self.find_element(*self.locator.THIRD_APP_2).send_keys('20')
        self.find_element(*self.locator.THIRD_APP_3).send_keys('30')
        self.find_element(*self.locator.THIRD_APP_6).send_keys('1')
        self.find_element(*self.locator.THIRD_APP_8).send_keys('80')
        self.scroll('700')
        sleep(0.3)
        self.find_element(*self.locator.THIRD_APP_12).send_keys('12')
        sleep(0.3)
        self.find_element(*self.locator.THIRD_APP_14).send_keys('140')
        sleep(0.3)
        assert '80' in self.browser.page_source
        assert '10' in self.browser.page_source
        self.find_element(*self.locator.AFTER).click()

    def app_3_after_2005(self):
        sleep(1)
        self.find_element(*self.locator.THIRD_APP_SECOND_PART).click()
        self.scroll('600')
        self.find_element(*self.locator.THIRD_APP_15).send_keys('150')
        self.find_element(*self.locator.THIRD_APP_17).send_keys('170')
        self.find_element(*self.locator.THIRD_APP_19).send_keys('190')
        self.find_element(*self.locator.THIRD_APP_22).send_keys('220')
        self.find_element(*self.locator.THIRD_APP_23).send_keys('0')
        self.find_element(*self.locator.THIRD_APP_26).send_keys('260')
        self.find_element(*self.locator.THIRD_APP_27).send_keys('270')
        self.find_element(*self.locator.THIRD_APP_28).send_keys('280')
        self.find_element(*self.locator.THIRD_APP_29).send_keys('290')
        self.find_element(*self.locator.THIRD_APP_30).send_keys('0')
        self.find_element(*self.locator.AFTER).click()

    def app_4(self):
        sleep(1)
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        self.find_element(*self.locator.B_APP_4).send_keys('150')
        self.find_element(*self.locator.C_APP_4).send_keys('150')
        self.find_element(*self.locator.D_APP_4).send_keys('150')
        self.find_element(*self.locator.E_APP_4).send_keys('150')
        self.find_element(*self.locator.ADD).click()
        self.find_element(*self.locator.AFTER).click()

    def app_5(self):
        sleep(1)
        self.scroll('500')
        self.find_element(*self.locator.ADD_STR).click()
        self.find_element(*self.locator.B_APP_5).send_keys('150')
        self.find_element(*self.locator.C_APP_5).send_keys('1')
        self.find_element(*self.locator.ADD).click()
        self.find_element(*self.locator.AFTER).click()

    def app_6_before_2004(self):
        sleep(1)
        self.find_element(*self.locator.SIXTH_APP_FIRST_CHAPTER).click()
        self.scroll('500')
        self.find_element(*self.locator.SIXTH_APP_2).send_keys('20')
        self.find_element(*self.locator.SIXTH_APP_4).send_keys('40')
        self.find_element(*self.locator.SIXTH_APP_5).send_keys('50')
        self.scroll('500')
        self.find_element(*self.locator.AFTER).click()

    def app_6_after_2005(self):
        sleep(1)
        self.scroll('400')
        self.find_element(*self.locator.SIXTH_APP_SECOND_CHAPTER).click()
        self.find_element(*self.locator.SIXTH_APP_7).send_keys('70')
        self.find_element(*self.locator.SIXTH_APP_8).send_keys('80')
        self.scroll('400')
        self.find_element(*self.locator.SIXTH_APP_9).send_keys('90')
        self.find_element(*self.locator.AFTER).click()

    def app_7(self):
        sleep(1)
        self.scroll('400')
        self.find_element(*self.locator.SEVEN_APP_1).send_keys('10')
        self.find_element(*self.locator.SEVEN_APP_2).send_keys('20')
        self.find_element(*self.locator.SEVEN_APP_4).send_keys('40')
        self.find_element(*self.locator.SEVEN_APP_5).send_keys('50')
        self.find_element(*self.locator.SEVEN_APP_6).send_keys('60')
        self.scroll('800')
        self.find_element(*self.locator.SEVEN_APP_8).send_keys('80')
        self.find_element(*self.locator.SEVEN_APP_9).send_keys('90')
        self.find_element(*self.locator.SEVEN_APP_10).send_keys('100')
        self.find_element(*self.locator.SEVEN_APP_12).send_keys('120')
        self.find_element(*self.locator.SEVEN_APP_13).send_keys('130')
        self.find_element(*self.locator.SEVEN_APP_15).send_keys('150')
        self.scroll('800')
        self.find_element(*self.locator.AFTER).click()

    def second_page(self):
        sleep(1)
        self.scroll('400')
        self.find_element(*self.locator.AFTER).click()

    def end_page(self):
        sleep(1)
        self.scroll('400')
        self.find_element(*self.locator.CONFIRM).click()
        self.find_element(*self.locator.FORM).click()
        sleep(3)
