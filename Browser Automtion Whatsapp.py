from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(r'C:\Users\USER\Downloads\edgedriver_win64\msedgedriver.exe')
driver.get('https://web.whatsapp.com')
wait = WebDriverWait(driver, 600)
target = '"Fahad"'  # Enter your friend's name
string = 'Message sent using Python!!!'  # Enter your message
x_arg = '//span[contains(@title,' + target + ')]'
target = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()
input_box = driver.find_element_by_id('DuUXI')
for i in range(100):
    input_box.send_keys(string+Keys.ENTER)

