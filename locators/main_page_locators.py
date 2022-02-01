from selenium.webdriver.common.by import By

'''Локаторы в главной странице'''
class MainPageLocatorsName(object):
    SEND_DOC_BUTTON = 'Подать документ'
    INPUT_SEARCH = 'Поиск'
    FIRST_RESULT_AFTER_SEARCH = 'Первый документ поиска'
    LOGIN_BUTTON_MAINPAGE = 'Войти'
    PROMT = ''
    PROMT_ACTIVATE = ''
    CHANGE_PROFILE = 'Изменить профиль'
    SELECT_FIZ_PROFILE = 'Физическое лицо'
    HALF_YEAR_SELECT = 'Квартал'
    FIRST_HALF_YEAR = 'Первый квартал'
    INPUT_YEAR = 'Годовой период'
    SELECT_YEAR_2020 = 'Выбор "2020" '
    SEND_TAX_PERIOD = 'Подать'
    ACTIVATE_SLIDER = 'Активация слайдера'
    FIRST_PAGE = 'Общая информация'


class MainPageLocators(object):
    SEND_DOC_BUTTON = (By.XPATH, '//span[text()="Подать документ"]')
    INPUT_SEARCH = (By.XPATH, '//input[@name="search"]')
    FIRST_RESULT_AFTER_SEARCH = (By.XPATH, '//span[@class="documents__text-document"]')
    LOGIN_BUTTON_MAINPAGE = (By.XPATH, '//*[text()=\'Войти\']')
    PROMT = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div[2]/div')
    PROMT_ACTIVATE = (By.XPATH, '//button[@role="switch"]')
    CHANGE_PROFILE = (By.XPATH, "//div[@class=\"home-profile__box\"]")
    SELECT_FIZ_PROFILE = (By.XPATH, "//*[text()=\"Физическое лицо\"]")
    # ВЫБОР НАЛОГОВОГО ПЕРИОДА
    HALF_YEAR_SELECT = (By.XPATH, '//div[@class="ant-select-selector"]')
    FIRST_HALF_YEAR = (By.XPATH, '//div[@class = "ant-select-item-option-content"][1]')
    INPUT_YEAR = (By.XPATH, '//*[@placeholder="Год"]')
    SELECT_YEAR_2020 = (By.XPATH, '//td[@title="2020"]')
    DATE_SELECT = (By.XPATH, '//*[@placeholder="Дата"]')
    DATE_SELECT_TODAY = (By.XPATH, '//*[text()="Сегодня"]')
    SEND_TAX_PERIOD = (By.XPATH, '//*[text()=\'Подать\']')
    # СЛАЙДЕР СЛЕВА ПЕРЕКЛЮЧЕНИЕ МЕЖДУ СТРАНИЦАМИ
    ACTIVATE_SLIDER = (By.XPATH, '//div[@class="ant-steps ant-steps-vertical steps"]')
    FIRST_PAGE = (By.XPATH, '//*[text()="Общая информация"]')
    # Подача документа
    SEND_DOC_1 = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div/div[4]/div/div/div/div/div/table/tbody/tr[2]/td[3]/div/svg')
    SEND_DOC_2 = (By.XPATH, '//*[@class="ant-dropdown-menu-title-content" and text()="Подать документ"]')
    # 860
    SELECT_860 = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div/div[4]/div/div/div/div/div/table/tbody/tr[2]/td[2]/span')
    SELECT_421 = (By.XPATH, '//*[text()="421.00 Расчет акциза за структурное подразделение или объекты, связанные с налогообложением"]')