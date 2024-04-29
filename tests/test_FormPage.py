from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.BaseClass import BaseClass
import time

class TestFormPage(BaseClass):

    def test_FillForms(self):


        name = "Spikee"
        email_id = "gautamspikee@gmail.com"
        user_password = "Spikee06@"
        gender = "Male"
        date_of_birth = "29091996"



        # navigate to website
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        self.driver.implicitly_wait(3)

        time.sleep(2)
        # enter details in the page
        self.driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(email_id)
        self.driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys(user_password)

        # check the check box and validate
        self.driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").is_selected()

        drop_down = self.driver.find_element(By.ID, "exampleFormControlSelect1")
        select = Select(drop_down)
        select.select_by_visible_text(gender)

        self.driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").is_selected()

        self.driver.find_element(By.CSS_SELECTOR, "input[name='bday']").send_keys(date_of_birth)

        self.driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(2)

        msg = self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text
        assert msg == self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text

        time.sleep(2)
