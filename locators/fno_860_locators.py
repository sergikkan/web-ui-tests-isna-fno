from selenium.webdriver.common.by import By


class FNO860LocatorsName(object):
    QUARTER_SELECT = 'Выбор квартала'
    FIRST_QUARTER_SELECT = 'Выбор первого квартала'
    YEAR_SELECT = 'Годовой период'
    SELECT_2021 = 'Выбор "2021" года'
    SEND_TAX_PERIOD = 'Подача даты'
    DECLARATION_TYPE = 'Вид отчетности (декларации)'
    INITIAL_SELECT = 'Первоначальная'
    TAX_PAYER_CATEGORIES = 'Категории налогоплательщика'
    TRUSTEE_SELECT = 'Доверительный управляющий'
    SUBMITTED_ANNEXES_TO_TAX_REPORTING = 'Представленные приложения к налоговой отчетности'
    PAYMENT_FOR_USING_WATER_RESOURCES = 'Плата за пользование водными ресурсами поверхностных источников'
    BUTTON_ADD_NEW_FORM = 'Добавление дополнительной декларации'
    BUTTON_001 = 'Декларация No 1'
    CHECKBOX_AVALIABLE_RESOLUTION = 'Наличие разрешительного документа на специальное водопользование'
    BUTTON_REMOVE_NEW_FORM = 'Удаление дополнительной декларации'
    SELECT_DATE = 'Дата выдачи'
    SELECT_FIRST_DATE = 'Выбор первого числа'
    INPUT_ALLOW_DOC = '№ разрешительного документа'
    SPECIAL_WATER_USING_TYPE = 'Вид специального водопользования'
    INDUSTRY = 'Промышленность, включая теплоэнергетику'
    WATER_UNITS = 'Единицы измерения водопользования'
    CUB = 'Куб.м'
    FIRST_MONTH_LIMIT = 'Лимит первого месяца'
    SECOND_MONTH_LIMIT = 'Лимит второго месяца'
    THIRD_MONTH_LIMIT = 'Лимит третьего месяца'
    FIRST_MONTH_FACT = 'Фактический объем водопользования в первом месяце'
    SECOND_MONTH_FACT = 'Фактический объем водопользования во втором месяце'
    THIRD_MOTH_FACT = 'Фактический объем водопользования в третьем месяце'
    RATE_WITHIN_THE_LIMIT = '860.01.004 Ставка платы в пределах установленного лимита'
    CALCULATED_WITH_LIMIT = '860.01.006 Исчисленная сумма платы в пределах установленного лимита'
    OGD_CODE = 'Код ОГД'
    SELECT_0301 = 'Выбор документа 0301'
    OGD_NAME = 'Название ОГД'
    ACMOLA_SELECT = 'Акмолинская область'
    FIO_GOV = 'ФИО'
    DATE_END_DECLARATION = 'Дата окончания срока декларации'
    SELECT_FIRST_DATE_END = 'Выбор первого числа'
    COD_GOV = 'Код GOV'
    URAL_CASP_SELECT = 'Урал Каспий выбор'
    CHECKBOX_ACCEPT = 'Соглашение'
    FORM = 'Формирование декларации'









