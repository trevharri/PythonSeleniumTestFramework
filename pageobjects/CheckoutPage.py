from selenium.webdriver.common.by import By

from pageobjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    checkout = (By.CSS_SELECTOR, '.card-title')
    goto_checkout_button = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkout_button = (By.CSS_SELECTOR, '.btn-success')

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.checkout)

    def getCardButton(self, button_path):
        button = (By.CSS_SELECTOR, button_path)
        return self.driver.find_element(*button)

    def getGoToCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.goto_checkout_button)

    def getCheckoutButton(self):
        self.driver.find_element(*CheckoutPage.checkout_button).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page

