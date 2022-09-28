from pages.check_count import counting
import time
import pytest
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service as ChromeService
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
    # headless mode - запуск без графического интерфейса (2 варианта):
    # options.add_argument('--headless')
    # options.headless = True
    options.add_argument('--enable-javascript')  # включаем JS в браузере
    # отключить информационные панели:
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-extensions")  # отключить расширения
    # отключить всплывающее окно: Не удалось загрузить расширение:
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-notifications')  # отключить уведомления
    options.add_argument('--disable-popup-blocking')  # отключить блок всплывающих окон
    options.add_argument('--ignore-certificate-errors')  # отключить проверку сертификата SSL
    # Чтобы предотвратить обнаружение WebDriver, управляемого Selenium, добавим скрипт:
    options.add_argument('--disable-blink-features=AutomationControlled')
    # Отключает обнаружение фишинга на стороне клиента:
    options.add_argument('--disable-client-side-phishing-detection')
    options.add_argument(f'--user-agent={userAgent}')
    # driver = webdriver.Chrome(options=options, executable_path='C:/Python/chromedriver.exe')
    chroms = ChromeService('C:/Python/chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=chroms)
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
