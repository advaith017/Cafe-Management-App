import pandas as pd
import streamlit as st
from database import view_all_orders, view_only_order_ids, delete_data


def delete():
    
    result = view_all_orders(0)
    #st.write(result)
    df = pd.DataFrame(result, columns=['item_no', 'order_id', 'product_id','qty','price','amount'])
  
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_orders = [i[0] for i in view_only_order_ids()]
    selected_order = st.selectbox("Order to Delete", list_of_orders)
    st.warning("Do you want to delete ::{}".format(selected_order))
    if st.button("Delete order"):
        delete_data(selected_order)
        st.success("Order has been deleted successfully")
    new_result = view_all_orders(0)
    df2 = pd.DataFrame(new_result, columns=['item_no', 'order_id', 'product_id','qty','price','amount'])
    with st.expander("Updated data"):
        st.dataframe(df2)