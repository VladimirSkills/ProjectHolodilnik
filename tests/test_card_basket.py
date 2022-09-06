"""Тестируем Карточку товара и Функционал Корзины (запуск через команду Run)"""

from pages.Config import MAIN_URL
from decimal import Decimal
import time
from pages.PageAutho import *
import pytest
import random
import string
import inspect  # используем метод для возвращения имени функции
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from pages.Settings import valid_email


def num_format(num_x):  # числовой формат:
    n = Decimal(str(num_x))
    number = n.quantize(Decimal("1"))
    formi = '{0:,}'.format(number).replace(',', '')
    return formi


"""ТЕСТИРОВАНИЕ КАРТОЧКИ ТОВАРА"""


# pytest -v --driver Chrome tests\test_card_basket.py::test_product_card
def test_product_card(browser):
    """Тестируем Карточки товаров на странице.
    Проверяем, что есть наименование, фото, цена, код товара, описание, статус наличия, кнопка <В корзину>"""
    driver = browser
    main_page = MainPage(driver)
    filter_page = FilterSort(driver)
    page = ProductCardBasket(driver)
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
        # Локатор на Наименование:
        productsname = main_page.find_elem_productsname()
        # Локатор на Фото:
        locateimages = page.find_elem_locateimages()
        # Локатор на Цены:
        priceall = filter_page.find_price_priceall()
        # Локатор на Код товара:
        cardbycode = page.find_elem_cardbycode()
        # Локатор на Описание товара:
        description = page.find_elem_description()
        # Локатор на Статус <В наличии или Нет>:
        statusavailable = filter_page.find_elem_statusavailable()
        # Локатор на кнопку <В корзину>:
        baskets = page.find_elem_basketsforcard()
        # Делаем скриншот:
        driver.save_screenshot(f"../screenshots/{inspect.currentframe().f_code.co_name}.png")
        # Делаем проверку, что все категории в карточках товаров на странице присутствуют:
        for i in range(len(productsname)):
            assert productsname[i].text != ""
            assert locateimages[i].get_attribute('src') != ""
            assert priceall[i].text != ""
            assert cardbycode[i].text.split(": ")[1] != ""
            assert description[i].text != ""
            assert statusavailable[i].text != ""
        # Делаем проверку наличия кнопок <В корзину>:
        for i in range(0, len(baskets)):
            assert baskets[i].text == "В корзину"
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


"""ТЕСТИРОВАНИЕ ФУНКЦИОНАЛА КОРЗИНЫ"""


# pytest -v --driver Chrome tests\test_card_basket.py::test_put_basket
def test_put_basket(browser):
    """Тестируем перемещение одного товара В корзину"""
    driver = browser
    main_page = MainPage(driver)
    page = ProductCardBasket(driver)
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
        # Получаем имя первого товара в списке:
        firstproductname = page.find_elem_firstproductname().text
        # Нажимаем на кнопку <В корзину> для первого товара в списке:
        page.find_elem_baskets().click()
        # Переходим в корзину:
        page.btn_click_inbasket().click()
        # Проверяем, что в корзине есть товар (имя != "") и его имя совпадает с ранее полученным:
        basketnamegoods = page.find_elem_basketnamegoods()  # локатор на имя товара в корзине
        assert basketnamegoods.text != ""
        assert firstproductname in basketnamegoods.text
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


# pytest -v --driver Chrome tests\test_card_basket.py::test_delete_from_basket
def test_delete_from_basket(browser):
    """Тестируем удаление товара из корзины"""
    driver = browser
    main_page = MainPage(driver)
    page = ProductCardBasket(driver)
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
        # Нажимаем на кнопку <В корзину> для первого товара в списке:
        page.find_elem_baskets().click()
        # Переходим в корзину:
        page.btn_click_inbasket().click()
        # Проверяем, что в корзине есть товар (имя != ""):
        basketnamegoods = page.find_elem_basketnamegoods()  # локатор на имя товара в корзине
        assert basketnamegoods.text != ""
        # Нажимаем на кнопку Удалить товар:
        page.btn_click_delfrombasket()
        driver.implicitly_wait(3)  # установка неявного ожидания
        # Подтверждаем удаление:
        page.btn_click_delfrombasketyes()
        # Проверяем, что появилась надпись "Корзина пуста":
        basketempty = page.find_elem_basketempty().text  # локатор на надпись
        assert "Корзина пуста" in basketempty
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


