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
**Getting Started
To run the script:**

Ensure you have the required dependencies installed, including Playwright and Pandas.
Place your Excel file with user data in the specified path or update the script to point to your desired data source.
Run the script to perform automated registration and login, and review the screenshots and logs for results.
