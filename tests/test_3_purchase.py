from time import sleep
from pages.purchase_page import PurchasePage

import allure


@allure.feature('Placing order')
@allure.story('Complete ticket purchase')
@allure.description('This test will perform the purchase tickets after placing order')
def test_purchase(browser):
    purchase_page = PurchasePage(browser)
    try:
        with allure.step('Proceed to checkout'):
            purchase_page.checkout_button().click()
            sleep(1)

        with allure.step('Selecting payment type and method'):
            purchase_page.payment_type_click()
            purchase_page.payment_method_click()
            sleep(1)

        with allure.step('Confirming to terms of purchase'):
            purchase_page.order_agreement_click()
            sleep(1)

        with allure.step('Placing the order and completing the payment'):
            purchase_page.place_order_click()
            sleep(1)

        with allure.step('Return to main page'):
            purchase_page.go_to_main()
            sleep(1)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        allure.attach(browser.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        raise
