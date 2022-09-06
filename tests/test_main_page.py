"""Тестируем Открытие и главную страницу сайта (запуск через команду Run)"""

from pages.PageAutho import MainPage, SearchField
from decimal import Decimal
import time
import pytest
import inspect  # используем метод для возвращения имени функции
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def num_format(num_x):  # числовой формат:
    n = Decimal(str(num_x))
    number = n.quantize(Decimal("1.00"))
    formi = '{0:,}'.format(number).replace(',', ' ')
    return formi


# pytest -v --driver Chrome tests\test_main_page.py::test_load_main_page
def test_load_main_page(browser):
    """Тестируем открытие сайта и время загрузки элементов главной странице сайта"""
    driver = browser
    page = MainPage(driver)
    start = time.time_ns()
    result_status = ""  # назначает статусу assert переменную
    try:
        page.enter_on_site()
        # Ожидаем загрузку всех главных элементов страницы:
        page.find_elem_rows()
        end = time.time_ns()
        res_time = (end - start) / 1000000000
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Время загрузки элементов на главной странице сайта: {num_format(res_time)} сек\n")
        assert driver.current_url == "https://samara.holodilnik.ru/"
        assert res_time <= 10
        result_status = "PASSED"  # если ошибок нет, то тест прошёл (записываем в переменную)
    except Exception:
        result_status = "FAILED"  # тест не прошёл
        raise  # метод raise в данном случае выводит Failed в консоль, для понимания, что тест не прошёл
    finally:  # метод, который позволяет вывести итоги после обработки исключения
        if result_status == "PASSED":
            symbol = u'\u2605'
        else:
            symbol = u'\u2716'
        # добавляем данные о статусе теста в отчётный файл:
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Результат теста: {result_status} {symbol}\n")


# pytest -v --driver Chrome tests\test_main_page.py::test_middle_load_page
def test_middle_load_page(browser):
    """Тестируем среднее время загрузки сайта при нескольких открытиях"""
    driver = browser
    page = MainPage(driver)
    start = time.time_ns()
    result_status = ""
    try:
        count = 5  # число повторений загрузки сайта
        for i in range(count):
            # Открываем сайт:
            page.enter_on_site()
        end = time.time_ns()
        res_time = (end - start) / 1000000000
        res_middle = res_time / count  # Среднее время загрузки
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Открываем сайт {count} раз подряд...\n"
                       f">> Среднее время загрузки главной страницы сайта: {num_format(res_middle)} сек\n"
                       f">> Ожидание: middle loading <= 2 сек\n")
        assert driver.current_url == "https://samara.holodilnik.ru/"
        assert res_middle <= 2
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


# pytest -v --driver Chrome tests\test_main_page.py::test_button_catalog
def test_button_catalog(browser):
    """Тестируем функционал кнопки Каталог"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Проверяем, что после нажатия открылся список с разделами сайта и в нём есть элемент Телевизоры:
        menu_tv = page.find_elem_tv()
        assert menu_tv.text == "Телевизоры", 'Элемент Телевизоры не найден!'
        # Кнопка Каталог после нажатия меняет название на Закрыть.
        # Проверим, что это произошло нажатием на Закрыть:
        page.btn_click_close()
        # Проверим, что список разделов исчез - через ожидание невидимости элемента Телевизоры:
        not_menu_tv = page.not_find_elem_tv()
        assert not_menu_tv.text == ""  # проверяем, что элемент Телевизоры невидим
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_smartphones
def test_menu_smartphones(browser):
    """Тестируем функционал раздела Смартфоны и гаджеты в Каталоге"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Смартфоны и гаджеты:
        smartphones = page.find_elem_smartphones()
        ActionChains(driver).move_to_element(smartphones).perform()  # наводим мышь
        # Наводим мышь на элемент Samsung:
        samsung = page.find_elem_samsung()
        ActionChains(driver).move_to_element(samsung).perform()  # наводим мышь
        # Открываем ссылку Samsung в новом окне:
        driver.execute_script("arguments[0].setAttribute('target','_blank');", samsung)
        samsung.click()
        # А на текущей странице открываем раздел Смартфоны и гаджеты:
        page.find_elem_smartphones().click()
        # Проверяем, что открылся раздел сайта Смартфоны и гаджеты:
        assert page.get_relative_link() == '/smartphones_gadgets/'
        # Переходим на вкладку открывшейся страницы Samsung и проверяем адрес на соответствие ожиданиям:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/smartphones_gadgets/all/samsung/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_tvsets
