from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import credentials
#setting browser and browser configs
firefox_options = Options()
firefox_options.add_argument("--disable-notifications")
driver = webdriver.Firefox(options=firefox_options)


username = credentials.username #getting username from credentials.py
password = credentials.password#getting password from credentials.py 

for i in range(3):#trying it thrice incase an error occurs
    driver.get('https://twitter.com/i/flow/login')#navigating to twitter website login
    try:
        usernamebox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@autocomplete = "username"]')))
        usernamebox.click()
        usernamebox.send_keys(username)#entering username
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '// span[contains(text(),"Next")]'))).click()#click next
        passwordbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@name = "password"]')))
        passwordbox.click()
        passwordbox.send_keys(password)#entering password
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid = "LoginForm_Login_Button"]'))).click()
    except: continue
    print('Login Successful')
    break
WebDriverWait(driver, 30).until(EC.url_to_be('https://twitter.com/home'))#wait till the page is loaded
driver.get(f'https://twitter.com/{username}/likes')#navigating to likes page
counter = 0 #counter to count unliked tweets
while True:
    try: 
        unlike_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid = "unlike"]')))
        unlike_button.click()
        driver.implicitly_wait(1)
    except TimeoutException: break #if there are no more liked tweets to unlike break the loop
    except: driver.refresh()
    counter += 1#update counter
    if counter % 10 == 0: driver.get(f'https://twitter.com/{username}/likes')#navigating to likes page/ refresing again, to solve the issue of twitter sometimes loading only 10 tweets at a time 

print(f'unliked {counter} likes')
print('Successfully unliked all the likes')