# pytest -v --driver Chrome tests\test_card_basket.py::test_input_basket
def test_input_basket(browser):
    """Тестируем Вход в Корзину через кнопку в главном меню сайта"""
    driver = browser
    page = ProductCardBasket(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Корзина в главном меню:
        page.btn_click_basket().click()
        # Проверяем, что мы зашли в корзину - будет надпись "Корзина пуста":
        basketempty = page.find_elem_basketempty().text  # локатор на надпись
        assert "Корзина пуста" in basketempty
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


# pytest -v --driver Chrome tests\test_card_basket.py::test_counter_basket
def test_counter_basket(browser):
    """Тестируем работу счётчика Корзины"""
    driver = browser
    main_page = MainPage(driver)
    page = ProductCardBasket(driver)
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
        # Фиксируем показание счётчика:
        counter1 = int(page.find_elem_basketnum().text)
        # Нажимаем на кнопку <В корзину> для первого товара в списке:
        page.find_elem_baskets().click()
        # Нажимаем на кнопку "Перейти в корзину":
        page.btn_click_inbasket().click()
        # Проверяем, что в корзине есть товар (имя != ""):
        basketnamegoods = page.find_elem_basketnamegoods()  # локатор на имя товара в корзине
        assert basketnamegoods.text != ""
        # Фиксируем показание счётчика:
        counter2 = int(page.find_elem_basketnum().text)
        # Проверяем, что счётчик показывает на один товар больше:
        assert counter1 + 1 == counter2
        # Удаляем товар из корзины:
        page.btn_click_delfrombasket()
        driver.implicitly_wait(3)  # установка неявного ожидания
        # Подтверждаем удаление:
        page.btn_click_delfrombasketyes()
        # Обновляем страницу для отображения показания счётчика:
        driver.refresh()
        # Фиксируем показание счётчика:
        counter3 = int(page.find_elem_basketnum().text)
        # Проверяем, что счётчик показывает первоначальное значение:
        assert counter1 == counter3
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


# pytest -v --driver Chrome tests\test_card_basket.py::test_save_goods_basket
def test_save_goods_basket(browser):
    """Тестируем сохранение товара в Корзине после закрытия сайта"""
    driver = browser
    main_page = MainPage(driver)
    page = ProductCardBasket(driver)
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
        # Нажимаем на кнопку <В корзину> для первого товара в списке:
        page.find_elem_baskets().click()
        # Нажимаем на кнопку "Перейти в корзину":
        page.btn_click_inbasket().click()
        # Проверяем, что в корзине есть товар (имя != ""):
        basketnamegoods = page.find_elem_basketnamegoods()  # локатор на имя товара в корзине
        assert basketnamegoods.text != ""
        # Открываем новую вкладку и закрываем текущую с сайтом:
        driver.execute_script(f"window.open('', '_blank');")
        driver.close()
        # Переходим на эту вкладку:
        driver.switch_to.window(driver.window_handles[-1])
        # Открываем на новой вкладке наш сайт:
        driver.execute_script(f"window.open('{MAIN_URL}', '_blank');")
        # Переходим на вкладку с сайтом:
        driver.switch_to.window(driver.window_handles[-1])
        # Нажимаем на значок Корзины:
        page.btn_click_basket().click()
        # Проверяем, что в корзине есть товар (имя != ""):
        basketnamegoods = page.find_elem_basketnamegoods()  # локатор на имя товара в корзине
        assert basketnamegoods.text != ""
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


# pytest -v --driver Chrome tests\test_card_basket.py::test_clear_basket
def test_clear_basket(browser):
    """Тестируем надпись в Корзине: <Очистить всю корзину>"""
    driver = browser
    main_page = MainPage(driver)
    page = ProductCardBasket(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        main_page.btn_click_catalog()
        # Наводим мышь на элемент Смартфоны и гаджеты:
        smartphones = main_page.find_elem_smartphones()
        ActionChains(driver).move_to_element(smartphones).perform()  # наводим мышь
        # Наводим мышь на элемент Смартфоны:
        smartphonprod = main_page.find_elem_smartphonprod()
        ActionChains(driver).move_to_element(smartphonprod).perform()  # наводим мышь
        smartphonprod.click()
        # Прокручиваем scroll до 3-го товара на странице:
        baskets_third = page.find_elem_baskets_third()
        driver.execute_script("arguments[0].scrollIntoView();", baskets_third)
        time.sleep(3)
        # Нажимаем на кнопку <В корзину>, а затем на кнопку <Продолжить покупки> для трёх товаров в списке:
        for i in range(0, 3):
            page.btn_click_baskets_some()[i].click()  # В корзину
            driver.implicitly_wait(3)
            page.btn_click_goshopping().click()  # Кнопка Продолжить...
            driver.implicitly_wait(3)
        # Скроллим вверх:
        driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
        # Нажимаем на значок Корзины:
        page.btn_click_basket().click()
        # Фиксируем показание счётчика:
        driver.implicitly_wait(3)
        counter = int(page.find_elem_basketnum().text)
        # Проверим, если в корзине три товара, нажимаем на надпись Очистить всю корзину:
        if counter == 3:
            page.btn_click_clearbasket()
            # Подтвердим удаление:
            page.btn_click_delfrombasketclear()
        else:
            print('Количество товаров в корзине не соответствует ожиданиям!')
        # Проверим, что в корзине появилась надпись: Корзина пуста
        basketempty = page.find_elem_basketempty().text  # локатор на надпись
        assert "Корзина пуста" in basketempty
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


# pytest -v --driver Chrome tests\test_card_basket.py::test_add_options_basket
def test_add_options_basket(browser):
    """Тестируем добавление дополнительных опций к товару в корзине / Страхование"""
    driver = browser
    main_page = MainPage(driver)
    page = ProductCardBasket(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        main_page.btn_click_catalog()
        # Наводим мышь на элемент Смартфоны и гаджеты:
        smartphones = main_page.find_elem_smartphones()
        ActionChains(driver).move_to_element(smartphones).perform()  # наводим мышь
        # Наводим мышь на элемент Смартфоны:
        smartphonprod = main_page.find_elem_smartphonprod()
        ActionChains(driver).move_to_element(smartphonprod).perform()  # наводим мышь
        smartphonprod.click()
        # Скроллим до первого элемента:
        baskets = page.find_elem_baskets()
        driver.execute_script("arguments[0].scrollIntoView();", baskets)
        # Добавляем первый товар в корзину:
        page.find_elem_baskets().click()
        driver.implicitly_wait(3)
        # Нажимаем Перейти в корзину:
        page.btn_click_inbasket2().click()
        # Фиксируем итоговую цену:
        totalprice1 = int("".join(filter(str.isdigit, page.find_elem_totalprice().text)))
        # Нажимаем на надпись Страхование техники:
        page.btn_click_insurance()
        # Выбираем программу "Год без хлопот"
        page.btn_click_nohassle()
        driver.implicitly_wait(3)
        driver.save_screenshot(f"../screenshots/{inspect.currentframe().f_code.co_name}.png")
        # Нажимаем на кнопку Добавить к заказу:
        page.btn_click_addorder()
        # Проверяем, что доп.опция добавлена к заказу:
        nohassleok = page.find_elem_nohassleok().text  # локатор на название доп. опции
        assert nohassleok != ""
        # Фиксируем итоговую цену повторно:
        totalprice2 = int("".join(filter(str.isdigit, page.find_elem_totalprice().text)))
        # Проверяем, что после добавления опции страхования, цена выросла:
        assert totalprice2 > totalprice1
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Дополнительная опция: {nohassleok}\n"
                       f">> Цена товара: {totalprice1}\n"
                       f">> Итоговая цена с доп. опцией: {totalprice2}\n")
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


# pytest -v --driver Chrome tests\test_card_basket.py::test_checkout_basket
def test_checkout_basket(browser):
    """Тестируем Оформление заказа"""
    driver = browser
    main_page = MainPage(driver)
    page = ProductCardBasket(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        main_page.btn_click_catalog()
        # Наводим мышь на элемент Смартфоны и гаджеты:
        smartphones = main_page.find_elem_smartphones()
        ActionChains(driver).move_to_element(smartphones).perform()  # наводим мышь
        # Наводим мышь на элемент Смартфоны:
        smartphonprod = main_page.find_elem_smartphonprod()
        ActionChains(driver).move_to_element(smartphonprod).perform()  # наводим мышь
        smartphonprod.click()
        # Скроллим до первого элемента:
        baskets = page.find_elem_baskets()
        driver.execute_script("arguments[0].scrollIntoView();", baskets)
        # Добавляем первый товар в корзину:
        page.find_elem_baskets().click()
        # Нажимаем Перейти в корзину:
        page.btn_click_inbasket2().click()
        driver.implicitly_wait(3)
        # Нажимаем кнопку Оформить заказ:
        page.btn_click_basketcheckout()
        time.sleep(2)
        """Указываем телефон, почту и ФИО"""
        # Генерируем случайные номер телефона:
        numbers = random.sample(string.digits, 7)
        numbers_list = list(numbers)
        phone = '937' + ''.join(numbers_list)
        driver.implicitly_wait(3)
        page.elem_click_basketphone()  # кликаем по полю телефон
        page.find_elem_basketphone(phone)  # вставляем телефон
        page.elem_click_basketemail()  # кликаем по полю
        page.find_elem_basketemail(valid_email)  # email
        page.elem_click_basketsurname()  # кликаем по полю
        page.find_elem_basketsurname('Скворцов')  # фамилия
        page.elem_click_basketname()  # кликаем по полю
        page.find_elem_basketname('Андрей')  # имя
        page.elem_click_basketlastname()  # кликаем по полю
        page.find_elem_basketlastname('Петрович')  # отчество
        # Скриншот:
        driver.save_screenshot(f"../screenshots/{inspect.currentframe().f_code.co_name}_1.png")
        time.sleep(2)
        # Нажимаем на кнопку: "Выбрать пункт самовывоза"
        basketpickup = page.btn_click_basketpickup()
        driver.execute_script("arguments[0].scrollIntoView();", basketpickup)
        basketpickup.click()
        time.sleep(2)
        # Выбираем Первый пункт:
        page.btn_click_basketpickup1()
        time.sleep(2)
        # Нажимаем на кнопку: "Заберу здесь"
        page.btn_click_basketpickuphere()
        time.sleep(2)
        # Выбираем Способ оплаты:
        basketpayment = page.btn_click_basketpayment()
        driver.execute_script("arguments[0].scrollIntoView();", basketpayment)
        driver.implicitly_wait(3)
        basketpayment.click()
        # Нажимаем на кнопку Оплатить:
        basketpay = page.btn_click_basketpay()
        driver.execute_script("arguments[0].scrollIntoView();", basketpay)
        basketpay.click()
        driver.implicitly_wait(4)
        # Проверяем, что заказ подтверждён:
        basketorderok = page.find_elem_basketorderok().text
        assert "Ваш заказ успешно оформлен" in basketorderok
        driver.save_screenshot(f"../screenshots/{inspect.currentframe().f_code.co_name}_2.png")
        with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
            file.write(f">> Подтверждение заказа: {basketorderok}\n")
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


# pytest -v --driver Chrome tests\test_card_basket.py::test_add_limit_goods
@pytest.mark.parametrize("value", [10, 30, 50, 60])
def test_add_limit_goods(browser, value):
    """Тестируем наличие лимита при добавлении одного и того же товара в корзину"""
    driver = browser
    main_page = MainPage(driver)
    page = ProductCardBasket(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        main_page.btn_click_catalog()
        # Наводим мышь на элемент Смартфоны и гаджеты:
        smartphones = main_page.find_elem_smartphones()
        ActionChains(driver).move_to_element(smartphones).perform()  # наводим мышь
        # Наводим мышь на элемент Смартфоны:
        smartphonprod = main_page.find_elem_smartphonprod()
        ActionChains(driver).move_to_element(smartphonprod).perform()  # наводим мышь
        smartphonprod.click()
        # Скроллим до первого элемента:
        baskets = page.find_elem_baskets()
        driver.execute_script("arguments[0].scrollIntoView();", baskets)
        # Добавляем первый товар в корзину:
        page.find_elem_baskets().click()
        # Нажимаем Перейти в корзину:
        page.btn_click_inbasket2().click()
        # Очищаем поле для указания кол-во товаров:
        numbergoods = page.find_elem_numbergoods()
        numbergoods.click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()  # выделение
        ActionChains(driver).key_down(Keys.BACKSPACE).key_up(Keys.BACKSPACE).perform()  # удаление
        numbergoods.send_keys(value)
        ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()  # Enter
        time.sleep(2)
        driver.refresh()
        numbergoods = page.find_elem_numbergoods()
        numbergoods.click()
        value2 = numbergoods.get_attribute('value')
        # Проверяем, что указанные значения валидны:
        assert value == int(value2)
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


# pytest -v --driver Chrome tests\test_card_basket.py::test_field_num_notvalid
@pytest.mark.parametrize("value", ['', ' ', -1, '#&', 'фs', '人我'],
                         ids=['empty', 'space', 'minus', 'symbol', 'letters', 'chinese'])
def test_field_num_notvalid(browser, value):
    """Тестируем поле для указания количества товаров на невалидные значения"""
    driver = browser
    main_page = MainPage(driver)
    page = ProductCardBasket(driver)
    result_status = ""
    try:
        page.enter_on_site()
        # Нажимаем на кнопку Каталог:
        main_page.btn_click_catalog()
        # Наводим мышь на элемент Смартфоны и гаджеты:
        smartphones = main_page.find_elem_smartphones()
        ActionChains(driver).move_to_element(smartphones).perform()  # наводим мышь
        # Наводим мышь на элемент Смартфоны:
        smartphonprod = main_page.find_elem_smartphonprod()
        ActionChains(driver).move_to_element(smartphonprod).perform()  # наводим мышь
        smartphonprod.click()
        # Скроллим до первого элемента:
        baskets = page.find_elem_baskets()
        driver.execute_script("arguments[0].scrollIntoView();", baskets)
        # Добавляем первый товар в корзину:
        page.find_elem_baskets().click()
        # Нажимаем Перейти в корзину:
        page.btn_click_inbasket2().click()
        # Очищаем поле для указания кол-во товаров:
        numbergoods = page.find_elem_numbergoods()
        numbergoods.click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()  # выделение
        ActionChains(driver).key_down(Keys.BACKSPACE).key_up(Keys.BACKSPACE).perform()  # удаление
        numbergoods.send_keys(value)
        ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()  # Enter
        time.sleep(2)
        driver.refresh()
        numbergoods = page.find_elem_numbergoods()
        numbergoods.click()
        value2 = numbergoods.get_attribute('value')
        # Проверяем, что указанные значения не будут валидными:
        assert value != int(value2)
        # И что на выходе будет единица:
        assert int(value2) == 1
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
