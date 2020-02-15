from time import sleep
from os import walk

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from secrets import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.matches = 0

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(2.5)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_btn.click()

        sleep(1.5)

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)

        sleep(1)

        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()

        sleep(1)

        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()

    def check(self):
        while True:
            try:
                self.popup()
            except Exception:
                try:
                    self.close_match()
                except Exception:
                    break

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()
        self.matches += 1

    def get_pic(self, profile_id, img_id):
        img = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div')
        img.screenshot(f"photos/{profile_id}_{img_id}.png")

    def swiper(self):
        files = []
        for (_, _, filename) in walk("photos"):
            files.extend(filename)
            break

        files2 = [int(file.split("_")[0]) for file in files]

        profile_id = max(files2) + 1
        i = 0

        for i in range(2):
            sleep(0.2)
            self.check()
            for image_id in range(5):
                self.get_pic(profile_id, image_id)
                sleep(0.1)
                ActionChains(self.driver).send_keys(Keys.SPACE).perform()
            profile_id += 1
            i += 1
            self.like()

bot = TinderBot()
bot.login()
