import streamlit as st
import mysql.connector

st.title("Motorqe Car Database Interface")
st.subheader("Welcome to the Motorqe Car Database Interface")

# Creating connection object
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpassed",
    auth_plugin='mysql_native_password'
)

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE motorqe")

cursor.execute("SHOW DATABASES")

for x in cursor:
    print(x)
