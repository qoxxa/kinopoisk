from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure
from kinopoisk.DataProvider import DataProvider
from selenium.webdriver.common.keys import Keys


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = DataProvider().get('base_url')
        self.__driver = driver

    @allure.step("Перейти на сайт")
    def go(self) -> None:
        self.__driver.get(self.__url)

    @allure.step("Авторизоваться под {email}:{password}")
    def login_as(self, email: str, password: str):
        WebDriverWait(self.__driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.styles_loginButton__LWZQp'))).click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#passp-field-login"))).send_keys(email)
        self.__driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#passp-field-passwd"))).send_keys(password)
        self.__driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    @allure.step("Получить имя пользователя")
    def get_account_name(self) -> str:
        ActionChains(self.__driver).move_to_element(WebDriverWait(self.__driver, 50).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.styles_root__42Fk8')))).perform()
        menu = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="styles_primaryTitle__lGNUB styles_primaryTitleDefaultAccount__a0_6V"]')))
        return menu.text

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url

    @allure.story("Поиск фильма по названию")
    def search_movie_by_title(self, title: str):
        search_bar = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[placeholder='Фильмы, сериалы, персоны']")))
        search_bar.send_keys(title)
        search_bar.send_keys(Keys.RETURN)

        movie_link = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, title)))
        movie_link.click()

        movie_title = self.__driver.find_element(By.CSS_SELECTOR, "[itemprop='name']")

        return movie_title.text

    @allure.story("Добавление фильма в 'Буду смотреть'")
    def add_to_favorites(self) -> str:
        self.__driver.find_element(By.CSS_SELECTOR, "button[title='Буду смотреть']").click()
        self.__driver.find_element(By.CSS_SELECTOR, '.styles_filmsToWatchButton__r_vSy').click()

        film_title = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.name')))

        return film_title.text

    @allure.story("Удаление фильма из 'Буду смотреть'")
    def delete_from_favorites(self, title: str) -> str:
        self.__driver.find_element(By.CSS_SELECTOR, '.styles_filmsToWatchButton__r_vSy').click()

        ActionChains(self.__driver).move_to_element(WebDriverWait(self.__driver, 50).until(EC.visibility_of_element_located((
            By.LINK_TEXT, title)))).perform()

        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[title="удалить фильм"]'))).click()

        notification = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.emptyMessage')))

        return notification.text

    @allure.story("Добавить комментарий")
    def add_comment(self, title: str, comment: str) -> str:
        self.__driver.find_element(By.CSS_SELECTOR, '.styles_filmsToWatchButton__r_vSy').click()

        ActionChains(self.__driver).move_to_element(
            WebDriverWait(self.__driver, 50).until(EC.visibility_of_element_located((
                By.LINK_TEXT, title)))).perform()

        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[title="Добавить комментарий"]'))).click()

        self.__driver.find_element(By.CSS_SELECTOR, '[onkeyup]').send_keys(comment)
        self.__driver.find_element(By.CSS_SELECTOR, '.save').click()

        ActionChains(self.__driver).move_to_element(
            WebDriverWait(self.__driver, 50).until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, '.add.edit.commentIconOn')))).perform()

        txt = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'div[class="sign"]')))

        return txt.text

    @allure.story("Редактировать комментарий")
    def edit_comment(self, title: str, comment_edit: str) -> str:
        self.__driver.find_element(By.CSS_SELECTOR, '.styles_filmsToWatchButton__r_vSy').click()

        ActionChains(self.__driver).move_to_element(
            WebDriverWait(self.__driver, 50).until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, '.add.edit.commentIconOn')))).perform()

        self.__driver.find_element(By.CSS_SELECTOR, '[value="редактировать"]').click()
        self.__driver.find_element(By.CSS_SELECTOR, '[onkeyup]').clear()
        self.__driver.find_element(By.CSS_SELECTOR, '[onkeyup]').send_keys(comment_edit)
        self.__driver.find_element(By.CSS_SELECTOR, '.save').click()

        ActionChains(self.__driver).move_to_element(
            WebDriverWait(self.__driver, 50).until(EC.visibility_of_element_located((
                By.LINK_TEXT, title)))).perform()

        ActionChains(self.__driver).move_to_element(
            WebDriverWait(self.__driver, 50).until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, '.add.edit.commentIconOn')))).perform()

        txt = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'div[class="sign"]')))

        return txt.text
