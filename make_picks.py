from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import json

fname = 'settings.json'

try:
   settings_file = open(fname)
except FileNotFoundError:
   print("File %s not found" % fname)
   exit()

with settings_file:
   settings = json.load(settings_file)

browser = webdriver.Firefox()
browser.set_page_load_timeout(30)
browser.get(settings['picksUrl'])

browser.find_element_by_id('userid').send_keys(settings['email'])
browser.find_element_by_id('password').send_keys(settings['password'])
browser.find_element_by_id('login_form').submit()

# Wait for page to load
delay = 10 # seconds max wait

WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'makePicks')))

games = browser.find_element_by_id('makePicks').find_elements_by_tag_name('li')

for game in games:
   if not 'locked' in game.get_attribute('class'):
      away = game.find_element_by_class_name('awayTeamSelection')
      home = game.find_element_by_class_name('homeTeamSelection')
      if (not 'selected' in home.get_attribute('class')) and (not 'selected' in away.get_attribute('class')):
         home.click()

points_tie_breaker = browser.find_element_by_id('mnfTieBreaker')

if points_tie_breaker.get_attribute('value') == '':
   points_tie_breaker.send_keys('44')

browser.find_element_by_id('pickSubmit').click()

browser.close()
