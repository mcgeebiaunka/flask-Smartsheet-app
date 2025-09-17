import smartsheet
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("SMARTSHEET_ACCESS_TOKEN")
smartsheet_client = smartsheet.Smartsheet(ACCESS_TOKEN)

try:
    sheets = smartsheet_client.Sheets.list_sheets(include_all=True)
    print("✅ Sheets your account can access:")
    for sheet in sheets.data:
        print(f"- {sheet.name} (ID: {sheet.id})")
except Exception as e:
    print("❌ Error listing sheets:", e)