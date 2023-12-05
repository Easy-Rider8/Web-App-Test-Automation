# Web Application Automated Testing Project

## Description

This project is an automated testing framework developed using Python with Selenium, Hamcrest, and Behave with the below features:

- Framework is based on the page object model.
- locators.py utilizes locators of the web page as a class.
- Reading test data from JSON file.
- Behave is used for behavior-driven development, Python style.
- Tests are composed under feature files with gherkin with steps 

The project is built on the Behave library, providing a scenario-based structure for the automated testing of web applications.

## Prerequisites

To run the project, the following software should be installed:

- Python 3.10.12
- Selenium
- Behave
- Hamcrest

You can install the prerequisites using the following command:
```
pip install -r requirements.txt
```
## Creating new test cases

To create a new test case, you have to follow the below steps:

- In **locators module**, create a new locator for the element you would like to use, as below:


      class DesiredLocators(object):
      
          DesiredName = (By.XPATH, '*')
          DesiredName2 = (By.XPATH, '*')
          ...

- In **test data module**, add the test data needed for your test case and you can create your own test JSON files, as below:

      {
          "testGroup":
          [
                  {
                      "testdata1": "01",
                      "testdata2": "admin",
                      ...
                  },
                  ...
          ]    
      }
- In the **pages** folder you can create new pages according to your project. You can derive new feature files from them or you can create new ones.
- In **settings module**, adapt your environments.
- Two sample feature files included. **login.py** and **page01.py** are their step definitions. You can derive new feature files from them or you can create new ones.
- One environment file under the **steps** folder. It will choose a driver which comes from the **settings module**.
- There is a **base page** which is the parent of all the page classes. It contains all the common action methods and utilities for all the pages.
- The **client page** is derived from the base page. This class is the parent of the sub-page classes. It contains all the common action methods and utilities for the sub-pages.
- The other pages are sub-pages.
- There are 3 modules under the **utils folder**;
    -   The **urlpicker module** picks a URL according to settings.py
    -   The **locators module** are locators apparently
    -   The **users module** reads users from the feature files' data tables and matches on steps according to the loop

## Run the test cases

- To run all test cases, this command reads the scenario files in the features directory and executes the tests.;
  
  `behave`
  
- To run specified test cases;
  
  `behave features/specifiedFeature`

- To run with allure;

  `behave -f allure_behave.formatter:AllureFormatter -o {allure_report_folder} {path_to_feature_file}`

- To see the report, you have to install the allure framework, check to allure framework, and execute the command;

  `allure serve {allure_report_folder}`



