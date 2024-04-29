from selenium.webdriver.common.by import By


class FormPage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys(name)
    name = (By.XPATH, "(//input[@name='name'])[1]")
    def getName(self):
        return self.driver.find_element(*FormPage.name)


    #self.driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(email_id)
    email = (By.CSS_SELECTOR, "input[name='email']")

    def get_email(self):
        return self.driver.find_element(*FormPage.email)

    #self.driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").
    password = (By.CSS_SELECTOR, "#exampleInputPassword1")
    def get_password(self):
        return self.driver.find_element(*FormPage.password)

    #self.driver.find_element(By.CSS_SELECTOR, "#exampleCheck1")
    checkBox = (By.CSS_SELECTOR, "#exampleCheck1")
    def get_check(self):
        return self.driver.find_element(*FormPage.checkBox)

    #self.driver.find_element(By.ID, "exampleFormControlSelect1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    def dd(self):
        return self.driver.find_element(*FormPage.dropdown)

    #self.driver.find_element(By.CSS_SELECTOR, "#inlineRadio2")
    radio = (By.CSS_SELECTOR, "#inlineRadio2")
    def radioButton(self):
        return self.driver.find_element(*FormPage.radio)

    #self.driver.find_element(By.CSS_SELECTOR, "input[name='bday']")
    dob = (By.CSS_SELECTOR, "input[name='bday']")
    def getDOB(self):
        return self.driver.find_element(*FormPage.dob)

    #self.driver.find_element(By.CSS_SELECTOR, "input[value='Submit']")
    submitButton = (By.CSS_SELECTOR, "input[value='Submit']")
    def clickSubmit(self):
        return self.driver.find_element(*FormPage.submitButton)

    #self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
    text_msg = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
    def textMSG(self):
        return self.driver.find_element(*FormPage.text_msg)