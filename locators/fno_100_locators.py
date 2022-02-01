from selenium.webdriver.common.by import By


class FNO100LocatorsName(object):
    # Названия локаторов в приложениях с добавлением строк
    # 1 ПРИЛОЖЕНИЕ
    ADD_STR = 'Добавление строки'
    B_APP_1 = 'B БИН/ИИН (Приложение 1)'
    C_APP_1 = 'C Код страны резиденства (Приложение 1)'
    C_SELECT_APP_1 = ''
    D_APP_1 = 'D Регистрационный номер нерезидента в стране резидентства (Приложение 1)'
    E_APP_1 = 'E Код вида расхода (Приложение 1)'
    E_SELECT_APP_1 = 'Выбор кода вида расхода (Приложение 1)'
    F_APP_1 = 'F Сумма (Приложение 1)'
    G_APP_1 = 'G Признак (Приложение 1)'
    G_SELECT_APP_1 = 'G Выбор признака (Приложение 1)'
    # 4 ПРИЛОЖЕНИЕ
    B_APP_4 = 'B Код вида международного договора (Приложение 2)'
    C_APP_4 = 'C Наименование международного договора (Приложение 2)'
    B_SELECT_APP_4 = 'Выбор кода вида международного договора (Приложение 2)'
    D_APP_4 = 'D Код страны, с которой РК заключен международный договор (Приложение 2)'
    D_SELECT_APP_4 = 'Выбор кода страны (Приложение 2)'
    E_APP_4 = 'E Доход, подлежащий освобождению от налогообложения (Приложение 2)'
    # 5 ПРИЛОЖЕНИЕ
    B_APP_5 = 'B Код страны'
    C_APP_5 = 'C Код вида доходов'
    D_APP_5 = 'D Код валюты'
    B_SELECT_3 = 'Выбор кода страны'
    C_SELECT_3 = 'Выбор кода вида доходов'
    D_SELECT_3 = 'Выбор кода валюты'
    E_APP_5 = 'E Сумма начисленных доходов из источников в иностранном государстве (в иностранной валюте)'
    F_APP_5 = 'F Сумма начисленных доходов из источников в иностранном государстве (в национальной валюте)'
    G_APP_5 = 'G В том числе сумма доходов от деятельности через постоянное учреждение в иностранном государстве (в ' \
              'иностранной валюте) '
    H_APP_5 = 'H В том числе сумма доходов от деятельности через постоянное учреждение в иностранном государстве (в ' \
              'национальной валюте) '
    I_APP_5 = 'I Сумма подоходного налога, подлежащего зачету'
    J_APP_5 = 'J Сумма вычетов постоянного учреждения в иностранном государстве ( в национальной валюте)'
    K_APP_5 = 'K Сумма управленческих и общеадминистративных  расходов резидента'
    # 9 ПРИЛОЖЕНИЕ
    B_APP_9 = 'B Наименование КИК или ПУ КИК (Приложение 9)'
    C_APP_9 = 'C Код страны регистрации (Приложение 9)'
    C_SELECT_APP_9 = 'Выбор кода страны (Приложение 9)'
    D_APP_9 = 'D Номер государственной (налоговой) регистрации КИК или ПУ КИК (Приложение 9)'
    E_APP_9 = 'E Коэффициент участия или контроля (Приложение 9)'
    F_APP_9 = 'F Код валюты (Приложение 9)'
    F_SELECT_APP_9 = 'Выбор кода валюты (Приложение 9)'
    G_APP_9 = 'G Финансовая прибыль до налогообложения (в иностранной валюте) (Приложение 9)'
    H_APP_9 = 'H Сумма уменьшений (в иностранной валюте) (Приложение 9)'
    I_APP_9 = 'I Финансовая прибыль с учетом уменьшений в иностранной валюте (Приложение 9)'
    J_APP_9 = 'J Сконцентрированная финансовая прибыль до налогооблажения в иностранной валюте (Приложение 9)'
    K_APP_9 = 'K Финансовая прибыль, подлежащая налогообложению в иностранной валюте (Приложение 9)'
    L_APP_9 = 'L Финансовая прибыль, подлежащая налогообложению в национальной валюте (Приложение 9)'
    M_APP_9 = 'M Сумма иностранного налога на прибыль по финансовой отчетности в иностранной валюте (Приложение 9)'
    N_APP_9 = 'N Сумма уплаченного иностранного налога на прибыль в иностранной валюте (Приложение 9)'
    O_APP_9 = 'O Сумма иностранного налога на прибыль, подлежащая отнесению в зачет, в национальной валюте (' \
              'Приложение 9) '
    P_APP_9 = 'P Доходы из источников в Республике Казахстан в национальной валюте (Приложение 9)'
    Q_APP_9 = 'Q Корпоративный подоходный налог, удержанный у источника выплаты (Приложение 9)'
    # 11 ПРИЛОЖЕНИЕ
    B_APP_11 = 'B БИН юридического лица / ИИН физического лица (Приложение 11)'
    C_APP_11 = 'C Код страны регистрации (Приложение 11)'
    C_SELECT_APP_11 = 'Выбор кода страны резидентства (Приложение 11)'
    D_APP_11 = 'D Номер государственной (налоговой) регистрации КИК или ПУ КИК (Приложение 11)'
    E_APP_11 = 'E Коэффициент участия или контроля (Приложение 11)'
    F_APP_11 = 'F Код валюты (Приложение 11)'
    G_A_APP_11 = 'G Номер документа (Приложение 11)'
    G_B_APP_11 = 'G Дата документа (Приложение 11)'
    E_SELECT_APP_11 = 'Выбор вида переданного имущества (Приложение 11)'
    F_SELECT_APP_11 = 'Выбор кода имущества (Приложение 11)'
    H_APP_11 = 'H Сумма безвозмездно полученного имущества (Приложение 11)'
    I_APP_11 = 'I Сумма безвозмездно переданного имущества (Приложение 11)'
    G_DATE_SELECT_APP_11 = 'Выбор даты документа (Приложение 11)'
    # 2 СТРАНИЦА
    REAL_INCOME_1 = 'I доход в виде вознаграждения по кредиту(займу, микрокредиту), операциям репо'
    REAL_INCOME_2 = 'II доход в виде вознаграждения по передаче имущества в финансовый лизинг'
    REAL_INCOME_3 = 'III роялти'
    REAL_INCOME_4 = 'IV доход от сдачи имущества в аренду'
    INCOME_2 = '100.00.002 Доход от прироста стоимости'
    INCOME_3 = '100.00.003 Доход от списания обязательств'
    INCOME_4 = '100.00.004 Доход по сомнительным обязательствам'
    INCOME_5 = '100.00.005 Доход от страховой, перестраховочной организации по договорам страхования, перестрахования'
    INCOME_6 = '100.00.006 Доход от снижения размеров созданных провизий (резервов)'
    INCOME_6_I = 'I в соответствии с пунктом 1 статьи 232 Налогового кодекса'
    INCOME_7_I = 'I по приобретенному праву требования (100.00.007)'
    INCOME_7_II = 'II по уступленному праву требования (100.00.007)'
    INCOME_8 = '100.00.008 Доход от выбытия фиксированных активов'
    INCOME_9 = '100.00.009 Полученные компенсации по ранее произведенным вычетам'
    INCOME_10 = '100.00.010 Доход в виде безвозмездно полученного имущества'
    INCOME_11 = '100.00.011 Доход, полученный при эксплуатации объектов социальной сферы'
    INCOME_12 = '100.00.012 Доход (убыток) от продажи предприятия как имущественного комплекса'
    INCOME_13 = '100.00.013 Доход некоммерческой организации, предусмотренный пунктом 2 статьи 289 Налогового кодекса'
    INCOME_14 = '100.00.014 Прочие доходы'

    # 3 СТРАНИЦА
    # Раздел. Корректировка совокупного годового дохода
    CORR_INCOME_1 = '100.00.016 Корректировка совокупного годового дохода в соответствии с пунктом 1 статьи 241 ' \
                    'Налогового кодекса, в том числе: '
    CORR_INCOME_2 = 'Поле I, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_3 = 'Поле II, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_4 = 'Поле III, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_5 = 'Поле IV, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_6 = 'Поле V, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_7 = 'Поле VI, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_8 = 'Поле VII, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_9 = 'Поле VIII, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_10 = 'Поле IX, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_11 = 'Поле X, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_12 = 'Поле XI, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_13 = 'Поле XII, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_14 = 'Поле XIII, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_15 = 'Поле XIV, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_16 = 'Поле XV, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_17 = 'Поле XVI, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_18 = 'Поле XVII, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_19 = 'Поле XVIII, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_20 = 'Поле XIX, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_21 = 'Поле XX, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_22 = 'Поле XXI, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_23 = 'Поле XXII, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_24 = 'Поле XXIII, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_25 = 'Поле XXIV, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_26 = 'Поле XXV, Раздел. Корректировка совокупного годового дохода'
    CORR_INCOME_27 = 'Поле I, Раздел. Корректировка совокупного годового дохода'
    # 4 СТРАНИЦА
    # Раздел. Вычеты
    STOCK_1 = 'I Запасы на начало налогового периода всего'
    STOCK_2 = 'II Запасы на конец налогового периода всего'
    STOCK_3 = 'III Приобретено запасов, работ и услуг всего, в том числе'
    # III раздел
    SERVICE_1 = 'A запасы'
    SERVICE_2 = 'B финансовые услуги'
    SERVICE_3 = 'C рекламные услуги'
    SERVICE_4 = 'D консультационные услуги'
    SERVICE_5 = 'E маркетинговые услуги'
    SERVICE_6 = 'F дизайнерские услуги'
    SERVICE_7 = 'G инжиниринговые услуги'
    SERVICE_8 = 'H прочие услуги и работы'
    # IV и далее
    STOCK_4 = 'Поле 4, Раздел. Вычеты (4 страница)'
    STOCK_5 = 'Поле 5, Раздел. Вычеты (4 страница)'
    STOCK_6 = 'Поле 6, Раздел. Вычеты (4 страница)'
    STOCK_7 = 'Поле 7, Раздел. Вычеты (4 страница)'
    STOCK_8 = 'Поле 8, Раздел. Вычеты (4 страница)'
    STOCK_9 = 'Поле 9, Раздел. Вычеты (4 страница)'
    # 100.00.020 и далее
    FIELD_1 = 'Поле 100.00.020'
    FIELD_2 = 'Поле 100.00.021'
    FIELD_3 = 'Поле 100.00.022'
    FIELD_4 = 'Поле 100.00.023'
    FIELD_5 = 'Поле 100.00.024'
    FIELD_6 = 'Поле 100.00.025'
    FIELD_7 = 'Поле 100.00.026'
    FIELD_8 = 'Поле 100.00.027'
    # 100.00.028 и далее
    LOANS_1 = 'I депозитов, включая остатки на корреспондентских счетах, размещенных в банках (100.00.028)'
    LOANS_2 = 'II кредитов (за исключением финансового лизинга), предоставленных банкам и клиентам (100.00.028)'
    LOANS_3 = 'III дебиторской задолженности по документарным расчетам и гарантиям (100.00.028)'
    LOANS_4 = 'IV условных обязательств по непокрытым аккредитивам, выпущенным или подтвержденным гарантиям (' \
              '100.00.028) '
    FIELD_9 = '100.00.029 Вычеты страховой, перестраховочной организации'
    FIELD_10 = '100.00.030 Вычет по уменьшению активов перестрахования'
    FIELD_11 = '100.00.031 Вычеты по расходам на ликвидацию полигонов размещения отходов и сумм отчислений в ' \
               'ликвидационный фонд полигонов размещения отходов '
    FIELD_12 = '100.00.032 Вычеты по расходам на научно-исследовательские, научно-технические работы и приобретение ' \
               'исключительных прав на объекты интеллектуальной собственности '
    FIELD_13 = '100.00.033'
    FIELD_14 = '100.00.034'
    FIELD_15 = '100.00.035'
    FIELD_16 = '100.00.036'
    FIELD_17_I = '100.00.037_I'
    FIELD_17_II = '100.00.037_II'
    FIELD_18 = '100.00.038'
    FIELD_19 = '100.00.039'
    FIELD_20_I = '100.00.040_I'
    FIELD_20_II = '100.00.040_II'
    FIELD_20_III = '100.00.040_III'
    FIELD_20_IV = '100.00.040_IV'
    # 5 СТРАНИЦЫ НЕТ, НИЖЕ 6 СТРАНИЦА
    # 100.00.052 Уменьшение налогооблагаемого дохода в соответствии со статьей 288 Налогового кодекса, в том числе:
    FIELD_21_I = '100.00.052 I'
    FIELD_21_I_A = '100.00.052 A'
    FIELD_21_I_B = '100.00.052 B'
    FIELD_21_II = '100.00.052 II'
    FIELD_22 = '100.00.056Ставка КПН(%)'
    FIELD_23_III = '100.00.058 III'
    FIELD_23_IV = '100.00.058 IV'
    FIELD_23_V = '100.00.058 V'
    FIELD_23_VI = '100.00.058 VI'
    # 100.00.59 Исчисленная сумма КПН с учетом уменьшения
    FIELD_24 = '100.00.59 Исчисленная сумма КПН с учетом уменьшения'
    # 100.00.061 КПН на чистый доход, исчисленный
    FIELD_25_A = '100.00.061 II процент'
    FIELD_25_B = '100.00.061 II процент (сумма)'
    FIELD_25_III = '100.00.061 III'
    FIELD_25_IV = '100.00.061 IV'
    # ПРИЛОЖЕНИЕ 1
    B = 'B БИН/ИИН'
    D = 'D Номер налоговой регистрации в стране резидентства нерезидента'
    F = 'F Сумма'
    # ПРИЛОЖЕНИЕ 2
    GROUP_1 = '100.02.001 I'
    GROUP_2 = '100.02.001 II'
    GROUP_3 = '100.02.001 III'
    GROUP_4 = '100.02.001 IV'
    GROUP_5 = '100.02.002 I'
    GROUP_6 = '100.02.002 II'
    GROUP_7 = '100.02.002 III'
    GROUP_8 = '100.02.002 IV'
    GROUP_9 = '100.02.003 I'
    GROUP_10 = '100.02.003 II'
    GROUP_11 = '100.02.003 III'
    GROUP_12 = '100.02.003 IV'
    GROUP_13 = '100.02.004 I'
    GROUP_14 = '100.02.004 II'
    GROUP_15 = '100.02.004 III'
    GROUP_16 = '100.02.004 IV'
    GROUP_17 = '100.02.005 I'
    GROUP_18 = '100.02.005 II'
    GROUP_19 = '100.02.005 III'
    GROUP_20 = '100.02.005 IV'
    GROUP_21 = '100.02.006 I'
    GROUP_22 = '100.02.006 II'
    GROUP_23 = '100.02.006 III'
    GROUP_24 = '100.02.006 IV'
    GROUP_25 = '100.02.007 I'
    GROUP_26 = '100.02.007 II'
    GROUP_27 = '100.02.007 III'
    GROUP_28 = '100.02.007 IV'
    GROUP_29 = '100.02.008 I'
    GROUP_30 = '100.02.008 II'
    GROUP_31 = '100.02.008 III'
    GROUP_32 = '100.02.008 IV'
    GROUP_33 = '100.02.009 I'
    GROUP_34 = '100.02.009 II'
    GROUP_35 = '100.02.009 III'
    GROUP_36 = '100.02.009 IV'
    GROUP_37 = '100.02.010 I'
    GROUP_38 = '100.02.010 II'
    GROUP_39 = '100.02.010 III'
    GROUP_40 = '100.02.010 IV'
    EXPENSES = '100.02.012'
    # ПРИЛОЖЕНИЕ 6
    YEAR_EXPENSE = '100.06.001 СОВОКУПНЫЙ ГОДОВОЙ ДОХОД, в том числе:'
    STR_1 = '100.06.002'
    STR_2 = '100.06.003'
    STR_3_I = '100.06.005 I'
    STR_3_II = '100.06.005 II'
    STR_4 = '100.06.006'
    STR_5 = '100.06.007'
    STR_6 = '100.06.008'
    STR_7 = '100.06.009'
    STR_8 = '100.06.011'
    STR_9_I = '100.06.012 I'
    STR_9_II = '100.06.012 II'
    STR_10 = '100.06.014'
    STR_11 = '100.06.016'
    STR_12 = '100.06.017'
    STR_13 = '100.06.018'
    STR_14 = '100.06.020'
    STR_15 = '100.06.022'
    STR_16_I = '100.06.024 I'
    STR_16_II = '100.06.024 II'
    STR_16_III = '100.06.024 III'
    STR_16_IV = '100.06.024 IV'
    STR_16_V = '100.06.024 V'
    STR_16_VI = '100.06.024 VI'
    STR_16_VII = '100.06.024 VII'
    STR_17_I = '100.06.025 I'
    PERCENT_2 = 'по ставке предусмотренной международным договором (B)'

    # ПРИЛОЖЕНИЕ 7
    # Раздел Активы
    START_1 = '100.07.001 START'
    END_1 = '100.07.001 END'
    START_2 = '100.07.002 START'
    END_2 = '100.07.002 END'
    START_3 = '100.07.003 START'
    END_3 = '100.07.003 END'
    START_4 = '100.07.004 START'
    END_4 = '100.07.004 END'
    START_5 = '100.07.005 START'
    END_5 = '100.07.005 END'
    START_6 = '100.07.006 START'
    END_6 = '100.07.006 END'
    START_7 = '100.07.007 START'
    END_7 = '100.07.007 END'
    START_8 = '100.07.008 START'
    END_8 = '100.07.008 END'
    START_9 = '100.07.009 START'
    END_9 = '100.07.009 END'
    START_10 = '100.07.010 START'
    END_10 = '100.07.010 END'
    START_11 = '100.07.011 START'
    END_11 = '100.07.011 END'
    START_12 = '100.07.012 START'
    END_12 = '100.07.012 END'
    START_13 = '100.07.013 START'
    END_13 = '100.07.013 END'
    START_14 = '100.07.014 START'
    END_14 = '100.07.014 END'
    START_15 = '100.07.015 START'
    END_15 = '100.07.015 END'
    START_16 = '100.07.016 START'
    END_16 = '100.07.016 END'
    START_17 = '100.07.017 START'
    END_17 = '100.07.017 END'
    # Раздел Обязательства
    START_19 = '100.07.019 START'
    END_19 = '100.07.019 END'
    START_20 = '100.07.020 START'
    END_20 = '100.07.020 END'
    START_21 = '100.07.021 START'
    END_21 = '100.07.021 END'
    START_22 = '100.07.022 START'
    END_22 = '100.07.022 END'
    START_23 = '100.07.023 START'
    END_23 = '100.07.023 END'
    START_24 = '100.07.024 START'
    END_24 = '100.07.024 END'
    START_25 = '100.07.025 START'
    END_25 = '100.07.025 END'
    START_26 = '100.07.026 START'
    END_26 = '100.07.026 END'
    START_27 = '100.07.027 START'
    END_27 = '100.07.027 END'
    START_28 = '100.07.028 START'
    END_28 = '100.07.028 END'
    START_29 = '100.07.029 START'
    END_29 = '100.07.029 END'
    # Раздел Капитал
    START_31 = '100.07.031 START'
    END_31 = '100.07.031 END'
    START_32 = '100.07.032 START'
    END_32 = '100.07.032 END'
    START_33 = '100.07.033 START'
    END_33 = '100.07.033 END'
    START_34 = '100.07.034 START'
    END_34 = '100.07.034 END'
    START_35 = '100.07.035 START'
    END_35 = '100.07.035 END'
    START_36 = '100.07.036 START'
    END_36 = '100.07.036 END'
    START_37 = '100.07.037 START'
    END_37 = '100.07.037 END'
    # 8 ПРИЛОЖЕНИЕ
    EIGHT_PAGE_1 = '100.08.001 Остаток на начало года'
    EIGHT_PAGE_2 = '100.08.002 A'
    EIGHT_PAGE_3 = '100.08.002 B'
    EIGHT_PAGE_4 = '100.08.002 C'
    EIGHT_PAGE_5 = '100.08.002 D'
    EIGHT_PAGE_6 = '100.08.003 A'
    EIGHT_PAGE_7 = '100.08.003 B'
    EIGHT_PAGE_8 = '100.08.003 C'
    EIGHT_PAGE_9 = '100.08.003 D'
    EIGHT_PAGE_10 = '100.08.003 E'
    EIGHT_PAGE_11 = '100.08.003 F'
    # 10 ПРИЛОЖЕНИЕ
    # Разделю. Доходы
    TEN_PAGE_1 = '100.10.001 Вознаграждения по депозитам'
    TEN_PAGE_2 = '100.10.002 Гранты'
    TEN_PAGE_3 = '100.10.003 Вступительные взносы'
    TEN_PAGE_4 = '100.10.004 Членские взносы'
    TEN_PAGE_5 = '100.10.005 Взносы участников кондоминиума'
    TEN_PAGE_6 = '100.10.006 Благотворительная помощь'
    TEN_PAGE_7 = '100.10.007 Спонсорская помощь'
    TEN_PAGE_8 = '100.10.008 Деньги и другое имущество, полученные на безвозмездной основе'
    TEN_PAGE_9 = '100.10.009 Превышение суммы положительной курсовой разницы над суммой отрицательной курсовой ' \
                 'разницы, возникшей по размещенным на депозите деньгам, в том числе по вознаграждениям по ним '
    TEN_PAGE_10 = '100.10.010 Доход, полученный по договору на осуществление государственного социального заказа'
    TEN_PAGE_11 = '100.10.011 Всего доходов'
    TEN_PAGE_12 = '100.10.012 Другие доходы, не указанные в пункте 2 статьи 289 Налогового кодекса'
    #
    TEN_PAGE_14_I = '100.10.014 I'
    TEN_PAGE_14_II = '100.10.014 II'
    TEN_PAGE_14_III = '100.10.014 III'
    TEN_PAGE_14_IV = '100.10.014 IV'
    TEN_PAGE_14_V = '100.10.014 V'
    TEN_PAGE_14_VI = '100.10.014 VI'
    TEN_PAGE_14_VII = '100.10.014 VII'
    TEN_PAGE_14_VIII = '100.10.014 VIII'
    TEN_PAGE_14_IX = '100.10.014 IX'
    TEN_PAGE_14_X = '100.10.014 X'
    TEN_PAGE_14_XI = '100.10.014 XI'
    TEN_PAGE_14_XII = '100.10.014 XII'
    TEN_PAGE_14_XIII = '100.10.014 XIII'
    TEN_PAGE_14_XIV = '100.10.014 XIV'
    TEN_PAGE_14_XV = '100.10.014 XV'
    TEN_PAGE_14_XVI = '100.10.014 XVI'
    TEN_PAGE_14_XVII = '100.10.014 XVII'
    TEN_PAGE_14_XVIII = '100.10.014 XVIII'
    TEN_PAGE_14_XIX = '100.10.014 XIX'
    TEN_PAGE_14_XIX_A = '100.10.014 XIX A'
    TEN_PAGE_14_XIX_B = '100.10.014 XIX B'
    TEN_PAGE_14_XIX_C = '100.10.014 XIX C'
    TEN_PAGE_14_XIX_D = '100.10.014 XIX D'
    TEN_PAGE_14_XIX_E = '100.10.014 XIX E'
    TEN_PAGE_14_XX = '100.10.014 XX'
    TEN_PAGE_14_XXI = '100.10.014 XXI'
    TEN_PAGE_15_I = '100.10.015 I'
    TEN_PAGE_15_II = '100.10.015 II'
    TEN_PAGE_15_III = '100.10.015 III'
    TEN_PAGE_15_IV = '100.10.015 IV'
    TEN_PAGE_15_V = '100.10.015 V'
    TEN_PAGE_15_VI = '100.10.015 VI'
    TEN_PAGE_15_VII = '100.10.015 VII'
    TEN_PAGE_15_VIII = '100.10.015 VIII'
    TEN_PAGE_15_IX = '100.10.015 IX'
    TEN_PAGE_15_X = '100.10.015 X'
    TEN_PAGE_15_XI = '100.10.015 XI'
    TEN_PAGE_16 = '100.10.016'
    TEN_PAGE_17 = '100.10.017'
    TEN_PAGE_18 = '100.10.018'
    TEN_PAGE_19 = '100.10.019'
    TEN_PAGE_20 = '100.10.020'
    TEN_PAGE_21 = '100.10.021'
    TEN_PAGE_22 = '100.10.022'

    # ПРИЛОЖЕНИЕ 12
    # Раздел. Доходы от оказания финансовых услуг, предусмотренных пунктом 3 статьи 6 Конституционного закона
    TWELVE_PAGE_1 = '100.12.001'
    TWELVE_PAGE_2 = '100.12.002'
    TWELVE_PAGE_3 = '100.12.003'
    TWELVE_PAGE_4 = '100.12.004'
    TWELVE_PAGE_5 = '100.12.005'
    # Раздел. Доходы от оказания сопутствующих услуг, предусмотренных пунктом 4 статьи 6 Конституционного закона
    TWELVE_PAGE_7 = '100.12.007'
    TWELVE_PAGE_8 = '100.12.008'
    TWELVE_PAGE_9 = '100.12.009'
    TWELVE_PAGE_10 = '100.12.010'
    # Раздел. Доходы, освобождаемые от налогообложения согласно пункту 7 статьи 6 Конституционного закона
    TWELVE_PAGE_12 = '100.12.012'


