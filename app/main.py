import streamlit as st
import os

env = os.getenv("APP_ENV", "Dev")  # default Dev
api_key = os.getenv("APP_KEY", "no-key")  # injected from GitHub secrets

if env == "Dev":
    st.set_page_config(page_title="Dev Environment")
    st.markdown("<body style='background-color: lightgreen;'></body>", unsafe_allow_html=True)
    st.title("🚧 Development Environment")
    st.success("✅ Connected with API Key for Dev")

elif env == "QA":
    st.set_page_config(page_title="QA Environment")
    st.markdown("<body style='background-color: lightyellow;'></body>", unsafe_allow_html=True)
    st.title("🧪 QA Environment")
    st.warning("✅ Connected with API Key for QA")

elif env == "Prod":
    st.set_page_config(page_title="Production Environment")
    st.markdown("<body style='background-color: lightcoral;'></body>", unsafe_allow_html=True)
    st.title("🚀 Production Environment")
    st.error("✅ Connected with API Key for Prod")

else:
    st.title("❓ Unknown Environment")

# Never print the actual API key, just confirm presence
if api_key == "no-key":
    st.error("❌ No API key found (check secrets configuration).")
else:
    st.info(f"🔒 Secret for {env} environment is configured properly.")
