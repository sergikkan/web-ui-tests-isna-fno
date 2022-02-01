
from selenium.webdriver.common.by import By

class FNO200LocatorsName(object):
    FIRST_PAGE_I_MONTH = 'Общая численность работников (человек): 1 месяц'
    FIRST_PAGE_II_MONTH = 'Общая численность работников (человек): 2 месяц'
    FIRST_PAGE_III_MONTH = 'Общая численность работников (человек): 3 месяц'
    FIRST_PAGE_IV_MONTH = 'В том числе иностранцев и лиц без гражданства 1 месяц'
    FIRST_PAGE_V_MONTH = 'В том числе иностранцев и лиц без гражданства 2 месяц'
    FIRST_PAGE_VI_MONTH = 'В том числе иностранцев и лиц без гражданства 3 месяц'
    APP_1_FIELD_1_I_MONTH = '200.01.001 Начисленные доходы: 1 месяц'
    APP_1_FIELD_1_II_MONTH = '200.01.001 Начисленные доходы: 2 месяц'
    APP_1_FIELD_1_III_MONTH = '200.01.001 Начисленные доходы: 3 месяц'
    APP_1_FIELD_1_A = 'в том числе за отчетный квартал A'
    APP_1_FIELD_1_B = 'в том числе за отчетный квартал B'
    APP_1_FIELD_1_C = 'в том числе за отчетный квартал C'
    APP_1_FIELD_1_D = 'в том числе за отчетный квартал D'
    APP_1_FIELD_1_E = 'в том числе за отчетный квартал E'
    APP_1_FIELD_3_I_MONTH = '200.01.003 Сумма индивидуального подоходного налога, исчисленного с начисленных доходов ' \
                            '1 месяц '
    APP_1_FIELD_3_II_MONTH = '200.01.003 Сумма индивидуального подоходного налога, исчисленного с начисленных доходов ' \
                             '2 месяц '
    APP_1_FIELD_3_III_MONTH = '200.01.003 Сумма индивидуального подоходного налога, исчисленного с начисленных ' \
                              'доходов 3 месяц '
    APP_1_FIELD_4 = '200.01.004 Задолженность по доходам, невыплаченным физическим лицам'
    APP_1_FIELD_5 = '200.01.005 Индивидуальный подоходный налог по доходам, начисленным, но не выплаченным на начало ' \
                    'отчетного квартала '
    APP_1_FIELD_6 = '200.01.006 Индивидуальный подоходный налог по доходам, начисленным, но не выплаченным на конец ' \
                    'отчетного квартала '
    APP_1_FIELD_7_I_MONTH = '200.01.007 Выплачено доходов 1 месяц'
    APP_1_FIELD_7_II_MONTH = '200.01.007 Выплачено доходов 2 месяц'
    APP_1_FIELD_7_III_MONTH = '200.01.007 Выплачено доходов 3 месяц'
    APP_1_FIELD_8_I_MONTH = '200.01.008 Облагаемый доходов 1 месяц'
    APP_1_FIELD_8_II_MONTH = '200.01.008 Облагаемый доходов 2 месяц'
    APP_1_FIELD_8_III_MONTH = '200.01.008 Облагаемый доходов 3 месяц'
    APP_1_FIELD_9_I_MONTH = '200.01.009 Начисленные доходы, с которых удерживаются (начисляются) обязательные ' \
                            'пенсионные взносы 1 месяц '
    APP_1_FIELD_9_II_MONTH = '200.01.009 Начисленные доходы, с которых удерживаются (начисляются) обязательные ' \
                             'пенсионные взносы 2 месяц '
    APP_1_FIELD_9_III_MONTH = '200.01.009 Начисленные доходы, с которых удерживаются (начисляются) обязательные ' \
                              'пенсионные взносы 3 месяц '
    APP_1_FIELD_10_I_MONTH = '200.01.010 Начисленные доходы с которых исчисляются (начисляются) обязательные ' \
                             'профессиональные пенсионные взносы 1 месяц '
    APP_1_FIELD_10_II_MONTH = '200.01.010 Начисленные доходы с которых исчисляются (начисляются) обязательные ' \
                              'профессиональные пенсионные взносы 2 месяц '
    APP_1_FIELD_10_III_MONTH = '200.01.010 Начисленные доходы с которых исчисляются (начисляются) обязательные ' \
                               'профессиональные пенсионные взносы 3 месяц '
    APP_1_FIELD_11_I_MONTH = '200.01.011 Начисленные доходы с которых исчисляются (начисляются) обязательные ' \
                             'пенсионные взносы работодателя 1 месяц '
    APP_1_FIELD_11_II_MONTH = '200.01.011 Начисленные доходы с которых исчисляются (начисляются) обязательные ' \
                              'пенсионные взносы работодателя 2 месяц '
    APP_1_FIELD_11_III_MONTH = '200.01.011 Начисленные доходы с которых исчисляются (начисляются) обязательные ' \
                               'пенсионные взносы работодателя 3 месяц '
    APP_1_FIELD_12_I_MONTH = '200.01.012 Заявляемый доход в свою пользу 1 месяц'
    APP_1_FIELD_12_II_MONTH = '200.01.012 Заявляемый доход в свою пользу 2 месяц'
    APP_1_FIELD_12_III_MONTH = '200.01.012 Заявляемый доход в свою пользу 3 месяц'
    APP_1_FIELD_13_I_MONTH = '200.01.013 Численность работников – инвалидов 1 месяц'
    APP_1_FIELD_13_II_MONTH = '200.01.013 Численность работников – инвалидов 2 месяц'
    APP_1_FIELD_13_III_MONTH = '200.01.013 Численность работников – инвалидов 3 месяц'
    APP_1_FIELD_14_I_MONTH = '200.01.014 Удельный вес численности работников – инвалидов в общей численности ' \
                             'работников 1 месяц '
    APP_1_FIELD_14_II_MONTH = '200.01.014 Удельный вес численности работников – инвалидов в общей численности ' \
                              'работников 2 месяц '
    APP_1_FIELD_14_III_MONTH = '200.01.014 Удельный вес численности работников – инвалидов в общей численности ' \
                               'работников 3 месяц '
    APP_1_FIELD_15_I_MONTH = '200.01.015 Удельный вес расходов по оплате труда работников – инвалидов в общих ' \
                             'расходах по оплате труда 1 месяц '
    APP_1_FIELD_15_II_MONTH = '200.01.015 Удельный вес расходов по оплате труда работников – инвалидов в общих ' \
                              'расходах по оплате труда 2 месяц '
    APP_1_FIELD_15_III_MONTH = '200.01.015 Удельный вес расходов по оплате труда работников – инвалидов в общих ' \
                               'расходах по оплате труда 3 месяц '
    APP_1_FIELD_16_I_MONTH = '200.01.016 Доходы работника, облагаемые социальным налогом 1 месяц'
    APP_1_FIELD_16_II_MONTH = '200.01.016 Доходы работника, облагаемые социальным налогом 2 месяц'
    APP_1_FIELD_16_III_MONTH = '200.01.016 Доходы работника, облагаемые социальным налогом 3 месяц'
    APP_1_FIELD_17_I_MONTH = '200.01.017 Доходы физических лиц, с которых исчисляются социальные отчисления 1 месяц'
    APP_1_FIELD_17_II_MONTH = '200.01.017 Доходы физических лиц, с которых исчисляются социальные отчисления 2 месяц'
    APP_1_FIELD_17_III_MONTH = '200.01.017 Доходы физических лиц, с которых исчисляются социальные отчисления 3 месяц'
    APP_1_FIELD_18_I_MONTH = '200.01.018 Доход, с которого исчисляются социальные отчисления в свою пользу 1 месяц'
    APP_1_FIELD_18_II_MONTH = '200.01.018 Доход, с которого исчисляются социальные отчисления в свою пользу 2 месяц'
    APP_1_FIELD_18_III_MONTH = '200.01.018 Доход, с которого исчисляются социальные отчисления в свою пользу 3 месяц'
    APP_1_FIELD_19_I_MONTH = '200.01.019 Доход, с которого исчисляются отчисления на обязательное социальное ' \
                             'медицинское страхование 1 месяц '
    APP_1_FIELD_19_II_MONTH = '200.01.019 Доход, с которого исчисляются отчисления на обязательное социальное ' \
                              'медицинское страхование 2 месяц '
    APP_1_FIELD_19_III_MONTH = '200.01.019 Доход, с которого исчисляются отчисления на обязательное социальное ' \
                               'медицинское страхование 3 месяц '
    APP_1_FIELD_20_I_MONTH = '200.01.020 Доход, с которого исчисляются взносы на обязательное социальное медицинское ' \
                             'страхование 1 месяц '
    APP_1_FIELD_20_II_MONTH = '200.01.020 Доход, с которого исчисляются взносы на обязательное социальное медицинское ' \
                              'страхование 2 месяц '
    APP_1_FIELD_20_III_MONTH = '200.01.020 Доход, с которого исчисляются взносы на обязательное социальное ' \
                               'медицинское страхование 3 месяц '

    SECOND_APP_C = 'Второе приложение, поле C'
    SECOND_APP_F = 'Второе приложение, поле F'
    SECOND_APP_G2 = 'Второе приложение, поле G2'
    SECOND_APP_N = 'Второе приложение, поле N'
    SECOND_APP_O = 'Второе приложение, поле O'
    SECOND_APP_P = 'Второе приложение, поле P'
    SECOND_APP_Q = 'Второе приложение, поле Q'
    SECOND_APP_R = 'Второе приложение, поле R'
    SECOND_APP_S = 'Второе приложение, поле S'
    SECOND_APP_T = 'Второе приложение, поле T'
    SECOND_APP_U = 'Второе приложение, поле U'
    SECOND_APP_V = 'Второе приложение, поле V'
    SECOND_APP_W = 'Второе приложение, поле W'
    SECOND_APP_X = 'Второе приложение, поле X'
    SECOND_APP_Y = 'Второе приложение, поле Y'
    SECOND_APP_Z = 'Второе приложение, поле Z'
    SECOND_APP_AA = 'Второе приложение, поле AA'
    SECOND_APP_AC = 'Второе приложение, поле AC'
    SECOND_APP_AD = 'Второе приложение, поле AD'
    SECOND_APP_AE = 'Второе приложение, поле AE'
    SECOND_APP_AF = 'Второе приложение, поле AF'
    SECOND_APP_AG = 'Второе приложение, поле AG'
    SECOND_APP_AI = 'Второе приложение, поле AI'
    BIN = 'БИН филиала/представительства'
    NAME_OF_FILIAL = 'Наименование филиала/представительства'
    WORKERS_1 = 'Общая численность работников (человек) 1 месяц'
    WORKERS_2 = 'Общая численность работников (человек) 2 месяц'
    WORKERS_3 = 'Общая численность работников (человек) 3 месяц'
    THIRD_APP_1_I_MONTH = '200.03.001 1 месяц'
    THIRD_APP_1_II_MONTH = '200.03.001 2 месяц'
    THIRD_APP_1_III_MONTH = '200.03.001 3 месяц'
    THIRD_APP_2_I_MONTH = '200.03.002 1 месяц'
    THIRD_APP_2_II_MONTH = '200.03.002 2 месяц'
    THIRD_APP_2_III_MONTH = '200.03.002 3 месяц'
    THIRD_APP_3_I_MONTH = '200.03.003 1 месяц'
    THIRD_APP_3_II_MONTH = '200.03.003 2 месяц'
    THIRD_APP_3_III_MONTH = '200.03.003 3 месяц'
    THIRD_APP_4_I_MONTH = '200.03.004 1 месяц'
    THIRD_APP_4_II_MONTH = '200.03.004 2 месяц'
    THIRD_APP_4_III_MONTH = '200.03.004 3 месяц'
    THIRD_APP_5_I_MONTH = '200.03.005 1 месяц'
    THIRD_APP_5_II_MONTH = '200.03.005 2 месяц'
    THIRD_APP_5_III_MONTH = '200.03.005 3 месяц'
    THIRD_APP_6_I_MONTH = '200.03.006 1 месяц'
    THIRD_APP_6_II_MONTH = '200.03.006 2 месяц'
    THIRD_APP_6_III_MONTH = '200.03.006 3 месяц'
    THIRD_APP_7_I_MONTH = '200.03.007 1 месяц'
    THIRD_APP_7_II_MONTH = '200.03.007 2 месяц'
    THIRD_APP_7_III_MONTH = '200.03.007 3 месяц'
    THIRD_APP_8_I_MONTH = '200.03.008 1 месяц'
    THIRD_APP_8_II_MONTH = '200.03.008 2 месяц'
    THIRD_APP_8_III_MONTH = '200.03.008 3 месяц'
    # 4 приложение
    NUMBER_OF_CONTRACT = '№ контракта'
    EMPLOYEES_NUMBER_1_I = 'Общая численность работников 1 месяц'
    EMPLOYEES_NUMBER_1_II = 'Общая численность работников 2 месяц'
    EMPLOYEES_NUMBER_1_III = 'Общая численность работников 3 месяц'
    EMPLOYEES_NUMBER_2_I = 'в том числе работников-иностранных специалистов 1 месяц'
    EMPLOYEES_NUMBER_2_II = 'в том числе работников-иностранных специалистов 2 месяц'
    EMPLOYEES_NUMBER_2_III = 'в том числе работников-иностранных специалистов 3 месяц'
    EMPLOYEES_NUMBER_3_I = 'работников-иностранных рабочих 1 месяц'
    EMPLOYEES_NUMBER_3_II = 'работников-иностранных рабочих 2 месяц'
    EMPLOYEES_NUMBER_3_III = 'работников-иностранных рабочих 3 месяц'
    EMPLOYEES_NUMBER_4_I = '200.04.001 Доходы работников, за исключением доходов работников иностранных специалистов ' \
                           'и иностранных рабочих, облагаемые социальным налогом 1 месяц '
    EMPLOYEES_NUMBER_4_II = '200.04.001 Доходы работников, за исключением доходов работников иностранных специалистов ' \
                            'и иностранных рабочих, облагаемые социальным налогом 2 месяц '
    EMPLOYEES_NUMBER_4_III = '200.04.001 Доходы работников, за исключением доходов работников иностранных ' \
                             'специалистов и иностранных рабочих, облагаемые социальным налогом 3 месяц '
    TAX_PERCENT_1 = '200.04.002 Ставка налога, % 1 месяц'
    TAX_PERCENT_2 = '200.04.002 Ставка налога, % 2 месяц'
    TAX_PERCENT_3 = '200.04.002 Ставка налога, % 3 месяц'
    # 5 приложение
    FIFTH_APP_C = 'Приложение 5, поле C'
    FIFTH_APP_B = 'Приложение 5, поле B'
    FIFTH_APP_G = 'Приложение 5, поле G'
    FIFTH_APP_H = 'Приложение 5, поле H'
    FIFTH_APP_I = 'Приложение 5, поле I'
    FIFTH_APP_J = 'Приложение 5, поле J'
    FIFTH_APP_K = 'Приложение 5, поле K'
    FIFTH_APP_L = 'Приложение 5, поле L'
    FIFTH_APP_M = 'Приложение 5, поле M'
    FIFTH_APP_N = 'Приложение 5, поле N'
    FIFTH_APP_O = 'Приложение 5, поле O'
    FIFTH_APP_P = 'Приложение 5, поле P'
    FIFTH_APP_Q = 'Приложение 5, поле Q'
    FIFTH_APP_R = 'Приложение 5, поле R'
    FIFTH_APP_S = 'Приложение 5, поле S'
    FIFTH_APP_T = 'Приложение 5, поле T'
    FIFTH_APP_U = 'Приложение 5, поле U'
    # 7 СТРАНИЦА
    SEVENTH_PAGE_1_I = '200.00.001 1 месяц'
    SEVENTH_PAGE_1_II = '200.00.001 2 месяц'
    SEVENTH_PAGE_1_III = '200.00.001 3 месяц'
    SEVENTH_PAGE_2_I = '200.00.002 1 месяц'
    SEVENTH_PAGE_2_II = '200.00.002 2 месяц'
    SEVENTH_PAGE_2_III = '200.00.002 3 месяц'
    SEVENTH_PAGE_3_I = '200.00.003 1 месяц'
    SEVENTH_PAGE_3_II = '200.00.003 2 месяц'
    SEVENTH_PAGE_3_III = '200.00.003 3 месяц'
    SEVENTH_PAGE_4_I = '200.00.004 1 месяц'
    SEVENTH_PAGE_4_II = '200.00.004 2 месяц'
    SEVENTH_PAGE_4_III = '200.00.004 3 месяц'
    SEVENTH_PAGE_5_I = '200.00.005 1 месяц'
    SEVENTH_PAGE_5_II = '200.00.005 2 месяц'
    SEVENTH_PAGE_5_III = '200.00.005 3 месяц'
    SEVENTH_PAGE_6_I = '200.00.006 1 месяц'
    SEVENTH_PAGE_6_II = '200.00.006 2 месяц'
    SEVENTH_PAGE_6_III = '200.00.006 3 месяц'
    SEVENTH_PAGE_7_I = '200.00.007 1 месяц'
    SEVENTH_PAGE_7_II = '200.00.007 2 месяц'
    SEVENTH_PAGE_7_III = '200.00.007 3 месяц'
    SEVENTH_PAGE_8_I = '200.00.008 1 месяц'
    SEVENTH_PAGE_8_II = '200.00.008 2 месяц'
    SEVENTH_PAGE_8_III = '200.00.008 3 месяц'
    SEVENTH_PAGE_9_I = '200.00.009 1 месяц'
    SEVENTH_PAGE_9_II = '200.00.009 2 месяц'
    SEVENTH_PAGE_9_III = '200.00.009 3 месяц'
    SEVENTH_PAGE_10_I = '200.00.010 1 месяц'
    SEVENTH_PAGE_10_II = '200.00.010 2 месяц'
    SEVENTH_PAGE_10_III = '200.00.010 3 месяц'
    SEVENTH_PAGE_11_I = '200.00.011 1 месяц'
    SEVENTH_PAGE_11_II = '200.00.011 2 месяц'
    SEVENTH_PAGE_11_III = '200.00.011 3 месяц'
    SEVENTH_PAGE_12_I = '200.00.012 1 месяц'
    SEVENTH_PAGE_12_II = '200.00.012 2 месяц'
    SEVENTH_PAGE_12_III = '200.00.012 3 месяц'

