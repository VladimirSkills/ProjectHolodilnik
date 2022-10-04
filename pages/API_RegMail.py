import json
import requests


class RegEmail:
    """Делаем запрос на сайт 1secmail.com и создаём виртуальный mailbox для регистрации на сайте holodilnik.ru.
     После отправки на почтовый ящик письма с кодом для входа, делаем запрос на получение содержимого письма."""

    def __init__(self):
        self.base_url = "https://www.1secmail.com/api/v1/"

    def get_api_email(self) -> json:
        """Получаем случайный адрес электронной почты"""

        action = {'action': 'genRandomMailbox', 'count': 1}
        res = requests.get(self.base_url, params=action)
        status_email = res.status_code
        try:
            result_email = res.json()
        except json.decoder.JSONDecodeError:
            result_email = res.text
        return result_email, status_email  # возвращаем случайно-сгенерированный почтовый ящик и статус ответа

    def get_id_letter(self, login: str, domain: str) -> json:
        """Проверяем почтовый ящик на наличие писем и достаём ID последнего письма.
        ID нужен для отправки запроса на получение содержимого письма."""

        action = {
            'action': 'getMessages',
            'login': login,
            'domain': domain,
        }
        res = requests.get(self.base_url, params=action)
        status_id = res.status_code
        try:
            result_id = res.json()
        except json.decoder.JSONDecodeError:
            result_id = res.text
        return result_id, status_id  # получаем данные последнего письма в mailbox, где находится его id

    def get_reg_code(self, login: str, domain: str, ids: str) -> json:
        """Получаем содержимое письма от магазина с кодом регистрации (id=ids)"""

        action = {
            'action': 'readMessage',
            'login': login,
            'domain': domain,
            'id': ids
        }
        res = requests.get(self.base_url, params=action)
        status_code = res.status_code
        try:
            result_code = res.json()
        except json.decoder.JSONDecodeError:
            result_code = res.text
        return result_code, status_code  # Получаем значение ключа: textBody, в котором находится код для регистрации


"""Разберём небольшой пример:"""


def get_api_email_example():
    """Получаем случайный адрес электронной почты"""
    action = {'action': 'genRandomMailbox', 'count': 1}
    # count - выводит кол-во email (нам нужен один)
    res = requests.get("https://www.1secmail.com/api/v1/", params=action)
    status_email = res.status_code
    result_email = res.json()
    return result_email, status_email


# запрос на получение виртуального почтового ящика
result_email, status_email = get_api_email_example()
# из запроса получаем email
email_reg = result_email[0]
# Если count будет равен больше 1, тогда email_reg нужно записать так: email_reg = result_email
print(email_reg, '\\', status_email)
# 051kbvea@kzccv.com \ 200
