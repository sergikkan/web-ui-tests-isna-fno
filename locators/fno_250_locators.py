from selenium.webdriver.common.by import By


class FNO250LocatorsName(object):
    NOTICE_NUMBER = 'Номер уведомления'
    PHONE_NUMBER = 'Номер телефона'
    E_MAIL = 'Электронный адрес'
    FIRST_PAGE_C = 'C Сумма'
    APP_1_B_1 = 'B Вид недвижимого имущества'
    APP_1_D_1 = 'D Идентификационный (кадастровый) номер'
    APP_1_E_1 = 'E Место нахождения (адрес)'

    APP_1_B_2 = 'B Вид транспорта'
    APP_1_C_2 = 'C Марка, модель'
    APP_1_E_2 = 'E Идентификационный (государственный) номер'
    APP_1_F_2 = 'F VIN-код (номер кузова)'

    APP_2_B_1 = 'B Идентификационный номер банковского учреждения'
    APP_2_C_1 = 'C Наименование банковского учреждения'
    APP_2_F_1 = 'F Сумма'

    APP_2_B_2 = 'BИдентификационный номер юридического лица'
    APP_2_C_2 = 'CНаименование юридического лица'
    APP_2_E_2 = 'EРазмер доли участия'

    APP_3_B_1 = 'BИдентификационный номер застройщика'
    APP_3_C_1 = 'CНаименование застройщика'
    APP_3_E_1 = 'EМесто нахождения (адрес)'
    APP_3_G_1 = 'GСумма'

    APP_3_B_2 = 'BВес золота'
    APP_3_E_2 = 'EСумма'

    APP_4_B_1 = 'BКоличество ценных бумаг, ПФИ принадлежащих подателю декларации'
    APP_4_E_1 = 'EЦена приобретения одной ценной бумаги, ПФИ'

    APP_4_B_2 = 'BКоличество паев принадлежащих подателю декларации'
    APP_4_E_2 = 'EНоминальная стоимость пая за единицу'

    APP_5_B_1 = 'B Вид объекта интелектуальной собственности'
    APP_5_C_1 = 'CНомер патента'

    APP_5_B_2 = 'BНаименование имущества (объекта)'
    APP_5_C_2 = 'CКоличество'
    APP_5_F_2 = 'FОценочная стоимость имущества (объекта)'

    APP_6_C_1 = 'CИдентификационный номер дебитора/кредитора'
    APP_6_D_1 = 'DФ.И.О./наименование дебитора/кредитора'
    APP_6_G_1 = 'GСумма задолженности'

    APP_6_B_2 = 'BНаименование имущества'
    APP_6_C_2 = 'CИдентификационный номер имущества'
    APP_6_D_2 = 'DИдентификационный номер ИИН/БИН доверительного управления'


