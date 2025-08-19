import streamlit as st
import os

# Get environment variables
env = os.getenv("APP_ENV", "dev").lower()  # default "dev"
api_key = os.getenv("APP_KEY", "")

# Default background
bg_color = "white"
page_title = "Unknown Environment"

if env == "dev":
    page_title = "Dev Environment"
    bg_color = "lightgreen"
    st.title("🚧 Development Environment")
    st.success("✅ Connected to Dev environment")

elif env == "qa":
    page_title = "QA Environment"
    bg_color = "lightyellow"
    st.title("🧪 QA Environment")
    st.warning("✅ Connected to QA environment")

elif env == "prod":
    page_title = "Production Environment"
    bg_color = "lightcoral"
    st.title("🚀 Production Environment")
    st.error("✅ Connected to Prod environment")

else:
    st.title("❓ Unknown Environment")

# Set page title
st.set_page_config(page_title=page_title)

# Apply background color using CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Secret key check (do not print actual key)
if not api_key:
    st.error("❌ No API key found (check secrets configuration).")
else:
    st.info(f"🔒 Secret for {env.upper()} environment is configured properly.")
    st.write(f"API key length: {len(api_key)} characters")  # safe debug
