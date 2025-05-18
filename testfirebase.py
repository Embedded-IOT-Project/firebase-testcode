import requests
import json
from datetime import datetime

FIREBASE_URL = 'https://safem8-ccdf0-default-rtdb.asia-southeast1.firebasedatabase.app/logs.json'

def ping_firebase(data):
    try:
        response = requests.post(FIREBASE_URL, data=json.dumps(data))
        if response.status_code == 200:
            print("✅ Data sent successfully:", response.json())
        else:
            print("❌ Failed to send data:", response.text)
    except Exception as e:
        print("⚠️ Error:", e)

# test payload
data_payload = {
    "timestamp": datetime.now().isoformat(),
    "device": "EPS32",
    "status": "online",
    "message": "Ping from Python script",
    "temp": "30"
}

ping_firebase(data_payload)