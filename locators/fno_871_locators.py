from selenium.webdriver.common.by import By


class FNO871LocatorsName(object):
    NOTICE_NUMBER = 'Номер уведомления'
    APP_E = 'E Номер документа, удостоверяющего личность арендатора- физического лица'
    APP_D = 'D ИИН (БИН) арендатора'
    APP_G = 'G Номер (при его наличии) договора аренды (пользования)'
    APP_I = 'I Назначение торгового места, торгового объекта'
    APP_J = 'J Местонахождения торгового места в торговом объекте'
    APP_L = 'L Сумма арендной платы в соответствии с договором аренды (пользования)'
    APP_M = 'M Фактически уплаченная сумма арендной платы'
    APP_N = 'N Сумма возмещаемых расходов в соответствии с договором аренды (пользования)'
    APP_O = 'O Фактически уплаченная сумма возмещаемых расходов'
    GENERAL_SQUARE = 'Общая площадь, кв.м'
    TRADE_SQUARE = 'Торговая площадь, кв.м'
    NUMBER_OF_TRADE_PLACES = 'Количество торговых мест'
    ADDRESS = 'Адрес места нахождения торгового объекта'


class FNO871Locators(object):
    # Выбор даты подачи
    YEAR_SELECT = (By.XPATH, '//*[@placeholder="Год"]')
    SELECT_2021 = (By.XPATH, '//*[@class="ant-picker-cell-inner" and text()="2021"]')
    SEND_TAX_PERIOD = (By.XPATH, '//*[text()="Подать"]')
    # Первая страница
    REGISTRY_TYPE = (By.XPATH, '//*[@name="declarationTypes"]')
    REGISTRY_TYPE_SELECT = (By.XPATH, '//*[@title="Дополнительная по уведомлению"]')
    CONTROL_TEXT = (By.XPATH, '//*[text()="Представленные приложения к налоговой отчетности"]')
    NOTICE_NUMBER = (By.XPATH, '//*[@name="noticeNumber"]')
    NOTICE_DATE = (By.XPATH, '//*[@name="noticeDate"]')
    NOTICE_DATE_SELECT = (By.XPATH, '//*[@class="ant-picker-cell ant-picker-cell-in-view ant-picker-cell-today"]')
    APPS = (By.XPATH, '//*[@aria-expanded="false"]')
    APP_SELECT = (By.XPATH, '//*[@title="Приложение 871.01 Реестр договоров аренды (пользования)"]')
    AFTER = (By.XPATH, '//*[text()="Далее"]')
    # Вторая страница
    GO_TO_SECOND_PAGE = (By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div[2]/div/div[2]/span')
    # Первое приложение
    ADD_APP = (By.XPATH, '//*[@aria-label="Add tab"]')
    REMOVE_APP = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div[1]/div[1]/div[1]/div/div['
                            '2]/button')
    NAME_OF_TRADE_ORGANISATION = (By.XPATH, '//*[@name="fnoContent.application_01[0]._3"]')
    NAME_OF_TRADE_OBJECT = (By.XPATH, '//*[@name="fnoContent.application_01[0]._4"]')
    CONFIRM = (By.XPATH, '//*[@name="fnoContent.application_01.0._4_A"]')
    CATEGORY_OF_OBJECT = (By.XPATH, '//*[@aria-expanded="false"]')
    CATEGORY_OF_OBJECT_SELECT = (By.XPATH, '//*[text()="Стационарный"]')
    GENERAL_SQUARE = (By.XPATH, '//*[@name="fnoContent.application_01[0]._6"]')
    TRADE_SQUARE = (By.XPATH, '//*[@name="fnoContent.application_01[0]._7"]')
    NUMBER_OF_TRADE_PLACES = (By.XPATH, '//*[@name="fnoContent.application_01[0]._8"]')
    ADDRESS = (By.XPATH, '//*[@name="fnoContent.application_01[0]._9"]')
    ADD_STR = (By.XPATH, '//*[text() = "Добавить строку"]')
    APP_E = (By.XPATH, '//*[@name="E"]')
    APP_F = (By.XPATH, '//*[@name="F"]')
    APP_F_SELECT = (By.XPATH, '//*[text()="Сегодня"]')
    APP_G = (By.XPATH, '//*[@name="G"]')
    APP_H = (By.XPATH, '//*[@name="H"]')
    APP_H_SELECT = (By.XPATH, '//*[text()="Сегодня"]')
    APP_I = (By.XPATH, '//*[@name="I"]')
    APP_J = (By.XPATH, '//*[@name="J"]')
    FROM = (By.XPATH, '//*[@placeholder="С"]')
    TO = (By.XPATH, '//*[@placeholder="По"]')
    FROM_SELECT = (By.XPATH, '//*[text()="1" and @class="ant-picker-cell-inner"]')
    TO_SELECT = (By.XPATH, '//*[text()="5" and @class="ant-picker-cell-inner"]')
    APP_L = (By.XPATH, '//*[@name="L"]')
    APP_M = (By.XPATH, '//*[@name="M"]')
    APP_N = (By.XPATH, '//*[@name="N"]')
    APP_O = (By.XPATH, '//*[@name="O"]')
    ADD = (By.XPATH, '//*[text()="Добавить"]')
    # Страница отправки
    CONFIRM_2 = (By.XPATH, '//*[@class="ant-checkbox"]')
    FORM = (By.XPATH, '//*[text()="Сформировать"]')

