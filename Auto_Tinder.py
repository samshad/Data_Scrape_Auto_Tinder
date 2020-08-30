from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
from auth import password, email


class AutoTinder:
    def __init__(self):
        self.email = email
        self.password = password
        webdriver_path = 'chromedriver_win32/chromedriver.exe'
        chrome_options = Options()
        #chrome_options.add_argument("-incognito")
        self.driver = webdriver.Chrome(webdriver_path, options=chrome_options)
        self.driver.maximize_window()
    
    def login(self):
        self.driver.get('https://tinder.com')

        cookies_accept_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button/span')
        cookies_accept_btn.click()

        delay = 5
        try:
            fb_btn = WebDriverWait(self.driver, delay).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')))
            fb_btn.click()

            sleep(3)
            base_window = self.driver.window_handles[0]
            self.driver.switch_to.window(self.driver.window_handles[1])

            email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
            email_in.send_keys(self.email)

            pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
            pw_in.send_keys(self.password)

            login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
            login_btn.click()

            self.driver.switch_to.window(base_window)

            try:
                location_allow = WebDriverWait(self.driver, delay).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')))
                location_allow.click()
            except TimeoutException:
                print("Location allow button Loading took too much time!")

            try:
                notification_allow = WebDriverWait(self.driver, delay).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')))
                notification_allow.click()
            except TimeoutException:
                print("Notification button Loading took too much time!")

        except TimeoutException:
            print("Facebook login button Loading took too much time!")

    def like(self):
        like_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def get_details(self):
        try:
            details = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/button')))
            expand_btn = self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/button')
            expand_btn.click()
            sleep(2)
            name = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div/h1').text
            age = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/span').text
            tags = self.driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div[3]')
            bio = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div').text
            if tags:
                for tag in tags:
                    print(tag)
            print(name, age, bio)
        except TimeoutException:
            print("Name, Age Loading took too much time!")


if __name__ == '__main__':
    bot = AutoTinder()
    bot.login()
    sleep(3)
    bot.get_details()

