import json
import allure
import requests
from urls import BASE_URL, ORDERS_URL

class OrderMethods:
    @allure.step('Создание нового заказ')
    def create_order(self, payload):
        return requests.post(f'{BASE_URL}{ORDERS_URL}', data=json.dumps(payload))

    @allure.step('Получение списка заказов')
    def get_orders_list(self):
        return requests.get(f'{BASE_URL}{ORDERS_URL}')
