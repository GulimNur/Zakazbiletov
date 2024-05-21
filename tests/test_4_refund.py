from time import sleep
from pages.refund_page import RefundPage
import allure


@allure.feature('Issue Refund')
@allure.story('Completing a refund form')
@allure.description('This test will perform complete a refund form')
def test_refund(browser):
    refund_page = RefundPage(browser)

    with allure.step('Go to site'):
        refund_page.open()

    with allure.step('Handle notification if present'):
        refund_page.handle_notification()
        sleep(2)

    with allure.step('Proceed to refund form'):
        refund_page.refund_request_click()
        sleep(2)

    with allure.step('Completing the refund form'):
        with allure.step('Enter event'):
            refund_page.event_send()
        with allure.step('Enter date'):
            refund_page.date_send()
        with allure.step('Enter name'):
            refund_page.name_send()
        with allure.step('Enter phone'):
            refund_page.phone_send()
        with allure.step('Enter order number'):
            refund_page.order_send()
        with allure.step('Enter email'):
            refund_page.email_send()
            sleep(1)
        with allure.step('Confirming the refund form'):
            refund_page.refund_button_click()
            sleep(1)

    with allure.step('Return to main page'):
        refund_page.go_to_main()
        sleep(1)
