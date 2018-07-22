# This program plays the game '2048'
# Written by Daniel Barrera
# 2/18/2018

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

play = True
high_score = 0
new_score = 0
command = 0

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

try:
    key_input = browser.find_element_by_tag_name('body')

    while play is True:
        while not browser.find_element_by_class_name('retry-button').is_displayed():
            command = random.randrange(0, 4)
            if command == 0:
                key_input.send_keys(Keys.UP)

            elif command == 1:

                key_input.send_keys(Keys.LEFT)

            elif command == 2:
                key_input.send_keys(Keys.DOWN)

            elif command == 3:
                key_input.send_keys(Keys.RIGHT)

            time.sleep(.01)

        new_score = browser.find_element_by_class_name('best-container').text
        if int(new_score) > int(high_score):
            high_score = new_score
            print(high_score)

        try:
            retry = browser.find_element_by_class_name('retry-button')
            retry.click()

        except Exception as exc:
            play = False
            print(exc)

except Exception as exc:
    browser.close()
    print(exc)

