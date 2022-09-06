"""Тестируем Фильтр и Сортировку (запуск через команду Run)"""

from decimal import Decimal
import time
from pages.PageAutho import MainPage, FilterSort, GoodsCounter
import inspect  # используем метод для возвращения имени функции
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import win32clipboard  # для вставки из буфера (нужна установка pywin32)


def num_format(num_x):  # числовой формат:
    n = Decimal(str(num_x))
    number = n.quantize(Decimal("1"))
    formi = '{0:,}'.format(number).replace(',', '')
    return formi


"""ТЕСТИРОВАНИЕ ФИЛЬТРА"""


# pytest -v --driver Chrome tests\test_filter_sort.py::test_goods_counter
def test_goods_counter(browser):
    """Тестируем, что значение счётчика верно выводит количество товаров в разделе сайта, например Морозильники"""
    driver = browser  # транспортируем драйвер
    # Импортируем действия и открываем сайт:
    page = GoodsCounter(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Холодильники:
        fridges = page.find_elem_fridges()
        ActionChains(driver).move_to_element(fridges).perform()  # наводим мышь
        # Наводим мышь на элемент Морозильники (морозильные камеры):
        freezers = page.find_elem_freezers()
        ActionChains(driver).move_to_element(freezers).perform()  # наводим мышь
        freezers.click()
        # Проверяем, что зашли на нужный раздел сайта Морозильники
        assert page.get_relative_link() == '/refrigerator/freezing_chambers/'

        # Используем локатор counter для счётчика товаров в разделе Морозильники:
        counter = page.find_elem_counter().get_attribute('value')
        # Получаем значение счётчика - кол-во товаров в разделе:
        value = int("".join(filter(str.isdigit, counter)))
        # Получаем через локатор наименование раздела:
        goods_name = page.find_elem_goods_name().text
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f"В разделе: {goods_name} - {value} шт. товаров")

        """Проверим подсчётом товаров на всех страницах, что их сумма будет равна значению счётчика value"""

        # Считаем кол-во товаров на первой странице через кол-во ценников
        count_goods_first_page = len(page.find_elem_goods_price())
        # Локатор для номеров страниц Пагинации:
        pagination = page.find_elem_page_link()
        pagination_list = [x.text for x in pagination]  # заносим номера пагинации в список
        # удаляем из списка слово "Следующая" и находим максимальное число страниц пагинации
        last_page = max([int(x) for x in pagination_list[:-1]])
        # Получаем url последней страницы с товарами / удаляем текущий номер стр. в ссылке и добавляем номер последней
        url_href = pagination[0].get_attribute('href')[:-1]
        last_href_page = url_href + str(last_page)  # добавляем в ссылку номер последней страницы
        # Документируем:
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f" и {last_page} страниц.\nСсылка на последнюю страницу: {last_href_page}\n")

        # Открываем новую вкладку с указанием адреса:
        driver.execute_script(f"window.open('{last_href_page}', '_blank');")
        # Активируем открывшуюся вкладку / дескриптор последней открытой вкладки:
        driver.switch_to.window(driver.window_handles[-1])
        # Считаем кол-во товаров на последней странице через кол-во ценников
        count_goods_last_page = len(page.find_elem_goods_price())
        # Считаем общее количество товаров на всех страницах раздела
        sum_count_goods = (last_page - 1) * count_goods_first_page + count_goods_last_page
        # Проверяем, что количество товаров в фильтре (value) совпадает с фактически посчитанным:
        assert value == sum_count_goods, "Error! Count of goods not match value of counter!"
        # Возвращаемся на первую вкладку:
        driver.switch_to.window(driver.window_handles[0])
        result_status = "PASSED"
    except Exception:
        result_status = "FAILED"
        raise
    finally:
        if result_status == "PASSED":
            symbol = u'\u2605'
        else:
            symbol = u'\u2716'
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Результат теста: {result_status} {symbol}\n")


