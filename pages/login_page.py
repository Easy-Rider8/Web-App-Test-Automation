from utils.locators import LoginPageLocators
from pages.base_page import BasePage
from utils.urlpicker import select_url as SU
from hamcrest import assert_that, contains_string, equal_to
from utils import users

"""Constructor of LoginPage class"""

class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super().__init__(driver)

    def validateUrl(self):
        assert_that(self.getUrl(),contains_string(SU()))

    def enterUsername(self, username):
        self.sendKeys(username , *self.locator.USERNAME)

    def enterPassword(self, password):
        self.sendKeys(password , *self.locator.PASSWORD)

    def clickLoginButton(self):
        self.clickElement(*self.locator.SUBMIT)

    def login(self, user):
        user = users.get_user(user)
        self.enterUsername(user["username"])
        self.enterPassword(user["password"])

    def validateInvalidCreds(self):
        assert_that(self.getElementText(*self.locator.ERROR_MESSAGE) , equal_to('*Error_Message'))