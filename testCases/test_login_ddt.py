import time

import pytest
from selenium import webdriver
from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import CustLogger
from utilities import XLUtils

class Test_002_Login_DDT:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    path = ".\\TestData\\LoginData.xlsx"

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.driver = setup
        logger = CustLogger.custlogger()
        logger.info("****************Test_002_Login_DDT********************")
        logger.info("****************Veryfying Login ddt Test********************")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in an Excel:", self.rows)

        lst_status = []
        for r in range(2,self.rows+1):
            self.username = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    logger.info("********Passed********")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    logger.info("********Failed********")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    logger.info("********Failed********")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    logger.info("********Passed********")
                    lst_status.append("Pass")

        if "Fail" in lst_status:
            logger.info("****************Login ddt Test Case Failed********************")
            self.driver.close()
            assert False
        else:
            logger.info("****************Login ddt Test Case Passed********************")
            self.driver.close()
            assert True