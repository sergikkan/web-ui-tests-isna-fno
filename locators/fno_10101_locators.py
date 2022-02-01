from selenium.webdriver.common.by import By

'''Локаторы в странице 101.10 ФНО'''
class FNO1010locatorsName(object):
    YEAR_SELECT = 'Годовой период'
    SELECT_2021 = '2021'
    SUBMIT_BUTTON = 'Подача документа'
    DECLARATION_TYPE_SELECT = 'Вид Расчета'
    INITIAL_SELECT = 'Первоначальный'
    SEPERATE_CATEGORY = 'Категория налогоплательщика'
    TAXPAYER_CHP = 'Выбор категорий налогоплательщика 1'
    CONFIDENTIONAL_SELECT = 'Выбор категорий налогоплательщика 2'
    FOUNDER_TAXPAYER = 'Выбор категорий налогоплательщика 3'
    RESIDENTION_SELECT = 'Признак резидентства'
    RESIDENTION_TRUE = 'Выбор пункта "Резидент РК" '
    RESIDENTION_FALSE = 'Выбор пункта "Нерезидент РК" '
    RESIDENTION_COUNTRY_CODE = 'Код страны резидентства'
    RESIDENTION_SELECT_AUS = 'Австралия'
    INPUT_TAX_CODE_NON_RESIDENT = 'Номер налоговой регистрации в стране резидентства'
    FIRST_TAX_CODEX_CHECKBOX = 'Расчет суммы авансовых платежей по КНП в соответствии с подпунктом 1) пункта 5 статьи ' \
                               '305 Налогового кодекса '
    SECOND_TAX_CODEX_CHECKBOX = 'Расчет суммы авансовых платежей по КНП в соответствии с подпунктом 2) пункта 5 ' \
                                'статьи 305 Налогового кодекса '
    AFTER_BUTTON_FIRST_PAGE = 'Далее'
    TOTAL_ADVANCE_AMOUNT = '100.01.01 Общая сумма авансовых платежей за предыдущий налоговый период'
    TOTAL_ADVANCE_AMOUNT_BEFORE_DECLARATION = '101.01.002 Cумма авансовых платежей, подлежащая уплате за период до ' \
                                              'сдачи декларации '
    AFTER_BUTTON_SECOND_PAGE = 'Далее'
    EXPECTED_SUM = '101.01.004 Предполагаемая сумма КПН, исчисленная в соответствии с пунктом 1 статьи 302 Налогового ' \
                   'кодекса '
    EXPECTED_SUM2 = '101.01.005 Предполагаемая сумма КПН, исчисленная в соответствии со статьей 652 Налогового кодекса'
    DECLINE_SUM1 = '101.01.007 Уменьшение суммы авансовых платежей в соответствии со статьей 700 Налогового кодекса'
    CODE = 'Код'
    SELECT_0302 = 'Выбор документа'
    ACCEPT_CHECKBOX_FNO = 'Пользовательское соглашение'
    FORM = 'Формирование'
    AVANCE_CALC = 'Калькуляция подачи'
    AVANCE_CALC_BEFORE_DEC = 'Калькуляция подачи перед декларацией'
    AVANCE_CALC_FIRST_SUB = 'Калькуляция первой подачи'




