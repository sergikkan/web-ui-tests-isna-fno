from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
import logging


# этот базовый класс обслуживает базовые атрибуты для каждой отдельной страницы, унаследованной от класса Page
class BasePage(object):
    def __init__(self, browser, base_url='http://knp.isna.kz/'):
        self.browser = browser
        self.base_url = base_url
        self.timeout = 30

    '''Взаимодействие с браузером'''

    # Найти элемент по локатору
    def find_element(self, *locator):
        return self.browser.find_element(*locator)

    # Открыть страницу knp
    def open(self):
        self.browser.get(self.base_url)

    # Получить заглавие страницы
    def get_title(self):
        return self.browser.title

    # Получить юрл страницы
    def get_url(self):
        return self.browser.current_url

    # Навести элемент на локатор
    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.browser).move_to_element(element)
        hover.perform()

    # Ожидание элемента
    def wait_element(self, *locator):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))

    '''Скроллы'''

    def scroll(self, size):
        self.browser.execute_script('window.scroll(0,' + size + ')')

    # Скролл 200 px
    def scroll_200_px(self):
        self.browser.execute_script('window.scroll(0, 200)')

    # Скролл 500 px
    def scroll_500_px(self):
        self.browser.execute_script('window.scroll(0, 500)')

    # Скролл 700 px
    def scroll_700_px(self):
        self.browser.execute_script('window.scroll(0, 700)')

    # Скролл 900 px
    def scroll_900_px(self):
        self.browser.execute_script('window.scroll(0, 900)')

    # Скролл 900 px
    def scroll_1500_px(self):
        self.browser.execute_script('window.scroll(0, 1500)')

    def scroll_2000_px(self):
        self.browser.execute_script('window.scroll(0, 2000)')

    '''Проверки с заполнением различных значений'''

    # Проверка с заполнением поля значением "0"
    def check_zero_value_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys(0)
        sleep(0.3)
        try:
            assert '0' in self.browser.page_source
        except AssertionError as err:
            logging.info('Получили ошибку!')
            logging.error('Не удалось ввести 0 в поле, по ФЛК должно вводиться! Наименование поля: ' + name)
            raise err
        element.clear()

    # Проверка с заполнением поля с буквами
    def check_letter_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('mM')
        try:
            assert 'mM' not in self.browser.page_source
        except AssertionError as err:
            logging.info('Получили ошибку!')
            logging.error('Вводятся буквы в поле, по ФЛК поле не должно принимать буквы, наименование поля: ' + name)
            raise err
        element.clear()

    # Проверка с заполнением поля с запятой
    def check_special_symbol_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('111,13')
        try:
            assert '111,13' not in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает дробные значения, по флк не должно, наименование поле: ' + name)
            raise err

    # Проверка максимальное кол-во символов
    def max_symbol_1_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('12')
        sleep(0.5)
        try:
            assert '12' not in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 1 символов, ограничение по ФЛК: 1 символов, '
                              'наименование поля: ' + name)
            raise err
        try:
            assert '1' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает меньше 1 символов, максимальное ограчение по ФЛК: 1 символов,'
                              ' Наименование поля: ' + name)
            raise err
        element.clear()

    def max_symbol_2_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('123')
        sleep(0.5)
        try:
            assert '12' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает меньше 2 символов, максимальное ограчение по ФЛК: 2 символов,'
                              ' Наименование поля: ' + name)
            raise err
        element.clear()

    def max_symbol_3_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('4567')
        sleep(0.2)
        try:
            assert '4567' not in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 3 символов, ограничение по ФЛК: 3 символов, '
                              'наименование поля: ' + name)
            raise err
        try:
            assert '123' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает меньше 3 символов, максимальное ограчение по ФЛК: 3 символов,'
                              ' Наименование поля: ' + name)
            raise err
        element.clear()

    def max_symbol_4_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('12345')
        try:
            assert '12345' not in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 4 символов, ограничение по ФЛК: 4 символов, '
                              'наименование поля: ' + name)
            raise err
        try:
            assert '1234' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает меньше 4 символов, максимальное ограчение по ФЛК: 4 символов,'
                              ' Наименование поля: ' + name)
            raise err
        element.clear()

    def max_symbol_5_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('123456')
        sleep(0.3)
        try:
            assert '12345' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 5 символов, ограничение по ФЛК: 5 символов, '
                              'наименование поля: ' + name)
            raise err
        sleep(0.6)
        try:
            assert '123456' not in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 5 символов, максимальное ограчение по ФЛК: 5 символов,'
                              ' Наименование поля: ' + name)
            raise err

    def max_symbol_6_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('1234567')
        sleep(0.5)
        try:
            assert '1234567' not in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 6 символов, ограничение по ФЛК: 6 символов, '
                              'наименование поля: ' + name)
            raise err
        try:
            assert '123456' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает меньше 6 символов, максимальное ограчение по ФЛК: 6 символов,'
                              ' Наименование поля: ' + name)
            raise err
        element.clear()

    def max_symbol_7_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('12345678')
        sleep(0.4)
        try:
            assert '1234567' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает меньше 7 символов, максимальное ограчение по ФЛК: 7 символов,'
                              ' Наименование поля: ' + name)
            raise err
        try:
            assert '12345678' not in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 7 символов, ограничение по ФЛК: 7 символов, '
                              'наименование поля:' + name)
            raise err
        element.clear()

    def max_symbol_8_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('123456789')
        try:
            assert '12345678' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 8 символов, ограничение по ФЛК: 8 символов, '
                              'наименование поля: ' + name)
            raise err
        sleep(0.6)
        try:
            assert '123456789' not in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 8 символов, максимальное ограчение по ФЛК: 8 символов,'
                              ' Наименование поля: ' + name)
            raise err

    def max_symbol_9_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('1234567890')
        sleep(0.5)
        try:
            assert '1234567890' not in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 9 символов, ограничение по ФЛК: 15 символов, '
                              'наименование поля: ' + name)
            raise err
        try:
            assert '123456789' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает меньше 9 символов, максимальное ограчение по ФЛК: 15 символов,'
                              ' Наименование поля: ' + name)
            raise err
        element.clear()

    def max_symbol_10_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('12345678901')
        sleep(0.3)
        try:
            assert '1234567890' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 10 символов, ограничение по ФЛК: 10 символов, '
                              'наименование поля: ' + name)
            raise err
        try:
            assert '12345678901' not in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 10 символов, максимальное ограчение по ФЛК: 10 символов,'
                              ' Наименование поля: ' + name)
            raise err

    def max_symbol_12_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('1234567890123')
        sleep(0.4)
        try:
            assert '123456789012' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает меньше 12 символов, максимальное ограчение по ФЛК: 14 символов,'
                              ' Наименование поля: ' + name)
            raise err
        try:
            assert '1234567890123' not in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 12 символов, ограничение по ФЛК: 12 символов, '
                              'наименование поля:' + name)
            raise err
        element.clear()

    def max_symbol_14_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('123456789012345')
        sleep(0.7)
        try:
            assert '12345678901234' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает меньше 14 символов, максимальное ограчение по ФЛК: 14 символов,'
                              ' Наименование поля: ' + name)
            raise err
        try:
            assert '123456789012345' not in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 14 символов, ограничение по ФЛК: 14 символов, '
                              'наименование поля:' + name)
            raise err
        element.clear()

    def max_symbol_15_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('1234567890123456')
        sleep(0.2)
        try:
            assert '123456789012345' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 15 символов, ограничение по ФЛК: 15 символов, '
                              'наименование поля: ' + name)
            raise err
        sleep(0.6)
        try:
            assert '1234567890123456' not in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 15 символов, максимальное ограчение по ФЛК: 15 символов,'
                              ' Наименование поля: ' + name)
            raise err
        element.clear()

    def max_symbol_16_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('12345678901234567')
        sleep(0.2)
        try:
            assert '1234567890123456' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 16 символов, ограничение по ФЛК: 16 символов, '
                              'наименование поля: ' + name)
            raise err
        sleep(0.6)
        try:
            assert '12345678901234567' not in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 16 символов, максимальное ограчение по ФЛК: 16 символов,'
                              ' Наименование поля: ' + name)
            raise err
        element.clear()

    def max_symbol_18_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('1234567890123456789')
        sleep(0.5)
        try:
            assert '1234567890123456789' not in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает меньше 18 символов, максимальное ограчение по ФЛК: 18 символов,'
                              ' Наименование поля: ' + name)
            raise err
        try:
            assert '123456789012345678' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 18 символов, ограничение по ФЛК: 18 символов, '
                              'наименование поля: ' + name)
            raise err
        element.clear()

    def max_symbol_20_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('123456789012345678901')
        sleep(0.4)
        try:
            assert '12345678901234567890' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает меньше 20 символов, максимальное ограчение по ФЛК: 20 символов,'
                              ' Наименование поля: ' + name)
            raise err
        try:
            assert '123456789012345678901' not in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 20 символов, ограничение по ФЛК: 20 символов, '
                              'наименование поля:' + name)
            raise err
        element.clear()

    def max_symbol_24_input(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('1234567890123456789012345')
        sleep(0.5)
        try:
            assert '123456789012345678901234' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает больше 24 символов, ограничение по ФЛК: 24 символов, '
                              'наименование поля: ' + name)
            raise err
        sleep(0.6)
        try:
            assert '1234567890123456789012345' not in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает меньше 24 символов, максимальное ограчение по ФЛК: 18 символов,'
                              ' Наименование поля: ' + name)
            raise err
        element.clear()

    # Проверка максимальное кол-во символов 9
    def max_symbol_9_input_fractional_number(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('123,1234567890')
        try:
            assert '123,1234567890' not in self.browser.page_source
        except AssertionError as err:
            logging.info('Получили ошибку!')
            logging.error('Поле принимает больше 9 символов + дробь в виде запятой, наименование поля: ' + name)
            raise err
        try:
            assert '123,123456789' in self.browser.page_source
        except AssertionError as err:
            logging.info('Получили ошибку!')
            logging.error('Поле не принимает больше 9 символов + дробь в виде запятой, наименование поля: ' + name)
            raise err

        element.clear()

    '''Боковой степпер'''

    # Боковй степпер проверка отрицательно
    def side_stepper_false(self):
        self.find_element(By.XPATH, '//*[@data-icon="close"]')

    # Боковй степпер проверка положительно
    def side_stepper_true(self):
        self.find_element(By.XPATH, '//*[@data-icon="check"]')

    def activate_stepper(self):
        self.hover(By.XPATH, '//div[@class="ant-steps ant-steps-vertical steps"]')

    def side_stepper_go_to_first_page(self):
        self.activate_stepper()
        sleep(1)
        self.find_element(By.XPATH, '//*[text()="Общая информация"]').click()

    '''Заполнение полей с различными значениями'''

    # Заполнение поля со словами
    def check_data_type_string(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('AutomatedTest')
        try:
            assert 'AutomatedTest' in self.browser.page_source
        except AssertionError as err:
            logging.info('Получили ошибку!')
            logging.error('Поле не принимает символы в виде букв, по ФЛК должно, наименование поля: ' + name)
            raise err
        element.clear()

    def check_data_type_special_symbol(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys(',!')
        try:
            assert ',!' in self.browser.page_source
        except AssertionError as err:
            logging.info('Получили ошибку!')
            logging.error('Не вводятся специальные символы ,!, по ФЛК должно наименование поля: ' + name)
            raise err
        element.clear()

    # Заполнение поля с 10000
    def check_data_type_whole_numbers_10000(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('10000')
        try:
            assert '10000' in self.browser.page_source
        finally:
            if AssertionError:
                logging.info('Получили ошибку!')
                logging.error('Не вводятся символы "10000" в элементе' + name)
        element.clear()

    # Заполнение поля с 5000
    def check_data_type_whole_numbers_5000(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('5000')
        try:
            assert '5000' in self.browser.page_source
        finally:
            if AssertionError:
                logging.info('Получили ошибку!')
                logging.error('Не вводятся символы "5000" в элементе' + name)
        element.clear()

    # Заполнение поля с дробными числами
    def check_data_type_fractional_numbers(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('50,5')
        sleep(0.7)
        try:
            assert '50,5' in self.browser.page_source
        except AssertionError as err:
            logging.error('Получили ошибку!')
            logging.exception('Поле принимает меньше 9 символов, максимальное ограчение по ФЛК: 15 символов,'
                              ' Наименование поля: ' + name)
            raise err
        element.clear()

    # Заполнение поля с отрицательными значениями (Не должна выйти ошибка)
    def check_data_type_negative_numbers_allow(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('-500')
        sleep(0.3)
        try:
            assert '-500' in self.browser.page_source
        except AssertionError as err:
            logging.info('Получили ошибку!')
            logging.error('Не вводятся отрицательные числа в поле, по ФЛК должны, наименование поля: ' + name)
            raise err
        try:
            assert 'Поле не может быть отрицательным' not in self.browser.page_source
        except AssertionError as err:
            logging.info('Получили ошибку!')
            logging.error('Выходит ошибка "Поле не может быть отрицательным". по ФЛК поле должно принимать '
                          'отрицатеьные числа, наименование поля: ' + name)
            raise err
        element.clear()

    # Заполнение поля с отрицательными цифрами (Должна выйти ошибка)
    def check_data_type_negative_numbers_ban(self, *locator, name):
        element = self.find_element(*locator)
        element.send_keys('-500')
        sleep(0.3)
        try:
            assert '-500' not in self.browser.page_source
        finally:
            if AssertionError:
                logging.info('Получили ошибку!')
                logging.error('Вводятся отрицательные числа в элементе' + name)
        try:
            assert 'Поле не может быть отрицательным' in self.browser.page_source
        finally:
            if AssertionError:
                logging.info('Получили ошибку!')
                logging.error('Вводятся отрицательные числа в элементе' + name)
        element.clear()

    '''Доп. проверки'''

    # Проверка без заполнения кода ОГД
    def check_without_filling_ogd_code(self):
        self.browser.find_element(By.XPATH, '//button[@disabled]').is_displayed()

    '''Взаимодействие с различными элементами на странице ФНО'''

    def after_button_click(self):
        self.browser.find_element(By.XPATH, '//*[text()="Далее"]').click()

    # Нерезидент РК
    def residention_false_check(self):
        residention_select = self.browser.find_element(By.XPATH, '//div[@class="ant-select ant-select-lg select'
                                                                 ' ant-select-single ant-select-show-arrow"]')
        residention_select.click()
        sleep(0.5)
        select_residention_false = self.browser.find_element(By.XPATH, '//*[text()="Нерезидент РК"]')
        select_residention_false.click()
        assert 'Код страны резидентства' in self.browser.page_source
        assert 'Номер налоговой регистрации' in self.browser.page_source

    # Нерезидент ПРОСТО
    def residention_false_check_second(self):
        residention_select = self.browser.find_element(By.XPATH, '//div[@class="ant-select ant-select-lg select'
                                                                 ' ant-select-single ant-select-show-arrow"]')
        residention_select.click()
        sleep(0.5)
        select_residention_false = self.browser.find_element(By.XPATH, '//*[text()="Нерезидент"]')
        select_residention_false.click()
        assert 'Код страны резидентства' in self.browser.page_source
        assert 'Номер налоговой регистрации' in self.browser.page_source

    # Дополнительный по уведомлению
    def declaration_type_additional_with_notification(self):
        declaration_type_select = self.browser.find_element(By.XPATH, '//div[@name = "declarationTypes"]')
        declaration_type_select.click()
        sleep(0.5)
        select_additional_with_notification = self.browser.find_element(By.XPATH, '//*[text()="Д'
                                                                                  'ополнительный по уведомлению"]')
        select_additional_with_notification.click()
        declaration_type_select.click()
        notification_number = self.browser.find_element(By.XPATH, '//input[@maxlength="20"]')
        notification_number.send_keys('123456789012345678901')
        sleep(0.3)
        assert '12345678901234567890' in self.browser.page_source
        assert '123456789012345678901' not in self.browser.page_source
        notification_number.clear()

    # Дополнительная по уведомлению
    def declaration_type_additional_with_notification_second(self):
        declaration_type_select = self.browser.find_element(By.XPATH, '//div[@name = "declarationTypes"]')
        declaration_type_select.click()
        sleep(0.5)
        select_additional_with_notification = self.browser.find_element(By.XPATH, '//*[text()="Д'
                                                                                  'ополнительная по уведомлению"]')
        select_additional_with_notification.click()
        declaration_type_select.click()
        notification_number = self.browser.find_element(By.XPATH, '//input[@maxlength="20"]')
        notification_number.send_keys('123456789012345678901')
        sleep(0.3)
        assert '12345678901234567890' in self.browser.page_source
        assert '123456789012345678901' not in self.browser.page_source

    # Активация подсказок
    def activate_promt(self):
        promt_slider = (By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[2]/div')
        promt_activate_button = (By.XPATH, '//button[@role="switch"]')
        element = self.browser.find_element(By.XPATH, promt_slider)
        hover = ActionChains(self.browser).move_to_element(element)
        hover.perform()
        self.browser.find_element(By.XPATH, promt_activate_button).click()

    # Проверка названия поля по ФЛК
    def assert_field_name_flk(self, text):
        sleep(1)
        try:
            assert text in self.browser.page_source
        finally:
            if AssertionError:
                logging.info('Получили ошибку!')
                logging.error('f'f'Не удалось обнаружить название поля {text}, '
                              'проверьте ФЛК и название поля на странице')

    def assert_calculation(self, value):
        sleep(1)
        try:
            assert value in self.browser.page_source
        finally:
            if AssertionError:
                logging.info('Получили ошибку!')
                logging.error('f'f'Проверьте калькуляцию должно было выйти значение: {value}')
