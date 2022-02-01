from locators.fno_400_locators import FNO_400_01Locators, FNO_400_02Locators, FNO_400_03Locators, FNO_400_04Locators \
    , FNO_400_05Locators, FNO_400_06Locators, FNO_400_07Locators, FNO_400_08Locators
from locators.main_page_locators import MainPageLocators
from browser_interaction import BasePage
from time import sleep
import allure


class FNO400Promt(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.locator = FNO_400_01Locators
        self.locator02 = FNO_400_02Locators
        self.locator03 = FNO_400_03Locators
        self.locator04 = FNO_400_04Locators
        self.locator05 = FNO_400_05Locators
        self.locator06 = FNO_400_06Locators
        self.locator07 = FNO_400_07Locators
        self.locator08 = FNO_400_08Locators
        self.main_locator = MainPageLocators

    def promt_check(self):
        sleep(1)
        self.hover(*self.main_locator.PROMT)
        self.find_element(*self.main_locator.PROMT_ACTIVATE).click()
        self.hover(*self.locator.DECLARATION_TYPE)
        sleep(0.2)
        #assert 'В строке 4 отмечается вид декларации, с учетом отнесения декларации к видам налоговой отчетности, ' \
        #       'указанным в статье 206 Налогового кодекса' in self.browser.page_source
        self.scroll('500')
        self.hover(*self.locator.TAXPAYER_CATEGORY)
        sleep(0.1)
        assert 'В строке 6 отмечается отдельная категория налогоплательщика в соответствии со статьей 40 Налогового ' \
               'кодекса' in self.browser.page_source
        self.hover(*self.locator.ANNEXES)
        sleep(0.1)
        assert 'Приложения к основной форме налоговой отчетности не представляются при отсутствии данных, подлежащих ' \
               'отражению в них (пункт 11 статьи 208 Налогового кодекса).' in self.browser.page_source
        self.find_element(*self.locator.ANNEXES).click()
        sleep(1)
        element = self.browser.find_element_by_xpath('//*[@title="Приложение 400.08  Облагаемые операции по '
                                                     'подакцизным товарам, предусмотренным подпунктом 6) статьи 462 '
                                                     'Налогового кодекса"]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        self.find_element(*self.locator.ANNEXES_SELECT_ALL).click()
        sleep(0.5)
        self.find_element(*self.locator.CONTROL_TEXT2).click()
        self.find_element(*self.locator.AFTER).click()
        # 1 приложение
        self.hover(*self.locator.PRODUCT_TYPE)
        sleep(0.1)
        assert 'В строке 400.01.001 А указывается вид продукции' in self.browser.page_source
        self.hover(*self.locator.QUALIFICATION_CODE)
        sleep(0.1)
        assert 'В строке 400.01.001 В указывается соответствующий код бюджетной классификации' in self.browser.page_source
        self.scroll('500')
        self.hover(*self.locator.BUT_1)
        sleep(0.1)
        assert 'В графе А указывается размер налоговой базы (литр)' in self.browser.page_source
        self.hover(*self.locator.BUT_2)
        sleep(0.1)
        assert 'В графе В указывается ставка акциза. Ставка акциза устанавливается в тенге на 1 литр' in self.browser.page_source

        self.hover(*self.locator.BUT_3)
        sleep(0.1)
        assert 'В графе А указывается размер налоговой базы (литр)' in self.browser.page_source
        self.hover(*self.locator.BUT_4)
        sleep(0.1)
        assert 'В графе В указывается ставка акциза. Ставка акциза устанавливается в тенге на 1 литр' in self.browser.page_source

        self.hover(*self.locator.BUT_5)
        sleep(0.1)
        assert 'В графе А указывается размер налоговой базы (литр)' in self.browser.page_source
        self.hover(*self.locator.BUT_6)
        sleep(0.1)
        assert 'В графе В указывается ставка акциза. Ставка акциза устанавливается в тенге на 1 литр' in self.browser.page_source

        self.hover(*self.locator.BUT_7)
        sleep(0.1)
        assert 'В графе А указывается размер налоговой базы (литр)' in self.browser.page_source
        self.hover(*self.locator.BUT_8)
        sleep(0.1)
        assert 'В графе В указывается ставка акциза. Ставка акциза устанавливается в тенге на 1 литр' in self.browser.page_source

        self.hover(*self.locator.BUT_9)
        sleep(0.1)
        assert 'В графе А указывается размер налоговой базы (литр)' in self.browser.page_source
        self.hover(*self.locator.BUT_10)
        sleep(0.1)
        assert 'В графе В указывается ставка акциза. Ставка акциза устанавливается в тенге на 1 литр' in self.browser.page_source

        self.hover(*self.locator.BUT_11)
        sleep(0.1)
        assert 'В графе А указывается размер налоговой базы (литр)' in self.browser.page_source
        self.hover(*self.locator.BUT_12)
        sleep(0.1)
        assert 'В графе В указывается ставка акциза. Ставка акциза устанавливается в тенге на 1 литр' in self.browser.page_source
        self.scroll('500')
        self.hover(*self.locator.BUT_13)
        sleep(0.1)
        assert 'В графе А указывается размер налоговой базы (литр)' in self.browser.page_source
        self.hover(*self.locator.BUT_14)
        sleep(0.1)
        assert 'В графе В указывается ставка акциза. Ставка акциза устанавливается в тенге на 1 литр' in self.browser.page_source

        self.hover(*self.locator.BUT_15)
        sleep(0.1)
        assert 'В графе А указывается размер налоговой базы (литр)' in self.browser.page_source
        self.hover(*self.locator.BUT_16)
        sleep(0.1)
        assert 'В графе В указывается ставка акциза. Ставка акциза устанавливается в тенге на 1 литр' in self.browser.page_source

        self.hover(*self.locator.BUT_17)
        sleep(0.1)
        assert 'В графе А указывается размер налоговой базы (литр)' in self.browser.page_source
        self.hover(*self.locator.BUT_18)
        sleep(0.1)
        assert 'В графе В указывается ставка акциза. Ставка акциза устанавливается в тенге на 1 литр' in self.browser.page_source

        self.hover(*self.locator.BUT_19)
        sleep(0.1)
        assert 'В графе А указывается размер налоговой базы (литр)' in self.browser.page_source
        self.hover(*self.locator.BUT_20)
        sleep(0.1)
        assert 'В графе В указывается ставка акциза. Ставка акциза устанавливается в тенге на 1 литр' in self.browser.page_source

        self.hover(*self.locator.BUT_21)
        sleep(0.1)
        assert 'В графе А указывается размер налоговой базы (литр)' in self.browser.page_source
        self.hover(*self.locator.BUT_22)
        sleep(0.1)
        assert 'В графе В указывается ставка акциза. Ставка акциза устанавливается в тенге на 1 литр' in self.browser.page_source

        self.hover(*self.locator.BUT_23)
        sleep(0.1)
        assert 'В графе А указывается размер налоговой базы (литр)' in self.browser.page_source
        self.hover(*self.locator.BUT_24)
        sleep(0.1)
        assert 'В графе В указывается ставка акциза. Ставка акциза устанавливается в тенге на 1 литр' in self.browser.page_source
        self.scroll('500')
        self.hover(*self.locator.BUT_25)
        sleep(0.1)
        assert 'В строке 400.01.014 отражаются суммы акциза, уплаченного поставщикам спирта и (или) виноматериала при ' \
               'приобретении для производства алкогольной продукции' in self.browser.page_source
        self.find_element(*self.locator.AFTER).click()

        # 2 ПРИЛОЖЕНИЕ
        self.hover(*self.locator02.ALC_TYPE)
        sleep(0.1)
        assert 'В строке 400.02.001 А указывается вид алкогольной продукции' in self.browser.page_source
        self.hover(*self.locator02.QUAL_CODE)
        sleep(0.1)
        assert 'В строке 400.02.001 В указывается соответствующий код бюджетной классификации' in self.browser.page_source
        self.scroll('500')
        self.hover(*self.locator02.OP1)
        sleep(0.1)
        assert 'В строке 400.02.002 указывается объем реализованной алкогольной продукции собственного производства' in self.browser.page_source
        self.hover(*self.locator02.OP2)
        sleep(0.1)
        assert 'В строке 400.02.003 указывается объем алкогольной продукции, переданный в качестве взноса в уставный ' \
               'капитал' in self.browser.page_source
        self.hover(*self.locator02.OP3)
        sleep(0.1)
        assert 'В строке 400.02.004 указывается объем алкогольной продукции, использованный при натуральной оплате' in self.browser.page_source
        self.hover(*self.locator02.OP4)
        sleep(0.1)
        assert 'В строке 400.02.005 указывается объем алкогольной продукции, отгруженный своим структурным ' \
               'подразделениям' in self.browser.page_source
        self.hover(*self.locator02.OP5)
        sleep(0.1)
        assert 'В строке 400.02.006 указывается объем алкогольной продукции, использованный для собственных ' \
               'производственных нужд налогоплательщика' in self.browser.page_source
        self.hover(*self.locator02.OP6)
        sleep(0.1)
        assert 'В строке 400.02.007 указывается объем реализованной конкурсной массы алкогольной продукции' in self.browser.page_source
        self.hover(*self.locator02.OP7)
        sleep(0.1)
        assert 'В строке 400.02.008 указывается объем перемещенной производителем с указанного в лицензии адреса ' \
               'производства алкогольной продукции' in self.browser.page_source
        self.hover(*self.locator02.OP8)
        sleep(0.1)
        assert 'В строке 400.02.009 указывается объем алкогольной продукции, в отношении которого установлен факт ' \
               'порчи или утраты' in self.browser.page_source
        sleep(0.2)
        self.scroll('500')
        self.hover(*self.locator02.KM1)
        sleep(0.1)
        assert 'В строке 400.02.010 I графы А указывается количество испорченных или утраченных учетно-контрольных ' \
               'марок' in self.browser.page_source
        self.hover(*self.locator02.ET1)
        sleep(0.1)
        assert 'В строке 400.02.010 I графы В указывается емкость потребительской тары' in self.browser.page_source
        self.hover(*self.locator02.KM2)
        sleep(0.1)
        assert 'В строке 400.02.010 II графы А указывается количество испорченных или утраченных учетно-контрольных ' \
               'марок' in self.browser.page_source
        self.hover(*self.locator02.ET2)
        sleep(0.1)
        assert 'В строке 400.02.010 II графы В указывается емкость потребительской тары' in self.browser.page_source
        self.hover(*self.locator02.KM3)
        sleep(0.1)
        assert 'В строке 400.02.010 III графы А указывается количество испорченных или утраченных учетно-контрольных ' \
               'марок' in self.browser.page_source
        self.hover(*self.locator02.ET3)
        sleep(0.1)
        assert 'В строке 400.02.010 III графы В указывается емкость потребительской тары' in self.browser.page_source
        self.hover(*self.locator02.EXCISE_RATE)
        sleep(0.1)
        assert 'В строке 400.02.012 указывается установленная ставка акциза' in self.browser.page_source
        self.scroll('500')
        self.find_element(*self.locator.AFTER).click()

        # 3 ПРИЛОЖЕНИЕ
        self.hover(*self.locator03.TOBACCO_TYPE)
        sleep(0.1)
        assert 'В строке 400.03.001 А указывается вид табачных изделий' in self.browser.page_source
        self.hover(*self.locator03.BUDGET_CODE)
        sleep(0.1)
        assert 'В строке 400.03.001 В указывается соответствующий код бюджетной классификации' in self.browser.page_source
        self.scroll('500')
        self.hover(*self.locator03.TOBACCO_TYPE)
        sleep(0.1)
        assert 'В строке 400.03.001 А указывается вид табачных изделий' in self.browser.page_source
        self.hover(*self.locator03.TOBACCO_OP1)
        sleep(0.1)
        assert 'В строке 400.03.002 указывается количество реализованных табачных изделий' in self.browser.page_source
        self.hover(*self.locator03.TOBACCO_OP2)
        sleep(0.1)
        assert 'В строке 400.03.003 указывается количество табачных изделий, переданных в качестве взноса в уставный ' \
               'капитал' in self.browser.page_source
        self.hover(*self.locator03.TOBACCO_OP3)
        sleep(0.1)
        assert 'В строке 400.03.004 указывается количество табачных изделий, использованных при натуральной оплате' in self.browser.page_source
        self.hover(*self.locator03.TOBACCO_OP4)
        sleep(0.1)
        assert 'В строке 400.03.005 указывается количество табачных изделий, отгруженных своим структурным ' \
               'подразделениям' in self.browser.page_source
        self.hover(*self.locator03.TOBACCO_OP5)
        sleep(0.1)
        assert 'В строке 400.03.006 указывается количество табачных изделий, использованных для собственных ' \
               'производственных нужд и для собственного производства подакцизных товаров' in self.browser.page_source
        self.hover(*self.locator03.TOBACCO_OP6)
        sleep(0.1)
        assert 'В строке 400.03.007 указывается количество реализованной конкурсной массы табачных изделий' in self.browser.page_source
        self.hover(*self.locator03.KAZ_REAL)
        sleep(0.1)
        assert 'В строке 400.03.008 А указывается количество табачных изделий, предназначенное для реализации на ' \
               'территории Республики Казахстан' in self.browser.page_source
        self.hover(*self.locator03.EXPORT_REAL)
        sleep(0.1)
        assert 'В строке 400.03.008 В указывается количество табачных изделий, предназначенное для реализации на ' \
               'экспорт' in self.browser.page_source
        self.hover(*self.locator03.TAX_CORRECT)
        sleep(0.1)
        assert 'В строке 400.03.009 указывается корректировка налоговой базы в соответствии с пунктом 2 статьи 290 ' \
               'Налогового Кодекса' in self.browser.page_source
        self.hover(*self.locator03.DAMAGED)
        sleep(0.1)
        assert 'В строке 400.03.010 указывается количество табачных изделий, в отношении которых установлен факт ' \
               'порчи или утраты' in self.browser.page_source
        self.scroll('500')
        self.hover(*self.locator03.AMOUNT1)
        sleep(0.1)
        assert 'В строке 400.03.011 I графы А указывается количество испорченных и утраченных акцизных марок' in self.browser.page_source
        self.hover(*self.locator03.AMOUNT2)
        sleep(0.1)
        assert 'В строке 400.03.011 I графы В указывается количество табачных изделий в штуках, килограммах в пачке' in self.browser.page_source
        self.hover(*self.locator03.AMOUNT3)
        sleep(0.1)
        assert 'В строке 400.03.011 II графы А указывается количество испорченных и утраченных акцизных марок приняты ' \
               'налоговыми органами в соответствии с пунктом 3 статьи 469 Налогового кодекса' in \
               self.browser.page_source
        self.hover(*self.locator03.AMOUNT4)
        sleep(0.1)
        assert 'В строке 400.03.011 II графы В указывается количество табачных изделий в штуках, килограммах в пачке ' \
               'приняты налоговыми органами в соответствии с пунктом 3 статьи 469 Налогового кодекса' in \
               self.browser.page_source
        self.scroll('500')
        self.hover(*self.locator03.EXCISE_RATE)
        sleep(0.1)
        assert 'В строке 400.03.013 указывается ставка акциза' in \
               self.browser.page_source
        self.hover(*self.locator03.EXCISE_SUM)
        sleep(0.1)
        assert 'В строке 400.03.015 указывается сумма акциза по испорченным акцизным маркам принятым налоговыми ' \
               'органами в соответствии с пунктом 3 статьи 469 Налогового кодекса' in \
               self.browser.page_source
        self.find_element(*self.locator.AFTER).click()

        # 4 ПРИЛОЖЕНИЕ
        self.hover(*self.locator04.OIL_REAL)
        sleep(0.1)
        assert 'В строке 400.04.001 указывается объем реализованной сырой нефти, газового конденсата, кроме сырой ' \
               'нефти, газового конденсата реализуемый на экспорт' in self.browser.page_source
        self.hover(*self.locator04.EXPORT_OIL1)
        sleep(0.1)
        assert 'В строке 400.04.002 А указывается объем сырой нефти, газового конденсата, реализуемые по экспорту в ' \
               'страны Евразийского экономического союза' in self.browser.page_source
        self.hover(*self.locator04.EXPORT_OIL2)
        sleep(0.1)
        assert 'В строке 400.04.002 В указывается объем сырой нефти, газового конденсата, реализуемые по экспорту в ' \
               'третьи страны' in self.browser.page_source
        self.scroll('500')
        self.hover(*self.locator04.USING1)
        sleep(0.1)
        assert 'В строке 400.04.003 указывается объем сырой нефти, газового конденсата, передаваемый на переработку ' \
               'на давальческой основе' in self.browser.page_source
        self.hover(*self.locator04.USING2)
        sleep(0.1)
        assert 'В строке 400.04.004 указывается объем сырой нефти, газового конденсата, использованный для ' \
               'собственных производственных нужд' in self.browser.page_source
        self.hover(*self.locator04.USING3)
        sleep(0.1)
        assert 'В строке 400.04.005 указывается объем сырой нефти, газового конденсата, переданный в качестве взноса ' \
               'в уставный капитал' in self.browser.page_source
        self.hover(*self.locator04.USING4)
        sleep(0.1)
        assert 'В строке 400.04.006 указывается объем сырой нефти, газового конденсата, использованный при ' \
               'натуральной оплате' in self.browser.page_source
        self.hover(*self.locator04.USING5)
        sleep(0.1)
        assert 'В строке 400.04.007 указывается объем сырой нефти, газового конденсата, отгруженный своим структурным ' \
               'подразделениям' in self.browser.page_source
        self.hover(*self.locator04.USING6)
        sleep(0.1)
        assert 'В строке 400.04.008 указывается объем реализованной конкурсной массы, конфискованный и (или) ' \
               'бесхозяйный, перешедший по праву наследования к государству и безвозмездно переданный в собственность ' \
               'государства сырой нефти, газового конденсата' in self.browser.page_source
        self.hover(*self.locator04.USING7)
        sleep(0.1)
        assert 'В строке 400.04.009 указывается перемещенный производителем с указанного в лицензии адреса ' \
               'производства объем сырой нефти, газового конденсата' in self.browser.page_source
        self.hover(*self.locator04.USING8)
        sleep(0.1)
        assert 'В строке 400.04.010 указывается объем сырой нефти, газового конденсата, в отношении которого ' \
               'установлен факт порчи или утраты' in self.browser.page_source
        self.scroll('500')
        self.hover(*self.locator04.TON_RATE)
        sleep(0.1)
        assert 'В строке 400.04.012 указывается установленная ставка акциза. Ставка акциза устанавливается в тенге на ' \
               '1 тонну.' in self.browser.page_source
        self.find_element(*self.locator.AFTER).click()

        # 5 ПРИЛОЖЕНИЕ
        self.scroll('500')
        self.hover(*self.locator05.OPT_1)
        sleep(0.1)
        assert 'В графе 400.05.001 I А указывается размер налоговой базы по облагаемой операции в тоннах по оптовой ' \
               'реализации бензина, собственного производства' in self.browser.page_source
        self.hover(*self.locator05.OPT_2)
        sleep(0.1)
        assert 'В графе 400.05.001 I B указывается ставка акциза по оптовой реализации бензина, собственного ' \
               'производства' in self.browser.page_source
        self.hover(*self.locator05.OPT_3)
        sleep(0.1)
        assert 'В графе 400.05.001 II А указывается размер налоговой базы по облагаемой операции в тоннах по оптовой ' \
               'реализации бензина, приобретенного в РК или по импорту' in self.browser.page_source
        self.hover(*self.locator05.OPT_4)
        sleep(0.1)
        assert 'В графе 400.05.001 II В указывается ставка акциза по оптовой реализации бензина, приобретенного в РК ' \
               'или по импорту' in self.browser.page_source
        self.hover(*self.locator05.OPT_5)
        sleep(0.1)
        assert 'В графе 400.05.001 III А указывается размер налоговой базы по облагаемой операции в тоннах по ' \
               'отгрузке бензина собственного производства структурным подразделениям для дальнейшей реализации' in \
               self.browser.page_source
        self.hover(*self.locator05.OPT_6)
        sleep(0.1)
        assert 'В графе 400.05.001 III В указывается ставка акциза по отгрузке бензина собственного производства ' \
               'структурным подразделениям для дальнейшей реализации' in self.browser.page_source
        self.hover(*self.locator05.OPT_7)
        sleep(0.1)
        assert 'В графе 400.05.001 IV А указывается размер налоговой базы по облагаемой операции в тоннах по оптовой ' \
               'реализации конкурсной массы, конфискованного и (или) бесхозяйного, перешедшего по праву наследования ' \
               'к государству и безвозмездно переданного в собственность государства' in self.browser.page_source
        self.hover(*self.locator05.OPT_8)
        sleep(0.1)
        assert 'В графе 400.05.001 IV В указывается ставка акциза по оптовой реализации конкурсной массы, ' \
               'конфискованного и (или) бесхозяйного, перешедшего по праву наследования к государству и безвозмездно ' \
               'переданного в собственность государства' in self.browser.page_source
        self.scroll('700')
        self.hover(*self.locator05.OPT_9)
        sleep(0.1)
        assert 'В графе 400.05.001 V А указывается размер налоговой базы по перемещению бензина, осуществляемое ' \
               'производителем с адреса производства в тоннах' in self.browser.page_source
        self.hover(*self.locator05.OPT_10)
        sleep(0.1)
        assert 'В графе 400.05.001 V В указывается ставка акциза по перемещению бензина, осуществляемое ' \
               'производителем с адреса производства' in self.browser.page_source
        self.scroll('300')
        self.hover(*self.locator05.ROZN_1)
        sleep(0.1)
        assert 'В графе 400.05.002 I А указывается размер налоговой базы по розничной реализации бензина собственного ' \
               'производства в тоннах' in self.browser.page_source
        self.hover(*self.locator05.ROZN_2)
        sleep(0.1)
        assert 'В графе 400.05.002 I В указывается ставка акциза по розничной реализации бензина собственного ' \
               'производства' in self.browser.page_source
        self.hover(*self.locator05.ROZN_3)
        sleep(0.1)
        assert 'В графе 400.05.002 II А указывается размер налоговой базы по розничной реализации бензина, ' \
               'приобретенного в РК или по импорту в тоннах' in self.browser.page_source
        self.hover(*self.locator05.ROZN_4)
        sleep(0.1)
        assert 'В графе 400.05.002 II В указывается ставка акциза по розничной реализации бензина, приобретенного в ' \
               'РК или по импорту' in self.browser.page_source
        self.hover(*self.locator05.ROZN_5)
        sleep(0.1)
        assert 'В графе 400.05.002 III А указывается размер налоговой базы по взносу в уставный капитал в тоннах' in self.browser.page_source
        self.hover(*self.locator05.ROZN_6)
        sleep(0.1)
        assert 'В графе 400.05.002 III В указывается ставка акциза по взносу в уставный капитал' in self.browser.page_source
        self.hover(*self.locator05.ROZN_7)
        sleep(0.1)
        assert 'В графе 400.05.002 IV А указывается размер налоговой базы по розничной реализации конкурсной массы, ' \
               'конфискованного и (или) бесхозяйного, перешедшего по праву наследования к государству и безвозмездно ' \
               'переданного в собственность государства в тоннах' in self.browser.page_source
        self.hover(*self.locator05.ROZN_8)
        sleep(0.1)
        assert 'В графе 400.05.002 IV В указывается ставка акциза по розничной реализации конкурсной массы, ' \
               'конфискованного и (или) бесхозяйного, перешедшего по праву наследования к государству и безвозмездно ' \
               'переданного в собственность государства' in self.browser.page_source
        self.scroll('700')
        self.hover(*self.locator05.ROZN_9)
        sleep(0.1)
        assert 'В графе 400.05.002 V А указывается размер налоговой базы по порче, утрате в тоннах' in self.browser.page_source
        self.hover(*self.locator05.ROZN_10)
        sleep(0.1)
        assert 'В графе 400.05.002 V В указывается ставка акциза по порче, утрате' in self.browser.page_source
        self.hover(*self.locator05.ROZN_11)
        sleep(0.1)
        assert 'В графе 400.05.002 VI А указывается размер налоговой базы по использованию бензина собственного ' \
               'производства на собственные производственные нужды в тоннах' in self.browser.page_source
        self.hover(*self.locator05.ROZN_12)
        sleep(0.1)
        assert 'В графе 400.05.002 VI В указывается ставка акциза по использованию бензина собственного производства ' \
               'на собственные производственные нужды' in self.browser.page_source
        self.hover(*self.locator05.ROZN_13)
        sleep(0.1)
        assert 'В графе 400.05.002 VII А указывается размер налоговой базы по использованию на собственные ' \
               'производственные нужды бензина, приобретенного для дальнейшей реализации на территории РК в тоннах' \
               in self.browser.page_source
        self.hover(*self.locator05.ROZN_14)
        sleep(0.1)
        assert 'В графе 400.05.002 VII В указывается ставка акциза по использованию на собственные производственные ' \
               'нужды бензина, приобретенного для дальнейшей реализации на территории РК ' in self.browser.page_source
        self.scroll('800')
        self.hover(*self.locator05.DOPT_1)
        sleep(0.1)
        assert 'В графе 400.05.004 I А указывается размер налоговой базы по в тоннах' in self.browser.page_source
        self.hover(*self.locator05.DOPT_2)
        sleep(0.1)
        assert 'В графе 400.05.004 I VII В указывается ставка акциза по оптовой реализации дизельного топлива, ' \
               'собственного производства' in self.browser.page_source
        self.hover(*self.locator05.DOPT_3)
        sleep(0.1)
        assert 'В графе 400.05.004 II А указывается размер налоговой базы по оптовой реализации дизельного топлива ' \
               'импортированного или приобретенного в РК в тоннах' in self.browser.page_source
        self.hover(*self.locator05.DOPT_4)
        sleep(0.1)
        assert 'В графе 400.05.004 II В указывается ставка акциза по оптовой реализации дизельного топлива ' \
               'импортированного или приобретенного в РК' in self.browser.page_source
        self.hover(*self.locator05.DOPT_5)
        sleep(0.1)
        assert 'В графе 400.05.004 III А указывается размер налоговой базы по отгрузке дизельного топлива ' \
               'собственного производства структурным подразделениям для дальнейшей реализации в тоннах' in \
               self.browser.page_source
        self.hover(*self.locator05.DOPT_6)
        sleep(0.1)
        assert 'В графе 400.05.004 III В указывается ставка акциза по отгрузке дизельного топлива собственного ' \
               'производства структурным подразделениям для дальнейшей реализации' in self.browser.page_source
        self.hover(*self.locator05.DOPT_7)
        sleep(0.1)
        assert 'В графе 400.05.004 IV А указывается размер налоговой базы по оптовой реализации конкурсной массы, ' \
               'конфискованного и (или) бесхозяйного, перешедшего по праву наследования к государству и безвозмездно ' \
               'переданного в собственность государства в тоннах' in self.browser.page_source
        self.hover(*self.locator05.DOPT_8)
        sleep(0.1)
        assert 'В графе 400.05.004 IV В указывается ставка акциза по оптовой реализации конкурсной массы, ' \
               'конфискованного и (или) бесхозяйного, перешедшего по праву наследования к государству и безвозмездно ' \
               'переданного в собственность государства' in self.browser.page_source
        self.scroll('700')
        self.hover(*self.locator05.DOPT_9)
        sleep(0.1)
        assert 'В графе 400.05.004 V А указывается размер налоговой базы по перемещению дизельного топлива, ' \
               'осуществляемое производителем с  адреса производства в тоннах' in self.browser.page_source
        self.hover(*self.locator05.DOPT_10)
        sleep(0.1)
        assert 'В графе 400.05.004 V В указывается ставка акциза по перемещению дизельного топлива, осуществляемое ' \
               'производителем с  адреса производства' in self.browser.page_source
        self.hover(*self.locator05.DROZ_1)
        sleep(0.1)
        assert 'В графе 400.05.005 I  А указывается размер налоговой базы по розничной реализации дизельного топлива ' \
               'собственного производства в тоннах' in self.browser.page_source
        self.hover(*self.locator05.DROZ_2)
        sleep(0.1)
        assert 'В графе 400.05.005 I В указывается ставка акциза по розничной реализации дизельного топлива ' \
               'собственного производства' in self.browser.page_source
        self.hover(*self.locator05.DROZ_3)
        sleep(0.1)
        assert 'В графе 400.05.005 II А указывается размер налоговой базы по розничной реализации дизельного топлива, ' \
               'импортированного или приобретенного в РК в тоннах' in self.browser.page_source
        self.hover(*self.locator05.DROZ_4)
        sleep(0.1)
        assert 'В графе 400.05.005 II В указывается ставка акциза по розничной реализации дизельного топлива, ' \
               'импортированного или приобретенного в РК' in self.browser.page_source
        self.scroll('600')
        self.hover(*self.locator05.DROZ_5)
        sleep(0.1)
        assert 'В графе 400.05.005 III А указывается размер налоговой базы по взносу в уставный капитал в тоннах' in self.browser.page_source
        self.hover(*self.locator05.DROZ_6)
        sleep(0.1)
        assert 'В графе 400.05.005 III В указывается ставка акциза по взносу в уставный капитал' in self.browser.page_source
        self.hover(*self.locator05.DROZ_7)
        sleep(0.1)
        assert 'В графе 400.05.005 IV А указывается размер налоговой базы по розничной реализации конкурсной массы, ' \
               'конфискованного и (или) бесхозяйного, перешедшего по праву наследования к государству и безвозмездно ' \
               'переданного в собственность государства  в тоннах' in self.browser.page_source
        self.hover(*self.locator05.DROZ_8)
        sleep(0.1)
        assert 'В графе 400.05.005 IV В указывается ставка акциза по розничной реализации конкурсной массы, ' \
               'конфискованного и (или) бесхозяйного, перешедшего по праву наследования к государству и безвозмездно ' \
               'переданного в собственность государства ' in self.browser.page_source
        self.hover(*self.locator05.DROZ_9)
        sleep(0.1)
        assert 'В графе 400.05.005 V А указывается размер налоговой базы по порче, утрате в тоннах' in self.browser.page_source
        self.hover(*self.locator05.DROZ_10)
        sleep(0.1)
        assert 'В графе 400.05.005 V В указывается ставка акциза по порче, утрате' in self.browser.page_source
        self.hover(*self.locator05.DROZ_11)
        sleep(0.1)
        assert 'В графе 400.05.005 VI А указывается размер налоговой базы по использованию дизельного топлива ' \
               'собственного производства на собственные производственные нужды в тоннах' in self.browser.page_source
        self.hover(*self.locator05.DROZ_12)
        sleep(0.1)
        assert 'В графе 400.05.005 VI В указывается ставка акциза по использованию дизельного топлива собственного ' \
               'производства на собственные производственные нужды' in self.browser.page_source
        self.scroll('200')
        self.hover(*self.locator05.DROZ_13)
        sleep(0.1)
        assert 'В графе 400.05.005 VII А указывается размер налоговой базы по использованию на собственные ' \
               'производственные нужды дизельного топлива, приобретенного для дальнейшей реализации на территории РК ' \
               'в тоннах' in self.browser.page_source
        self.hover(*self.locator05.DROZ_14)
        sleep(0.1)
        assert 'В графе 400.05.005 VII В указывается ставка акциза по использованию на собственные производственные ' \
               'нужды дизельного топлива, приобретенного для дальнейшей реализации на территории РК' in \
               self.browser.page_source
        self.scroll('800')
        self.hover(*self.locator05.EXC_PAY1)
        sleep(0.1)
        assert 'В графе А указывается код бюджетной классификации. Одному коду бюджетной классификации соответствует ' \
               'одна строка' in \
               self.browser.page_source
        self.hover(*self.locator05.EXC_PAY2)
        sleep(0.1)
        assert 'в графе В указывается сумма исчисленного акциза за отчетный месяц' in \
               self.browser.page_source
        self.scroll('2000')
        self.find_element(*self.locator.AFTER).click()

        # 6 ПРИЛОЖЕНИЕ
        self.scroll('500')
        self.find_element(*self.locator06.ADD_STR).click()
        self.hover(*self.locator06.QUAL_CODE)
        sleep(0.1)
        assert 'В графе В указывается код бюджетной классификации' in self.browser.page_source
        self.hover(*self.locator06.USED_MATERIALS)
        sleep(0.1)
        assert 'В графе С указывается объем использованного сырья на производство подакцизного товара в отчетном ' \
               'налоговом периоде. Объем использованного сырья подакцизного товара определяется в соответствии с ' \
               'налоговой базой' in self.browser.page_source
        self.hover(*self.locator06.EXCISE_RATE)
        sleep(0.1)
        assert 'В графе D указывается ставка акциза' in self.browser.page_source
        self.hover(*self.locator06.DEDUCTION_AMOUNT)
        sleep(0.1)
        assert 'В графе Е указывается сумма акциза, подлежащая вычету' in self.browser.page_source
        self.find_element(*self.locator06.CANCEL_ADD_STR).click()
        self.scroll('500')
        self.find_element(*self.locator.AFTER).click()
        # 7 ПРИЛОЖЕНИЕ
        self.scroll('500')
        self.hover(*self.locator07.EXCISE_NO1)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO2)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO3)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO4)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO5)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO6)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO7)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO8)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.scroll('700')
        self.hover(*self.locator07.EXCISE_NO9)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO10)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO11)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO12)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO13)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO14)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO15)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO16)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.scroll('800')
        self.hover(*self.locator07.EXCISE_NO17)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO18)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO19)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO20)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO21)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO22)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO23)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO24)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.scroll('850')
        self.hover(*self.locator07.EXCISE_NO25)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.EXCISE_NO26)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.ALC_1)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.ALC_2)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.ALC_3)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.hover(*self.locator07.ALC_4)
        sleep(0.1)
        assert '' in self.browser.page_source
        self.find_element(*self.locator.AFTER).click()
        # 8 ПРИЛОЖЕНИЕ
        self.scroll('300')
        self.hover(*self.locator08.OPER1)
        sleep(0.1)
        assert 'В строке 400.08.001 указывается количество реализованных подакцизных товаров' in self.browser.page_source
        self.hover(*self.locator08.OPER2)
        sleep(0.1)
        assert 'В строке 400.08.002 указывается количество подакцизных товаров, переданных в качестве взноса в ' \
               'уставный капитал' in self.browser.page_source
        self.hover(*self.locator08.OPER3)
        sleep(0.1)
        assert 'В строке 400.08.003 указывается количество подакцизных товаров, использованных при натуральной оплате' in self.browser.page_source
        self.hover(*self.locator08.OPER4)
        sleep(0.1)
        assert 'В строке 400.08.004 указывается количество подакцизных товаров, отгруженных своим структурным ' \
               'подразделениям' in self.browser.page_source
        self.hover(*self.locator08.OPER5)
        sleep(0.1)
        assert 'В строке 400.08.005 указывается количество подакцизных товаров, использованных для собственных ' \
               'производственных нужд плательщика' in self.browser.page_source
        self.hover(*self.locator08.OPER6)
        sleep(0.1)
        assert 'В строке 400.08.006 указывается количество реализованной конкурсной массы, конфискованных и (или) ' \
               'бесхозяйных, перешедших по праву наследования к государству и безвозмездно переданных в собственность ' \
               'государства подакцизных товаров' in self.browser.page_source
        self.hover(*self.locator08.OPER7)
        sleep(0.1)
        assert 'В строке 400.08.007 указывается количество перемещенных  производителем подакцизных товаров с ' \
               'указанного в лицензии адреса производства' in self.browser.page_source
        self.hover(*self.locator08.OPER8)
        sleep(0.1)
        assert 'В строке 400.08.008 указывается количество подакцизных товаров собственного производства, в отношении ' \
               'которых установлен факт порчи или утраты' in self.browser.page_source
        self.scroll('500')
        self.hover(*self.locator08.OPER10)
        sleep(0.1)
        assert 'В строке 400.08.010 указывается ставка акциза за 1 кубический сантиметр объема двигателя' in self.browser.page_source
        self.find_element(*self.locator.AFTER).click()