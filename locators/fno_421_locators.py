from selenium.webdriver.common.by import By


class FNO_421_Locators_Name(object):
    # 421.01.001 Спирт собственного производства
    LITER_1 = 'Отгруженный для производства алкогольной продукции 1 (Налоговая база (литр))'
    EXC_RATE_1 = 'Отгруженный для производства алкогольной продукции 1 (Ставка акциза)'
    LITER_2 = 'Отгруженный не для производства алкогольной продукции 2 (Налоговая база (литр))'
    EXC_RATE_2 = 'Отгруженный не для производства алкогольной продукции 2 (Ставка акциза)'
    # 421.01.003 Виноматериал собственного производства
    WINE_LITER_1 = 'Отгруженный для производства алкогольной продукции 1 (Налоговая база (литр))'
    WINE_EXC_1 = 'Отгруженный для производства алкогольной продукции 1 (Налоговая база (литр))'
    WINE_LITER_2 = 'Отгруженный не для производства алкогольной продукции 2 (Налоговая база (литр))'
    WINE_EXC_2 = 'Отгруженный не для производства алкогольной продукции 2 (Налоговая база (литр))'
    # 3 СТРАНИЦА
    BUT_1 = 'Спирта (Объем реализованного подакцизного товара)'
    BUT_2 = 'Спирта (Стоимость реализации)'
    BUT_3 = 'Водки и водки особой (Объем реализованного подакцизного товара)'
    BUT_4 = 'Водки и водки особой (Стоимость реализации)'
    BUT_5 = 'Ликерно-водочные изделия (Объем реализованного подакцизного товара)'
    BUT_6 = 'Ликерно-водочные изделия (Стоимость реализации)'
    BUT_7 = 'Вина (Объем реализованного подакцизного товара)'
    BUT_8 = 'Вина (Стоимость реализации)'
    BUT_9 = 'Конъяка (Объем реализованного подакцизного товара)'
    BUT_10 = 'Конъяка (Стоимость реализации)'
    BUT_11 = 'Бренди (Объем реализованного подакцизного товара)'
    BUT_12 = 'Бренди (Стоимость реализации)'
    BUT_13 = 'Пиво (Объем реализованного подакцизного товара)'
    BUT_14 = 'Пиво (Стоимость реализации)'
    BUT_15 = 'Виноматериал (Объем реализованного подакцизного товара)'
    BUT_16 = 'Виноматериал (Стоимость реализации)'
    BUT_17 = 'Бензин (за исключением авиационного) (Объем реализованного подакцизного товара)'
    BUT_18 = 'Бензин (за исключением авиационного) (Стоимость реализации)'
    BUT_19 = 'Дизельное топливо (Объем реализованного подакцизного товара)'
    BUT_20 = 'Дизельное топливо (Стоимость реализации)'
    BUT_21 = 'Спиртосодержащая продукция медицинского назначения (кроме бальзамов), зарегистрированная в соотвествии ' \
             '' \
             'с законодательством Республики казахстан в качестве лекарственного средства (стоимость реализации)  (' \
             'Объем реализованного подакцизного товара) '
    BUT_22 = 'Спиртосодержащая продукция медицинского назначения (кроме бальзамов), зарегистрированная в соотвествии ' \
             'с законодательством Республики казахстан в качестве лекарственного средства (стоимость реализации) (' \
             'Стоимость реализации) '
    C = 'C Объем использованного сырья (литр)'
    D = 'D Ставка акциза'
    E = 'E ставка акциза'
    # Приложение 400.04
    # Оптовая реализация бензина, произведенного структурным подразделением или объектами, связанными с налогообложением
    TAX_BASE_1 = 'Налоговая база (тонна) I'
    EXC_R_1 = 'Ставка акциза I'
    TAX_BASE_2 = 'Налоговая база (тонна) II'
    EXC_R_2 = 'Ставка акциза II'
    TAX_BASE_3 = 'Налоговая база (тонна) III'
    EXC_R_3 = 'Ставка акциза III'
    TAX_BASE_4 = 'Налоговая база (тонна) IV'
    EXC_R_4 = 'Ставка акциза IV'

    TAX_BASE_5 = 'Налоговая база (тонна) V'
    EXC_R_5 = 'Ставка акциза V'
    TAX_BASE_6 = 'Налоговая база (тонна) VI'
    EXC_R_6 = 'Ставка акциза VI'
    TAX_BASE_7 = 'Налоговая база (тонна) VII'
    EXC_R_7 = 'Ставка акциза VII'
    TAX_BASE_8 = 'Налоговая база (тонна) VIII'
    EXC_R_8 = 'Ставка акциза VIII'
    TAX_BASE_9 = 'Налоговая база (тонна) IX'
    EXC_R_9 = 'Ставка акциза IX'
    TAX_BASE_10 = 'Налоговая база (тонна) X'
    EXC_R_10 = 'Ставка акциза X'

    TAX_BASE_11 = 'Налоговая база (тонна) XI'
    EXC_R_11 = 'Ставка акциза XI'
    TAX_BASE_12 = 'Налоговая база (тонна) XII'
    EXC_R_12 = 'Ставка акциза XII'
    TAX_BASE_13 = 'Налоговая база (тонна) XIII'
    EXC_R_13 = 'Ставка акциза XIII'
    TAX_BASE_14 = 'Налоговая база (тонна) XIV'
    EXC_R_14 = 'Ставка акциза XIV'

    TAX_BASE_15 = 'Налоговая база (тонна) XV'
    EXC_R_15 = 'Ставка акциза XV'
    TAX_BASE_16 = 'Налоговая база (тонна) XVI'
    EXC_R_16 = 'Ставка акциза XVI'
    TAX_BASE_17 = 'Налоговая база (тонна) XVII'
    EXC_R_17 = 'Ставка акциза XVII'
    TAX_BASE_18 = 'Налоговая база (тонна) XVIII'
    EXC_R_18 = 'Ставка акциза XVIII'
    TAX_BASE_19 = 'Налоговая база (тонна) XIX'
    EXC_R_19 = 'Ставка акциза XIX'
    TAX_BASE_20 = 'Налоговая база (тонна) XX'
    EXC_R_20 = 'Ставка акциза XX'

    BUDG_QUAL_CODE = 'Код бюджетной классификации 1'
    BUDG_QUAL_CODE_SELECT = 'Выбор Код бюджетной классификации 1'
    VOL_EXC = 'Объем подакцизного товара (тонна) 1'
    SUM_EXC = 'Сумма акциза 1'
    BUDG_QUAL_CODE_2 = 'Код бюджетной классификации 2'
    BUDG_QUAL_CODE_2_SELECT = 'Выбор Код бюджетной классификации 2'
    VOL_EXC_2 = 'Объем подакцизного товара (тонна) 2'
    SUM_EXC_2 = 'Сумма акциза 2'


