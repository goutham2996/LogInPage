import time

from selenium.webdriver.common.by import By

from pageobjects.ChecckOutPage import CheckOut
from pageobjects.HomePage import HomePage
from pageobjects.PurchasePage import PurchasePage
from pageobjects.ShopPage import ShopPage
from utilities.BaseClass import BaseClass


class TestShopping(BaseClass):


    def test_shopping(self):
        url = "https://rahulshettyacademy.com/angularpractice/"
        #navigating website
        self.driver.get(url)
        self.driver.implicitly_wait(3)

        homePage = HomePage(self.driver)
        homePage.click_link().click()

        shopPage = ShopPage(self.driver)

        items_of_phone = shopPage.item_list()
        for i in items_of_phone:
            phone = i.find_element(By.XPATH, "div/h4").text
            if phone == "iphone X":
                i.find_element(By.XPATH, "div/button").click()

        shopPage.checkout_button().click()
        time.sleep(1)

        checkOut = CheckOut(self.driver)
        checkOut.checkout_button().click()

        purchasePage = PurchasePage(self.driver)
        purchasePage.send_country().send_keys("ind")

        self.verifyLinkPresense("India")

        purchasePage.selectCountry().click()
        purchasePage.agree().click()
        purchasePage.purchaseButton().click()

        time.sleep(1)

        textMSG = purchasePage.msgDisplayed().text
        print(textMSG)
        assert "Success" in textMSG




