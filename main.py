from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(50)
driver.get("https://www.digikala.com/users/login/?backUrl=/")
username = driver.find_element('xpath','//*[@id="__next"]/main/div[2]/div[2]/form/label/div/div/input')
username.send_keys('')
username.send_keys(Keys.RETURN)
sleep(5)
password =driver.find_element('xpath','//*[@id="__next"]/main/div[2]/div[2]/form/label/div/div[1]/input')
password.send_keys('')
password.send_keys(Keys.RETURN)
sleep(5)
driver.quit()



