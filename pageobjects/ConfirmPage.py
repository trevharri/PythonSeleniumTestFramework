from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country_input = (By.ID, 'country')
    country_option = (By.LINK_TEXT, 'Spain')
    purchase_button = (By.CSS_SELECTOR, '.btn-success')
    success_message = (By.CSS_SELECTOR, 'div.alert-success')

    def getCountryInput(self):
        return self.driver.find_element(*ConfirmPage.country_input)

    def getCountryOption(self):
        return self.driver.find_element(*ConfirmPage.country_option)

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

    def getSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.success_message)



