from selenium.webdriver.common.by import By


class CheckOut:

    def __init__(self, driver):
        self.driver = driver

    checkout = (By.XPATH, "//button[@class='btn btn-success']")
    def checkout_button(self):
        return self.driver.find_element(*CheckOut.checkout)



