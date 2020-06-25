import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
# 'pass' is a keyword in python that tells that we are not doing any operation

@pytest.mark.usefixtures("setup")  # connecting the browser setup from conftest file to this file
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]  #name of which file the loggeer is called other wise it will  print the base class name
        logger = logging.getLogger(loggerName)
        #logger = logging.getLogger(__name__)

        filehandler = logging.FileHandler('logfile.log')  # it is the file location,come from parent logging not object, give file name where logs will be printed

        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s : %(message)s")

        filehandler.setFormatter(formatter)  # pass info of formatter to filehandler

        # now all the info of formatting is in file handler and then to logger
        logger.addHandler(filehandler)  # filehandler object, logger is asking in which file i have to print the logs, what is the format?

        logger.setLevel(logging.DEBUG)

        return logger

    def verifyLinkPresence(self,text):
        element = WebDriverWait(self.driver, 10)
        element.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self,locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