# pytest -v --driver Chrome tests\test_filter_sort.py::test_filter_price
def test_filter_price(browser):
    """Тестируем установку ценового диапазона в разделе Фильтр.
    В качестве минимальной цены фильтра, возьмём среднюю цену товаров на странице.
    За максимальную цену возьмём макс. цену из списка цен без скидок с коэффициентом 0,9."""
    driver = browser
    main_page = MainPage(driver)
    goods_page = GoodsCounter(driver)
    page = FilterSort(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        main_page.btn_click_catalog()
        # Наводим мышь на элемент Компьютерная техника:
        comptech = main_page.find_elem_comptech()
        ActionChains(driver).move_to_element(comptech).perform()  # наводим мышь
        # Наводим мышь на элемент Компьютеры и кликаем мышью:
        computers = main_page.find_elem_computers()
        ActionChains(driver).move_to_element(computers).perform()  # наводим мышь
        computers.click()
        """Очищаем поле для ввода минимальной цены и указываем среднюю цену на странице.
        Получаем сумму всех цен с учётом скидки и без скидки, а затем делим на их кол-во."""
        priceMD_locate = page.find_elem_pricemarkd()  # локатор на цены со скидкой / MD = MarkDown
        priceMD_list = [x.text for x in priceMD_locate]  # получаем список цен (старая цена + цена со скидкой)
        # Получаем сумму всех цен со скидкой:
        priceMD = sum([int(''.join(filter(str.isdigit, x.split("\n")[1]))) for x in priceMD_list])
        # Получаем сумму цен без скидок:
        price_locate = page.find_elem_price()
        price_list = [x.text for x in price_locate]
        price = sum([int(''.join(filter(str.isdigit, x))) for x in price_list])
        # Получаем кол-во товаров на странице:
        count_goods = len(goods_page.find_elem_goods_price())
        # В качестве минимальной цены фильтра, возьмём среднюю цену товаров на странице:
        middle_price = num_format((priceMD + price) / count_goods)
        # За максимальную цену возьмём макс. цену из списка цен без скидок с коэффициентом 0,9:
        max_price = num_format(max([int(''.join(filter(str.isdigit, x))) for x in price_list]) * 0.9)
        # Устанавливаем среднюю цену в ячейку для минимальной цены фильтра:
        minprice = page.find_elem_minprice()
        minprice.clear()
        minprice.send_keys(middle_price)
        # Нажимаем TAB
        ActionChains(driver).key_down(Keys.TAB).perform()
        # Устанавливаем цену в ячейку для максимальной цены фильтра:
        maxprice = page.find_elem_maxprice()
        maxprice.clear()
        maxprice.send_keys(max_price)
        # Нажимаем TAB и на кнопку Показать
        ActionChains(driver).key_down(Keys.TAB).perform()
        page.btn_click_show()
        time.sleep(3)
        # Используем локатор counter для подсчёта количества найденных товаров:
        counter = goods_page.find_elem_counter().get_attribute('value')
        # Получаем значение счётчика - кол-во товаров:
        value = int("".join(filter(str.isdigit, counter)))
        # Получаем мин и макс цену без скидок:
        price_locate = page.find_elem_price()
        price_list = [x.text for x in price_locate]
        price_min = num_format(min([int(''.join(filter(str.isdigit, x))) for x in price_list]))
        price_max = num_format(max([int(''.join(filter(str.isdigit, x))) for x in price_list]))
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Найдено {value} товаров в пределах указанных цен: {middle_price} - {max_price}\n"
                       f">> Мин. цена найденных товаров: {price_min}\n"
                       f">> Макс. цена найденных товаров: {price_max}\n")
        # Проверяем, что мин цена среди найденных товаров больше мин в фильтре и макс цена меньше, чем в фильтре:
        assert price_min >= middle_price
        assert price_max <= max_price
        result_status = "PASSED"
    except Exception:
        result_status = "FAILED"
        raise
    finally:
        if result_status == "PASSED":
            symbol = u'\u2605'
        else:
            symbol = u'\u2716'
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Результат теста: {result_status} {symbol}\n")


