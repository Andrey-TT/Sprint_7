import allure
import pytest
from conftest import courier, courier_methods

class TestCreateCourier:
    @allure.title('Тест регистрации курьера ("ok":true, статус ответа 201)')
    def test_create_courier(self, courier):
        response = courier[2]
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Тест невозможности регистрации двух одинаковых курьеров (статус ответа 409)')
    def test_create_two_identical_couriers(self, courier_methods, courier):
        payload = courier[1]
        response = courier_methods.registration_new_courier(payload)
        assert (response.status_code == 409 and response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.')

    @allure.title('Тест невозможности регистрации курьера при отсутствии обязательных полей: логина или пароля (статус ответа 400)')
    @pytest.mark.parametrize('empty_field_name', ["login", "password"])
    def test_create_courier_with_empty_field_login_or_password(self, courier_methods, empty_field_name):
        payload = courier_methods.courier_data_generation()
        payload[empty_field_name] = ''
        response = courier_methods.registration_new_courier(payload)
        assert (response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для создания учетной записи')

    @allure.title('Тест регистрации курьера при пустом поле first_name ("ok":true, статус ответа 201)')
    def test_create_courier_with_empty_field_first_name(self, courier_methods):
        payload = courier_methods.courier_data_generation()
        payload['first_name'] = ''
        response = courier_methods.registration_new_courier(payload)
        courier_id = courier_methods.login_courier(payload['login'], payload['password'])
        courier_methods.delete_courier(courier_id)
        assert response.status_code == 201 and response.text == '{"ok":true}'
