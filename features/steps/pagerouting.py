from behave import given
from utils.urlpicker import select_url as SU
from pages.login_page import LoginPage
from pages.a_dashboard_page import AdminPage
from pages.ru_dashboard_page import RestrictedUserPage
from pages.su_dashboard_page import StandartUserPage
from pages.page01 import Page01Page

routingInformation = {

    "Page01":[lambda context:(context.homePage.openSubSubMenuFirstItem())]

    }

@given('the "{Page}" has been opened as "{role}" role')

def validate_page_open(context,Page,role):

    try:
        context.driver.get(SU())
        context.loginPage = LoginPage(context.driver)
    except:
        assert False,"Test is failed in open login page"
    
    try:
        context.loginPage.validateUrl()
    except:
        context.driver.close()
        assert False,"Test is failed in validate login page url"

    try:
        context.loginPage.login(role)
    except:
        context.driver.close()
        assert False,"Test is failed in enter login credentials"

    try:
        context.loginPage.clickLoginButton()
    except:
        context.driver.close()
        assert False,"Test is failed in enter login"

    match role:
        case "admin":
            try:
                context.homePage = AdminPage(context.driver)
                context.homePage.validatePageLoaded()
            except:
                context.driver.close()
                assert False,"Test is failed in validating homepage"
        case "standart_user":
            try:
                context.homePage = StandartUserPage(context.driver)
                context.homePage.validatePageLoaded()
            except:
                context.driver.close()
                assert False,"Test is failed in validating homepage"
        case "restricted_user":
            try:
                context.homePage = RestrictedUserPage(context.driver)
                context.homePage.validatePageLoaded()
            except:
                context.driver.close()
                assert False,"Test is failed in validating homepage"

    try:
        context.homePage.openSubSubMenu()
        for element in routingInformation[Page]:
            element(context)
    except:
        context.driver.close()
        assert False,"Test is failed in validating " + Page + " Page"

    match Page:
        case "Page01":
            try:
                context.customPage = Page01Page(context.driver)
            except:
                context.driver.close()
                assert False,"Test is failed in validating Page01"

    context.customPage.validatePageisTrue() 