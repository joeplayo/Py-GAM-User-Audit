# PyGAM GAM and Python Automation / User Audit for Activity Report for Users who have not logged in <90 Days.

Use GAM and Python to Automate Auditing your Users and Generate that info into a CSV in order to free up Licenses and perge Inactive Accounts.

GAM installation or GAMX is required for this to work.

Python Scripts to run in Conjunction with Google Admin Manager

Install and provision 

First Open Terminal and run the following Command: 'gam print users fields email,givenName,familyName,lastlogintime > C:\YourName\YourDirectory\user_activity.csv'

Open Explorer
Go to Wherever you save inactive_users_audit.py
Copy Path
Open a new Admin CMD Line / Terminal Window 
Type "CD" then Paste the Copied Path
Run the following: python inactive_users_audit.py

Open user_activity.csv with Excel or Google Sheets, and it should be auditted correctly.
