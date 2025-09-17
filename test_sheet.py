import smartsheet
import os
from dotenv import load_dotenv

load_dotenv()

smartsheet_client = smartsheet.Smartsheet(os.getenv("SMARTSHEET_ACCESS_TOKEN"))
SHEET_ID = int(os.getenv("SMARTSHEET_SHEET_ID"))

try:
    sheet = smartsheet_client.Sheets.get_sheet(SHEET_ID)
    print(f"✅ Connected to sheet: {sheet.name}")
    print(f"Total columns: {len(sheet.columns)}")
    for col in sheet.columns:
        print(f"- {col.title} (ID: {col.id}, Type: {col.type})")
except smartsheet.exceptions.SmartsheetException as e:
    print("❌ Error accessing sheet:", e)