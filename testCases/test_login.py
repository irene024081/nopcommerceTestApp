import pytest
from selenium import webdriver
from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator

class Test_001_Login:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGenerator.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("***** Test_001_Login *****")
        self.logger.info("***** Verifying Home Page Title *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        self.driver.close()
        if actual_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("***** Verified Home Page Title Passed*****")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png" )
            self.driver.close()
            self.logger.error("***** Verified Home Page Title Failed*****")
            assert False

    def test_login(self,setup):
        self.logger.info("***** Verifying Login *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login_page = LoginPage(self.driver)
        self.login_page.setUserName(self.username)
        self.login_page.setPassword(self.password)
        self.login_page.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png" )
            self.driver.close()
            self.logger.info("***** Verified Login Passed*****")
            assert True
        else:
            self.driver.close()
            self.logger.error("***** Verified Login Failed*****")
            assert False


