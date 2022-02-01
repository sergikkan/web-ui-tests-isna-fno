from selenium.webdriver.common.by import By


class FNO_500_Locators_Name(object):
    # ПРИЛОЖЕНИЕ 1
    # Сырая нефть
    OIL_1 = '500.01.001 Годовой объем добычи сырой нефти'
    OIL_2 = '500.01.002 Объем добытой сырой нефти за налоговый период'
    OIL_3 = '500.01.003 Средняя цена реализации сырой нефти'
    OIL_4 = '500.01.004 Фактические затраты на добычу сырой нефти'
    OIL_5 = '500.01.005 Налоговая база'
    OIL_6 = '500.01.006 Корректировка налоговой базы в соответствии с Законом о трансфертном ценообразовании'
    OIL_8 = '500.01.008 Ставка'
    OIL_9 = '500.01.009 Начислено роялти на сырую нефть'
    OIL_10 = '500.01.010 Корректировка'
    OIL_11 = '500.01.011 Сумма роялти на сырую нефть, подлежащая уплате'
    # Газовый конденсат
    GAS_1 = '500.01.012 Годовой объем добычи газового конденсата'
    GAS_2 = '500.01.013 Объем добытого газового конденсата за налоговый период'
    GAS_3 = '500.01.014 Средняя цена реализации газового конденсата'
    GAS_4 = '500.01.015 Фактические затраты на добычу газового конденсата'
    GAS_5 = '500.01.016 Налоговая база'
    GAS_6 = '500.01.017 Корректировка налоговой базы в соответствии с Законом о трансфертном ценообразовании'
    GAS_8 = '500.01.019 Ставка'
    GAS_9 = '500.01.020 Начислено роялти на газовый конденсат'
    GAS_10 = '500.01.021 Корректировка'
    GAS_11 = '500.01.022 Сумма роялти на газовый конденсат, подлежащая уплате'
    # Природный газ
    NATURE_GAS_1 = '500.01.023 Годовой объем добычи природного газа'
    NATURE_GAS_2 = '500.01.024 Объем добытого природного газа за налоговый период'
    NATURE_GAS_3 = '500.01.025 Средняя цена реализации природного газа'
    NATURE_GAS_4 = '500.01.026 Фактические затраты на добычу природного газа'
    NATURE_GAS_5 = '500.01.027 Налоговая база'
    NATURE_GAS_6 = '500.01.028 Корректировка налоговой базы в соответствии с Законом о трансфертном ценообразовании'
    NATURE_GAS_8 = '500.01.030 Ставка'
    NATURE_GAS_9 = '500.01.031 Начислено роялти за природный газ'
    NATURE_GAS_10 = '500.01.032 Корректировка'
    NATURE_GAS_11 = '500.01.033 Сумма роялти на природный газ, подлежащая уплате'
    # Подземные воды
    WATER_1 = '500.01.034 Объем добытых подземных вод за налоговый период'
    WATER_2 = '500.01.035 Налоговая база'
    WATER_3 = '500.01.036 Ставка'
    WATER_4 = '500.01.037 Сумма роялти по подземным водам, подлежащая уплате'

    # 2 ПРИЛОЖЕНИЕ
    SECOND_APP_1 = '500.02.001 Достигнутый уровень добычи'
    SECOND_APP_2 = '500.02.002 Сумма бонуса добычи'
    SECOND_APP_3 = '500.02.003 Сумма бонуса с начала года'
    SECOND_APP_4 = '500.02.004 Сумма бонуса за текущий налоговый период'

    # 3 ПРИЛОЖЕНИЕ
    # До 1 января 2004 года
    THIRD_APP_1 = '500.03.001 Общий объем добытой продукции'
    THIRD_APP_2 = '500.03.002 Общий объем реализованный продукции'
    THIRD_APP_3 = '500.03.003 Общая стоимость реализованный продукции'
    THIRD_APP_6 = '500.03.006 Сумма уплаченного роялти'
    THIRD_APP_8 = '500.03.008 Корректировка стоимости продукции, подлежащая распределению на компенсационную и ' \
                  'прибыльную в соответствии с Законом о трансфертном ценообразовании '
    THIRD_APP_12 = '500.03.012 Ставка доли республики по разделу продукции (%)'
    THIRD_APP_14 = '500.03.014 Начислено процентов банка'
    # После 1 января 2005 года
    THIRD_APP_15 = '500.03.015 Общий объем добытой продукции'
    THIRD_APP_17 = '500.03.017 Доход от корректировки в соответствии с Законом о трансфертном ценообразовании'
    THIRD_APP_19 = '500.03.019 Общий объем реализованной продукции'
    THIRD_APP_22 = '500.03.022 Доля компенсационной продукции'
    THIRD_APP_23 = '500.03.023 Объем компенсационной продукции'
    THIRD_APP_26 = '500.03.026 R-фактор (показатель доходности), единиц'
    THIRD_APP_27 = '500.03.027 BHP (внутренняя норма рентабельности), %'
    THIRD_APP_28 = '500.03.028 Р-фактор (ценовой коэффициент), долларов США'
    THIRD_APP_29 = '500.03.029 Доля недропользователя в прибыльной продукции %'
    THIRD_APP_30 = '500.03.030 Доля недропользователя в прибыльной продукции'

    # 4 ПРИЛОЖЕНИЕ
    B_APP_4 = 'B РНН/Код страны резидентства'
    C_APP_4 = 'C Объем реализованной продукции'
    D_APP_4 = 'D Цена реализации'
    E_APP_4 = 'E Доход от реализации'

    # 5 ПРИЛОЖЕНИЕ
    B_APP_5 = 'B Наименование показателей'
    C_APP_5 = 'C Сумма'

    # 6 ПРИЛОЖЕНИЕ
    SIXTH_APP_1 = '500.06.001 Затраты, подлежащие возмещению за счет компенсационной продукции на начало отчетного ' \
                  'налогового периода '
    SIXTH_APP_2 = "500.06.002Фактически произведенные затраты, подлежащие возмещению за счет компенсационной " \
                  "продукции за отчетный налоговый период "
    SIXTH_APP_4 = '500.06.004Сумма, начисленная на остаток невозмещенных затрат на начало отчетного налогового периода'
    SIXTH_APP_5 = '500.06.005 Затраты, возмещаемые за счет компенсационной продукции в отчетный налоговый период'
    SIXTH_APP_7 = '500.06.007 Возмещаемые затраты, не возмещенные недропользователю на начало налогового периода'
    SIXTH_APP_8 = '500.06.008 Возмещаемые затраты, фактически произведенные в отчетном налоговом периоде'
    SIXTH_APP_9 = '500.06.009 Возмещаемые затраты, фактически возмещенные за счет компенсационной продукции'

    # 7 ПРИЛОЖЕНИЕ
    SEVEN_APP_1 = '500.07.001 Объем добытой нефти'
    SEVEN_APP_2 = '500.07.002 Цена нефти'
    SEVEN_APP_4 = '500.07.004 Сумма дополнительного платежа по нефти'
    SEVEN_APP_5 = '500.07.005Объем добытого газа'
    SEVEN_APP_6 = '500.07.006 Цена газа'
    SEVEN_APP_8 = '500.07.008 Сумма дополнительного платежа по газу'
    SEVEN_APP_9 = '500.07.009 Объем добытых прочих полезных ископаемых'
    SEVEN_APP_10 = '500.07.010 Цена добытых прочих полезных ископаемых'
    SEVEN_APP_12 = '500.07.012 Сумма дополнительного платежа по прочим полезным ископаемым'
    SEVEN_APP_13 = '500.07.013 Ставка (справочно)'
    SEVEN_APP_15 = '500.07.015 Иные виды платежей, предусмотренные соглашением (контрактом) о разделе продукции'


