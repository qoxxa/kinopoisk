from MainPage import MainPage
import allure


@allure.title("Авторизация на сайте")
@allure.description("Авторизация")
@allure.id(1)
@allure.severity("Blocker")
def test_auth(browser, test_data: dict):
    email = test_data.get('email')
    password = test_data.get('password')
    url = test_data.get('base_url')
    username = "Константин Погодин"

    ui = MainPage(browser)
    ui.go()
    ui.login_as(email, password)

    name = ui.get_account_name()

    with allure.step("Имя пользователя должно быть "+username):
        assert name == username

    current_url = ui.get_current_url()

    with allure.step("Проверить, что мы на странице "+current_url):
        assert ui.get_current_url().startswith(url)


@allure.title("Поиск фильма по названию")
@allure.description("Поиск")
@allure.id(2)
@allure.severity("Blocker")
def test_search_movie_to_title(browser, test_data: dict):
    title = test_data.get('movie_title')
    movie_year = test_data.get("movie_release_date")

    ui = MainPage(browser)
    ui.go()
    search = ui.search_movie_by_title(title)

    with allure.step("Проверка, что название фильма и год соответствует"):
        assert search == f"{title}{' '}({movie_year})"


@allure.title("Добавление в избранное")
@allure.description("Добавляет фильм в избранное, для дальнейшего просмотра")
@allure.id(3)
@allure.severity("Major")
def test_add_to_favorites(browser, test_data: dict):
    email = test_data.get('email')
    password = test_data.get('password')
    title = test_data.get('movie_title')

    ui = MainPage(browser)
    ui.go()
    ui.login_as(email, password)
    ui.search_movie_by_title(title)

    film_title = ui.add_to_favorites()

    with allure.step("Проверка, что фильм с данным названием добавился в избранное"):
        assert title == film_title


@allure.title("Добавление комментария, к избранному фильму")
@allure.description("Комментарии")
@allure.id(4)
@allure.severity("Minor")
def test_add_comment(browser, test_data: dict):
    email = test_data.get('email')
    password = test_data.get('password')
    title = test_data.get('movie_title')
    comment = test_data.get('comment_txt')

    ui = MainPage(browser)
    ui.go()
    ui.login_as(email, password)

    comment_add = ui.add_comment(title, comment)

    with allure.step("Проверка, что комментарий добавлен, и соответствует введённому"):
        assert comment_add == comment


@allure.title("Редактирование комментария")
@allure.description("Редактирует комментарий к избранному фильму")
@allure.id(5)
@allure.severity("Minor")
def test_edit_comment(browser, test_data: dict):
    email = test_data.get('email')
    password = test_data.get('password')
    new_comment = test_data.get('comment_edit_txt')
    title = test_data.get('movie_title')

    ui = MainPage(browser)
    ui.go()
    ui.login_as(email, password)

    comment_add = ui.edit_comment(title, new_comment)

    with allure.step("Проверка, что комментарий редактирован"):
        assert new_comment == comment_add


@allure.title("Удаление комментария")
@allure.description("Удаляет комментарий у избранного фильма")
@allure.id(6)
@allure.severity("Minor")
def test_delete_from_favorites(browser, test_data: dict):
    email = test_data.get('email')
    password = test_data.get('password')
    title = test_data.get('movie_title')
    notification = test_data.get('notification_favorites')

    ui = MainPage(browser)
    ui.go()
    ui.login_as(email, password)

    delete = ui.delete_from_favorites(title)

    with allure.step("Проверка, что фильмы отсутствуют"):
        assert delete == notification
