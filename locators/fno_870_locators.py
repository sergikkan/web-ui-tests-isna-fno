from selenium.webdriver.common.by import By


class FNO870LocatorsName(object):
    QUARTER_SELECT = 'Выбор квартала'
    FIRST_QUARTAL_SELECT = 'Выбор первого квартала'
    YEAR_SLEECT = 'Годовой период'
    SELECT_2021 = 'Выбор "2021" года'
    SEND_TAX_PERIOD = 'Подача даты'
    DECLARATION_TYPE = 'Вид отчетности (декларации)'
    INITIAL = 'Первоначальная'
    BIN = 'БИН юридического лица'
    TAXPAYER_CATEGORIES = 'Категории налогоплательщика'
    TAXPAYER_CATEGORIES_SELECT = 'Доверительный управляющий'
    SUBMITTED_ANNEXES_TO_TAX_REPORTING = 'Представленные приложения к налоговой отчетности'
    SELECT_APPLICATIONS_TO_TAX_REPORTING = 'Выбор приложения к налоговой отчетности'
    ADD_NEW_TAB = 'Добавление дополнительной декларации'
    REMOVE_NEW_TAB = 'Удаление дополнительной декларации'
    ENVIRONMENTAL_PERMIT = 'Наличие экологического разрешения'
    PEMISSION_NO = 'No разрешения'
    DATE_OF_ISSUE = 'Дата выдачи'
    DATE_SELECT = 'Выбор даты выдачи'
    CATEGORIES_OF_OBJECT = 'Категория объектов'
    CATEGORY_SELECT = 'Выбор категории'
    TYPE_OF_SPECIAL_NATURE_MANAGEMENT = 'Вид специального природопользования'
    SELECT_TYPE = 'Выбор вида природопользования'
    UNITS_OF_MEASUREMENT = 'Единицы измерения природопользования'
    SELECT_TYPE_OF_UNITS = 'Выбор единиц измерения'
    CLASSIFICATION_CODE = 'Код опасных отходов согласно Классификатору отходов'
    TYPE_OF_POLLUTANT_PARAGRAPH = 'Вид загрязняющего вещества (Пункт)'
    TYPE_OF_POLLUTANT_SUBPARAGRAPH = 'Вид загрязняющего вещества (Подпункт)'
    REMAINING_STANDARD_AT_THE_BEGINNING = 'Остаток норматива на начало квартала'
    ACTUAL_VOLUME_OF_EMISSIONS_1 = 'Фактический объем эмиссий в пределах установленных нормативов'
    ACTUAL_VOLUME_OF_EMISSIONS_2 = 'Фактический объем эмиссий сверх установленных нормативов'
    REMAINING_STANDARD_AT_THE_END = 'Остаток норматива на конец квартала'
    THE_RATE_OF_PAYMENT_ESTABLISHED = 'Ставка платы, установленная согласно статье 576 Налогового кодекса'
    THE_SIZE_OF_THE_INCREASE_IN = 'Размер повышения ставки платы по решению местных представительных органов'
    COEFFICIENTS_APPLIED_TO_PAYERS = 'Коэффициенты, применяемые к плательщикам платы'
    SELECT_COEFFICIENT = 'Выбор коэффицента'
    CODE = 'Код'
    SELECT_0302 = 'Выбор документа'
    ACCEPT_CHECKBOX_FNO = 'Пользовательское соглашение'
    FORM = 'Формирование'







