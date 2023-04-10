import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    def __init__(self,driver):
        self.driver=driver

    def clickCustomerMenu(self):
        self.driver.find_element(By.XPATH,"//a[@href='#']//p[contains(text(),'Customers')]").click()

    def clickCustomerItem(self):
        self.driver.find_element(By.XPATH,"//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]").click()

    def clickAddNew(self):
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Add new']").click()

    def setEmail(self,email):
        self.driver.find_element(By.NAME,"Email").send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.ID,"Password").send_keys(password)

    def setFname(self,fname):
        self.driver.find_element(By.ID,"FirstName").send_keys(fname)

    def setLname(self,lname):
        self.driver.find_element(By.ID,"LastName").send_keys(lname)

    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.ID,"Gender_Male").click()
        elif gender=="Female":
            self.driver.find_element(By.ID,"Gender_Female").click()
        else:
            self.driver.find_element(By.ID, "Gender_Female").click()

    def setDOB(self,dob):
        self.driver.find_element(By.ID,"DateOfBirth").send_keys(dob)

    def setCompName(self,compname):
        self.driver.find_element(By.NAME,"Company").send_keys(compname)

    def setCustomerRole(self,role):
        self.driver.find_element(By.XPATH,"//div[@class='input-group-append input-group-required']//div[@role='listbox']").click()
        time.sleep(3)
        if role== "Registered":
            self.listitem=self.driver.find_element(By.XPATH,"//li[contains(text(),'Registered')]")
        elif role=="Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, "//li[contains(text(),'Forum Moderators')]")
        elif role=="Vendors":
            self.listitem = self.driver.find_element(By.XPATH,"//li[contains(text(),'Vendors')]")
        elif role=="Guests":
            self.listitem = self.driver.find_element(By.XPATH, "//ul[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.driver.find_element(By.XPATH,"//li[contains(text(),'Guests')]")
        else:
            self.listitem = self.driver.find_element(By.XPATH, "//li[contains(text(),'Guests')]")
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)


    def setManagerRole(self,role):
        drp = Select(self.driver.find_element(By.XPATH,"//select[@id='VendorId']"))
        if role=="Vendor 1":
            drp.select_by_visible_text(role)
        else:
            drp.select_by_visible_text(role)

    def setAdminComment(self,comment):
        self.driver.find_element(By.XPATH,"//textarea[@id='AdminComment']").send_keys(comment)

    def clickSave(self):
        self.driver.find_element(By.XPATH,"//button[@name='save']").click()
