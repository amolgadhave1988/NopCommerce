from selenium.webdriver.common.by import By


class Search_Customer:
    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,"SearchEmail").send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element(By.ID,"SearchFirstName").send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID,"SearchLastName").send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH,"//button[@id='search-customers']").click()

    def noofrows(self):
        return len(self.driver.find_elements(By.XPATH,"//table[@id='customers-grid']//tbody/tr"))

    def noofcolumns(self):
        return len(self.driver.find_elements(By.XPATH,"//table[@id='customers-grid']//tbody/tr[1]/td"))

    def searchCustomerByEmail(self,emailid):
        flag = False
        for r in range(1,self.noofrows()+1):
            email = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if email==emailid:
                flag=True
                break
        return flag

    def searchCustomerByName(self,CustName):
        flag = False
        for r in range(1,self.noofrows()+1):
            name = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if name==CustName:
                flag=True
                break
        return flag

