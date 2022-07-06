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
        'Price', ['Select', '10-15 L', '15-20 L', '20-25 L', '25-30 L', '30-50 L', '50-70 L', '70-99 L', '01-1.5 Cr', '1.5-3 Cr', '3-4 Cr'])
with col12:
    cartype_option = st.selectbox('Car Type', [
        'Select', 'Hatchback', 'Sedan', 'SUV', 'Sports', 'MPV'])
with col13:
    fueltype_option = st.selectbox('Fuel Type', [
        'Select', 'Petrol', 'Diesel', 'Electric', 'Hybrid'])
with col14:
    seats_option = st.selectbox('Number of Seats', [
        'Select', '2', '4', '5', '7'])

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
    "CREATE TABLE IF NOT EXISTS car_details(company VARCHAR(100), car_type VARCHAR(50), fuel VARCHAR(255), seats INT(20), price INT(20))")


st.markdown("<h3 font-size: 10px; color: orange;'>Available Options</h3>",
            unsafe_allow_html=True)

if (price_option == '10-15 L') and (cartype_option == 'Hatchback') and (fueltype_option == 'Petrol') and (seats_option == '5'):
    cursor.execute(
        "SELECT * FROM car_details WHERE car_type = 'Hatchback' AND fuel = 'Petrol' AND seats = 5 AND price BETWEEN 1000000 AND 1500000")
    myresult = pd.DataFrame(cursor.fetchall())
    st.write(myresult)
elif (price_option == '10-15 L') and (cartype_option == 'Hatchback') and (fueltype_option == 'Diesel') and (seats_option == '5'):
    cursor.execute(
        "SELECT * FROM car_details WHERE car_type = 'Hatchback' AND fuel = 'Diesel' AND seats = 5 AND price BETWEEN 1000000 AND 1500000")
    myresult = pd.DataFrame(cursor.fetchall())
    st.write(myresult)
elif (price_option == '10-15 L') and (cartype_option == 'SUV') and (fueltype_option == 'Petrol') and (seats_option == '5'):
    cursor.execute(
        "SELECT * FROM car_details WHERE car_type = 'SUV' AND fuel = 'Petrol' AND seats = 5 AND price BETWEEN 1000000 AND 1500000")
    myresult = pd.DataFrame(cursor.fetchall())
    st.write(myresult)
elif (price_option == '10-15 L') and (cartype_option == 'SUV') and (fueltype_option == 'Diesel') and (seats_option == '5'):
    cursor.execute(
        "SELECT * FROM car_details WHERE car_type = 'SUV' AND fuel = 'Diesel' AND seats = 5 AND price BETWEEN 1000000 AND 1500000")
    myresult = pd.DataFrame(cursor.fetchall())
    st.write(myresult)
elif (price_option == '15-20 L') and (cartype_option == 'SUV') and (fueltype_option == 'Diesel') and (seats_option == '5'):
    cursor.execute(
        "SELECT * FROM car_details WHERE car_type = 'SUV' AND fuel = 'Diesel' AND seats = 5 AND price BETWEEN 1500000 AND 2000000")
    myresult = pd.DataFrame(cursor.fetchall())
    st.write(myresult)
elif (price_option == '20-25 L') and (cartype_option == 'SUV') and (fueltype_option == 'Diesel') and (seats_option == '5'):
    cursor.execute(
        "SELECT * FROM car_details WHERE car_type = 'SUV' AND fuel = 'Diesel' AND seats = 5 AND price BETWEEN 2000000 AND 2500000")
    myresult = pd.DataFrame(cursor.fetchall())
    st.write(myresult)
elif (price_option == '25-30 L') and (cartype_option == 'SUV') and (fueltype_option == 'Diesel') and (seats_option == '5'):
    cursor.execute(
        "SELECT * FROM car_details WHERE car_type = 'SUV' AND fuel = 'Diesel' AND seats = 5 AND price BETWEEN 2500000 AND 3000000")
    myresult = pd.DataFrame(cursor.fetchall())
    st.write(myresult)
