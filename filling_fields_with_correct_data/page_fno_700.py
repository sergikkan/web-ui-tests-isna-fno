from locators.fno_700_locators import FNO700Locators
from browser_interaction import BasePage
import allure
from time import sleep
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
import pyautogui


class FNO700Page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO700Locators

    def check_tax_period_text(self):
        try:
            assert 'Декларация по налогу на транспортные средства, по земельному налогу и налогу на имущество (форма ' \
                   '700.00)' \
                   in self.browser.page_source
        finally:
            allure.attach(self.browser.get_screenshot_as_png(), name='Выборка налогового периода',
                          attachment_type=allure.attachment_type.PNG)

    # ВЫБОР НАЛОГОВОГО ПЕРИОДА ФНО700
    def select_date_tax_pay(self):
        sleep(1)
        self.find_element(*self.locator.YEAR_SELECT).click()
        sleep(0.5)
        self.find_element(*self.locator.SELECT_2021).click()
        sleep(2)
        self.find_element(*self.locator.SEND_TAX_PERIOD).click()

    def first_page(self):
        self.find_element(*self.locator.DECLARATION_TYPE).click()
        sleep(0.3)
        self.find_element(*self.locator.DECLARATION_TYPE_SELECT).click()
        self.find_element(*self.locator.CONTROL_TEXT).click()
        self.find_element(*self.locator.NOTICE_NUMBER).send_keys('123zxc/.;')
        sleep(0.3)
        self.find_element(*self.locator.NOTICE_DATE).click()
        sleep(0.3)
        self.find_element(*self.locator.NOTICE_DATE_SELECT).click()
        assert '123zxc/.;' not in self.browser.page_source
        self.scroll('600')
        self.find_element(*self.locator.TAX_PAYER_CATEGORIES).click()
        sleep(0.3)
        self.find_element(*self.locator.TAX_PAYER_CATEGORIES_SELECT).click()
        self.find_element(*self.locator.CONTROL_TEXT_2).click()
        self.find_element(*self.locator.APPS).click()
        sleep(0.3)
        self.find_element(*self.locator.APPS_SELECT_ALL).click()
        self.find_element(*self.locator.AFTER).click()

    def app_1(self):
        self.find_element(*self.locator.FIND).click()
        sleep(0.3)
        self.find_element(*self.locator.FIND_0101).send_keys('0')
        sleep(0.3)
        self.find_element(*self.locator.SELECT_0101).click()
        self.find_element(*self.locator.CONFIRM).click()
        self.find_element(*self.locator.TYPE_OF_TAX).click()
        sleep(0.3)
        self.find_element(*self.locator.TYPE_OF_TAX_SELECT).click()
        self.find_element(*self.locator.CHAPTER_1).click()
        self.scroll('800')
        self.find_element(*self.locator.FIRST_1).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIRST_2).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIRST_3).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIRST_4).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIRST_5).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIRST_6).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIRST_7).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIRST_8).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIRST_9).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIRST_10).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIRST_11).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIRST_12).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.CHAPTER_2).click()
        self.scroll('600')
        self.find_element(*self.locator.SECOND_1).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SECOND_2).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SECOND_3).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.CHAPTER_3).click()
        self.scroll('600')
        self.find_element(*self.locator.THIRD_1).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.THIRD_2).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.THIRD_3).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.THIRD_4).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.THIRD_5).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.THIRD_6).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.THIRD_7).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.THIRD_8).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.THIRD_9).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.CHAPTER_4).click()
        self.scroll('600')
        self.find_element(*self.locator.FOURTH_1).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FOURTH_2).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FOURTH_3).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FOURTH_4).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FOURTH_5).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FOURTH_6).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.CHAPTER_5).click()
        self.scroll('500')
        self.find_element(*self.locator.FIFTH_1).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIFTH_2).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIFTH_3).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIFTH_4).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIFTH_5).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIFTH_6).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIFTH_7).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIFTH_8).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIFTH_9).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIFTH_10).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIFTH_11).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.FIFTH_12).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.CHAPTER_6).click()
        self.scroll('700')
        self.find_element(*self.locator.SIXTH_1).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_2).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_3).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_4).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_5).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_6).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_7).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_8).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_9).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_10).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_11).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_12).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_13).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_14).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_15).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_16).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_17).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_18).send_keys('123')
        self.scroll('600')
        self.find_element(*self.locator.SIXTH_19).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_20).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_21).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_22).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_23).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_24).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_25).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SIXTH_26).send_keys('123')
        self.find_element(*self.locator.CHAPTER_7).click()
        self.scroll('600')
        self.find_element(*self.locator.SEVENTH_1).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_2).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_3).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_4).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_5).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_6).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_7).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_8).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_9).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_10).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_11).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_12).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_13).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_14).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_15).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_16).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_17).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_18).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_19).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.SEVENTH_20).send_keys('123')
        self.scroll('600')
        self.find_element(*self.locator.CHAPTER_8).click()
        self.find_element(*self.locator.EIGHT_1).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.EIGHT_2).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.EIGHT_3).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.EIGHT_4).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.EIGHT_5).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.EIGHT_6).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.EIGHT_7).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.EIGHT_8).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.EIGHT_9).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.EIGHT_10).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.EIGHT_11).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.EIGHT_12).send_keys('123')
        self.scroll('600')
        self.find_element(*self.locator.CHAPTER_9).click()
        self.find_element(*self.locator.NINTH_1).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.NINTH_2).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.NINTH_3).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.NINTH_4).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.NINTH_5).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.NINTH_6).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.NINTH_7).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.NINTH_8).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.NINTH_9).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.NINTH_10).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.NINTH_11).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.NINTH_12).send_keys('123')
        self.scroll('600')
        self.find_element(*self.locator.CHAPTER_10).click()
        self.find_element(*self.locator.TENTH_1).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.TENTH_2).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.TENTH_3).send_keys('123')
        sleep(0.2)
        self.find_element(*self.locator.TENTH_4).send_keys('123')
        self.scroll('500')
        self.find_element(*self.locator.SUM).send_keys('123')
        self.find_element(*self.locator.AFTER).click()

    def app_2(self):
        sleep(2)
        pyautogui.moveTo(655, 738, 0.1)
        pyautogui.click()
        sleep(0.3)
        self.find_element(*self.locator.FIND_0101).send_keys('0')
        sleep(0.3)
        self.find_element(*self.locator.SELECT_0101).click()
        self.find_element(*self.locator.CONFIRM).click()
        sleep(1)
        pyautogui.moveTo(1137, 738, 0.1)
        pyautogui.click()
        sleep(0.7)
        pyautogui.moveTo(958, 243, 0.1)
        pyautogui.click()
        pyautogui.write('0')
        sleep(0.3)
        self.find_element(*self.locator.SELECT_0101).click()
        pyautogui.moveTo(907, 734, 1)
        pyautogui.click()
        sleep(0.5)
        self.scroll('650')
        self.find_element(*self.locator.FIELD_APP_2).send_keys('123')
        self.find_element(*self.locator.ADD_STR).click()
        self.find_element(*self.locator.SECOND_APP_B).send_keys('123')
        self.find_element(*self.locator.SECOND_APP_D).send_keys('123')
        self.find_element(*self.locator.SECOND_APP_C).click()
        sleep(0.2)
        self.find_element(*self.locator.SECOND_APP_C_SELECT).click()
        self.find_element(*self.locator.SECOND_APP_E).click()
        sleep(0.2)
        self.find_element(*self.locator.SECOND_APP_E_SELECT).click()
        self.find_element(*self.locator.SECOND_APP_F).send_keys('123')
        self.find_element(*self.locator.SECOND_APP_G).send_keys('123')
        self.find_element(*self.locator.SECOND_APP_H).send_keys('123')
        self.find_element(*self.locator.SECOND_APP_I).send_keys('123')
        element = self.browser.find_element_by_xpath('//*[text()="Далее"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        self.find_element(*self.locator.SECOND_APP_J).send_keys('123')
        self.find_element(*self.locator.SECOND_APP_K).send_keys('123')
        self.find_element(*self.locator.SECOND_APP_L).send_keys('123')
        self.find_element(*self.locator.SECOND_APP_M).send_keys('123')
        self.find_element(*self.locator.ADD).click()
        self.find_element(*self.locator.AFTER).click()

    def app_3(self):
        sleep(1)
        self.find_element(*self.locator.FIND).click()
        sleep(0.3)
        self.find_element(*self.locator.FIND_0101).send_keys('0')
        sleep(0.3)
        self.find_element(*self.locator.SELECT_0101).click()
        self.find_element(*self.locator.CONFIRM).click()
        self.find_element(*self.locator.FIELD_APP_3).send_keys('123')
        self.scroll('5000')
        self.find_element(*self.locator.ADD_STR).click()
        self.find_element(*self.locator.APP_3_C).send_keys('123')
        pyautogui.moveTo(650, 399, 0.1)
        pyautogui.click()
        sleep(0.7)
        pyautogui.moveTo(958, 243, 0.1)
        pyautogui.click()
        pyautogui.write('0')
        sleep(0.3)
        self.find_element(*self.locator.SELECT_0101).click()
        pyautogui.moveTo(907, 734, 1)
        pyautogui.click()
        sleep(0.5)
        self.find_element(*self.locator.ADD).click()
        self.find_element(*self.locator.AFTER).click()

    def fifth_page(self):
        self.find_element(*self.locator.FIFTH_PAGE_FIELD_2).send_keys('123')
        self.find_element(*self.locator.FIFTH_PAGE_FIELD_4).send_keys('123')
        self.find_element(*self.locator.FIFTH_PAGE_FIELD_5_I).send_keys('123')
        self.find_element(*self.locator.FIFTH_PAGE_FIELD_5_II).send_keys('123')
        self.find_element(*self.locator.FIFTH_PAGE_FIELD_9).send_keys('123')
        self.scroll('5000')
        self.find_element(*self.locator.FIFTH_PAGE_FIELD_10).send_keys('123')
        self.find_element(*self.locator.FIFTH_PAGE_FIELD_11).send_keys('123')
        self.find_element(*self.locator.AFTER).click()

    def end_page(self):
        self.scroll('600')
        self.find_element(*self.locator.CONFIRMATION).click()
        self.find_element(*self.locator.FORM).click()
        sleep(5)