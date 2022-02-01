from selenium.webdriver.common.by import By

'''Локаторы в странице 101.02 ФНО'''


class FNO10102locatorsName(object):
    YEAR_SELECT = 'Годовой период'
    SELECT_2021 = 'Выбор годового периода'
    SUBMIT_BUTTON = 'Подача документа'
    DECLARATION_TYPE_SELECT = 'Вид Расчета'
    INITIAL_SELECT = 'Выбор вида расчета'
    WITH_NOTIFICATION = 'Уведомление'
    NOTIFICATION_NUM = 'Номер уведомлений'
    DATE = 'Дата'
    BUTTON_NEXT_X2 = 'Кнопка "Далее" '
    SELECT_30 = 'Выбор 30'
    SEPERATE_CATEGORY = 'Категория налогоплательщика'
    CONFIDENTIONAL_SELECT = 'Выбор категорий налогоплательщика'
    TAXPAYER_CHP = 'Выбор категорий налогоплательщика 2'
    FOUNDER_TAXPAYER = 'Выбор категорий налогоплательщик 3'
    RESIDENTION_SELECT = 'Признак резидентства'
    RESIDENTION_TRUE = 'Выбор пункта "Резидент РК"'
    RESIDENTION_FALSE = 'Выбор пункта "Нерезидент РК" '
    RESIDENTION_COUNTRY_CODE = 'Код страны резидентства'
    RESIDENTION_SELECT_AUS = 'Выбор кода страны резидентства'
    INPUT_TAX_CODE_NON_RESIDENT = 'Номер налоговой регистрации в стране резидентства'
    FIRST_TAX_CODEX_CHECKBOX = 'Расчет суммы авансовых платежей по КНП в соответствии с подпунктом 1) пункта 5 статьи ' \
                               '305 Налогового кодекса '
    SECOND_TAX_CODEX_CHECKBOX = 'Расчет суммы авансовых платежей по КНП в соответствии с подпунктом 2) пункта 5 ' \
                                'статьи 305 Налогового кодекса '
    AFTER_BUTTON_FIRST_PAGE = 'Далее'
    FIRST_PARAPGRAPH_INPUT = '101.02.001 Исчисленная сумма КПН на предыдущий налоговый период 1'
    SECOND_PARAPGRAPH_INPUT = '101.02.001 Исчисленная сумма КПН на предыдущий налоговый период 2'
    ADVANCE_PAYMENT_3_5 = '101.02.002 Сумма авансовых платежей, подлежащая уплате за период после сдачи декларации'
    ADVANCE_PAYMENT_700 = '101.02.003 Уменьшение суммы авансовых платежей в соответствии со статьей 700 Налогового ' \
                          'кодекса '
    ADVANCE_PAYMENT_MONTHLY = '101.02.004 Сумма ежемесячного авансового платежа'
    SUPPOSED_SUM1 = '101.02.005 Предполагаемая сумма КПН, исчисленная в соответствии с пунктом 1 статьи 302 ' \
                    'Налогового кодекса '
    SUPPOSED_SUM2 = '101.02.006 Предполагаемая сумма КПН, исчисленная в соответствии со статьей 652 Налогового кодекса'
    DECREASE_AVANCE_PAYMENT = '101.02.008 Уменьшение суммы авансовых платежей в соответствии со статьей 700 ' \
                              'Налогового кодекса '
    TOTAL_AVANCE_PAYMENT = '101.02.009 Сумма ежемесячного авансового платежа'
    KNP_BEFORE = ''
    AVANCE_BEFORE = ''
    CALC_DECLARATION007 = ''

