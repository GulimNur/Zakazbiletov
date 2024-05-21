from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.event_page import EventPage
# from pages.authorization_page import AuthorizationPage

# Test 3 - Placing the order
# Clicking on placing the order button
checkout_button = (By.XPATH, '//a[@class="btn btn-block btn-danger"]')
# Selecting order form
# order_form = (By.ID, 'order-form')
# Selecting payment type
payment_type = (By.ID, 'orderform-paymenttype')
# Selecting Qiwi Terminal to see the notification
payment_method = (By.XPATH, '//option[@value="2"]')
# Clicking on check-box on agreement
order_agreement = (By.XPATH, '//label[@class="custom-control-label" and text()="Ознакомлен и согласен с "]')
# Selecting order button
place_order = (By.XPATH, '//button[@class="btn btn-danger btn-block js-click-loading"]')
# Return to main page
go_to_main = (By.XPATH, '//a[@class="btn btn-danger"]')


class PurchasePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.event_page = EventPage(browser)  # continuing from event selection

    def checkout_button(self):
        return self.find(checkout_button)

    def checkout_button_click(self):
        self.checkout_button().click()

    def payment_type(self):
        return self.find(payment_type)

    def payment_type_click(self):
        self.payment_type().click()

    def payment_method(self):
        return self.find(payment_method)

    def payment_method_click(self):
        self.payment_method().click()

    def order_agreement(self):
        return self.find(order_agreement)

    def order_agreement_click(self):
        self.order_agreement().click()

    def place_order(self):
        return self.find(place_order)

    def place_order_click(self):
        self.place_order().click()

    def go_to_main(self):
        return self.find(go_to_main)


