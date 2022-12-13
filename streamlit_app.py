import streamlit

streamlit.title('My parents New Health Diner')

streamlit.header('Breakfast Favourites')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some Fruits",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show1 = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show1)

streamlit.header('Fruitvise Fruit Advise!')

import requests
fruityvise_response = requests.get("https://fruityvise.com/api.fruit/" + "kiwi")
streamlit.text(fruityvise_respose.json())
fruityvise_normalized = pandas.json_normalize(fruityvise_response.json())
streamlit.dataframe(fruityvise_normalized)
