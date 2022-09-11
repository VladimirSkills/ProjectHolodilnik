from selenium.webdriver.common.by import By

"""
СОКРАЩЕНИЯ:
b -> button (кнопка)
f -> find (найти)
v -> value (значение)
Например:
bENTER -> кнопка Войти
fENTER -> найти элемент с названием Войти
vEMAIL -> вводим значение в элемент email
"""


class LocatorsProject:
    """Локаторы проекта."""

    # Кнопка Войти + Найти элемент
    REG_bfENTER = (By.XPATH, '//span[contains(text(), "Войти")]')
    # Кнопка Другой способ
    REG_bWAY = (By.XPATH, '//a[contains(text(), "Другой способ")]')
    # Кнопка По смс или email коду
    REG_bEMAIL = (By.XPATH, '//button[contains(text(), "По смс или email коду")]')
    # Кнопка По паролю
    AUTH_bBYPASS = (By.XPATH, '//button[contains(text(), "По паролю")]')
    # Вводим адрес почты в поле email
    REG_vEMAIL = (By.XPATH, '//input[@id="phoneORemail_id"]')
    # Кнопка Получить код
    REG_bGET_CODE = (By.XPATH, '//button[contains(text(), "Получить код")]')
    # Вводим code регистрации в поле для ввода
    REG_vCODE = (By.XPATH, '//input[@inputmode="numeric"]')
    # Локатор на надпись: Введите код
    REG_fINPUTCODE = (By.XPATH, '//div[contains(text(), "Введите код")]')
    # Локатор на надпись при неверном пароле
    AUTH_fERRORPASS = (By.CSS_SELECTOR, '#error_id')
    # Кнопка Личный кабинет
    REG_bUSER = (By.XPATH, '//span[contains(text(), "Личный кабинет")]')
    # Пункт меню Смена пароля
    REG_bCHANGE_PASS = (By.XPATH, '//span[contains(text(), "Смена пароля")]')
    # Вводим password в поле Пароль / Новый пароль и в Проверочное поле
    AUTH_vPASS = (By.XPATH, '//input[@id="password_id"]')  # при авторизации
    REG_vPASS = (By.CSS_SELECTOR, '#password')  # при регистрации
    REG_vPASS2 = (By.CSS_SELECTOR, '#password2')  # при регистрации
    # Кнопка Сохранить изменения
    REG_bSAVE = (By.XPATH, '//input[@value="Сохранить изменения"]')
    # Нажимаем на label Выход
    REG_bEXIT = (By.XPATH, '//a[@class="button button_type_link button_with_icon"]')
    # Кнопка Войти при авторизации
    AUTH_bLOGIN = (By.XPATH, '//button[contains(text(), "Войти")]')
    # Кнопка КАТАЛОГ
    # //button[@id="headerMenuToggle"]
    GOOD_bCATALOG = (By.XPATH, '//span[contains(text(), "Каталог")]')
    # КАТАЛОГ. Раздел Холодильники
    GOOD_fFRIDGES = (By.XPATH, '//a[@data-ga-event-action="refrigerator"]/span')
    # Раздел Холодильники. Подраздел Морозильники (морозильные камеры)
    GOOD_fFREEZERS = (By.XPATH, '//a[contains(text(), "Морозильники (морозильные камеры)")]')
    # Локатор счётчика товаров
    GOOD_fCOUNTER = (By.XPATH, '//input[@id="cfilter_btnsubmit"]')
    # Локатор Наименования раздела
    GOOD_fGOODSNAME = (By.XPATH, '//div[@class="container"]//h1')
    # Локатор Цена товара
    GOOD_fGOODSPRICE = (By.XPATH, '//div[@class="price"]')
    # Локатор Номера страниц Пагинации
    GOOD_fPAGELINK = (By.XPATH, '//a[@class="page-link"]')
    # Локатор на ряды элементов главной страницы
    MPAGE_fROW = (By.CSS_SELECTOR, '.row')
    # Локатор на раздел Каталога - Телевизоры
    MPAGE_fTV = (By.XPATH, '//a[@data-ga-event-action="tv_all"]')
    # Кнопка Каталога с надписью Закрыть
    MPAGE_bCLOSE = (By.XPATH, '//span[contains(text(), "Закрыть")]')
    # КАТАЛОГ. Раздел Смартфоны и гаджеты
    GOOD_fSMARTPHONES = (By.XPATH, '//a[@data-ga-event-action="smartphones_gadgets"]/span')
    # Раздел Смартфоны и гаджеты. Подраздел Samsung
    GOOD_fSAMSUNG = (By.XPATH, '//a[contains(text(), "Samsung")]')
    # Раздел Смартфоны и гаджеты. Подраздел Смартфоны
    GOOD_fSMARTPHONPROD = (By.XPATH, '//a[contains(text(), "Смартфоны")]')
    # Телевизоры. Подраздел Цифровые телевизионные ресиверы
    MPAGE_fRECEIVERS = (By.XPATH, '//a[contains(text(), "Цифровые телевизионные ресиверы")]')
    # КАТАЛОГ. Раздел Аудио-видео
    MPAGE_fAUDIO = (By.XPATH, '//a[@data-ga-event-action="audio_video"]/span')
    # Аудио-видео. Подраздел Аудиотехника
    MPAGE_fATECHNIQUE = (By.XPATH, '//a[contains(text(), "Аудиотехника")]')
    # КАТАЛОГ. Раздел Компьютерная техника
    MPAGE_bfCOMPTECH = (By.XPATH, '//a[@data-ga-event-action="digital_tech"]/span')
    # Компьютерная техника. Подраздел ЖК мониторы
    MPAGE_fLCDMONITOR = (By.XPATH, '//a[contains(text(), "ЖК мониторы")]')
    # Компьютерная техника. Подраздел Компьютеры
    MPAGE_fCOMPUTER = (By.XPATH, '//a[contains(text(), "Компьютеры")]')  # //a[@data-ga-event-action="computers"]
    # КАТАЛОГ. Стиральные машины
    MPAGE_bfWASHERS = (By.XPATH, '//a[@data-ga-event-action="washers"]/span')
    # Стиральные машины. Подраздел Сушильные автоматы
    MPAGE_fDRYAUTO = (By.XPATH, '//a[contains(text(), "Сушильные автоматы")]')
    # Стиральные машины. Подраздел - Все
    MPAGE_bfALLWASHERS = (By.CSS_SELECTOR, '.menu-categories__order')
    # MPAGE_bfEACHWASHERS = (By.TAG_NAME, 'a')  # не получается не делать локатор в самом тесте
    # КАТАЛОГ. Встраиваемая техника
    MPAGE_bfBUILTIN = (By.XPATH, '//a[@data-ga-event-action="built-in"]/span')
    # Встраиваемая техника. Встраиваемые винные шкафы
    MPAGE_fWINECASE = (By.XPATH, '//a[contains(text(), "Встраиваемые винные шкафы")]')
    # КАТАЛОГ. Посудомоечные машины
    MPAGE_bfDISWASHERS = (By.XPATH, '//a[@data-ga-event-action="dishwashers_all"]/span')
    # Посудомоечные машины. Компактные посудомоечные машины
    MPAGE_fCOMPWASHERS = (By.XPATH, '//a[contains(text(), "Компактные посудомоечные машины")]')
    # КАТАЛОГ. Плиты
    MPAGE_bfSTOVES = (By.XPATH, '//a[@data-ga-event-action="gas-stoves"]/span')
    # Плиты. Газовые плиты
    MPAGE_fGASCOOKERS = (By.XPATH, '//a[contains(text(), "Газовые плиты")]')
    # КАТАЛОГ. Техника для кухни
    MPAGE_bfFORKITCHEN = (By.XPATH, '//a[@data-ga-event-action="small_domestic"]/span')
    # Техника для кухни. Кофейное оборудование
    MPAGE_fCOFFEESET = (By.XPATH, '//a[contains(text(), "Кофейное оборудование")]')
    # КАТАЛОГ. Техника для дома
    MPAGE_bfDOMESTIC = (By.XPATH, '//a[@data-ga-event-action="domestic"]/span')
    # Техника для дома. Умный дом
    MPAGE_fSMARTHOUSE = (By.XPATH, '//a[@data-category-id="prop_smart_house"]')  # //a[contains(text(), "Умный дом")]/0
    # КАТАЛОГ. Красота и здоровье
    MPAGE_bfBEAUTY = (By.XPATH, '//a[@data-ga-event-action="beauty"]/span')
    # Красота и здоровье. Фены
    MPAGE_fHAIRDRIERS = (By.XPATH, '//a[@data-ga-event-action="hair_driers"]')  # //a[contains(text(), "Фены")]/0
    # КАТАЛОГ. Климатическая техника
    MPAGE_bfCLIMATIC = (By.XPATH, '//a[@data-ga-event-action="climatic"]/span')
    # Климатическая техника. Камины
    MPAGE_fFIREPLACES = (By.XPATH, '//a[contains(text(), "Камины")]')
    # КАТАЛОГ. Строительство и ремонт
    MPAGE_bfCONSTRUCTION = (By.XPATH, '//a[@data-ga-event-action="construction_repair"]/span')
    # Строительство и ремонт. Перфораторы
    MPAGE_fPERFORATORS = (By.XPATH, '//a[contains(text(), "Перфораторы")]')
    # КАТАЛОГ. Товары для дома и сада
    MPAGE_bfCOTTAGEGARD = (By.XPATH, '//a[@data-ga-event-action="cottage_repair"]/span')
    # Товары для дома и сада. Мебель для дома
    MPAGE_fFURNITURE = (By.XPATH, '//a[contains(text(), "Мебель для дома")]')
    # КАТАЛОГ. Спорт и отдых
    MPAGE_bfSPORTGOODS = (By.XPATH, '//a[@data-ga-event-action="sport_recreation"]/span')
    # Спорт и отдых. Силовые тренажеры
    MPAGE_fSTRONGFITNESS = (By.XPATH, '//a[contains(text(), "Силовые тренажеры")]')
    # КАТАЛОГ. Детские товары
    MPAGE_bfKIDS = (By.XPATH, '//a[@data-ga-event-action="kids"]/span')
    # Детские товары. Конструкторы
    MPAGE_fCONSTRUCTORS = (By.XPATH, '//a[contains(text(), "Конструкторы")]')
    # КАТАЛОГ. Уцененные товары
    MPAGE_bfDISCOUNTED = (By.XPATH, '//a[@href="//www.holodilnik.ru/repair/"]')  # li[data-target="tabRepair"]
    # Уцененные товары. 1-ая категория в списке
    MPAGE_fDISCOUNTFIRST = (By.XPATH, '//div[@class="menu-categories__list-title"]')  # [0]
    # Указатель Назад (если она присутствует, то на странице по-прежнему выводится список категорий
    # и нужно продолжать выбирать товар. Если указателя нет, категория открыта и активен список товаров.
    MPAGE_bfDISCOUNTBACK = (By.CSS_SELECTOR, 'div[data-menu-breadcrumb-link="back"]')
    MPAGE_bfDISCOUNTSECOND = (By.CSS_SELECTOR,
                              '.menu-categories__order.menu-categories__order--repair'
                              '.menu-categories__order--repair-limit.menu-categories__order--current>div>a')  # [0]
    # Уцененные товары. Локатор на область и локатор на все категории товаров в области
    MPAGE_fALLDISCOUNTGOODS = (By.CSS_SELECTOR, '.menu-categories__order.menu-categories__order--current'
                                                '>.menu-categories__list')
    # Уценённые товары. Карточка товара. Локатор на карточки
    MPAGE_fDISCOUNTPRODUCTS = (By.XPATH, '//div[@class="preview-product discounted"]')
    # Уценённые товары. Карточка товара. Наименование товара
    MPAGE_fPRODUCTNAME = (By.CSS_SELECTOR, '.product-name')
    # Уценённые товары. Карточка товара. Изображение товара
    MPAGE_fPRODUCTIMAGE = (By.XPATH, '//div[@class="preview-product discounted"]//img[@class="img-fluid"]')
    # Уценённые товары. Карточка товара. Цена товара
    MPAGE_fPRODUCTPRICE = (By.XPATH, '//div[@class="price"]')
    # Уценённые товары. Карточка товара. Скидка
    MPAGE_fOLDPRICE = (By.XPATH, '//div[@class="old-price"]')
    # Уценённые товары. Карточка товара. Причина уценки
    MPAGE_fREASONMARKDOWN = (By.XPATH, '//div[@class="preview-product discounted"]//li')
    # КАТАЛОГ. АКЦИИ
    MPAGE_bfACTION = (By.XPATH, '//a[@data-ga-event-action="action"]/span')
    # АКЦИИ. Список акций
    MPAGE_bfBRANDACTION = (By.XPATH, '//a[@class="brand-action"]')
    # КАТАЛОГ. БРЕНД-ЗОНЫ
    MPAGE_bfBRANDS = (By.XPATH, '//a[@data-ga-event-action="brands"]/span')
    # Страница сайта. Элемент скролл вверх
    MPAGE_bfSCROLLUP = (By.XPATH, '//div[@class="scroll-up show"]')
    MPAGE_bfNOSCROLLUP = (By.XPATH, '//div[@class="scroll-up"]')
    # ВЕРХНЕЕ МЕНЮ. Header
    MPAGE_fHEADER = (By.CSS_SELECTOR, '#menuCategories>.menu-categories__item>a')
    # ЛОГОТИП сайта
    MPAGE_bLOGOIMAGE = (By.CSS_SELECTOR, '.navbar-logo__image')
    # Главная страница. Body
    MPAGE_bfBODY = (By.XPATH, '//div[@class="swiper-slide"]//a')
    # Body. Товар дня
    MPAGE_bfGOODDAY = (By.XPATH, '//div[@class="promotion__row"]//a')
    # Body. Товар дня. Наименование товара
    MPAGE_fGOODDAYNAME = (By.XPATH, '//h1[contains(text(), *)]')
    # ВЕРХНЕЕ МЕНЮ. Footer
    MPAGE_fFOOTER = (By.XPATH, '//div[@id="accordionFooter"]//a')
    # ВЕРХНЕЕ МЕНЮ. Избранное
    MPAGE_bFAVORITES = (By.XPATH, '//span[contains(text(), "В избранное")]')
    # ВЕРХНЕЕ МЕНЮ. Счётчик Избранное
    MPAGE_bFAVORITESCOUNT = (By.CSS_SELECTOR, '#favorite_products_count')
    # Локатор на значки социальных сетей
    MPAGE_bNETWORK = (By.XPATH, '//div[@class="item-social__list"]//a')
    # Локатор на выбор города
    MPAGE_bTOWN = (By.CSS_SELECTOR, '.region-header.js-ga-event-click')
    # Локатор на город Казань
    MPAGE_bTOWNKAZAN = (By.XPATH, '//li[@data-modal-region="27"]//a[contains(text(), "Казань")]')

    # ПОЛЕ ПОИСК. Поле
    SEARCH_vFIELD = (By.CSS_SELECTOR, '#top_search')
    # ПОЛЕ ПОИСК. Кнопка
    SEARCH_bSEARCH = (By.XPATH, '//button[@type="submit"]')
    # ПОЛЕ ПОИСК. Локатор на наименование элементов Цифровые телевизионные ресиверы
    SEARCH_fBYNAME = (By.XPATH, '//div[@class="col-12"]//div[@class="product-name"]')
    # ПОЛЕ ПОИСК. Локатор на количество найденных товаров
    SEARCH_fAMOUNTFOUND = (By.CSS_SELECTOR, '.found_rows>b')
    # ПОЛЕ ПОИСК. Локатор на комментарии при негативном тестировании
    SEARCH_fCOMENTFOUND = (By.CSS_SELECTOR, '.found_rows')
    # ПОЛЕ ПОИСК. Локатор на код товара элементов Цифровые телевизионные ресиверы
    SEARCH_fBYCODE = (By.XPATH, '//div[@class="product-code"]//span')

    # ФИЛЬТР. Локатор на кнопку Закрыть рекламу про скидку
    FTRS_bADVERTIS = (By.CSS_SELECTOR, '.popmechanic-close')
    # ФИЛЬТР. Локатор на поле с минимальной ценой
    FTRS_vMINPRICE = (By.CSS_SELECTOR, '#min_txt_price')
    # ФИЛЬТР. Локатор на поле с максимальной ценой
    FTRS_vMAXPRICE = (By.CSS_SELECTOR, '#max_txt_price')
    # ФИЛЬТР. Локатор на все цены
    FTRS_fPRICEALL = (By.XPATH, '//div[@class="price"]')
    # ФИЛЬТР. Локатор Цена товара с учётом скидки (два числа) *
    FTRS_fPRICEMARKD = (By.XPATH, '//div[@class="price" and child::*]')
    # ФИЛЬТР. Локатор на старые цены (только числа) **
    FTRS_fMARKDOWN = (By.XPATH, '//div[@class="price"]//*[contains(text(), *)]')
    # ФИЛЬТР. Локатор Цена товара без учёта скидки (+ символ ₽) ***
    FTRS_fPRICE = (By.XPATH, '//div[@class="price" and contains(text(), *)]')
    # ФИЛЬТР. Кнопка Показать
    FTRS_bSHOW = (By.XPATH, '//a[contains(text(), "Показать")]')
    # ФИЛЬТР. Кнопка Очистить
    FTRS_bCLEAR = (By.CSS_SELECTOR, '#cfilter_btnclear')
    # ФИЛЬТР. Поиск по Производителю: ACER
    FTRS_bPROD_ACER = (By.CSS_SELECTOR, '#cfilter_1324_vendor_1_label')
    # ФИЛЬТР. Поиск по Производителю: Lenovo
    FTRS_bPROD_LENOVO = (By.CSS_SELECTOR, '#cfilter_1324_vendor_5_label')
    # ФИЛЬТР. Кнопка Операционная система
    FTRS_bOPERSYSTEM = (By.XPATH, '//span[@class="hdr-title" and contains(text(), "Операционная система")]')
    # ФИЛЬТР. Поиск по Операционная система: DOS
    FTRS_bOS_DOS = (By.CSS_SELECTOR, '#cfilter_1324_27376_3_label')
    # ФИЛЬТР. Поиск по Операционная система: Windows 10 Professional
    FTRS_bOS_WINDOWS = (By.CSS_SELECTOR, '#cfilter_1324_27376_7_label')
    # ФИЛЬТР. Поиск Операционной системы в карточке товара
    FTRS_fFIND_OS = (By.XPATH,
                     '//table[@class="table table-borderless"]//span[contains(text(), "Операционная система")]')
    # СОРТИРОВКА. Кнопка
    FTRS_bSORTING = (By.CSS_SELECTOR, '#dropdownItemSorting')
    # СОРТИРОВКА. Сначала дешёвые
    FTRS_bSORTCHEAP = (By.XPATH, '//a[contains(text(), "Сначала дешевые")]')
    # СОРТИРОВКА. Сначала дорогие
    FTRS_bSORTEXPENS = (By.XPATH, '//a[contains(text(), "Сначала дорогие")]')
    # СОРТИРОВКА. По наличию на складе
    FTRS_bSORTSTOCK = (By.XPATH, '//a[contains(text(), "По наличию на складе")]')
    # СОРТИРОВКА. По размеру скидки
    FTRS_bSORTMARKDOWN = (By.XPATH, '//a[contains(text(), "По размеру скидки")]')
    # СОРТИРОВКА. Популярные
    FTRS_bSORTPOPULAR = (By.XPATH, '//a[contains(text(), "Популярные")]')
    # ФИЛЬТР. Опция "Нет в наличии"
    FTRS_bNOTAVAILABLE = (By.CSS_SELECTOR, '#cfilter_1324_st_1_hidden_label')
    # ФИЛЬТР. Поле в карточке: "Статус наличия товара"
    FTRS_fSTATUSAVAILABLE = (By.XPATH, '//div[@class="item-status"]/div[contains(text(), *)]')

    # КАРТОЧКА ТОВАРА. Локатор на изображения
    PCB_fLOCATEIMAGES = (By.XPATH, '//div[@class="col product-image"]//img[@class="img-fluid"]')
    # КАРТОЧКА ТОВАРА. Локатор на описание товара
    PCB_fDESCRIPTION = (By.XPATH, '//table[@class="table table-borderless"]')
    # КАРТОЧКА ТОВАРА. Локатор на кнопку В корзину
    PCB_fBASKET = (By.XPATH, '//a[@class="btn btn-order  " and contains(text(), "В корзину")]')
    # КОРЗИНА. Локатор на счётчик
    PCB_fBASKETNUM = (By.CSS_SELECTOR, '#numInCart')
    # КОРЗИНА. Кнопка Перейти в корзину
    PCB_bINBASKET = (By.XPATH, '//a[contains(text(), "Перейти в корзину")]')
    # КОРЗИНА. Кнопка Перейти в корзину из всплывающего окна
    PCB_bINBASKET2 = (By.CSS_SELECTOR, '#modal-product-add-cart-button')
    # КОРЗИНА. Наименование товара в корзине
    PCB_fBASKETNAMEGOODS = (By.XPATH, '//div[@class="basket__items-element-name-text"]/a')
    # КОРЗИНА. Локатор на значок Корзина
    PCB_bBASKET = (By.XPATH, '//span[contains(text(), "Корзина")]')
    # КОРЗИНА. Локатор на кнопку Удалить
    PCB_bDELFROMBASKET = (By.XPATH, '//span[@data-original-title="Удалить"]')
    # КОРЗИНА. Локатор на кнопку Подтвердить удаление
    PCB_bDELFROMBASKETYES = (By.XPATH, '//button[contains(text(), "Удалить")]')
    # КОРЗИНА. Локатор на надпись "Корзина пуста"
    PCB_fBASKETEMPTY = (By.XPATH, '//div[contains(text(), "Корзина пуста")]')
    # КОРЗИНА. Локатор на кнопку "Продолжить покупки"
    PCB_bGOSHOPPING = (By.XPATH, '//div[contains(text(), "Продолжить покупки")]')
    # КОРЗИНА. Локатор на кнопку "Очистить корзину"
    PCB_bCLEARBASKET = (By.XPATH, '//span[contains(text(), "Очистить корзину")]')
    # КОРЗИНА. Локатор на надпись "Страхование техники"
    PCB_bINSURANCE = (By.XPATH, '//span[contains(text(), "Страхование техники")]')
    # КОРЗИНА. Страхование техники. Надпись "Год без хлопот" [1]
    PCB_bNOHASSLE = (By.CSS_SELECTOR, '.field-radio__label-info')
    # КОРЗИНА. Страхование техники. Кнопка Добавить к заказу
    PCB_bADDORDER = (By.XPATH, '//button[contains(text(), "Добавить к заказу")]')
    # КОРЗИНА. Страхование техники. Локатор на доп. опцию "Год без хлопот"
    PCB_fNOHASSLEOK = (By.CSS_SELECTOR, '.basket__items-element-addons-selected-item-info-text')
    # КОРЗИНА. Локатор на Итоговую цену в Корзине
    PCB_fTOTALPRICE = (By.CSS_SELECTOR, '.basket__summary-row-value>span')

    # КОРЗИНА. Кнопка Оформить заказ
    PCB_bBASKETCHECKOUT = (By.XPATH, '//button[contains(text(), "Оформить заказ")]')
    # КОРЗИНА. Оформление заказа. Поле/Ввод Телефон
    PCB_fBASKETPHONE = (By.XPATH, '//label[contains(text(), "Телефон")]')  # 9371586985 (937+random)
    PCB_vBASKETPHONEIN = (By.CSS_SELECTOR, '#OrderPhone')
    # КОРЗИНА. Оформление заказа. Поле/Ввод Email
    PCB_fBASKETEMAIL = (By.XPATH, '//label[contains(text(), "Email")]')
    PCB_vBASKETEMAILIN = (By.CSS_SELECTOR, '#OrderEmail')
    # КОРЗИНА. Оформление заказа. Поля/Ввод ФИО
    PCB_fBASKETSURNAME = (By.XPATH, '//label[contains(text(), "Фамилия")]')
    PCB_vBASKETSURNAMEIN = (By.CSS_SELECTOR, '#OrderFIO_L')
    PCB_fBASKETNAME = (By.XPATH, '//label[contains(text(), "Имя")]')
    PCB_vBASKETNAMEIN = (By.CSS_SELECTOR, '#OrderFIO_F')
    PCB_fBASKETLASTNAME = (By.XPATH, '//label[contains(text(), "Отчество")]')
    PCB_vBASKETLASTNAMEIN = (By.CSS_SELECTOR, '#OrderFIO_T')
    # КОРЗИНА. Оформление заказа. Кнопка "Выбрать пункт самовывоза"
    PCB_bBASKETPICKUP = (By.XPATH, '//div[contains(text(), "Выбрать пункт самовывоза")]')
    # КОРЗИНА. Оформление заказа. Первый пункт
    PCB_bBASKETPICKUP1 = (By.XPATH, '//div[@onclick="appYaMaps.handleMapPickupItemSelect(0)"]')
    # КОРЗИНА. Оформление заказа. Кнопка "Заберу здесь"
    PCB_bBASKETPICKUPHERE = (By.XPATH, '//a[contains(text(), "Заберу здесь")]')  # [0]
    # КОРЗИНА. Оформление заказа. Способ оплаты
    PCB_bBASKETPAYMENT = (By.XPATH, '//span[contains(text(), "Картой / наличными")]')
    # КОРЗИНА. Оформление заказа. Кнопка Оформить
    PCB_bBASKETPAY = (By.XPATH, '//button[contains(text(), "Оформить")]')
    # КОРЗИНА. Оформление заказа. Подтверждение
    PCB_fBASKETORDEROK = (By.XPATH, '//div[@class="checkout__confirm-status"]')
    # КОРЗИНА. Локатор на кол-во товаров
    PCB_fNUMBERSGOODS = (By.XPATH, '//span[@class="widget-quantity__control"]/input[@type="text"]')
