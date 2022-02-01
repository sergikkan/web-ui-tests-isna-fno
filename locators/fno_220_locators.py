from selenium.webdriver.common.by import By



class FNO220LocatorsName(object):
    # 2 Страница
    INCOME_1 = '220.00.001 Доход от реализации'
    INCOME_2 = '220.00.002 Доход от прироста стоимости'
    INCOME_3 = '220.00.003 Прочие доходы'
    INCOME_5 = '220.00.005 Корректировка дохода индивидуального предпринимателя, полученного совокупно за налоговый ' \
               'период, осуществляемая в соответствии с пунктом 1 статьи 241 Налогового кодекса '
    INCOME_6 = '220.00.006 Корректировка дохода индивидуального предпринимателя, полученного совокупно за налоговый ' \
               'период, осуществляемая в соответствии с пунктом 2 статьи 241 Налогового кодекса '
    INCOME_7_I = '220.00.007 I Корректировка доходов'
    INCOME_7_II = '220.00.007 II Корректировка вычетов'
    INCOME_8 = '220.00.008 Корректировка доходов в соответствии с Законом о трансфертном ценообразовании'
    INCOME_9 = '220.00.009 Корректировка вычетов в соответствии с Законом о трансфертном ценообразовании'
    # 3 Страница
    STOCK_1 = '220.00.011 I Запасы на начало налогового периода всего'
    STOCK_2 = '220.00.011 II Запасы на конец налогового периода всего'
    STOCK_3_A = 'A Товарно-материальные запасы'
    STOCK_3_B = 'B Финансовые услуги'
    STOCK_3_C = 'C Рекламные услуги'
    STOCK_3_D = 'D Консультационные услуги'
    STOCK_3_E = 'E Маркетинговые услуги'
    STOCK_3_F = 'F Дизайнерские услуги'
    STOCK_3_G = 'G Инжиниринговые услуги'
    STOCK_3_H = 'H Прочие услуги и работы'
    STOCK_4 = '220.00.011 IV Расходы по начисленным доходам работников и иным выплатам физическим лицам'
    STOCK_5 = '220.00.011 V Стоимость работ и услуг, себестоимость запасов, признанные расходами будущих периодов в ' \
              'предыдущих налоговых периодах и относимые на вычеты в отчетном налоговом периоде '
    STOCK_6 = '220.00.011 VI Стоимость работ и услуг, себестоимость запасов, признаваемые последующими расходами'
    STOCK_7 = '220.00.011 VII Стоимость работ и услуг, себестоимость запасов, включаемые в первоначальную стоимость ' \
              'фиксированных активов, объектов преференций и активов, не подлежащих амортизации '
    STOCK_8 = '220.00.011 VIII Стоимость работ и услуг, себестоимость запасов, не относимые на вычеты на основании ' \
              'статьи 264 НК '
    STOCK_9 = '220.00.011 IX Стоимость работ и услуг, себестоимость запасов, признаваемые расходами будущих периодов ' \
              'и подлежащие отнесению на вычеты в последующие налоговые периоды '
    THIRD_PAGE_12 = '220.00.012 Штрафы, пени, неустойки'
    THIRD_PAGE_13 = '220.00.013 Сумма НДС, относимая на вычеты по основаниям, установленным пунктом 9 статьи 243 ' \
                    'Налогового кодекса '
    THIRD_PAGE_14 = '220.00.014 Отчисления в ГФСС, ФСМС, ОПВР'
    THIRD_PAGE_15 = '220.00.015 Вычеты по вознаграждению'
    THIRD_PAGE_16 = '220.00.016 Суммы представительских расходов'
    THIRD_PAGE_17 = '220.00.017 Сомнительные требования'
    THIRD_PAGE_18 = '220.00.018 Налоги и платежи в бюджет'
    THIRD_PAGE_20 = '220.00.020 Прочие вычеты'
    # 4 СТРАНИЦА
    # Выбор вычетов взять из 3 страницы
    FOURTH_PAGE_22 = '220.00.022 Налоговые вычеты в виде обязательных пенсионных взносов'
    FOURTH_PAGE_24 = '220.00.024 Стандартные налоговые вычеты'
    FOURTH_PAGE_25_I = '220.00.025 I По добровольным пенсионным взносам'
    FOURTH_PAGE_25_II = '220.00.025 II На медицину'
    FOURTH_PAGE_25_III = '220.00.025 III По вознаграждениям'
    # 5 СТРАНИЦА
    FIFTH_PAGE_33_I = '220.00.033 I Уменьшение налогооблагаемого дохода в соответствии с подпунктом 1) пункта 1 ' \
                      'статьи 288 Налогового кодекса '
    FIFTH_PAGE_33_II = '220.00.033 II Уменьшение налогооблагаемого дохода в соответствии с подпунктом 3) пункта 1 ' \
                       'статьи 288 Налогового кодекса '
    FIFTH_PAGE_35 = '220.00.035 Убытки, перенесенные из предыдущих налоговых периодов'
    FIFTH_PAGE_37 = '220.00.037 Облагаемый доход индивидуального предпринимателя, осуществляющего электронную ' \
                    'торговлю товарами '
    FIFTH_PAGE_38 = '220.00.038 Корректировка дохода в соответствии со статьей 341 Налогового кодекса'
    # 6 СТРАНИЦА
    SIXTH_PAGE_42_III = ''
    SIXTH_PAGE_42_IV = ''
    SIXTH_PAGE_42_V = ''
    SIXTH_PAGE_43 = '220.00.043 Уменьшение ИПН в соответствии с налоговым законодательством'
    SIXTH_PAGE_44 = '220.00.044 ВСЕГО НАЛОГА К УПЛАТЕ'
    # 1 ПРИЛОЖЕНИЕ
    ADD_STR = 'Добавление строки'
    FIRST_APP_B = 'B ИИН/БИН'
    FIRST_APP_C = 'C Код страны резидентства'
    FIRST_APP_C_SELECT = 'Код страны резидентства (выбор)'
    FIRST_APP_D = 'D Номер налоговой регистрации нерезидента- контрагента в стране резидентства нерезидента'
    FIRST_APP_E = 'E Код вида расхода'
    FIRST_APP_E_SELECT = 'Выбор кода вида расхода'
    FIRST_APP_F = 'F Сумма'
    ADD = 'Добавить'
    CANCEL_ADD_STR = 'Отменить'

    # 2 ПРИЛОЖЕНИЕ
    SECOND_APP_B = 'B Код вида международного договора'
    SECOND_APP_B_SELECT = 'Выбор кода вида международного договора'
    SECOND_APP_C = 'C Наименование международного договора'
    SECOND_APP_C_SELECT = 'Выбор наименования международного договора'
    SECOND_APP_D = 'D Код страны, с которой заключен международный договор'
    SECOND_APP_D_SELECT = 'Выбор кода страны, с которой заключен международный договор'
    SECOND_APP_E = 'E Доход, подлежащий освобождению от налогообложения согласно положениям международного договора'

    # 3 ПРИЛОЖЕНИЕ
    THIRD_APP_B = 'B Код страны'
    THIRD_APP_B_SELECT = 'Выбор Кода страны'
    THIRD_APP_C = 'C Код вида дохода'
    THIRD_APP_C_SELECT = 'Выбор кода вида дохода'
    THIRD_APP_D = 'D Код вида валюты дохода, указанного в графе Е'
    THIRD_APP_D_SELECT = 'Выбор кода вида валюты дохода'
    THIRD_APP_G = 'G Сумма подоходного налога, подлежащего вычету'
    THIRD_APP_E = 'E Сумма начисленных доходов из источников в иностранном государстве (в иностранной валюте)'
    THIRD_APP_F = 'F Сумма начисленных доходов из источников в иностранном государстве (в национальной валюте)'

    # 4 ПРИЛОЖЕНИЕ
    FOURTH_APP_1_I = '220.04.001 I'
    FOURTH_APP_1_II = '220.04.001 II'
    FOURTH_APP_1_III = '220.04.001 III'
    FOURTH_APP_1_IV = '220.04.001 IV'
    FOURTH_APP_2_I = '220.04.002 I'
    FOURTH_APP_2_II = '220.04.002 II'
    FOURTH_APP_2_III = '220.04.002 III'
    FOURTH_APP_2_IV = '220.04.002 IV'
    FOURTH_APP_3_I = '220.04.003 I'
    FOURTH_APP_3_II = '220.04.003 II'
    FOURTH_APP_3_III = '220.04.003 III'
    FOURTH_APP_3_IV = '220.04.003 IV'
    FOURTH_APP_4_I = '220.04.004 I'
    FOURTH_APP_4_II = '220.04.004 II'
    FOURTH_APP_4_III = '220.04.004 III'
    FOURTH_APP_4_IV = '220.04.004 IV'
    FOURTH_APP_5_I = '220.04.005 I'
    FOURTH_APP_5_II = '220.04.005 II'
    FOURTH_APP_5_III = '220.04.005 III'
    FOURTH_APP_5_IV = '220.04.005 IV'
    FOURTH_APP_6_I = '220.04.006 I'
    FOURTH_APP_6_II = '220.04.006 II'
    FOURTH_APP_6_III = '220.04.006 III'
    FOURTH_APP_6_IV = '220.04.006 IV'
    FOURTH_APP_7_I = '220.04.007 I'
    FOURTH_APP_7_II = '220.04.007 II'
    FOURTH_APP_7_III = '220.04.007 II'
    FOURTH_APP_7_IV = '220.04.007 IV'
    FOURTH_APP_8_I = '220.04.008 I'
    FOURTH_APP_8_II = '220.04.008 II'
    FOURTH_APP_8_III = '220.04.008 III'
    FOURTH_APP_8_IV = '220.04.008 IV'
    FOURTH_APP_9_I = '220.04.009 I'
    FOURTH_APP_9_II = '220.04.009 II'
    FOURTH_APP_9_III = '220.04.009 III'
    FOURTH_APP_9_IV = '220.04.009 IV'
    FOURTH_APP_10_I = '220.04.010 I'
    FOURTH_APP_10_II = '220.04.010 II'
    FOURTH_APP_10_III = '220.04.010 III'
    FOURTH_APP_10_IV = '220.04.010 IV'
    FOURTH_APP_11_I = '220.04.011 I'
    FOURTH_APP_11_II = '220.04.011 II'
    FOURTH_APP_11_III = '220.04.011 III'
    FOURTH_APP_11_IV = '220.04.011 IV'
    FOURTH_APP_12 = '220.04.012'

    # 5 ПРИЛОЖЕНИЕ
    FIFTH_APP_B = 'B Наименование КИК или ПУ КИК'
    FIFTH_APP_C = 'C Код страны регистрации'
    FIFTH_APP_C_SELECT = ''
    FIFTH_APP_F = 'F Код валюты'
    FIFTH_APP_F_SELECT = ''
    FIFTH_APP_D = 'D Номер государственной (налоговой) регистрации КИК или ПУ КИК'
    FIFTH_APP_E = 'E Коэффицент участия или контроля'
    FIFTH_APP_G = 'G Финансовая прибыль до налогообложения в иностранной валюте'
    FIFTH_APP_H = 'H Сумма уменьшений в иностранной валюте'
    FIFTH_APP_I = 'I Финансовая прибыль, подлежащая налогообложению в Республике Казахстан в иностранной валюте'
    FIFTH_APP_J = 'J Финансовая прибыль, подлежащая налогообложению в национальной валюте'
    FIFTH_APP_K = 'K Сумма иностранного налога на прибыль, подлежащая отнесению в зачет, в национальной валюте'
    FIFTH_APP_L = 'L Доходы из источников в Республике Казахстан в национальной валюте'
    FIFTH_APP_M = 'M Корпоративный подоходный налог, удержанный у источника выплаты'

