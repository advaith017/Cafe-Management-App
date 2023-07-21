# Importing pakages
import streamlit as st
import mysql.connector

from create import create

from bill import bill
from delete import delete
# from read import read
from update import update
from query import query

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="password"
# )
# c = mydb.cursor()
#
# c.execute("CREATE DATABASE ebike")
order_id=0

def main():
    st.title("Cafe Billing App: ")
    menu = ["Add", "Bill","Edit", "Remove","Query Window"]
    choice = st.sidebar.selectbox("Menu", menu)

    
    if choice == "Add":
        st.subheader("Take order here:")
        global order_id
        order_id+=1
        create()
        


    elif choice == "Bill":
        st.subheader("View all orders")
        bill()

    elif choice == "Edit":
        st.subheader("Update created tasks")
        update()

    elif choice == "Remove":
        st.subheader("Delete created tasks")
        delete()

    elif choice == "Query Window":
        st.subheader("Entery SQL Query")
        query()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()
