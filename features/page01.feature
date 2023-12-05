Feature: Page 01

    In order to look at the data on Page 01
    As a user
    I want to see the Charts, Datatables, Column Chart, Pie Chart
    Background:
        Given the "Page01" has been opened as "admin" role

    @smoke
    Scenario: Visibility of the Charts, Datatables, Column Chart, Pie Chart
        Then the "Chart" is loaded
        And the "DataTable" is loaded
        And the "Column Chart" is loaded
        And the "Pie Chart" is loaded
