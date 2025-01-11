from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time


def unlike_all_posts(username, password):
    try:
        # Set up the WebDriver using the Service class
        service = Service("C:\\Users\\anujt\\Downloads\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        # Open Instagram
        driver.get("https://www.instagram.com/")
        time.sleep(3)

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
            select_option= driver.find_element(By.XPATH,'//span[@data-bloks-name="bk.components.Text" and contains(text(), "Select")]')
            select_option.click()
            print("Selected option to select all")
            time.sleep(5)
            checkbox_elements = driver.find_elements(By.XPATH, '//*[@aria-label="Toggle checkbox"]')
            #selectable_posts = driver.find_elements(By.XPATH,"//div[contains(@role, 'button')]//span[@aria-label='Unlike']")
            print("Selectable posts:\n")
            if not checkbox_elements:
                print("No more posts to select.")
                break

            for i, post in enumerate(checkbox_elements):
                if i >= 15:  # Limit to 100 posts
                    break
                print("Clicking post")
                post.click()
                time.sleep(0.5)  # Slight delay to mimic user behavior

            # Click the "Unlike" button
            unlike_button = driver.find_element(By.XPATH, '//div[@aria-label="Unlike"]')
            if unlike_button:
                print("Clicking unlike button")
                unlike_button.click()
                time.sleep(2)  # Wait for dialog box to appear

                # Handle confirmation dialog
                confirmation_dialog = driver.find_element(By.XPATH, '//button[.//div[text()="Unlike"]]')
                if confirmation_dialog:
                    confirmation_dialog.click()
                    print("Confirmed unliking posts.")
            else:
                print("No 'Unlike' button found.")
                break

            # Scroll down to load more posts
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            time.sleep(5)

        print("Completed unliking posts.")
        #driver.quit()

    except Exception as e:
        print(f"Error: {e}")
        if 'driver' in locals():
            print("Driver quit")
            #driver.quit()


# Replace with your Instagram credentials
username = "jeetgilluniverse"
password = "divya@1234"

unlike_all_posts(username, password)