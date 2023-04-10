import pytest
from selenium import webdriver
from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import CustLogger

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.driver = setup
        logger = CustLogger.custlogger()
        logger.info("****************Test_001_Login********************")
        logger.info("****************Veryfying Home Page Title********************")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.driver.close()
            assert True
            logger.info("****************Home Page Title test is Passed********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            logger.error("****************Home Page Title test is Failed********************")
            assert False

    @pytest.mark.regression
    def test_login(self,setup):
        self.driver = setup
        logger = CustLogger.custlogger()
        logger.info("****************Veryfying Login Test********************")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
            logger.info("****************Login test is Passed********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            logger.error("****************Login test is Failed********************")
            assert False
