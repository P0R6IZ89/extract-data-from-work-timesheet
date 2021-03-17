import os
import signal

import datetime
from calendar import monthrange

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from secrets import *

current_time = datetime.datetime.now()

user_id = USER_ID # Your user id to login
user_password = USER_PASSWORD # Your password

user_id_field = 'uid' 
user_password_field = 'pwd' 

base_url = BASE_URL
urls_suffix_list = URLS_SUFFIX_LIST

wait_00 = WAIT_00
wait_01 = WAIT_01
wait_02 = WAIT_02
xpath_00 = XPATH_00
xpath_01 = XPATH_01
xpath_02 = XPATH_02

webdriver_path = '/usr/bin/geckodriver' 

options = Options()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument('--disable-gpu')
driver = webdriver.Firefox(executable_path=webdriver_path, options=options)
wait = WebDriverWait(driver, 10)


        
class WebScrapper(object):
    def __init__(self):
        driver.get(os.path.join(base_url, 'login'))
        id_elem = wait.until(
            expected_conditions.presence_of_element_located(
                (By.ID, user_id_field)
                )
            )
        id_elem.send_keys(user_id)
        pwd_elem = driver.find_element_by_id(user_password_field)
        pwd_elem.send_keys(user_password)
        pwd_elem.send_keys(Keys.RETURN)

    
    def scrap(self):
        days_list = []
        for tab in urls_suffix_list:
            print(tab)
            wait.until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, wait_00)
            ))
            driver.get(os.path.join(base_url, tab))
            if not tab: # timeline
                time_line_elem = wait.until(
                    expected_conditions.visibility_of_element_located(
                        (By.XPATH, wait_01)
                    )
                )

            elif tab == urls_suffix_list[1]:
                for post in range(1, 4): # Extract last 4 information posts
                    information_elem = wait.until(
                        expected_conditions.presence_of_element_located(
                            (By.XPATH, XPATH_00.format(post))
                        )
                    )

            elif tab == urls_suffix_list[2]:
                wait.until(expected_conditions.presence_of_element_located((By.XPATH, wait_02)))
                for week in range(1, 6):
                    for work_day in range(1, 8):
                        for index in range(1, 5):
                            try:
                                each_day = driver.find_element_by_xpath(xpath_01.format(week, work_day, index))
                                if each_day.text: # If there are data append to list
                                    days_list.append(each_day.text)
                                    break
                            except:
                                pass

                if current_time.day > monthrange(current_time.year, current_time.month)[1]: # If is last day of month, change to next page
                    next_month = wait.until(
                        expected_conditions.presence_of_element_located(
                            (By.XPATH, xpath_02))).click() 
                    wait.until(expected_conditions.presence_of_element_located((By.XPATH, wait_02)))
                    def extract_next_month():
                        for week in range(1, 6):
                            for work_day in range(1, 8):
                                for index in range(1, 5):
                                    try:
                                        next_month_first_day = driver.find_element_by_xpath(xpath_01.format(week, work_day, index))
                                        if next_month_first_day.text:
                                            clean_next_month_first_day = next_month_first_day.text
                                            return clean_next_month_first_day
                                    except:
                                        pass
                else:
                    pass
                    days_list.clear()
        driver.close()

x = WebScrapper()
x.scrap()
