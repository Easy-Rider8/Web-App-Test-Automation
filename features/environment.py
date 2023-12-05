from selenium import webdriver
from config.settings import Configuration


def before_scenario(context, scenario):

    match Configuration.BROWSER:
        case "chrome":
            context.driver = webdriver.Chrome()
        case "firefox":
            context.driver = webdriver.Firefox()
        case 'safari':
            context.driver = webdriver.Safari()
        case 'ie':
            context.driver = webdriver.Ie()
        case 'edge':
            context.driver = webdriver.Edge()
        case _:
            raise ValueError("Browser you entered '"+ Configuration.BROWSER + "' is invalid option")

    context.driver.maximize_window()

def after_scenario(context, scenario):

    context.driver.close()