# https://github.com/pavanoltraining/nopCommerceProject

from  selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperty import ReadConfig
from utilities.customeLogger import LogGen


class Test_001_login:
    # base_URL = "https://admin-demo.nopcommerce.com/"
    # usernamee = "admin@yourstore.com"
    # passwordd = "admin"

    base_URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserMail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_homePageTitle(self,setup):
        self.logger.info("*****************Test_001_login******************")
        self.logger.info("**************Verify HomePage Title******************")
        self.driver = setup
        self.driver.get(self.base_URL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************Home Page title Test are Passed******************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle1.png")
            self.driver.close()
            self.logger.error("**************Home Page title Test are Fail******************")
            assert False

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("**************Verifing LogIn Test******************")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogIn()
        act_title = self.driver.title
        #self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**************LogIn Test Passed******************")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_loginPage1.png")
            self.driver.close()
            self.logger.error("**************LogIn Test Page Link Failed******************")
            assert False


