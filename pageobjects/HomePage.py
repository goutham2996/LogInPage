from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    link = (By.LINK_TEXT, "Shop")
    def click_link(self):
        return self.driver.find_element(*HomePage.link)