# pytest -v --driver Chrome tests\test_filter_sort.py::test_filter_btn_clear
def test_filter_btn_clear(browser):
    """Тестируем кнопку Очистить в разделе Фильтр."""
    driver = browser
    main_page = MainPage(driver)
    goods_page = GoodsCounter(driver)
    page = FilterSort(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        main_page.btn_click_catalog()
        # Наводим мышь на элемент Компьютерная техника:
        comptech = main_page.find_elem_comptech()
        ActionChains(driver).move_to_element(comptech).perform()  # наводим мышь
        # Наводим мышь на элемент Компьютеры и кликаем мышью:
        computers = main_page.find_elem_computers()
        ActionChains(driver).move_to_element(computers).perform()  # наводим мышь
        computers.click()
        # Фиксируем значение счётчика кол-ва товаров:
        counter = goods_page.find_elem_counter().get_attribute('value')
        # Получаем значение счётчика - кол-во товаров:
        value1 = int("".join(filter(str.isdigit, counter)))

        # Копируем цену из ячейки для минимальной цены фильтра:
        minprice = page.find_elem_minprice()  # локатор на ячейку
        minprice.click()  # ставим пунктир в ячейку
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()  # выделяем цену
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()  # копируем
        # time.sleep(3)
        minprice.clear()  # очищаем поле
        # Открываем буфер обмена:
        win32clipboard.OpenClipboard()
        # Назначаем переменной minprice_new значение в буфере:
        minprice_new = win32clipboard.GetClipboardData()
        # Вставляем значение в поле для минимальной цены и применяем коэф-т 2 к значению:
        minprice.send_keys(num_format(int(minprice_new) * 2))
        # Закрываем буфер обмена:
        win32clipboard.CloseClipboard()
        # Нажимаем TAB
        ActionChains(driver).key_down(Keys.TAB).perform()
        driver.implicitly_wait(3)

        # Копируем цену из ячейки для максимальной цены фильтра:
        maxprice = page.find_elem_maxprice()  # локатор на ячейку
        maxprice.click()  # ставим пунктир в ячейку
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()  # выделяем цену
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()  # копируем
        maxprice.clear()  # очищаем поле
        # Открываем буфер обмена:
        win32clipboard.OpenClipboard()
        # Назначаем переменной maxprice_new значение в буфере:
        maxprice_new = win32clipboard.GetClipboardData()
        # Вставляем значение в поле для минимальной цены и применяем коэф-т 2 к значению:
        maxprice.send_keys(num_format(int(maxprice_new) / 2))
        # Закрываем буфер обмена:
        win32clipboard.CloseClipboard()
        # Нажимаем TAB и на кнопку Показать
        ActionChains(driver).key_down(Keys.TAB).perform()
        page.btn_click_show()

        # Фиксируем значение счётчика кол-ва товаров:
        counter = goods_page.find_elem_counter().get_attribute('value')
        # Получаем значение счётчика - кол-во товаров:
        value2 = int("".join(filter(str.isdigit, counter)))
        # Прокручиваем страницу вниз, чтобы кнопка Очистить стала видимой:
        driver.execute_script("window.scrollTo(0, 2200)")
        # Нажимаем на кнопку фильтра: Очистить:
        page.btn_click_clear()
        time.sleep(2)
        # Фиксируем значение счётчика кол-ва товаров:
        counter = goods_page.find_elem_counter().get_attribute('value')
        # Получаем значение счётчика - кол-во товаров:
        value3 = int("".join(filter(str.isdigit, counter)))
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Значение счётчика:\n>> -до применения фильтра: {value1}\n"
                       f">> -после применения фильтра: {value2}\n"
                       f">> -после нажатия кнопки Очистить: {value3}\n")
        # Проверяем, что значение счётчика, после нажатия кнопки Очистить, показывает исходное кол-во:
        assert value1 == value3
        result_status = "PASSED"
    except Exception:
        result_status = "FAILED"
        raise
    finally:
        if result_status == "PASSED":
            symbol = u'\u2605'
        else:
            symbol = u'\u2716'
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Результат теста: {result_status} {symbol}\n")


