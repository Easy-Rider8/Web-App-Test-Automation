Feature: Validate the login feature

    In order to look at the data 
    As a user
    I want to login to the Website

    Background:
        When open the website
        Then the login page has been opened
  
    Scenario Outline: Login with valid credentials
        Given enter the username and the password according to role is "<role>"
        When click on the Sign In button
        Then login is successful and dashboard is opened

    Examples: 
        |role             |
        |admin            |
        |standart_user    |
        |restricted_user  |

    Scenario Outline: Login with invalid credentials
        Given enter the username and the password according to role is "<role>"
        When click on the Sign In button
        Then login is failed and invalid credential error message is displayed

    Examples: 
        |role             |
        |invalid_user     |
        |invalid_password |
        |empty_username   |
        |empty_password   |