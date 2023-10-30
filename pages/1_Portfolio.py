import streamlit as st

st.header("Portfolio")
st.markdown("Track personal portfolio, a quick overview of watchlist companies overall financial health")

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Investment", value="150 M", delta="-50 M")

with col2:
    st.metric(label="Cash", value="225 M", delta="25 M")
