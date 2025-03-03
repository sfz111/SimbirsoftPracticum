# Практикум SDET: тестовое задание

### Используемые технологии и инструменты
1) Python 3.10
2) Selenium Webdriver + Chrome
3) Webdriver manager
3) Cелекторы для поиска элементов: CSS, XPath, ID
4) Тестовый фреймворк - PyTest
5) Паттерн проектирования Page Object Model
6) Формирования отчетов о пройденных тестах через Allure

### Кейс для автоматизации:
**Предусловие:**
1. Открыть браузер
2. Перейти по ссылке https://practice-automation.com/form-fields/

**Шаги:**
1. Заполнить поле Name
2. Заполнить поле Password
3. Из списка What is your favorite drink? выбрать Milk и Coffee 
4. Из списка What is your favorite color? выбрать Yellow 
5. В поле Do you like automation? выбрать любой вариант 
6. Поле Email заполнить строкой формата name@example.com
7. В поле Message написать количество инструментов, описанных в пункте Automation tools. В поле Message дополнительно написать инструмент из списка Automation tools, содержащий
наибольшее количество символов (Дополнительный пункт)
8. Нажать на кнопку Submit

**Ожидаемый результат:**
Появился алерт с текстом Message received!

### Порядок действий для запуска автотестов локально (для MacOs)

1. #### Установить python 3.10
2. #### Активировать виртуальное окружение

3. #### Установить пакеты
```
pip3 install -r requirements.txt
```
4. #### Запуск тестов 
* Запуск всех тестов без отчета
```
pytest test_form_filling
```

* Запуск теста **test_form_filling** с генерацией отчета в allure
```
pytest -k test_form_filling --alluredir=allure_results

# запуск allure отчета локально
allure serve allure_results
```
Пример отчета о прохождении теста

![img.png](img.png)
