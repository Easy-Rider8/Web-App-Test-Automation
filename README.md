# Web Application Automated Testing Project

This project is an automated testing project developed using Python with Selenium, Hamcrest, and Behave. 
The project is built on the Behave library, providing a scenario-based structure for the automated testing of web applications.

## Getting Started

These steps include the dependencies and procedures necessary to run the project on your local machine.

## Prerequisites

To run the project, the following software should be installed:

- Python 3.10.12
- Selenium
- Behave
- Hamcrest

You can install the prerequisites using the following command:
```
pip install selenium behave hamcrest
```
## Configuration

Download and install the Selenium WebDriver: Selenium WebDriver

In the project directory, create a configuration file named config.ini and configure the required settings:
```
[WebDriver]
driver_path = /path/to/your/driver
```
Create scenario files for Behave under the features directory.
## Usage

You can run the tests by using the following command in the project directory:
```
behave
```
This command reads the scenario files in the features directory and executes the tests.

## Contributing

Fork this repository.

Create a new branch (git checkout -b feature/somefeature).

Commit your changes (git commit -am 'Add some feature').

Push your branch (git push origin feature/feature).

Open a pull request.

