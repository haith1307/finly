import streamlit as st
import time
import streamlit as st
from common.finly_mongo import FinlyMongo
import pandas as pd

finly = FinlyMongo(is_atlas=True)

with st.sidebar:
    company = st.selectbox("Select company", finly.db['financial_data'].distinct('metadata.symbol'))

st.header(f"Watchlist - {company}")

option = st.selectbox('Select Financial year', ['2019', '2020', '2021', '2022'])
st.subheader("Financial Report Summary")
if option == "2019":
    st.markdown("In 2019, Tesla Inc., an electric vehicle and clean energy company, reported a total revenue of \$24.6 billion, representing a significant increase of 14% compared to the previous year. The company's automotive segment accounted for the majority of the revenue, generating \$24.4 billion, while its energy generation and storage segment contributed \$369 million. Despite the revenue growth, Tesla experienced a net loss of \$862 million in 2019, primarily due to high operating expenses and significant investments in research and development. The company's gross margin also faced pressure, declining from 20.9% in 2018 to 19.4% in 2019, primarily driven by pricing pressure and manufacturing inefficiencies. Despite the financial challenges, Tesla continued to focus on expanding its production capacity and investing in new models, setting the stage for future growth in the electric vehicle market.")
elif option == "2020":
    st.write("In 2020, Tesla Inc., a leading electric vehicle and renewable energy company, achieved a remarkable year of financial performance. The company reported total revenue of \$31.5 billion, representing an impressive growth of 45% compared to the previous year. Tesla's automotive segment contributed \$27.2 billion to the revenue, while its energy generation and storage segment generated \$1.97 billion. The company's net income also surged to \$721 million in 2020, marking its first full year of profitability. Tesla's gross margin improved to 21.3%, driven by higher vehicle deliveries, cost reductions, and increased regulatory credit sales. The successful financial results reflect Tesla's strong market position and growing demand for electric vehicles globally.")
elif option == "2021":
    st.write("I apologize for the inconvenience, but as an AI language model, my responses are based on pre-existing information up until September 2021. Therefore, I don't have access to specific financial data for Tesla in 2021. I recommend referring to Tesla's official investor relations webpage or their published financial reports for the most accurate and up-to-date information regarding their financial performance in 2021.")
elif option == "2022":
    st.write("Told you I only data since September 2021. 2022 is then obviously a no, why dont you understand??!?")

st.subheader("Metrics")

col1, col2, col3 = st.columns(3)

eps_lst = []
for eps in finly.db['financial_data'].find({"metadata.symbol": company, 'metadata.type': 'quarterlyBasicEPS'}, sort=[('date', -1)]):
    eps_lst.append(eps['data']['raw'])

net_income = []
for record in finly.db['financial_data'].find({"metadata.symbol": company, 'metadata.type': 'quarterlyNetIncome'}, sort=[('date', -1)]):
    net_income.append(record['data']['raw'])

total_revenue = []
for record in finly.db['financial_data'].find({"metadata.symbol": company, 'metadata.type': 'quarterlyTotalRevenue'}, sort=[('date', -1)]):
    total_revenue.append(record['data']['raw'])

total_expense = []
for record in finly.db['financial_data'].find({"metadata.symbol": company, 'metadata.type': 'quarterlyTotalExpenses'}, sort=[('date', -1)]):
    total_expense.append(record['data']['raw'])


with col1:
    st.metric(label="Net Income", value=f"$ {net_income[0]/10**9:.2f} B", delta=f"{(net_income[0] - net_income[2])/net_income[2] * 100 :.2f} %")
with col2:
    st.metric(label="Total Revenue", value=f"$ {total_revenue[0]/10**9:.2f} B", delta=f"{(total_revenue[0] - total_revenue[2])/total_revenue[2] * 100 :.2f} %")
with col3:
    st.metric(label="Total Expenses", value=f"$ {total_expense[0]/10**9:.2f} B", delta=f"{(total_expense[0] - total_expense[2])/total_expense[2] * 100 :.2f} %")

# with col1:
#     st.metric(label=" Basic EPS", value=eps_lst[0], delta=f"{(eps_lst[0] - eps_lst[2]) / eps_lst[2] * 100 :.2f} %")

st.subheader("Significant Numbers")
dates = []
data = []
for obj in finly.db['financial_data'].find({'metadata.symbol': company, 'metadata.type': 'quarterlyOperatingExpense'}):
    dates.append(obj['date'])
    data.append(obj['data']['raw'])
df = pd.DataFrame(data={'Date': dates, 'Operating Expense': data})
st.line_chart(df, x="Date", y="Operating Expense")



# if option == "2019":
#     with col1:
#         st.metric(label="Total income", value="$862 M")
#     with col2:
#         st.metric(label="Total revenue", value="$ 24.6 B")
#     with col3:
#         st.metric(label="Something here", value="$ 100 M")
# elif option == "2020":
#     with col1:
#         st.metric(label="Total income", value="$ 721 M", delta="-16.65 %")
#     with col2:
#         st.metric(label="Total revenue", value="$ 31.5 B", delta="28.05 %")
#     with col3:
#         st.metric(label="Something here", value="$ 225 M", delta="225.00 %")

