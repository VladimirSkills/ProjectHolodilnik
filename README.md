## Project of testing <a href = "https://samara.holodilnik.ru/" target="_blank">Holodilnik</a> website.
### Project structure:

### Папка tests:
<Html>
<strong>test_authorization</strong> - Тестируем Регистрацию и Авторизацию на сайте
<br><strong>test_main_page</strong> - Тестируем Открытие сайта и Элементы на главной странице сайта
<br><strong>test_filter_sort</strong> - Тестируем работу Фильтра и Сортировку товаров
<br><strong>test_card_basket</strong> - Тестируем Карточку товара и Функционал Корзины
<br><strong>Notebook.json</strong> - Файл для сохранения результатов тестов
</Html>

### Папка pages:
<Html>
<strong>API_RegMail</strong> - GET-запросы к виртуальному почтовому ящику (1secmail.com) для получения валидного Email и кода для регистрации на сайте.
<br><strong>Locators</strong> - локаторы XPath и CSS на web-элементы сайта
<br><strong>PageAutho</strong> - функции-обёртки для локаторов, распределённые по классам в зависимости от тематики тестов
<br><strong>BaseApp</strong> - функции для применения к локаторам явных ожиданий, получения главной страницы сайта и пути текущей страницы
<br><strong>Config</strong> - исходные статические данные
<br><strong>Settings</strong> - сохранённые, в процессе теста, виртуальные учётные данные
<br><strong>check_count</strong> - файл для нумерации тестов при сохранении результатов в файл Notebook.json. Для обнуления счётчика нужно указать значение = 0.
  
</Html>

### Папка screenshots:
В папке сохраняются скриншоты некоторых страниц.


<Html>
  
<br><strong>ВНИМАНИЕ!
<br>Тесты настроены на запуск через Run!</strong>
<br>При запуске через CMD из Terminal, файлы для хранения учётных данных не будут сохраняться в нужных папках,
что приведёт к ошибке во время выполнения теста.
<br>При необходимости запуска из Terminal можно закомментировать строки, сохраняющие данные в файл, в т.ч. в файле conftest.py
<br><strong>Также на сайте есть Антиробот.</strong> При поточном запуске тестов, возможна блокировка сайта. Лимит на авторизацию - 10 раз.
</Html>

### Ссылка на <a href = "https://docs.google.com/spreadsheets/d/1FHDxmiSO98ZI1dfT5XpDk1JZF2L_adC8/edit?usp=sharing&ouid=113320492480885390471&rtpof=true&sd=true" target="_blank">ЧЕК-ЛИСТ</a> с комментариями.




<Html>
<br><img src="https://i.pinimg.com/564x/ff/cd/a1/ffcda1ddf83fe41924b1481d0ad1ccee.jpg" width="80" height="100">

  
</Html>