elif (price_option == '30-50 L') and (cartype_option == 'SUV') and (fueltype_option == 'Diesel') and (seats_option == '5'):
    cursor.execute(
        "SELECT * FROM car_details WHERE car_type = 'SUV' AND fuel = 'Diesel' AND seats = 5 AND price BETWEEN 3000000 AND 5000000")
    myresult = pd.DataFrame(cursor.fetchall())
    st.write(myresult)
elif (price_option == '50-70 L') and (cartype_option == 'SUV') and (fueltype_option == 'Diesel') and (seats_option == '5'):
    cursor.execute(
        "SELECT * FROM car_details WHERE car_type = 'SUV' AND fuel = 'Diesel' AND seats = 5 AND price BETWEEN 5000000 AND 7000000")
    myresult = pd.DataFrame(cursor.fetchall())
    st.write(myresult)
elif (price_option == '70-99 L') and (cartype_option == 'SUV') and (fueltype_option == 'Diesel') and (seats_option == '5'):
    cursor.execute(
        "SELECT * FROM car_details WHERE car_type = 'SUV' AND fuel = 'Diesel' AND seats = 5 AND price BETWEEN 7000000 AND 9900000")
    myresult = pd.DataFrame(cursor.fetchall())
    st.write(myresult)
elif (price_option == '3-4 Cr') and (cartype_option == 'Sports') and (fueltype_option == 'Petrol') and (seats_option == '2'):
    cursor.execute(
        "SELECT * FROM car_details WHERE car_type = 'Sports' AND fuel = 'Petrol' AND seats = 2 AND price BETWEEN 30000000 AND 40000000")
    myresult = pd.DataFrame(cursor.fetchall())
    st.write(myresult)
elif (price_option == '25-30 L') and (cartype_option == 'SUV') and (fueltype_option == 'Electric') and (seats_option == '5'):
    cursor.execute(
        "SELECT * FROM car_details WHERE car_type = 'SUV' AND fuel = 'Electric' AND seats = 5 AND price BETWEEN 2500000 AND 3000000")
    myresult = pd.DataFrame(cursor.fetchall())
    st.write(myresult)
elif (price_option == '20-25 L') and (cartype_option == 'SUV') and (fueltype_option == 'Electric') and (seats_option == '5'):
    cursor.execute(
        "SELECT * FROM car_details WHERE car_type = 'SUV' AND fuel = 'Electric' AND seats = 5 AND price BETWEEN 2000000 AND 2500000")
    myresult = pd.DataFrame(cursor.fetchall())
    st.write(myresult)
elif (price_option == '30-35 L') and (cartype_option == 'SUV') and (fueltype_option == 'Electric') and (seats_option == '5'):
    cursor.execute(
        "SELECT * FROM car_details WHERE car_type = 'SUV' AND fuel = 'Electric' AND seats = 5 AND price BETWEEN 3000000 AND 3500000")
    myresult = pd.DataFrame(cursor.fetchall())
    st.write(myresult)
elif (price_option == '15-20 L') and (cartype_option == 'SUV') and (fueltype_option == 'Diesel') and (seats_option == '7'):
    cursor.execute(
        "SELECT * FROM car_details WHERE car_type = 'SUV' AND fuel = 'Diesel' AND seats = 7 AND price BETWEEN 1500000 AND 2000000")
    myresult = pd.DataFrame(cursor.fetchall())
    st.write(myresult)
elif (price_option == '15-20 L') and (cartype_option == 'SUV') and (fueltype_option == 'Electric') and (seats_option == '5'):
    cursor.execute(
        "SELECT * FROM car_details WHERE car_type = 'SUV' AND fuel = 'Electric' AND seats = 5 AND price BETWEEN 1500000 AND 2000000")
    myresult = pd.DataFrame(cursor.fetchall())
    st.write(myresult)

for x in cursor:
    print(x)
