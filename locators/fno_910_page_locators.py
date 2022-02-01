from selenium.webdriver.common.by import By

'''Локаторы в странице 910 ФНО'''


class FNO910LocatorsName(object):
    HALF_YEAR_SELECT = 'Выбор квартала'
    FIRST_HALF_YEAR = 'Выбор первого квартала'
    INPUT_YEAR = 'Годовой период'
    SELECT_YEAR_2020 = 'Выбор "2021" года'
    SEND_TAX_PERIOD = 'Подача даты'
    DECLARATION_TYPE_SELECT = 'Вид отчетности (декларации)'
    INITIAL_SELECT = 'Первоначальная'
    CURRENCY_TYPE = 'Валюта'
    CURRENCY_INPUT = 'Внутрення валюта'
    TALA_SELECT = 'Тала'
    TENGE_SELECT = 'Тенге'
    SEPERATE_CATEGORY = 'Отдельные категории налогоплательщика'
    CLASS_SELECT = 'Доверительный управляющий'
    ACCOUNTANT = 'Ведет бухгалтерский учет'
    RESIDENTION_SELECT = 'Признак резидентства'
    SELECT_RESIDENT_TRUE = 'Резидент РК'
    TIS_CHECKBOX = 'Наличие трехкомпонентной интегрированной системы (ТИС)'
    TIS_NAME_INPUT = 'Наименование трехкомпонентной интегрированной системы'
    TIS_CARD_NUMBER_INPUT = 'Номер регистрационной карточки'
    TIS_DATE_INPUT = 'Дата постановки на учет'
    TIS_DATE_SELECT = 'Выбор даты постановки на учет'
    AFTER_BUTTON = 'Далее'
    A_INPUT_INCOME_CASHLESS = 'A Доходы, полученные путем безналичных расчетов'
    B_INPUT_INCOME_CASHLESS = 'B Доходы, полученные путем наличных расчетов'
    A_I = 'A I в том числе с применением ТИС'
    B_I = 'B I в том числе с применением ТИС'
    INCOME_WITH_LAW = '910.00.002 В том числе доход от корректировки в соответствии с Законом о трансфертном ценообразовании'
    EMPLOYEE_QUANTITY = '910.00.003 Среднесписочная численность работников, в том числе:'
    PENSIONER_QUANTITY = 'A пенсионеры'
    INVALID_QUANTITY = 'B инвалиды'
    AVERAGE_SALARY = '910.00.008 Сумма индивидуального (корпоративного) подоходного налога, подлежащего уплате в ' \
                     'бюджет (910.00.007 х 0.5) '
    SALARY = '910.00.004 Среднемесячная заработная плата на одного работника'
    IPN_1_MONTH = 'Доход для исчисления социальных отчислений за 1 месяц'
    IPN_2_MONTH = 'Доход для исчисления социальных отчислений за 2 месяц'
    IPN_3_MONTH = 'Доход для исчисления социальных отчислений за 3 месяц'
    IPN_4_MONTH = 'Доход для исчисления социальных отчислений за 4 месяц'
    IPN_5_MONTH = 'Доход для исчисления социальных отчислений за 5 месяц'
    IPN_6_MONTH = 'Доход для исчисления социальных отчислений за 6 месяц'




