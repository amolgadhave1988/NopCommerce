from selenium.webdriver.common.by import By


class DeleteCustomer:
    def __init__(self,driver):
        self.driver=driver

    def noofrows(self):
        return len(self.driver.find_elements(By.XPATH,"//table[@id='customers-grid']//tbody/tr"))

    def clickeditCustomer(self,emailid):
        for r in range(1,self.noofrows()+1):
            email = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if email==emailid:
                self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[7]").click()
                break

    def clickdelete(self):
        self.driver.find_element(By.XPATH,"//span[@id='customer-delete']").click()
