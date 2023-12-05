from pages.client_page import ClientPage
from utils.locators import StandartUserDashboardPageLocators
from hamcrest import assert_that,equal_to


"""Constructor of StandartUserPage class"""

class StandartUserPage(ClientPage):

    def __init__(self, driver):
        self.locatorStandartUser = StandartUserDashboardPageLocators
        super().__init__(driver)

    def validatePageLoaded(self):
        self.openSubMenu()
        assert_that(self.getElementText(*self.locatorStandartUser.DASHBOARD_TXT) , equal_to('*Dashboard_Text'))