class FNO870Locators(object):
    #Налоговый период
    #ВЫБОР КВАРТАЛА
    QUARTER_SELECT = (By.XPATH, '//*[@aria-expanded="false"]')
    FIRST_QUARTAL_SELECT = (By.XPATH, '//*[text()="1 квартал"]')
    YEAR_SLEECT = (By.XPATH, '//*[@placeholder="Год"]')
    SELECT_2021 = (By.XPATH, '//*[@title="2021"]')
    SEND_TAX_PERIOD = (By.XPATH, '//*[text()="Подать"]')
    #Вид отчетности (декларации)
    DECLARATION_TYPE = (By.XPATH, '//*[@name="declarationTypes"]')
    #Выбор типа отчетности
    INITIAL = (By.XPATH, '//*[text()="Первоначальная"]')
    #БИН юр.лица
    BIN = (By.XPATH, '//*[@name="fnoContent.commonInfo._2"]')
    #Категории налогоплательщика
    TAXPAYER_CATEGORIES = (By.XPATH, '//*[@name="taxpayerCategories"]')
    #Выбор категории налогоплательщика
    TAXPAYER_CATEGORIES_SELECT = (By.XPATH, '//*[text()="Доверительный управляющий в соответствии со статьей 40 '
                                            'Налогового кодекса"]')
    #Представленные приложения к налоговой отчетности
    SUBMITTED_ANNEXES_TO_TAX_REPORTING = (By.XPATH, '//*[@class="ant-select ant-tree-select ant-select-lg'
                                                    ' appselector ant-select-multiple ant-select-show-search"]')
    #Выбор приложения к налоговой отчетности
    SELECT_APPLICATIONS_TO_TAX_REPORTING = (By.XPATH, '//*[text()="Плата за эмиссии в окружающую среду"]')
    '''#Новая страница'''
    ADD_NEW_TAB = (By.XPATH, '//button[@class="ant-tabs-nav-add" and @aria-label="Add tab"]')
    REMOVE_NEW_TAB = (By.XPATH, '//*[@class="ant-tabs-tab-remove"]')
    #Наличие экологического разрешения
    ENVIRONMENTAL_PERMIT = (By.XPATH, '//input[@name="fnoContent.application_01.0._4.value"]')
    #No разрешения
    PEMISSION_NO = (By.XPATH, '//*[@name="fnoContent.application_01.0._4.A"]')
    #Дата выдачи
    DATE_OF_ISSUE = (By.XPATH, '//*[@name="fnoContent.application_01.0._4.B"]')
    #Выбор даты выдачи
    DATE_SELECT = (By.XPATH, '//*[@class="ant-picker-cell ant-picker-cell-in-view ant-picker-cell-today"]')
    #Код опасных отходов согласно Классификатору отходов*
    CLASSIFICATION_CODE = (By.XPATH, '//*[@name="fnoContent.application_01.0._6.hazardousWasteCode"]')
    #Категория объектов
    CATEGORIES_OF_OBJECT = (By.XPATH, '//*[@id="rc-tabs-3-panel-0"]/div[3]/div[3]/div/div/div[2]/div[1]/div/div/div')
    #Выбор категории
    CATEGORY_SELECT = (By.XPATH, '//*[text()="I категория"]')
    #Вид специального природопользования
    TYPE_OF_SPECIAL_NATURE_MANAGEMENT = (By.XPATH, '//*[@id="rc-tabs-0-panel-0"]/div[4]/div[1]/div/div/div[2]/div[1]/div/div/div/span[1]')
    #Выбор вида природопользования
    SELECT_TYPE = (By.XPATH, '//*[@title="Выбросы загрязняющих веществ от стационарных источников"]')
    #Единицы измерения природопользования
    UNITS_OF_MEASUREMENT = (By.XPATH, '//*[@id="rc-tabs-0-panel-0"]/div[4]/div[2]/div/div/div[2]/div[1]/div/div/div')
    #Выбор единиц измерения
    SELECT_TYPE_OF_UNITS = (By.XPATH, '//*[@title="Тонна"]')
    #Вид загрязняющего вещества (Пункт)
    TYPE_OF_POLLUTANT_PARAGRAPH = (By.XPATH, '//*[@name="fnoContent.application_01.0._6.item"]')
    #Вид загрязняющего вещества (Подпункт)
    TYPE_OF_POLLUTANT_SUBPARAGRAPH = (By.XPATH, '//*[@name="fnoContent.application_01.0._6.subItem"]')
    #Раздел. Сведения об объемах загрязнения
    #Остаток норматива на начало квартала
    REMAINING_STANDARD_AT_THE_BEGINNING = (By.XPATH, '//*[@name="fnoContent.application_01.0._001"]')
    #Фактический объем эмиссий в пределах установленных нормативов
    ACTUAL_VOLUME_OF_EMISSIONS_1 = (By.XPATH, '//*[@name="fnoContent.application_01.0._003"]')
    #Фактический объем эмиссий сверх установленных нормативов
    ACTUAL_VOLUME_OF_EMISSIONS_2 = (By.XPATH, '//*[@name="fnoContent.application_01.0._004"]')
    #Остаток норматива на конец квартала
    REMAINING_STANDARD_AT_THE_END = (By.XPATH, '//*[@name="fnoContent.application_01.0._005"]')
    #Раздел. Сведения об установленных ставках для исчисления платы за эмиссии в окружающую среду
    #Ставка платы, установленная согласно статье 576 Налогового кодекса
    THE_RATE_OF_PAYMENT_ESTABLISHED = (By.XPATH, '//*[@name="fnoContent.application_01.0._006"]')
    #Размер повышения ставки платы по решению местных представительных органов
    THE_SIZE_OF_THE_INCREASE_IN = (By.XPATH, '//*[@name="fnoContent.application_01.0._007"]')
    #Коэффициенты, применяемые к плательщикам платы
    COEFFICIENTS_APPLIED_TO_PAYERS = (By.XPATH, '//*[@id="rc_select_9"]')
    #Выбор коэффицента
    SELECT_COEFFICIENT = (By.XPATH, '//*[@title="коэффициент 0,3"]')
    '''Третья страница ОТПРАВКА'''
    CODE = (By.XPATH, '//*[@id="rc_select_10"]')
    SELECT_0302 = (By.XPATH, '//div[contains(@class, \'ant-select-item-option-content\') and text() = \'0301\']')
    ACCEPT_CHECKBOX_FNO = (By.XPATH, '//input[@name="fnoContent.taxpayerResponsibility.isResponsible"]')
    FORM = (By.XPATH, '//*[text()=\'Сформировать\']')


