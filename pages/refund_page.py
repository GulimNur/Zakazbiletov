from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

# Test 4 - Issue a refund

# refund function
refund_request_locator = (By.XPATH, '//a[@class="nav-link" and text()="Оформить возврат"]')
# refund form complete
line_event = (By.ID, 'refundsform-event')
line_date = (By.ID, 'refundsform-date')
line_name = (By.ID, 'refundsform-name')
line_phone = (By.ID, 'refundsform-phone')
line_order = (By.ID, 'refundsform-order')
line_email = (By.ID, 'refundsform-email')
# click on refund button
refund_button = (By.XPATH, '//button[@class="btn btn-danger"]')
# Return to main page
go_to_main = (By.XPATH, '//a[@class="btn btn-danger"]')


class RefundPage(BasePage):
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

    def refund_request(self):
        return self.find(refund_request_locator)

    def refund_request_click(self):
        self.refund_request().click()

    def refund_button(self):
        return self.find(refund_button)

    def refund_button_click(self):
        self.refund_button().click()

    def go_to_main(self):
        return self.find(go_to_main)

    ############################
    def line_event(self):
        return self.find(line_event)

    def line_event_click(self):
        self.line_event().click()

    def event_send(self):
        self.line_event().clear()
        self.line_event().send_keys('Большой Летний Фестиваль 2024')

    ############################
    def line_date(self):
        return self.find(line_date)

    def line_date_click(self):
        self.line_date().click()

    def date_send(self):
        self.line_date().clear()
        self.line_date().send_keys('22 июн. - 16:00')

    ############################
    def line_name(self):
        return self.find(line_name)

    def line_name_click(self):
        self.line_name().click()

    def name_send(self):
        self.line_name().clear()
        self.line_name().send_keys('Gulim Nur')

    ############################
    def line_phone(self):
        return self.find(line_phone)

    def line_phone_click(self):
        self.line_phone().click()

    def phone_send(self):
        self.line_phone().clear()
        self.line_phone().send_keys('7750255759')

    ############################
    def line_order(self):
        return self.find(line_order)

    def line_order_click(self):
        self.line_order().click()

    def order_send(self):
        self.line_order().clear()
        self.line_order().send_keys('123456')

    ############################
    def line_email(self):
        return self.find(line_email)

    def line_email_click(self):
        self.line_email().click()

    def email_send(self):
        self.line_email().clear()
        self.line_email().send_keys('ngulim@yahoo.co.uk')
