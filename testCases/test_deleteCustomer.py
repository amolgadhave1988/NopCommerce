import time

from selenium.webdriver.common.by import By

from utilities.readProperties import ReadConfig
from utilities.customLogger import CustLogger
from pageObject.LoginPage import LoginPage
from pageObject.AddCustomer import AddCustomer
from pageObject.DeleteCustomer import DeleteCustomer

class Test_005_DeleteCusstomer:
    baseURl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = CustLogger.custlogger()

    def test_delete_Customer(self,setup):
        self.driver = setup
        self.logger.info("*********Launching website**********")
        self.driver.get(self.baseURl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*********Login Successful**********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickCustomerMenu()
        self.addcust.clickCustomerItem()

        self.delcust = DeleteCustomer(self.driver)
        self.delcust.clickeditCustomer("james_pan@nopCommerce.com")
        time.sleep(3)
        self.delcust.clickdelete()
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Delete']").click()

        self.logger.info("****************Delete Customer Validation********************")
        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if "The customer has been deleted successfully." in self.msg:
            assert True
            self.logger.info("****************Delete Customer Test Passed********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "DeleteCustomer.png")
            self.logger.info("****************Delete Customer Test Failed********************")
        self.driver.close()