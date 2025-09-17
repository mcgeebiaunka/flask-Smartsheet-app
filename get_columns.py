import requests

ACCESS_TOKEN = "hPChOir7OB1srrh2YBWbvFWK4f7VJtR3ti8SW"
SHEET_ID = 1061698400112516  # replace with your real sheet ID

url = f"https://api.smartsheet.com/2.0/sheets/{1061698400112516}"
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("📋 Columns in your sheet:")
    for col in data["columns"]:
        print(f"Name: {col['title']}   ID: {col['id']}   Type: {col['type']}")
else:
    print(f"❌ Error: {response.status_code} - {response.text}")