def test_menu_tvsets(browser):
    """Тестируем функционал раздела Телевизоры в Каталоге"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Телевизоры:
        menu_tv = page.find_elem_tv()
        ActionChains(driver).move_to_element(menu_tv).perform()  # наводим мышь
        # time.sleep(2)
        # Наводим мышь на элемент Цифровые телевизионные ресиверы:
        receivers = page.find_elem_receivers()
        ActionChains(driver).move_to_element(receivers).perform()  # наводим мышь
        # time.sleep(2)
        # Открываем ссылку Цифровые телевизионные ресиверы в новом окне:
        driver.execute_script("arguments[0].setAttribute('target','_blank');", receivers)
        receivers.click()
        # time.sleep(2)
        # А на текущей странице открываем раздел Телевизоры:
        page.find_elem_tv().click()
        # Проверяем, что открылся раздел сайта Телевизоры:
        assert page.get_relative_link() == '/tv_all/'
        # Переходим на вкладку страницы Цифровые телевизионные ресиверы и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/tv_all/digital_tv_receivers/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_audiovideo
def test_menu_audiovideo(browser):
    """Тестируем функционал раздела Аудио-видео в Каталоге"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Аудио-видео:
        menu_audio = page.find_elem_audio()
        ActionChains(driver).move_to_element(menu_audio).perform()  # наводим мышь
        # time.sleep(2)
        # Наводим мышь на элемент Аудиотехника:
        atechnique = page.find_elem_atechniq()
        ActionChains(driver).move_to_element(atechnique).perform()  # наводим мышь
        # time.sleep(2)
        # Открываем ссылку Аудиотехника в новом окне:
        driver.execute_script("arguments[0].setAttribute('target','_blank');", atechnique)
        atechnique.click()
        # time.sleep(2)
        # А на текущей странице открываем раздел Аудио-видео:
        page.find_elem_audio().click()
        # Проверяем, что открылся раздел сайта Аудио-видео:
        assert page.get_relative_link() == '/audio_video/'
        # Переходим на вкладку страницы Аудиотехника и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/audio_video/audio_equipment/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_comptechnica
def test_menu_comptechnica(browser):
    """Тестируем функционал раздела Компьютерная техника в Каталоге"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Компьютерная техника:
        menu_comptech = page.find_elem_comptech()
        ActionChains(driver).move_to_element(menu_comptech).perform()  # наводим мышь
        # time.sleep(2)
        # Наводим мышь на элемент ЖК мониторы:
        lcdmonitors = page.find_elem_lcdmonitor()
        ActionChains(driver).move_to_element(lcdmonitors).perform()  # наводим мышь
        # time.sleep(2)
        # Открываем ссылку ЖК мониторы в новом окне:
        driver.execute_script("arguments[0].setAttribute('target','_blank');", lcdmonitors)
        lcdmonitors.click()
        # time.sleep(2)
        # А на текущей странице открываем раздел Компьютерная техника:
        page.find_elem_comptech().click()
        # Проверяем, что открылся раздел сайта Компьютерная техника:
        assert page.get_relative_link() == '/digital_tech/'
        # Переходим на вкладку страницы ЖК мониторы и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/digital_tech/lcd_monitors/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_refrigerator
def test_menu_refrigerator(browser):
    """Тестируем функционал раздела Холодильники в Каталоге"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Холодильники:
        fridges = page.find_elem_fridges()
        ActionChains(driver).move_to_element(fridges).perform()  # наводим мышь
        # time.sleep(2)
        # Наводим мышь на элемент Морозильники (морозильные камеры):
        freezers = page.find_elem_freezers()
        ActionChains(driver).move_to_element(freezers).perform()  # наводим мышь
        # time.sleep(2)
        # Открываем ссылку Морозильники в новом окне:
        driver.execute_script("arguments[0].setAttribute('target','_blank');", freezers)
        freezers.click()
        # time.sleep(2)
        # А на текущей странице открываем раздел Холодильники:
        page.find_elem_fridges().click()
        # Проверяем, что открылся раздел сайта Холодильники:
        assert page.get_relative_link() == '/refrigerator/'
        # Переходим на вкладку страницы Морозильники и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/refrigerator/freezing_chambers/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_washers
