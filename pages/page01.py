from pages.client_page import ClientPage
from utils.locators import Page01PageLocators
from hamcrest import assert_that,equal_to


"""Constructor of Page01Page class"""

class Page01Page(ClientPage):

    def __init__(self, driver):
        self.locatorPage01 = Page01PageLocators
        super().__init__(driver)

    pagegraph = {
        "Chart": "CHART",
        "DataTable": "DATATABLE",
        "Column Chart": "COLUMN_CHART",
        "Pie Chart": "PIE_CHART"
        }

    def validatePageisTrue(self):
        element_txt = self.getElementText(*self.locator.SUB_SUB_MENU_MAIN_TITLE)
        assert_that(element_txt, equal_to('*Sub_Sub_Menu_Text'))

    def validateGraphLoad(self,graph):
        attributes = vars(self.locatorPage01)
        given_attribute = self.pagegraph[graph]
        for attribute, value in attributes.items():
            if attribute == given_attribute:
                self.verifyElementDisplayed(*value)
                break


