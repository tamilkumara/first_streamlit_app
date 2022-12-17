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


#New Section to display fruityvice api response
st.header("Fruityvice Fruit Advice!")

#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    st.text(back_from_function) # change to text
except URLError as e:
  st.error()

#---------

#my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_cur.execute("select * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#st.header("The fruit load list contains:")
#st.text(my_data_rows)
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")
#-------------
st.header ("The fruit load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()

# Add a button to load the fruit
if st.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    st.text(my_data_rows)  # change to text

    
st.stop()
#---------
#st.header("What fruit would you like to add ?")
add_my_fruit = st.text_input('What fruit would you like to add?','Banana')
st.write('Thanks for adding ', add_my_fruit)

userinput_response = requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit)
st.text(userinput_response.json())

# normalize ? 
userinput_response_normalized = pd.json_normalize(userinput_response.json())
st.text(userinput_response_normalized)
