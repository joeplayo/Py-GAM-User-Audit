from telegram.ext import Updater, CommandHandler
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Authenticate with Google Workspace Admin SDK
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']
SERVICE_ACCOUNT_FILE = 'path/to/service_account_credentials.json'

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('admin', 'directory_v1', credentials=creds)

# List all users in the domain
def list_users():
    users = service.users().list(customer='my_customer', orderBy='email').execute()
    return users.get('users', [])

# Function to check if a user is inactive
def is_inactive(user):
    # Implement your logic here to determine if the user is inactive
    # For example, you could check the last login date
    return True

# Command handler for /audit_users command
def audit_users(update, context):
    users = list_users()
    inactive_users = []
    for user in users:
        if is_inactive(user):
            inactive_users.append(user['primaryEmail'])
    if inactive_users:
        update.message.reply_text(f"Inactive users: {', '.join(inactive_users)}")
    else:
        update.message.reply_text("No inactive users found.")

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("audit_users", audit_users))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
