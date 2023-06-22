from pageobjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        product = "Blackberry"
        log = self.getLogger()
        home_page = HomePage(self.driver)

        checkout_page = home_page.shopItems()
        log.info("Getting all card titles")
        products = checkout_page.getCardTitles()
        products_text_list = [product.text for product in products]
        if product in products_text_list:
            index = products_text_list.index(product)
            log.info("Matching product found: {}".format(product))
            button_css_path = f"div.col-lg-9 app-card:nth-child({index + 1}) button"
        checkout_page.getCardButton(button_css_path).click()
        # print(self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").text)
        checkout_page.getGoToCheckoutButton().click()
        confirm_page = checkout_page.getCheckoutButton()

        confirm_page.getCountryInput().send_keys('Spain')
        log.info("Entering country name: Spain")
        self.verifyLinkPresense('Spain')
        confirm_page.getCountryOption().click()
        confirm_page.getPurchaseButton().click()
        assert 'success' in confirm_page.getSuccessMessage().text.lower()
