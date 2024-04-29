from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageobjects.FormPage import FormPage
from utilities.BaseClass import BaseClass
import time

class TestFormPage(BaseClass):

    def test_FillForms(self):



        email_id = "gautamspikee@gmail.com"
        uname = "Spikee"
        user_password = "Spikee06@"
        gender = "Male"
        date_of_birth = "29091996"
        url = "https://rahulshettyacademy.com/angularpractice/"



        # navigate to website
        self.driver.get(url)
        self.driver.implicitly_wait(3)


        # enter details in the page
        formPage = FormPage(self.driver)
        formPage.getName().send_keys(uname)
        formPage.get_email().send_keys(email_id)
        formPage.get_password().send_keys(user_password)

        # check the check box and validate

        formPage.get_check().click()
        assert formPage.get_check().is_selected()

        drop_down = formPage.dd()
        select = Select(drop_down)
        select.select_by_visible_text(gender)

        formPage.radioButton().click()
        assert formPage.radioButton().is_selected()

        formPage.getDOB().send_keys(date_of_birth)

        formPage.clickSubmit().click()
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(1)

        msg = formPage.textMSG().text
        assert msg == formPage.textMSG().text

        time.sleep(1)
