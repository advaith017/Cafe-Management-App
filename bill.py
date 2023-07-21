import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_orders,add_bill


def bill():
    order_id=0
    order_id = st.number_input("Order Number:",value=0)
    result = view_all_orders(order_id)
    #st.write(result)
    df = pd.DataFrame(result, columns=['item_no', 'order_id', 'product_id','qty','price','amount'])

    with st.expander("View all Orders"):
        st.dataframe(df)
    Total = df['amount'].sum()
    st.write("Total Bill:")
    st.write(Total)
    Amt_rendered= float(st.text_input("Amount Paid",value=0))
    if(Amt_rendered<Total):
        st.warning("Full amount not paid!")
    else:
        st.write("Balance returned:")
        st.write(Amt_rendered-Total)
        add_bill(order_id,Total,Amt_rendered)