from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException, TimeoutException, NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, InvalidSelectorException as EX
from utils.urlpicker import select_url as SU


"""This class is the parent of all the page classes"""
"""It contains all the common action methods and utilities for all the pages"""

class BasePage(object):

    def __init__(self, driver, base_url=SU()):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def findElement(self, *locator):
        return self.driver.find_element(*locator)

    def clickElement(self, *locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            element.click()
        except EX as e:
            print("Exception! Can't click on the element")
            return False

    def inputElement(self, *locator, text):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            element.send_keys(text)
        except EX as e:
            print("Exception! Can't input to the element")
            return False

    def getElementText(self, *locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element.text
        except EX as e:
            print("Exception! Can't get text from the element")
            return False
                 
    def getElementAttribute(self, *locator, attribute_name):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element.get_attribute(attribute_name)
        except EX as e:
            print("Exception! Can't get attribute from the element")
            return False
        
    def getTitle(self):
        return self.driver.title

    def getUrl(self):
        return self.driver.current_url

    def hover(self, *locator):
        try:
            element = self.findElement(*locator)
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
        except:
            print("Exception! Can't hover on the element")
            return False

    def verifyElementDisplayed(self, *locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except EX as e:
            print("Exception! Can't display the element")
            return False

    def sendKeys(self, item, *locator):
        self.findElement(*locator).send_keys(item)

    def searchItemResultCheck(self, *locator, item):
        self.findElement(*locator).send_keys(item)
        self.findElement(*locator).send_keys(Keys.ENTER)
        return self.findElement(locator).text