class FNO_421_Locators(object):
    # Выбор налогового периода
    SCROLLBAR = (By.XPATH, '//*[@class="rc-virtual-list-scrollbar-thumb"]')
    MONTH_BODY = (By.XPATH, '//*[@class="rc-virtual-list-holder"]')
    MONTH = (By.XPATH, '//*[@class="ant-select-selection-search-input"]')
    MONTH_SELECT_HOVER = (By.XPATH, '//*[@title="Январь"]')
    MONTH_SELECT = (By.XPATH, '//*[@title="Декабрь"]')
    YEAR = (By.XPATH, '//*[@placeholder="Год"]')
    YEAR_SELECT = (By.XPATH, '//*[text()="2020" and @class="ant-picker-cell-inner"]')
    SEND_DOC = (By.XPATH, '//*[text()="Подать"]')
    # 1 страница
    # Сведения о декларации
    PAYMENT_TYPE = (By.XPATH, '//*[@name="declarationTypes"]')
    PAYMENT_TYPE_SELECT = (By.XPATH, '//*[text() = "Первоначальная"]')
    DATE = (By.XPATH, '//*[@title="2020"]')
    DATE_SELECT = (By.XPATH, '//*[text() = "Декабрь"]')
    EXCISE_CALC = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div[2]/div/div/div/div[2]/div['
                             '1]/div/div/div')
    EXCISE_CALC_SELECT = (By.XPATH, '//*[text()="объекты, связанные с налогообложением юридического лица или '
                                    'индивидуального предпринимателя"]')
    # Сведения о налогоплательщике
    TAX_PAYER_CATEGORIES = (By.XPATH, '//*[@name="taxpayerCategories"]')
    TAX_PAYER_CATEGORIES_SELECT = (By.XPATH, "//*[text() = 'Доверительный управляющий']")
    # Код налогового органа: по месту регистрационного учета, объекта, связанного с налогобложением
    CODE1 = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div[7]/div[1]/div/div/div[2]/div[1]/div')
    CODE1_SELECT = (By.XPATH, '//*[@title="ДГД по Акмолинской области"]')
    # Код налогового органа: по месту регистрационного учета структурного подразделения юридического лица
    CODE2 = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div[7]/div[2]/div/div/div[2]/div['
                       '1]/div/span/div[1]')
    CODE2_SELECT = (By.XPATH, '//*[@title="0302"]')
    # Представленные приложения к налоговой отчетности
    APPLICATIONS = (By.XPATH, '//*[@class="ant-select ant-tree-select ant-select-lg appselector ant-select-multiple '
                              'ant-select-show-search"]')
    APPLICATION_01 = (By.XPATH, '//*[text() = "Выбрать все"]')
    APPLICATION_02 = (By.XPATH, '//*[text() = "Приложение 421.02  Облагаемые операции по алкогольной продукции и ('
                                'или) конкурсной массе спирта, алкогольной продукции, а также спиртосодержащей '
                                'продукции медицинского назначения, зарегистрированной в соответствии с '
                                'законодательством Республики Казахстан в качестве лекарственного средства"]')
    APPLICATION_03 = (By.XPATH, '//*[text() = "Приложение 421.03  Вычет из налога по алкогольной продукции"]')
    APPLICATION_04 = (By.XPATH, '//*[text() = "Приложение 421.04  Облагаемые операции по бензину (за исключением '
                                'авиационного) и (или) дизельному топливу"]')
    CONTROL_TEXT2 = (By.XPATH, '//*[text() = "© 2021 Комитет государственных доходов МФ РК"]')
    AFTER = (By.XPATH, '//*[text() = "Далее"]')

    # 2 СТРАНИЦА (1 Приложение)
    # Раздел. Сумма акциза по спирту
    # 421.01.001 Спирт собственного производства
    # I
    LITER_1 = (By.XPATH, '//*[@name="fnoContent.application_01._001.I.A"]')
    EXC_RATE_1 = (By.XPATH, '//*[@name="fnoContent.application_01._001.I.B"]')
    # II
    LITER_2 = (By.XPATH, '//*[@name="fnoContent.application_01._001.II.A"]')
    EXC_RATE_2 = (By.XPATH, '//*[@name="fnoContent.application_01._001.II.B"]')
    # Раздел. Сумма акциза по виноматериалу
    # 421.01.003 Виноматериал собственного производства
    # I
    WINE_LITER_1 = (By.XPATH, '//*[@name="fnoContent.application_01._003.I.A"]')
    WINE_EXC_1 = (By.XPATH, '//*[@name="fnoContent.application_01._003.I.B"]')
    # II
    WINE_LITER_2 = (By.XPATH, '//*[@name="fnoContent.application_01._003.II.A"]')
    WINE_EXC_2 = (By.XPATH, '//*[@name="fnoContent.application_01._003.II.B"]')

    # 3 СТРАНИЦА
    # I
    BUT_1 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.I.A"]')
    BUT_2 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.I.B"]')
    # II
    BUT_3 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.II.A"]')
    BUT_4 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.II.B"]')
    # III
    BUT_5 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.III.A"]')
    BUT_6 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.III.B"]')
    # IV
    BUT_7 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.IV.A"]')
    BUT_8 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.IV.B"]')
    # V
    BUT_9 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.V.A"]')
    BUT_10 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.V.B"]')
    # VI
    BUT_11 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.VI.A"]')
    BUT_12 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.VI.B"]')
    # VII
    BUT_13 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.VII.A"]')
    BUT_14 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.VII.B"]')
    # VIII
    BUT_15 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.VIII.A"]')
    BUT_16 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.VIII.B"]')
    # IX
    BUT_17 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.IX.A"]')
    BUT_18 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.IX.B"]')
    # X
    BUT_19 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.X.A"]')
    BUT_20 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.X.B"]')
    # XI
    BUT_21 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.XI.A"]')
    BUT_22 = (By.XPATH, '//*[@name="fnoContent.exciseTaxForStructuralDivision._009.XI.B"]')

    # 4 СТРАНИЦА
    CODE_OGD = (By.XPATH, '//*[text()="Код"]')
    CODE_OGD_SELECT = (By.XPATH, '//*[@title="0301"]')
    CONFIRM = (By.XPATH, '//*[text() = "Я несу ответственность в соответствии с законами Республики Казахстан за '
                         'достоверность и полноту сведений, приведенных в данном Расчете."]')
    FORM = (By.XPATH, '//*[text() = "Сформировать"]')

    # 2 СТРАНИЦА (2 ПРИЛОЖЕНИЕ)
    ADD_STR = (By.XPATH, '//*[text() = "Добавить строку"]')
    B = (By.XPATH, '//*[@name="B"]')
    B_SELECT = (By.XPATH, '//*[text() = "Все виды спирта и (или) виноматериала, алкогольной продукции, ввозимых на '
                          'территорию РК с терр. государств-членов ТС"]')
    C = (By.XPATH, '//*[@name="C"]')
    C_SELECT = (By.XPATH, '//*[@label="Бюджетное изъятие из бюджета города астаны"]')
    D = (By.XPATH, '//*[@name="D"]')
    E = (By.XPATH, '//*[@name="E"]')
    ADD = (By.XPATH, '//*[text() = "Добавить"]')

    # 2 СТРАНИЦА (4 ПРИЛОЖЕНИЕ)
    # 421.04.001
    TAX_BASE_1 = (By.XPATH, '//*[@name="fnoContent.application_04._001.I.A"]')
    EXC_R_1 = (By.XPATH, '//*[@name="fnoContent.application_04._001.I.B"]')
    TAX_BASE_2 = (By.XPATH, '//*[@name="fnoContent.application_04._001.II.A"]')
    EXC_R_2 = (By.XPATH, '//*[@name="fnoContent.application_04._001.II.B"]')
    TAX_BASE_3 = (By.XPATH, '//*[@name="fnoContent.application_04._001.III.A"]')
    EXC_R_3 = (By.XPATH, '//*[@name="fnoContent.application_04._001.III.B"]')
    TAX_BASE_4 = (By.XPATH, '//*[@name="fnoContent.application_04._001.IV.A"]')
    EXC_R_4 = (By.XPATH, '//*[@name="fnoContent.application_04._001.IV.B"]')
    # 421.04.002
    TAX_BASE_5 = (By.XPATH, '//*[@name="fnoContent.application_04._002.I.A"]')
    EXC_R_5 = (By.XPATH, '//*[@name="fnoContent.application_04._002.I.B"]')
    TAX_BASE_6 = (By.XPATH, '//*[@name="fnoContent.application_04._002.II.A"]')
    EXC_R_6 = (By.XPATH, '//*[@name="fnoContent.application_04._002.II.B"]')
    TAX_BASE_7 = (By.XPATH, '//*[@name="fnoContent.application_04._002.III.A"]')
    EXC_R_7 = (By.XPATH, '//*[@name="fnoContent.application_04._002.III.B"]')
    TAX_BASE_8 = (By.XPATH, '//*[@name="fnoContent.application_04._002.IV.A"]')
    EXC_R_8 = (By.XPATH, '//*[@name="fnoContent.application_04._002.IV.B"]')
    TAX_BASE_9 = (By.XPATH, '//*[@name="fnoContent.application_04._002.V.A"]')
    EXC_R_9 = (By.XPATH, '//*[@name="fnoContent.application_04._002.V.B"]')
    TAX_BASE_10 = (By.XPATH, '//*[@name="fnoContent.application_04._002.VI.A"]')
    EXC_R_10 = (By.XPATH, '//*[@name="fnoContent.application_04._002.VI.B"]')
    # 421.04.004
    TAX_BASE_11 = (By.XPATH, '//*[@name="fnoContent.application_04._004.I.A"]')
    EXC_R_11 = (By.XPATH, '//*[@name="fnoContent.application_04._004.I.B"]')
    TAX_BASE_12 = (By.XPATH, '//*[@name="fnoContent.application_04._004.II.A"]')
    EXC_R_12 = (By.XPATH, '//*[@name="fnoContent.application_04._004.II.B"]')
    TAX_BASE_13 = (By.XPATH, '//*[@name="fnoContent.application_04._004.III.A"]')
    EXC_R_13 = (By.XPATH, '//*[@name="fnoContent.application_04._004.III.B"]')
    TAX_BASE_14 = (By.XPATH, '//*[@name="fnoContent.application_04._004.IV.A"]')
    EXC_R_14 = (By.XPATH, '//*[@name="fnoContent.application_04._004.IV.B"]')
    # 421.04.005
    TAX_BASE_15 = (By.XPATH, '//*[@name="fnoContent.application_04._005.I.A"]')
    EXC_R_15 = (By.XPATH, '//*[@name="fnoContent.application_04._005.I.B"]')
    TAX_BASE_16 = (By.XPATH, '//*[@name="fnoContent.application_04._005.II.A"]')
    EXC_R_16 = (By.XPATH, '//*[@name="fnoContent.application_04._005.II.B"]')
    TAX_BASE_17 = (By.XPATH, '//*[@name="fnoContent.application_04._005.III.A"]')
    EXC_R_17 = (By.XPATH, '//*[@name="fnoContent.application_04._005.III.B"]')
    TAX_BASE_18 = (By.XPATH, '//*[@name="fnoContent.application_04._005.IV.A"]')
    EXC_R_18 = (By.XPATH, '//*[@name="fnoContent.application_04._005.IV.B"]')
    TAX_BASE_19 = (By.XPATH, '//*[@name="fnoContent.application_04._005.V.A"]')
    EXC_R_19 = (By.XPATH, '//*[@name="fnoContent.application_04._005.V.B"]')
    TAX_BASE_20 = (By.XPATH, '//*[@name="fnoContent.application_04._005.VI.A"]')
    EXC_R_20 = (By.XPATH, '//*[@name="fnoContent.application_04._005.VI.B"]')
    # 421.03.007 Сумма вычета, итого
    BUDG_QUAL_CODE = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div[15]/div[1]/div/div/div['
                                '2]/div[1]/div/div/div/span[1]')
    BUDG_QUAL_CODE_SELECT = (By.XPATH, '//*[@label="Бюджетное изъятие из бюджета города астаны"]')

    VOL_EXC = (By.XPATH, '//*[@name="fnoContent.application_04._007.I.B"]')
    SUM_EXC = (By.XPATH, '//*[@name="fnoContent.application_04._007.I.C"]')
    BUDG_QUAL_CODE_2 = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div[16]/div[1]/div/div/div['
                                  '2]/div[1]/div/div/div/span[1]')
    BUDG_QUAL_CODE_2_SELECT = (By.XPATH, '//*[@label="Поступления арендной платы за пользование комплексом байконур"]')
    VOL_EXC_2 = (By.XPATH, '//*[@name="fnoContent.application_04._007.II.B"]')
    SUM_EXC_2 = (By.XPATH, '//*[@name="fnoContent.application_04._007.II.C"]')