class FNO250Locators(object):
    # Выбор налогового периода
    CATEGORY = (By.XPATH, '//*[@role="combobox"]')
    SELECT_CATEGORY = (By.XPATH, '//*[text()="1A"]')
    SEND_TAX_PERIOD = (By.XPATH, '//*[text()="Подать"]')
    # ПЕРВАЯ СТРАНИЦА
    DECLARATION_TYPE = (By.XPATH, '//*[@name="declarationTypes"]')
    DECLARATION_TYPE_SELECT = (By.XPATH, '//*[@title="Дополнительная по уведомлению"]')
    CONTROL_TEXT = (By.XPATH, '//*[text()="Вид декларации"]')
    NOTICE_NUMBER = (By.XPATH, '//*[@name="noticeNumber"]')
    NOTICE_DATE = (By.XPATH, '//*[@name="noticeDate"]')
    NOTICE_DATE_SELECT = (By.XPATH, '//*[@class="ant-picker-cell ant-picker-cell-in-view ant-picker-cell-today"]')
    RESIDENTION = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div[6]/div[1]/div/div/div[2]/div['
                             '1]/div/div/div')
    RESIDENTION_SELECT = (By.XPATH, '//*[@title="Резидент РК"]')
    PHONE_NUMBER = (By.XPATH, '//*[@name="fnoContent.commonInfo._4_1"]')
    E_MAIL = (By.XPATH, '//*[@name="fnoContent.commonInfo._4_2"]')
    CONFIRMATION_1 = (By.XPATH, '//*[@name="app_01"]')
    CONFIRMATION_2 = (By.XPATH, '//*[@name="app_02"]')
    CONFIRMATION_3 = (By.XPATH, '//*[@name="app_03"]')
    CONFIRMATION_4 = (By.XPATH, '//*[@name="app_04"]')
    CONFIRMATION_5 = (By.XPATH, '//*[@name="app_05"]')
    CONFIRMATION_6 = (By.XPATH, '//*[@name="app_06"]')
    CONFIRMATION_7 = (By.XPATH, '//*[@name="app_07"]')
    CONFIRMATION_8 = (By.XPATH, '//*[@name="app_08"]')
    CONFIRMATION_9 = (By.XPATH, '//*[@name="app_09"]')
    CONFIRMATION_10 = (By.XPATH, '//*[@name="app_10"]')
    CONFIRMATION_11 = (By.XPATH, '//*[@name="app_11"]')
    CONFIRMATION_12 = (By.XPATH, '//*[@name="app_12"]')
    ADD_STR = (By.XPATH, '//*[text() = "Добавить строку"]')
    CANCEL_ADD_STR = (By.XPATH, '//*[text() = "Отменить"]')
    FIRST_PAGE_B = (By.XPATH, '//*[@name="B"]')
    FIRST_PAGE_B_SELECT = (By.XPATH, '//*[@label="Австралийский доллар"]')
    FIRST_PAGE_C = (By.XPATH, '//*[@name="C"]')
    ADD = (By.XPATH, '//*[text() = "Добавить"]')
    AFTER = (By.XPATH, '//*[text()="Далее"]')
    APP_1_B_1 = (By.XPATH, '//*[@name="B"]')
    APP_1_C_1 = (By.XPATH, '//*[@name="C"]')
    APP_1_C_1_SELECT = (By.XPATH, '//*[@label="Республика македония"]')
    APP_1_D_1 = (By.XPATH, '//*[@name="D"]')
    APP_1_E_1 = (By.XPATH, '//*[@name="E"]')

    APP_1_B_2 = (By.XPATH, '//*[@name="B"]')
    APP_1_C_2 = (By.XPATH, '//*[@name="C"]')
    APP_1_D_2 = (By.XPATH, '//*[@name="D"]')
    APP_1_D_2_SELECT = (By.XPATH, '//*[@label="Республика македония"]')
    APP_1_E_2 = (By.XPATH, '//*[@name="E"]')
    APP_1_F_2 = (By.XPATH, '//*[@name="F"]')

    APP_2_B_1 = (By.XPATH, '//*[@name="B"]')
    APP_2_C_1 = (By.XPATH, '//*[@name="C"]')
    APP_2_D_1 = (By.XPATH, '//*[@name="D"]')
    APP_2_D_1_SELECT = (By.XPATH, '//*[@label="Республика македония"]')
    APP_2_E_1 = (By.XPATH, '//*[@name="E"]')
    APP_2_E_1_SELECT = (By.XPATH, '//*[@label="Австралийский доллар"]')
    APP_2_F_1 = (By.XPATH, '//*[@name="F"]')

    APP_2_B_2 = (By.XPATH, '//*[@name="B"]')
    APP_2_C_2 = (By.XPATH, '//*[@name="C"]')
    APP_2_D_2 = (By.XPATH, '//*[@name="D"]')
    APP_2_D_2_SELECT = (By.XPATH, '//*[@label="Республика македония"]')
    APP_2_E_2 = (By.XPATH, '//*[@name="E"]')

    APP_3_B_1 = (By.XPATH, '//*[@name="B"]')
    APP_3_C_1 = (By.XPATH, '//*[@name="C"]')
    APP_3_D_1 = (By.XPATH, '//*[@name="D"]')
    APP_3_D_1_SELECT = (By.XPATH, '//*[@label="Республика македония"]')
    APP_3_E_1 = (By.XPATH, '//*[@name="E"]')
    APP_3_F_1 = (By.XPATH, '//*[@name="F"]')
    APP_3_F_1_SELECT = (By.XPATH, '//*[@label="Австралийский доллар"]')
    APP_3_G_1 = (By.XPATH, '//*[@name="G"]')

    APP_3_B_2 = (By.XPATH, '//*[@name="B"]')
    APP_3_C_2 = (By.XPATH, '//*[@name="C"]')
    APP_3_C_2_SELECT = (By.XPATH, '//*[@label="Республика македония"]')
    APP_3_D_2 = (By.XPATH, '//*[@name="D"]')
    APP_3_D_2_SELECT = (By.XPATH, '//*[@label="Австралийский доллар"]')
    APP_3_E_2 = (By.XPATH, '//*[@name="E"]')

    APP_4_B_1 = (By.XPATH, '//*[@name="B"]')
    APP_4_C_1 = (By.XPATH, '//*[@name="C"]')
    APP_4_C_1_SELECT = (By.XPATH, '//*[@label="Республика македония"]')
    APP_4_D_1 = (By.XPATH, '//*[@name="D"]')
    APP_4_D_1_SELECT = (By.XPATH, '//*[@label="Австралийский доллар"]')
    APP_4_E_1 = (By.XPATH, '//*[@name="E"]')

    APP_4_B_2 = (By.XPATH, '//*[@name="B"]')
    APP_4_C_2 = (By.XPATH, '//*[@name="C"]')
    APP_4_C_2_SELECT = (By.XPATH, '//*[@label="Республика македония"]')
    APP_4_D_2 = (By.XPATH, '//*[@name="D"]')
    APP_4_D_2_SELECT = (By.XPATH, '//*[@label="Австралийский доллар"]')
    APP_4_E_2 = (By.XPATH, '//*[@name="E"]')

    APP_5_B_1 = (By.XPATH, '//*[@name="B"]')
    APP_5_C_1 = (By.XPATH, '//*[@name="C"]')
    APP_5_D_1 = (By.XPATH, '//*[@name="D"]')
    APP_5_D_1_SELECT = (By.XPATH, '//*[@label="Республика македония"]')
    APP_5_E_1 = (By.XPATH, '//*[@name="E"]')
    TODAY = (By.XPATH, '//*[@class="ant-picker-today-btn"]')

    APP_5_B_2 = (By.XPATH, '//*[@name="B"]')
    APP_5_C_2 = (By.XPATH, '//*[@name="C"]')
    APP_5_D_2 = (By.XPATH, '//*[@name="D"]')
    APP_5_D_2_SELECT = (By.XPATH, '//*[@label="Республика македония"]')
    APP_5_E_2 = (By.XPATH, '//*[@name="E"]')
    APP_5_E_2_SELECT = (By.XPATH, '//*[@label="Австралийский доллар"]')
    APP_5_F_2 = (By.XPATH, '//*[@name="F"]')

    APP_6_B_1 = (By.XPATH, '//*[@name="B"]')
    APP_6_B_1_SELECT = (By.XPATH, '//*[@label="Дебиторская"]')
    APP_6_C_1 = (By.XPATH, '//*[@name="C"]')
    APP_6_D_1 = (By.XPATH, '//*[@name="D"]')
    APP_6_E_1 = (By.XPATH, '//*[@name="E"]')
    APP_6_E_1_SELECT = (By.XPATH, '//*[@label="Республика македония"]')
    APP_6_F_1 = (By.XPATH, '//*[@name="F"]')
    APP_6_F_1_SELECT = (By.XPATH, '//*[@label="Австралийский доллар"]')
    APP_6_G_1 = (By.XPATH, '//*[@name="G"]')

    APP_6_B_2 = (By.XPATH, '//*[@name="B"]')
    APP_6_C_2 = (By.XPATH, '//*[@name="C"]')
    APP_6_D_2 = (By.XPATH, '//*[@name="D"]')
    APP_6_E_2 = (By.XPATH, '//*[@name="E"]')
    APP_6_F_2 = (By.XPATH, '//*[@name="F"]')
