import pytest

from TestData.HomePageData import HomePageData
from pageobjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmit(self, getdata):
        home_page = HomePage(self.driver)
        home_page.getNameField().send_keys(getdata["name"])
        home_page.getEmailField().send_keys(getdata["email"])
        home_page.getPasswordField().send_keys(getdata["password"])
        self.setDropdown(home_page.getDropdown(), getdata["gender"])
        home_page.getRadioButton().click()
        home_page.getSubmitButton().click()
        alert_text = home_page.getAlert().text
        assert 'success' in alert_text
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePageData)
    def getdata(self, request):
        return request.param
