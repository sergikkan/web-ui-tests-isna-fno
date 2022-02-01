from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from locators.fno_910_page_locators import FNO910Locators
from locators.main_page_locators import MainPageLocators
from browser_interaction import BasePage
from time import sleep
import allure


class FNO_910_promt(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO910Locators
        self.locator_main = MainPageLocators

    def activate_promt(self):
        self.hover(*self.locator_main.PROMT)
        self.find_element(*self.locator_main.PROMT_ACTIVATE).click()

    def first_page_promt(self):
        self.hover(*self.locator.DECLARATION_TYPE_SELECT)
        self.browser.find_element(By.XPATH, "//*[contains(.,'Соответствующие ячейки отмечаются с учетом "
                                            "отнесения декларации к видам налоговой отчетности, указанным в "
                                            "статье 206 Налогового кодекса')]")
        self.hover(*self.locator.SEPERATE_CATEGORY)
        self.find_element(By.XPATH, "//*[contains(.,'Ячейки C или D отмечаются"
                                    " индивидуальными предпринимателями')]")
        self.scroll('500')
        self.hover(*self.locator.TIS_CHECKBOX)
        self.browser.find_element(By.XPATH, "//*[contains(.,'Ячейка отмечается в случае, если НП в "
                                            "соответствии с пунктом 2-1 статьи 687 Налогового кодекса поставил "
                                            "на учет в налоговых органах контрольно-кассовую машину с функцией "
                                            "фиксации и передачи данных или установил трехкомпонентную "
                                            "интегрированную систему (ТИС)')]")
        self.find_element(*self.locator.TIS_CHECKBOX).click()
        self.hover(*self.locator.TIS_STOCK_BEGINNING_TAX_PERIOD)
        self.find_element(By.XPATH, "//*[contains(.,'Указывается стоимость запасов на начало налогового "
                                    "периода всего')]")

        self.browser.execute_script('window.scroll(0,600)')
        self.find_element(*self.locator.AFTER_BUTTON).click()

    def second_page_promt(self):
        sleep(1)
        self.hover(*self.locator.A_INPUT_INCOME_CASHLESS)
        self.browser.find_element(By.XPATH, "//*[contains(.,'В строке А отмечаются доходы, полученные путем "
                                            "безналичных расчетов')]")
        self.hover(*self.locator.B_INPUT_INCOME_CASHLESS)

        self.browser.find_element(By.XPATH, "//*[contains(.,'В строке В отмечаются доходы, полученные "
                                            "путем наличных расчетов')]")
        self.hover(*self.locator.A_INPUT_INCOME_CASHLESS)
        calculation_of_taxes = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[4]/div/div/div'
                                                                   '[4]/form/div[1]/div[1]/div/div[2]/div/div/div/'
                                                                   'div/div[1]/div/div')
        ActionChains(self.browser).move_to_element(to_element=calculation_of_taxes).perform()
        self.browser.find_element(By.XPATH, "//*[contains(.,'В строке 910.00.001 указывается доход, определяемый в "
                                            "соответствии со статьей 681 Налогового кодекса, с учетом корректировок, "
                                            "производимых в соответствии с пунктом 6 статьи 681 Налогового кодекса')]")
        self.hover(*self.locator.A_I)
        self.browser.find_element(By.XPATH, "//*[contains(.,'В том числе, в строке I, отмечаются доходы,"
                                            " полученные с применением ТИС')]")
        self.hover(*self.locator.B_I)
        self.browser.find_element(By.XPATH, "//*[contains(.,'В том числе, в строке I отмечаются доходы,"
                                            " полученные с применением ТИС')]")

        self.hover(*self.locator.INCOME_WITH_LAW)
        self.browser.find_element(By.XPATH, "//*[contains(.,'В строке 910.00.002 указывается доход, определяемый в"
                                            " соответствии с Законом Республики Казахстан от 5 июля 2008 года «О "
                                            "трансфертном ценообразовании»')]")
        self.scroll_500_px()
        self.hover(*self.locator.EMPLOYEE_QUANTITY)
        self.browser.find_element(By.XPATH, "//*[contains(.,'В строке 910.00.003 указывается среднесписочная"
                                            " численность работников за налоговый период')]")
        self.hover(*self.locator.PENSIONER_QUANTITY)
        self.browser.find_element(By.XPATH, "//*[contains(.,'В строке 910.00.003 А указывается среднесписочная"
                                            " численность работников-пенсионеров')]")
        self.hover(*self.locator.INVALID_QUANTITY)
        self.browser.find_element(By.XPATH, "//*[contains(.,'В строке 910.00.003 В указывается"
                                            " среднесписочная численность работников-инвалидов')]")
        calc_sended_tax = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[4]/div/div/div[4]/form'
                                                              '/div[7]/div/div/div[2]/div/div/div/div/div[1]/div/div')
        ActionChains(self.browser).move_to_element(to_element=calc_sended_tax).perform()
        self.browser.find_element(By.XPATH, "//*[contains(.,'В строке 910.00.005 указывается сумма налогов, исчисленных"
                                            " по ставке, установленной пунктом 1 статьи 687 Налогового кодекса,"
                                            " определяемая по формуле: 910.00.001 х 3%')]")
        calc_tax_after_coorection = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[4]/div/div/'
                                                                        'div[4]/form/div[9]/div/div/div[2]/div/div/div'
                                                                        '/div/div[1]/div/div')
        ActionChains(self.browser).move_to_element(to_element=calc_tax_after_coorection).perform()
        self.browser.find_element(By.XPATH, "//*[contains(.,'В строке 910.00.007 указывается сумма налогов после"
                                            " корректировки, которая определяется по"
                                            " формуле: 910.00.005 – 910.00.006')]")
        self.hover(*self.locator.AVERAGE_SALARY)
        self.browser.find_element(By.XPATH, "//*[contains(.,'В строке 910.00.009 указывается сумма социального налога, "
                                            "подлежащего уплате в бюджет в размере 1/2 от исчисленной суммы налогов по"
                                            " декларации за минусом суммы социальных отчислений в Государственный фонд"
                                            " социального страхования, определяемая по формуле: (910.00.007 х 0,5) – "
                                            "910.00.013 VII – 910.00.020 VII. При этом, Если Вы имеете право на "
                                            "применение положения статьи 57 п.4 Закона о введении Налогового кодекса,"
                                            " то вправе указать «0».')]")
        IPN_calc = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[4]/div/div/div[4]/'
                                                       'form/div[13]/div/div/div[2]/div/div/div/div/div[1]/div/div')
        ActionChains(self.browser).move_to_element(to_element=IPN_calc).perform()
        self.browser.find_element(By.XPATH, "//*[contains(.,'В строке 910.00.011 указывается сумма ИПН "
                                            "(КПН), подлежащего уплате в бюджет, определяемая по формуле: "
                                            "910.00.008 – 910.00.010')]")
        self.find_element(*self.locator.AFTER_BUTTON).click()

    def third_page_promt(self):
        self.hover(*self.locator.IPN_FIRST)
        self.browser.find_element(By.XPATH, "//*[contains(.,'В строках с 910.00.017 I по 910.00.017 VI указывается "
                                            "сумма ИПН, исчисленного с доходов граждан РК, выплаченных ФЛ, и "
                                            "подлежащего перечислению в бюджет за каждый месяц отчетного периода')]")
        self.browser.execute_script('window.scroll(0, 300)')
        total_ipn_to_pay = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[4]/div/div/div[4]/form'
                                                               '/div[1]/div[3]/div/div/div/div/div/div[2]/div[1]/div')
        ActionChains(self.browser).move_to_element(to_element=total_ipn_to_pay).perform()
        self.browser.find_element(By.XPATH, "//*[contains(.,'Строка 910.00.017 VII предназначена для отражения итоговой"
                                            " суммы ИПН, исчисленного с доходов граждан РК за полугодие, определяемая"
                                            " как сумма строк с 910.00.017 I по 910.00.017 VI')]")
        self.browser.execute_script('window.scroll(0, 650)')
        self.hover(*self.locator.IPN_SECOND)
        self.browser.find_element(By.XPATH, "//*[contains(.,'В строках с 910.00.018 I по 910.00.018 VI указывается"
                                            " сумма ИПН, исчисленного с доходов иностранцев и лиц без гражданства, "
                                            "выплаченных ФЛ, и подлежащего перечислению в бюджет за каждый месяц "
                                            "отчетного периода')]")
        ipn2_total = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[4]/div/div/div[4]/form/div'
                                                         '[3]/div[3]/div/div/div/div/div/div[2]/div[1]/div/div')
        ActionChains(self.browser).move_to_element(to_element=ipn2_total).perform()
        self.browser.find_element(By.XPATH, "//*[contains(.,'Строка 910.00.018 VII предназначена для отражения"
                                            " итоговой суммы ИПН, исчисленного с доходов иностранцев и лиц без "
                                            "гражданства за полугодие, определяемая как сумма строк с 910.00.018"
                                            " I по 910.00.018 VI')]")
        self.browser.execute_script('window.scroll(0, 1200)')
        self.hover(*self.locator.FL_INCOME)
        self.browser.find_element(By.XPATH, "//*[contains(.,'В строках с 910.00.019 I по 910.00.019 VI указывается "
                                            "сумма расходов работодателя, выплачиваемых ФЛ в виде доходов за налоговый"
                                            " период в соответствии с Законом об обязательном социальном страховании,"
                                            " за каждый месяц отчетного периода')]")
        self.browser.execute_script('window.scroll(0, 1600)')
        self.hover(*self.locator.FL_TOTAL_I)
        self.browser.find_element(By.XPATH, '//*[contains(.,"Строка 910.00.019 VII предназначена для отражения итогово'
                                            'й суммы доходов ФЛ, с которых исчисляются СО за полугодие, определяемая'
                                            ' как сумма строк с 910.00.019 I по 910.00.019 VI")]')
        self.hover(*self.locator.FL_TOTAL_II)
        self.browser.find_element(By.XPATH, '//*[contains(.,"Строка 910.00.020 VII предназначена для отражения итоговой'
                                            ' суммы СО за полугодие, определяемая как сумма строк с 910.00.020 I'
                                            ' по 910.00.020 VI")]')
        self.hover(*self.locator.OPV)
        self.browser.find_element(By.XPATH, '//*[text()=" указывается сумма доходов, начисленных ФЛ, с которых '
                                            'удерживаются (начисляются) ОПВ за каждый месяц отчетного периода."]')
        self.browser.execute_script('window.scroll(0, 2500)')
        self.hover(*self.locator.OPV_TOTAL_I)
        self.browser.find_element(By.XPATH, '//*[contains(.,"Строка 910.00.021 VII предназначена для отражения итоговой суммы доходов, начисленных ФЛ, с которых удерживаются (начисляются) ОПВ за полугодие, определяемая как сумма строк с 910.00.021 I по 910.00.021 VI")]')
        self.hover(*self.locator.OPV_TOTAL_II)
        self.browser.find_element(By.XPATH, '//*[contains(.,"Строка 910.00.022 VII предназначена для отражения итоговой'
                                            ' суммы ОПВ за полугодие, определяемая как сумма строк с 910.00.022 '
                                            'I по 910.00.022 VI")]')
        ''

    def sending_page_promt(self):
        sleep(1)
        self.hover(*self.locator.BIN_INPUT)
        self.browser.find_element(By.XPATH, "//*[contains(.,'По строке 910.00.028 указывается БИН аппарата акимов"
                                            " городов районного значения, сел, поселков, сельских округов "
                                            "по месту нахождения ИП, согласно справочнику МСУ')]")
