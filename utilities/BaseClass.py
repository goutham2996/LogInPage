import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    country_visible = (By.XPATH, "//a[normalize-space()='India']")

    def verifyLinkPresense(self, text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            expected_conditions.visibility_of_element_located((By.LINK_TEXT, text)))
        return element

