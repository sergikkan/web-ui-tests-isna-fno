from selenium.webdriver.common.by import By


class FNO701LocatorsName(object):
    NOTICE_NUMBER = 'Номер уведомления'
    FIELD = '701.00.001 Сумма текущих платежей, подлежащих уплате'
    APP_C = 'C Сумма текущих платежей, подлежащих уплате'

class FNO701Locators(object):
    YEAR = (By.XPATH, '//*[@placeholder="Год"]')
    SELECT_2021 = (By.XPATH, '//*[@class="ant-picker-cell-inner" and text()="2021"]')
    SEND_TAX_PERIOD = (By.XPATH, '//*[text()="Подать"]')
    # Первая страница
    DECLARATION_TYPE = (By.XPATH, '//*[@name="declarationTypes"]')
    DECLARATION_TYPE_SELECT = (By.XPATH, '//*[@title="Дополнительная по уведомлению"]')
    CONTROL_TEXT = (By.XPATH, '//*[text()="Вид Расчёта"]')
    CONTROL_TEXT_2 = (By.XPATH, '//*[text()="Отдельные категории налогоплательщика"]')
    NOTICE_NUMBER = (By.XPATH, '//*[@name="fnoContent.commonInfo._5.A"]')
    NOTICE_DATE = (By.XPATH, '//*[@name="fnoContent.commonInfo._5.B"]')
    NOTICE_DATE_SELECT = (By.XPATH, '//*[@class="ant-picker-cell ant-picker-cell-in-view ant-picker-cell-today"]')
    TAX_PAYER_CATEGORIES = (By.XPATH, '//*[@name="taxpayerCategories"]')
    TAX_PAYER_CATEGORIES_SELECT = (By.XPATH, '//*[text()="A"]')
    APPS = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div[1]/div[7]/div/div[1]/div/div/div['
                      '1]/div/div/div')
    APP_SELECT = (By.XPATH, '//*[@title="Приложение к Расчету 701.00"]')
    AFTER = (By.XPATH, '//*[text()="Далее"]')
    # Первое приложение
    TYPE = (By.XPATH, '//*[@id="rc-tabs-4-panel-0"]/div[1]/div/div/div/div[2]/div[1]/div/div/div')
    TYPE_SELECT = (By.XPATH, '//*[text()=" - общеустановленный порядок"]')
    FIELD = (By.XPATH, '//*[@name="fnoContent.application[0]._001"]')
    ADD_STR = (By.XPATH, '//*[text() = "Добавить строку"]')
    FIND = (By.XPATH, '//*[text()="Найти"]')
    FIND_0101 = (By.XPATH, '//*[@placeholder="Поиск по БИН, Код, Наименованию аппарата акима"]')
    SELECT_0101 = (By.XPATH, '//*[text()="0101"]')
    CONFIRM = (By.XPATH, '//*[text()="Подтвердить"]')
    APP_C = (By.XPATH, '//*[@name="C"]')
    ADD = (By.XPATH, '//*[text()="Добавить"]')
    CONFIRMATION = (By.XPATH, '//*[text()="Я несу ответственность в соответствии с законами Республики Казахстан за '
                              'достоверность и полноту сведений,  приведенных в данном Расчете."]')
    FORM = (By.XPATH, '//*[text()="Сформировать"]')