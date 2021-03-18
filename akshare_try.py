import akshare as ak
import streamlit as st

df = ak.stock_zh_a_daily(symbol="sz000002", start_date="20101103", end_date="20210318", adjust="qfq")
st.write(df)