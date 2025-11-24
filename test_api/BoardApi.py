import requests
from DataProvider import DataProvider
import allure


class KinopoiskApi:
    @allure.step('Запрос test_api')
    def __init__(self) -> None:
        self.url = DataProvider().get('api_url')

    @allure.step('Поиск по названию')
    def find_by_title(self, my_params: dict):
        resp = requests.get(self.url + '/v1.4/movie/search', headers=DataProvider().get('token'), params=my_params)
        return resp

    @allure.step('Поиск по id')
    def find_by_id(self, id):
        resp = requests.get(self.url + '/v1.4/movie/' + str(id), headers=DataProvider().get('token'))
        return resp

    @allure.step('Поиск по имени')
    def search_by_name(self, my_params):
        resp = requests.get(self.url + 'v1.4/person/search', headers=DataProvider().get('token'), params=my_params)
        return resp

    @allure.step('Универсальный поиск')
    def uni_find(self, my_params):
        resp = requests.get(self.url + 'v1.4/movie', headers=DataProvider().get('token'), params=my_params)
        return resp
