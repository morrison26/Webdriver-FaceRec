from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
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

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        ActionChains(self.driver).send_keys(Keys.ARROW_UP)
        for image_id in range(5):
            self.get_pic(profile_id, image_id)
            ActionChains(self.driver).send_keys(Keys.SPACE)
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
        img = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[1]/span/a[2]/div/div[1]/div/div[1]/div/div/div')
        img.screenshot(f"pictures/{profile_id}_{img_id}")
    #
    #     actions.send_keys(Keys)

    def swiper(self):
        i = 0

        while i < 10:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.popup()
                except Exception:
                    self.close_match()
            i += 1

bot = TinderBot()
bot.login()
