import allure
import pytest
from conftest import courier, courier_methods

class TestLoginCourier:
    @allure.title('Тест авторизации зарегистрированного курьера ("id":id курьера, статус ответа 200)')
    def test_login_courier(self, courier, courier_methods):
        payload = courier[1]
        login_message = {"id":courier[0]}
        login = payload["login"]
        password = payload["password"]
        response = courier_methods.login_courier(login, password)
        assert response.status_code == 200 and response.json() == login_message

    @allure.title('Тест невозможности авторизации незарегистрированного курьера (статус ответа 404)')
    def test_login_with_unregistered_courier(self, courier_methods):
        login = "unregistered_login",
        password = "unregistered_password"
        response = courier_methods.login_courier(login, password)
        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Тест невозможности авторизации зарегистрированного курьера при отсутствии ввода обязательных полей (статус ответа 400)')
    @pytest.mark.parametrize('empty_field_name', ["login", "password"])
    def test_login_courier_with_empty_field_login_or_password(self, courier, courier_methods, empty_field_name):
        payload = courier[1]
        payload[empty_field_name] = ''
        login = payload["login"]
        password = payload["password"]
        response = courier_methods.login_courier(login, password)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Тест невозможности авторизации зарегистрированного курьера при вводе некорректных данных (статус ответа 404)')
    @pytest.mark.parametrize('field_name', ["login", "password"])
    def test_login_courier_with_incorrect_login_or_password(self, courier, courier_methods, field_name):
        payload = courier[1]
        payload[field_name] = 'incorrect_data'
        login = payload["login"]
        password = payload["password"]
        response = courier_methods.login_courier(login, password)
        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'