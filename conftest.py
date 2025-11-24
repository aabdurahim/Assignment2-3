import os
import pytest
from selenium import webdriver

BROWSERS = [
    ("chrome", "latest", "Windows", "11"),
    ("firefox", "latest", "Windows", "11"),
    ("safari", "16.0", "OS X", "Ventura"),
]

def make_options(browser_name, browser_version, os_name, os_version, session_name):
    bstack_options = {
        "os": os_name,
        "osVersion": os_version,
        "sessionName": session_name,
        "buildName": "Homework Build",
        "projectName": "BrowserStack Homework"
    }

    name = browser_name.lower()
    if name == "chrome":
        options = webdriver.ChromeOptions()
    elif name == "firefox":
        options = webdriver.FirefoxOptions()
    elif name == "safari":
        options = webdriver.SafariOptions()
    else:
        options = webdriver.ChromeOptions()

    options.set_capability("browserName", browser_name)
    options.set_capability("browserVersion", browser_version)
    options.set_capability("bstack:options", bstack_options)

    return options

@pytest.fixture(params=BROWSERS, ids=lambda x: f"{x[0]}-{x[2]}{x[3]}")
def driver(request):
    username = os.environ.get("BROWSERSTACK_USERNAME")
    access_key = os.environ.get("BROWSERSTACK_ACCESS_KEY")
    if not username or not access_key:
        raise Exception("Set BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY in environment.")

    browser_name, browser_version, os_name, os_version = request.param
    session_name = request.node.name

    options = make_options(browser_name, browser_version, os_name, os_version, session_name)

    url = f"https://{username}:{access_key}@hub.browserstack.com/wd/hub"

    driver = webdriver.Remote(command_executor=url, options=options)
    yield driver
    try:
        driver.quit()
    except Exception:
        pass