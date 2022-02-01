from locators.fno_10103_locators import FNO10103Locators, FNO10103PromtText
from locators.main_page_locators import MainPageLocators
from browser_interaction import BasePage



class FNO10103Promt(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO10103Locators
        self.locator_main = MainPageLocators
        self.locator_promt = FNO10103PromtText

    def activate_promt(self):
        self.hover(*self.locator_main.PROMT)
        self.find_element(*self.locator_main.PROMT_ACTIVATE).click()

    def first_page_promt(self):
        self.hover(*self.locator.DECLARATION_TYPE)
        self.browser.find_element_by_xpath('//*[text()="Соответствующие ячейки отмечаются с учетом отнесения расчета к '
                                           'видам налоговой отчетности, указанным в статье 206 Налогового кодекса"]')
        self.scroll('700')
        self.hover(*self.locator.FIRST_MONTH_I)
        self.find_element(*self.locator_promt.PROMT_TEXT_10103001)
        self.hover(*self.locator.SECOND_MONTH_I)
        self.find_element(*self.locator_promt.PROMT_TEXT_10103001)
        self.hover(*self.locator.THIRD_MONTH_I)
        self.find_element(*self.locator_promt.PROMT_TEXT_10103001)
        self.hover(*self.locator.FIRST_MONTH_II)
        self.find_element(*self.locator_promt.PROMT_TEXT_10103002)
        self.hover(*self.locator.SECOND_MONTH_II)
        self.find_element(*self.locator_promt.PROMT_TEXT_10103002)
        self.hover(*self.locator.THIRD_MONTH_II)
        self.find_element(*self.locator_promt.PROMT_TEXT_10103002)

