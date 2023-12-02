import streamlit as st

st.set_page_config(
    page_title="Investing Tips",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("💡 INVESTING TIPS")
st.divider()
col_1, col_2, col_3 = st.columns(3)
with col_1:
    st.text("Industry-focused")
    st.code("""
    Aircraft sector has low liquidity
    """)
    st.code("""
    Cash flow rate is high (~20%) among
    energy sectors due to
    """)
    st.code("""
    Tech companies usually come with
    huge investment
    """)

with col_2:
    st.text("Investing Rules")
    st.code("""
        Diversify your portfolio
        """)
    st.code("""
        Do thorough research and avoid timing
        the market
        """)
    st.code("""
    Set long-term goals because investing
    is a long-term endeavor
    """)
    st.code("""
    Invest based on risk tolerance:
    understand your comfort level
    with risk and align investments
    accordingly
    """)
    st.code("""
    Consider costs and fees because high
    fees can eat into your returns over
    time.
    """)

with col_3:
    st.text("Fun stuff")
    st.code("""
    print("Random coding stuff")
    print("cause coding is fun, rite?")
    """)
    st.code("""
    answer = input("How you doin?")
    if answer == ":smile:":
        print(":wink:")
    else:
        print("run away")
    """)
    st.code("""
    print("Hello, World!")
    """)
    st.code("""
    # Do you remember single-line comments?
    '''
    How about ...
                    multi-line ...
                                comments?
    '''
    """)
