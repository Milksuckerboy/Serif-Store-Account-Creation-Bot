# Serif Store Account Creator
#
# A Python script using Selenium to automate the creation of a free account
# on the Serif store for a specific product checkout flow.
#
# Author: Milksuckerboy
# License: MIT License (A common, permissive open-source license)

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# --- SCRIPT CONFIGURATION ---
# It's good practice to put configurable variables at the top.
# This makes it easy for other users to change settings without digging into the code.

# The target URL for the specific checkout basket
TARGET_URL = "https://store.serif.com/en-us/checkout/?basket=47d8e6b4b90006b696cfb31da9f7cc4ad6b644a67f61841c"

# Set your desired credentials here.
# For security, you might want to load these from a separate config file or environment variables.
EMAIL_TO_ENTER = "your-test-email@example.com"
PASSWORD_TO_ENTER = "YourSecureP@ssw0rd123!"

def create_serif_account(driver):
    """
    Main function to automate the account creation process.
    """
    try:
        # 1. Navigate to the website
        print(f"Navigating to: {TARGET_URL}")
        driver.get(TARGET_URL)
        wait = WebDriverWait(driver, 10)

        # 2. Handle the cookie consent pop-up by removing it with JavaScript
        print("Waiting for the cookie consent pop-up...")
        cookie_banner = wait.until(EC.presence_of_element_located((By.ID, "cookie-notice")))
        print("Cookie pop-up found. Removing it with JavaScript...")
        driver.execute_script("arguments[0].remove();", cookie_banner)
        print("Cookie pop-up removed successfully.")

        # 3. Enter Email and Continue
        print("Waiting for the email input field...")
        email_field = wait.until(EC.visibility_of_element_located((By.ID, "new-email")))
        email_field.click()
        print(f"Entering email: {EMAIL_TO_ENTER}")
        email_field.send_keys(EMAIL_TO_ENTER)
        time.sleep(1) # Short pause for stability

        print("Clicking the 'Continue' button...")
        continue_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        continue_button.click()

        # 4. Fill in Personal Details
        print("Waiting for user detail fields...")
        first_name_field = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
        
        first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
        random_first_name = random.choice(first_names)
        print(f"Entering first name: {random_first_name}")
        first_name_field.send_keys(random_first_name)

        last_name_field = driver.find_element(By.ID, "last-name")
        last_names = ["Smith", "Jones", "Williams", "Brown", "Davis"]
        random_last_name = random.choice(last_names)
        print(f"Entering last name: {random_last_name}")
        last_name_field.send_keys(random_last_name)

        password_field = driver.find_element(By.ID, "new-password")
        print("Entering password...")
        password_field.send_keys(PASSWORD_TO_ENTER)

        # 5. Agree to Terms and Create Account
        print("Waiting for the 'Terms and Conditions' checkbox...")
        terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "terms-and-conditions")))
        print("Clicking the checkbox using JavaScript...")
        driver.execute_script("arguments[0].click();", terms_checkbox)
        
        print("Waiting for the 'Create Account' button...")
        create_account_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        print("Clicking 'Create Account'...")
        create_account_button.click()

        print("\nAutomation successful! Account creation process completed.")
        print("The browser will remain open for 20 seconds to view the result.")
        time.sleep(20)

    except TimeoutException as e:
        print(f"\nError: A timeout occurred. An element might not have appeared in time.")
        print(f"Details: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

def main():
    """
    Initializes the WebDriver and starts the automation.
    """
    print("--- Starting Serif Account Creation Script ---")
    
    # Initialize the WebDriver
    # Using a 'with' statement ensures the browser is closed even if errors occur.
    with webdriver.Firefox() as driver:
        create_serif_account(driver)

    print("\n--- Script Finished ---")

if __name__ == "__main__":
    main()