class FNO220Locators(object):
    # 1 СТРАНИЦА
    DECLARATION_TYPE = (By.XPATH, '//*[@name="declarationTypes"]')
    DECLARATION_TYPE_SELECT = (By.XPATH, '//*[@title="Первоначальная"]')
    TAX_PAYER_CATEGORIES = (By.XPATH, '//*[@name="taxpayerCategories"]')
    TAX_PAYER_CATEGORIES_SELECT = (By.XPATH, '//*[text()="доверительный управляющий"]')
    RESIDENTION = (By.XPATH, '//*[@id="root"]/div/div[4]/div[4]/div/div/div[4]/form/div[6]/div/div/div/div[2]/div['
                             '1]/div/div/div')
    RESIDENTION_SELECT = (By.XPATH, '//*[@title="Нерезидент РК"]')
    RESIDENTION_CODE = (By.XPATH, '//*[@id="rc_select_5"]')
    RESIDENTION_CODE_SELECT = (By.XPATH, '//*[@label="Афганистан"]')
    TAX_NUMBER = (By.XPATH, '//*[@name="fnoContent.commonInfo._10.B"]')
    APPS = (By.XPATH, '//*[@id="root"]/div/div[4]/div[4]/div/div/div[4]/form/div[8]/span/div[2]/div[1]/div/div/div['
                      '1]/div/div/div')
    APPS_SELECT_ALL = (By.XPATH, '//*[text()="Выбрать все"]')
    CONTROL_TEXT2 = (By.XPATH, '//*[text()="© 2021 Комитет государственных доходов МФ РК"]')
    AFTER = (By.XPATH, '//*[text() = "Далее"]')

    # 2 СТРАНИЦА
    INCOME_1 = (By.XPATH, '//*[@name="fnoContent.revenueCalculation._001"]')
    INCOME_2 = (By.XPATH, '//*[@name="fnoContent.revenueCalculation._002"]')
    INCOME_3 = (By.XPATH, '//*[@name="fnoContent.revenueCalculation._003"]')
    INCOME_5 = (By.XPATH, '//*[@name="fnoContent.revenueCalculation._005"]')
    INCOME_6 = (By.XPATH, '//*[@name="fnoContent.revenueCalculation._006"]')
    INCOME_7_I = (By.XPATH, '//*[@name="fnoContent.revenueCalculation._007.I"]')
    INCOME_7_II = (By.XPATH, '//*[@name="fnoContent.revenueCalculation._007.II"]')
    INCOME_8 = (By.XPATH, '//*[@name="fnoContent.revenueCalculation._008"]')
    INCOME_9 = (By.XPATH, '//*[@name="fnoContent.revenueCalculation._009"]')

    # 3 СТРАНИЦА
    DEDUCTIONS = (By.XPATH, '//*[@role="combobox"]')
    DEDUCTIONS_SELECT_ALL = (By.XPATH, '//*[text()="Выбрать все"]')
    # Раздел. Вычеты
    STOCK_1 = (By.XPATH, '//*[@name="fnoContent.deduction._011.I"]')
    STOCK_2 = (By.XPATH, '//*[@name="fnoContent.deduction._011.II"]')
    STOCK_3_A = (By.XPATH, '//*[@name="fnoContent.deduction._011.III.A"]')
    STOCK_3_B = (By.XPATH, '//*[@name="fnoContent.deduction._011.III.B"]')
    STOCK_3_C = (By.XPATH, '//*[@name="fnoContent.deduction._011.III.C"]')
    STOCK_3_D = (By.XPATH, '//*[@name="fnoContent.deduction._011.III.D"]')
    STOCK_3_E = (By.XPATH, '//*[@name="fnoContent.deduction._011.III.E"]')
    STOCK_3_F = (By.XPATH, '//*[@name="fnoContent.deduction._011.III.F"]')
    STOCK_3_G = (By.XPATH, '//*[@name="fnoContent.deduction._011.III.G"]')
    STOCK_3_H = (By.XPATH, '//*[@name="fnoContent.deduction._011.III.H"]')
    # 220.00.011 IV
    STOCK_4 = (By.XPATH, '//*[@name="fnoContent.deduction._011.IV"]')
    STOCK_5 = (By.XPATH, '//*[@name="fnoContent.deduction._011.V"]')
    STOCK_6 = (By.XPATH, '//*[@name="fnoContent.deduction._011.VI"]')
    STOCK_7 = (By.XPATH, '//*[@name="fnoContent.deduction._011.VII"]')
    STOCK_8 = (By.XPATH, '//*[@name="fnoContent.deduction._011.VIII"]')
    STOCK_9 = (By.XPATH, '//*[@name="fnoContent.deduction._011.IX"]')
    THIRD_PAGE_12 = (By.XPATH, '//*[@name="fnoContent.deduction._012"]')
    THIRD_PAGE_13 = (By.XPATH, '//*[@name="fnoContent.deduction._013"]')
    THIRD_PAGE_14 = (By.XPATH, '//*[@name="fnoContent.deduction._014"]')
    THIRD_PAGE_15 = (By.XPATH, '//*[@name="fnoContent.deduction._015"]')
    THIRD_PAGE_16 = (By.XPATH, '//*[@name="fnoContent.deduction._016"]')
    THIRD_PAGE_17 = (By.XPATH, '//*[@name="fnoContent.deduction._017"]')
    THIRD_PAGE_18 = (By.XPATH, '//*[@name="fnoContent.deduction._018"]')
    THIRD_PAGE_20 = (By.XPATH, '//*[@name="fnoContent.deduction._020"]')
    # 4 СТРАНИЦА
    # Выбор вычетов взять из 3 страницы
    FOURTH_PAGE_22 = (By.XPATH, '//*[@name="fnoContent.deduction.taxDeduction._022"]')
    FOURTH_PAGE_24 = (By.XPATH, '//*[@name="fnoContent.deduction.taxDeduction._024"]')
    FOURTH_PAGE_25_I = (By.XPATH, '//*[@name="fnoContent.deduction.taxDeduction._025.I"]')
    FOURTH_PAGE_25_II = (By.XPATH, '//*[@name="fnoContent.deduction.taxDeduction._025.II"]')
    FOURTH_PAGE_25_III = (By.XPATH, '//*[@name="fnoContent.deduction.taxDeduction._025.III"]')
    # 5 СТРАНИЦА
    FIFTH_PAGE_33_I = (By.XPATH, '//*[@name="fnoContent.taxableIncome._033.I"]')
    FIFTH_PAGE_33_II = (By.XPATH, '//*[@name="fnoContent.taxableIncome._033.II"]')
    FIFTH_PAGE_35 = (By.XPATH, '//*[@name="fnoContent.taxableIncome._035"]')
    FIFTH_PAGE_37 = (By.XPATH, '//*[@name="fnoContent.taxableIncome._037"]')
    FIFTH_PAGE_38 = (By.XPATH, '//*[@name="fnoContent.taxableIncome._038"]')
    # 6 СТРАНИЦА
    SIXTH_PAGE_42_III = (By.XPATH, '//*[@name="fnoContent.taxLiabilityCalculation._042.III"]')
    SIXTH_PAGE_42_IV = (By.XPATH, '//*[@name="fnoContent.taxLiabilityCalculation._042.IV"]')
    SIXTH_PAGE_42_V = (By.XPATH, '//*[@name="fnoContent.taxLiabilityCalculation._042.V"]')
    SIXTH_PAGE_43 = (By.XPATH, '//*[@name="fnoContent.taxLiabilityCalculation._043"]')
    SIXTH_PAGE_44 = (By.XPATH, '//*[@name="fnoContent.taxLiabilityCalculation._044"]')

    '''1 ПРИЛОЖЕНИЕ'''
    # 1 ПРИЛОЖЕНИЕ
    ADD_STR = (By.XPATH, '//*[text()="Добавить строку"]')
    FIRST_APP_B = (By.XPATH, '//*[@name="B"]')
    FIRST_APP_C = (By.XPATH, '//*[@name="C"]')
    FIRST_APP_C_SELECT = (By.XPATH, '//*[text()="Афганистан"]')
    FIRST_APP_D = (By.XPATH, '//*[@name="D"]')
    FIRST_APP_E = (By.XPATH, '//*[@name="E"]')
    FIRST_APP_E_SELECT = (By.XPATH, '//*[@label="Финансовые услуги"]')
    FIRST_APP_F = (By.XPATH, '//*[@name="F"]')
    ADD = (By.XPATH, '//*[text()="Добавить"]')
    CANCEL_ADD_STR = (By.XPATH, '//*[text()="Отменить"]')

    # 2 ПРИЛОЖЕНИЕ
    SECOND_APP_B = (By.XPATH, '//*[@name="B"]')
    SECOND_APP_B_SELECT = (By.XPATH, '//*[text()="01"]')
    SECOND_APP_C = (By.XPATH, '//*[@name="C"]')
    SECOND_APP_C_SELECT = (By.XPATH, '//*[@title="Конвенция об избежании двойного налогообложения и предотвращении '
                                     'уклонения от уплаты налогов на доход и капитал"]')
    SECOND_APP_D = (By.XPATH, '//*[@name="D"]')
    SECOND_APP_D_SELECT = (By.XPATH, '//*[text()="Афганистан"]')
    SECOND_APP_E = (By.XPATH, '//*[@name="E"]')

    # 3 ПРИЛОЖЕНИЕ
    THIRD_APP_B = (By.XPATH, '//*[@name="B"]')
    THIRD_APP_B_SELECT = (By.XPATH, '//*[text()="Афганистан"]')
    THIRD_APP_C = (By.XPATH, '//*[@name="C"]')
    THIRD_APP_C_SELECT = (By.XPATH, '//*[@label="Доходы от реализации товаров на территории Республики Казахстан"]')
    THIRD_APP_D = (By.XPATH, '//*[@name="D"]')
    THIRD_APP_D_SELECT = (By.XPATH, '//*[text()="Австралийский доллар"]')
    THIRD_APP_G = (By.XPATH, '//*[@name="G"]')
    THIRD_APP_E = (By.XPATH, '//*[@name="E"]')
    THIRD_APP_F = (By.XPATH, '//*[@name="F"]')

    # 4 ПРИЛОЖЕНИЕ
    FOURTH_APP_DEDUCTIONS = (By.XPATH, '//*[@name="fnoContent.application_04.treeSelect"]')
    CONTROL_TEXT = (By.XPATH, '//*[text()="II"]')
    FOURTH_APP_1_I = (By.XPATH, '//*[@name="fnoContent.application_04._001.I"]')
    FOURTH_APP_1_II = (By.XPATH, '//*[@name="fnoContent.application_04._001.II"]')
    FOURTH_APP_1_III = (By.XPATH, '//*[@name="fnoContent.application_04._001.III"]')
    FOURTH_APP_1_IV = (By.XPATH, '//*[@name="fnoContent.application_04._001.IV"]')
    FOURTH_APP_2_I = (By.XPATH, '//*[@name="fnoContent.application_04._002.I"]')
    FOURTH_APP_2_II = (By.XPATH, '//*[@name="fnoContent.application_04._002.II"]')
    FOURTH_APP_2_III = (By.XPATH, '//*[@name="fnoContent.application_04._002.III"]')
    FOURTH_APP_2_IV = (By.XPATH, '//*[@name="fnoContent.application_04._002.IV"]')
    FOURTH_APP_3_I = (By.XPATH, '//*[@name="fnoContent.application_04._003.I"]')
    FOURTH_APP_3_II = (By.XPATH, '//*[@name="fnoContent.application_04._003.II"]')
    FOURTH_APP_3_III = (By.XPATH, '//*[@name="fnoContent.application_04._003.III"]')
    FOURTH_APP_3_IV = (By.XPATH, '//*[@name="fnoContent.application_04._003.IV"]')
    FOURTH_APP_4_I = (By.XPATH, '//*[@name="fnoContent.application_04._004.I"]')
    FOURTH_APP_4_II = (By.XPATH, '//*[@name="fnoContent.application_04._004.II"]')
    FOURTH_APP_4_III = (By.XPATH, '//*[@name="fnoContent.application_04._004.III"]')
    FOURTH_APP_4_IV = (By.XPATH, '//*[@name="fnoContent.application_04._004.IV"]')
    FOURTH_APP_5_I = (By.XPATH, '//*[@name="fnoContent.application_04._005.I"]')
    FOURTH_APP_5_II = (By.XPATH, '//*[@name="fnoContent.application_04._005.II"]')
    FOURTH_APP_5_III = (By.XPATH, '//*[@name="fnoContent.application_04._005.III"]')
    FOURTH_APP_5_IV = (By.XPATH, '//*[@name="fnoContent.application_04._005.IV"]')
    FOURTH_APP_6_I = (By.XPATH, '//*[@name="fnoContent.application_04._006.I"]')
    FOURTH_APP_6_II = (By.XPATH, '//*[@name="fnoContent.application_04._006.II"]')
    FOURTH_APP_6_III = (By.XPATH, '//*[@name="fnoContent.application_04._006.III"]')
    FOURTH_APP_6_IV = (By.XPATH, '//*[@name="fnoContent.application_04._006.IV"]')
    FOURTH_APP_7_I = (By.XPATH, '//*[@name="fnoContent.application_04._007.I"]')
    FOURTH_APP_7_II = (By.XPATH, '//*[@name="fnoContent.application_04._007.II"]')
    FOURTH_APP_7_III = (By.XPATH, '//*[@name="fnoContent.application_04._007.III"]')
    FOURTH_APP_7_IV = (By.XPATH, '//*[@name="fnoContent.application_04._007.IV"]')
    FOURTH_APP_8_I = (By.XPATH, '//*[@name="fnoContent.application_04._008.I"]')
    FOURTH_APP_8_II = (By.XPATH, '//*[@name="fnoContent.application_04._008.II"]')
    FOURTH_APP_8_III = (By.XPATH, '//*[@name="fnoContent.application_04._008.III"]')
    FOURTH_APP_8_IV = (By.XPATH, '//*[@name="fnoContent.application_04._008.IV"]')
    FOURTH_APP_9_I = (By.XPATH, '//*[@name="fnoContent.application_04._009.I"]')
    FOURTH_APP_9_II = (By.XPATH, '//*[@name="fnoContent.application_04._009.II"]')
    FOURTH_APP_9_III = (By.XPATH, '//*[@name="fnoContent.application_04._009.III"]')
    FOURTH_APP_9_IV = (By.XPATH, '//*[@name="fnoContent.application_04._009.IV"]')
    FOURTH_APP_10_I = (By.XPATH, '//*[@name="fnoContent.application_04._010.I"]')
    FOURTH_APP_10_II = (By.XPATH, '//*[@name="fnoContent.application_04._010.II"]')
    FOURTH_APP_10_III = (By.XPATH, '//*[@name="fnoContent.application_04._010.III"]')
    FOURTH_APP_10_IV = (By.XPATH, '//*[@name="fnoContent.application_04._010.IV"]')
    FOURTH_APP_11_I = (By.XPATH, '//*[@name="fnoContent.application_04._011.I"]')
    FOURTH_APP_11_II = (By.XPATH, '//*[@name="fnoContent.application_04._011.II"]')
    FOURTH_APP_11_III = (By.XPATH, '//*[@name="fnoContent.application_04._011.III"]')
    FOURTH_APP_11_IV = (By.XPATH, '//*[@name="fnoContent.application_04._011.IV"]')
    FOURTH_APP_12 = (By.XPATH, '//*[@name="fnoContent.application_04._012"]')

    # 5 ПРИЛОЖЕНИЕ
    FIFTH_APP_B = (By.XPATH, '//*[@name="B"]')
    FIFTH_APP_C = (By.XPATH, '//*[@name="C"]')
    FIFTH_APP_C_SELECT = (By.XPATH, '//*[text()="Афганистан"]')
    FIFTH_APP_F = (By.XPATH, '//*[@name="F"]')
    FIFTH_APP_F_SELECT = (By.XPATH, '//*[@label="Австралийский доллар"]')
    FIFTH_APP_D = (By.XPATH, '//*[@name="D"]')
    FIFTH_APP_E = (By.XPATH, '//*[@name="E"]')
    FIFTH_APP_G = (By.XPATH, '//*[@name="G"]')
    FIFTH_APP_H = (By.XPATH, '//*[@name="H"]')
    FIFTH_APP_I = (By.XPATH, '//*[@name="I"]')
    FIFTH_APP_J = (By.XPATH, '//*[@name="J"]')
    FIFTH_APP_K = (By.XPATH, '//*[@name="K"]')
    FIFTH_APP_L = (By.XPATH, '//*[@name="L"]')
    FIFTH_APP_M = (By.XPATH, '//*[@name="M"]')