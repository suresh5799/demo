import streamlit as st
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Debug: Check if secrets are loaded
try:
    service_account_info = json.loads(st.secrets["GOOGLE_SERVICE_ACCOUNT"])
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    drive_service = build('drive', 'v3', credentials=credentials)
    st.write("✅ Google Drive API connected successfully!")
except Exception as e:
    st.error(f"❌ Google Drive API connection failed: {e}")

# Debug: Check if Drive files are listed
try:
    results = drive_service.files().list(pageSize=10).execute()
    files = results.get("files", [])
    if not files:
        st.warning("⚠️ No files found in Google Drive.")
    else:
        st.write("📂 Files in Google Drive:")
        for file in files:
            st.write(f"{file['name']} ({file['id']})")
except Exception as e:
    st.error(f"❌ Failed to fetch files: {e}")

# Debug: Check if search input is working
query = st.text_input("Enter the Goal Name (e.g., Secure Flash)")
if query:
    st.write(f"🔍 Searching for: {query}")
