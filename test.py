import streamlit as st
import requests
import os

# JDoodleのAPI情報（freeプラン）
JDoodle_Client_ID = st.secrets["client_id"]
JDoodle_Client_Secret = st.secrets["client_secret"]

# ファイルのアップロード
uploaded_file = st.file_uploader("Upload your Java file", type="java")

if uploaded_file:
    java_code = uploaded_file.read().decode("utf-8")
    
    # JDoodle APIにリクエストを送信
    api_url = "https://api.jdoodle.com/v1/execute"
    data = {
        "script": java_code,
        "language": "java",
        "versionIndex": "3",  # Javaバージョン（例: 3 = JDK 1.8.0_66）
        "clientId": JDoodle_Client_ID,
        "clientSecret": JDoodle_Client_Secret
    }

    response = requests.post(api_url, json=data)
    
    if response.status_code == 200:
        result = response.json()
        st.write("Output:")
        st.write(result.get("output", "No output"))
    else:
        st.write(f"Error: {response.status_code}")
