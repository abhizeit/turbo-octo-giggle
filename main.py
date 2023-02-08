import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui as pg
from selenium.webdriver.common.by import By
from datetime import date
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



today = date.today()
today = today.strftime("%d-%m-%Y")
chrome_driver_path = Service('C:/Development/chromedriver.exe')
driver = webdriver.Chrome(service=chrome_driver_path)

# open the course Platform

driver.get("https://course.masaischool.com")

# fill in the credentials

email = driver.find_element(By.ID, "email")
email.send_keys(YOUR_EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(YOUR_PASSWORD)

#login

submit = driver.find_element(By.CSS_SELECTOR, "button")
submit.click()

#open the lectures page

lecture = driver.find_element(By.LINK_TEXT, "Lectures")
lecture.click()

#find the scrum link

scrum_link = driver.find_element(By.PARTIAL_LINK_TEXT, today)
print(scrum_link)
scrum_link.click()

# get the zoom link

join_meet = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div/a")
join_meet.click()

#switch to newly opened window

driver.switch_to.window(driver.window_handles[1])

#wait until the JOIN button  appears on the screen
try:
    zoom_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.mbTuDeF1"))
    )
    zoom_button.click()
    time.sleep(4)
    pg.press('tab', presses=2)
    pg.press('enter')
    time.sleep(4)
finally:
    #swith back to the main window
    driver.switch_to.window(driver.window_handles[0])

#open the menu
menu = driver.find_element(By.XPATH, "/html/body/div[2]/nav/div[1]/div/div[2]/div/div/div[1]/span/button")
menu.click()

#logout from the website
logout = driver.find_element(By.XPATH, "/html/body/div[2]/nav/div[1]/div/div[2]/div/div/div[2]/div/form/a")
logout.click()
time.sleep(5)

#quit the browser
driver.quit()








