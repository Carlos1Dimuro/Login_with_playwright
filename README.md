**Automated Registration and Login Script**

This repository contains a script that automates the registration and login process for the website "buggy.justtestit.org" using Playwright. Below is a detailed explanation of the script's functionality and its components.

**Script Overview**
The script is designed to:

Register users: It fills out the registration form on the website using data from an Excel file.
Log in users: It logs in with the newly registered credentials to verify successful registration.
Take Screenshots: Screenshots are taken after successful logins and in case of failures to assist with bug reporting.
Key Features

**Data Source:**

The script reads user data from an Excel file (Libro1.xlsx) located on the user’s computer. This file includes columns for various user details such as username, first name, last name, and password.
The path to the Excel file is specified in the script, but it could easily be modified to read data from another source if needed (e.g., a CSV file, a database, or another type of file).

**Browser Automation:**

The script uses Playwright to launch a Chromium browser. It’s currently configured to run in non-headless mode (i.e., with a visible browser window), but this can be changed as per your requirements.
Although the script is tested with Chromium (the engine behind Chrome), Playwright supports other browsers such as Firefox and WebKit (Safari). You can easily switch browsers by modifying the line where the browser is launched.

**Registration Process:**

The script navigates to the homepage of the website.
It clicks the 'Register' button to access the registration form.
It automatically fills out the registration form with data from the Excel file and submits it.

**Login Process:**

After registering a user, the script logs in with the same credentials.
It checks for elements that confirm a successful login, like the presence of a "Logout" button.

**Error Handling and Screenshots:**

As a best practice, the script takes screenshots after each successful login, saving them in the same directory as the Excel file.
If any error occurs during registration or login, the script captures a screenshot at the moment of failure. This helps in bug reporting by providing visual evidence of the issue.
All errors are logged with appropriate messages, indicating which user’s registration or login attempt failed.

**Flexibility and Modifications:**

The script is flexible and can be easily modified to accommodate different testing scenarios or browser environments. You can adjust the data source, target browsers, and other configurations as needed.

**Getting Started**

**How to Run the Script**
Follow these steps to set up and execute the script for automated registration and login:

**Clone the Repository:**

**bash
Copiar código**
git clone https://github.com/Carlos1Dimuro/Login_with_playwright.git

After cloning, navigate into the directory of the cloned repository:
cd your-repository

**Install Required Dependencies:**
Ensure you have Python installed. Then, install the necessary Python libraries by running:

**bash
Copiar código**
pip install pandas playwright openpyxl

**Locate the Excel File:**

The Excel file is included in the repository. It is located at data/Libro1.xlsx (or the appropriate path based on your repository structure).

**Update the Script with the Correct Path:**

Open the script file (e.g., automation_script.py) in a text editor.

***Locate the line where the Excel file path is specified:***
**python
Copiar código**
file_path = r"data/Libro1.xlsx"
Ensure the path matches the location of the Excel file within the repository.

**Run the Script:
Execute the script using Python:**

bash
Copiar código
python automation_script.py

Review Results:

The script will perform automated registration and login on the specified website.
Check the screenshots directory for the output files. The filenames will indicate whether the login was successful or if there was an error.

Troubleshooting:

If you encounter any issues, make sure that the Excel file's structure matches the script's expected format.
Verify that all dependencies are correctly installed.
Review any error messages printed in the console for guidance on resolving issues.
Or contact me so we can find a solution.
**https://www.linkedin.com/in/carlosdimurolarg/**
