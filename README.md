# web-ui-automation
This repository is for learning purposes only. Based on the courses from TAU, I've been learning techniques involving python selenium for web ui automation testing. Following the design of the page, object, model pattern and using behavior-driven-development for creating test scenarios. 

# Local Installation

## Python Setup
You will need Python 3.8 or higher.
You can download the latest Python version from [Python.org](https://www.python.org/downloads/).

As well as pipenv [pipenv](https://docs.pipenv.org/).
To install pipenv, run `pip install pipenv` from the command line.

Once you have locally cloned the repository, go into the command line(into the repository) and run `pipenv install`, this will install everything you need from the Pipfile.

## Webdrivers
Currently I've only been running tests from the Edge(Chromium browser). 
Download the latest version of Edge(Chromium) from [Microsoft](https://www.microsoft.com/en-us/edge)
Download the webdriver for the current version of Edge(Chromium not the legacy Edge)
[EdgeWebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

### WebDriver Setup for Windows

To install EdgeWebDriver on Windows:

1. Create a folder named `C:\Selenium`.
2. Move the executables into this folder.
3. Add this folder to the *Path* environment variable. (See [How to Add to Windows PATH Environment Variable](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/).)

## Run the Tests
On the command line, run `python -m pytest`
If you want to run tests in parallel, run `python -m pytest -n {# of threads you want to run}`