def test_menu_washers(browser):
    """Тестируем функционал раздела Стиральные машины в Каталоге.
    Расширенный охват проверок (тестируем открытие всех ссылок) и делаем скриншот"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Стиральные машины:
        washers = page.find_elem_washers()
        ActionChains(driver).move_to_element(washers).perform()  # наводим мышь
        driver.implicitly_wait(3)
        # Делаем скриншот списка товаров элемента Стиральные машины:
        driver.save_screenshot(f"../screenshots/{inspect.currentframe().f_code.co_name}.png")
        # Получаем потомков (childs) раздела Стиральные машины из локатора allwashers:
        allwashers = page.find_elem_allwashers()
        childs = allwashers.find_elements(By.TAG_NAME, 'a')
        # Извлекаем ссылку из каждого потомка и открываем её в отдельном окне:
        for item in childs:
            href = item.get_attribute('href')
            driver.execute_script(f"window.open('{href}', '_blank');")
        # А на текущей странице открываем раздел Стиральные машины:
        page.find_elem_washers().click()
        # Проверяем, что открылся раздел сайта Стиральные машины:
        assert page.get_relative_link() == '/washers/'

        # Переходим поочерёдно на открытые вкладки и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/washers/washing_machines/'
        driver.switch_to.window(driver.window_handles[-2])
        assert page.get_relative_link() == '/built-in/washing_mashines/'
        driver.switch_to.window(driver.window_handles[-3])
        assert page.get_relative_link() == '/washers/activator_washing_machines/'
        driver.switch_to.window(driver.window_handles[-4])
        assert page.get_relative_link() == '/washers/washing_mashines_with_dryer/'
        driver.switch_to.window(driver.window_handles[-5])
        assert page.get_relative_link() == '/washers/drying_automatic_device/'
        driver.switch_to.window(driver.window_handles[-6])
        assert page.get_relative_link() == '/washers/washing_accessories/'
        driver.switch_to.window(driver.window_handles[-7])
        assert page.get_relative_link() == '/washers/washing_machines_accessories/'
        driver.switch_to.window(driver.window_handles[-8])
        assert page.get_relative_link() == '/washers/drying_automatic_device_accessories/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_builtin
def test_menu_builtin(browser):
    """Тестируем функционал раздела Встраиваемая техника в Каталоге"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Встраиваемая техника:
        builtin = page.find_elem_builtin()
        ActionChains(driver).move_to_element(builtin).perform()  # наводим мышь
        # Наводим мышь на элемент Встраиваемые винные шкафы:
        winecase = page.find_elem_winecase()
        ActionChains(driver).move_to_element(winecase).perform()  # наводим мышь
        # Открываем ссылку Встраиваемые винные шкафы в новом окне:
        driver.execute_script("arguments[0].setAttribute('target','_blank');", winecase)
        winecase.click()
        # А на текущей странице открываем раздел Встраиваемая техника:
        page.find_elem_builtin().click()
        # Проверяем, что открылся раздел сайта Встраиваемая техника:
        assert page.get_relative_link() == '/built-in/'
        # Переходим на вкладку страницы Встраиваемые винные шкафы и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/built-in/built_in_chamber_for_wine/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_diswashers
def test_menu_diswashers(browser):
    """Тестируем функционал раздела Посудомоечные машины в Каталоге"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Посудомоечные машины:
        diswashers = page.find_elem_diswashers()
        ActionChains(driver).move_to_element(diswashers).perform()  # наводим мышь
        # Наводим мышь на элемент Компактные посудомоечные машины:
        compwashers = page.find_elem_compwashers()
        ActionChains(driver).move_to_element(compwashers).perform()  # наводим мышь
        # Открываем ссылку Компактные посудомоечные машины в новом окне:
        driver.execute_script("arguments[0].setAttribute('target','_blank');", compwashers)
        compwashers.click()
        # А на текущей странице открываем раздел Посудомоечные машины:
        page.find_elem_diswashers().click()
        # Проверяем, что открылся раздел сайта Посудомоечные машины:
        assert page.get_relative_link() == '/dishwashers_all/'
        # Переходим на вкладку страницы Компактные посудомоечные машины и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/dishwashers_all/compact_dishwashers_machines/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_gasstoves
def test_menu_gasstoves(browser):
    """Тестируем функционал раздела Плиты в Каталоге"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Плиты:
        stoves = page.find_elem_stoves()
        ActionChains(driver).move_to_element(stoves).perform()  # наводим мышь
        # Наводим мышь на элемент Газовые плиты:
        gascookers = page.find_elem_gascookers()
        ActionChains(driver).move_to_element(gascookers).perform()  # наводим мышь
        # Открываем ссылку Газовые плиты в новом окне:
        driver.execute_script("arguments[0].setAttribute('target','_blank');", gascookers)
        gascookers.click()
        # А на текущей странице открываем раздел Плиты:
        page.find_elem_stoves().click()
        # Проверяем, что открылся раздел сайта Плиты:
        assert page.get_relative_link() == '/gas-stoves/'
        # Переходим на вкладку страницы Газовые плиты и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/gas-stoves/gas_cookers/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_forkitchen
