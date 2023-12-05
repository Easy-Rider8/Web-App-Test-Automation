from pages.client_page import ClientPage
from utils.locators import RestrictedUserDashboardPageLocators
from hamcrest import assert_that,equal_to


"""Constructor of RestrictedUserPage class"""

class RestrictedUserPage(ClientPage):

    def __init__(self, driver):
        self.locatorRestrictedUser = RestrictedUserDashboardPageLocators
        super().__init__(driver)

    def validatePageLoaded(self):
        self.openSubMenu()
        assert_that(self.getElementText(*self.locatorRestrictedUser.DASHBOARD_TXT) , equal_to('*Dashboard_Text'))