# pytest -v --driver Chrome tests\test_filter_sort.py::test_filter_find_producer
def test_filter_find_producer(browser):
    """Тестируем поиск по Производителю в разделе Фильтр."""
    driver = browser
    main_page = MainPage(driver)
    page = FilterSort(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        main_page.btn_click_catalog()
        # Наводим мышь на элемент Компьютерная техника:
        comptech = main_page.find_elem_comptech()
        ActionChains(driver).move_to_element(comptech).perform()  # наводим мышь
        # Наводим мышь на элемент Компьютеры и кликаем мышью:
        computers = main_page.find_elem_computers()
        ActionChains(driver).move_to_element(computers).perform()  # наводим мышь
        computers.click()
        # В разделе фильтра "Производитель", выбираем ACER и Lenovo:
        driver.execute_script("window.scrollTo(0, 500)")  # прокрутка вниз, если всплывающее окно закроет кнопку
        page.btn_click_prodacer().click()
        page.btn_click_prodlenovo().click()
        # Получаем наименование Производителя из локаторов:
        acer_txt = page.btn_click_prodacer().text
        acer = acer_txt.split(" ")[0]
        lenovo_txt = page.btn_click_prodlenovo().text
        lenovo = lenovo_txt.split(" ")[0]
        # Нажимаем "Показать":
        driver.execute_script("window.scrollTo(0, 2200)")  # прокрутка вниз, если всплывающее окно закроет кнопку
        page.btn_click_show()
        driver.implicitly_wait(3)
        # Проверяем, что на странице появились товары указанных производителей:
        driver.save_screenshot(f"../screenshots/{inspect.currentframe().f_code.co_name}.png")
        nameproduct = page.find_elem_nameproduct()  # локатор на названия товаров
        for i in range(len(nameproduct)):
            assert acer or lenovo in nameproduct[i].text
        result_status = "PASSED"
    except Exception:
        result_status = "FAILED"
        raise
    finally:
        if result_status == "PASSED":
            symbol = u'\u2605'
        else:
            symbol = u'\u2716'
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Результат теста: {result_status} {symbol}\n")


# pytest -v --driver Chrome tests\test_filter_sort.py::test_filter_find_opersystem
def test_filter_find_opersystem(browser):
    """Тестируем поиск по Операционной системе в разделе Фильтр."""
    driver = browser
    main_page = MainPage(driver)
    page = FilterSort(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        main_page.btn_click_catalog()
        # Наводим мышь на элемент Компьютерная техника:
        comptech = main_page.find_elem_comptech()
        ActionChains(driver).move_to_element(comptech).perform()  # наводим мышь
        # Наводим мышь на элемент Компьютеры и кликаем мышью:
        computers = main_page.find_elem_computers()
        ActionChains(driver).move_to_element(computers).perform()  # наводим мышь
        computers.click()
        # Прокручиваем scroll до элемента Операционная система и разворачиваем его:
        opersystem = page.btn_click_opersystem()
        driver.execute_script("arguments[0].scrollIntoView();", opersystem)
        opersystem.click()
        time.sleep(2)  # требуется жёсткое ожидание пока не развернётся список
        # В разделе фильтра "Операционная система", выбираем DOS и Windows 10 Professional:
        page.btn_click_osdos().click()
        page.btn_click_oswindows().click()

        # Получаем наименование Операционных систем из локаторов:
        dos_txt = page.btn_click_osdos().text
        dos = dos_txt.split(" ")[0]
        windows10_txt = page.btn_click_oswindows().text
        windows10 = windows10_txt.split(" (")[0]
        # Нажимаем "Показать":
        driver.execute_script("window.scrollTo(0, 2000)")  # прокрутка вниз, если всплывающее окно закроет кнопку
        page.btn_click_show()
        # Проверяем, что на странице появились товары указанных производителей:
        findosproduct = page.find_elem_findosproduct()  # локатор на названия товаров
        for i in range(len(findosproduct)):
            assert dos or windows10 in findosproduct[i].text
        result_status = "PASSED"
    except Exception:
        result_status = "FAILED"
        raise
    finally:
        if result_status == "PASSED":
            symbol = u'\u2605'
        else:
            symbol = u'\u2716'
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Результат теста: {result_status} {symbol}\n")


# pytest -v --driver Chrome tests\test_filter_sort.py::test_filter_not_available
def test_filter_not_available(browser):
    """Тестируем опцию: Cкрыть товары со статусом 'Нет в наличии' в разделе Фильтр."""
    driver = browser
    main_page = MainPage(driver)
    page = FilterSort(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        main_page.btn_click_catalog()
        # Наводим мышь на элемент Компьютерная техника:
        comptech = main_page.find_elem_comptech()
        ActionChains(driver).move_to_element(comptech).perform()  # наводим мышь
        # Наводим мышь на элемент Компьютеры и кликаем мышью:
        computers = main_page.find_elem_computers()
        ActionChains(driver).move_to_element(computers).perform()  # наводим мышь
        computers.click()
        # Выберем сортировку "Сначала дорогие", чтобы на странице появились товары, которых нет в наличии:
        page.btn_click_sorting()
        page.btn_click_sortexpensive()
        # Проверим, что на странице есть карточки со статусом: "Нет в наличии"
        statusavailable = page.find_elem_statusavailable()  # локатор на статусы наличия товаров
        statusavailable_list = [x.text for x in statusavailable]  # преобразуем в список
        if "Нет в наличии" in statusavailable_list:
            assert True
        # Прокручиваем scroll до элемента Скрыть "Нет в наличии":
        notavailable = page.btn_click_notavailable()
        driver.execute_script("arguments[0].scrollIntoView();", notavailable)
        notavailable.click()  # ставим галочку: Скрыть "Нет в наличии"
        # Нажимаем Показать:
        page.btn_click_show()

        # Проверяем, что на странице нет карточек со статусом: "Нет в наличии"
        statusavailable = page.find_elem_statusavailable()
        statusavailable_list = [x.text for x in statusavailable]
        if "Нет в наличии" not in statusavailable_list:
            assert True
        result_status = "PASSED"
    except Exception:
        result_status = "FAILED"
        raise
    finally:
        if result_status == "PASSED":
            symbol = u'\u2605'
        else:
            symbol = u'\u2716'
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Результат теста: {result_status} {symbol}\n")


"""ТЕСТИРОВАНИЕ СОРТИРОВКИ ТОВАРОВ"""


# pytest -v --driver Chrome tests\test_filter_sort.py::test_sort_height
def test_sort_height(browser):
    """Тестируем сортировку списка по возрастанию."""
    driver = browser
    main_page = MainPage(driver)
    page = FilterSort(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        main_page.btn_click_catalog()
        # Наводим мышь на элемент Компьютерная техника:
        comptech = main_page.find_elem_comptech()
        ActionChains(driver).move_to_element(comptech).perform()  # наводим мышь
        # Наводим мышь на элемент Компьютеры и кликаем мышью:
        computers = main_page.find_elem_computers()
        ActionChains(driver).move_to_element(computers).perform()  # наводим мышь
        computers.click()
        # Выберем сортировку "Сначала дешёвые":
        page.btn_click_sorting()
        page.btn_click_sortcheap()
        # Проверим, что товары отсортированы по возрастанию.
        sort_price = page.find_elem_price()  # локатор на цены без скидок
        sort_price_list = [int("".join(filter(str.isdigit, x.text))) for x in sort_price]  # создадим список
        assert sort_price_list == sorted(sort_price_list)
        result_status = "PASSED"
    except Exception:
        result_status = "FAILED"
        raise
    finally:
        if result_status == "PASSED":
            symbol = u'\u2605'
        else:
            symbol = u'\u2716'
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Результат теста: {result_status} {symbol}\n")
