import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Investing Tips",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)
# st-emotion-cache-5rimss
st.title("💡 INVESTING TIPS")
st.markdown(
    """
    <style>
    .st-emotion-cache-5rimss {
        font-family: "Consolas";
        margin-top: 0rem;
        margin-bottom: 0.25rem;
        color: rgb(49,51,63);
        background-color: rgb(248, 249, 251);
        border-radius:0.5rem;
        padding-top: 0.5rem;
        padding-left: 1rem;
        padding-right: 1rem;
        padding-bottom: 0.5rem;
    }
    
    .st-emotion-cache-nahz7x {
        font-family: "Source Code Pro";
        margin-top: 0rem;
        margin-bottom: 0.25rem;
        background-color: rgb(26,28,36);
        border-radius:0.5rem;
        padding-top: 0.5rem;
        padding-left: 1rem;
        padding-right: 1rem;
        padding-bottom: 0.5rem;
    }
     .st-emotion-cache-nahz7x e1nzilvr5 {
        font-family: "Source Code Pro";
        margin-top: 0rem;
        margin-bottom: 0.25rem;
        background-color: rgb(0,0,0);
        border-radius:0.5rem;
        padding-top: 0.5rem;
        padding-left: 1rem;
        padding-right: 1rem;
        padding-bottom: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True
)
investing_df = pd.read_csv("data/investing_tips.csv")
industry_focused_tips = investing_df[investing_df['category'] == "Industry-focused"]['tip'].to_list()
investing_rules = investing_df[investing_df['category'] == "Investing Rules"]['tip'].to_list()
fun_stuff = investing_df[investing_df['category'] == "Fun stuff"]['tip'].to_list()

col_1, col_2, col_3 = st.columns(3)
with col_1:
    st.text("Industry-focused")
    for tip in industry_focused_tips:
        st.markdown(tip)

with col_2:
    st.text("Investing Rules")
    for tip in investing_rules:
        st.markdown(tip)

with col_3:
    st.text("Fun stuff")
    for tip in fun_stuff:
        st.markdown(tip)
