import streamlit as st
import pandas as pd

st.title('My parents New Health Diner')
st.header('Breakfast Favourites')

st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avacado Toast - For Muthu')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = st.multiselect("Pick some Fruits",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

st.text(fruits_to_show)

st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
st.text(fruityvice_response.json())

# normalize ? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

st.text(fruityvice_normalized)

# code for connecting snowflake into streamlit

import snowflake.connector
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
st.text("The fruit load list contains:")
st.text(my_data_rows)

#---------
st.header("What fruit would you like to add ?")
add_my_fruit = st.text_input('What fruit would you like information about?','Banana')
st.write('Thanks for adding ', add_my_fruit)

import requests
userinput_response = requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit)
st.text(userinput_response.json())

# normalize ? 
userinput_response_normalized = pd.json_normalize(userinput_response.json())
st.text(userinput_response_normalized)
