from pages.base_page import BasePage
from utils.locators import ClientPageLocators


"""Constructor of ClientPage class"""
"""This class is the parent of the sub page classes"""
"""It contains all the common action methods and utilities for the sub pages"""

class ClientPage(BasePage):

    def __init__(self, driver):
        self.locator = ClientPageLocators
        super().__init__(driver)

    def openSubMenu(self):
        self.clickElement(*self.locator.SUB_MENU)

    def openSubSubMenu(self):
        self.clickElement(*self.locator.SUB_SUB_MENU)

    def openSubSubMenuFirstItem(self):
        self.clickElement(*self.locator.SUB_SUB_MENU_FIRST_ITEM)


