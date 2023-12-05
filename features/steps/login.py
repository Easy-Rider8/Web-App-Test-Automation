from behave import given,when,then
from utils.urlpicker import select_url as SU
from pages.login_page import LoginPage
from pages.a_dashboard_page import AdminPage
from pages.ru_dashboard_page import RestrictedUserPage
from pages.su_dashboard_page import StandartUserPage


@when('open the website')

def open_login_page(context):
    try:
        context.driver.get(SU())
        context.loginPage = LoginPage(context.driver)
    except:
        assert False,"Test is failed in open login page"


@then('the login page has been opened')

def validate_login_page(context):
    try:
        context.loginPage.validateUrl()
    except:
        context.driver.close()
        assert False,"Test is failed in validate login page url"


@given('enter the username and the password according to role is "{role}"')

def enter_login_creds(context,role):
    try:
        context.loginPage.login(role)
        context.role=role
    except:
        context.driver.close()
        assert False,"Test is failed in enter login credentials"


@when('click on the Sign In button')

def click_signin_button(context):
    try:
        context.loginPage.clickLoginButton()
    except:
        context.driver.close()
        assert False,"Test is failed in enter login"


@then('login is successful and dashboard is opened')

def validate_dashboard_page(context):
    match context.role:
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
    

@then('login is failed and invalid credential error message is displayed')

def validate_invalid_login(context):
    try:
        context.loginPage.validateInvalidCreds()
    except:
        context.driver.close()
        assert False,"Test is failed in validating invalid login"
