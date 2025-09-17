import smartsheet
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get token
ACCESS_TOKEN = os.getenv("SMARTSHEET_ACCESS_TOKEN")

if not ACCESS_TOKEN:
    print("❌ No Smartsheet token found in environment. Check your .env file.")
    exit()

# Initialize client
smartsheet_client = smartsheet.Smartsheet(ACCESS_TOKEN)

# Simple test: get your account details
try:
    user_profile = smartsheet_client.Users.get_current_user()
    print("✅ Smartsheet connection successful!")
    print("Hello,", user_profile.email)
except Exception as e:
    print("❌ Error connecting to Smartsheet:", e)