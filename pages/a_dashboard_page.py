from pages.client_page import ClientPage
from utils.locators import AdminDashboardPageLocators
from hamcrest import assert_that,equal_to


"""Constructor of AdminPage class"""

class AdminPage(ClientPage):

    def __init__(self, driver):
        self.locatorAdmin = AdminDashboardPageLocators

        super().__init__(driver)

    def validatePageLoaded(self):
        self.openSubMenu()
        assert_that(self.getElementText(*self.locatorAdmin.DASHBOARD_TXT) , equal_to('*Dashboard_Text'))