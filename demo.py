import streamlit as st
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load credentials
service_account_info = json.loads(st.secrets["GOOGLE_SERVICE_ACCOUNT"])
creds = service_account.Credentials.from_service_account_info(service_account_info)

# Connect to Google Drive API
drive_service = build("drive", "v3", credentials=creds)

# Define Folder ID
FOLDER_ID = "1N36EC-B3dN7wx3wUYC732os1S6RzjwHh"  # Replace with actual Google Drive Folder ID

# Query Google Drive API
query = f"'{FOLDER_ID}' in parents and trashed=false"
try:
    results = drive_service.files().list(q=query, fields="files(id, name)").execute()
    st.write("*API Response:*", results)  # Print raw API response for debugging
    files = results.get("files", [])

    if files:
        st.write("### Google Drive Files:")
        for file in files:
            st.write(f"📄 {file['name']} (ID: {file['id']})")
    else:
        st.write("⚠️ No files found in Google Drive.")
except Exception as e:
    st.error(f"Error fetching files: {str(e)}")