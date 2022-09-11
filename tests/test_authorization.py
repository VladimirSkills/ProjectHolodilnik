"""Тестируем Регистрацию и Авторизацию на сайте (запуск через команду Run)"""

from pages.API_RegMail import RegEmail
from pages.PageAutho import RegPage, AuthPage
from pages.Settings import valid_email, valid_password
import time
import pytest
import allure
from faker import Faker  # Для генерации случайного password


"""
ВНИМАНИЕ...
Тесты настроены на запуск через Run!
При запуске через CMD из Terminal, файлы для хранения учётных данных не будут сохраняться в нужных папках,
что приведёт к ошибке во время выполнения теста.
В случае необходимости запуска через CMD, нужно поменять путь к файлам:
с: r"../tests/<имя файла>"
на: "<имя файла>"
...и поменять путь импорта данных из этих файлов, например:
с: from pages.<имя файла> import valid_email, valid_password
на: <имя файла> import valid_email, valid_password
"""

fake = Faker()


class AuthUser:
    @staticmethod
    def random():  # Функция генерирует случайные валидные данные
        password = fake.password()
        return password


def generate_string(num):
    return "x" * num


# pytest -v --driver Chrome tests\test_authorization.py::TestAuthorization
@allure.severity(allure.severity_level.CRITICAL)
class TestAuthorization:
    """Проверка Регистрации и Авторизации на сайте"""

    # Выносим данные в тело класса для доступа к значениям переменных из всех функций класса:
    password = AuthUser.random()  # получаем валидный пароль
    result_email, status_email = RegEmail().get_api_email()  # запрос на получение валидного почтового ящика
    email_reg = result_email[0]  # из запроса получаем валидный email

    # pytest -v --driver Chrome tests\test_authorization.py::TestAuthorization::test_registration_valid
    @allure.severity(allure.severity_level.CRITICAL)
    def test_registration_valid(self, browser):
        """Тестируем валидный вариант регистрации при использовании email и получения кода для входа на почту.
        Используем виртуальный почтовый ящик '1secmail.com' и получаем данные через GET запросы.
        Также сразу создаём пароль через приложение Faker и сохраняем учётные данные в файл settings."""

        driver = browser  # транспортируем драйвер
        # Импортируем действия и открываем сайт:
        page = RegPage(driver)
        result_status = ""
        try:
            page.enter_on_site()
            """1.Отправляем запрос на создание почтового ящика:"""
            # Разделяем email на имя и домен для использования в следующих запросах:
            symbol = self.email_reg.find('@')
            mail_name = self.email_reg[0:symbol]
            mail_domain = self.email_reg[symbol + 1:len(self.email_reg)]
            # Заводим блокнот для хронологии выполнения тестов:
            with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
                file.write(f"Email: '{str(self.email_reg)}'\n>Name: '{mail_name}'\n>Domain: '{mail_domain}'\n")
            # И создаём файл settings для сохранения учётных данных, появляющихся в процессе тестирования:
            with open(r"../pages/Settings.py", 'w', encoding='utf8') as file:
                file.write(f"valid_email = '{str(self.email_reg)}'\nvalid_password = '{self.password}'\n")
            # Сверяем полученные данные с нашими ожиданиями
            assert self.status_email == 200, "status_email error"
            assert len(self.result_email) > 0, "len(result_email) > 0 error"

            """2.Активируем окно ввода кода для прохождения регистрации на сайте:"""
            # Нажимаем на кнопку Войти:
            page.btn_click_enter()
            driver.implicitly_wait(3)
            # Нажимаем на кнопку Другой способ:
            page.btn_click_way()
            driver.implicitly_wait(3)
            # Нажимаем на кнопку По смс или email коду:
            page.btn_click_email()
            driver.implicitly_wait(3)
            # Вводим адрес почты/Email:
            page.enter_email(self.email_reg)
            # Нажимаем на кнопку Получить код:
            page.btn_click_getcode()
            time.sleep(3)  # подождём, пока на почту придёт письмо...

            """3.Проверяем почтовый ящик на наличие писем и достаём ID последнего письма:"""
            result_id, status_id = RegEmail().get_id_letter(mail_name, mail_domain)
            # Получаем id письма с кодом из почтового ящика:
            id_letter = result_id[0].get('id')
            with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
                file.write(f"Id letter: '{str(id_letter)}'\n")
            # Сверяем полученные данные с нашими ожиданиями
            assert status_id == 200, "status_id error"
            assert id_letter > 0, "id_letter > 0 error"

            """4.Получаем код регистрации из письма от интернет-магазина:"""
            result_code, status_code = RegEmail().get_reg_code(mail_name, mail_domain, id_letter)
            # Получаем значение ключа textBody из текста письма:
            text_body = result_code.get('textBody')
            # Извлекаем код из текста методом find:
            reg_code = text_body[
                       text_body.find('Ваш код авторизации: ') + len('Ваш код авторизации: '):text_body.find("С уважением")]
            with open(r"../tests/Notebook.json", 'a', encoding='utf8') as file:
                file.write(f"Registration code: {str(reg_code)}\n")
            # Сверяем полученные данные с нашими ожиданиями
            assert status_code == 200, "status_code error"
            assert reg_code != "", "reg_code != '' error"
            # Вставляем code регистрации в поле для ввода:
            page.enter_code(reg_code)

            """5.Проверяем, что регистрация пройдена и можно зайти в Личный кабинет:"""
            # Так как элемент перекрывается всплывающим меню (NameUser), для клика по нему используем JS.
            # time.sleep(2)  # нужно именно 2 сек
            driver.implicitly_wait(5)  # установка неявного ожидания
            driver.execute_script("arguments[0].click();", page.btn_click_user())
            assert page.get_relative_link() == '/usercp/', "No registration!"

            """6.Создаём пароль для дальнейшей авторизации на сайте"""
            # Нажимаем на пункт меню Смена пароля:
            page.btn_click_changepass()
            # В классе сгенерировали случайный пароль методом Faker и сохранили его в переменной password.
            # Вставляем Пароль в поле Новый пароль и в проверочное поле:
            page.enter_pass(self.password)
            page.enter_pass2(self.password)
            driver.implicitly_wait(3)
            # Нажимаем на кнопку Сохранить изменения:
            page.btn_click_save()
            # Нажимаем на label Выход:
            page.btn_click_exit()
            # Проверяем, что мы вышли...
            assert "Войти" in page.find_elem_enter().text, "Element Enter not found!"
            result_status = "PASSED"
            return self.email_reg, self.password
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

    # pytest -v --driver Chrome tests\test_authorization.py::TestAuthorization::test_authorization_valid
    @allure.severity(allure.severity_level.NORMAL)
    def test_authorization_valid(self, browser):
        """Валидное тестирование Авторизации.
        На сайте стоит ограничение на 10 авторизаций. После интервал = 10 минут"""
        driver = browser
        # Импортируем действия и открываем сайт:
        page = AuthPage(driver)
        result_status = ""
        try:
            page.enter_on_site()
            p = TestAuthorization()
            email = p.email_reg  # импортируем email_reg и сохраняем в переменную email
            passw = p.password  # импортируем password и сохраняем в passw
            # Нажимаем на кнопку Войти:
            page.btn_click_enter()
            driver.implicitly_wait(3)
            # Нажимаем на кнопку Другой способ:
            page.btn_click_way()
            driver.implicitly_wait(3)
            # Нажимаем на кнопку По паролю:
            page.btn_click_bypass()
            driver.implicitly_wait(3)
            # Вводим адрес почты/Email. Если тест регистрации не запускался
            # (т.е. данные из Faker != settings), берём валидные данные из файла settings:
            if email == valid_email:
                mail, site_pass = email, passw
            else:
                mail, site_pass = valid_email, valid_password
            page.enter_email(mail)
            # Вводим пароль/Password:
            page.enter_pass(site_pass)
            driver.implicitly_wait(3)
            # Нажимаем на кнопку Войти:
            page.btn_click_login()
            # Проверяем, что мы прошли авторизацию и зашли в Личный кабинет:
            # Так как элемент перекрывается всплывающим меню (NameUser), для клика по нему используем JS.
            driver.implicitly_wait(3)  # установка неявного ожидания
            driver.execute_script("arguments[0].click();", page.btn_click_user())
            assert page.get_relative_link() == '/usercp/', "No authorization!"
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

    # pytest -v --driver Chrome tests\test_authorization.py::TestAuthorization::test_registration_not_valid
    @pytest.mark.parametrize("value",
                             ['', '   ', 12345, '     @mail.ru', '@mail.ru', 'my_mail@', 'my_mail@ru', '-12345@mail.ru',
                              'my_mail@.ru', 'five@mail.ru', 'five5@mail.рус', 'mail@mail.mail', 'five5@mail.r',
                              'five5@ 123.com', generate_string(250) + '@mail.ru'])
    def test_registration_not_valid(self, browser, value):
        """Тестируем невалидный вариант регистрации. [НЕГАТИВНЫЙ ТЕСТ]"""

        driver = browser  # транспортируем драйвер
        # Импортируем действия и открываем сайт:
        auth_page = AuthPage(driver)
        page = RegPage(driver)
        result_status = ""
        try:
            page.enter_on_site()
            # Нажимаем на кнопку Войти:
            page.btn_click_enter()
            driver.implicitly_wait(2)
            # Нажимаем на кнопку Другой способ:
            page.btn_click_way()
            driver.implicitly_wait(2)
            # Нажимаем на кнопку По смс или email коду:
            page.btn_click_email()
            driver.implicitly_wait(2)
            # Вводим адрес почты/Email (поле для вставки невалидных значений):
            page.enter_email(value)
            # Нажимаем на кнопку Получить код:
            page.btn_click_getcode()
            # Если появится надпись "Нужно ввести...", значит указанное невалидное значение не прошло проверку:
            errorpass = auth_page.find_elem_errorpass().text  # локатор на надпись "Нужно ввести..."
            assert "Нужно ввести" in errorpass
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

    # pytest -v --driver Chrome tests\test_authorization.py::TestAuthorization::test_authorization_not_valid
    @pytest.mark.parametrize("value_mail", ['bq33lazqu@dcctb.com', 'bqlazqu@dcctb.com'],
                             ids=['not active email', 'active email'])
    @pytest.mark.parametrize("value_pass", ['dk4Tdib#j', 'asdf1234w', '$&*@*&$*@&'],
                             ids=['not active pass', 'valid pass from another email', 'not valid pass'])
    def test_authorization_not_valid(self, browser, value_mail, value_pass):
        """Тестируем невалидный вариант авторизации. [НЕГАТИВНЫЙ ТЕСТ]"""
        driver = browser
        # Импортируем действия и открываем сайт:
        page = AuthPage(driver)
        result_status = ""
        try:
            page.enter_on_site()
            # Нажимаем на кнопку Войти:
            page.btn_click_enter()
            driver.implicitly_wait(2)
            # Нажимаем на кнопку Другой способ:
            page.btn_click_way()
            driver.implicitly_wait(2)
            # Нажимаем на кнопку По паролю:
            page.btn_click_bypass()
            driver.implicitly_wait(2)
            # Вводим адрес почты/Email:
            page.enter_email(value_mail)
            # Вводим пароль/Password:
            page.enter_pass(value_pass)
            driver.implicitly_wait(2)
            # Нажимаем на кнопку Войти:
            page.btn_click_login()
            # Проверяем, что невалидные значения сайт не принимает:
            time.sleep(1)
            errorpass = page.find_elem_errorpass().text  # локатор на надпись при неверно указанных данных
            assert 'Еmail и(или) пароль указаны неверно' in errorpass
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