class FNO1010locators(object):
    # СТРАНИЦА С ВЫБОРОМ НАЛОГОВОГО ПЕРИОДА
    YEAR_SELECT = (By.XPATH, '//div[@class="ant-picker-input"]')
    SELECT_2021 = (By.XPATH, '//td[@title="2020"]')
    # SELECT_2021 = (By.XPATH, '//*[contains(@title, \'2020\')] ')
    SUBMIT_BUTTON = (By.XPATH, '//*[text()=\'Подать\']')
    # ПЕРВАЯ СТРАНИЦА
    # ОБЩАЯ ИНФОМРАЦИЯ
    DECLARATION_TYPE_SELECT = (By.XPATH, '//div[@name="declarationTypes"]')
    INITIAL_SELECT = (By.XPATH, '//span[@title="Первоначальный"]')
    # Сведения о налогоплательщике (НП)
    SEPERATE_CATEGORY = (By.XPATH, '//div[@name="taxpayerCategories"]')
    CONFIDENTIONAL_SELECT = (By.XPATH, '//*[text()="Налогоплательщик, применяющий СНР в соответствии  '
                                       'со статьями 697-701 Налогового кодекса"]')
    TAXPAYER_CHP = (By.XPATH, '//*[text()="Налогоплательщик, применяющий СНР в соответствии '
                              ' со статьями 697-701 Налогового кодекса"]')
    FOUNDER_TAXPAYER = (By.XPATH, '//*[text()=\'Учредитель доверительного управления\']')

    RESIDENTION_SELECT = (By.XPATH, '//div[@class="ant-select ant-select-lg select ant-select-single ant-select-show'
                                    '-arrow"]')
    RESIDENTION_TRUE = (By.XPATH, '//*[text()=\'Резидент РК\']')
    RESIDENTION_FALSE = (By.XPATH, '//*[text()=\'Нерезидент РК\']')
    RESIDENTION_COUNTRY_CODE = (By.XPATH, '//input[@id="rc_select_8"]')
    RESIDENTION_SELECT_AUS = (By.XPATH, '//*[text()=\'Австралия\']')
    INPUT_TAX_CODE_NON_RESIDENT = (By.XPATH, '//div[@name="fnoContent.commonInfo._8_B"]')

    # Предоставляемые расчет
    FIRST_TAX_CODEX_CHECKBOX = (By.XPATH, '//span[text()="Расчет суммы авансовых платежей по КНП в соответствии с '
                                          'подпунктом 1) пункта 5 статьи 305 Налогового кодекса"]')
    SECOND_TAX_CODEX_CHECKBOX = (By.XPATH, '//span[text()="Расчет суммы авансовых платежей по КНП в соответствии с'
                                           ' подпунктом 2) пункта 5 статьи 305 Налогового кодекса"]')

    # КНОПКА ДАЛЕЕ
    AFTER_BUTTON_FIRST_PAGE = (By.XPATH, '//*[text()=\'Далее\']')
    # ВТОРАЯ СТРАНИЦА ПЕРВЫЙ ВАРИАНТ
    # Расчет суммы авансовых платежей по КПН в соответствии с подпунктом 1) пункта 5 статьи 305 Налогового кодекса
    TOTAL_ADVANCE_AMOUNT = (By.XPATH, '//input[@name="fnoContent.amountAdvancePayment._001"]')
    TOTAL_ADVANCE_AMOUNT_BEFORE_DECLARATION = (By.XPATH, '//input[@name="fnoContent.amountAdvancePayment._002"]')
    AFTER_BUTTON_SECOND_PAGE = (By.XPATH, '//*[text()=\'Далее\']')
    # ВТОРАЯ СТРАНИЦА ВТОРОЙ ВАРИАНТ
    EXPECTED_SUM = (By.XPATH, '//input[@name="fnoContent.amountAdvancePayment._004"]')
    EXPECTED_SUM2 = (By.XPATH, '//input[@name="fnoContent.amountAdvancePayment._005"]')
    DECLINE_SUM1 = (By.XPATH, '//input[@name="fnoContent.amountAdvancePayment._007"]')

    # ПОСЛЕДНЯЯ СТРАНИЦА ОТПРАВКА
    CODE = (By.XPATH, '//div[@class="ant-select ant-select-lg ant-select-single ant-select-'
                      'show-arrow ant-select-show-search"][1]')
    SELECT_0302 = (By.XPATH, '//div[contains(@class, \'ant-select-item-option-content\') and text() = \'0301\']')
    ACCEPT_CHECKBOX_FNO = (By.XPATH, '//input[@name="fnoContent.taxpayerResponsibility.isResponsible"]')
    FORM = (By.XPATH, '//*[text()=\'Сформировать\']')
    AVANCE_CALC = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div[5]/div[2]/div/div/'
                             'div/div/div[1]/div/div')
    AVANCE_CALC_BEFORE_DEC = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div['
                                        '11]/div[2]/div/div/div/div/div[1]/div/div')
    AVANCE_CALC_FIRST_SUB = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div[5]/div[2]'
                                       '/div/div/div/div/div[1]/div/div')