class FNO10102locators(object):
    # СТРАНИЦА С ВЫБОРОМ НАЛОГОВОГО ПЕРИОДА
    YEAR_SELECT = (By.XPATH, '//div[@class="ant-picker-input"]')
    SELECT_2021 = (By.XPATH, '//td[@title="2020"]')
    # SELECT_2021 = (By.XPATH, '//*[contains(@title, \'2020\')] ')
    SUBMIT_BUTTON = (By.XPATH, '//*[text()=\'Подать\']')
    # ПЕРВАЯ СТРАНИЦА
    # ОБЩАЯ ИНФОМРАЦИЯ
    DECLARATION_TYPE_SELECT = (By.XPATH, '//div[@name="declarationTypes"]')
    INITIAL_SELECT = (By.XPATH, '//span[@title="Первоначальный"]')
    WITH_NOTIFICATION = (By.XPATH, '//span[text()=\'Дополнительный по уведомлению\']')
    NOTIFICATION_NUM = (By.XPATH, '//input[@name="fnoContent.commonInfo._5.A"]')
    DATE = (By.XPATH, '//input[@name="fnoContent.commonInfo._5.B"]')
    BUTTON_NEXT_X2 = (By.XPATH, '//button[@class="ant-picker-header-super-next-btn"]')
    SELECT_30 = (By.XPATH, '//div[text()="30"]')
    # Сведения о налогоплательщике (НП)
    SEPERATE_CATEGORY = (By.XPATH, '//div[@name="taxpayerCategories"]')
    CONFIDENTIONAL_SELECT = (By.XPATH, '//*[@title="Налогоплательщик, применяющий СНР в соответствии  со статьями 697-701 Налогового кодекса"]')
    TAXPAYER_CHP = (By.XPATH, '//*[text()=\'НП, применяющий СНР\']')
    FOUNDER_TAXPAYER = (By.XPATH, '//*[text()=\'Учредитель доверительного управления\']')

    RESIDENTION_SELECT = (By.XPATH, '//div[@class="ant-select ant-select-lg select ant-select-single ant-select-show'
                                    '-arrow"]')
    RESIDENTION_TRUE = (By.XPATH, '//*[text()=\'Резидент РК\']')
    RESIDENTION_FALSE = (By.XPATH, '//*[text()=\'Нерезидент РК\']')
    RESIDENTION_COUNTRY_CODE = (By.XPATH, '//input[@aria-controls="rc_select_5_list"]8"]')
    RESIDENTION_SELECT_AUS = (By.XPATH, '//*[text()=\'Австралия\']')
    INPUT_TAX_CODE_NON_RESIDENT = (By.XPATH, '//div[@name="fnoContent.commonInfo._8_B"]')

    # Предоставляемые расчет
    FIRST_TAX_CODEX_CHECKBOX = (By.XPATH, '//span[text()="Расчет суммы авансовых платежей по КНП в соответствии с '
                                          'подпунктом 3) пункта 5 статьи 305 Налогового кодекса"]')
    SECOND_TAX_CODEX_CHECKBOX = (By.XPATH, '//span[text()="Расчет суммы авансовых платежей по КПН в соответствии с '
                                           'подпунктом 4) пункта 5 статьи 305 Налогового кодекса"]')

    # КНОПКА ДАЛЕЕ
    AFTER_BUTTON_FIRST_PAGE = (By.XPATH, '//*[text()=\'Далее\']')
    # ВТОРАЯ СТРАНИЦА ВЫБОР 101.02.001Исчисленная сумма КПН на предыдущий налоговый период
    FIRST_PARAPGRAPH_INPUT = (By.XPATH, '//input[@name="fnoContent.calculatedAmount._001.I"]')
    SECOND_PARAPGRAPH_INPUT = (By.XPATH, '//input[@name="fnoContent.calculatedAmount._001.II"]')
    # ВЫБОР ПЕРВОГО ПОДПУНКТА ВТОРАЯ СТРАНИЦА
    ADVANCE_PAYMENT_3_5 = (By.XPATH, '//input[@name="fnoContent.calculatedAmount._002"]')
    ADVANCE_PAYMENT_700 = (By.XPATH, '//input[@name="fnoContent.calculatedAmount._003"]')
    ADVANCE_PAYMENT_MONTHLY = (By.XPATH, '//input[@name="fnoContent.calculatedAmount._004"]')

    # ВЫБОР ВТОРОГО ПОДПУНКТА ВТОРАЯ СТРАНИЦА
    SUPPOSED_SUM1 = (By.XPATH, '//input[@name = "fnoContent.calculatedAmount._005"]')
    SUPPOSED_SUM2 = (By.XPATH, '//input[@name = "fnoContent.calculatedAmount._006"]')
    DECREASE_AVANCE_PAYMENT = (By.XPATH, '//input[@name = "fnoContent.calculatedAmount._008"]')
    TOTAL_AVANCE_PAYMENT = (By.XPATH, '//input[@name = "fnoContent.calculatedAmount._009"]')

    # SPANЫ ПРИ КОТОРЫХ ДОЛЖНА ВЫХОДИТЬ ПОДСКАЗ
    KNP_BEFORE = (By.XPATH, '//*[text()="Исчисленная сумма КПН на предыдущий налоговый период"]')
    AVANCE_BEFORE = (By.XPATH, '//*[text()="Сумма авансовых платежей, подлежащая уплате за период '
                               'после сдачи декларации"]')
    CALC_DECLARATION007 = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div[8]/'
                                     'div[2]/div/div/div/div/div[1]/div/div')