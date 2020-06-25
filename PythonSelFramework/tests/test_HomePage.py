import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):



    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)

        log.info("Name is " + getData["name"])

        #homePage.getName().send_keys(getData[0]) TUPLE DATA TYPE
        homepage.getName().send_keys(getData["name"]) #DICTIONARY DATA TYPE


        #homePage.getEmail().send_keys(getData[1]) TUPLE DATA TYPE
        log.info("Email is " + getData["email"])
        homepage.getEmail().send_keys(getData["email"]) #DICTIONARY DATA TYPE

        #self.selectOptionByText(homePage.getGender(), getData[2]) TUPLE DATA TYPE
        log.info("Gender is " + getData["gender"])
        self.selectOptionByText(homepage.getGender(), getData["gender"]) #DICTIONARY DATA TYPE
        # as dropdown code can be used in multiple tests so
        # make it generic and place the code in base class, the attributes of it are locator and text

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert "Success!" in alertText

        self.driver.refresh()   # we are using refresh here because the url belongs to class and will execute only
        # once before the class therefore concatnating the data we are sending so by doing refresh we refresh the browser
    # this fixture is not common to all test cases therefore we will not write the code in conftest file,
    # this fixture is only for this page

    #@pytest.fixture(params= HomePageData.test_HomePage_data

    # params support both tuple and dictionary data type , above is an example of tuple and we address the data through indexes
    # where as dictionary datatype is key value pair like hashmaps/hashtables in java
    #dictionary data type is declared in{}
    @pytest.fixture(params= HomePageData.getTestData("Testcase2"))    #data coming from testdata package
    def getData(self, request):
        return request.param