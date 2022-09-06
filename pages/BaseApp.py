from pages.Config import MAIN_URL
from urllib.parse import urlparse
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = MAIN_URL

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator} "
                                                              f">> Page didn't load! Restart test please!")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator} "
                                                              f">> Page didn't load! Restart test please!")

    def not_find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator),
                                                      message=f"Locator in view {locator}")

    def enter_on_site(self):
        return self.driver.get(self.base_url)

    def get_relative_link(self):
        url_path = urlparse(self.driver.current_url)
        return url_path.path
