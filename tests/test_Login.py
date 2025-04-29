from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
import allure


BASE_URL = "https://ok.ru/"
EMPTY_LOGIN_ERROR = "Введите логин"
EMPTY_PASSWORD_ERROR = "Введите пароль"
WRONG_PASSWORD = '1'

#Тест 2
@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при пустом поле логина в форме авторизации')
@allure.feature('Тест Login Page')
@allure.story('Негативный:Аутентификация:Не заполняем пароль')
def test_empty_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.push_text('MyLogin')
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_PASSWORD_ERROR


