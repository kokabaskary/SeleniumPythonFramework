import pytest
from selenium import webdriver
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)


@pytest.fixture(scope="class")  # as this will execute once before the test therefore setting scope as class
def setup(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    elif browser_name == "IE":
        print("IE driver")

    driver.get('https://rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()

    request.cls.driver = driver #this driver on right belongs to the local driver defined above, while
                                # the driver on the left .driver is the class driver for other pages
    yield
    driver.close()
