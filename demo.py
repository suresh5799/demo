import streamlit as st
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

try:
    # Convert secret JSON string into dictionary
    service_account_json = st.secrets["GOOGLE_SERVICE_ACCOUNT"]
    service_account_info = json.loads(service_account_json)

    # Authenticate Google Drive API
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    drive_service = build("drive", "v3", credentials=credentials)

    st.success("✅ Connected to Google Drive successfully!")

except json.JSONDecodeError as e:
    st.error(f"❌ JSON Decode Error: Check secrets formatting. {e}")

except Exception as e:
    st.error(f"❌ Google Drive API connection failed: {e}")
