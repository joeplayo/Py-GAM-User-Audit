# PyGAM Generate User Activity Report for Users who have not logged in <90 Days.
Python Scripts to run in Conjunction with Google Admin Manager

First Open Terminal and run the following Command: 'gam print users fields email,givenName,familyName,lastlogintime > C:\YourName\YourDirectory\user_activity.csv'

Open Explorer
Go to Wherever you save inactive_users_audit.py
Copy Path
Open a new Admin CMD Line / Terminal Window 
Type "CD" then Paste the Copied Path
Run the following: python inactive_users_audit.py

Open user_activity.csv with Excel or Google Sheets, and it should be auditted correctly.
