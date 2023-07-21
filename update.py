import datetime

import pandas as pd
import streamlit as st
from database import view_all_orders, view_only_order_ids, get_order, edit_order_data


def update():
    result = view_all_orders(0)
    item_names=['Strawberry','Butterscotch','Belgian Chocolate','Pistachio Almond Fudge','Oreo Milkshake','Mississippi Mud']
    # st.write(result)
    prices=[0,50,50,80,80,125,125]
    df = pd.DataFrame(result, columns=['item_no', 'order_id', 'product_id','qty','price','amount'])
    with st.expander("Current Orders"):
        st.dataframe(df)
    list_of_order = list(range(0,len(df.index)))
    selected_order = st.selectbox("order to Edit", list_of_order)
    selected_result = get_order(df.iloc[selected_order]['order_id'],df.iloc[selected_order]['product_id'])
    #st.write(selected_result)
    if selected_result:
        name = selected_result[0][0]
        prod_id = selected_result[0][1]
        price = selected_result[0][2]
        qty = selected_result[0][3]
       
        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_name = st.selectbox("Item Name:",item_names)
            new_qty = st.number_input("Quantity:",value=0)
        new_prod_id=item_names.index(new_name)+1
        if st.button("Update Items"):
            edit_order_data(new_prod_id,new_qty,prices[new_prod_id],prod_id)
            st.success("Successfully updated:: {} to ::{}".format(name, new_name))

    result2 = view_all_orders(0)
    df2 = pd.DataFrame(result2, columns=['item_no', 'order_id', 'product_id','qty','price','amount'])
    with st.expander("Updated data"):
        st.dataframe(df2)
