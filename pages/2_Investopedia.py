import streamlit as st

st.header("Investopedia")

st.subheader("Liquidity")
st.markdown("**1. Current ratio:**")

col_1, col_2 = st.columns(2)
with col_1:
    st.markdown("""A liquidity ratio that measures a company's ability to pay short-term obligations or those due within one year. It 
 tells investors and analysts how a company can maximize the current assets on its balance sheet to satisfy current debt
 and other payables
            """)
with col_2:
    st.latex(r''' {CurrentRatio} = {Current Asset}/{Current Liability} ''')

st.markdown("**2. Quick ratio:**")
col_1, col_2 = st.columns(2)
with col_1:
    st.markdown("""The quick ratio is an indicator of a company’s short-term liquidity position and measures a company’s
     ability to meet its short-term obligations with its most liquid assets.""")
with col_2:
    st.latex(r''' {QuickRatio} = ({Cash} + {Short-termInvestments} + {AccountsReceivables})/{CurrentLiability}''')

