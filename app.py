import os
# not final choice
import signal
import time

import datetime
from calendar import monthrange

from flask import Flask

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Initialize Flask
app = Flask(__name__)

current_time = datetime.datetime.now()

# Initialize Seleniun
user_id = '01243111'
user_password ='04180418'

user_id_field = 'uid'
user_password_field = 'pwd'

tabs_list = ['', 'information', 'calendar', 'summary']
time_line_alert_types = ['Shift fixed', 'Post notification', 'Shift adjustment', 'Shift draft']
base_url = 'https://wps.fastretailing.com/'

time_line_xpath = '/html/body/div[2]/div[1]/div[1]/div/section/ng-include[2]'
information_class = 'information'

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
        days_list = []
        for tab in tabs_list:

            driver.get(os.path.join(base_url, tab))

            if not tab:
                Login.login(self)
                print('*****Timeline*****')
                time_line_elem = WebDriverWait(driver, 10).until(
                    expected_conditions.presence_of_element_located(
                        (By.XPATH, time_line_xpath)
                    )
                )
                # print(time_line_elem.text)

            elif tab == 'information':
                print('*****Information*****')
                for post in range(1, 4):
                    information_elem = WebDriverWait(driver, 10).until(
                        expected_conditions.presence_of_element_located(
                            (By.XPATH, '/html/body/div[2]/div[1]/div/div/section/section/div/div[{0}]'.format(post))
                        )
                    )
                    # print(information_elem.text)

            elif tab == 'calendar':
                print('*****Calendar*****')
                # print(monthrange(current_time.year, current_time.month))
                # Search for an element to check whether loaded
                load_page = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div/section/div/section/ng-include[1]/table/tbody')))
                if load_page:
                    for week in range(1, 6):
                        for work_day in range(1, 8):
                            for index in range(1, 5):
                                try:
                                    # print('week', week, 'day', work_day, 'index', index)
                                    each_day = driver.find_element_by_xpath(
                                        '/html/body/div[2]/div[1]/div/div/section/div/section/ng-include[1]/table/tbody/tr[{0}]/td[{1}]/a/div/div[{2}]/div'
                                        .format(week, work_day, index))
                                    if each_day.text:
                                        days_list.append(each_day.text)
                                except:
                                    pass
                    
                    print(days_list)
                    print('TODAY IS')
                    print(days_list[current_time.day - 1])
                    print('Tomorrow is')
                    # CHANGE HERE !!!!!!!!!!!!!!
                    if 29 > monthrange(current_time.year, current_time.month)[1]:
                        print('if tomorrow is more than lastday of calendar')
                        print(days_list[current_time.day])
                    else:
                        pass
                        
                    days_list.clear()


            elif tab == 'summary':
                print('*****Summary*****')

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