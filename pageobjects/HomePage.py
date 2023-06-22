from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageobjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")

    name_locator = (By.CSS_SELECTOR, "input[name='name']")
    email_locator = (By.CSS_SELECTOR, "input[name='email']")
    password_locator = (By.CSS_SELECTOR, "input[type='password']")
    radio_locator = (By.CSS_SELECTOR, "#inlineRadio1")
    submit_locator = (By.CSS_SELECTOR, ".btn")
    alert_locator = (By.CSS_SELECTOR, ".alert")
    dropdown_locator = (By.CSS_SELECTOR, '#exampleFormControlSelect1')

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page

    def getNameField(self):
        return self.driver.find_element(*HomePage.name_locator)

    def getEmailField(self):
        return self.driver.find_element(*HomePage.email_locator)

    def getPasswordField(self):
        return self.driver.find_element(*HomePage.password_locator)

    def getRadioButton(self):
        return self.driver.find_element(*HomePage.radio_locator)

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submit_locator)

    def getAlert(self):
        return self.driver.find_element(*HomePage.alert_locator)

    def getDropdown(self):
        return self.driver.find_element(*HomePage.dropdown_locator)