# 1 СТРАНИЦА
# Раздел. Общая информация о налогоплательщике
class FNO_500_Locators(object):
    DECLARATION_TYPE = (By.XPATH, '//*[@name="declarationTypes"]')
    DECLARATION_TYPE_SELECT = (By.XPATH, '//*[@title="Первоначальная"]')

    CONTRACT_NAME = (By.XPATH, '//*[@name="fnoContent.commonInfo._7"]')
    CONTRACT_NUMBER = (By.XPATH, '//*[@name="fnoContent.commonInfo._10"]')
    CONTRACT_DATE = (By.XPATH, '//*[@name="fnoContent.commonInfo._9"]')
    CONTRACT_DATE_SELECT_BEFORE_2005_1 = (By.XPATH, '//*[text()="2007"]')
    CONTRACT_DATE_SELECT_BEFORE_2005_2 = (By.XPATH, '//*[text()="2001"]')
    CONTRACT_DATE_SELECT_BEFORE_2005_3 = (By.XPATH, '//*[text()="6"]')
    CONTRACT_DATE_SELECT_AFTER_2005 = (By.XPATH, '//*[text()="15"]')
    CODE = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div[6]/div[1]/div/div/div[2]/div['
                      '1]/div/span/div[1]/div/span[1]')
    CODE_SELECT = (By.XPATH, '//*[text()="0002"]')
    UNIT = (By.XPATH, '//*[@name="fnoContent.commonInfo._11"]')
    APPS = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div[8]/div/div[1]/div/div/div[1]/div/div/div')
    APPS_SELECT_ALL = (By.XPATH, '//*[text()="Выбрать все"]')
    CONTROL_TEXT2 = (By.XPATH, '//*[text() = "© 2021 Комитет государственных доходов МФ РК"]')
    AFTER = (By.XPATH, '//*[text()="Далее"]')

    # ПРИЛОЖЕНИЕ 1
    CHAPTER_1 = (By.XPATH, '//*[@name="fnoContent.application_01.fossilOil"]')
    CHAPTER_2 = (By.XPATH, '//*[@name="fnoContent.application_01.gasCondensate"]')
    CHAPTER_3 = (By.XPATH, '//*[text()="Природный газ"]')
    CHAPTER_4 = (By.XPATH, '//*[text()="Подземные воды"]')
    # Сырая нефть
    OIL_1 = (By.XPATH, '//*[@name="fnoContent.application_01._001"]')
    OIL_2 = (By.XPATH, '//*[@name="fnoContent.application_01._002"]')
    OIL_3 = (By.XPATH, '//*[@name="fnoContent.application_01._003"]')
    OIL_4 = (By.XPATH, '//*[@name="fnoContent.application_01._004"]')
    OIL_5 = (By.XPATH, '//*[@name="fnoContent.application_01._005"]')
    OIL_6 = (By.XPATH, '//*[@name="fnoContent.application_01._006"]')

    OIL_8 = (By.XPATH, '//*[@name="fnoContent.application_01._008"]')
    OIL_9 = (By.XPATH, '//*[@name="fnoContent.application_01._009"]')
    OIL_10 = (By.XPATH, '//*[@name="fnoContent.application_01._010"]')
    OIL_11 = (By.XPATH, '//*[@name="fnoContent.application_01._011"]')

    # Газовый конденсат
    GAS_1 = (By.XPATH, '//*[@name="fnoContent.application_01._012"]')
    GAS_2 = (By.XPATH, '//*[@name="fnoContent.application_01._013"]')
    GAS_3 = (By.XPATH, '//*[@name="fnoContent.application_01._014"]')
    GAS_4 = (By.XPATH, '//*[@name="fnoContent.application_01._015"]')
    GAS_5 = (By.XPATH, '//*[@name="fnoContent.application_01._016"]')
    GAS_6 = (By.XPATH, '//*[@name="fnoContent.application_01._017"]')

    GAS_8 = (By.XPATH, '//*[@name="fnoContent.application_01._019"]')
    GAS_9 = (By.XPATH, '//*[@name="fnoContent.application_01._020"]')
    GAS_10 = (By.XPATH, '//*[@name="fnoContent.application_01._021"]')
    GAS_11 = (By.XPATH, '//*[@name="fnoContent.application_01._022"]')

    # Природный газ
    NATURE_GAS_1 = (By.XPATH, '//*[@name="fnoContent.application_01._023"]')
    NATURE_GAS_2 = (By.XPATH, '//*[@name="fnoContent.application_01._024"]')
    NATURE_GAS_3 = (By.XPATH, '//*[@name="fnoContent.application_01._025"]')
    NATURE_GAS_4 = (By.XPATH, '//*[@name="fnoContent.application_01._026"]')
    NATURE_GAS_5 = (By.XPATH, '//*[@name="fnoContent.application_01._027"]')
    NATURE_GAS_6 = (By.XPATH, '//*[@name="fnoContent.application_01._028"]')

    NATURE_GAS_8 = (By.XPATH, '//*[@name="fnoContent.application_01._030"]')
    NATURE_GAS_9 = (By.XPATH, '//*[@name="fnoContent.application_01._031"]')
    NATURE_GAS_10 = (By.XPATH, '//*[@name="fnoContent.application_01._032"]')
    NATURE_GAS_11 = (By.XPATH, '//*[@name="fnoContent.application_01._033"]')

    # Подземные воды
    WATER_1 = (By.XPATH, '//*[@name="fnoContent.application_01._034"]')
    WATER_2 = (By.XPATH, '//*[@name="fnoContent.application_01._035"]')
    WATER_3 = (By.XPATH, '//*[@name="fnoContent.application_01._036"]')
    WATER_4 = (By.XPATH, '//*[@name="fnoContent.application_01._037"]')

    # ПРИЛОЖЕНИЕ 2
    # Разделы
    PART_1 = (By.XPATH, '//*[text()="Раздел. Бонус добычи к уплате"]')
    PART_2 = (By.XPATH, '//*[text()="Раздел. Бонус добычи до коммерческого обнаружения"]')

    # Раздел. Бонус добычи к уплате
    # 500.02.001
    SECOND_APP_1 = (By.XPATH, '//*[@name="fnoContent.application_02._001"]')
    SECOND_APP_2 = (By.XPATH, '//*[@name="fnoContent.application_02._002"]')
    SECOND_APP_3 = (By.XPATH, '//*[@name="fnoContent.application_02._003"]')
    # Раздел. Бонус добычи до коммерческого обнаружения
    SECOND_APP_4 = (By.XPATH, '//*[@name="fnoContent.application_02._004"]')

    # ПРИЛОЖЕНИЕ 3
    # Раздел до 1 января 2004 года
    THIRD_APP_FIRST_PART = (By.XPATH, '//*[@name="fnoContent.application_03._1"]')
    THIRD_APP_SECOND_PART = (By.XPATH, '//*[@name="fnoContent.application_03._2"]')
    THIRD_APP_1 = (By.XPATH, '//*[@name="fnoContent.application_03._001"]')
    THIRD_APP_2 = (By.XPATH, '//*[@name="fnoContent.application_03._002"]')
    THIRD_APP_3 = (By.XPATH, '//*[@name="fnoContent.application_03._003"]')
    THIRD_APP_6 = (By.XPATH, '//*[@name="fnoContent.application_03._006"]')
    THIRD_APP_8 = (By.XPATH, '//*[@name="fnoContent.application_03._008"]')
    THIRD_APP_12 = (By.XPATH, '//*[@name="fnoContent.application_03._012"]')
    THIRD_APP_14 = (By.XPATH, '//*[@name="fnoContent.application_03._014"]')
    # Раздел после 1 января 2005 года
    THIRD_APP_15 = (By.XPATH, '//*[@name="fnoContent.application_03._015"]')
    THIRD_APP_17 = (By.XPATH, '//*[@name="fnoContent.application_03._017"]')
    THIRD_APP_19 = (By.XPATH, '//*[@name="fnoContent.application_03._019"]')
    THIRD_APP_22 = (By.XPATH, '//*[@name="fnoContent.application_03._022"]')
    THIRD_APP_23 = (By.XPATH, '//*[@name="fnoContent.application_03._023"]')
    THIRD_APP_26 = (By.XPATH, '//*[@name="fnoContent.application_03._026"]')
    THIRD_APP_27 = (By.XPATH, '//*[@name="fnoContent.application_03._027"]')
    THIRD_APP_28 = (By.XPATH, '//*[@name="fnoContent.application_03._028"]')
    THIRD_APP_29 = (By.XPATH, '//*[@name="fnoContent.application_03._029"]')
    THIRD_APP_30 = (By.XPATH, '//*[@name="fnoContent.application_03._030"]')

    # ПРИЛОЖЕНИЕ 4
    ADD_STR = (By.XPATH, '//*[text()="Добавить строку"]')
    B_APP_4 = (By.XPATH, '//*[@name="B"]')
    C_APP_4 = (By.XPATH, '//*[@name="C"]')
    D_APP_4 = (By.XPATH, '//*[@name="D"]')
    E_APP_4 = (By.XPATH, '//*[@name="E"]')
    ADD = (By.XPATH, '//*[text()="Добавить"]')
    CANCEL_ADD_STR = (By.XPATH, '//*[text()="Отменить"]')

    # ПРИЛОЖЕНИЕ 5
    B_APP_5 = (By.XPATH, '//*[@name="B"]')
    C_APP_5 = (By.XPATH, '//*[@name="C"]')

    # ПРИЛОЖЕНИЕ 6
    SIXTH_APP_FIRST_CHAPTER = (By.XPATH, '//*[@name="fnoContent.application_06._1"]')
    SIXTH_APP_SECOND_CHAPTER = (By.XPATH, '//*[@name="fnoContent.application_06._2"]')
    # Раздел до 1 января 2004 года
    SIXTH_APP_1 = (By.XPATH, '//*[@name="fnoContent.application_06._001"]')
    SIXTH_APP_2 = (By.XPATH, '//*[@name="fnoContent.application_06._002"]')
    SIXTH_APP_4 = (By.XPATH, '//*[@name="fnoContent.application_06._004"]')
    SIXTH_APP_5 = (By.XPATH, '//*[@name="fnoContent.application_06._005"]')

    # Раздел после 1 января 2005 года
    SIXTH_APP_7 = (By.XPATH, '//*[@name="fnoContent.application_06._007"]')
    SIXTH_APP_8 = (By.XPATH, '//*[@name="fnoContent.application_06._008"]')
    SIXTH_APP_9 = (By.XPATH, '//*[@name="fnoContent.application_06._009"]')

    # ПРИЛОЖЕНИЕ 7
    SEVEN_APP_1 = (By.XPATH, '//*[@name="fnoContent.application_07._001"]')
    SEVEN_APP_2 = (By.XPATH, '//*[@name="fnoContent.application_07._002"]')

    SEVEN_APP_4 = (By.XPATH, '//*[@name="fnoContent.application_07._004"]')
    SEVEN_APP_5 = (By.XPATH, '//*[@name="fnoContent.application_07._005"]')
    SEVEN_APP_6 = (By.XPATH, '//*[@name="fnoContent.application_07._006"]')

    SEVEN_APP_8 = (By.XPATH, '//*[@name="fnoContent.application_07._008"]')
    SEVEN_APP_9 = (By.XPATH, '//*[@name="fnoContent.application_07._009"]')
    SEVEN_APP_10 = (By.XPATH, '//*[@name="fnoContent.application_07._010"]')

    SEVEN_APP_12 = (By.XPATH, '//*[@name="fnoContent.application_07._012"]')
    SEVEN_APP_13 = (By.XPATH, '//*[@name="fnoContent.application_07._013"]')

    SEVEN_APP_15 = (By.XPATH, '//*[@name="fnoContent.application_07._015"]')

    # СТРАНИЦА ОТПРАВКИ
    CONFIRM = (By.XPATH, '//*[@name="fnoContent.taxpayerResponsibility.isResponsible"]')
    FORM = (By.XPATH, '//*[text()="Сформировать"]')