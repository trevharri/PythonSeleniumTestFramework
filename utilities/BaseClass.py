import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures('setup')
class BaseClass:

    def verifyLinkPresense(self, link_txt):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, link_txt)))

    def setDropdown(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