def test_menu_forkitchen(browser):
    """Тестируем функционал раздела Техника для кухни в Каталоге"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Техника для кухни:
        forkitchen = page.find_elem_forkitchen()
        ActionChains(driver).move_to_element(forkitchen).perform()  # наводим мышь
        # Прокручиваем scroll вниз и Наводим мышь на элемент Кофейное оборудование:
        coffeeset = page.find_elem_coffeeset()
        driver.execute_script("arguments[0].scrollIntoView();", coffeeset)
        ActionChains(driver).move_to_element(coffeeset).perform()  # наводим мышь
        # Открываем ссылку Кофейное оборудование в новом окне:
        driver.execute_script("arguments[0].setAttribute('target','_blank');", coffeeset)
        coffeeset.click()
        # А на текущей странице открываем раздел Техника для кухни:
        page.find_elem_forkitchen().click()
        # Проверяем, что открылся раздел сайта Техника для кухни:
        assert page.get_relative_link() == '/small_domestic/'
        # Переходим на вкладку страницы Кофейное оборудование и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/small_domestic/coffee_set/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_domestichome
def test_menu_domestichome(browser):
    """Тестируем функционал раздела Техника для дома в Каталоге"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Техника для дома:
        domestic = page.find_elem_domestic()
        ActionChains(driver).move_to_element(domestic).perform()  # наводим мышь
        # Наводим мышь на элемент Умный дом:
        smarthouse = page.find_elem_smarthouse()
        ActionChains(driver).move_to_element(smarthouse).perform()  # наводим мышь
        # Открываем ссылку Умный дом в новом окне:
        driver.execute_script("arguments[0].setAttribute('target','_blank');", smarthouse)
        smarthouse.click()
        # А на текущей странице открываем раздел Техника для дома:
        page.find_elem_domestic().click()
        # Проверяем, что открылся раздел сайта Техника для дома:
        assert page.get_relative_link() == '/domestic/'
        # Переходим на вкладку страницы Умный дом и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/domestic/smart_house/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_beauty
def test_menu_beauty(browser):
    """Тестируем функционал раздела Красота и здоровье в Каталоге"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Красота и здоровье:
        beauty = page.find_elem_beauty()
        ActionChains(driver).move_to_element(beauty).perform()  # наводим мышь
        # Наводим мышь на элемент Фены:
        hairdriers = page.find_elem_hairdriers()
        ActionChains(driver).move_to_element(hairdriers).perform()  # наводим мышь
        # Открываем ссылку Фены в новом окне:
        driver.execute_script("arguments[0].setAttribute('target','_blank');", hairdriers)
        hairdriers.click()
        # А на текущей странице открываем раздел Красота и здоровье:
        page.find_elem_beauty().click()
        # Проверяем, что открылся раздел сайта Красота и здоровье:
        assert page.get_relative_link() == '/beauty/'
        # Переходим на вкладку страницы Фены и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/beauty/hair_driers/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_climatic
def test_menu_climatic(browser):
    """Тестируем функционал раздела Климатическая техника в Каталоге"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Климатическая техника:
        climatic = page.find_elem_climatic()
        ActionChains(driver).move_to_element(climatic).perform()  # наводим мышь
        # Наводим мышь на элемент Камины:
        fireplaces = page.find_elem_fireplaces()
        ActionChains(driver).move_to_element(fireplaces).perform()  # наводим мышь
        # Открываем ссылку Камины в новом окне:
        driver.execute_script("arguments[0].setAttribute('target','_blank');", fireplaces)
        fireplaces.click()
        # А на текущей странице открываем раздел Климатическая техника:
        page.find_elem_climatic().click()
        # Проверяем, что открылся раздел сайта Климатическая техника:
        assert page.get_relative_link() == '/climatic/'
        # Переходим на вкладку страницы Камины и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/climatic/fireplaces/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_construction
def test_menu_construction(browser):
    """Тестируем функционал раздела Строительство и ремонт в Каталоге"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Строительство и ремонт:
        construction = page.find_elem_construction()
        ActionChains(driver).move_to_element(construction).perform()  # наводим мышь
        # Наводим мышь на элемент Перфораторы:
        perforators = page.find_elem_perforators()
        ActionChains(driver).move_to_element(perforators).perform()  # наводим мышь
        # Открываем ссылку Перфораторы в новом окне:
        driver.execute_script("arguments[0].setAttribute('target','_blank');", perforators)
        perforators.click()
        # А на текущей странице открываем раздел Строительство и ремонт:
        page.find_elem_construction().click()
        # Проверяем, что открылся раздел сайта Строительство и ремонт:
        assert page.get_relative_link() == '/construction_repair/'
        # Переходим на вкладку страницы Перфораторы и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/construction_repair/perforators/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_cottagegard
def test_menu_cottagegard(browser):
    """Тестируем функционал раздела Товары для дома и сада в Каталоге"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Товары для дома и сада:
        cottagegard = page.find_elem_cottagegard()
        ActionChains(driver).move_to_element(cottagegard).perform()  # наводим мышь
        # Прокручиваем scroll вниз и Наводим мышь на элемент Мебель для дома:
        furniture = page.find_elem_furniture()
        driver.execute_script("arguments[0].scrollIntoView();", furniture)
        ActionChains(driver).move_to_element(furniture).perform()  # наводим мышь
        # Открываем ссылку Мебель для дома в новом окне:
        driver.execute_script("arguments[0].setAttribute('target','_blank');", furniture)
        furniture.click()
        # А на текущей странице открываем раздел Товары для дома и сада:
        page.find_elem_cottagegard().click()
        # Проверяем, что открылся раздел сайта Товары для дома и сада:
        assert page.get_relative_link() == '/cottage_repair/'
        # Переходим на вкладку страницы Мебель для дома и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/cottage_repair/furniture_for_home/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_sportgoods
