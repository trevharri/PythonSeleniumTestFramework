import pytest

from TestData.HomePageData import HomePageData
from pageobjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmit(self, getdata):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        home_page.getNameField().send_keys(getdata["name"])
        log.info(f'Name is {getdata["name"]}')
        home_page.getEmailField().send_keys(getdata["email"])
        log.info(f'Email is {getdata["email"]}')
        home_page.getPasswordField().send_keys(getdata["password"])
        log.info(f'Password is {getdata["password"]}')
        self.setDropdown(home_page.getDropdown(), getdata["gender"])
        log.info(f'Gender is {getdata["gender"]}')
        home_page.getRadioButton().click()
        log.info('Submitting form')
        home_page.getSubmitButton().click()
        alert_text = home_page.getAlert().text
        log.info('Asserting that "success" is in alert text')
        assert 'success' in alert_text
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePageData)
    def getdata(self, request):
        return request.param
