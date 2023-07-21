import streamlit as st
from database import add_order

 
Classic =  0
Premium = 0 
Shakes = 0 
product_id=[0]*7

def create():
    item_no=1
    col1, col2,col3 = st.columns(3)
    order_id=0
    order_id = st.number_input("Order Number:",value=0)
    prices=[0,50,50,80,80,125,125]
    # def s():
        
    #     global product_id
    #     product_id[1]+=1
    # def b():
    #     global product_id
    #     product_id[2]+=1
    # def bel():
    #     global product_id
    #     product_id[3]+=1
    # def a():
    #     global product_id
    #     product_id[4]+=1
    # def o():
    #     global product_id
    #     product_id[5]+=1
    # def m():
    #     global product_id
    #     product_id[6]+=1    
    global product_id
    with col1:
       
        product_id[1] = st.number_input("Strawberry",value=0)
        product_id[2] = st.number_input("Butterscotch",value=0)
    with col2:
        product_id[3] = st.number_input("Belgian",value=0)
        product_id[4] = st.number_input("Pistachio",value=0)
    with col3:
        product_id[5] = st.number_input("Oreo",value=0)
        product_id[6] = st.number_input("Mississippi",value=0)

    if(st.button("Place Order")):
        for i in range(1,7):
            if(product_id[i]>0):
                add_order(item_no,order_id,i,product_id[i],prices[i])
                item_no+=1
        order_id+=1
        item_no=1
    
        
