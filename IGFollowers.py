"""
An automation project that requests Instagram login info from user, 
logs in, and then prints each follower's username and account name. 
"""

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://instagram.com/")

# Waits 30 seconds before finding each element in this script.
driver.implicitly_wait(30)

# Navigate and logs in to user's account.
username = driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input",
)

usernametxt = input('Username: ')
username.send_keys(usernametxt)

password = driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input",
)

passwordtxt = input('Password: ')
password.send_keys(passwordtxt)

try:
    login_button = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div",
    )
    login_button.click()
except:
    print("Incorrect username or password.")

# Navigate to user's account followers.
profile = driver.find_element(
    By.XPATH,
    "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a/div"
    )

profile.click()

followers = driver.find_element(
    By.XPATH, 
    '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a'
    )

followers.click()

usernames = driver.find_elements(
    By.CLASS_NAME, "_aacl._aaco._aacw._aacx._aad7._aade"
)

# Prints followers' usernames.
for usn in usernames:
    print(usn.text)
    
