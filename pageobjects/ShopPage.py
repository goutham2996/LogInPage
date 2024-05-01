from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self, driver):
        self.driver = driver

    item = (By.XPATH, "//div[@class='card h-100']")
    def item_list(self):
        return self.driver.find_elements(*ShopPage.item)

    item_IPHONE = (By.XPATH, "div/h4")
    def check_phone(self):
        return self.driver.find_element(*ShopPage.item_IPHONE)

    item_f = (By.XPATH, "div/button")
    def item_found(self):
        return self.driver.find_elements(*ShopPage.item_f)

    button = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    def checkout_button(self):
        return self.driver.find_element(*ShopPage.button)

