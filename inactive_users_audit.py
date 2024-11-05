import csv
from datetime import datetime

# in GAM enter 'gam print users fields email,givenName,familyName,lastlogintime > C:\Users\joepl\user_activity.csv'

# Define the number of days for inactivity threshold (90 days)
INACTIVITY_THRESHOLD_DAYS = 90
CURRENT_DATE = datetime.now()

# Path to the CSV file exported by GAM # Use your own location
csv_file_path = 'C:\\Users\\joepl\\user_activity.csv'


# List to store inactive users
inactive_users = []

# Function to convert the Google last login string to a datetime object
def parse_last_login_date(date_str):
    try:
        # Example date format from GAM: 2023-06-01T12:45:00Z
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z").date()
    except ValueError:
        return None

# Read the CSV file and check for inactive users
with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        user_email = row['primaryEmail']  # Updated to primaryEmail
        first_name = row['name.givenName']
        last_name = row['name.familyName']
        last_login = row['lastLoginTime']

        # Skip users with no last login date
        if not last_login or last_login == 'Never':
            inactive_users.append((first_name, last_name, user_email))
            continue

        # Parse the last login date
        last_login_date = parse_last_login_date(last_login)

        # Check if the user has been inactive for more than 90 days
        if last_login_date and (CURRENT_DATE.date() - last_login_date).days > INACTIVITY_THRESHOLD_DAYS:
            inactive_users.append((first_name, last_name, user_email))

# Output the list of inactive users
if inactive_users:
    print(f"Users inactive for more than {INACTIVITY_THRESHOLD_DAYS} days:")
    for first_name, last_name, email in inactive_users:
        print(f"{first_name} {last_name} <{email}>")
else:
    print(f"No users have been inactive for more than {INACTIVITY_THRESHOLD_DAYS} days.")


