import unittest

import time
from time import sleep
from appium import webdriver
import pandas as  pd




class AppiumTests(unittest.TestCase):
    
    
    def setUp(self):
        
        desired_caps = {}
                
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.1'
        desired_caps['deviceName'] = 'ALE'
        desired_caps['udid'] = 'your_udid'
        desired_caps['noReset'] = True
        desired_caps['appPackage'] = 'com.tripadvisor.tripadvisor'
        desired_caps['appActivity'] = 'com.tripadvisor.tripadvisor.TripAdvisorTripAdvisorActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        
    def testHot(self):
        time.sleep(10)
        self.driver.find_element_by_id('com.tripadvisor.tripadvisor:id/expanded_pill').click()
        time.sleep(7)
        self.driver.find_element_by_id('com.tripadvisor.tripadvisor:id/query_text').send_keys('London, England')
        self.driver.press_keycode(66)
        time.sleep(5)
        self.driver.find_element_by_class_name('android.view.View').click()
        time.sleep(5)
        self.driver.find_element_by_id('com.tripadvisor.tripadvisor:id/search_image').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.tripadvisor.tripadvisor:id/what_query_text').send_keys('The Grocvenor Hotel')
        
        self.driver.press_keycode(66)
        time.sleep(5)
        self.driver.find_element_by_accessibility_id('Отели').click()
        time.sleep(5)
        ff = self.driver.find_elements_by_xpath('//android.widget.RelativeLayout')
        self.driver.scroll(ff[6],ff[0])
        time.sleep(5)
        hot = self.driver.find_element_by_id('com.tripadvisor.tripadvisor:id/title')
        if hot.text == 'The Grosvenor Hotel':
        
            self.driver.find_element_by_xpath("//*[contains(@text,'The Grosvenor Hotel')]").click()
            time.sleep(5)
        else:
            self.driver.scroll(ff[6],ff[0])
            time.sleep(5)
            self.driver.find_element_by_xpath("//*[contains(@text,'The Grosvenor Hotel')]").click()
        time.sleep(5)
        
        event = {
                
                1:'2019-05-01',
                2:'2019-05-20',
                3:'2019-06-10',
                4:'2019-06-20',
                5:'2019-07-01'
            
                }
        
        for i in range(1,6):
            
            print(event[i])
            time.sleep(10)
            but =self.driver.find_element_by_id('com.tripadvisor.tripadvisor:id/set_dates_button')
            time.sleep(3)
            but.click()
            time.sleep(3)
            self.driver.find_element_by_id('com.tripadvisor.tripadvisor:id/action_clear').click()

            time.sleep(5)
            self.driver.find_element_by_accessibility_id(event[i]).click()
            time.sleep(10)
            
            self.driver.find_element_by_accessibility_id(event[i][:9] + '6').click()
            time.sleep(5)
    
            self.driver.press_keycode(66)
            time.sleep(15)
            vv = self.driver.find_elements_by_xpath('//android.widget.TextView')
            self.driver.scroll(vv[2],vv[0])
            time.sleep(3)
            self.driver.find_element_by_id('com.tripadvisor.tripadvisor:id/text_links_open_close_button').click()    
            title = self.driver.find_elements_by_id('com.tripadvisor.tripadvisor:id/title')
            price = self.driver.find_elements_by_id('com.tripadvisor.tripadvisor:id/price')
            date = self.driver.find_elements_by_id('com.tripadvisor.tripadvisor:id/set_dates_button')
            titles = []
            for til in title:
                titles.append(til.text)
            prices = []
            for pri in price:
                prices.append(pri.text)
            dates = []
            for day in date:
                dates.append(day.text)
            dtj = pd.DataFrame(prices[1:], titles, dates)
            dtj.to_json('{}.json'.format(i))
            path_screen = '/home/path_your_file'
            file ='screen{}.png'.format(i)
            self.driver.save_screenshot(path_screen + file)
            self.driver.scroll(vv[1],vv[4])
            time.sleep(3)
            
            
    def testDown(self):
        self.driver.quit()

if __name__ == '__main__':
  unittest.main()