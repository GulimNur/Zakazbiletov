from time import sleep
from pages.authorization_page import AuthorizationPage
import allure


@allure.feature('Authorization')
@allure.story('Authorization to the system')
@allure.description('This test will perform authorization to the website')
def test_authorization(browser):
    authorization_page = AuthorizationPage(browser)

    with allure.step('Go to site'):
        authorization_page.open()

    with allure.step('Handle notification if present'):
        authorization_page.handle_notification()
        sleep(1)

    with allure.step('Click login button'):
        authorization_page.login_button().click()
        sleep(1)

    with allure.step('Write username'):
        authorization_page.username_send()
        sleep(1)

    with allure.step('Write password'):
        authorization_page.password_send()
        sleep(1)

    with allure.step('Click enter button'):
        authorization_page.enter_button().click()
        sleep(1)

    with allure.step('Verify login by checking profile icon'):
        assert authorization_page.profile_icon().is_displayed()
        sleep(1)


@allure.feature('Button Check')
@allure.story('Check if the login button is displayed')
@allure.description('This test will check if the login button is displayed on the site')
def test_button_check(browser):
    with allure.step('Open browser'):
        authorization_page = AuthorizationPage(browser)

    with allure.step('Go to site'):
        authorization_page.open()

    with allure.step('Handle notification if present'):
        authorization_page.handle_notification()
        sleep(2)

    with allure.step('Login button is displayed'):
        assert authorization_page.login_button().is_displayed()
        sleep(10)



