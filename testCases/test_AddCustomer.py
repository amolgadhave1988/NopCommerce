import random
import string
import time

import pytest
from selenium.webdriver.common.by import By

from utilities.customLogger import CustLogger
from utilities.readProperties import ReadConfig
from pageObject.LoginPage import LoginPage
from pageObject.AddCustomer import AddCustomer

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = CustLogger.custlogger()

    @pytest.mark.sanity
    def test_AddCustomer(self,setup):
        self.driver = setup
        self.logger.info("****************Test_003_AddCustomer********************")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************Login Successful********************")

        self.logger.info("****************Add Customer Info********************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickCustomerMenu()
        self.addcust.clickCustomerItem()
        self.addcust.clickAddNew()
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("abc123")
        self.addcust.setFname("Amol")
        self.addcust.setLname("Gadhave")
        self.addcust.setGender("Male")
        self.addcust.setDOB("02/12/1988")
        self.addcust.setCompName("XYZ")
        self.addcust.setCustomerRole("Forum Moderators")
        self.addcust.setManagerRole("Vendor 2")
        self.addcust.setAdminComment("This is for Testing........")
        time.sleep(3)
        self.addcust.clickSave()
        self.logger.info("****************Saving Customer Info********************")

        self.logger.info("****************Add Customer Validation********************")
        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)

        if "customer has been added successfully." in self.msg:
            assert True
            self.logger.info("****************Add Customer Test Passed********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "AddCustomer.png")
            self.logger.info("****************Add Customer Test Failed********************")

        self.driver.close()
        self.logger.info("****************Add Customer Test Completed********************")


def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range (size))