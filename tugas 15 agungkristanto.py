# from dbm.ndbm import library
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

#variable
url="https://www.saucedemo.com/"
username="standard_user"
usernameblank=""
passw="secret_sauce"

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    #test case pertama
    def test_success_login(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"user-name").send_keys(username) # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys(passw) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#login-button").click()
        
        time.sleep(1)
         # validasi

        response_data = driver.find_element(By.CSS_SELECTOR,"#item_4_title_link > div").text

        self.assertIn(response_data, 'Sauce Labs Backpack')

        print(response_data)
    
    #test case kedua
    def test_blank_username_login(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"user-name").send_keys(usernameblank) # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys(passw) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#login-button").click()
        
        time.sleep(1)
         # validasi

        response_data = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3").text

        self.assertIn(response_data, 'Epic sadface: Username is required')

    
    #test case ketiga
    def test_blank_password_login(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"user-name").send_keys(username) # isi username
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("") # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#login-button").click()
        
        time.sleep(1)
         # validasi

        response_data = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3").text
        self.assertIn(response_data, 'Epic sadface: Password is required')

    #test case keempat
    def test_failed_password_login(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"user-name").send_keys(username) # isi username
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("xxxxx") # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#login-button").click()
        
        time.sleep(1)
         # validasi

        response_data = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3").text

        self.assertIn(response_data, 'Epic sadface: Username and password do not match any user in this service')

    #test case kelima
    def test_failed_username_login(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"user-name").send_keys("xdxdxd") # isi username
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys(passw) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#login-button").click()
        
        time.sleep(1)

         # validasi

        response_data = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3").text

        self.assertIn(response_data, 'Epic sadface: Username and password do not match any user in this service')

     #test case kelima
    def test_failed_username_login(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"user-name").send_keys("xdxdxd") # isi username
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys(passw) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#login-button").click()
        
        time.sleep(1)
        
         # validasi

        response_data = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3").text

        self.assertIn(response_data, 'Epic sadface: Username and password do not match any user in this service')

    #test case keenam
    def test_click_product(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"user-name").send_keys(username) # isi username
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys(passw) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#login-button").click()
        driver.find_element(By.CSS_SELECTOR,"#item_2_title_link > div").click()
        
        time.sleep(1)
        
         # validasi

        response_data = driver.find_element(By.CSS_SELECTOR,"#inventory_item_container > div > div > div.inventory_details_desc_container > div.inventory_details_name.large_size").text

        self.assertIn(response_data, 'Sauce Labs Onesie')


    #test case ketujuh
    def test_click_add_cart(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"user-name").send_keys(username) # isi username
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys(passw) # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#login-button").click()
        driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack").click()
        
        time.sleep(1)
        
         # validasi

        response_data = driver.find_element(By.CSS_SELECTOR,"#remove-sauce-labs-bike-light").text

        self.assertIn(response_data, 'Remove')
     


    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()