class FNO100Locators(object):
    DECLARATION_TYPE = (By.XPATH, '//*[@name="declarationTypes"]')
    DECLARATION_TYPE_SELECT = (By.XPATH, '//*[@title="Первоначальная"]')
    TAX_PAYER_CATEGORIES = (By.XPATH, '//*[@name="taxpayerCategories"]')
    TAX_PAYER_CATEGORIES_SELECT = (By.XPATH, '//*[text()="Доверительный управляющий"]')
    RESIDENT = (By.XPATH, '//*[@id="rc_select_2"]')
    RESIDENT_SELECT = (By.XPATH, '//*[@title="Резидент РК"]')
    # Участник МФЦА в соответствии с Конституционным законом РК "О МФЦА"
    CONFIRM_1 = (By.XPATH, '//*[@name="fnoContent.commonInfo._7"]')
    # Наличие у резидента постоянного учреждения за пределами Республики Казахстан
    CONFIRM_2 = (By.XPATH, '//*[@name="fnoContent.commonInfo._12"]')
    # Представленные приложения к налоговой отчетности
    APPS = (By.XPATH, '//*[@id="root"]/div/div[4]/div[4]/div/div/div[4]/form/div[8]/div[2]/div[1]/div/div/div[1]')
    # Приложения
    APP_1 = (By.XPATH, '//*[text() = "Выбрать все"]')
    APP_2 = (By.XPATH, '//*[text() = "Приложение 100.02"]')
    APP_3 = (By.XPATH, '//*[text() = "Приложение 100.03"]')
    APP_4 = (By.XPATH, '//*[text() = "Приложение 100.04"]')
    APP_5 = (By.XPATH, '//*[text() = "Приложение 100.05"]')
    APP_6 = (By.XPATH, '//*[text() = "Приложение 100.06"]')
    APP_7 = (By.XPATH, '//*[text() = "Приложение 100.07"]')
    APP_8 = (By.XPATH, '//*[text() = "Приложение 100.08"]')
    APP_9 = (By.XPATH, '//*[text() = "Приложение 100.09"]')
    APP_10 = (By.XPATH, '//*[text() = "Приложение 100.10"]')
    APP_11 = (By.XPATH, '//*[text() = "Приложение 100.11"]')
    APP_12 = (By.XPATH, '//*[text() = "Приложение 100.12"]')
    CONTROL_TEXT2 = (By.XPATH, '//*[text() = "© 2021 Комитет государственных доходов МФ РК"]')
    AFTER = (By.XPATH, '//*[text() = "Далее"]')

    # 2 страница
    # Раздел. Совокупный годовой доход
    REAL_INCOME_1 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._001.I"]')
    REAL_INCOME_2 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._001.II"]')
    REAL_INCOME_3 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._001.III"]')
    REAL_INCOME_4 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._001.IV"]')
    # Раздел с 100.00.002 по 100.00.014
    INCOME_2 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._002"]')
    INCOME_3 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._003"]')
    INCOME_4 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._004"]')
    INCOME_5 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._005"]')
    INCOME_6 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._006.total"]')
    INCOME_6_I = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._006.I"]')
    INCOME_7_I = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._007.I"]')
    INCOME_7_II = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._007.II"]')
    INCOME_8 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._008"]')
    INCOME_9 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._009"]')
    INCOME_10 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._010"]')
    INCOME_11 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._011"]')
    INCOME_12 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._012"]')
    INCOME_13 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._013"]')
    INCOME_14 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncome._014"]')
    # 3 страница
    # Раздел. Корректировка совокупного годового дохода
    # 100.00.016
    CORR_INCOME_1 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.total"]')
    CORR_INCOME_2 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.I"]')
    CORR_INCOME_3 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.II"]')
    CORR_INCOME_4 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.III"]')
    CORR_INCOME_5 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.IV"]')
    CORR_INCOME_6 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.V"]')
    CORR_INCOME_7 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.VI"]')
    CORR_INCOME_8 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.VII"]')
    CORR_INCOME_9 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.VIII"]')
    CORR_INCOME_10 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.IX"]')
    CORR_INCOME_11 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.X"]')
    CORR_INCOME_12 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.XI"]')
    CORR_INCOME_13 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.XII"]')
    CORR_INCOME_14 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.XIII"]')
    CORR_INCOME_15 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.XIV"]')
    CORR_INCOME_16 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.XV"]')
    CORR_INCOME_17 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.XVI"]')
    CORR_INCOME_18 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.XVII"]')
    CORR_INCOME_19 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.XVIII"]')
    CORR_INCOME_20 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.XIX"]')
    CORR_INCOME_21 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.XX"]')
    CORR_INCOME_22 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.XXI"]')
    CORR_INCOME_23 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.XXII"]')
    CORR_INCOME_24 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.XXIII"]')
    CORR_INCOME_25 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.XXIV"]')
    CORR_INCOME_26 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._016.XXV"]')
    # 100.00.017 Корректировка совокупного годового дохода в соответствии с пунктом 3 статьи 241 Налогового кодекса
    CORR_INCOME_27 = (By.XPATH, '//*[@name="fnoContent.totalAnnualIncomeAdjustment._017"]')
    # 4 страница
    # 100.00.019 Расходы по реализованным товарам (работам, услугам)
    STOCK_1 = (By.XPATH, '//*[@name="fnoContent.deduction._019.I"]')
    STOCK_2 = (By.XPATH, '//*[@name="fnoContent.deduction._019.II"]')
    # STOCK_3 = (By.XPATH, '//*[@name="fnoContent.deduction._019.III.total"]')
    # III раздел
    SERVICE_1 = (By.XPATH, '//*[@name="fnoContent.deduction._019.III.A"]')
    SERVICE_2 = (By.XPATH, '//*[@name="fnoContent.deduction._019.III.B"]')
    SERVICE_3 = (By.XPATH, '//*[@name="fnoContent.deduction._019.III.C"]')
    SERVICE_4 = (By.XPATH, '//*[@name="fnoContent.deduction._019.III.D"]')
    SERVICE_5 = (By.XPATH, '//*[@name="fnoContent.deduction._019.III.E"]')
    SERVICE_6 = (By.XPATH, '//*[@name="fnoContent.deduction._019.III.F"]')
    SERVICE_7 = (By.XPATH, '//*[@name="fnoContent.deduction._019.III.G"]')
    SERVICE_8 = (By.XPATH, '//*[@name="fnoContent.deduction._019.III.H"]')
    # IV Расходы по начисленным доходам работников и иным выплатам физическим лицам до IX
    STOCK_4 = (By.XPATH, '//*[@name="fnoContent.deduction._019.IV"]')
    STOCK_5 = (By.XPATH, '//*[@name="fnoContent.deduction._019.V"]')
    STOCK_6 = (By.XPATH, '//*[@name="fnoContent.deduction._019.VI"]')
    STOCK_7 = (By.XPATH, '//*[@name="fnoContent.deduction._019.VII"]')
    STOCK_8 = (By.XPATH, '//*[@name="fnoContent.deduction._019.VIII"]')
    STOCK_9 = (By.XPATH, '//*[@name="fnoContent.deduction._019.IX"]')
    # 100.00.020 Штрафы, пени, неустойки
    FIELD_1 = (By.XPATH, '//*[@name="fnoContent.deduction._020"]')
    FIELD_2 = (By.XPATH, '//*[@name="fnoContent.deduction._021"]')
    FIELD_3 = (By.XPATH, '//*[@name="fnoContent.deduction._022"]')
    FIELD_4 = (By.XPATH, '//*[@name="fnoContent.deduction._023"]')
    FIELD_5 = (By.XPATH, '//*[@name="fnoContent.deduction._024"]')
    FIELD_6 = (By.XPATH, '//*[@name="fnoContent.deduction._025"]')
    FIELD_7 = (By.XPATH, '//*[@name="fnoContent.deduction._026"]')
    FIELD_8 = (By.XPATH, '//*[@name="fnoContent.deduction._027"]')
    # 100.00.028 Вычеты по отчислениям в резервные фонды в соответствии со статьей 250 Налогового кодекса, в том числе
    LOANS_1 = (By.XPATH, '//*[@name="fnoContent.deduction._028.I"]')
    LOANS_2 = (By.XPATH, '//*[@name="fnoContent.deduction._028.II"]')
    LOANS_3 = (By.XPATH, '//*[@name="fnoContent.deduction._028.III"]')
    LOANS_4 = (By.XPATH, '//*[@name="fnoContent.deduction._028.IV"]')
    # 100.00.029 Вычеты страховой, перестраховочной организации
    FIELD_9 = (By.XPATH, '//*[@name="fnoContent.deduction._029"]')
    FIELD_10 = (By.XPATH, '//*[@name="fnoContent.deduction._030"]')
    FIELD_11 = (By.XPATH, '//*[@name="fnoContent.deduction._031"]')
    FIELD_12 = (By.XPATH, '//*[@name="fnoContent.deduction._032"]')
    FIELD_13 = (By.XPATH, '//*[@name="fnoContent.deduction._033"]')
    FIELD_14 = (By.XPATH, '//*[@name="fnoContent.deduction._034"]')
    FIELD_15 = (By.XPATH, '//*[@name="fnoContent.deduction._035"]')
    FIELD_16 = (By.XPATH, '//*[@name="fnoContent.deduction._036"]')
    # 100.00.037 Вычет сумм компенсаций при служебных командировках и поездах членов органа управления
    # налогоплательщика, в том числе:
    FIELD_17_I = (By.XPATH, '//*[@name="fnoContent.deduction._037.I"]')
    FIELD_17_II = (By.XPATH, '//*[@name="fnoContent.deduction._037.II"]')
    FIELD_18 = (By.XPATH, '//*[@name="fnoContent.deduction._038"]')
    FIELD_19 = (By.XPATH, '//*[@name="fnoContent.deduction._039"]')
    FIELD_20_I = (By.XPATH, '//*[@name="fnoContent.deduction._040.I"]')
    FIELD_20_II = (By.XPATH, '//*[@name="fnoContent.deduction._040.II"]')
    FIELD_20_III = (By.XPATH, '//*[@name="fnoContent.deduction._040.III"]')
    FIELD_20_IV = (By.XPATH, '//*[@name="fnoContent.deduction._040.IV"]')
    # 5 СТРАНИЦЫ НЕТ, НИЖЕ 6 СТРАНИЦА
    # 100.00.052 Уменьшение налогооблагаемого дохода в соответствии со статьей 288 Налогового кодекса, в том числе:
    FIELD_21_I = (By.XPATH, '//*[@name="fnoContent.calculationNodAndNO.calculationNod._052.I.total"]')
    FIELD_21_I_A = (By.XPATH, '//*[@name="fnoContent.calculationNodAndNO.calculationNod._052.I.A"]')
    FIELD_21_I_B = (By.XPATH, '//*[@name="fnoContent.calculationNodAndNO.calculationNod._052.I.B"]')
    FIELD_21_II = (By.XPATH, '//*[@name="fnoContent.calculationNodAndNO.calculationNod._052.II"]')
    FIELD_22 = (By.XPATH, '//*[@name="fnoContent.calculationNodAndNO.calculationNO._056"]')
    FIELD_23_III = (By.XPATH, '//*[@name="fnoContent.calculationNodAndNO.calculationNO._058.III"]')
    FIELD_23_IV = (By.XPATH, '//*[@name="fnoContent.calculationNodAndNO.calculationNO._058.IV"]')
    FIELD_23_V = (By.XPATH, '//*[@name="fnoContent.calculationNodAndNO.calculationNO._058.V"]')
    FIELD_23_VI = (By.XPATH, '//*[@name="fnoContent.calculationNodAndNO.calculationNO._058.VI"]')
    # 100.00.59 Исчисленная сумма КПН с учетом уменьшения
    FIELD_24 = (By.XPATH, '//*[@name="fnoContent.calculationNodAndNO.calculationNO._059.I"]')
    # 100.00.061 КПН на чистый доход, исчисленный
    FIELD_25_A = (By.XPATH, '//*[@name="fnoContent.calculationNodAndNO.calculationNO._061.II.A"]')
    FIELD_25_B = (By.XPATH, '//*[@name="fnoContent.calculationNodAndNO.calculationNO._061.II.B"]')
    FIELD_25_III = (By.XPATH, '//*[@class="ant-select-selector"]')
    FIELD_25_III_SELECT = (By.XPATH, '//*[text()="Афганистан"]')
    FIELD_25_IV = (By.XPATH, '//*[@name="fnoContent.calculationNodAndNO.calculationNO._061.IV"]')

    # ПРИЛОЖЕНИЯ С 1 ПО 12
    # ПРИЛОЖЕНИЕ 1
    ADD_STR = (By.XPATH, '//*[text()="Добавить строку"]')
    B_APP_1 = (By.XPATH, '//*[@name="B"]')
    C_APP_1 = (By.XPATH, '//*[@name="C"]')
    C_SELECT_APP_1 = (By.XPATH, '//*[text()="Афганистан"]')
    D_APP_1 = (By.XPATH, '//*[@name="D"]')
    E_APP_1 = (By.XPATH, '//*[@name="E"]')
    E_SELECT_APP_1 = (By.XPATH, '//*[text() = "Финансовые услуги"]')
    F_APP_1 = (By.XPATH, '//*[@name="F"]')
    G_APP_1 = (By.XPATH, '//*[@name="G"]')
    G_SELECT_APP_1 = (By.XPATH, '//*[@label="Если затраты (расходы) понесены исключительно в целях осуществления '
                                'деятельности, налогообложение которой осуществляется в рамках специального налогового '
                                'режима в соответствии со статьями 697, 698, 699, 700 и 701 Налогового кодекса"]')
    ADD = (By.XPATH, '//*[text() = "Добавить"]')
    # ПРИЛОЖЕНИЕ 2
    # Раздел. Вычеты по фиксированным активам
    # 100.02.001 Стоимостный баланс групп (подгрупп) на начало налогового периода
    GROUP_1 = (By.XPATH, '//*[@name="fnoContent.application_02._001.I"]')
    GROUP_2 = (By.XPATH, '//*[@name="fnoContent.application_02._001.II"]')
    GROUP_3 = (By.XPATH, '//*[@name="fnoContent.application_02._001.III"]')
    GROUP_4 = (By.XPATH, '//*[@name="fnoContent.application_02._001.IV"]')
    # 100.02.002 Стоимость поступивших фиксированных активов
    GROUP_5 = (By.XPATH, '//*[@name="fnoContent.application_02._002.I"]')
    GROUP_6 = (By.XPATH, '//*[@name="fnoContent.application_02._002.II"]')
    GROUP_7 = (By.XPATH, '//*[@name="fnoContent.application_02._002.III"]')
    GROUP_8 = (By.XPATH, '//*[@name="fnoContent.application_02._002.IV"]')
    # 100.02.003 Стоимость выбывших фиксированных активов
    GROUP_9 = (By.XPATH, '//*[@name="fnoContent.application_02._003.I"]')
    GROUP_10 = (By.XPATH, '//*[@name="fnoContent.application_02._003.II"]')
    GROUP_11 = (By.XPATH, '//*[@name="fnoContent.application_02._003.III"]')
    GROUP_12 = (By.XPATH, '//*[@name="fnoContent.application_02._003.IV"]')
    # 100.02.004 Последующие расходы по фиксированным активам, относимые на увеличение стоимостных балансов групп (
    # подгрупп) в соответствии с пунктом 2 статьи 272 Налогового кодекса
    GROUP_13 = (By.XPATH, '//*[@name="fnoContent.application_02._004.I"]')
    GROUP_14 = (By.XPATH, '//*[@name="fnoContent.application_02._004.II"]')
    GROUP_15 = (By.XPATH, '//*[@name="fnoContent.application_02._004.III"]')
    GROUP_16 = (By.XPATH, '//*[@name="fnoContent.application_02._004.IV"]')
    # 100.02.005 Стоимостной баланс групп (подгрупп) на конец налогового периода
    GROUP_17 = (By.XPATH, '//*[@name="fnoContent.application_02._005.I"]')
    GROUP_18 = (By.XPATH, '//*[@name="fnoContent.application_02._005.II"]')
    GROUP_19 = (By.XPATH, '//*[@name="fnoContent.application_02._005.III"]')
    GROUP_20 = (By.XPATH, '//*[@name="fnoContent.application_02._005.IV"]')
    # 100.02.006 Амортизационные отчисления по фиксированным активам
    GROUP_21 = (By.XPATH, '//*[@name="fnoContent.application_02._006.I"]')
    GROUP_22 = (By.XPATH, '//*[@name="fnoContent.application_02._006.II"]')
    GROUP_23 = (By.XPATH, '//*[@name="fnoContent.application_02._006.III"]')
    GROUP_24 = (By.XPATH, '//*[@name="fnoContent.application_02._006.IV"]')
    # 100.02.007 Двойная норма амортизации в соответствии с пунктом 7 статьи 271 Налогового кодекса
    GROUP_25 = (By.XPATH, '//*[@name="fnoContent.application_02._007.I"]')
    GROUP_26 = (By.XPATH, '//*[@name="fnoContent.application_02._007.II"]')
    GROUP_27 = (By.XPATH, '//*[@name="fnoContent.application_02._007.III"]')
    GROUP_28 = (By.XPATH, '//*[@name="fnoContent.application_02._007.IV"]')
    # 100.02.008 Величина стоимостного баланса группы и признаваемый убыток по подгруппам (I группы) при выбытии всех
    # фиксированных активов
    GROUP_29 = (By.XPATH, '//*[@name="fnoContent.application_02._008.I"]')
    GROUP_30 = (By.XPATH, '//*[@name="fnoContent.application_02._008.II"]')
    GROUP_31 = (By.XPATH, '//*[@name="fnoContent.application_02._008.III"]')
    GROUP_32 = (By.XPATH, '//*[@name="fnoContent.application_02._008.IV"]')
    # 100.02.009
    GROUP_33 = (By.XPATH, '//*[@name="fnoContent.application_02._009.I"]')
    GROUP_34 = (By.XPATH, '//*[@name="fnoContent.application_02._009.II"]')
    GROUP_35 = (By.XPATH, '//*[@name="fnoContent.application_02._009.III"]')
    GROUP_36 = (By.XPATH, '//*[@name="fnoContent.application_02._009.IV"]')
    # 100.02.010 Последующие расходы по фиксированным активам, относимые на вычеты в соответствии с пунктом 2 статьи
    # 272 Налогового кодекса
    GROUP_37 = (By.XPATH, '//*[@name="fnoContent.application_02._010.I"]')
    GROUP_38 = (By.XPATH, '//*[@name="fnoContent.application_02._010.II"]')
    GROUP_39 = (By.XPATH, '//*[@name="fnoContent.application_02._010.III"]')
    GROUP_40 = (By.XPATH, '//*[@name="fnoContent.application_02._010.IV"]')
    # 100.02.012 Последующие расходы по арендуемым основным средствам, относимые на вычеты в соответствии с пунктом 5
    # статьи 272 Налогового кодекса
    EXPENSES = (By.XPATH, '//*[@name="fnoContent.application_02._012"]')
    # МЕСТО ДЛЯ ПРИЛОЖЕНИЯ 3

    # 4 ПРИЛОЖЕНИЕ
    B_APP_4 = (By.XPATH, '//*[@name="B"]')
    C_APP_4 = (By.XPATH, '//*[@name="C"]')
    B_SELECT_APP_4 = (By.XPATH, '//*[text()="Конвенция об избежании двойного налогообложения и предотвращении '
                                'уклонения от '
                                'уплаты налогов на доход и капитал"]')
    D_APP_4 = (By.XPATH, '//*[@name="D"]')
    D_SELECT_APP_4 = (By.XPATH, '//*[text()="Афганистан"]')
    E_APP_4 = (By.XPATH, '//*[@name="E"]')

    # 5 ПРИЛОЖЕНИЕ
    B_APP_5 = (By.XPATH, '//*[@name="B"]')
    C_APP_5 = (By.XPATH, '//*[@name="C"]')
    D_APP_5 = (By.XPATH, '//*[@name="D"]')
    B_SELECT_3 = (By.XPATH, '//*[text()="Афганистан"]')
    C_SELECT_3 = (By.XPATH, '//*[text()="доход от реализации товаров на территории Республики Казахстан, а также '
                            'доход от реализации товаров, находящихся в Республике Казахстан, за ее пределы в рамках '
                            'осуществления внешнеторговой деятельности"]')
    D_SELECT_3 = (By.XPATH, '//*[text()="Австралийский доллар"]')
    E_APP_5 = (By.XPATH, '//*[@name="E"]')
    F_APP_5 = (By.XPATH, '//*[@name="F"]')
    G_APP_5 = (By.XPATH, '//*[@name="G"]')
    H_APP_5 = (By.XPATH, '//*[@name="H"]')
    I_APP_5 = (By.XPATH, '//*[@name="I"]')
    J_APP_5 = (By.XPATH, '//*[@name="J"]')
    K_APP_5 = (By.XPATH, '//*[@name="K"]')
    L_APP_5 = (By.XPATH, '//*[@name="L"]')
    M_APP_5 = (By.XPATH, '//*[@name="M"]')
    N_APP_5 = (By.XPATH, '//*[@name="N"]')
    O_APP_5 = (By.XPATH, '//*[@name="O"]')
    P_APP_5 = (By.XPATH, '//*[@name="P"]')
    Q_APP_5 = (By.XPATH, '//*[@name="Q"]')
    # 6 ПРИЛОЖЕНИЕ
    # Признак видов деятельности
    ACTIVITY_TYPE = (By.XPATH, '//*[@role="combobox"]')
    ACTIVITY_TYPE_SELECT = (By.XPATH, '//*[text()="Признак 1 – виды деятельности, на которые распространяется СНР в '
                                      'соответствии со статьями 697, 698, 699, 700 и 701 НК с исчислением КПН по '
                                      'ставке, предусмотренной пунктом 1 статьи 313 НК"]')
    # 100.06.001 СОВОКУПНЫЙ ГОДОВОЙ ДОХОД, в том числе:
    YEAR_EXPENSE = (By.XPATH, '//*[@name="fnoContent.application_06[0]._001.I"]')
    # 100.06.002 Корректировка совокупного годового дохода в соответствии с пунктом 1 статьи 241 Налогового кодекса
    STR_1 = (By.XPATH, '//*[@name="fnoContent.application_06[0]._002"]')
    STR_2 = (By.XPATH, '//*[@name="fnoContent.application_06[0]._003"]')
    STR_3_I = (By.XPATH, '//*[@name="fnoContent.application_06[0]._005.I"]')
    STR_3_II = (By.XPATH, '//*[@name="fnoContent.application_06[0]._005.II"]')
    STR_4 = (By.XPATH, '//*[@name="fnoContent.application_06[0]._006"]')
    STR_5 = (By.XPATH, '//*[@name="fnoContent.application_06[0]._007"]')
    STR_6 = (By.XPATH, '//*[@name="fnoContent.application_06[0]._008"]')
    STR_7 = (By.XPATH, '//*[@name="fnoContent.application_06[0]._009"]')
    STR_8 = (By.XPATH, '//*[@name="fnoContent.application_06[0]._011"]')
    STR_9_I = (By.XPATH, '//*[@name="fnoContent.application_06[0]._012.I"]')
    STR_9_II = (By.XPATH, '//*[@name="fnoContent.application_06[0]._012.II"]')
    STR_10 = (By.XPATH, '//*[@name="fnoContent.application_06[0]._014"]')
    STR_11 = (By.XPATH, '//*[@name="fnoContent.application_06[0]._016"]')
    STR_12 = (By.XPATH, '//*[@name="fnoContent.application_06[0]._017"]')
    STR_13 = (By.XPATH, '//*[@name="fnoContent.application_06[0]._018"]')
    STR_14 = (By.XPATH, '//*[@name="fnoContent.application_06[0]._020"]')
    STR_15 = (By.XPATH, '//*[@name="fnoContent.application_06[0]._022"]')
    STR_16_I = (By.XPATH, '//*[@name="fnoContent.application_06[0]._024.I"]')
    STR_16_II = (By.XPATH, '//*[@name="fnoContent.application_06[0]._024.II"]')
    STR_16_III = (By.XPATH, '//*[@name="fnoContent.application_06[0]._024.III"]')
    STR_16_IV = (By.XPATH, '//*[@name="fnoContent.application_06[0]._024.IV"]')
    STR_16_V = (By.XPATH, '//*[@name="fnoContent.application_06[0]._024.V"]')
    STR_16_VI = (By.XPATH, '//*[@name="fnoContent.application_06[0]._024.VI"]')
    STR_16_VII = (By.XPATH, '//*[@name="fnoContent.application_06[0]._024.VII"]')
    STR_17_I = (By.XPATH, '//*[@name="fnoContent.application_06[0]._025.I"]')
    PERCENT = (By.XPATH, '//*[@name="fnoContent.application_06[0]._027.II.A"]')
    PERCENT_2 = (By.XPATH, '//*[@name="fnoContent.application_06[0]._027.II.B"]')
    COUNTRY = (By.XPATH, '//*[@id="rc-tabs-4-panel-0"]/div[35]/div[4]/div/div/div/div[1]/div/div/div/span[1]')
    COUNTRY_SELECT = (By.XPATH, '//*[@label="Афганистан"]')
    NAME_OF_INT_CONTRACT = (By.XPATH, '//*[@name="fnoContent.application_06[0]._027.IV"]')

    # ПРИЛОЖЕНИЕ 7
    CONTROL_TEXT = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[4]')
    CHAPTER_1 = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div[1]/div/div[2]/div[1]/div['
                           '1]/label/span/input')
    CHAPTER_2 = (By.XPATH, '//*[text()="Раздел. Обязательства"]')
    CHAPTER_3 = (By.XPATH, '//*[text()="Раздел. Капитал"]')
    # РАЗДЕЛ. АКТИВЫ
    # 100.07.001 Денежные средства и их эквиваленты
    START_1 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.active._001"]')
    END_1 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.active._001"]')
    START_2 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.active._002"]')
    END_2 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.active._002"]')
    START_3 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.active._003"]')
    END_3 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.active._003"]')
    START_4 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.active._004"]')
    END_4 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.active._004"]')
    START_5 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.active._005"]')
    END_5 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.active._005"]')
    START_6 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.active._006"]')
    END_6 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.active._006"]')
    START_7 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.active._007"]')
    END_7 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.active._007"]')
    START_8 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.active._008"]')
    END_8 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.active._008"]')
    START_9 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.active._009"]')
    END_9 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.active._009"]')
    START_10 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.active._010"]')
    END_10 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.active._010"]')
    START_11 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.active._011"]')
    END_11 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.active._011"]')
    START_12 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.active._012"]')
    END_12 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.active._012"]')
    START_13 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.active._013"]')
    END_13 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.active._013"]')
    START_14 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.active._014"]')
    END_14 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.active._014"]')
    START_15 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.active._015"]')
    END_15 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.active._015"]')
    START_16 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.active._016"]')
    END_16 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.active._016"]')
    START_17 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.active._017"]')
    END_17 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.active._017"]')
    # Раздел. Обязательства
    START_19 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.commitment._019"]')
    END_19 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.commitment._019"]')
    START_20 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.commitment._020"]')
    END_20 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.commitment._020"]')
    START_21 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.commitment._021"]')
    END_21 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.commitment._021"]')
    START_22 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.commitment._022"]')
    END_22 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.commitment._022"]')
    START_23 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.commitment._023"]')
    END_23 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.commitment._023"]')
    START_24 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.commitment._024"]')
    END_24 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.commitment._024"]')
    START_25 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.commitment._025"]')
    END_25 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.commitment._025"]')
    START_26 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.commitment._026"]')
    END_26 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.commitment._026"]')
    START_27 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.commitment._027"]')
    END_27 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.commitment._027"]')
    START_28 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.commitment._028"]')
    END_28 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.commitment._028"]')
    START_29 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.commitment._029"]')
    END_29 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.commitment._029"]')
    # Раздел. Капитал
    START_31 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.capital._031"]')
    END_31 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.capital._031"]')
    START_32 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.capital._032"]')
    END_32 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.capital._032"]')
    START_33 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.capital._033"]')
    END_33 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.capital._033"]')
    START_34 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.capital._034"]')
    END_34 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.capital._034"]')
    START_35 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.capital._035"]')
    END_35 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.capital._035"]')
    START_36 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.capital._036"]')
    END_36 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.capital._036"]')
    START_37 = (By.XPATH, '//*[@name="fnoContent.application_07.atBeginOfTaxPeriod.capital._037"]')
    END_37 = (By.XPATH, '//*[@name="fnoContent.application_07.atEndOfTaxPeriod.capital._037"]')
    # ПРИЛОЖЕНИЕ 8
    # 100.08.001 Остаток на начало года (переносится строка 100.08.004 предыдущего года)
    EIGHT_PAGE_1 = (By.XPATH, '//*[@name="fnoContent.application_08._001"]')
    EIGHT_PAGE_2 = (By.XPATH, '//*[@name="fnoContent.application_08._002.A"]')
    EIGHT_PAGE_3 = (By.XPATH, '//*[@name="fnoContent.application_08._002.B"]')
    EIGHT_PAGE_4 = (By.XPATH, '//*[@name="fnoContent.application_08._002.C"]')
    EIGHT_PAGE_5 = (By.XPATH, '//*[@name="fnoContent.application_08._002.D"]')
    EIGHT_PAGE_6 = (By.XPATH, '//*[@name="fnoContent.application_08._003.A"]')
    EIGHT_PAGE_7 = (By.XPATH, '//*[@name="fnoContent.application_08._003.B"]')
    EIGHT_PAGE_8 = (By.XPATH, '//*[@name="fnoContent.application_08._003.C"]')
    EIGHT_PAGE_9 = (By.XPATH, '//*[@name="fnoContent.application_08._003.D"]')
    EIGHT_PAGE_10 = (By.XPATH, '//*[@name="fnoContent.application_08._003.E"]')
    EIGHT_PAGE_11 = (By.XPATH, '//*[@name="fnoContent.application_08._003.F"]')
    # ПРИЛОЖЕНИЕ 9
    B_APP_9 = (By.XPATH, '//*[@name="B"]')
    C_APP_9 = (By.XPATH, '//*[@name="C"]')
    C_SELECT_APP_9 = (By.XPATH, '//*[text()="Афганистан"]')
    D_APP_9 = (By.XPATH, '//*[@name="D"]')
    E_APP_9 = (By.XPATH, '//*[@name="E"]')
    F_APP_9 = (By.XPATH, '//*[@name="F"]')
    F_SELECT_APP_9 = (By.XPATH, '//*[text()="Австралийский доллар"]')
    G_APP_9 = (By.XPATH, '//*[@name="G"]')
    H_APP_9 = (By.XPATH, '//*[@name="H"]')
    I_APP_9 = (By.XPATH, '//*[@name="I"]')
    J_APP_9 = (By.XPATH, '//*[@name="J"]')
    K_APP_9 = (By.XPATH, '//*[@name="K"]')
    L_APP_9 = (By.XPATH, '//*[@name="L"]')
    M_APP_9 = (By.XPATH, '//*[@name="M"]')
    N_APP_9 = (By.XPATH, '//*[@name="N"]')
    O_APP_9 = (By.XPATH, '//*[@name="O"]')
    P_APP_9 = (By.XPATH, '//*[@name="P"]')
    Q_APP_9 = (By.XPATH, '//*[@name="Q"]')

    # ПРИЛОЖЕНИЕ 10
    EARNING_TEN = (By.XPATH, '//*[text()="Доходы НКО"]')
    EXPENSES_TEN = (By.XPATH, '//*[text()="Расходы НКО"]')
    # Доходы
    TEN_PAGE_1 = (By.XPATH, '//*[@name="fnoContent.application_10._001"]')
    TEN_PAGE_2 = (By.XPATH, '//*[@name="fnoContent.application_10._002"]')
    TEN_PAGE_3 = (By.XPATH, '//*[@name="fnoContent.application_10._003"]')
    TEN_PAGE_4 = (By.XPATH, '//*[@name="fnoContent.application_10._004"]')
    TEN_PAGE_5 = (By.XPATH, '//*[@name="fnoContent.application_10._005"]')
    TEN_PAGE_6 = (By.XPATH, '//*[@name="fnoContent.application_10._006"]')
    TEN_PAGE_7 = (By.XPATH, '//*[@name="fnoContent.application_10._007"]')
    TEN_PAGE_8 = (By.XPATH, '//*[@name="fnoContent.application_10._008"]')
    TEN_PAGE_9 = (By.XPATH, '//*[@name="fnoContent.application_10._009"]')
    TEN_PAGE_10 = (By.XPATH, '//*[@name="fnoContent.application_10._010"]')
    TEN_PAGE_12 = (By.XPATH, '//*[@name="fnoContent.application_10._012"]')
    # Расходы
    TEN_PAGE_14_I = (By.XPATH, '//*[@name="fnoContent.application_10._014.I"]')
    TEN_PAGE_14_II = (By.XPATH, '//*[@name="fnoContent.application_10._014.II"]')
    TEN_PAGE_14_III = (By.XPATH, '//*[@name="fnoContent.application_10._014.III"]')
    TEN_PAGE_14_IV = (By.XPATH, '//*[@name="fnoContent.application_10._014.IV"]')
    TEN_PAGE_14_V = (By.XPATH, '//*[@name="fnoContent.application_10._014.V"]')
    TEN_PAGE_14_VI = (By.XPATH, '//*[@name="fnoContent.application_10._014.VI"]')
    TEN_PAGE_14_VII = (By.XPATH, '//*[@name="fnoContent.application_10._014.VII"]')
    TEN_PAGE_14_VIII = (By.XPATH, '//*[@name="fnoContent.application_10._014.VIII"]')
    TEN_PAGE_14_IX = (By.XPATH, '//*[@name="fnoContent.application_10._014.IX"]')
    TEN_PAGE_14_X = (By.XPATH, '//*[@name="fnoContent.application_10._014.X"]')
    TEN_PAGE_14_XI = (By.XPATH, '//*[@name="fnoContent.application_10._014.XI"]')
    TEN_PAGE_14_XII = (By.XPATH, '//*[@name="fnoContent.application_10._014.XII"]')
    TEN_PAGE_14_XIII = (By.XPATH, '//*[@name="fnoContent.application_10._014.XIII"]')
    TEN_PAGE_14_XIV = (By.XPATH, '//*[@name="fnoContent.application_10._014.XIV"]')
    TEN_PAGE_14_XV = (By.XPATH, '//*[@name="fnoContent.application_10._014.XV"]')
    TEN_PAGE_14_XVI = (By.XPATH, '//*[@name="fnoContent.application_10._014.XVI"]')
    TEN_PAGE_14_XVII = (By.XPATH, '//*[@name="fnoContent.application_10._014.XVII"]')
    TEN_PAGE_14_XVIII = (By.XPATH, '//*[@name="fnoContent.application_10._014.XVIII"]')
    TEN_PAGE_14_XIX = (By.XPATH, '//*[@name="fnoContent.application_10._014.XIX"]')
    TEN_PAGE_14_XIX_A = (By.XPATH, '//*[@name="fnoContent.application_10._014.XIX.A"]')
    TEN_PAGE_14_XIX_B = (By.XPATH, '//*[@name="fnoContent.application_10._014.XIX.B"]')
    TEN_PAGE_14_XIX_C = (By.XPATH, '//*[@name="fnoContent.application_10._014.XIX.C"]')
    TEN_PAGE_14_XIX_D = (By.XPATH, '//*[@name="fnoContent.application_10._014.XIX.D"]')
    TEN_PAGE_14_XIX_E = (By.XPATH, '//*[@name="fnoContent.application_10._014.XIX.E"]')
    TEN_PAGE_14_XX = (By.XPATH, '//*[@name="fnoContent.application_10._014.XX"]')
    TEN_PAGE_14_XXI = (By.XPATH, '//*[@name="fnoContent.application_10._014.XXI"]')
    TEN_PAGE_15_I = (By.XPATH, '//*[@name="fnoContent.application_10._015.I"]')
    TEN_PAGE_15_II = (By.XPATH, '//*[@name="fnoContent.application_10._015.II"]')
    TEN_PAGE_15_III = (By.XPATH, '//*[@name="fnoContent.application_10._015.III"]')
    TEN_PAGE_15_IV = (By.XPATH, '//*[@name="fnoContent.application_10._015.IV"]')
    TEN_PAGE_15_V = (By.XPATH, '//*[@name="fnoContent.application_10._015.V"]')
    TEN_PAGE_15_VI = (By.XPATH, '//*[@name="fnoContent.application_10._015.VI"]')
    TEN_PAGE_15_VII = (By.XPATH, '//*[@name="fnoContent.application_10._015.VII"]')
    TEN_PAGE_15_VIII = (By.XPATH, '//*[@name="fnoContent.application_10._015.VIII"]')
    TEN_PAGE_15_IX = (By.XPATH, '//*[@name="fnoContent.application_10._015.IX"]')
    TEN_PAGE_15_X = (By.XPATH, '//*[@name="fnoContent.application_10._015.X"]')
    TEN_PAGE_15_XI = (By.XPATH, '//*[@name="fnoContent.application_10._015.XI"]')
    TEN_PAGE_16 = (By.XPATH, '//*[@name="fnoContent.application_10._016"]')
    TEN_PAGE_17 = (By.XPATH, '//*[@name="fnoContent.application_10._017"]')
    TEN_PAGE_18 = (By.XPATH, '//*[@name="fnoContent.application_10._018"]')
    TEN_PAGE_19 = (By.XPATH, '//*[@name="fnoContent.application_10._019"]')
    TEN_PAGE_20 = (By.XPATH, '//*[@name="fnoContent.application_10._020"]')
    TEN_PAGE_21 = (By.XPATH, '//*[@name="fnoContent.application_10._021"]')
    TEN_PAGE_22 = (By.XPATH, '//*[@name="fnoContent.application_10._022"]')
    # ПРИЛОЖЕНИЕ 11
    B_APP_11 = (By.XPATH, '//*[@name="B"]')
    C_APP_11 = (By.XPATH, '//*[@name="C"]')
    C_SELECT_APP_11 = (By.XPATH, '//*[text()="Афганистан"]')
    D_APP_11 = (By.XPATH, '//*[@name="D"]')
    E_APP_11 = (By.XPATH, '//*[@name="E"]')
    F_APP_11 = (By.XPATH, '//*[@name="F"]')
    G_A_APP_11 = (By.XPATH, '//*[@name="G.A"]')
    G_B_APP_11 = (By.XPATH, '//*[@name="G.B"]')
    E_SELECT_APP_11 = (By.XPATH, '//*[text()="благотворительная помощь"]')
    F_SELECT_APP_11 = (By.XPATH, '//*[text()="деньги"]')
    H_APP_11 = (By.XPATH, '//*[@name="H"]')
    I_APP_11 = (By.XPATH, '//*[@name="I"]')
    G_DATE_SELECT_APP_11 = (By.XPATH, '//*[text()="Сегодня"]')
    # ПРИЛОЖЕНИЕ 12
    TWELVE_CHAPTER_1 = (By.XPATH, '//*[text()="Раздел. Доходы от оказания финансовых услуг, предусмотренных пунктом 3 '
                                  'статьи 6 Конституционного закона"]')
    TWELVE_CHAPTER_2 = (By.XPATH, '//*[text()="Раздел. Доходы от оказания сопутствующих услуг, предусмотренных '
                                  'пунктом 4 статьи 6 Конституционного закона"]')
    TWELVE_CHAPTER_3 = (By.XPATH, '//*[text()="Раздел. Доходы, освобождаемые от налогообложения согласно пункту 7 '
                                  'статьи 6 Конституционного закона"]')
    TWELVE_CHAPTER_4 = (
        By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/div/div/div[4]/form/div[1]/div[2]/div[4]/div[1]/label/span/input')
    # РАЗДЕЛ 1
    TWELVE_PAGE_1 = (By.XPATH, '//*[@name="fnoContent.application_12._001"]')
    TWELVE_PAGE_2 = (By.XPATH, '//*[@name="fnoContent.application_12._002"]')
    TWELVE_PAGE_3 = (By.XPATH, '//*[@name="fnoContent.application_12._003"]')
    TWELVE_PAGE_4 = (By.XPATH, '//*[@name="fnoContent.application_12._004"]')
    TWELVE_PAGE_5 = (By.XPATH, '//*[@name="fnoContent.application_12._005"]')
    # РАЗДЕЛ 2
    TWELVE_PAGE_7 = (By.XPATH, '//*[@name="fnoContent.application_12._007"]')
    TWELVE_PAGE_8 = (By.XPATH, '//*[@name="fnoContent.application_12._008"]')
    TWELVE_PAGE_9 = (By.XPATH, '//*[@name="fnoContent.application_12._009"]')
    TWELVE_PAGE_10 = (By.XPATH, '//*[@name="fnoContent.application_12._010"]')
    # РАЗДЕЛ 3
    TWELVE_PAGE_12 = (By.XPATH, '//*[@name="fnoContent.application_12._012"]')

    # ДОПОЛНИТЕЛЬНО
    GO_TO_APP_1 = (By.XPATH, '//*[text()="7"]')
    GO_TO_APP_6 = (By.XPATH, '//*[text()="12"]')
    GO_TO_APP_8 = (By.XPATH, '//*[text()="14"]')
    GO_TO_APP_7 = (By.XPATH, '//*[text()="13"]')
    GO_TO_APP_9 = (By.XPATH, '//*[text()="15"]')
    GO_TO_APP_10 = (By.XPATH, '//*[text()="16"]')
    GO_TO_APP_11 = (By.XPATH, '//*[text()="17"]')
    GO_TO_APP_12 = (By.XPATH, '//*[text()="18"]')
    CANCEL_ADD_STR = (By.XPATH, '//*[text()="Отменить"]')
