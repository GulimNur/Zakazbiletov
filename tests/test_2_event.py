from time import sleep
from pages.event_page import EventPage
from pages.authorization_page import AuthorizationPage
import allure


@allure.feature('Event Flow')
@allure.story('Search and select an event')
@allure.description('This test will perform search and selection of an event')
def test_event_flow(browser):
    event_page = EventPage(browser)
    authorization_page = AuthorizationPage(browser)

    try:
        authorization_page.open()
        with allure.step('Navigate to concerts'):
            event_page.concert_button_click()
            sleep(1)

        with allure.step('Searching by city'):
            event_page.city_filter_click()
            sleep(1)
            event_page.city_select_click()
            sleep(1)

        with allure.step('Searching by date'):
            event_page.search_by_date_click()
            sleep(1)

        with allure.step('Selecting a concert'):
            event_page.select_event_click()
            sleep(1)

        with allure.step('Click on "+" button'):
            event_page.plus_button_click()
            sleep(1)

        with allure.step('Adding tickets'):
            event_page.add_tickets_click()
            sleep(1)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        allure.attach(browser.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        raise