def test_menu_sportgoods(browser):
    """Тестируем функционал раздела Спорт и отдых в Каталоге"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Спорт и отдых:
        sportgoods = page.find_elem_sportgoods()
        ActionChains(driver).move_to_element(sportgoods).perform()  # наводим мышь
        # Наводим мышь на элемент Силовые тренажеры:
        strongfitness = page.find_elem_strongfitness()
        ActionChains(driver).move_to_element(strongfitness).perform()  # наводим мышь
        # Открываем ссылку Силовые тренажеры в новом окне:
        driver.execute_script("arguments[0].setAttribute('target','_blank');", strongfitness)
        strongfitness.click()
        # А на текущей странице открываем раздел Спорт и отдых:
        page.find_elem_sportgoods().click()
        # Проверяем, что открылся раздел сайта Спорт и отдых:
        assert page.get_relative_link() == '/sport_recreation/'
        # Переходим на вкладку страницы Силовые тренажеры и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/sport_recreation/strength_fitness_equipment/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_kids
def test_menu_kids(browser):
    """Тестируем функционал раздела Детские товары в Каталоге"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Детские товары:
        kids = page.find_elem_kids()
        ActionChains(driver).move_to_element(kids).perform()  # наводим мышь
        # Прокручиваем scroll вниз и Наводим мышь на элемент Конструкторы:
        constructors = page.find_elem_constructors()
        driver.execute_script("arguments[0].scrollIntoView();", constructors)
        ActionChains(driver).move_to_element(constructors).perform()  # наводим мышь
        # Открываем ссылку Конструкторы в новом окне:
        driver.execute_script("arguments[0].setAttribute('target','_blank');", constructors)
        constructors.click()
        # А на текущей странице открываем раздел Детские товары:
        page.find_elem_kids().click()
        # Проверяем, что открылся раздел сайта Детские товары:
        assert page.get_relative_link() == '/kids/'
        # Переходим на вкладку страницы Конструкторы и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/kids/lego_constructors/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_discounted
def test_menu_discounted(browser):  # В случае некорректного загрузки страницы, возможна ошибка с определением локатора
    """Тестируем функционал раздела Уцененные товары в Каталоге. Проверяем наличие скидки и получаем причину уценки"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Прокручиваем scroll вниз и Наводим мышь на элемент Уцененные товары:
        discounted = page.find_elem_discounted()
        driver.execute_script("arguments[0].scrollIntoView();", discounted)
        ActionChains(driver).move_to_element(discounted).perform()  # наводим мышь
        # time.sleep(3)
        # Сохраняем список Категорий уценённых товаров:
        alldiscount = page.find_elem_alldiscount()
        for i in range(len(alldiscount)):
            with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
                file.write(f">> Уценённые товары: {alldiscount[i].text}\n")

        # Наводим мышь на 1-ую категорию в 1-ом списке.
        # (мы не можем зафиксировать локатор, так как категория может меняться)
        discountfirst = page.find_elem_discountfirst()
        ActionChains(driver).move_to_element(discountfirst).perform()  # наводим мышь
        discountfirst.click()
        # Если на новой странице есть надпись Назад, тогда снова переходим по 1-му в списке товару.
        # Иначе уже открыты карточки с описанием товаров и можно сделать проверку на наличие скидки...
        # Надпись Назад:
        discback = page.find_elem_discountback()
        if discback.text == "Назад":
            # Нажимаем на 1-ую категорию во 2-ом списке.
            page.find_elem_discountsecond().click()

        # Проверка карточки, что она содержит: Наименование, фото, цена, старая цена
        # Карточка товара содержит Наименование товара:
        productname = page.find_elem_productname()
        assert productname.text != ""
        # Карточка товара содержит Изображение товара:
        productimage = page.find_elem_productimage()
        assert productimage.get_attribute('src') != ""
        # Карточка товара содержит Цена товара:
        productprice = page.find_elem_productprice().text
        # В цене есть символ рубля. Извлекаем цену через удаление символа и пробелов, используя find:
        symbol_price = productprice.find('₽')
        productprice_int = productprice[0:symbol_price - 1]
        assert int(productprice_int) > 0
        # Карточка товара содержит Старую цену:
        oldprice = page.find_elem_oldprice().text
        symbol_old = oldprice.find('₽')
        oldprice_int = oldprice[0:symbol_old-1]
        assert int(oldprice_int) > 0
        # Карточка товара содержит Скидку:
        assert (int(oldprice_int) - int(productprice_int)) > 0
        # Карточка товара содержит Причину уценки:
        reasonmarkdown = page.find_elem_reasonmarkdown()
        assert len(reasonmarkdown.text) > 20
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Наименование товара: {productname.text}\n"
                       f">> Изображение товара: {productimage.get_attribute('src')}\n"
                       f">> Цена товара с учётом скидки: {int(productprice_int)} руб.\n"
                       f">> Скидка: {int(oldprice_int) - int(productprice_int)} руб.\n"
                       # Причина уценки:
                       f">> {reasonmarkdown.text}\n")
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_action
def test_menu_action(browser):
    """Проверка открытия раздела Акции"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Прокручиваем scroll вниз и Наводим мышь на элемент Акции:
        action = page.find_elem_action()
        driver.execute_script("arguments[0].scrollIntoView();", action)
        action.click()
        # Проверяем, что открылся раздел сайта Акции:
        assert page.get_relative_link() == '/action/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_brandaction
