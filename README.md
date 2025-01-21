# Проект: Автоматизированные тесты для сайта Кинопоиск

## Задача

Данный проект предназначен для автоматизации тестирования веб-сайта kinopoisk.ru. Тесты охватывают как функциональность пользовательского интерфейса (UI), так и API. Основная цель проекта — обеспечить качество и стабильность приложения через выполнение автоматизированных тестов.

## Запуск тестов

Для запуска тестов выполните следующие шаги:
1. Склонировать проект


2. Убедитесь, что у вас установлены все зависимости, указанные в `requirements.txt`.
    Для автоматической установки, воспользуйтесь командой: 
    ```bash
    pip install -r requirements.txt
    ```
    

3. Запустите тесты с генерацией отчётности, используя один из следующих режимов:
   - Запуск UI-тестов:
     ```bash
     pytest -s -v --alluredir=allure-results test_api.py
     ```
   - Запуск API-тестов:
     ```bash
     pytest -s -v --alluredir=allure-results test_ui.py
     ```
     и откройте отчет с помощью команды:
        ```bash
        allure serve allure_results
        ```

4. Для автоматизации отчётности allure, используйте команду:
    ```bash
    ./run.sh
    ```
      
## Структура проекта


- **requirements.txt**: Содержит список необходимых библиотек для выполнения тестов.
- **pytest.ini**: Настройки для pytest, включая пути к тестам и шаблон имен файлов.
- **run.sh**: Скрипт для запуска тестов и автоматизации отчётности allure.
- **DataProvider.py**: Возвращает данные из базы.
- **/test_ui/page/MainPage.py**: Методы для работы c UI тестами.
- **/test_api/page_api/BoardApi.py**: Методы для работы c API тестами.
- **/test_api/test_ui.py**: Тесты, проверяющие функциональность UI.
- **/test_api/test_api.py**: Тесты, проверяющие функциональность API.
- **test_data.json**: База с тестовыми данными.


## Полезные ссылки

- [Подсказка по markdown] (https://markdownguide.offshoot.io/cheat-sheet/)
- [Генератор файла .gitignore] (https://www.toptal.com/developers/gitignore)
- [Про pip freeze] (https://pip.pypa.io/en/latest/cli/pip_freeze/)

## Финальный проект
- [Тест-план Кинопоиск] (https://koxxa.yonote.ru/share/1011ca00-b777-4bd8-828f-8a7cc04baab6)
