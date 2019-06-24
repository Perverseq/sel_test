from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PWTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_1(self):
        driver = self.driver
        driver.get('https://www.google.com/')
        input_field = driver.find_element_by_name("q")
        input_field.send_keys('Perfect World russia')
        input_field.send_keys(Keys.ENTER)
        assert "бесплатная онлайн игра" in driver.page_source
        site = driver.find_element_by_partial_link_text("Perfect World – бесплатная онлайн игра")
        site.click()
        news = driver.find_element_by_xpath('//*[@id="menu"]/li[1]/a')
        news.click()
        assert "Все новости" in driver.page_source
        about = driver.find_element_by_xpath('//*[@id="menu"]/li[2]/a')
        about.click()
        assert "30 миллионов" in driver.page_source

    def test_2(self):
        driver = self.driver
        driver.get("https://pw.mail.ru/")
        login_button = driver.find_element_by_id('block_user_not_registered_not_authed')
        login_button.click()
        email_field = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, "js_kit_signin__box__login")))
        email_field.send_keys('login')
        password_field = driver.find_element_by_id('js_kit_signin__password__input')
        password_field.send_keys('password')
        log_in_button = driver.find_element_by_id('js_kit_signin__submit')
        log_in_button.click()
        donate = driver.find_element_by_xpath("/html/body/div[3]/div/div[4]/a[1]")
        donate.click()
        driver.switch_to.frame(driver.find_element_by_id('payment_iframe'))
        _wait = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='xform-bonus']")))
        select = Select(driver.find_element_by_xpath('//*[@id="xform-bonus"]'))
        select.select_by_value('5')
        time.sleep(1)
        assert "66,90" == driver.find_element_by_id("xform-sum").get_attribute('value')
        select.select_by_value('10')
        time.sleep(1)
        assert "133,80" == driver.find_element_by_id("xform-sum").get_attribute('value')
        select.select_by_value('20')
        time.sleep(1)
        assert "267,60" == driver.find_element_by_id("xform-sum").get_attribute('value')
        select.select_by_value('50')
        time.sleep(1)
        assert "669" == driver.find_element_by_id("xform-sum").get_attribute('value')
        select.select_by_value('100')
        time.sleep(1)
        assert "1338" == driver.find_element_by_id("xform-sum").get_attribute('value')
        select.select_by_value('300')
        time.sleep(1)
        assert "4014" == driver.find_element_by_id("xform-sum").get_attribute('value')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
