import streamlit as st
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# ✅ Load Service Account Credentials
try:
    service_account_info = json.loads(st.secrets["GOOGLE_SERVICE_ACCOUNT"])
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    drive_service = build('drive', 'v3', credentials=credentials)
    st.write("✅ Google Drive API connected successfully!")
except Exception as e:
    st.error(f"❌ Google Drive API connection failed: {e}")

# ✅ Define the Google Drive Folder ID
FOLDER_ID = "1N36EC-B3dN7wx3wUYC732os1S6RzjwHh"  # 🔴 Replace with your actual Google Drive Folder ID

# ✅ Fetch Files from the Specific Folder
try:
    query = f"'{FOLDER_ID}' in parents and mimeType='application/pdf'"
    results = drive_service.files().list(q=query, pageSize=10).execute()
    files = results.get("files", [])

    if not files:
        st.warning("⚠️ No PDF files found in the folder.")
    else:
        st.write("📂 PDF Files in the Folder:")
        for file in files:
            st.write(f"{file['name']} ({file['id']})")
except Exception as e:
    st.error(f"❌ Failed to fetch files: {e}")
