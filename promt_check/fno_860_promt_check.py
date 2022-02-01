from locators.fno_860_locators import FNO860Locators
from locators.main_page_locators import MainPageLocators
from browser_interaction import BasePage
from time import sleep
import allure


class FNO860Promt(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO860Locators
        self.main_locator = MainPageLocators

    def promt_check(self):
        sleep(1)
        self.hover(*self.main_locator.PROMT)
        self.find_element(*self.main_locator.PROMT_ACTIVATE).click()
        self.hover(*self.locator.CHECKBOX_AVALIABLE_RESOLUTION)
        assert 'Указывается при наличии разрешительного документа на специальное водопользование' in \
               self.browser.page_source
        self.scroll('500')
        sleep(1)
        self.hover(*self.locator.FIRST_8600101)
        sleep(1)
        assert 'Сведения об объемах водопользования для исчисления платы заполняется в единицах измерения ' \
               'водопользования, указанных в строке 5' in self.browser.page_source
        self.hover(*self.locator.SECOND_D8600102)
        sleep(0.1)
        assert 'Сведения об объемах водопользования для исчисления платы заполняется в единицах измерения' \
               ' водопользования, указанных в строке 5' in self.browser.page_source
        self.hover(*self.locator.THIRD_8600103)
        sleep(0.1)
        assert 'Сведения об объемах водопользования для исчисления платы заполняется в единицах измерения ' \
               'водопользования, указанных в строке 5' in self.browser.page_source
        self.scroll('700')
        self.hover(*self.locator.RATE_WITHIN_THE_LIMIT)
        sleep(0.1)
        assert 'Указывается ставка платы за пользование водными ресурсами поверхностных источников в пределах' \
               ' установленного лимита, утвержденная местным представительным органом области' \
               ' (города республиканского значения, столицы)' in self.browser.page_source
        self.scroll('900')
        self.hover(*self.locator.FOURTH_CALCULATED_05)
        sleep(0.1)
        assert 'Указывается исчисленная сумма платы за пользование водными ресурсами поверхностных' \
               ' источников в пределах установленного лимита за налоговый' \
               ' период, подлежащей уплате в бюджет' in self.browser.page_source
        self.hover(*self.locator.SEVEN)
        sleep(0.1)
        assert 'Указывается сумма исчисленной платы за пользование водными ресурсами поверхностных источников сверх' \
               ' установленного лимита за налоговый период, подлежащей уплате в бюджет. Определяется как' \
               ' ( 860.01.003 IV х 860.01.005)' in self.browser.page_source
        self.hover(*self.locator.FIFVTH)
        sleep(0.1)
        assert 'Общая сумма платы за пользование водными ресурсами поверхностных источников по всем ' \
               'видам специального водопользования. Определяется как 860.01.006+860.01.007' in self.browser.page_source
