import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Cheat sheet",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="expanded"
)

df = pd.read_csv("data/dictionary.csv")
st.title("🔍 INVESTING DICTIONARY")
st.markdown("""A tailor-made dictionary for investing terminologies, categorised by the financial report sections: 
balance sheet, profit and loss statement and cash flow. An additional section is also added for interesting 
findings.""")
st.divider()

st.header("Balance Sheet")
balance_sheet_term = st.selectbox('Select terminology:', df[df['category'] == 'Balance Sheet']['term'])
st.info(df[df['term'] == balance_sheet_term]['definition'].to_list()[0])
st.divider()

st.header("Profit Loss Statement")
p_and_l_term = st.selectbox('Select terminology:', df[df['category'] == 'Profit Loss Statement']['term'])
st.info(df[df['term'] == p_and_l_term]['definition'].to_list()[0])
st.divider()

st.header("Cash Flow")
cash_flow_term = st.selectbox('Select terminology:', df[df['category'] == 'Cash Flow']['term'])
st.info(df[df['term'] == cash_flow_term]['definition'].to_list()[0])
st.divider()

st.header("Other")
other_term = st.selectbox('Select terminology:', df[df['category'] == 'Other']['term'])
st.info(df[df['term'] == other_term]['definition'].to_list()[0])
st.divider()



