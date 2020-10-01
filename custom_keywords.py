from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as KEYS
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import xlsxwriter

workbook = xlsxwriter.Workbook('Data_list.xlsx')
worksheet = workbook.add_worksheet()
from robot.api.deco import keyword

driver = webdriver.Chrome(r"C:\Users\sougar\Downloads\chromedriver_win32\chromedriver.exe")
actions = ActionChains(driver)


class AmazonUI():
    @keyword('sample_login')
    def sample(self):
        driver.maximize_window()
        driver.get("https://www.amazon.in")

    @keyword('search item')
    def search_item(self, item_name):
        driver.find_element_by_id("twotabsearchtextbox").send_keys("{}".format(item_name))
        driver.find_element_by_xpath('//*[@id="nav-search-submit-text"]').click()

    @keyword('select_category')
    def select_category(self, category, sub_category):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nav-hamburger-menu")))
        driver.find_element_by_xpath("//a[@role='button' and @aria-label='Open Menu']").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "hmenu-content")))
        category = driver.find_element_by_xpath("//a[@class='hmenu-item']/div[contains(text(),'{}')]".format(category))
        category.click()
        sub_category = driver.find_element_by_xpath(
            "//a[@class='hmenu-item' and contains(text(),'{}')]".format(sub_category))
        sub_category.click()
        time.sleep(1)

    @keyword('select_brand')
    def select_brand(self, brand):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "brandsRefinements")))
        brand = driver.find_element_by_xpath(
            '//div[@id="brandsRefinements"]//span[contains(text(),"{}")]'.format(brand))
        brand.location_once_scrolled_into_view
        brand.click()
        time.sleep(1)

    @keyword('select_screen')
    def select_screen(self, screen_size):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "brandsRefinements")))
        screen = driver.find_element_by_xpath(
            '//ul[@class="a-unordered-list a-nostyle a-vertical a-spacing-medium"]//span[contains(text(),"{}")]'.format(
                screen_size))
        screen.location_once_scrolled_into_view
        screen.click()
        time.sleep(1)

    @keyword('select item')
    def select_item(self, item_name):
        iphoneXS = driver.find_element_by_xpath('//span[contains(text(),"{}")]'.format(item_name))
        iphoneXS.location_once_scrolled_into_view
        iphoneXS.click()
        time.sleep(1)

    @keyword('save_screenshot')
    def save_screenshot(self):
        driver.save_screenshot('WebsiteScreenShot.png')

    @keyword('print_data')
    def print_data(self):
        row = 0
        column = 0
        data = driver.find_element_by_xpath('//*[@id="search"]')
        content = data.find_elements_by_tag_name('a')
        for item in content:
            text = item.text
            worksheet.write(row, column, text)
            row += 1
        workbook.close()

    @keyword('close_browser')
    def close(self):
        driver.close()
