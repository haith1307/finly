import streamlit as st

st.set_page_config(
    page_title="Finly",
    page_icon="💸",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Finly")
st.subheader("Making investing an ease by turning sophisticated financial data into familiar, actionable insights")
st.divider()
st.header("About")

st.markdown("""
There are currently two main features in Finly:
1. 🔍 **INVESTING DICTIONARY:** A handbook containing definitions of main statistics and indicators
2. 💡 **INVESTING TIPS**: A note of interesting notes, information about major industries along our discovery path
3. 📕 **WATCHLIST:** A detailed outlook of the company's situation over observed years

👈  *Please use the side bar for navigation* 
""")

st.divider()
st.caption("Happy investing 😉😉")
