# https://github.com/pavanoltraining/nopCommerceProject
import time

from  selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperty import ReadConfig
from utilities.customeLogger import LogGen
from  utilities import XLUnits


class Test_002_DDT_login:
    # base_URL = "https://admin-demo.nopcommerce.com/"
    # usernamee = "admin@yourstore.com"
    # passwordd = "admin"

    base_URL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login_ddt(self,setup):
        self.logger.info("*************Test_002_DDT_login*******************")
        self.logger.info("**************Verifing LogIn DDT Test******************")
        self.driver = setup
        self.driver.get(self.base_URL)

        self.lp = LoginPage(self.driver)

        self.rows = XLUnits.getRowCount(self.path,'Sheet1')
        print("Numbers of Rows i a Excel:",self.rows)

        lst_status = []    # Empty List Variable

        for r in range(2,self.rows+1):
            self.user = XLUnits.readData(self.path, "Sheet1", r, 1)
            self.password1 = XLUnits.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUnits.readData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password1)
            self.lp.clickLogIn()
            # time.sleep(2)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                   self.logger.info("*****Passed*******")
                   self.lp.clickLogIn()
                   lst_status.append("Pass")
                elif self.exp == "Fail":
                     self.logger.info("*****Failed********")
                     self.lp.clickLogIn()
                     lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****Failed******")
                    self.lp.clickLogIn()
                    lst_status.append("Pass")
                elif self.exp != "Fail":
                    self.logger.info("*****Passed*********")
                    self.lp.clickLogIn()
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("*************Login DDT Test Pass*************")
            self.driver.close()
            assert True

        else:
            self.logger.info("*************Login DDT Test Failed*************")
            self.driver.close()
            assert False

        self.logger.info("*************End of Login DDT Test*******************")
        self.logger.info("**************Completed TC_LoginDDT__002******************")














