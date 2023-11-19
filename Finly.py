import streamlit as st
st.set_page_config(
    page_title="Finly",
    page_icon="💸",
    layout="centered",
    initial_sidebar_state="expanded"
)
st.title("Finly")
st.subheader("Making investing an ease by turning sophisticated financial data into familiar, actionable insights")
st.image("images/front-page.webp")
st.divider()
st.header("About")
st.markdown("""
There are currently two main features in Finly:
1. 🔍 **INVESTING CHEAT SHEET:** A handbook containing definitions of main statistics and “rule-of-thumb” or main indicators and/or interesting information about major industries
2. 📕 **WATCHLIST:** A detailed outlook of the company's situation over observed years

👈  *Please use the side bar for navigation* 
""")
st.divider()
st.caption("Happy investing 😉😉")



