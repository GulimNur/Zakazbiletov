from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

login_button = (By.XPATH, '//div[@class="auth"]/child::button[@class="btn"]')
email_field = (By.ID, 'loginform-email')
password_field = (By.ID, 'loginform-password')
enter_button = (By.XPATH, '//button[@class="btn btn-danger btn-block"]')
profile_icon = (By.XPATH,'//div[@class="auth"]/descendant::button[@class="btn dropdown-toggle"]')

 # enter_button locator '//button[@class="btn btn-danger btn-block"]'
 # enter_button locator '//*[@id="login-form"]/child::button[@class="btn btn-danger btn-block"


class AuthorizationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://zakazbiletov.kz/')

    def handle_notification(self):
        try:
            # Check if the notification window is present
            notification_window = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.ID, 'onesignal-slidedown-cancel-button'))
            )
            # Click the "Later" option if the notification window appears
            notification_window.click()
            print("Clicked 'Later' on the notification window.")
        except Exception as e:
            # If an exception occurs, print the error message
            print("Error handling notification window:", str(e))
            # Proceeding with login regardless of the error
            print("Proceeding with login.")

    def login_button(self):
        return self.find(login_button)

    def login_button_click(self):
        self.login_button().click()

    def enter_button(self):
        return self.find(enter_button)

    def enter_button_click(self):
        self.enter_button().click()

    def profile_icon(self):
        return self.find(profile_icon)

    ####################################################################

    def username(self):
        return self.find(email_field)

    def username_click(self):
        self.username().click()

    def username_send(self):
        self.username().clear()
        self.username().send_keys('ngulim@yahoo.co.uk')

        ####################################################################

    def password(self):
        return self.find(password_field)

    def password_click(self):
        self.password().click()

    def password_send(self):
        self.password().clear()
        self.password().send_keys('!1testKino!')