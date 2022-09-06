from pages.check_count import counting
import time
import pytest
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
options = Options()
ua = UserAgent()
userAgent = ua.random


# Функция для подсчёта количества запусков тестов.
# Для обнуления счётчика нужно установить значение переменной counting = 0 в файле check_count.
def counter():
    count = counting + 1
    with open(r"../pages/check_count.py", 'w', encoding='utf8') as file:
        file.write(f"counting = {count}\n")
    return count


@pytest.fixture(autouse=False, scope="session")
def browser():
    with webdriver.Chrome() as driver:
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # options.add_argument("--headless")  # запуск браузера без графического интерфейса
        options.add_argument('disable-infobars')  # отключить информационные панели
        options.add_argument('--disable-notifications')  # отключить уведомления
        options.add_argument('--disable-popup-blocking')  # отключить всплывающие окна
        webdriver.Chrome(options=options)  # executable_path='C:/Python/chromedriver.exe')
        options.add_argument(f"--user-agent={userAgent}")
        # Переходим на страницу сайта
        driver.maximize_window()

        yield driver

        driver.quit()


@pytest.fixture(autouse=True)
# Получение времени обработки теста
def time_delta_teardown(request):
    count = counter()
    with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
        file.write(f"\n>>>[{count}]<>{request.node.name}\n")
    start_time = time.time_ns()  # засекаем время начала теста
    yield
    end_time = time.time_ns()
    res_time = (end_time - start_time)//1000000
    with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
        file.write(f">> Время выполнения теста: {res_time/1000} сек\n")
    print(f"\n>>> {request.node.name} >>> Время выполнения теста: {res_time}мс ({res_time/1000}сек)")