def test_menu_brandaction(browser):
    """Проверяем, что раздел Акции не пустой"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Прокручиваем scroll вниз и Наводим мышь на элемент Акции:
        action = page.find_elem_action()
        driver.execute_script("arguments[0].scrollIntoView();", action)
        action.click()
        # Проверяем, что раздел акции не пустой:
        brandaction = page.find_elem_brandaction()
        assert len(brandaction) > 0
        # Получаем кол-во акций:
        if brandaction[0].text in "Все акции":
            amount_action = len(brandaction) - 1
        else:
            amount_action = len(brandaction)
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Количество текущих акций: {amount_action}\n"
                       f">> Ссылки на акции:\n")
        # Получим ссылки на все акции:
        for i in range(len(brandaction)):
            hrefs = brandaction[i].get_attribute('href')
            with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
                file.write(f">> -{hrefs}\n")
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_brands
def test_menu_brands(browser):
    """Проверка открытия раздела Бренд-зоны"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Прокручиваем scroll вниз и Наводим мышь на элемент Бренд-зоны:
        brands = page.find_elem_brands()
        driver.execute_script("arguments[0].scrollIntoView();", brands)
        brands.click()
        # Проверяем, что открылся раздел сайта Бренд-зоны:
        assert page.get_relative_link() == '/brands/'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_popularbrands
def test_menu_popularbrands(browser):
    """Проверяем, что раздел Бренд-зоны не пустой"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Прокручиваем scroll вниз и Наводим мышь на элемент Бренд-зоны:
        brands = page.find_elem_brands()
        driver.execute_script("arguments[0].scrollIntoView();", brands)
        brands.click()
        # Проверяем, что раздел Бренд-зоны не пустой:
        brandaction = page.find_elem_brandaction()
        assert len(brandaction) > 0
        # Получаем кол-во акций:
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Количество популярных брендов: {len(brandaction)}\n"
                       f">> Ссылки на бренды:\n")
        # Получим ссылки на все бренды:
        for i in range(len(brandaction)):
            hrefs = brandaction[i].get_attribute('href')
            with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
                file.write(f">> -{hrefs}\n")
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


# pytest -v --driver Chrome tests\test_main_page.py::test_find_scrollup
def test_find_scrollup(browser):
    """Проверка появления кнопки наверх при прокрутке страницы вниз"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Проверяем, что кнопка наверх отсутствует:
        no_scrollup = page.not_find_element_scrollup()
        assert no_scrollup.text == ""
        # Прокручиваем страницу Вниз:
        driver.execute_script("window.scrollTo(0, 500)")
        driver.implicitly_wait(3)  # установка неявного ожидания
        # Проверяем, что появилась кнопка наверх:
        scrollup = page.btn_click_scrollup()
        driver.implicitly_wait(3)
        assert scrollup.text == 'Наверх'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_click_scrollup
def test_click_scrollup(browser):
    """Проверка нажатия кнопки наверх после прокрутки страницы вниз"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Прокручиваем страницу Вниз:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.implicitly_wait(3)  # установка неявного ожидания
        # Нажимаем на кнопку Наверх:
        page.btn_click_scrollup().click()
        # Проверяем, что мы поднялись, т.е. кнопка Наверх должна быть невидимой:
        time.sleep(1)  # установка ожидания
        no_scrollup = page.not_find_element_scrollup()
        assert no_scrollup.text == ""
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


# pytest -v --driver Chrome tests\test_main_page.py::test_menu_header
def test_menu_header(browser):
    """Проверка работы элементов Верхнего Меню"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Локатор на элементы Верхнего Меню:
        header = page.find_elem_header()
        # Извлекаем ссылку из каждого элемента и открываем её в отдельном окне:
        for item in header:
            href = item.get_attribute('href')
            driver.execute_script(f"window.open('{href}', '_blank');")
        # Переходим поочерёдно на открытые вкладки и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/smarthome/'
        driver.switch_to.window(driver.window_handles[-2])
        assert page.get_relative_link() == '/smartphones_gadgets/smartphones/'
        driver.switch_to.window(driver.window_handles[-3])
        assert page.get_relative_link() == '/tv_all/tv/'
        driver.switch_to.window(driver.window_handles[-4])
        assert page.get_relative_link() == '/digital_tech/computers/'
        driver.switch_to.window(driver.window_handles[-5])
        assert page.get_relative_link() == '/refrigerator/'
        driver.switch_to.window(driver.window_handles[-6])
        assert page.get_relative_link() == '/washers/'
        driver.switch_to.window(driver.window_handles[-7])
        assert page.get_relative_link() == '/gas-stoves/'
        driver.switch_to.window(driver.window_handles[-8])
        assert page.get_relative_link() == '/climatic/'
        driver.switch_to.window(driver.window_handles[-9])
        assert page.get_relative_link() == '/cottage_repair/'
        driver.switch_to.window(driver.window_handles[-10])
        assert page.get_relative_link() == '/construction_repair/'
        # Делаем скриншот последней открытой страницы:
        driver.save_screenshot(f"../screenshots/{inspect.currentframe().f_code.co_name}.png")
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


