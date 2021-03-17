import os
# not final choice
import signal
import time

import datetime
from calendar import monthrange

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from secrets import USER_ID, USER_PASSWORD, BASE_URL, TAB_LIST, TIMELINE_ALERT_TYPE, TIMELINE_XPATH

current_time = datetime.datetime.now()

user_id = USER_ID
user_password = USER_PASSWORD

user_id_field = 'uid'
user_password_field = 'pwd'

tabs_list = TAB_LIST
timeline_alert_types = TIMELINE_ALERT_TYPE
base_url = BASE_URL

timeline_xpath = TIMELINE_XPATH

webdriver_path = '/usr/bin/geckodriver'

options = Options()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument('--disable-gpu')
driver = webdriver.Firefox(executable_path=webdriver_path, options=options)
wait = WebDriverWait(driver, 10)


        
class WebScrapper(object):
    def __init__(self):
        print("init DONE")
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
        print("scrap DONE")
        data = 'data'
        days_list = []
        for tab in tabs_list:
            print(tab)
            wait.until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, 'html.ng-scope body.pace-done')
            ))
            print('loaded', tab)
            driver.get(os.path.join(base_url, tab))
            if not tab:
                time_line_elem = wait.until(
                    expected_conditions.visibility_of_element_located(
                        (By.XPATH, timeline_xpath)
                    )
                )

            elif tab == 'information':
                for post in range(1, 4):
                    information_elem = wait.until(
                        expected_conditions.presence_of_element_located(
                            (By.XPATH, '/html/body/div[2]/div[1]/div/div/section/section/div/div[{0}]'.format(post))
                        )
                    )

            elif tab == 'calendar':
                load_page = wait.until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div/section/div/section/ng-include[1]/table/tbody')))
                if load_page:
                    for week in range(1, 6):
                        for work_day in range(1, 8):
                            for index in range(1, 5):
                                try:
                                    each_day = driver.find_element_by_xpath(
                                        '/html/body/div[2]/div[1]/div/div/section/div/section/ng-include[1]/table/tbody/tr[{0}]/td[{1}]/a/div/div[{2}]/div'
                                        .format(week, work_day, index))
                                    if each_day.text:
                                        days_list.append(each_day.text)
                                        break
                                except:
                                    pass

                if current_time.day > monthrange(current_time.year, current_time.month)[1]:
                    next_month = wait.until(
                        expected_conditions.presence_of_element_located(
                            (By.XPATH, '/html/body/div[2]/div[1]/div/div/section/div/ng-include/header/div/ul/li[5]/a/ng-include/div'))).click()
                    load_page = wait.until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div/section/div/section/ng-include[1]/table/tbody')))
                    time.sleep(5)
                    def extract_next_month():
                        for week in range(1, 6):
                            for work_day in range(1, 8):
                                for index in range(1, 5):
                                    try:
                                        next_month_first_day = driver.find_element_by_xpath(
                                            '/html/body/div[2]/div[1]/div/div/section/div/section/ng-include[1]/table/tbody/tr[{0}]/td[{1}]/a/div/div[{2}]/div'
                                            .format(week, work_day, index))
                                        if next_month_first_day.text:
                                            clean_next_month_first_day = next_month_first_day.text
                                            return clean_next_month_first_day
                                    except:
                                        pass
                        
                    print(extract_next_month())
                else:
                    pass
                        
                    days_list.clear()

            elif tab == 'summary':
                pass

        driver.close()
        return data
x = WebScrapper()
x.scrap()

def keyboardInterruptHandler(signal, frame):
    print('Exiting Driver')
    driver.close()
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)
