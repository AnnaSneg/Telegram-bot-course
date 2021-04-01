"""
To determine the course for today and the rates for the period, different symbols of the same currency are used. So for the
rates for the day (https://www.cbr.ru/currency_base/daily/), it is enough to know the numeric or alphabetic currency
code (for example: Australian dollar, numeric code-036, alphabetic code-AUD), and to view the rate in dynamics
(https://www.cbr.ru/currency_base/dynamics/?UniDbQuery.Posted
=True&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=R01010&UniDbQuery.From=01.09.
2020&UniDbQuery.To=21.11.2020), a special code is required (for example: Australian dollar - R01010).
The list below combines all the symbols for a single currency.
"""

all_currency = [
    ('Австралийский доллар', 'Australian Dollar', '1', 'R01010', '036', 'AUD'),
    ('Австрийский шиллинг', 'Austrian Shilling', '1000', 'R01015'),
    ('Азербайджанский манат', 'Azerbaijan Manat', '1', 'R01020', '944', 'AZN'),
    ('Фунт стерлингов Соединенного королевства', 'British Pound Sterling', '1', 'R01035', '826'),
    ('Ангольская новая кванза', 'Angolan new Kwanza', '100000', 'R01040'),
    ('Армянский драм', 'Armenia Dram', '1000', 'R01060', '051', 'AMD'),
    ('Белорусский рубль', 'Belarussian Ruble', '1', 'R01090', '933', 'BYN'),
    ('Бельгийский франк', 'Belgium Franc', '1000', 'R01095'),
    ('Болгарский лев', 'Bulgarian lev', '1', 'R01100', '975', 'BGN'),
    ('Бразильский реал', 'Brazil Real', '1', 'R01115', '986', 'BRL'),
    ('Венгерский форинт', 'Hungarian Forint', '100', 'R01135', '348', 'HUF'),
    ('Гонконгский доллар', 'Hong Kong Dollar', '10', 'R01200', '344', 'HKD'),
    ('Греческая драхма', 'Greek Drachma', '10000', 'R01205'),
    ('Датская крона', 'Danish Krone', '10', 'R01215', '208', 'DKK'),
    ('Доллар США', 'US Dollar', '1', 'R01235', '840', 'USD'),
    ('Евро', 'Euro', '1', 'R01239', '978', 'EUR'),
    ('Индийская рупия', 'Indian Rupee', '100', 'R01270', '356', 'INR'),
    ('Ирландский фунт', 'Irish Pound', '100', 'R01305'),
    ('Исландская крона', 'Iceland Krona', '10000', 'R01310'),
    ('Испанская песета', 'Spanish Peseta', '10000', 'R01315'),
    ('Итальянская лира', 'Italian Lira', '100000', 'R01325'),
    ('Казахстанский тенге', 'Kazakhstan Tenge', '100', 'R01335', '398', 'KZT'),
    ('Канадский доллар', 'Canadian Dollar', '1', 'R01350', '124', 'CAD'),
    ('Киргизский сом', 'Kyrgyzstan Som', '100', 'R01370', '417', 'KGS'),
    ('Китайский юань', 'China Yuan', '10', 'R01375', '156', 'CNY'),
    ('Кувейтский динар', 'Kuwaiti Dinar', '10', 'R01390'),
    ('Латвийский лат', 'Latvian Lat', '1', 'R01405'),
    ('Ливанский фунт', 'Lebanese Pound', '100000', 'R01420'),
    ('Литовский лит', 'Lithuanian Lita', '1', 'R01435'),
    ('Литовский талон', 'Lithuanian talon', '1', 'R01435'),
    ('Молдавский лей', 'Moldova Lei', '10', 'R01500', '498', 'MDL'),
    ('Немецкая марка', 'Deutsche Mark', '1', 'R01510'),
    ('Немецкая марка', 'Deutsche Mark', '100', 'R01510'),
    ('Нидерландский гульден', 'Netherlands Gulden', '100', 'R01523'),
    ('Норвежская крона', 'Norwegian Krone', '10', 'R01535', '578', 'NOK'),
    ('Польский злотый', 'Polish Zloty', '1', 'R01565', '985', 'PLN'),
    ('Португальский эскудо', 'Portuguese Escudo', '10000', 'R01570'),
    ('Румынский лей', 'Romanian Leu', '10000', 'R01585', '946', 'RON'),
    ('Румынский лей', 'Romanian Leu', '10', 'R01585', '946', 'RON'),
    ('СДР (специальные права заимствования)', 'SDR', '1', 'R01589', '960', 'XDR'),
    ('Сингапурский доллар', 'Singapore Dollar', '1', 'R01625', '702', 'SGD'),
    ('Суринамский доллар', 'Surinam Dollar', '1', 'R01665'),
    ('Таджикский сомони', 'Tajikistan Ruble', '10', 'R01670', '972', 'TJS'),
    ('Таджикский рубл', 'Tajikistan Ruble', '10', 'R01670'),
    ('Турецкая лира', 'Turkish Lira', '1', 'R01700', '949', 'TRY'),
    ('Туркменский манат', 'Turkmenistan Manat', '10000', 'R01710'),
    ('Новый туркменский манат', 'New Turkmenistan Manat', '1', 'R01710', '934', 'TMT'),
    ('Узбекский сум', 'Uzbekistan Sum', '1000', 'R01717', '860', 'UZS'),
    ('Украинская гривна', 'Ukrainian Hryvnia', '10', 'R01720', '980', 'UAH'),
    ('Украинский карбованец', 'Ukrainian Hryvnia', '1', 'R01720'),
    ('Финляндская марка', 'Finnish Marka', '100', 'R01740'),
    ('Французский франк', 'French Franc', '1000', 'R01750'),
    ('Чешская крона', 'Czech Koruna', '10', 'R01760', '203', 'CZK'),
    ('Шведская крона', 'Swedish Krona', '10', 'R01770', '752', 'SEK'),
    ('Швейцарский франк', 'Swiss Franc', '1', 'R01775', '756', 'CHF'),
    ('ЭКЮ', 'ECU', '1', 'R01790'),
    ('Эстонская крона', 'Estonian Kroon', '10', 'R01795'),
    ('Югославский новый динар', 'Yugoslavian Dinar', '1', 'R01804'),
    ('Южноафриканский рэнд', 'S.African Rand', '10', 'R01810', '710', 'ZAR'),
    ('Вон Республики Корея', 'South Korean Won', '1000', 'R01815', '410', 'KRW'),
    ('Японская иена', 'Japanese Yen', '100', 'R01820', '392', 'JPY')]


def get_r0(ccy):
    for i in all_currency:
        if ccy in i:
            return i[3] #return the RO value for urlmonth in the month module

