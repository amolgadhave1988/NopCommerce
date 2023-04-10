import time

import pytest

from pageObject.AddCustomer import AddCustomer
from pageObject.LoginPage import LoginPage
from utilities.customLogger import CustLogger
from utilities.readProperties import ReadConfig
from pageObject.SearchCustomer import Search_Customer


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = CustLogger.custlogger()

    @pytest.mark.regression
    def test_SearchCustByEmail(self,setup):
        self.driver = setup
        self.logger.info("****************Test_004_SearchCustomerByEmail********************")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************Login Successful********************")

        self.logger.info("****************Search Customer********************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickCustomerMenu()
        self.addcust.clickCustomerItem()

        self.searchcust = Search_Customer(self.driver)
        self.searchcust.setEmail("james_pan@nopCommerce.com")
        self.searchcust.clickSearch()
        time.sleep(3)
        status = self.searchcust.searchCustomerByEmail("james_pan@nopCommerce.com")
        if status==True:
            assert True
            self.logger.info("****************Search Customer Test By Email is passed********************")
        self.driver.close()