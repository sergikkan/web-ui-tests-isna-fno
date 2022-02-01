from selenium.webdriver.common.by import By


class FNO70101LocatorsName(object):
    NOTICE_NUMBER = 'Номер уведомления'
    SECOND_PAGE_C = 'C Сумма текущих платежей, подлежащих уплате не позднее 25 февраля'
    SECOND_PAGE_D = 'D Сумма текущих платежей, подлежащих уплате не позднее 25 мая'
    SECOND_PAGE_E = 'E Сумма текущих платежей, подлежащих уплате не позднее 25 августа'
    SECOND_PAGE_F = 'F Сумма текущих платежей, подлежащих уплате не позднее 25 ноября'
    APP_C = 'C Сумма текущих платежей, подлежащих уплате не позднее 25 февраля'
    APP_D = 'D Сумма текущих платежей, подлежащих уплате не позднее 25 мая'
    APP_E = 'E Сумма текущих платежей, подлежащих уплате не позднее 25 августа'
    APP_F = 'F Сумма текущих платежей, подлежащих уплате не позднее 25 ноября'


class FNO70101Locators(object):
    YEAR_SELECT = (By.XPATH, '//*[@placeholder="Год"]')
    SELECT_2021 = (By.XPATH, '//*[@class="ant-picker-cell-inner" and text()="2021"]')
    SEND_TAX_PERIOD = (By.XPATH, '//*[text()="Подать"]')
    # ПЕРВАЯ СТРАНИЦА
    # Контрольные тексты для выключения всплывающей таблицы посредством клика
    CONTROL_TEXT_1 = (By.XPATH, '//*[text()="Налоговый период"]')
    CONTROL_TEXT_2 = (By.XPATH, '//*[text()="Отдельные категории налогоплательщика"]')
    DECLARATION_TYPE = (By.XPATH, '//div[@name="declarationTypes"]')
    DECLARATION_TYPE_SELECT = (By.XPATH, '//span[text()="Дополнительная по уведомлению"]')
    NOTICE_NUMBER = (By.XPATH, '//*[@name="fnoContent.commonInfo._5.A"]')
    NOTICE_DATE = (By.XPATH, '//*[@name="fnoContent.commonInfo._5.B"]')
    NOTICE_DATE_SELECT = (By.XPATH, '//*[text()="Сегодня"]')
    TAX_PAYER_CATEGORIES = (By.XPATH, '//*[@name="taxpayerCategories"]')
    TAX_PAYER_CATEGORIES_SELECT = (By.XPATH, '//*[text()=" – учредитель доверительного управления в соответствии со '
                                             'статьей 40 Налогового кодекса"]')
    APPS = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div[7]/div/div[1]/div/div/div['
                      '1]/div/div/div')
    APP_SELECT = (By.XPATH, '//*[@title="Приложение к Расчету 701.01"]')
    AFTER = (By.XPATH, '//*[text()="Далее"]')
    # ВТОРАЯ СТРАНИЦА
    ADD_STR = (By.XPATH, '//*[text()="Добавить строку"]')
    SECOND_PAGE_A = (By.XPATH, '//*[@name="A"]')
    SECOND_PAGE_A_SELECT = (By.XPATH, '//*[text()="104302 - Земельный налог на земли населенных пунктов."]')
    SECOND_PAGE_C = (By.XPATH, '//*[@name="C"]')
    SECOND_PAGE_D = (By.XPATH, '//*[@name="D"]')
    SECOND_PAGE_E = (By.XPATH, '//*[@name="E"]')
    SECOND_PAGE_F = (By.XPATH, '//*[@name="F"]')
    CANCEL_ADD_STR = (By.XPATH, '//*[text()="Отменить"]')
    ADD = (By.XPATH, '//*[text()="Добавить"]')
    # ПЕРВОЕ ПРИЛОЖЕНИЕ
    FIND = (By.XPATH, '//*[text()="Найти"]')
    FIND_0 = (By.XPATH, '//*[@placeholder="Поиск по БИН, Код, Наименованию аппарата акима"]')
    SELECT_0305 = (By.XPATH, '//*[text()="0305"]')
    CONFIRM = (By.XPATH, '//*[text()="Подтвердить"]')
    APP_C = (By.XPATH, '//*[@name="C"]')
    APP_D = (By.XPATH, '//*[@name="D"]')
    APP_E = (By.XPATH, '//*[@name="E"]')
    APP_F = (By.XPATH, '//*[@name="F"]')
    CONFIRMATION = (By.XPATH, '//*[text()="Я несу ответственность в соответствии с законами Республики Казахстан за '
                              'достоверность и полноту сведений,  приведенных в данном расчете."]')
    FORM = (By.XPATH, '//*[text()="Сформировать"]')