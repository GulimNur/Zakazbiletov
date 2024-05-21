from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.authorization_page import AuthorizationPage

# Test 2 - Search function to find concerts

# Selecting event type
searching_concert = (By.XPATH, '//a[@class="nav-link" and text()="Концерты"]')
# City dropdown menu options
city_filter = (By.XPATH, '//button[@class="btn btn-link dropdown-toggle"]')
# Selecting city Almaty
city = (By.XPATH, '//a[@href="/ru/events/3-kontserty?city=1-almaty"]')
# Searching events by date
event_date = (By.XPATH, '//a[@class="link link--dashed asc"]')
# Selecting an event
event_name = (By.XPATH, '//div[@class="event-item-title js-truncate" and text()="Большой Летний Фестиваль 2024"]')
# Adding tickets
ticket_number = (By.NAME, 'add')
ticket_add = (By.XPATH, '//button[@class="btn btn-danger"]')


class EventPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.authorization_page = AuthorizationPage(browser)

    def concert_button(self):
        return self.find(searching_concert)

    def concert_button_click(self):
        self.concert_button().click()

    def city_filter(self):
        return self.find(city_filter)

    def city_filter_click(self):
        self.city_filter().click()

    def city_select(self):
        return self.find(city)

    def city_select_click(self):
        self.city_select().click()

    def search_by_date(self):
        return self.find(event_date)

    def search_by_date_click(self):
        self.search_by_date().click()

    def select_event(self):
        return self.find(event_name)

    def select_event_click(self):
        self.select_event().click()

    def plus_button(self):
        return self.find(ticket_number)

    def plus_button_click(self):
        self.plus_button().click()

    def add_tickets(self):
        return self.find(ticket_add)

    def add_tickets_click(self):
        self.add_tickets().click()
