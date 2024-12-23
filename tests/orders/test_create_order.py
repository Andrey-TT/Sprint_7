import allure
import pytest
from data import ORDER_DATA
from conftest import order_methods

class TestCreateOrder:
    @allure.title('Тест создания заказа с разными вариантами выбранного цвета (track: номер заказа, статус ответа 201)')
    @pytest.mark.parametrize('color', (['BLACK'], ['GREY'], ['BLACK', 'GREY'], []))
    def test_create_order_with_different_color(self, order_methods, color):
        payload = ORDER_DATA
        payload["color"] = color
        response = order_methods.create_order(payload)
        assert response.status_code == 201 and 'track' in response.json()
