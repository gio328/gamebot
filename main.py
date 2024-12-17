from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


try:
    # Find the cookie element
    cookie = driver.find_element(By.ID, "cookie")
    
    while True:
        cookie.click()
        time.sleep(0.2)

except NoSuchElementException as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("Stopped")
    driver.quit()