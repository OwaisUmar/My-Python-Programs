from selenium import webdriver
from selenium.webdriver.common.keys import Keys

edge = webdriver.Edge(r'C:\Users\USER\Downloads\edgedriver_win64\msedgedriver.exe')
edge.get('https://www.google.com')
search = edge.find_element_by_class_name('a4bIc')
search.click('Owais')