class FNO910Locators(object):
    HALF_YEAR_SELECT = (By.XPATH, '//div[@class="ant-select-selector"]')
    FIRST_HALF_YEAR = (By.XPATH, '//div[@class = "ant-select-item-option-content"][1]')
    INPUT_YEAR = (By.XPATH, '//*[@placeholder="Год"]')
    SELECT_YEAR_2020 = (By.XPATH, '//*[@title="2020"]')
    SEND_TAX_PERIOD = (By.XPATH, '//*[text()=\'Подать\']')
    # ПЕРВАЯ СТРАНИЦА
    GO_TO_SECOND_PAGE = (By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div[2]/div/div[2]/span')
    # Раздел. Общая информация
    DECLARATION_TYPE_SELECT = (By.XPATH, '//div[@name="declarationTypes"]')
    INITIAL_SELECT = (By.XPATH, '//span[text()="Первоначальная"]')
    CURRENCY_TYPE = (By.XPATH, '//div[@class="ant-select ant-select-lg select ant-select-single '
                               'ant-select-show-arrow ant-select-show-search"]')
    CURRENCY_INPUT = (By.XPATH, '//input[@id="rc_select_54"]')
    TALA_SELECT = (By.XPATH, '//*[text()="Тала"]')
    TENGE_SELECT = (By.XPATH, '//*[text()="Тенге"]')
    # Сведения о налогоплательщике (налоговом агенте, агенте или плательщике социальных платежей)
    SEPERATE_CATEGORY = (By.XPATH, '//div[@name="taxpayerCategories"]')
    CLASS_SELECT = (By.XPATH, '//span[text()="Доверительный управляющий в соответствии со статьей 40 Налогового '
                              'кодекса"]')
    ACCOUNTANT = (By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[3]/div[1]/div/div/div[3]/span[4]')
    RESIDENTION_SELECT = (By.XPATH, '//*[@id="root"]/div/div[4]/div[4]/div/div/div[4]/form/div[1]/div[4]/div['
                                    '2]/div/div/div[2]/div[1]/div/div/div')
    SELECT_RESIDENT_TRUE = (By.XPATH, '//div[text()="Резидент"]')
    # Наличие трехкомпонентной интегрированной системы (ТИС)
    TIS_CHECKBOX = (By.XPATH, '//input[@name="fnoContent.commonInfo.isShowTis"]')
    TIS_NAME_INPUT = (By.XPATH, '//input[@name="fnoContent.commonInfo._6.A"]')
    TIS_CARD_NUMBER_INPUT = (By.XPATH, '//input[@name="fnoContent.commonInfo._6.B"]')
    TIS_DATE_INPUT = (By.XPATH, '//input[@name="fnoContent.commonInfo._6.C"]')
    TIS_DATE_SELECT = (By.XPATH, '//div[@class="ant-picker-cell-inner" and text()="1"]')
    TIS_STOCK_BEGINNING_TAX_PERIOD = (By.XPATH, '//input[@name="fnoContent.inventoryInfo._027.A"]')
    TIS_STOCK_ENDING_TAX_PERIOD = (By.XPATH, '//input[@name="fnoContent.inventoryInfo._027.B"]')
    ACQURIED = (By.XPATH, '//input[@name="fnoContent.inventoryInfo._027.C"]')
    # КНОПКА Далее после заполнения первой страницы
    AFTER_BUTTON = (By.XPATH, '//*[text()="Далее"]')
    # ВТОРАЯ страница
    # 910.00.001 Доход
    A_INPUT_INCOME_CASHLESS = (By.XPATH, '//input[@name="fnoContent.calculatedTax._001.A"]')
    B_INPUT_INCOME_CASHLESS = (By.XPATH, '//input[@name="fnoContent.calculatedTax._001.B"]')
    A_I = (By.XPATH, '//input[@name="fnoContent.calculatedTax._001.AI"]')
    B_I = (By.XPATH, '//input[@name="fnoContent.calculatedTax._001.BI"]')
    INCOME_WITH_LAW = (By.XPATH, '//input[@name="fnoContent.calculatedTax._002"]')
    EMPLOYEE_QUANTITY = (By.XPATH, '//input[@name="fnoContent.calculatedTax._003.total"]')
    PENSIONER_QUANTITY = (By.XPATH, '//input[@name="fnoContent.calculatedTax._003.A"]')
    INVALID_QUANTITY = (By.XPATH, '//input[@name="fnoContent.calculatedTax._003.B"]')
    AVERAGE_SALARY = (By.XPATH, '//input[@name="fnoContent.calculatedTax._009"]')
    SALARY = (By.XPATH, '//input[@name="fnoContent.calculatedTax._004"]')
    # ТРЕТЬЯ СТРАНИЦА
    # 910.00.012-013 Доход для исчисления социальных отчислений (CО) и Сумма СО, к уплате
    INCOME_SO_1 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._012.I"]')
    INCOME_SO_2 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._012.II"]')
    INCOME_SO_3 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._012.III"]')
    INCOME_SO_4 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._012.IV"]')
    INCOME_SO_5 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._012.V"]')
    INCOME_SO_6 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._012.VI"]')
    # 910.00.014-015 Доход, для исчисления обязательных пенсионных взносов (ОПВ) и Сумма ОПВ, к уплате
    INCOME_OPV_1 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._014.I"]')
    INCOME_OPV_2 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._014.II"]')
    INCOME_OPV_3 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._014.III"]')
    INCOME_OPV_4 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._014.IV"]')
    INCOME_OPV_5 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._014.V"]')
    INCOME_OPV_6 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._014.VI"]')
    # 910.00.016 Сумма взносов на обязательное социальное медицинское страхование, к уплате
    CON_SUM_1 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._016.I"]')
    CON_SUM_2 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._016.II"]')
    CON_SUM_3 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._016.III"]')
    CON_SUM_4 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._016.IV"]')
    CON_SUM_5 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._016.V"]')
    CON_SUM_6 = (By.XPATH, '//*[@name="fnoContent.calculatedSocialPaymentForIP._016.VI"]')
    # ЧЕТВЕРТАЯ СТРАНИЦА
    # 910.00.017 Сумма ИПН, подлежащая перечислению в бюджет с доходов граждан РК
    IPN_1_MONTH = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._017.I"]')
    IPN_2_MONTH = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._017.II"]')
    IPN_3_MONTH = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._017.III"]')
    IPN_4_MONTH = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._017.IV"]')
    IPN_5_MONTH = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._017.V"]')
    IPN_6_MONTH = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._017.VI"]')
    # 910.00.018 Сумма ИПН, подлежащая перечислению в бюджет с доходов иностранцев и лиц без гражданства
    IPN_NO_RESIDENT_1 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._018.I"]')
    IPN_NO_RESIDENT_2 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._018.II"]')
    IPN_NO_RESIDENT_3 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._018.III"]')
    IPN_NO_RESIDENT_4 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._018.IV"]')
    IPN_NO_RESIDENT_5 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._018.V"]')
    IPN_NO_RESIDENT_6 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._018.VI"]')
    # 910.00.019-020 Доходы ФЛ, с которых исчисляются СО и Сумма СО, к уплате
    FL_INCOME_1 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._019.I"]')
    FL_INCOME_2 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._019.II"]')
    FL_INCOME_3 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._019.III"]')
    FL_INCOME_4 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._019.IV"]')
    FL_INCOME_5 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._019.V"]')
    FL_INCOME_6 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._019.VI"]')
    # 910.00.021-022 Доходы работников, с которых удерживаются (начисляются) ОПВ и Сумма ОПВ, к уплате
    OPV_1 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._021.I"]')
    OPV_2 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._021.II"]')
    OPV_3 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._021.III"]')
    OPV_4 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._021.IV"]')
    OPV_5 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._021.V"]')
    OPV_6 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._021.VI"]')
    # 910.00.023-024 Доходы работников, принимаемых для исчисления обязательных
    # профессиональных пенсионных взносов (ОППВ) и Сумма ОППВ, к уплате
    OPPV_1 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._023.I"]')
    OPPV_1_TO_PAY = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._024.I"]')
    OPPV_2 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._023.II"]')
    OPPV_2_TO_PAY = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._024.II"]')
    OPPV_3 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._023.III"]')
    OPPV_3_TO_PAY = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._024.III"]')
    OPPV_4 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._023.IV"]')
    OPPV_4_TO_PAY = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._024.IV"]')
    OPPV_5 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._023.V"]')
    OPPV_5_TO_PAY = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._024.V"]')
    OPPV_6 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._023.VI"]')
    OPPV_6_TO_PAY = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._024.VI"]')
    # 910.00.025-026 Доходы, принимаемые для исчисления взносов и отчислений на обязательное социальное
    # медицинское страхование (ОСМС) и Сумма взносов и отчислений на ОСМС, к уплате
    OSMS_1 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._025.I"]')
    OSMS_1_TO_PAY = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._026.I"]')
    OSMS_2 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._025.II"]')
    OSMS_2_TO_PAY = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._026.II"]')
    OSMS_3 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._025.III"]')
    OSMS_3_TO_PAY = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._026.III"]')
    OSMS_4 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._025.IV"]')
    OSMS_4_TO_PAY = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._026.IV"]')
    OSMS_5 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._025.V"]')
    OSMS_5_TO_PAY = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._026.V"]')
    OSMS_6 = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._025.VI"]')
    OSMS_6_TO_PAY = (By.XPATH, '//input[@name="fnoContent.calculatedSocialAndIPNForIndividual._026.VI"]')
    # ПЯТАЯ СТРАНИЦА ОТПРАВКА ДОКУМЕНТА
    # ПОСЛЕДНЯЯ СТРАНИЦА ОТПРАВКА
    CODE = (By.XPATH, '//input[@id="rc_select_7"]')
    SELECT_0301 = (By.XPATH, '//div[contains(@class, \'ant-select-item-option-content\') and text() = \'0301\']')
    ACCEPT_CHECKBOX_FNO = (By.XPATH, '//input[@name="fnoContent.taxpayerResponsibility.isResponsible"]')
    BIN_INPUT = (By.XPATH, '//input[@name="fnoContent.inventoryInfo._028"]')
    FORM = (By.XPATH, '//*[text()=\'Сформировать\']')
    # ПОДСКАЗКИ
    IPN_FIRST = (By.XPATH, '//*[text()="Сумма ИПН, подлежащая перечислению в бюджет с доходов граждан РК"]')
    IPN_SECOND = (By.XPATH, '//*[text()="Сумма ИПН, подлежащая перечислению в бюджет'
                            ' с доходов иностранцев и лиц без гражданства"]')
    FL_INCOME = (By.XPATH, '//*[text()="Доходы ФЛ, с которых исчисляются СО и Сумма СО, к уплате"]')
    OPV = (By.XPATH, '//*[text()="Доходы работников, с которых удерживаются (начисляются) ОПВ и Сумма ОПВ, к уплате"]')
    OPPV = (By.XPATH, '//*[text()="Доходы работников, принимаемых для исчисления обязательных'
                      ' профессиональных пенсионных взносов (ОППВ) и Сумма ОППВ, к уплате"]')
    OSMS = (By.XPATH, '//*[text()="Доходы, принимаемые для исчисления взносов и отчислений на '
                      'обязательное социальное медицинское страхование (ОСМС) и Сумма взносов'
                      ' и отчислений на ОСМС, к уплате"]')
    FL_TOTAL_I = (By.XPATH, '//span[@class="cabinet__label-input_color-primary" and text() = "910.00.019.VII "]')
    FL_TOTAL_II = (By.XPATH, '//span[@class="cabinet__label-input_color-primary" and text() = "910.00.020.VII "]')
    OPV_TOTAL_I = (By.XPATH, '//span[@class="cabinet__label-input_color-primary" and text() = "910.00.021.VII "]')
    OPV_TOTAL_II = (By.XPATH, '//span[@class="cabinet__label-input_color-primary" and text() = "9910.00.022.VII "]')


