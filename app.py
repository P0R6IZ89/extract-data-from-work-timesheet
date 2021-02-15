import os
# not final choice
import time
import signal

from flask import Flask

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Initialize Flask
app = Flask(__name__)

# Initialize Seleniun
is_loged_in = False
user_id = '01243111'
user_password ='04180418'

user_id_field = 'uid'
user_password_field = 'pwd'

tabs_list = ['', 'information', 'calender', 'summary']
time_line_alert_types = ['Shift fixed', 'Post notification', 'Shift adjustment', 'Shift draft']
base_url = 'https://wps.fastretailing.com/'

time_line_xpath = '/html/body/div[2]/div[1]/div[1]/div/section/ng-include[2]'

webdriver_path = '/usr/bin/geckodriver'

options = Options()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument('--disable-gpu')
driver = webdriver.Firefox(executable_path=webdriver_path, options=options)

class Login(object):
    def __init__(self):
        print('Login init')
        pass
        
    def login (self):
        print('loging in')
        # id_elem = driver.find_element_by_id(user_id_field)
        id_elem = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.ID, user_id_field)
                )
            )
        id_elem.send_keys(user_id)
        pwd_elem = driver.find_element_by_id(user_password_field)
        pwd_elem.send_keys(user_password)
        pwd_elem.send_keys(Keys.RETURN)
        self.is_loged_in = True
        print('loged in')

class Scrapper(object):
    def __init__(self):
        pass
    
    def scrapp(self, tabs_list):
        for tab in tabs_list:

            driver.get(os.path.join(base_url, tab))

            if not tab:
                
                Login.login(self)
                time_line_elem = WebDriverWait(driver, 10).until(
                    expected_conditions.presence_of_element_located(
                        (By.XPATH, time_line_xpath)
                    )
                )

                print(is_loged_in)
                print(time_line_elem.text)
                time.sleep(10)

            if tab == 'information':
                time.sleep(2)
                pass

            if tab == 'calender':
                time.sleep(2)
                pass

            if tab == 'summary':
                time.sleep(2)
                pass

            # driver.get(os.path.join(base_url, tab))
            # time.sleep(5)
        driver.close()
            
# Draft
x = Scrapper()
x.scrapp(tabs_list)

def keyboardInterruptHandler(signal, frame):
    print('Exiting Driver')
    driver.close()
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)


# @app.route('/')
# def hello():
#     return 'Hello, its working'

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000)