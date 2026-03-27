import streamlit as st

st.set_page_config(
    page_title="My Business Portal",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("📊 My Business Portal")

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.metric("Active Users", "128", "+12%")

with col2:
    st.metric("Revenue (MTD)", "$1.2M", "+8.3%")

with col3:
    st.metric("Open Tickets", "23", "-5")

st.divider()

st.subheader("Quick Actions")
st.info("Replace with real business logic and Snowflake queries")
