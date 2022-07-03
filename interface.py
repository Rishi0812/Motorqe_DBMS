import streamlit as st
import mysql.connector
from PIL import Image
import pandas as pd

col1, col2, col3 = st.columns(3)
image = Image.open('Motorqe-LOGO.jpeg')

with col1:
    st.image(image, width=300)
with col2:
    st.write(' ')
with col3:
    st.image(image, width=300)


st.markdown("<h1 style='text-align: center; font-size: 40px; color: black;'>Motorqe Car Database Interface</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-size: 20px; color: orange;'>Welcome to the Motorqe Car Database Interface</h2>", unsafe_allow_html=True)

col11, col12, col13, col14 = st.columns(4)

with col11:
    price_option = st.selectbox(
        'Price', ['Select', 'Audi', 'BMW', 'Mercedes', 'Volkswagen'])
with col12:
    cartype_option = st.selectbox('Car Type', [
        'Audi', 'BMW', 'Mercedes', 'Volkswagen'])
with col13:
    fueltype_option = st.selectbox('Fuel Type', [
        'Audi', 'BMW', 'Mercedes', 'Volkswagen'])
with col14:
    seats_option = st.selectbox('Number of Seats', [
        'Audi', 'BMW', 'Mercedes', 'Volkswagen'])

st.write('Price:', price_option)

# Creating connection object
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpassed",
    auth_plugin='mysql_native_password'
)

cursor = mydb.cursor()

# cursor.execute("CREATE DATABASE motorqe")
cursor.execute("USE motorqe")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS car_details(company VARCHAR(100), type VARCHAR(50), fuel VARCHAR(255), seats INT(20), price INT(20))")

cursor.execute(
    "INSERT INTO car_details(company, type, fuel, seats, price) VALUES(%s, %s, %s, %s, %s)", ('Mercedes Benz', 'SUV', 'Diesel', 5, 2000000))

if cartype_option == 'Mercedes':
    cursor.execute(
        "SELECT * FROM car_details WHERE company = 'Mercedes Benz'")
    myresult = pd.DataFrame(cursor.fetchall())
    st.write(myresult)

for x in cursor:
    print(x)
