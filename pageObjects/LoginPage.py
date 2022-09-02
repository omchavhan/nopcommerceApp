from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_logIn_xpath = "//button[normalize-space()='Log in']"
    link_text_Login = "Logout"

    def __init__(self, driver):
        # self.driver = webdriver.Chrome(executable_path="C:\\Users\\GiTESH SONAR\\PycharmProjects\\nopcommerceApp\\chromedriver.exe")
        self.driver = driver


    def setUserName(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)


    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)


    def clickLogIn(self):
        self.driver.find_element(By.XPATH,self.button_logIn_xpath).click()


    def clickLogOut(self):
        self.driver.find_element_by_link_text(By.LINK_TEXT,self.link_text_Login).click()



