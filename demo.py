import streamlit as st
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

try:
    # Load Google Service Account JSON from Streamlit Secrets
    service_account_info = json.loads(st.secrets["GOOGLE_SERVICE_ACCOUNT"])
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    
    # Create Google Drive API Client
    drive_service = build('drive', 'v3', credentials=credentials)
    st.success("✅ Google Drive API connected successfully!")

except Exception as e:
    st.error(f"❌ Google Drive API connection failed: {e}")