# pytest -v --driver Chrome tests\test_main_page.py::test_click_logoimage
def test_click_logoimage(browser):
    """Проверка нажатия на логотип сайта"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на Логотип сайта:
        page.btn_click_logoimage()
        # Проверяем, что открылась главная страница:
        assert page.get_relative_link() == "/"
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


# pytest -v --driver Chrome tests\test_main_page.py::test_click_body
def test_click_body(browser):
    """Проверка работы элементов в теле главной страницы"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        driver.implicitly_wait(3)
        # Локатор на элементы Body:
        body = page.btn_click_body()
        # Извлекаем ссылку из каждого элемента и открываем её в отдельном окне:
        for item in body:
            href = item.get_attribute('href')
            driver.execute_script(f"window.open('{href}', '_blank');")
        # Делаем скриншот последней страницы:
        last_page = -len(body)
        driver.switch_to.window(driver.window_handles[last_page])
        driver.save_screenshot(f"../screenshots/{inspect.currentframe().f_code.co_name}.png")
        # Проверяем, что количество элементов на странице больше 10:
        assert len(body) > 10
        # Локатор на Товар дня:
        driver.switch_to.window(driver.window_handles[0])
        page.btn_goodday()
        gooddayname = page.find_elem_gooddayname().text
        assert gooddayname != ""
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Товар дня:\n{gooddayname}\n")
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


# pytest -v --driver Chrome tests\test_main_page.py::test_click_footer
# @pytest.mark.skip(reason="При запуске теста Антиробот блокирует сайт!")
def test_click_footer(browser):
    """Проверка работы элементов в подвале главной страницы.
    При выполнении теста открываются все ссылки в подвале сайта на новых вкладках и делается скриншот страницы
    последней открытой вкладки... Чтобы сайт не заблочили во время теста, часть кода закомментирована."""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Локатор на элементы footer:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        footer = page.find_elem_footer()
        for item in footer:
            name_href = item.text
            href = item.get_attribute('href')
            # driver.execute_script(f"window.open('{href}', '_blank');")
            with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
                file.write(f">> {name_href}: {href}\n")

        # # Делаем скриншот последней страницы:
        # last_page = -len(footer)
        # driver.switch_to.window(driver.window_handles[last_page])
        # driver.save_screenshot(f"../screenshots/{inspect.currentframe().f_code.co_name}.png")
        # # Проверяем, что открылась страница по последней ссылке в footer:
        # assert page.get_relative_link() == '/about/public_offer/'
        href_last_element = footer[-1].get_attribute('href')
        assert '/about/public_offer/' in href_last_element
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


