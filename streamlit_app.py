import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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

#st.header("Fruityvice Fruit Advice!")

#New Section to display fruityvice api response
streamlit.header ('Fruitvvice Fruit Advice! ")
try:
  fruit_choice = st.text input ('What fruit would you like information about?')
  if not fruit choice:
    st.error("Please select a fruit to get information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    st.text(fruityvice_normalized) # change to text
except URLError as e:
st.error()

#---------
#fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
#st.write('The user entered ', fruit_choice)


#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#st.text(fruityvice_response.json())

# normalize ? 
#fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

#st.text(fruityvice_normalized)

# code for connecting snowflake into streamlit

#---------------
st.stop()


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
st.header("The fruit load list contains:")
st.text(my_data_rows)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
               
#---------
#st.header("What fruit would you like to add ?")
add_my_fruit = st.text_input('What fruit would you like to add?','Banana')
st.write('Thanks for adding ', add_my_fruit)

userinput_response = requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit)
st.text(userinput_response.json())

# normalize ? 
userinput_response_normalized = pd.json_normalize(userinput_response.json())
st.text(userinput_response_normalized)
