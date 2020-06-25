import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage
from pageObjects.checkoutPage import CheckOutPage
from pageObjects.confirmPage import ConfirmPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):  # inheriting the  baseclass

    def test_e2e(self):

        log = self.getLogger()

        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()

        log.info("Getting all the card titles")
        cards = checkOutPage.getCardTitles()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            print(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        checkOutPage.checkOutPage1().click()
        confirmPage = checkOutPage.checkOutItems()

        log.info("Entering Country Name as ind")

        confirmPage.selectLocation().send_keys("ind")

        self.verifyLinkPresence("India")

        confirmPage.countrySelected().click()

        confirmPage.selectCheckBox().click()

        confirmPage.clickPurchaseButton().click()

        successText = confirmPage.orderSuccesConfirmText().text

        log.info("Text received from application is " + successText)
        assert "Success!" in successText  # asserting just a  substring

        self.driver.get_screenshot_as_file("screen.png")
