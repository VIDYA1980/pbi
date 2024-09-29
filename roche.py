import streamlit as st

# Embed Power BI dashboard using Streamlit's iframe method
st.title("Power BI Dashboard")

# Streamlit provides st.components.v1.iframe for embedding an iframe
st.components.v1.iframe(src="https://app.powerbi.com/reportEmbed?reportId=b6ab9932-d4bf-4f70-8848-9cf78c225aaa&autoAuth=true&ctid=d4963ce2-af94-4122-95a9-644e8b01624d", width=1000, height=600)
