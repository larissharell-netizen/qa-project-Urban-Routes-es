import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page import UrbanRoutesPage


class TestUrbanRoutes:

   driver = None

   def setup_method(self):
       options = Options()
       options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
       self.driver = webdriver.Chrome(options=options)
       self.driver.get(data.urban_routes_url)
       self.routes_page = UrbanRoutesPage(self.driver)

   def teardown_method(self):
       self.driver.quit()

   def route_and_comfort(self):
       self.routes_page.set_route(data.address_from, data.address_to)
       self.routes_page.click_call_taxi()
       self.routes_page.select_comfort()

   def ready_to_order(self):
       self.route_and_comfort()
       self.routes_page.fill_phone(data.phone_number)
       self.routes_page.add_card(data.card_number, data.card_code)
       self.routes_page.set_message(data.message_for_driver)


   def test_1_set_route(self):
       address_from = data.address_from
       address_to = data.address_to
       self.routes_page.set_route(address_from, address_to)
       assert self.routes_page.get_from() == address_from
       assert self.routes_page.get_to() == address_to

   def test_2_select_comfort_tariff(self):
       self.route_and_comfort()
       assert self.routes_page.get_active_tariff() == 'Comfort'

   def test_3_fill_phone_number(self):
       self.route_and_comfort()
       self.routes_page.fill_phone(data.phone_number)
       assert self.routes_page.get_phone() == data.phone_number

   def test_4_add_credit_card(self):
       self.route_and_comfort()
       self.routes_page.add_card(data.card_number, data.card_code)
       assert self.routes_page.get_payment_method() == 'Tarjeta'

   def test_5_write_message_for_driver(self):
       self.route_and_comfort()
       self.routes_page.set_message(data.message_for_driver)
       assert self.routes_page.get_message() == data.message_for_driver

   def test_6_order_blanket_and_tissues(self):
       self.route_and_comfort()
       self.routes_page.request_blanket()
       assert self.routes_page.is_blanket_active() is True

   def test_7_order_two_ice_creams(self):
       self.route_and_comfort()
       self.routes_page.add_ice_creams(2)
       assert self.routes_page.get_ice_cream_count() == 2

   def test_8_search_taxi_modal_appears(self):
       self.ready_to_order()
       self.routes_page.click_order()
       assert self.routes_page.is_search_modal_visible()
       assert 'Buscar' in self.routes_page.get_order_title()

   def test_9_driver_info_appears(self):
       self.ready_to_order()
       self.routes_page.click_order()
       assert self.routes_page.is_search_modal_visible()
       assert self.routes_page.wait_for_driver_info(timeout=60).is_displayed()
