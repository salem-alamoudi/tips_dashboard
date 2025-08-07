# importing libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# setting page config
st.set_page_config(
    page_title="Tip Dashboard",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# loading the dataset
df = pd.read_csv('tips.csv')

# Sidebar
st.sidebar.header('Tips Dashboard')
st.sidebar.image('tips1.jpeg')
st.sidebar.write("This dashboard is using Tips dataset from seaborn for educational purposes.")
st.sidebar.write(" ")
st.sidebar.write("Filter your data:")

cat_filter = st.sidebar.selectbox("Categorical Filtering", [None, 'sex', 'smoker', 'day', 'time'])
num_filter = st.sidebar.selectbox("Numerical Filtering", [None, 'total_bill', 'tip'])
row_filter = st.sidebar.selectbox("Row Filtering", [None, 'sex', 'smoker', 'day', 'time'])
col_filter = st.sidebar.selectbox("Column Filtering", [None, 'total_bill', 'tip'])

st.sidebar.write("")
st.sidebar.markdown("Made with ❤️ by [Eng. Salem Alamoudi]")

# Body
st.subheader("Total Bill vs Tips")

# row a
a1, a2, a3, a4 = st.columns(4)
a1.metric("Max. Total Bill", df['total_bill'].max())
a2.metric("Max. Tip", df['tip'].max())
a3.metric("Min. Total Bill", df['total_bill'].min())
a4.metric("Min. Tip", df['tip'].min())

# row b — scatter
kwargs = dict()
if cat_filter: kwargs['color'] = cat_filter
if num_filter: kwargs['size'] = num_filter
if col_filter: kwargs['facet_col'] = col_filter
if row_filter: kwargs['facet_row'] = row_filter

fig = px.scatter(
    data_frame=df,
    x='total_bill',
    y='tip',
    **kwargs
)
st.plotly_chart(fig, use_container_width=True)

# row c — other charts
c1, c2, c3 = st.columns((4, 3, 3))
with c1:
    st.text("Sex vs Total Bills")
    fig = px.bar(data_frame=df, x='sex', y='total_bill')
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.text("Smoker/Non-smoker vs Tips")
    fig = px.pie(data_frame=df, names='smoker', values='tip')
    st.plotly_chart(fig, use_container_width=True)

with c3:
    st.text("Day vs Tips")
    fig = px.pie(data_frame=df, names='day', values='tip', hole=0.3)
    st.plotly_chart(fig, use_container_width=True)
