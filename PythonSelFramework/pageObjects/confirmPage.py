from selenium.webdriver.common.by import By


# driver.find_element_by_link_text("India")
# driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']")
# driver.find_element_by_css_selector("[type='submit']")
# driver.find_element_by_class_name("alert-success")

class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    location = (By.ID, "country")
    country = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "[type='submit']")
    successText = (By.CLASS_NAME, "alert-success")

    def selectLocation(self):
        return self.driver.find_element(*ConfirmPage.location)

    def countrySelected(self):
        return self.driver.find_element(*ConfirmPage.country)

    def selectCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def clickPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def orderSuccesConfirmText(self):
        return self.driver.find_element(*ConfirmPage.successText)
