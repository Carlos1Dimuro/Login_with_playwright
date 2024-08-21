import os
import pandas as pd
from playwright.sync_api import sync_playwright

def main():
    """
    Main function to automate the registration and login process using Playwright.
    It reads user data from an Excel file, performs registration, logs in, and 
    takes screenshots on success or failure.
    """
    # Load the Excel file. Replace with the location where you placed the Excel file.
    file_path = r"location where you placed the Excel file\Libro1.xlsx"
    users_df = pd.read_excel(file_path, engine='openpyxl')
    # Get the directory path of the Excel file
    base_path = os.path.dirname(file_path)

    # Start Playwright
    with sync_playwright() as p:
        # Launch the browser in headless mode
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Iterate over each row in the DataFrame to perform registration and login
        for index, row in users_df.iterrows():
            try:
                page.goto("https://buggy.justtestit.org/", wait_until="load", timeout=6000)

                # Click the 'Register' button on the main page
                page.click('text=Register')  # Use text to identify the button

                # Fill in the registration form fields
                page.fill('input[formcontrolname="username"]', str(row['Col']))
                page.fill('input[formcontrolname="firstName"]', str(row['Col1']))
                page.fill('input[formcontrolname="lastName"]', str(row['Col2']))
                page.fill('input[formcontrolname="password"]', str(row['Col3']))
                page.fill('input[formcontrolname="confirmPassword"]', str(row['Col4']))
                # Wait until button "Register" appears
                page.wait_for_selector('button[type="submit"]', timeout=6000)
                # Click the 'Register' button after filling in the form data
                page.click('button[type="submit"].btn.btn-default')

                # Wait until the login field appears
                page.wait_for_selector('input[name="login"]', timeout=6000)

                # Log in with the new user
                page.fill('input[name="login"]', str(row['Col5']))
                page.fill('input[name="password"]', str(row['Col6']))
                page.click('button[type="submit"]')

                # Wait until an element visible only when logged in appears
                try:
                    page.wait_for_selector('text=Logout', timeout=6000)
                    # Take a screenshot after successful login
                    screenshot_path = os.path.join(base_path, f"{row['Col']}_logged_in.png")
                    page.screenshot(path=screenshot_path)
                    # Log out
                    page.click('text=Logout')
                    page.wait_for_selector('text=Login', timeout=6000)
                except Exception:
                    # Capture the screen of the error message if login fails
                    screenshot_error_path = os.path.join(base_path, f"{row['Col']}error.png")
                    page.screenshot(path=screenshot_error_path)
                    print(f"Error in row {index}: Login failed for user {row['Col']}")

            except Exception as e:
                print(f"Error in row {index}: {e}")

        browser.close()

if __name__ == "__main__":
    main()
