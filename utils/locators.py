from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class LoginPageLocators(object):

    USERNAME = (By.XPATH, '*')
    PASSWORD = (By.XPATH, '*')
    SUBMIT = (By.XPATH, '*')
    ERROR_MESSAGE = (By.XPATH, '*')

class ClientPageLocators(object):

    SUB_SUB_MENU_MAIN_TITLE = (By.XPATH, '*')
    SUB_MENU = (By.XPATH, '*')
    DASHBOARD = (By.XPATH, '*')
    SUB_SUB_MENU = (By.XPATH, '*')
    SUB_SUB_MENU_FIRST_ITEM = (By.XPATH, '*')

class Page01PageLocators(object):

    # Charts, Tables, Graphs, Datatables

    CHART = (By.XPATH, '*')
    DATATABLE = (By.XPATH, '*')
    COLUMN_CHART = (By.XPATH, '*')
    PIE_CHART = (By.XPATH, '*')

class AdminDashboardPageLocators(object):

    DASHBOARD_TXT = (By.XPATH, '*')

class StandartUserDashboardPageLocators(object):

    DASHBOARD_TXT = (By.XPATH, '*')

class RestrictedUserDashboardPageLocators(object):

    DASHBOARD_TXT = (By.XPATH, '*')