# pytest -v --driver Chrome tests\test_main_page.py::test_search_by_name
def test_search_by_name(browser):
    """Проверка поиска по Имени товара"""
    driver = browser
    main_page = MainPage(driver)
    page = SearchField(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        main_page.btn_click_catalog()
        # Наводим мышь на элемент Телевизоры:
        menu_tv = main_page.find_elem_tv()
        ActionChains(driver).move_to_element(menu_tv).perform()  # наводим мышь
        # Нажимаем на элемент Цифровые телевизионные ресиверы:
        main_page.find_elem_receivers().click()
        # Получаем наименование 3-го элемента в списке товаров
        byname = page.find_elem_byname().text
        # Вставляем полученное название в поле Поиска:
        page.find_elem_field(byname)
        # Нажимаем на кнопку поиска:
        page.btn_search()
        # Проверяем, что получены результаты поиска:
        amountfound = page.find_elem_amountfound().text  # счётчик найденных товаров
        assert int(amountfound) > 0
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


# pytest -v --driver Chrome tests\test_main_page.py::test_search_by_code
def test_search_by_code(browser):
    """Проверка поиска по Коду товара"""
    driver = browser
    main_page = MainPage(driver)
    page = SearchField(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        main_page.btn_click_catalog()
        # Наводим мышь на элемент Телевизоры:
        menu_tv = main_page.find_elem_tv()
        ActionChains(driver).move_to_element(menu_tv).perform()  # наводим мышь
        # Нажимаем на элемент Цифровые телевизионные ресиверы:
        main_page.find_elem_receivers().click()
        # Получаем код 2-го элемента в списке товаров
        bycode = page.find_elem_bycode().text
        symbol = bycode.find(': ')
        bycode_num = bycode[symbol+2:len(bycode)]
        # Вставляем полученный код в поле Поиска:
        page.find_elem_field(bycode_num)
        # Нажимаем на кнопку поиска:
        page.btn_search()
        # Проверяем, что получены результаты поиска:
        amountfound = page.find_elem_amountfound().text  # счётчик найденных товаров
        assert int(amountfound) > 0
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


@pytest.mark.parametrize("value", ['Однокамерный холодильник', 'Single chamber refrigerator',
                                   '441142', 'Цифровой телевизионный ресивер 448010', '123456789'],
                         ids=['name_rus', 'name_en', 'code', 'name + code', 'digit'])
def test_search_valid(browser, value):
    """Проверка поля Поиск при указании валидных значений"""
    driver = browser
    page = SearchField(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Вставляем значение в поле Поиска:
        page.find_elem_field(value)
        time.sleep(2)
        # Нажимаем на кнопку поиска:
        page.btn_search()
        # Проверяем, что получены результаты поиска:
        amountfound = page.find_elem_amountfound().text
        assert int(amountfound) > 0
        # Сохраняем комментарии результатов поиска:
        comentfound = page.find_elem_comentfound().text
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Результаты поиска:\n>> {comentfound}\n")
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


def generate_string(num):
    return "x" * num


def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


def big_number(x):
    return x ** x * x


@pytest.mark.parametrize("value", ['', '    ', generate_string(255), chinese_chars(), special_chars(), big_number(82),
                                   '<script>alert(123)</script>'], ids=['Empty', 'Spaces', '255 symbols', 'chinese',
                                                                        'special', 'big_number', 'script-XSS'])
def test_search_notvalid(browser, value):
    """Проверка поля Поиск при указании НЕвалидных значений"""
    driver = browser
    page = SearchField(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Вставляем значение в поле Поиска:
        page.find_elem_field(value)
        time.sleep(2)
        # Нажимаем на кнопку поиска:
        page.btn_search()
        # Проверяем, что получены результаты поиска:
        amountfound = page.find_elem_amountfound().text
        assert int(amountfound) > 0
        # Сохраняем комментарии результатов поиска:
        comentfound = page.find_elem_comentfound().text
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Результаты поиска:\n>> {comentfound}\n")
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


# pytest -v --driver Chrome tests\test_main_page.py::test_add_favorites
def test_add_favorites(browser):
    """Тестируем добавление товара <В избранное>"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        page.btn_click_catalog()
        # Наводим мышь на элемент Компьютерная техника:
        comptech = page.find_elem_comptech()
        ActionChains(driver).move_to_element(comptech).perform()  # наводим мышь
        # Наводим мышь на элемент Компьютеры и кликаем мышью:
        computers = page.find_elem_computers()
        ActionChains(driver).move_to_element(computers).perform()  # наводим мышь
        computers.click()
        # Запишем значение счётчика Избранное:
        favoritcounter1 = page.find_elem_favoritcounter().text  # локатор на счётчик
        # Нажмём на надпись "В избранное" на первой карточке товара:
        page.btn_click_favorites().click()
        time.sleep(2)
        # Проверим, что значение счётчика Избранное стало больше:
        favoritcounter2 = page.find_elem_favoritcounter().text  # локатор на счётчик
        assert int(favoritcounter2) > int(favoritcounter1)
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


# pytest -v --driver Chrome tests\test_main_page.py::test_social_network
def test_social_network(browser):
    """Тестируем открытие ссылок на значках Соцсетей"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Скроллим вниз страницы:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.implicitly_wait(3)
        # Нажимаем поочерёдно на значки и открываем ссылки в новой вкладке:
        networks = page.btn_click_network()
        for item in networks:
            href = item.get_attribute('href')
            driver.execute_script(f"window.open('{href}', '_blank');")
        # Переходим поочерёдно на открытые вкладки и проверяем ожидания:
        driver.switch_to.window(driver.window_handles[-1])
        assert page.get_relative_link() == '/holodilnik__ru'
        driver.switch_to.window(driver.window_handles[-2])
        assert page.get_relative_link() == '/@holodilnik.ru'
        driver.switch_to.window(driver.window_handles[-3])
        assert page.get_relative_link() == '/id/60e587652be2883c90bfb907'
        driver.switch_to.window(driver.window_handles[-4])
        assert page.get_relative_link() == '/group/61678334509134'
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


# pytest -v --driver Chrome tests\test_main_page.py::test_change_town
def test_change_town(browser):
    """Тестируем изменение текущего города"""
    driver = browser
    page = MainPage(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на выбор города:
        page.btn_click_town().click()
        driver.implicitly_wait(3)
        # Выбираем Казань:
        page.btn_click_townkazan()
        driver.implicitly_wait(3)
        # Проверяем, что текущий город - Казань:
        kazan = page.btn_click_town().text
        # Можем сделать скриншот:
        driver.save_screenshot(f"../screenshots/{inspect.currentframe().f_code.co_name}.png")
        assert "Казань" in kazan
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
