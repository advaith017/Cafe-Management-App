import pandas as pd
import streamlit as st
import mysql.connector 

mydb = mysql.connector.connect(
host="localhost", user="root", password="root", database="cafe")

c = mydb.cursor()

def query():
    try:
        u_input=st.text_input("Enter the Query:")
        c.execute(str(u_input))
        #mydb.commit()
        data=c.fetchall()
        for i in data:
            st.write(i)
    except:
        st.write('No query entered')