class FNO860Locators(object):
    # ВЫБОР НАЛОГОВОГО ПЕРИОДА
    QUARTER_SELECT = (By.XPATH, '//input[@id="rc_select_0"]')
    FIRST_QUARTER_SELECT = (By.XPATH, '//*[text()="1 квартал"]')
    YEAR_SELECT = (By.XPATH, "//*[@placeholder=\"Год\"]")
    SELECT_2020 = (By.XPATH, '//td[@title="2020"]')
    SEND_TAX_PERIOD = (By.XPATH, '//*[text()="Подать"]')
    # Раздел. Общая информация
    DECLARATION_TYPE = (By.XPATH, '//div[@name="declarationTypes"]')
    INITIAL_SELECT = (By.XPATH, '//span[text()="Первоначальная"]')
    # Сведения о налогоплательщике
    TAX_PAYER_CATEGORIES = (By.XPATH, '//*[@name="taxpayerCategories"]')
    TRUSTEE_SELECT = (By.XPATH, '//*[text()="Доверительный управляющий"]')
    # Представленные приложения к налоговой отчетности
    SUBMITTED_ANNEXES_TO_TAX_REPORTING = (By.XPATH, '//div[@class="ant-select ant-tree-select ant-select-lg'
                                                    ' appselector ant-select-multiple ant-select-show-search"]')
    PAYMENT_FOR_USING_WATER_RESOURCES = (By.XPATH, '//span[text()="Плата за пользование водными' \
                                                   ' ресурсами поверхностных источников"]')
    '''Вторая страница'''
    # Раздел. Общая информация
    BUTTON_ADD_NEW_FORM = (By.XPATH, '//button[@aria-label="Add tab"]')
    BUTTON_001 = (By.XPATH, '//div[@role="tab" and text()="001"]')
    CHECKBOX_AVALIABLE_RESOLUTION = (By.XPATH, '//input[@name="fnoContent.application_01.0._3.isAvailable"]')
    BUTTON_REMOVE_NEW_FORM = (By.XPATH, '//button[@type="button" and @class="ant-tabs-tab-remove"]')
    SELECT_DATE = (By.XPATH, '//input[@name="fnoContent.application_01.0._3.A"]')
    SELECT_FIRST_DATE = (By.XPATH, '//div[@class="ant-picker-cell-inner" and text()="1"]')
    INPUT_ALLOW_DOC = (By.XPATH, '//input[@name="fnoContent.application_01.0._3.B"]')
    SPECIAL_WATER_USING_TYPE = (By.XPATH, '//*[@id="rc-tabs-2-panel-0"]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div')
    INDUSTRY = (By.XPATH, '//*[@label="Промышленность, включая теплоэнергетику"]')
    WATER_UNITS = (By.XPATH, '//*[@id="rc-tabs-1-panel-0"]/div[2]/div[2]/div/div/div[2]/div[1]/div/div/span')
    CUB = (By.XPATH, '//div[@label="Куб.м"]')
    # Раздел. Сведения об объемах водопользования (в единицах измерения, указанных в строке 5) для исчисления платы
    # 860.01.001Установленный лимит (из расчета за отчетный налоговый период)
    FIRST_MONTH_LIMIT = (By.XPATH, '//input[@name="fnoContent.application_01[0]._001.I"]')
    SECOND_MONTH_LIMIT = (By.XPATH, '//input[@name="fnoContent.application_01[0]._001.II"]')
    THIRD_MONTH_LIMIT = (By.XPATH, '//input[@name="fnoContent.application_01[0]._001.III"]')
    # 860.01.002Фактический объем водопользования за отчетный налоговый год
    FIRST_MONTH_FACT = (By.XPATH, '//input[@name="fnoContent.application_01[0]._002.I"]')
    SECOND_MONTH_FACT = (By.XPATH, '//input[@name="fnoContent.application_01[0]._002.II"]')
    THIRD_MOTH_FACT = (By.XPATH, '//input[@name="fnoContent.application_01[0]._002.III"]')
    # 860.01.004Ставка платы в пределах установленного лимита
    RATE_WITHIN_THE_LIMIT = (By.XPATH, '//input[@name="fnoContent.application_01[0]._004"]')
    # 860.01.006Исчисленная сумма платы в пределах установленного лимита
    CALCULATED_WITH_LIMIT = (By.XPATH, '//input[@name="fnoContent.application_01[0]._006"]')
    # ТРЕТЬЯ СТРАНИЦА ОТПРАВКА
    OGD_CODE = (By.XPATH, '//input[@id="rc_select_10"]')
    SELECT_0301 = (By.XPATH, '//*[@title="0301"]')
    OGD_NAME = (By.XPATH, '//input[@id="rc_select_11"]')
    ACMOLA_SELECT = (By.XPATH, '//*[@title="ДГД по Акмолинской области"]')
    FIO_GOV = (By.XPATH, '//*[@name="fnoContent.taxpayerResponsibility.fullNameOfficialPersonWaterFund"]')
    DATE_END_DECLARATION = (By.XPATH, '//*[@name="fnoContent.taxpayerResponsibility.declarationCertificatio'
                                      'nDateWaterFundOrg"]')
    SELECT_FIRST_DATE_END = (By.XPATH, '//div[@class="ant-picker-cell-inner" and text()="1"]')
    COD_GOV = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div[5]/div[2]/div/div/div/div[1]/div/div/div')
    URAL_CASP_SELECT = (By.XPATH, '//div[@class="ant-select-item-option-content" and text()="0314"]')
    CHECKBOX_ACCEPT = (By.XPATH, '//*[@name="fnoContent.taxpayerResponsibility.isResponsible"]')
    FORM = (By.XPATH, '//*[text()=\'Сформировать\']')
    '''ЛОКАТОРЫ ДЛЯ ПОДСКАЗОК'''
    FIRST_8600101 = (By.XPATH, '//span[text()="Установленный лимит (из расчета за отчетный налоговый период)"]')
    SECOND_D8600102 = (By.XPATH, '//span[text()="Фактический объем водопользования за отчетный налоговый год"]')
    THIRD_8600103 = (By.XPATH, '//*[text()="6 000 "]')
    FOURTH_CALCULATED_05 = (By.XPATH, '//*[@id="rc-tabs-0-panel-0"]/div[9]/div[2]/div/div/div/div/div[1]/div/div')
    FIFVTH = (By.XPATH,
              '//*[@id="rc-tabs-0-panel-0"]/div[9]/div[2]')
    SEVEN = (By.XPATH, '//*[@id="rc-tabs-0-panel-0"]/div[12]/div[2]/div/div/div/div/div[1]/div/div')
