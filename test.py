import streamlit as st

KEY = st.secrets.AzureApiKey.key
ENDPOINT = st.secrets.AzureApiKey.endpoint

# 以下の書き方でも可
KEY = st.secrets["AzureApiKey"]["key"]