class FNO200Locators(object):
    # 1 СТРАНИЦА
    DECLARATION_TYPE = (By.XPATH, '//*[@name="declarationTypes"]')
    DECLARATION_TYPE_SELECT = (By.XPATH, '//*[text()="Первоначальная"]')
    TAX_PERIOD = (By.XPATH, '//*[@id="rc_select_1"]')
    TAX_PERIOD_SELECT = (By.XPATH, '//*[@title="1 квартал"]')
    APPS = (By.XPATH, '//*[@id="root"]/div/div[4]/div[4]/div/div/div[4]/form/div[3]/div[2]/div[1]/div/div/div['
                      '1]/div/div/div')
    APPS_SELECT_ALL = (By.XPATH, '//*[text()="Выбрать все"]')
    # Сведения о налогоплательщике (НП)
    TAXPAYER_CATEGORY = (By.XPATH, '//*[@name="taxpayerCategories"]')
    TAXPAYER_CATEGORY_SELECT_A = (By.XPATH, '//*[text()="A"]')
    TAXPAYER_CATEGORY_SELECT_B = (By.XPATH, '//*[text()="B"]')
    TAXPAYER_CATEGORY_SELECT_C = (By.XPATH, '//*[text()="C"]')
    TAXPAYER_CATEGORY_SELECT_E = (By.XPATH, '//*[text()="E"]')
    RESIDENT = (By.XPATH, '//*[@id="rc_select_3"]')
    RESIDENT_SELECT = (By.XPATH, '//*[@title="Резидент"]')
    FIRST_PAGE_I_MONTH = (By.XPATH, '//*[@name="fnoContent.commonInfo._8._1"]')
    FIRST_PAGE_II_MONTH = (By.XPATH, '//*[@name="fnoContent.commonInfo._8._2"]')
    FIRST_PAGE_III_MONTH = (By.XPATH, '//*[@name="fnoContent.commonInfo._8._3"]')
    FIRST_PAGE_IV_MONTH = (By.XPATH, '//*[@name="fnoContent.commonInfo._8._4"]')
    FIRST_PAGE_V_MONTH = (By.XPATH, '//*[@name="fnoContent.commonInfo._8._5"]')
    FIRST_PAGE_VI_MONTH = (By.XPATH, '//*[@name="fnoContent.commonInfo._8._6"]')
    CONFIRMATION_FIRST_PAGE_2 = (By.XPATH, '//*[text()="В том числе иностранцев и лиц без гражданства"]')
    CONFIRMATION_FIRST_PAGE_1 = (By.XPATH, '//*[text()="Наличие структурных подразделений"]')
    CONTROL_TEXT = (By.XPATH, '//*[text() = "© 2021 Комитет государственных доходов МФ РК"]')
    AFTER = (By.XPATH, '//*[text()="Далее"]')

    # 1 ПРИЛОЖЕНИЕ
    # Раздел. Индивидуальный подоходный налог
    APP_1_FIELD_1_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._001.I"]')
    APP_1_FIELD_1_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._001.II"]')
    APP_1_FIELD_1_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._001.III"]')
    APP_1_FIELD_1_A = (By.XPATH, '//*[@name="fnoContent.application_01._001.A"]')
    APP_1_FIELD_1_B = (By.XPATH, '//*[@name="fnoContent.application_01._001.B"]')
    APP_1_FIELD_1_C = (By.XPATH, '//*[@name="fnoContent.application_01._001.C"]')
    APP_1_FIELD_1_D = (By.XPATH, '//*[@name="fnoContent.application_01._001.D"]')
    APP_1_FIELD_1_E = (By.XPATH, '//*[@name="fnoContent.application_01._001.E"]')
    APP_1_FIELD_3_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._003.I"]')
    APP_1_FIELD_3_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._003.II"]')
    APP_1_FIELD_3_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._003.III"]')
    APP_1_FIELD_4 = (By.XPATH, '//*[@name="fnoContent.application_01._004"]')
    APP_1_FIELD_5 = (By.XPATH, '//*[@name="fnoContent.application_01._005"]')
    APP_1_FIELD_6 = (By.XPATH, '//*[@name="fnoContent.application_01._006"]')
    APP_1_FIELD_7_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._007.I"]')
    APP_1_FIELD_7_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._007.II"]')
    APP_1_FIELD_7_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._007.III"]')
    APP_1_FIELD_8_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._008.I"]')
    APP_1_FIELD_8_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._008.II"]')
    APP_1_FIELD_8_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._008.III"]')
    APP_1_FIELD_9_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._009.I"]')
    APP_1_FIELD_9_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._009.II"]')
    APP_1_FIELD_9_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._009.III"]')
    APP_1_FIELD_10_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._010.I"]')
    APP_1_FIELD_10_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._010.II"]')
    APP_1_FIELD_10_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._010.III"]')
    APP_1_FIELD_11_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._011.I"]')
    APP_1_FIELD_11_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._011.II"]')
    APP_1_FIELD_11_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._011.III"]')
    APP_1_FIELD_12_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._012.I"]')
    APP_1_FIELD_12_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._012.II"]')
    APP_1_FIELD_12_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._012.III"]')
    APP_1_FIELD_13_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._013.I"]')
    APP_1_FIELD_13_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._013.II"]')
    APP_1_FIELD_13_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._013.III"]')
    APP_1_FIELD_14_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._014.I"]')
    APP_1_FIELD_14_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._014.II"]')
    APP_1_FIELD_14_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._014.III"]')
    APP_1_FIELD_15_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._015.I"]')
    APP_1_FIELD_15_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._015.II"]')
    APP_1_FIELD_15_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._015.III"]')
    APP_1_FIELD_16_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._016.I"]')
    APP_1_FIELD_16_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._016.II"]')
    APP_1_FIELD_16_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._016.III"]')
    APP_1_FIELD_17_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._017.I"]')
    APP_1_FIELD_17_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._017.II"]')
    APP_1_FIELD_17_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._017.III"]')
    APP_1_FIELD_18_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._018.I"]')
    APP_1_FIELD_18_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._018.II"]')
    APP_1_FIELD_18_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._018.III"]')
    APP_1_FIELD_19_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._019.I"]')
    APP_1_FIELD_19_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._019.II"]')
    APP_1_FIELD_19_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._019.III"]')
    APP_1_FIELD_20_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._020.I"]')
    APP_1_FIELD_20_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._020.II"]')
    APP_1_FIELD_20_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_01._020.III"]')
    # 2 ПРИЛОЖЕНИЕ
    CANCEL_ADD_STR = (By.XPATH, '//*[text()="Отменить"]')
    ADD_STR = (By.XPATH, '//*[text()="Добавить строку"]')
    ADD = (By.XPATH, '//*[text()="Добавить"]')
    SECOND_APP_C = (By.XPATH, '//*[@name="C"]')
    SECOND_APP_D = (By.XPATH, '//*[@name="D"]')
    SECOND_APP_D_SELECT = (By.XPATH, '//*[@title="Резидент"]')
    SECOND_APP_E = (By.XPATH, '//*[@name="E"]')
    SECOND_APP_E_SELECT = (By.XPATH, '//*[@label="Египет"]')
    SECOND_APP_F = (By.XPATH, '//*[@name="F"]')
    SECOND_APP_G_1 = (By.XPATH, '//*[@name="G1"]')
    SECOND_APP_G_1_SELECT = (By.XPATH, '//*[text()="паспорт иностранного гражданина"]')
    SECOND_APP_G_2 = (By.XPATH, '//*[@name="G2"]')
    SECOND_APP_G_3 = (By.XPATH, '//*[@name="G3"]')
    SECOND_APP_G_3_SELECT = (By.XPATH, '//*[@class="ant-picker-cell ant-picker-cell-start ant-picker-cell-in-view"]')
    SECOND_APP_I = (By.XPATH, '//*[@name="I"]')
    SECOND_APP_I_SELECT = (By.XPATH, '//*[@label="Конвенция об избежании двойного налогообложения и предотвращении '
                                     'уклонения от уплаты налогов на доход и капитал"]')
    SECOND_APP_J = (By.XPATH, '//*[@name="J"]')
    SECOND_APP_H = (By.XPATH, '//*[@name="H"]')
    SECOND_APP_H_SELECT = (By.XPATH, '//*[@label="Доход от реализации товаров на территории Республики Казахстан, '
                                     'а также доход от реализации товаров, находящихся в Республике Казахстан, '
                                     'за ее пределами в рамках осуществления внешнеторговой деятельности"]')
    SECOND_APP_K = (By.XPATH, '//*[@name="K"]')
    SECOND_APP_K_SELECT = (By.XPATH, '//*[@label="Афганистан"]')
    SECOND_APP_L = (By.XPATH, '//*[@name="L"]')
    SECOND_APP_M = (By.XPATH, '//*[@name="M"]')
    SECOND_APP_N = (By.XPATH, '//*[@name="N"]')
    SECOND_APP_O = (By.XPATH, '//*[@name="O"]')
    SECOND_APP_P = (By.XPATH, '//*[@name="P"]')
    SECOND_APP_Q = (By.XPATH, '//*[@name="Q"]')
    SECOND_APP_R = (By.XPATH, '//*[@name="R"]')
    SECOND_APP_S = (By.XPATH, '//*[@name="S"]')
    SECOND_APP_T = (By.XPATH, '//*[@name="T"]')
    SECOND_APP_U = (By.XPATH, '//*[@name="U"]')
    SECOND_APP_V = (By.XPATH, '//*[@name="V"]')
    SECOND_APP_W = (By.XPATH, '//*[@name="W"]')
    SECOND_APP_X = (By.XPATH, '//*[@name="X"]')
    SECOND_APP_Y = (By.XPATH, '//*[@name="Y"]')
    SECOND_APP_Z = (By.XPATH, '//*[@name="Z"]')
    SECOND_APP_AA = (By.XPATH, '//*[@name="AA"]')
    SECOND_APP_AC = (By.XPATH, '//*[@name="AC"]')
    SECOND_APP_AD = (By.XPATH, '//*[@name="AD"]')
    SECOND_APP_AE = (By.XPATH, '//*[@name="AE"]')
    SECOND_APP_AF = (By.XPATH, '//*[@name="AF"]')
    SECOND_APP_AG = (By.XPATH, '//*[@name="AG"]')
    SECOND_APP_AI = (By.XPATH, '//*[@name="AI"]')
    # 3 ПРИЛОЖЕНИЕ
    BIN = (By.XPATH, '//*[@name="fnoContent.application_03[0]._7"]')
    NAME_OF_FILIAL = (By.XPATH, '//*[@name="fnoContent.application_03[0]._8"]')
    TYPE_OF_TAX = (By.XPATH, '//*[@id="rc-tabs-0-panel-0"]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div')
    TYPE_OF_TAX_SELECT = (By.XPATH, '//*[@title="Первоначальная"]')
    CONTROL_TEXT_2 = (By.XPATH, '//*[text()="Налоговый период"]')
    CODE_1 = (By.XPATH, '//*[@id="rc_select_7"]')
    CODE_1_SELECT = (By.XPATH, '//*[text()="0301"]')
    CODE_2 = (By.XPATH, '//*[@id="rc_select_10"]')
    CODE_2_SELECT = (By.XPATH, '//*[@title="УГД по Аккольскому району"]')
    WORKERS_1 = (By.XPATH, '//*[@name="fnoContent.application_03[0]._10._1"]')
    WORKERS_2 = (By.XPATH, '//*[@name="fnoContent.application_03[0]._10._2"]')
    WORKERS_3 = (By.XPATH, '//*[@name="fnoContent.application_03[0]._10._3"]')
    THIRD_APP_1_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._001.I"]')
    THIRD_APP_1_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._001.II"]')
    THIRD_APP_1_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._001.III"]')
    THIRD_APP_2_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._002.I"]')
    THIRD_APP_2_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._002.II"]')
    THIRD_APP_2_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._002.III"]')
    THIRD_APP_3_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._003.I"]')
    THIRD_APP_3_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._003.II"]')
    THIRD_APP_3_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._003.III"]')
    THIRD_APP_4_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._004.I"]')
    THIRD_APP_4_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._004.II"]')
    THIRD_APP_4_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._004.III"]')
    THIRD_APP_5_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._005.I"]')
    THIRD_APP_5_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._005.II"]')
    THIRD_APP_5_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._005.III"]')
    THIRD_APP_6_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._006.I"]')
    THIRD_APP_6_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._006.II"]')
    THIRD_APP_6_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._006.III"]')
    THIRD_APP_7_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._007.I"]')
    THIRD_APP_7_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._007.II"]')
    THIRD_APP_7_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._007.III"]')
    THIRD_APP_8_I_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._008.I"]')
    THIRD_APP_8_II_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._008.II"]')
    THIRD_APP_8_III_MONTH = (By.XPATH, '//*[@name="fnoContent.application_03[0]._008.III"]')
    CODE_3 = (By.XPATH, '//*[@id="rc-tabs-0-panel-0"]/div[16]/div[1]/div/div/div[2]/div[1]/div/span/div[1]/div/span[1]')
    CODE_3_SELECT = (By.XPATH, '//*[text()="0303"]')
    CODE_4 = (By.XPATH, '//*[@id="rc-tabs-0-panel-0"]/div[16]/div[2]/div/div/div[2]/div[1]/div/span/div[1]/div/span[1]')
    CODE_4_SELECT = (By.XPATH, '//*[text()="0304"]')
    CONFIRMATION_2 = (By.XPATH, '//*[text()="Я несу ответственность в соответствии с законами Республики Казахстан за '
                                'достоверность и полноту сведений,  приведенных в данной налоговой отчетности."]')

    # ПРИЛОЖЕНИЕ 4
    NUMBER_OF_CONTRACT = (By.XPATH, '//*[@name="fnoContent.application_04[0]._4_A"]')
    DATE_OF_CONTRACT = (By.XPATH, '//*[@name="fnoContent.application_04[0]._4_B"]')
    DATE_OF_CONTRACT_SELECT = (By.XPATH, '//*[text()="1"]')
    EMPLOYEES_NUMBER_1_I = (By.XPATH, '//*[@name="fnoContent.application_04[0]._3_1"]')
    EMPLOYEES_NUMBER_1_II = (By.XPATH, '//*[@name="fnoContent.application_04[0]._3_2"]')
    EMPLOYEES_NUMBER_1_III = (By.XPATH, '//*[@name="fnoContent.application_04[0]._3_3"]')
    EMPLOYEES_NUMBER_2_I = (By.XPATH, '//*[@name="fnoContent.application_04[0]._3_4"]')
    EMPLOYEES_NUMBER_2_II = (By.XPATH, '//*[@name="fnoContent.application_04[0]._3_5"]')
    EMPLOYEES_NUMBER_2_III = (By.XPATH, '//*[@name="fnoContent.application_04[0]._3_6"]')
    EMPLOYEES_NUMBER_3_I = (By.XPATH, '//*[@name="fnoContent.application_04[0]._3_7"]')
    EMPLOYEES_NUMBER_3_II = (By.XPATH, '//*[@name="fnoContent.application_04[0]._3_8"]')
    EMPLOYEES_NUMBER_3_III = (By.XPATH, '//*[@name="fnoContent.application_04[0]._3_9"]')
    EMPLOYEES_NUMBER_4_I = (By.XPATH, '//*[@name="fnoContent.application_04[0]._001.I"]')
    EMPLOYEES_NUMBER_4_II = (By.XPATH, '//*[@name="fnoContent.application_04[0]._001.II"]')
    EMPLOYEES_NUMBER_4_III = (By.XPATH, '//*[@name="fnoContent.application_04[0]._001.III"]')
    TAX_PERCENT_1 = (By.XPATH, '//*[@name="fnoContent.application_04[0]._002.I"]')
    TAX_PERCENT_2 = (By.XPATH, '//*[@name="fnoContent.application_04[0]._002.II"]')
    TAX_PERCENT_3 = (By.XPATH, '//*[@name="fnoContent.application_04[0]._002.III"]')

    # ПРИЛОЖЕНИЕ 5
    FIFTH_APP_C = (By.XPATH, '//*[@name="C"]')
    FIFTH_APP_B = (By.XPATH, '//*[@name="B"]')
    FIFTH_APP_D = (By.XPATH, '//*[@name="D"]')
    FIFTH_APP_D_SELECT = (By.XPATH, '//*[text()="Работник"]')
    FIFTH_APP_E = (By.XPATH, '//*[@name="E"]')
    FIFTH_APP_E_SELECT = (By.XPATH, '//*[text()="Пенсионер"]')
    FIFTH_APP_G = (By.XPATH, '//*[@name="G"]')
    FIFTH_APP_F = (By.XPATH, '//*[text()="Является физическим лицом структурного подразделения"]')
    FIFTH_APP_H = (By.XPATH, '//*[@name="H"]')
    FIFTH_APP_I = (By.XPATH, '//*[@name="I"]')
    FIFTH_APP_J = (By.XPATH, '//*[@name="J"]')
    FIFTH_APP_K = (By.XPATH, '//*[@name="K"]')
    FIFTH_APP_L = (By.XPATH, '//*[@name="L"]')
    FIFTH_APP_M = (By.XPATH, '//*[@name="M"]')
    FIFTH_APP_N = (By.XPATH, '//*[@name="N"]')
    FIFTH_APP_O = (By.XPATH, '//*[@name="O"]')
    FIFTH_APP_P = (By.XPATH, '//*[@name="P"]')
    FIFTH_APP_Q = (By.XPATH, '//*[@name="Q"]')
    FIFTH_APP_R = (By.XPATH, '//*[@name="R"]')
    FIFTH_APP_S = (By.XPATH, '//*[@name="S"]')
    FIFTH_APP_T = (By.XPATH, '//*[@name="T"]')
    FIFTH_APP_U = (By.XPATH, '//*[@name="U"]')

    # 7 СТРАНИЦА (после всех приложений)
    SEVENTH_PAGE_1_I =(By.XPATH, '//*[@name="fnoContent.calculatedIndicators._001.I"]')
    SEVENTH_PAGE_1_II = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._001.II"]')
    SEVENTH_PAGE_1_III = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._001.III"]')
    SEVENTH_PAGE_2_I = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._002.I"]')
    SEVENTH_PAGE_2_II = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._002.II"]')
    SEVENTH_PAGE_2_III = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._002.III"]')
    SEVENTH_PAGE_3_I = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._003.I"]')
    SEVENTH_PAGE_3_II = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._003.II"]')
    SEVENTH_PAGE_3_III = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._003.III"]')
    SEVENTH_PAGE_4_I = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._004.I"]')
    SEVENTH_PAGE_4_II = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._004.II"]')
    SEVENTH_PAGE_4_III = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._004.III"]')
    SEVENTH_PAGE_5_I = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._005.I"]')
    SEVENTH_PAGE_5_II = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._005.II"]')
    SEVENTH_PAGE_5_III = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._005.III"]')
    SEVENTH_PAGE_6_I = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._006.I"]')
    SEVENTH_PAGE_6_II = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._006.II"]')
    SEVENTH_PAGE_6_III = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._006.III"]')
    SEVENTH_PAGE_7_I = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._007.I"]')
    SEVENTH_PAGE_7_II = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._007.II"]')
    SEVENTH_PAGE_7_III = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._007.III"]')
    SEVENTH_PAGE_8_I = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._008.I"]')
    SEVENTH_PAGE_8_II = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._008.II"]')
    SEVENTH_PAGE_8_III = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._008.III"]')
    SEVENTH_PAGE_9_I = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._009.I"]')
    SEVENTH_PAGE_9_II = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._009.II"]')
    SEVENTH_PAGE_9_III = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._009.III"]')
    SEVENTH_PAGE_10_I = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._010.I"]')
    SEVENTH_PAGE_10_II = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._010.II"]')
    SEVENTH_PAGE_10_III = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._010.III"]')
    SEVENTH_PAGE_11_I = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._011.I"]')
    SEVENTH_PAGE_11_II = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._011.II"]')
    SEVENTH_PAGE_11_III = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._011.III"]')
    SEVENTH_PAGE_12_I = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._012.I"]')
    SEVENTH_PAGE_12_II = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._012.II"]')
    SEVENTH_PAGE_12_III = (By.XPATH, '//*[@name="fnoContent.calculatedIndicators._012.III"]')
    # СТРАНИЦА ОТПРАВКИ
    CONFIRMATION_3 = (By.XPATH, '//*[@name="fnoContent.taxpayerResponsibility.isResponsible"]')
    FORM_DECLARATION = (By.XPATH, '//*[text()="Сформировать"]')
