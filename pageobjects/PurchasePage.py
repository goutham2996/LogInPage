from selenium.webdriver.common.by import By


class PurchasePage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    def send_country(self):
        return self.driver.find_element(*PurchasePage.country)

    clickOnIndia = (By.XPATH, "//a[normalize-space()='India']")

    def selectCountry(self):
        return self.driver.find_element(*PurchasePage.clickOnIndia)

    iAgree = (By.XPATH, "//label[@for='checkbox2']")
    def agree(self):
        return self.driver.find_element(*PurchasePage.iAgree)

    purchase = (By.XPATH, "//input[@value='Purchase']")
    def purchaseButton(self):
        return self.driver.find_element(*PurchasePage.purchase)

    text_msg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    def msgDisplayed(self):
        return self.driver.find_element(*PurchasePage.text_msg)
