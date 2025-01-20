import allure
from kinopoisk.test_api.page_api.BoardApi import KinopoiskApi

api = KinopoiskApi()


@allure.title("Поиск фильма названию")
@allure.description("Поиск")
@allure.id(1)
@allure.severity("Critical")
def test_find_by_title(test_data: dict):
    query = test_data.get('movie_query')
    name = query['query']
    year = test_data.get('movie_release_date')
    find = api.find_by_title(query)
    json_film = find.json()

    with allure.step("Проверяем, что список не пуст"):
        assert len(json_film) > 0
    with allure.step("Проверка статус кода"):
        assert find.status_code == 200
    with allure.step("Проверка, что название, соответствует запросу"):
        assert json_film['docs'][0]['name'] == name
    with allure.step("Проверка, что год выхода, соответствует запросу"):
        assert json_film['docs'][0]['year'] == year


@allure.title("Поиск фильма по id")
@allure.description("Поиск")
@allure.id(2)
@allure.severity("Critical")
def test_find_by_id(test_data: dict):
    id = test_data.get('movie_id')
    type = test_data.get('type')
    type_movie = type['movie']
    find = api.find_by_id(id)
    json_film = find.json()

    with allure.step("Проверяем, что список не пуст"):
        assert len(json_film) > 0
    with allure.step("Проверка статус кода"):
        assert find.status_code == 200
    with allure.step("Проверка, что id соответствует запросу"):
        assert json_film['id'] == id
    with allure.step("Проверка, что тип, является фильмом"):
        assert json_film['type'] == type_movie


@allure.title("Поиск персон(актёров, режиссёров) по имени")
@allure.description("Поиск")
@allure.id(3)
@allure.severity("Major")
def test_search_by_name(test_data: dict):
    query = test_data.get('movie_person_name')
    actor = query['query']
    id = test_data.get('actor_id')
    find = api.search_by_name(query)
    json_film = find.json()

    with allure.step("Проверяем, что список не пуст"):
        assert len(json_film) > 0
    with allure.step("Проверка статус кода"):
        assert find.status_code == 200
    with allure.step("Проверка, что имя актёра, соответствует запросу"):
        assert json_film['docs'][0]['name'] == actor
    with allure.step("Проверка, что id актёра, соответствует"):
        assert json_film['docs'][0]['id'] == id


@allure.title("Поиск по рейтингу")
@allure.description("Поиск")
@allure.id(4)
@allure.severity("Major")
def test_search_by_rating(test_data: dict):
    query = test_data.get('movie_rating_and_year')
    find = api.uni_find(query)
    json_film = find.json()

    with allure.step("Проверяем, что список не пуст"):
        assert len(json_film) > 0
    with allure.step("Проверка статус кода"):
        assert find.status_code == 200
        assert json_film['docs'][0]['rating']['kp'] > 8.19


@allure.title("Поиск фильма по типу")
@allure.description("Поиск")
@allure.id(5)
@allure.severity("Критический")
def test_search_type(test_data: dict):
    query = test_data.get("movie_type_query")
    cartoon = query['cartoon']
    type = cartoon['type']
    find = api.uni_find(cartoon)
    json_film = find.json()

    with allure.step("Проверяем, что список не пуст"):
        assert len(json_film) > 0
    with allure.step("Проверка статус кода"):
        assert find.status_code == 200
    with allure.step("Проверка, что тип, является мультфильмом"):
        assert json_film['docs'][0]['type'] == type


@allure.title("Поиск фильма с несуществующим id (Негативный)")
@allure.description("Поиск")
@allure.id(6)
@allure.severity("Minor")
def test_negative_search_id(test_data: dict):
    with allure.step("Отправляем GET запрос с несуществующим ID"):
        id = test_data.get('failed_id')
        find = api.find_by_id(id)

        with allure.step("Проверка статус кода"):
            assert find.status_code == 400
