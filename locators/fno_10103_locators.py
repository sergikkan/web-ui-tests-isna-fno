from selenium.webdriver.common.by import By


class FNO10103LocatorsName(object):
    DECLARATION_TYPE = 'Вид декларации'
    INITIAL_SELECT = 'Выбор вида декларации'
    RESIDENTION_SELECT = 'Признак резидентства'
    SELECT_RESIDENT_TRUE = 'Выбор пункта "Резидент РК" '
    SELECT_RESIDENT_FALSE = 'Выбор пункта "Нерезидент РК" '
    FIRST_MONTH_I = 'Первый месяц 1'
    SECOND_MONTH_I = 'Второй месяц 1'
    THIRD_MONTH_I = 'Третий месяц 1'
    FIRST_MONTH_II = 'Первый месяц 2'
    SECOND_MONTH_II = 'Второй месяц 2'
    THIRD_MONTH_II = 'Третий месяц 2'
    AFTER_BUTTON = 'Кнопка "Далее" '
    CODE = 'Код'
    SELECT_0302 = 'Выбор документа'
    ACCEPT_CHECKBOX_FNO = 'Пользовательское соглашение'
    FORM = 'Формирование'

class FNO10103Locators(object):
    DECLARATION_TYPE = (By.XPATH, '//div[@name="declarationTypes"]')
    INITIAL_SELECT = (By.XPATH, '//span[text()="Первоначальный"]')
    RESIDENTION_SELECT = (By.ID, 'rc_select_2')
    SELECT_RESIDENT_TRUE = (By.XPATH, '//div[text()="Резидент РК"]')
    SELECT_RESIDENT_FALSE = (By.XPATH, '//div[text()="Нерезидент РК"]')
    ##101.03.001Сумма выплачиваемого дохода за квартал
    FIRST_MONTH_I = (By.XPATH, '//input[@name="fnoContent.calculation._001.I"]')
    SECOND_MONTH_I = (By.XPATH, '//input[@name="fnoContent.calculation._001.II"]')
    THIRD_MONTH_I = (By.XPATH, '//input[@name="fnoContent.calculation._001.III"]')
    # 101.03.002Сумма налога, удержанного у источника выплаты за квартал
    FIRST_MONTH_II = (By.XPATH, '//input[@name="fnoContent.calculation._002.I"]')
    SECOND_MONTH_II = (By.XPATH, '//input[@name="fnoContent.calculation._002.II"]')
    THIRD_MONTH_II = (By.XPATH, '//input[@name="fnoContent.calculation._002.III"]')
    # кнопка далее
    AFTER_BUTTON = (By.XPATH, '//*[text()="Далее"]')
    # ТРЕТЬЯ КНОПКА СФОРМИРОВАНИЕ И ОТПРАВКА ДОКУМЕНТА
    CODE = (By.XPATH, '//div[@class="ant-select ant-select-lg ant-select-single ant-select-'
                      'show-arrow ant-select-show-search"][1]')
    SELECT_0302 = (By.XPATH, '//div[contains(@class, \'ant-select-item-option-content\') and text() = \'0301\']')
    ACCEPT_CHECKBOX_FNO = (By.XPATH, '//input[@name="fnoContent.taxpayerResponsibility.isResponsible"]')
    FORM = (By.XPATH, '//*[text()=\'Сформировать\']')


class FNO10103PromtText(object):
    PROMT_TEXT_10103001 = (By.XPATH, '//*[text()="Строки 101.03.001 I, 101.03.001 II и 101.03.001 III '
                                     'предназначены для отражения суммы доходов, облагаемых у источника '
                                     'выплаты, выплачиваемых налоговым агентом за каждый '
                                     'месяц налогового периода"]')
    PROMT_TEXT_10103002 = (By.XPATH, '//*[text()="Строки 101.03.002 I, 101.03.002 II и 101.03.002 III предназначены '
                                     'для отражения суммы КПН, удержанного у источника выплаты, и '
                                     'подлежащего уплате в бюджет за каждый месяц налогового периода. "]')