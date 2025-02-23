import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import ElementNotInteractableException
import time

batch = 100

def unlike_all_posts(username, password):
    try:
        # Set up the WebDriver using the Service class
        service = Service("C:\\Users\\Divya\\Downloads\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        # Open Instagram
        driver.get("https://www.instagram.com/")
        time.sleep(1)
        
        # allow cookies
        driver.find_element(By.XPATH, "//button[text()='Allow all cookies']").click()

        # Login
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

        # Wait for OTP entry
        print("Please enter the OTP manually in the browser.")
        input("Press Enter after entering the OTP and completing the login process...")

        # Navigate to 'Your Activity' > 'Likes'
        driver.get("https://www.instagram.com/your_activity/interactions/likes/")
        time.sleep(5)

        # Unlike posts
        while True:
            # Select up to 100 posts
            WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.XPATH,'//span[@data-bloks-name="bk.components.Text" and contains(text(), "Select")]'))).click()
            print("Selected option to select all")
            time.sleep(0.5)
            checkbox_elements = driver.find_elements(By.XPATH, '//*[@aria-label="Toggle checkbox"]')
            #selectable_posts = driver.find_elements(By.XPATH,"//div[contains(@role, 'button')]//span[@aria-label='Unlike']")
            print("Selectable posts:\n")
            if not checkbox_elements:
                print("No more posts to select.")
                break
            
            i = 0
            while i < batch:
                try:
                    checkbox_elements = driver.find_elements(By.XPATH, '//*[@aria-label="Toggle checkbox"]')
                    post = checkbox_elements[i]
                except IndexError:
                    break
                print("Clicking post")
                driver.execute_script("arguments[0].scrollIntoView();", post)
                try:
                    post.click()
                except ElementNotInteractableException:
                    pass
                i += 1
                time.sleep(0.05)  # Slight delay to mimic user behavior

            # Click the "Unlike" button
            unlike_button = driver.find_element(By.XPATH, '//div[@aria-label="Unlike"]')
            if unlike_button:
                print("Clicking unlike button")
                unlike_button.click()
                time.sleep(0.5)  # Wait for dialog box to appear

                # Handle confirmation dialog
                confirmation_dialog = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[.//div[text()="Unlike"]]')))
                if confirmation_dialog:
                    confirmation_dialog.click()
                    time.sleep(0.5)
                    driver.refresh() # refresh the page to bypass some kind of rate limiter that instagram has set up to slow down the loading of posts after the unlike button is clicked
                    print("Confirmed unliking posts.")
            else:
                print("No 'Unlike' button found.")
                break

            time.sleep(1)

        print("Completed unliking posts.")
        #driver.quit()

    except Exception as e:
        print(f"Error: {e}")
        if 'driver' in locals():
            print("Driver quit")
            #driver.quit()


# Replace with your Instagram credentials
username = "YOURINSTAUSERNAME"
password = "YOURPASSWORD"

unlike_all_posts(username, password)
