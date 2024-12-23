import allure
from conftest import order_methods

class TestGetOrdersList:
    @allure.title('Тест получения списка заказов (статус ответа 200)')
    def test_get_orders_list(self, order_methods):
        response = order_methods.get_orders_list()
        assert response.status_code == 200 and "orders" in response.json()