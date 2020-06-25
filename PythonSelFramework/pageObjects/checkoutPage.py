from selenium.webdriver.common.by import By

from pageObjects.confirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements_by_css_selector(".card-title a")
    # driver.find_element_by_xpath("//button[@class='btn btn-success']")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")  # find_element_by_xpath("div/button")
    checkOut1 = (By.CSS_SELECTOR, "a[class*='btn-primary']")  # checkout button on top of page 1
    # driver.find_element_by_css_selector("a[class*='btn-primary']")
    checkOut2 = (By.XPATH, "//button[@class='btn btn-success']")  # checkout button on 2nd page

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutPage1(self):
        return self.driver.find_element(*CheckOutPage.checkOut1)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut2).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
