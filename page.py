from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import retrieve_phone_code


class UrbanRoutesPage:

   from_field = (By.ID, 'from')
   to_field = (By.ID, 'to')
   tariff = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')

   call_taxi_button = (By.CSS_SELECTOR, 'button.button.round')
   active_tariff = (By.CSS_SELECTOR, '.tcard.active .tcard-title')

   phone_button = (By.CLASS_NAME, 'np-button')
   phone_input = (By.ID, 'phone')
   phone_next_button = (By.XPATH, '//button[contains(@class,"button") and text()="Siguiente"]')
   phone_code_input = (By.XPATH, '//input[@id="code" and not(contains(@class,"card-input"))]')
   phone_confirm_button = (By.XPATH, '//button[contains(@class,"button") and text()="Confirmar"]')
   phone_shown = (By.CSS_SELECTOR, '.np-text')

   payment_button = (By.CLASS_NAME, 'pp-button')
   add_card_option = (By.CLASS_NAME, 'pp-plus-container')
   card_number_input = (By.ID, 'number')
   card_code_input = (By.CSS_SELECTOR, 'input.card-input#code')
   card_link_button = (By.XPATH, '//button[contains(@class,"button") and text()="Agregar"]')
   card_modal_close = (By.CSS_SELECTOR, '.payment-picker .close-button')
   payment_method_text = (By.CSS_SELECTOR, '.pp-value-text')

   comment_input = (By.ID, 'comment')

   blanket_switch = (By.XPATH,
                     '//div[text()="Manta y pañuelos"]/ancestor::div[contains(@class,"r-type-switch")]'
                     '//span[contains(@class,"slider")]')
   blanket_checkbox = (By.XPATH,
                       '//div[text()="Manta y pañuelos"]/ancestor::div[contains(@class,"r-type-switch")]'
                       '//input[contains(@class,"switch-input")]')
   ice_cream_plus = (By.XPATH,
                     '//div[text()="Helado"]/ancestor::div[contains(@class,"r-type")]'
                     '//div[contains(@class,"counter-plus")]')
   ice_cream_value = (By.XPATH,
                      '//div[text()="Helado"]/ancestor::div[contains(@class,"r-type")]'
                      '//div[contains(@class,"counter-value")]')

   order_button = (By.CSS_SELECTOR, 'button.smart-button')
   order_modal = (By.CSS_SELECTOR, '.order.shown')
   order_title = (By.CSS_SELECTOR, '.order-header-title')
   driver_info = (By.CSS_SELECTOR, '.order-btn-group')

   def __init__(self, driver):
       self.driver = driver

   def set_from(self, from_address):
       from_field = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.from_field))
       from_field.send_keys(from_address)

   def set_to(self, to_address):
       self.driver.find_element(*self.to_field).send_keys(to_address)

   def get_from(self):
       return self.driver.find_element(*self.from_field).get_property('value')

   def get_to(self):
       return self.driver.find_element(*self.to_field).get_property('value')

   def set_route(self, address_from, address_to):
       self.set_from(address_from)
       self.set_to(address_to)

   def visible(self, locator, timeout=15):
       return WebDriverWait(self.driver, timeout).until(
           expected_conditions.visibility_of_element_located(locator))

   def click(self, locator, timeout=15):
       WebDriverWait(self.driver, timeout).until(
           expected_conditions.element_to_be_clickable(locator)).click()


   def click_call_taxi(self):
       self.click(self.call_taxi_button)

   def select_comfort(self):
       self.click(self.tariff)

   def get_active_tariff(self):
       return self.visible(self.active_tariff).text


   def fill_phone(self, phone):
       self.click(self.phone_button)
       field = self.visible(self.phone_input)
       field.clear()
       field.send_keys(phone)
       self.click(self.phone_next_button)
       code = retrieve_phone_code(self.driver)
       code_field = self.visible(self.phone_code_input)
       code_field.clear()
       code_field.send_keys(code)
       self.click(self.phone_confirm_button)

   def get_phone(self):
       return self.visible(self.phone_shown).text


   def add_card(self, number, code):
       self.click(self.payment_button)
       self.click(self.add_card_option)
       self.visible(self.card_number_input).send_keys(number)
       code_field = self.visible(self.card_code_input)
       code_field.send_keys(code)
       code_field.send_keys(Keys.TAB)
       self.click(self.card_link_button)
       self.click(self.card_modal_close)

   def get_payment_method(self):
       return self.visible(self.payment_method_text).text


   def set_message(self, message):
       field = self.visible(self.comment_input)
       field.clear()
       field.send_keys(message)

   def get_message(self):
       return self.visible(self.comment_input).get_property('value')


   def request_blanket(self):
       self.click(self.blanket_switch)

   def is_blanket_active(self):
       return self.driver.find_element(*self.blanket_checkbox).is_selected()


   def add_ice_creams(self, quantity):
       for _ in range(quantity):
           self.click(self.ice_cream_plus)

   def get_ice_cream_count(self):
       return int(self.visible(self.ice_cream_value).text)


   def click_order(self):
       self.click(self.order_button)

   def is_search_modal_visible(self):
       return self.visible(self.order_modal).is_displayed()

   def get_order_title(self):
       return self.visible(self.order_title).text

   def wait_for_driver_info(self, timeout=60):
       return self.visible(self.driver_info, timeout)
